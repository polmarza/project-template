---
name: init-proyecto
description: Convierte la plantilla en el repositorio del proyecto real, una sola vez —README, CLAUDE.md, LICENSE, .env.example, MCPs, docs/ que no aplican, changelog y borrado de .template/—. Úsala cuando los documentos de docs/ estén rellenos y la carpeta .template/ siga existiendo.
---

Convierte esta plantilla en el repositorio del proyecto real. Es un proceso de una sola vez.

## Antes de empezar

1. Lee todos los archivos de `docs/`.
2. Si están vacíos o incompletos, **no inicialices todavía**: primero complétalos con el usuario
   siguiendo el orden de `CLAUDE.md` (prd.md → business.md → design-system.md → architecture.md →
   data-model.md → roadmap.md → user-flows.md). No hacen falta los ocho: mira antes la tabla "Qué
   documentación necesita cada proyecto" de `CLAUDE.md` y pide solo los que apliquen al tamaño de
   este proyecto.
3. Si no existe `.template/`, el repo ya está inicializado. Dilo y no toques nada, salvo que el
   usuario pida rehacer algo concreto.

## Datos que necesitas

Pregunta solo lo que no puedas deducir de `docs/`:

- Nombre del proyecto y descripción de una línea
- Estado actual (En desarrollo / Beta / Producción)
- Autor y año para la licencia

## Qué hacer

Antes de tocar nada, abre `CLAUDE.md` con la herramienta de lectura. Cuando se carga solo al
empezar la sesión, Claude Code le quita los comentarios `<!-- ... -->`, y ahí es justo donde están
los placeholders y los ejemplos que vas a sustituir.

1. **`README.md`** — reescríbelo entero para el proyecto, a partir de lo que hay en `docs/`. Debe
   explicar el producto, no la plantilla. Estructura sugerida: nombre y descripción de una línea,
   qué problema resuelve, requisitos previos, variables de entorno (referencia a `.env.example`),
   instalación y desarrollo (`pnpm install`, `pnpm dev`), estructura de carpetas, cómo contribuir
   (referencia a `CLAUDE.md` y al protocolo) y estado del proyecto. Los badges de la cabecera
   apuntan al repositorio de la plantilla: quítalos o repóntalos al del proyecto.
2. **`CLAUDE.md`** — rellena nombre, descripción, estado, stack, estructura de carpetas,
   convenciones y "Qué NO hacer". El contenido real va fuera de los comentarios, o el agente no lo
   verá. Borra los comentarios que ya no apliquen, la sección "Inicialización del proyecto" y las
   referencias a `.template/` del arranque y del protocolo de cambios. **El "Protocolo de MCPs" se
   queda**: sigue aplicando cada vez que entre una integración nueva.
3. **`LICENSE`** — sustituye la línea de copyright de la plantilla por el año actual y el titular
   de este proyecto.
4. **`.env.example`** — deja solo las variables que el stack elegido necesita de verdad.
5. **MCPs** — pregunta qué servidores MCP quiere y con qué alcance, siguiendo el "Protocolo de
   MCPs" de `CLAUDE.md`. Si prefieres tratarlo aparte, lanza `/mcp-setup`.
6. **`docs/`** — borra los documentos que este proyecto no necesite según la tabla "Qué
   documentación necesita cada proyecto". Los que no aplican se borran, no se dejan vacíos: un
   archivo con solo comentarios hace que el arranque de cada sesión se pare a preguntar por él.
   `docs/features/` se queda vacía, solo con su `README.md`.
7. **`mejoras/backlog.md`** — borra el ejemplo comentado y déjalo listo para entradas reales.
8. **Borrados** — `.template/` entera (es el historial de la plantilla, no del proyecto) y esta
   misma skill, `.claude/skills/init-proyecto/`, que deja de tener sentido una vez hecha. Enseña
   antes la lista exacta de lo que va a desaparecer y espera confirmación. Después quita las
   referencias que queden a `.template/assets/` (hay una en `docs/features/README.md`) y a
   `/init-proyecto` (en `README.md` y `CLAUDE.md`).
9. **`changelog/`** — debe quedar sin entradas heredadas. Crea la primera entrada real del
   proyecto (tipo: Configuración) con `/changelog` y quita de `changelog/README.md` la referencia
   a la plantilla, o borra el archivo.
10. **Restos** — busca referencias sobrantes y corrige cada una que hable de la plantilla en lugar
    del proyecto:
    `grep -ril "plantilla\|template" . --exclude-dir=.git --exclude-dir=node_modules`
11. **Comprobación final** — pasa `/diagnostico`: documentación, entorno, variables, MCPs y tests.
    Si algo sale en FALLO, arréglalo antes de dar la inicialización por terminada.

**Regla general:** al terminar, ningún archivo del repo se describe a sí mismo como plantilla ni
explica cómo usarla. Toda la documentación habla del producto que se está construyendo.

## Al terminar

Resume al usuario qué archivos han cambiado y pregunta: "¿Empezamos a construir?"
