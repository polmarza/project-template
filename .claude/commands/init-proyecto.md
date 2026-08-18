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

Ejecuta el checklist de "Inicialización del proyecto" de `CLAUDE.md`:

1. `README.md` — reescríbelo entero para el proyecto (qué es, qué problema resuelve, requisitos,
   variables de entorno, instalación con `pnpm`, estructura, cómo contribuir, estado). Sin
   referencias a la plantilla.
2. `CLAUDE.md` — rellena nombre, descripción, estado, stack, estructura de carpetas, convenciones
   y "Qué NO hacer". Borra los comentarios que ya no apliquen y la sección de inicialización del
   proyecto (ya no hace falta) junto con la referencia a este comando. **El "Protocolo de MCPs" se
   queda**: sigue aplicando cada vez que entre una integración nueva.
3. `LICENSE` — sustituye la línea de copyright de la plantilla por el año actual y el
   titular de este proyecto.
4. `.env.example` — deja solo las variables del stack real.
5. MCPs — pregunta qué servidores MCP quiere y con qué alcance, siguiendo el "Protocolo de MCPs"
   de `CLAUDE.md`. Si prefieres tratarlo aparte, lanza `/mcp-setup`.
6. `docs/` — borra los documentos que este proyecto no necesite según la tabla de tamaños. Los que
   no aplican se borran, no se dejan vacíos: un archivo con solo comentarios hace que el arranque
   de cada sesión se pare a preguntar por él. `docs/features/` se queda vacía, solo con su
   `README.md`.
7. `mejoras/backlog.md` — borra el ejemplo comentado.
8. `.template/` — bórrala (`rm -rf .template`). Quita después las referencias a
   `.template/assets/` que queden en otros archivos: hay una en `docs/features/README.md`.
9. `changelog/` — crea la primera entrada real del proyecto (tipo: Configuración) con `/changelog`
   y limpia de `changelog/README.md` la referencia a la plantilla.
10. Verifica que no queden restos:
    `grep -ril "plantilla\|template" . --exclude-dir=.git --exclude-dir=node_modules`
11. Pasa `/doctor` como última comprobación: entorno, variables, MCPs y tests. Si algo sale en
    FALLO, arréglalo antes de dar la inicialización por terminada.

## Al terminar

Resume al usuario qué archivos han cambiado y pregunta: "¿Empezamos a construir?"
