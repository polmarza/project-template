# La regla de la tercera columna pasa a verificarse sola

**Fecha:** 2026-08-18 13:13
**Tipo:** Feature
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

La tabla de cobertura de `docs/features/` tenía una regla clara —ningún requisito sin su tercera
columna— pero era prosa: dependía de que quien rellenaba la tabla la cumpliera. Ahora hay un script
que la comprueba, y corre en CI.

**`scripts/verificar-cobertura.mjs`** lee `docs/prd.md` y todas las fichas de `docs/features/`, y
falla si encuentra:

- Una fila sin la columna "Se valida con" rellena.
- Una excepción `no verificable por interfaz:` sin razón, o con una razón de menos de 15
  caracteres ("no aplica" no cuela).
- Una tercera columna que no es ni ruta ni excepción ("pendiente", "TBD", un guion).
- Un identificador que no está declarado en `docs/prd.md`, o declarado dos veces allí.
- Un requisito listado en "Requisitos que cierra" que no tiene fila en la tabla.
- Una ficha sin `**Estado:**` válido o sin sección `## Cobertura`.
- **Un test declarado que no existe en disco**, cuando la ficha dice estar **Verificada**.

Ese último es el que justifica el script: es el fallo típico al delegar —declarar
`tests/registro.spec.ts` en la tabla y no escribirlo nunca— y es invisible leyendo el diff, porque
no aparece un archivo que no existe.

Node sin dependencias, solo módulos nativos. No hay nada que instalar y no toca `package.json`.

**`.github/workflows/cobertura.yml`** lo ejecuta en cada pull request y en cada push a `main`.

## Qué se modificó

- `scripts/verificar-cobertura.mjs` — nuevo
- `.github/workflows/cobertura.yml` — nuevo
- `CLAUDE.md` — comando en el paso "Cerrar" del ciclo de feature; nuevo apartado "La verificación
  de cobertura" con qué comprueba, qué no, y por qué corre en CI
- `docs/features/README.md` — la regla de la tercera columna ahora remite al script; aclarado que
  una fila puede declarar varios tests separados por comas
- `.claude/commands/doctor.md` — la comprobación de fichas pasa a ejecutar el script y reportar su
  salida; se mantiene a mano lo que exige criterio (tests existentes pero vacíos)
- `.claude/settings.json` — permitido `node scripts/*`
- `README.md` — `scripts/` en el contenido; paso 3 del protocolo; fila en la tabla de adaptación

## Por qué

Hasta ahora todo el protocolo era autodeclarado, y con un agente de por medio eso significa que
quien afirma haber cumplido y quien tenía que cumplir son el mismo. La regla de la tercera columna
era la más importante del ciclo de feature y también la más fácil de incumplir en silencio.

Corre en CI a propósito, no en un hook local ni solo cuando el agente se acuerda: una comprobación
que el comprobado puede saltarse no es una comprobación. Si falla en CI se arregla la causa; no se
toca el workflow.

**La decisión de diseño que sostiene todo esto** es que la existencia de los archivos solo se exige
en estado **Verificada**. Los tests se escriben después de implementar, así que una ficha en
construcción con el archivo aún sin crear es lo correcto, no un fallo. Un script que chillara ahí
daría rojos legítimos que habría que ignorar, y una verificación que se ignora por sistema es peor
que ninguna: enseña a ignorar los rojos.

Lo que comprueba es estructural, no semántico. Un test vacío pasa la verificación. Pero un archivo
vacío se ve en el diff del PR y uno inexistente no, así que el suelo sube: ya no basta con no
escribir el test.

## Verificado

Probado sobre una copia del repositorio con fichas de prueba:

- Plantilla sin rellenar y repositorio sin fichas → sale limpio, código 0. Era el caso crítico: si
  un clon recién hecho diera rojo, el workflow nacería desactivado.
- Ficha **Verificada** con test existente y una excepción bien justificada → 0 fallos.
- Ficha **En construcción** con el test todavía sin escribir → 0 fallos (no debe exigirlo).
- Ficha con los nueve modos de fallo mezclados → los nueve detectados, código 1.
