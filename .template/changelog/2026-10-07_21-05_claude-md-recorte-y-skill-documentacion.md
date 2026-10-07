# CLAUDE.md baja de 308 a 231 líneas, y la tabla de documentación pasa a una skill

**Fecha:** 2026-10-07 21:05
**Tipo:** Refactor
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

`CLAUDE.md` pasa de **308 a 231 líneas** (14.557 a unos 10.000 caracteres), contadas sin los
comentarios `<!-- -->`, que Claude Code no carga. La guía oficial recomienda menos de 200 por
archivo. Mismo criterio que en agosto: las reglas se quedan, los procedimientos viven en la skill
que se carga cuando toca.

| Sección | Antes | Después | Qué pasó |
|---------|------:|--------:|----------|
| Estado del proyecto y arranque | 28 | 14 | El flujo de "docs vacíos" pasa a `/init-proyecto`; queda la condición que lo dispara |
| Qué documentación necesita cada proyecto | 28 | 11 | La tabla y el orden de relleno pasan a la skill nueva `/documentacion`; quedan tres reglas |
| Documentación de referencia | 9 | 0 | Repetía el arranque y la tabla; la mención a `docs/features/` pasa a "Documentación" |
| Ciclo de trabajo de una feature | 23 | 18 | Se mantienen los cuatro tiempos y la regla de cobertura; el detalle ya estaba en `docs/features/README.md` |
| Protocolo de cambios + de PRs | 31 | 21 | Una sola sección; se quedan las dos reglas de evidencia |

- **Skill nueva `/documentacion`** (`.claude/skills/documentacion/SKILL.md`): tamaño del proyecto,
  tabla de qué documentos aplican, orden de relleno, borrado de los que no aplican y qué hacer
  cuando el proyecto crece. Es una skill aparte, y no parte de `/init-proyecto`, porque esta se
  borra al terminar la inicialización y la regla "el tamaño puede subir a mitad de camino" tiene
  que seguir disponible después.
- **`/init-proyecto` absorbe el arranque:** pregunta "¿Qué quieres construir y para quién?", carga
  `/documentacion`, rellena los documentos y solo entonces inicializa. Su `description` dispara
  con `.template/` o con `docs/` vacío, y al borrarla se retira también el paso 2 del arranque de
  `CLAUDE.md`.
- **Plantilla de PR:** recibe el porqué de pedir evidencia y no casillas, que salió de `CLAUDE.md`.

## Qué se modificó

- `CLAUDE.md`
- `.claude/skills/documentacion/SKILL.md` (nuevo)
- `.claude/skills/init-proyecto/SKILL.md`, `.claude/skills/diagnostico/SKILL.md`
- `.github/pull_request_template.md`
- `README.md`: siete skills en lugar de seis, y la tabla de skills con `/documentacion`

## Por qué

Un archivo más corto se cumple mejor, y lo que sigue ahí tiene que ser lo que se puede incumplir
sin que nadie saque el tema. El flujo de arranque, la tabla de tamaños y el checklist de PR se
usan en momentos concretos y encajan con una `description` clara.

**El riesgo, y cómo se acota:** el arranque de proyecto es lo que más puede salir mal si la skill
no se carga (código escrito con los docs vacíos). Por eso `CLAUDE.md` conserva una condición
explícita ("si existe `.template/` o `docs/` está vacío, carga `/init-proyecto`") y no una simple
referencia.

**Lo que no se ha tocado:** Límites de ejecución, Qué NO hacer y las reglas del Protocolo de MCPs,
que sí pueden incumplirse sin que alguien lo mencione. Siguen a 231 líneas, por encima de las 200;
bajar más implicaría sacar reglas, no procedimientos. Queda abierta la opción de `.claude/rules/`
con `paths:` cuando el proyecto tenga código.

## Verificado

- No quedan referencias a las secciones eliminadas ("Qué documentación necesita cada proyecto",
  "Documentación de referencia") fuera del changelog histórico.
- Claude Code lista `documentacion` e `init-proyecto` con su `description` actualizada.
- `node scripts/verificar-cobertura.mjs` → `Sin fichas de feature todavía: nada que verificar.`
