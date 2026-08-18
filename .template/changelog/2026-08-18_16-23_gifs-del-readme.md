# Cuatro GIF para el README: el argumento, el artefacto y la prueba

**Fecha:** 2026-08-18 16:23
**Tipo:** Documentación
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

El README explicaba el protocolo entero en prosa. Ahora lo enseña, con cuatro GIF que hablan tres
idiomas distintos a propósito:

- **`comparativa.gif`** (cabecera) — dos carriles de tarjetas: sin plantilla, cada sesión empieza
  de cero y la flecha vuelve al principio; con plantilla, la línea llega recta a un check verde.
  Es un **argumento**.
- **`flujo.gif`** ("¿Cómo funciona el protocolo?") — un árbol de archivos creciendo fase a fase:
  los `docs/` marcados `vacío` que se llenan, `.template/` tachándose, y la pastilla de la ficha
  pasando de Acordada a En construcción y a Verificada. Es un **artefacto**: no explica el
  producto, es el producto.
- **`cobertura.gif`** (sección nueva "La regla que lo sostiene") — el script pasando con la ficha
  en construcción, fallando al marcarla Verificada sin el test, y volviendo a pasar cuando existe.
  Es una **prueba**.
- **`excepcion.gif`** (`docs/features/README.md`) — columna vacía y "no aplica" rechazados; con la
  razón concreta, verde.

El diagrama Mermaid del ciclo se elimina: contaba lo mismo que `flujo.gif` con menos detalle, y
tener los dos era repetirse.

Todo vive en `.template/assets/`, junto con los tres generadores. Al inicializar un proyecto la
carpeta se borra y el README se reescribe, así que imágenes y referencias desaparecen juntas.

## Qué se modificó

- `.template/assets/` — nueva: cuatro GIF, tres generadores (`gen-comparativa.py`, `gen-flujo.py`,
  `gen-terminal.py`) y un `README.md` con cómo regenerarlos
- `README.md` — GIF de cabecera bajo la llamada a la acción; `flujo.gif` sustituye al diagrama
  Mermaid; nueva sección "La regla que lo sostiene" con `cobertura.gif`
- `docs/features/README.md` — `excepcion.gif` tras la regla de la tercera columna
- `.template/README.md` — documenta la carpeta `assets/`
- `CLAUDE.md` y `.claude/commands/init-proyecto.md` — al borrar `.template/` hay que quitar las
  referencias que apuntan a sus imágenes; se nombra la de `docs/features/README.md`

## Por qué

Un repositorio plantilla tiene la particularidad de que su página de inicio es el producto: lo
primero que hace alguien es mirar el README y decidir en quince segundos si esto le sirve. Diez
puntos numerados no ganan esa decisión.

Los tres registros son deliberados y no intercambiables. El diagrama de carriles es una afirmación
que nadie puede verificar —como toda comparativa de antes y después, es una caricatura amable del
problema—. El árbol que crece es concreto pero sigue siendo un dibujo. Los GIF de terminal son lo
único del README que un escéptico puede reproducir en su máquina, y por eso se quedan aunque sean
los más feos: son la parte que demuestra en vez de prometer.

## Verificado

- Los GIF de terminal se componen de la salida literal de `verificar-cobertura.mjs` ejecutado
  sobre un proyecto de prueba (un catálogo de vinilos, el ejemplo del propio `CLAUDE.md`). Ni una
  línea de ese texto está escrita a mano.
- Peso total de los cuatro: 675 KB. El mayor, `flujo.gif`, 244 KB.
- `node scripts/verificar-cobertura.mjs` sigue saliendo limpio.
