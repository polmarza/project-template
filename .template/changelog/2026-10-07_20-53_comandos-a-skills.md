# Los comandos pasan a ser skills, y `/doctor` pasa a llamarse `/diagnostico`

**Fecha:** 2026-10-07 20:53
**Tipo:** Migración
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

Claude Code ha fusionado los comandos personalizados con las skills. Según su documentación
oficial, un archivo en `.claude/commands/deploy.md` y una skill en
`.claude/skills/deploy/SKILL.md` crean el mismo `/deploy`. Los comandos siguen funcionando, pero
quedan como formato heredado, y todo lo nuevo (frontmatter, archivos de apoyo, carga automática)
llega a las skills. La plantilla se pasa al formato actual:

- **Los seis comandos son ahora skills**, cada uno en `.claude/skills/<nombre>/SKILL.md`. Se han
  movido con `git mv` para que conserven el historial. Cada uno lleva frontmatter con `name`,
  `description` (qué hace y **cuándo usarlo**) y, si recibe argumentos, `argument-hint`.
- **`/doctor` pasa a llamarse `/diagnostico`.** El `/doctor` de Claude Code es ahora una skill
  nativa (revisa la instalación, el coste en contexto de skills y MCPs, y audita los `CLAUDE.md`
  con `/doctor prompt-audit`). Una skill del proyecto con el mismo nombre la sustituye, así que el
  `/doctor` de la plantilla dejaba sin acceso al nativo. Con el cambio de nombre, ambos conviven.
- **El checklist de inicialización sale de `CLAUDE.md`** y queda solo en `/init-proyecto`. Estaba
  duplicado en los dos sitios. `CLAUDE.md` conserva la regla (inicializar por iniciativa propia, y
  que ningún archivo se describa como plantilla después) y remite a la skill.
- **`/init-proyecto` incorpora tres cosas que faltaban:**
  - Abrir `CLAUDE.md` con Read antes de rellenarlo. Claude Code quita los comentarios
    `<!-- ... -->` del `CLAUDE.md` que se carga automáticamente, y los placeholders están justo
    ahí.
  - Borrar la propia skill al terminar.
  - Pedir confirmación antes de cualquier borrado, según el límite 4 de ejecución.
- **Regla nueva en "Qué NO hacer":** los procedimientos nuevos van a `.claude/skills/`, no a
  `CLAUDE.md` ni a `.claude/commands/`.

## Qué se modificó

- `.claude/commands/*.md` → `.claude/skills/<nombre>/SKILL.md` (seis archivos; `doctor.md` →
  `diagnostico/SKILL.md`), con frontmatter añadido
- `.claude/skills/init-proyecto/SKILL.md`: checklist completo, nota sobre los comentarios
  ocultos, confirmación antes de borrar y autoborrado de la skill
- `.claude/skills/diagnostico/SKILL.md`: en qué se diferencia del `/doctor` nativo
- `CLAUDE.md`: el checklist de inicialización se sustituye por una referencia a la skill,
  `/doctor` → `/diagnostico` y regla nueva sobre dónde van los procedimientos
- `README.md`: la sección "Comandos" pasa a "Skills" y se explica la carga automática;
  `/doctor` → `/diagnostico`; se añade la skill de inicialización a la tabla de lo que se borra
- `.template/README.md`, `docs/architecture.md`: "comando" → "skill"

## Por qué

En el refactor del 18 de agosto, al llevar los procedimientos de `CLAUDE.md` a los comandos, se
apuntó un coste: *lo que está en un comando se carga solo si alguien lo invoca*. Con las skills
eso deja de ser así. Claude Code tiene en contexto la `description` de cada skill y carga la skill
entera cuando la tarea encaja. Por eso las descripciones dicen cuándo usar cada una, y no solo qué
hacen: es lo que decide si se cargan sin que nadie las invoque.

La documentación oficial de memoria va en la misma dirección. Recomienda que cada `CLAUDE.md` no
pase de 200 líneas y que los procedimientos de varios pasos vivan en skills. El checklist de
inicialización era exactamente eso, y además estaba duplicado.

**Lo que no se ha tocado, y por qué:**

- **`AGENTS.md`.** Desde la v2.1.277, Claude Code lee `AGENTS.md` cuando no hay `CLAUDE.md`.
  Pasar las instrucciones a `AGENTS.md` haría el repo legible para otros agentes (Codex, Cursor…).
  Es una decisión de alcance, no una corrección, así que queda abierta.
- **El resto de `CLAUDE.md`.** Sin comentarios ocupa unas 310 líneas, por encima de las 200
  recomendadas. Recortar más significaría sacar reglas, no procedimientos, y la frontera de agosto
  se mantiene.

## Verificado

- Claude Code carga las seis skills con su frontmatter: aparecen en el listado de skills de la
  sesión, con su `description`.
- No queda en el repo ninguna referencia a `.claude/commands/` ni al `/doctor` de la plantilla,
  salvo en el changelog histórico.
- `node scripts/verificar-cobertura.mjs` → `Sin fichas de feature todavía: nada que verificar.`
  (exit 0)
