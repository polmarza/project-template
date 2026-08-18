# README con cabecera, diagrama y tabla de comandos; licencia con titular real

**Fecha:** 2026-08-18 15:09
**Tipo:** Documentación
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

**Licencia.** `LICENSE` llevaba desde el primer commit con los placeholders `[YEAR]` y
`[AUTHOR]` sin rellenar, lo que dejaba la plantilla en un limbo: dice MIT pero sin titular, que
es como no decir nada. Ahora es `Copyright (c) 2026 Pol Marzà` — 2026 por el primer commit del
repositorio, del 7 de mayo.

Eso obligaba a tocar tres sitios más: el checklist de inicialización de `CLAUDE.md`, el comando
`/init-proyecto` y la tabla de adaptación del README pedían "sustituye `[YEAR]` y `[AUTHOR]`",
y esos marcadores ya no existen. Ahora dicen lo que toca: la plantilla se distribuye con el
copyright de su autor y cada proyecto pone el suyo al inicializar.

**README.** Cabecera centrada con cuatro badges (estado del workflow de cobertura, licencia,
pnpm v11 y agnosticismo de stack) y un enlace directo a *Usar esta plantilla*, que hasta ahora
solo se mencionaba de pasada en el paso 1.

Añadido un diagrama Mermaid del ciclo completo —requisito con criterio → ficha Acordada → En
construcción → tests sobre el código real → Verificada → PR con la cobertura verificada en CI—
como resumen visual antes de los diez puntos del protocolo, que se leían como un muro.

Y una tabla de comandos: los seis slash commands estaban enterrados dentro de un bullet de la
sección "¿Qué hay dentro?", donde no los encontraba nadie.

## Qué se modificó

- `LICENSE` — titular y año reales
- `README.md` — cabecera con badges y llamada a la acción; diagrama Mermaid del ciclo de feature;
  nueva sección "Comandos"; fila de `LICENSE` en la tabla de adaptación reescrita; pie con el
  copyright
- `CLAUDE.md` — paso 3 del checklist de inicialización (copyright en vez de placeholders); aviso
  en el paso 1 de que los badges apuntan al repositorio de la plantilla y hay que quitarlos o
  repuntarlos
- `.claude/commands/init-proyecto.md` — mismo cambio en su paso 3

## Por qué

Lo de la licencia no era cosmético: un MIT sin titular no concede permisos a nadie con claridad,
y este repositorio es público y está pensado para que la gente lo copie.

Lo del README, en cambio, sí es presentación — pero de la clase que importa en un repositorio
plantilla, donde la página de inicio es el producto. Los badges elegidos son los cuatro que dicen
algo cierto y comprobable; no hay ninguno decorativo del tipo "PRs welcome" ni métricas de
paquetes que este repositorio no publica.

## Verificado

- Las cuatro URLs de badge devuelven `200` con `image/svg+xml`.
- El badge del workflow refleja el estado real del último run en `main`.
- `node scripts/verificar-cobertura.mjs` sigue saliendo limpio.
