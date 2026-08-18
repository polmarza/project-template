# CLAUDE.md se queda con las reglas; los procedimientos se van a los comandos

**Fecha:** 2026-08-18 16:37
**Tipo:** Refactor
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

`CLAUDE.md` pasa de **516 a 370 líneas** (-28%) sin perder una sola regla. Lo que se ha ido son
los *cómo*, que ya vivían duplicados en los comandos y ahora viven solo allí.

El criterio aplicado, sección por sección: *si nadie menciona este tema en toda la sesión,
¿cambia algo que esto esté aquí?*

- **Regla** — el agente puede incumplirla sin que nadie saque el tema. Se queda.
  ("La clave real nunca se escribe en `.mcp.json`.")
- **Procedimiento** — solo hace falta cuando estás haciendo esa cosa concreta, y entonces se invoca
  el comando, que lo trae. Se va.
  (`claude mcp add --transport http <nombre> --scope project <url>`.)

| Sección | Antes | Después | El procedimiento vive en |
|---------|------:|--------:|--------------------------|
| Protocolo de MCPs | 94 | 30 | `/mcp-setup` |
| Protocolo de cambios + de PRs | ~98 | 42 | `changelog/README.md`, `/changelog`, plantilla de PR |
| Ciclo de trabajo de una feature | 54 | 31 | `/feature`, `docs/features/README.md` |

**Antes de cortar nada se comprobó que el destino lo tuviera de verdad.** Dos cosas solo existían
en `CLAUDE.md` y se movieron primero:

- La tabla de alcances (`user` / `project` / `local`, con dónde vive cada uno) y la sintaxis de
  expansión `${VAR}` de `.mcp.json` → `/mcp-setup`.
- El razonamiento de que la verificación es estructural y no semántica —un test vacío pasa, pero un
  archivo vacío se ve en el diff y uno inexistente no— → `docs/features/README.md`.

De paso: eliminada la referencia a `/autopilot`, un comando que no existe en este repositorio.

## Qué se modificó

- `CLAUDE.md` — comprimidas las secciones de MCPs, cambios, PRs y ciclo de feature; fuera la
  referencia muerta a `/autopilot`
- `.claude/commands/mcp-setup.md` — recibe la tabla de alcances y la expansión de `${VAR}`
- `docs/features/README.md` — recibe el porqué de la verificación estructural y el de que corra en CI

## Por qué

El coste en tokens nunca fue el problema: 6.400 tokens son un 3% de la ventana de contexto. El
problema es la **atención**. Una regla en la línea 400, rodeada de trescientas líneas de
procedimiento que el agente no necesita en esa sesión, compite con todo lo demás. Los archivos más
cortos se cumplen mejor, y eso no lo arregla que los tokens sean baratos.

Había además duplicación literal, no teórica: el formato del changelog estaba en `CLAUDE.md`, en
`changelog/README.md` y en `/changelog`; la regla de la tercera columna, en `CLAUDE.md`, en
`docs/features/README.md` y en `/feature`. Tres copias de lo mismo es una garantía de que
divergirán.

**Lo que se pierde, y conviene decirlo:** lo que está en `CLAUDE.md` está en contexto garantizado;
lo que está en un comando se carga solo si alguien lo invoca. Cada línea que sale se debilita un
poco. Por eso la frontera se puso donde se puso: nadie ejecuta `claude mcp add` por accidente, pero
sí puede escribir una clave real en un archivo que se commitea sin haber invocado `/mcp-setup`.

## Verificado

- Auditadas trece reglas del documento original contra todo el repositorio: las trece siguen
  presentes, en `CLAUDE.md` o en el archivo que se carga cuando toca.
- Los seis comandos referenciados en `CLAUDE.md` existen en `.claude/commands/` (`/security-review`
  es nativo de Claude Code).
- Sin separadores duplicados ni secciones huérfanas tras el recorte.
- `node scripts/verificar-cobertura.mjs` sigue saliendo limpio.
