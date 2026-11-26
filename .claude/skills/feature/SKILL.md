---
name: feature
description: Crea la ficha de una feature en docs/features/, con su tabla de cobertura, antes de escribir código. Úsala cuando se acuerde construir algo que cierra requisitos del PRD, toca varias capas o va a durar más de una sesión. No hace falta para un arreglo puntual, un cambio de copy o un ajuste de estilos.
argument-hint: "[nombre-de-la-feature]"
---

Crea la ficha de una feature nueva en `docs/features/`, siguiendo el formato de
`docs/features/README.md`.

Esto se hace **antes** de escribir código, no después. La ficha es el acuerdo previo; si ya hay
código escrito, lo que toca es una entrada de changelog, no una ficha retroactiva.

## 1. Comprueba que hace falta

Una ficha se justifica si el trabajo cierra requisitos del PRD, toca varias capas o va a durar más
de una sesión. Para un arreglo puntual o un cambio de copy, dilo y no la crees: basta el changelog
al terminar.

## 2. Reúne el contexto

Lee `docs/prd.md` para localizar qué requisitos (`M-01`, `S-02`…) cierra esta feature. Si el
trabajo no se corresponde con ningún requisito del PRD, hay dos posibilidades y conviene
preguntarlas antes de seguir:

- Es alcance nuevo → hay que añadirlo al PRD primero, con su ID y su criterio de aceptación.
- Está fuera de alcance → va a `mejoras/`, no a `docs/features/`.

Lee también `docs/architecture.md` y `docs/data-model.md` si la feature toca estructura o datos.

## 3. Pregunta lo que no puedas deducir

- Nombre de la feature (el archivo será `kebab-case.md`)
- Qué debe poder hacer el usuario cuando esto exista
- Qué queda explícitamente fuera
- Qué tiene que pasar cuando algo falla, si no se deduce del PRD ni de `docs/user-flows.md`

## 4. Escribe la ficha

Usa la plantilla de `docs/features/README.md`. Estado inicial: **Acordada**.

**Comportamiento.** Escribe solo lo que harías distinto de lo que quiere el usuario si no estuviera
escrito: los estados que ve, qué se le dice y qué se conserva cuando algo falla, los casos límite y
los datos o contratos que la feature crea o consume. Lo que no aplique se borra. Si el flujo ya
está en `docs/user-flows.md`, enlaza su `FLOW-xx`. Si la feature usa IA, fija con el usuario el
conjunto de casos y el umbral con que se evaluará, antes de construir.

La tabla de cobertura se rellena entera, sin huecos. Por cada requisito, la tercera columna lleva
una de tres cosas:

- La ruta del test que lo validará.
- `revisión humana: <qué se mira>; <qué tiene que verse>`, cuando se comprueba mejor con los ojos
  que con un test: cómo se ve una pantalla, cómo suena una conversación. Las dos partes, concretas:
  otra persona tiene que poder repetirla.
- `no verificable por interfaz: <razón concreta>` seguido de cómo se comprobará entonces, para lo
  que no tiene interfaz que mirar (un índice, una variable de entorno).

Si no sabes cuál poner, pregunta — no lo dejes en blanco ni escribas un test que sabes que no vas
a escribir. Y no uses la revisión humana para lo que un test cubriría bien: el test se repite solo
en cada PR; la revisión depende de que alguien la haga.

**Plan.** Ordena las filas de la tabla en pasos según sus dependencias: primero lo que otros
necesitan (datos, contratos), después lo que se apoya en ello. Cada paso dice qué queda revisable
al terminarlo y, si toca datos o servicios externos, cómo se deshace. Añade los riesgos que puedan
torcer el orden. Una ficha de una sola fila tiene un plan de una línea; no lo infles.

## 5. Revísala como un QA antes de enseñarla

Relee la ficha como si fueras a encontrarle los fallos, no a defenderla, junto con los requisitos
del PRD que cierra. Busca:

- **Ambigüedades:** palabras que el agente rellenaría a su manera ("rápido", "bien", "los que no
  valen") o un "entonces" que no se puede mirar y decir sí o no.
- **Contradicciones:** entre requisitos de la ficha, o entre la ficha y el PRD.
- **Casos límite sin cubrir:** el caso negativo previsible, datos vacíos o repetidos, qué pasa si
  falla una integración, un estado de la interfaz que nadie ha descrito.
- **Plan que no se sostiene:** un paso que depende de otro posterior, un paso que no deja nada
  revisable, o uno que toca datos sin decir cómo se deshace.
- **Choques con las reglas:** con `AGENTS.md` (límites de ejecución, "Qué NO hacer") o con
  `docs/` (arquitectura, modelo de datos, design system).

Preséntalo como lista numerada, **sin proponer soluciones todavía**: si las propones a la vez, el
usuario acepta la tuya sin pensar la suya. Cada punto se cierra con el usuario de una de tres
formas: se corrige la ficha (o el PRD), pasa a "Decisiones tomadas" o pasa a "Fuera de esta
feature". Repite la revisión si la ficha cambia mucho. Si no encuentras nada, dilo, y di qué has
revisado.

## 6. Confirma antes de construir

Enseña la ficha al usuario y pregunta si el acuerdo es correcto. Con su visto bueno, cambia el
estado a **En construcción** y empieza.

## 7. Construye un paso del plan cada vez

Cada paso del plan es una unidad de trabajo. Impleméntalo, di qué has cambiado y cómo verlo
funcionando (qué abrir, qué hacer, qué debería aparecer), ciérralo en un commit propio y **para**.
El siguiente paso empieza con el visto bueno del usuario, salvo que te pida avanzar varios
seguidos.

Así el usuario revisa trozos que puede comprobar, un error en el paso 2 no se descubre cuando ya
está construido encima el 5, y cada paso tiene un punto al que volver.

El plan puede cambiar de orden o partir un paso en dos; dilo y actualiza la ficha. Lo que no puede
es crecer en silencio: si aparece un requisito que no está en el PRD, para y pregúntalo. Va al PRD,
con su ID y su criterio, antes que a la tabla y al código. Los tests van después, en su propia pasada, como dice
`docs/testing.md`.

Mantén el estado al día durante el trabajo, no al final: es lo que permite retomar la feature en
otra sesión sin reconstruir el contexto.
