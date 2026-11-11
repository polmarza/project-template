# El README enlaza la skill new-project como atajo para empezar

**Fecha:** 2026-11-11 16:12
**Tipo:** Documentación
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

"¿Cómo empezar?" gana un párrafo al final de sus cinco pasos: quien empieza proyectos a menudo
puede instalar la skill [`new-project`](https://github.com/polmarza/new-project), que hace los
pasos 1 y 2 (crear el repositorio desde la plantilla y abrirlo con el agente) con una sola frase.
Incluye el comando para instalarla.

Los cinco pasos no cambian: "Usar esta plantilla" sigue siendo el camino por defecto y no exige
instalar nada.

## Qué se modificó

- `README.md`: párrafo "El atajo" y comando de instalación al final de "¿Cómo empezar?"

## Por qué

La skill automatiza lo que hasta ahora se hacía a mano en cada proyecto: abrir la plantilla, pulsar
"Use this template", poner nombre, marcarlo como privado, clonar y abrir una sesión en la carpeta.
Se ha publicado hoy como repositorio propio y el README de la plantilla es el sitio donde la va a
buscar quien llega a ella.

Vive fuera de la plantilla, y no en `.claude/skills/`, porque se usa justo antes de que el proyecto
exista: las skills de `.claude/skills/` solo se cargan dentro de un proyecto ya clonado. Por eso se
instala a nivel de usuario y aquí solo se enlaza.

## Verificado

- `gh repo view polmarza/new-project --json visibility` → `PUBLIC`: el enlace del README resuelve
  para cualquiera.
- El comando de instalación, ejecutado sin credenciales contra una carpeta temporal en lugar de
  `~/.claude/skills/` → clona, con `SKILL.md` en la raíz y `scripts/crear-proyecto.sh` ejecutable.
- `node scripts/verificar-cobertura.mjs` → `Sin fichas de feature todavía: nada que verificar.`
  (exit 0)
- No verificado: que la skill se active en una sesión nueva de otro usuario tras instalarla así.
