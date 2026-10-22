# AGENTS.md pasa a ser el contrato, y el ciclo de feature gana clarificación y una fila cada vez

**Fecha:** 2026-10-22 09:49
**Tipo:** Refactor
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

Tres mejoras sacadas de comparar la plantilla con el flujo de Spec-Driven Development que enseña el
curso de MoureDev (`mouredev/hello-sdd`): constitución, spec, clarificación, plan, tareas,
implementación y validación.

- **`AGENTS.md` es el contrato de entrada.** Todo lo que había en `CLAUDE.md` pasa a `AGENTS.md`.
  Como `CLAUDE.md` sigue existiendo, git no lo registra como renombrado: la historia de esas reglas
  anterior a este cambio está en `git log -- CLAUDE.md`. `CLAUDE.md` se queda en una línea que lo importa
  (`@AGENTS.md`) más lo único que es específico de Claude Code: cómo se lanzan las skills y qué es
  el `/doctor` nativo. `AGENTS.md` explica además que las skills son archivos que cualquier agente
  puede abrir y seguir, no solo comandos de Claude Code.
- **Clarificación antes de acordar.** `/feature` tiene un paso nuevo (el 5): antes de enseñar la
  ficha, el agente la revisa como un QA y presenta en lista numerada las ambigüedades, las
  contradicciones, los casos límite sin cubrir y los choques con `AGENTS.md` o `docs/`, **sin
  proponer soluciones**. Cada punto se cierra corrigiendo la ficha, pasándolo a "Decisiones
  tomadas" o a "Fuera de esta feature". El tiempo **Acordar** de `AGENTS.md` lo recoge.
- **Una fila cada vez.** El tiempo **Construir** de `AGENTS.md` y el paso 7 de `/feature`: se
  implementa una fila de la tabla de cobertura, el agente dice qué ha cambiado y cómo verlo
  funcionando, y para hasta el visto bueno. Los tests siguen yendo después, en su propia pasada.

## Qué se modificó

- `CLAUDE.md` → `AGENTS.md` (renombrado), con la cabecera nueva y los tiempos Acordar y Construir
- `CLAUDE.md` (nuevo): import de `AGENTS.md` y la sección "Específico de Claude Code"
- `.claude/skills/feature/SKILL.md`: pasos 5 (revisión QA) y 7 (una fila cada vez)
- `docs/features/README.md`: la tabla de estados recoge la revisión y la construcción por filas
- `.claude/skills/init-proyecto/SKILL.md`: se rellena `AGENTS.md`; `CLAUDE.md` no se toca
- `.claude/skills/changelog/`, `diagnostico/`, `documentacion/`, `mcp-setup/`,
  `docs/architecture.md`, `.template/README.md`: las referencias a las reglas apuntan a `AGENTS.md`
- `README.md`: `AGENTS.md` en "¿Qué hay dentro?", paso 3 del protocolo con la revisión y las filas,
  y la tabla de "Adaptar para tu proyecto"

## Por qué

**`AGENTS.md`:** la decisión quedó abierta en el changelog del 7 de octubre ("es una decisión de
alcance, no una corrección"). La plantilla se presenta como agnóstica al stack, pero no lo era al
agente: con Codex, Cursor o Copilot el contrato no se leía. Se usa import desde `CLAUDE.md` y no la
lectura directa de `AGENTS.md` que hacen las versiones recientes de Claude Code cuando falta
`CLAUDE.md`, porque el import funciona en cualquier versión y deja un sitio para lo específico de
Claude Code sin mezclarlo con las reglas comunes.

**Clarificación:** era el hueco más claro frente al flujo del curso. `/feature` ya preguntaba lo
que no podía deducir, pero nadie buscaba activamente los fallos de la ficha antes de construir. Lo
de no proponer soluciones es deliberado: si llegan a la vez que el problema, el usuario acepta la
del agente sin pensar la suya.

**Una fila cada vez:** el curso lo hace con un `tasks.md` y "haz una tarea y para". Aquí no se crea
un archivo de tareas porque la tabla de cobertura ya enlaza cada requisito con dónde se implementa
y con qué se valida; la unidad de trabajo es la fila. El objetivo es el mismo: que el usuario
revise trozos que puede comprobar y que un error en un requisito no aparezca cuando ya hay otros
cinco construidos encima.

**Lo que no se ha adoptado del curso, y por qué:** `tasks.md` (duplicaría la tabla de cobertura),
la notación EARS (dos formatos de criterio de aceptación confunden; se mantiene "Dado…, cuando…,
entonces…") y los tests antes del código (la plantilla los escribe después a propósito; ver
`docs/testing.md`).

## Verificado

- Claude Code (2.1.100) carga `AGENTS.md` a través del import: con todas las herramientas de lectura
  desactivadas, `claude -p` responde qué se hace en "Construir" (una fila de la tabla cada vez) y
  dice que la regla viene de `AGENTS.md`.
- No queda ninguna referencia a `CLAUDE.md` como archivo de reglas fuera del changelog histórico y
  de `.template/assets/gen-flujo.py`, que genera un GIF ya publicado.
- `node scripts/verificar-cobertura.mjs` → `Sin fichas de feature todavía: nada que verificar.`
  (exit 0)
