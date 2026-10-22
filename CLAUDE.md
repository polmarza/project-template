# CLAUDE.md

@AGENTS.md

## Específico de Claude Code

Las instrucciones del proyecto están en `AGENTS.md`, importado arriba: es el archivo que leen todos
los agentes. Aquí va solo lo que aplica únicamente a Claude Code. Si una regla vale para cualquier
agente, va en `AGENTS.md`, no aquí.

- Las skills de `.claude/skills/` se lanzan con `/nombre`, y Claude Code las carga por su cuenta
  cuando la tarea encaja con su `description`.
- El `/doctor` nativo no es `/diagnostico`: revisa la instalación de Claude Code y, con
  `/doctor prompt-audit`, si las instrucciones del proyecto y las skills están desfasadas o se
  contradicen.
