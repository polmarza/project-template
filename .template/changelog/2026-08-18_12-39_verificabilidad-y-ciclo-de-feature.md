# Verificabilidad: criterios de aceptación, ficha de feature y evidencia en el PR

**Fecha:** 2026-08-18 12:39
**Tipo:** Documentación
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

La plantilla cubría bien el principio de un proyecto (documentar antes de escribir) y el registro
posterior (changelog, PR, mejoras), pero no decía nada sobre cómo se sabe que algo está terminado.
"Hecho" quedaba en manos de quien lo declaraba. Este cambio cierra ese hueco en cuatro piezas.

**1. Los requisitos del PRD ahora son comprobables.** Cada entrada MoSCoW de `docs/prd.md` lleva
un identificador estable (`M-01`, `S-01`, `C-01`) y un criterio de aceptación en formato
"Dado…, cuando…, entonces…", con la condición de que el "entonces" sea observable: un mensaje
visible, una redirección, un registro creado. No un adjetivo. El ID es el nombre por el que ese
requisito se cita después en la ficha, en el changelog, en el PR y en el nombre del test.

**2. Nueva capa intermedia: `docs/features/`.** Entre la documentación del proyecto y el código no
había ninguna unidad de trabajo. Ahora cada feature tiene su ficha —qué se construye, qué
requisitos cierra, qué queda fuera— y sobre todo una **tabla de cobertura** con una regla: ningún
requisito se queda sin tercera columna. O lleva la ruta del test que lo valida, o lleva
`no verificable por interfaz: <razón concreta>` y cómo se comprueba entonces. La ficha tiene tres
estados (Acordada / En construcción / Verificada) que se actualizan durante el trabajo, no al
final, para poder retomar una feature en otra sesión sin reconstruir el contexto.

**3. Los tests se escriben después de implementar.** Nueva sección en `docs/testing.md`. El
compromiso de validar se adquiere antes (la tabla de cobertura); el test se escribe leyendo el
código ya existente. Con las reglas que se derivan: verificar que el selector existe antes de
asertar, añadir `data-testid` si no hay selector estable, una aserción por cada "entonces", y
nunca arreglar un test que falla quitándole aserciones.

**4. El PR se cierra con evidencia.** La plantilla de PR pide ahora los requisitos que cierra, una
sección de evidencia con la salida real de los comandos ejecutados y una tabla de verificación por
requisito. El checklist sigue estando, pero deja de ser la prueba: lo que prueba es la salida
pegada.

Además, dos cosas que faltaban y no dependen del stack:

- **Tabla de proporcionalidad** en `CLAUDE.md`: qué documentos de `docs/` son obligatorios según
  el tamaño del proyecto (sitio pequeño / producto / producto con negocio). Los que no aplican se
  borran en la inicialización, no se dejan vacíos.
- **Sección "Límites de ejecución"** en `CLAUDE.md`: todo se prueba en local, el agente no
  despliega, los secretos no se imprimen ni se pasan por la línea de comandos, y nada destructivo
  sin confirmación previa con el alcance exacto.

Dos comandos nuevos: `/feature` (crea la ficha antes de construir) y `/doctor` (parte del estado
de documentación, fichas a medias, entorno, variables, MCPs y tests; solo diagnostica, no arregla).

## Qué se modificó

- `CLAUDE.md` — nueva sección "Qué documentación necesita cada proyecto" con la tabla de tamaños;
  nueva sección "Límites de ejecución"; nueva sección "Ciclo de trabajo de una feature"; paso 5 de
  arranque (revisar fichas En construcción) y referencia a `/doctor`; campo `Requisitos` en el
  formato de changelog; dos ejemplos nuevos en la lista de documentación afectada; pasos 2 y 4 del
  protocolo de PRs (requisitos y evidencia) con el apartado "Por qué la evidencia y no la casilla";
  dos reglas nuevas en "Qué NO hacer"; `docs/features/` en la estructura de carpetas; paso 7 del
  checklist de inicialización (borrar documentos que no apliquen) y renumeración
- `docs/prd.md` — IDs estables y criterios de aceptación en el bloque MoSCoW
- `docs/features/README.md` — nuevo: formato de la ficha, regla de la tabla de cobertura y estados
- `docs/testing.md` — nueva sección "Cuándo se escriben los tests"
- `docs/architecture.md` — la estrategia de despliegue debe dejar escrito quién despliega
- `.claude/commands/feature.md` — nuevo comando `/feature`
- `.claude/commands/doctor.md` — nuevo comando `/doctor`
- `.claude/commands/changelog.md` — campo `Requisitos` y comprobación del estado de la ficha
- `.claude/commands/init-proyecto.md` — tabla de tamaños al completar docs; paso de borrado de
  documentos que no apliquen; `/doctor` como comprobación final; renumeración
- `.github/pull_request_template.md` — sección "Requisitos que cierra", sección "Evidencia" con
  tabla de verificación, checklist reformulado
- `changelog/README.md` — campo `Requisitos` en el formato, sincronizado con `CLAUDE.md`
- `.claude/settings.json` — permitidas tres comprobaciones de solo lectura que necesita `/doctor`:
  `node -v`, `node --version` y `claude mcp list`
- `README.md` — `docs/features/` en el contenido; el protocolo pasa de 6 a 10 pasos; comandos
  nuevos; filas de `docs/` y `docs/features/` en la tabla de adaptación; `/doctor` en el arranque

## Por qué

El protocolo anterior era enteramente autodeclarado. Todas las reglas eran "el agente debe", y el
checklist del PR lo marcaba el mismo agente que había hecho el trabajo: quien afirmaba haber
verificado y quien tenía que verificar eran el mismo. Una casilla marcada no distingue entre "lo
ejecuté y pasó" y "estoy razonablemente seguro de que pasaría"; la salida de un comando sí.

El hueco de fondo era otro: la plantilla gobernaba el proyecto pero no la unidad de trabajo. Una
feature existía como conversación → código → entrada de changelog escrita a posteriori. No había
ningún artefacto que dijera "esto es lo que acordamos construir y así sabremos que funciona"
**antes** del código, así que el alcance se renegociaba solo, sin que nadie lo notara.

La regla de la tercera columna es la que sostiene el resto. Lo que se queda sin validar casi nunca
se decide: se escurre. Nadie dice "este requisito no lo vamos a comprobar"; simplemente no aparece
en ningún sitio y nadie lo echa de menos hasta que falla. Obligar a escribir la excepción convierte
una omisión invisible en una frase que alguien puede leer y discutir.

Lo de escribir los tests después de implementar viene del mismo sitio. Un test escrito durante la
planificación apunta a selectores y rutas imaginados; cuando no coinciden con la realidad, casi
nadie lo reescribe: se le van quitando aserciones hasta que pasa, y queda un test que no comprueba
nada pero da luz verde. Es peor que no tenerlo, porque además tranquiliza.

La tabla de proporcionalidad resuelve el problema opuesto. Exigir ocho documentos rellenos para una
landing es la forma más rápida de que el protocolo se abandone en la segunda semana, y un protocolo
abandonado no protege nada. La ceremonia tiene que escalar con lo que está en juego.
