# La instalación del panel MoSCoW funciona también en versiones antiguas de Claude Code

**Fecha:** 2026-11-15 19:45
**Tipo:** Configuración
**Requisitos:** Ninguno (corrige el cambio de `2026-11-15_13-56_panel-moscow.md`)

## Qué se hizo

El comando de instalación del mod pasa de `claude plugin install moscow-panel --marketplace
polmarza/moscow-panel` a dos comandos, `claude plugin marketplace add polmarza/mod-moscow-panel` y
`claude plugin install moscow-panel@moscow-panel`. Además, el repositorio del mod se llama ahora
`mod-moscow-panel`, y los enlaces lo reflejan.

## Qué se modificó

- `README.md`, `CLAUDE.md`, `.claude/skills/init-proyecto/SKILL.md` y
  `.claude/skills/diagnostico/SKILL.md`: comando y enlace nuevos.
- `.template/changelog/2026-11-15_13-56_panel-moscow.md`: mismo cambio en su texto.

## Por qué

La opción `--marketplace` solo existe en versiones recientes de Claude Code: en la 2.1.100 el
comando falla con `error: unknown option '--marketplace'`. Los dos comandos separados funcionan en
las dos versiones probadas. El nombre del repositorio cambia por decisión del autor del mod; los
enlaces antiguos redirigen, pero conviene apuntar al nombre actual.

## Verificado

- `claude plugin marketplace add polmarza/mod-moscow-panel` y `claude plugin install
  moscow-panel@moscow-panel`, con las versiones 2.1.100 y 2.1.321 y `CLAUDE_CONFIG_DIR` apuntando a
  una carpeta vacía → marketplace añadido, mod instalado y visible en `claude plugin list`.
- Ejecutados además en la terminal real del autor (2.1.100): los dos terminan con `✔ Successfully`.
- `git grep` de `--marketplace` y de `polmarza/moscow-panel` → sin resultados.
