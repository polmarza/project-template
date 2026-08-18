#!/usr/bin/env node
/**
 * Verifica las tablas de cobertura de `docs/features/` contra los requisitos de `docs/prd.md`.
 *
 * Comprueba lo que se puede comprobar sin interpretar nada: que ninguna fila se quede sin
 * validación declarada, que los identificadores existan, y que los tests prometidos existan
 * de verdad cuando la ficha dice estar Verificada.
 *
 * Lo que NO comprueba: que el test valide lo que dice validar, ni que la razón de una excepción
 * sea honesta. Esto detecta la promesa incumplida, no el trabajo mal hecho.
 *
 * Uso:  node scripts/verificar-cobertura.mjs
 * Sale con código 1 si hay fallos. Los avisos no rompen la ejecución.
 */

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join, dirname, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const PRD = join(RAIZ, 'docs', 'prd.md');
const FICHAS = join(RAIZ, 'docs', 'features');

const ESTADOS = ['Acordada', 'En construcción', 'Verificada'];
const EXCEPCION = 'no verificable por interfaz:';
const RAZON_MINIMA = 15;

const fallos = [];
const avisos = [];

const fallo = (donde, mensaje) => fallos.push({ donde, mensaje });
const aviso = (donde, mensaje) => avisos.push({ donde, mensaje });

/** Los bloques comentados son plantilla, no contenido. */
const sinComentarios = (texto) => texto.replace(/<!--[\s\S]*?-->/g, '');
const sinBackticks = (texto) => texto.replace(/`/g, '').trim();

// ─── docs/prd.md ──────────────────────────────────────────────────────────────

function requisitosDelPrd() {
  if (!existsSync(PRD)) {
    aviso('docs/prd.md', 'No existe: no se pueden contrastar los identificadores de las fichas');
    return new Set();
  }

  const ids = new Set();
  const texto = sinComentarios(readFileSync(PRD, 'utf8'));

  // Solo cuentan las líneas de declaración: `- **[M-01] Título** — Dado…`.
  // Una mención del ID en otra parte del documento no declara nada.
  for (const linea of texto.split('\n')) {
    const m = linea.match(/^\s*-\s*\*\*\[([MSC]-\d+)\]/);
    if (!m) continue;
    if (ids.has(m[1])) fallo('docs/prd.md', `El identificador ${m[1]} está declarado dos veces`);
    ids.add(m[1]);
  }

  return ids;
}

// ─── docs/features/*.md ───────────────────────────────────────────────────────

function seccionCobertura(lineas) {
  const inicio = lineas.findIndex((l) => /^##\s+Cobertura\s*$/.test(l.trim()));
  if (inicio === -1) return null;
  const resto = lineas.slice(inicio + 1);
  const fin = resto.findIndex((l) => /^##\s/.test(l));
  return fin === -1 ? resto : resto.slice(0, fin);
}

function filasDeTabla(lineas) {
  return lineas
    .map((l) => l.trim())
    .filter((l) => l.startsWith('|'))
    .map((l) => l.replace(/^\|/, '').replace(/\|$/, '').split('|').map((c) => c.trim()))
    .filter((celdas) => !celdas.every((c) => /^:?-{3,}:?$/.test(c)))
    .filter((celdas) => !/^requisito$/i.test(celdas[0] ?? ''));
}

function leerFicha(nombre) {
  const rel = `docs/features/${nombre}`;
  const texto = sinComentarios(readFileSync(join(FICHAS, nombre), 'utf8'));
  const lineas = texto.split('\n');

  const mEstado = texto.match(/^\*\*Estado:\*\*\s*(.+)$/m);
  const estado = mEstado ? mEstado[1].trim() : null;

  const mReq = texto.match(/^\*\*Requisitos que cierra:\*\*\s*(.+)$/m);
  const declarados = mReq
    ? mReq[1].split(',').map((s) => sinBackticks(s)).filter((s) => /^[MSC]-\d+$/.test(s))
    : [];

  const seccion = seccionCobertura(lineas);
  return { rel, estado, declarados, filas: seccion ? filasDeTabla(seccion) : null };
}

function validarFicha(ficha, idsPrd) {
  const { rel, estado, declarados, filas } = ficha;

  if (!estado) {
    fallo(rel, 'Falta la línea `**Estado:**` en la cabecera');
  } else if (!ESTADOS.includes(estado)) {
    fallo(rel, `Estado "${estado}" no válido. Debe ser: ${ESTADOS.join(' · ')}`);
  }

  if (filas === null) {
    fallo(rel, 'No tiene sección `## Cobertura`');
    return;
  }
  if (filas.length === 0) {
    fallo(rel, 'La tabla de cobertura está vacía');
    return;
  }

  const verificada = estado === 'Verificada';
  const enTabla = new Set();

  for (const celdas of filas) {
    const id = sinBackticks(celdas[0] ?? '');
    const validacion = (celdas[2] ?? '').trim();

    if (!id) {
      fallo(rel, 'Hay una fila sin identificador de requisito');
      continue;
    }
    enTabla.add(id);

    if (idsPrd.size > 0 && !idsPrd.has(id)) {
      fallo(rel, `${id}: no está declarado en docs/prd.md`);
    }

    if (celdas.length < 3) {
      fallo(rel, `${id}: la fila no tiene las tres columnas`);
      continue;
    }

    // ── La regla de la tercera columna ──
    if (!validacion) {
      fallo(rel, `${id}: la columna "Se valida con" está vacía. Escribe la ruta del test o ` +
                 `"${EXCEPCION} <razón concreta>"`);
      continue;
    }

    if (validacion.toLowerCase().startsWith(EXCEPCION)) {
      const razon = validacion.slice(EXCEPCION.length).trim();
      if (razon.length < RAZON_MINIMA) {
        fallo(rel, `${id}: la excepción no explica nada ("${razon || 'sin texto'}"). ` +
                   `Escribe la razón concreta y cómo se comprueba entonces`);
      }
      continue;
    }

    const rutas = validacion.split(',').map(sinBackticks).filter(Boolean);
    const pareceRuta = rutas.every((r) => r.includes('/') || r.includes('.'));

    if (!pareceRuta) {
      fallo(rel, `${id}: "${validacion}" no es ni una ruta de test ni una excepción justificada`);
      continue;
    }

    // Las fichas pueden llegar en un pull request, así que las rutas son entrada no
    // confiable: se comprueba siempre que apunten dentro del repositorio, en cualquier
    // estado, y no solo al cerrar la ficha.
    const contenidas = [];
    for (const ruta of rutas) {
      const destino = resolve(RAIZ, ruta);
      if (destino !== RAIZ && !destino.startsWith(RAIZ + sep)) {
        fallo(rel, `${id}: la ruta ${ruta} apunta fuera del repositorio`);
        continue;
      }
      contenidas.push({ ruta, destino });
    }

    // La existencia solo se exige al cerrar: los tests se escriben después de implementar,
    // así que una ficha en construcción con el archivo aún sin crear es lo normal.
    if (!verificada) continue;

    for (const { ruta, destino } of contenidas) {
      if (!existsSync(destino)) {
        fallo(rel, `${id}: la ficha está Verificada pero ${ruta} no existe`);
      }
    }
  }

  for (const id of declarados) {
    if (!enTabla.has(id)) {
      fallo(rel, `${id} aparece en "Requisitos que cierra" pero no tiene fila en la tabla`);
    }
  }

  return enTabla;
}

// ─── Ejecución ────────────────────────────────────────────────────────────────

function main() {
  if (!existsSync(FICHAS)) {
    console.log('No existe docs/features/: nada que verificar.');
    return 0;
  }

  const nombres = readdirSync(FICHAS)
    .filter((n) => n.endsWith('.md') && n !== 'README.md')
    .sort();

  if (nombres.length === 0) {
    console.log('Sin fichas de feature todavía: nada que verificar.');
    return 0;
  }

  const idsPrd = requisitosDelPrd();
  const cubiertos = new Set();

  for (const nombre of nombres) {
    const ficha = leerFicha(nombre);
    const enTabla = validarFicha(ficha, idsPrd) ?? new Set();
    for (const id of enTabla) cubiertos.add(id);
  }

  for (const id of idsPrd) {
    if (!cubiertos.has(id)) {
      aviso('docs/prd.md', `${id} no aparece en ninguna ficha todavía`);
    }
  }

  // ── Informe ──
  console.log(`\nVerificación de cobertura — ${nombres.length} ficha(s)\n`);

  const porArchivo = new Map();
  for (const f of fallos) {
    if (!porArchivo.has(f.donde)) porArchivo.set(f.donde, []);
    porArchivo.get(f.donde).push(f.mensaje);
  }

  for (const [donde, mensajes] of porArchivo) {
    console.log(`  ${donde}`);
    for (const m of mensajes) console.log(`    FALLO  ${m}`);
    console.log('');
  }

  for (const a of avisos) {
    console.log(`  ATENCIÓN  ${a.mensaje}  (${a.donde})`);
  }
  if (avisos.length) console.log('');

  if (fallos.length === 0) {
    console.log(avisos.length
      ? `Sin fallos. ${avisos.length} aviso(s) que no bloquean.\n`
      : 'Todo en orden.\n');
    return 0;
  }

  console.log(`${fallos.length} fallo(s)${avisos.length ? `, ${avisos.length} aviso(s)` : ''}.\n`);
  return 1;
}

process.exit(main());
