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

## 4. Escribe la ficha

Usa la plantilla de `docs/features/README.md`. Estado inicial: **Acordada**.

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

## 5. Revísala como un QA antes de enseñarla

Relee la ficha como si fueras a encontrarle los fallos, no a defenderla, junto con los requisitos
del PRD que cierra. Busca:

- **Ambigüedades:** palabras que el agente rellenaría a su manera ("rápido", "bien", "los que no
  valen") o un "entonces" que no se puede mirar y decir sí o no.
- **Contradicciones:** entre requisitos de la ficha, o entre la ficha y el PRD.
- **Casos límite sin cubrir:** el caso negativo previsible, datos vacíos o repetidos, qué pasa si
  falla una integración.
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

## 7. Construye una fila cada vez

Cada fila de la tabla de cobertura es una unidad de trabajo. Implementa un requisito, di qué has
cambiado y cómo verlo funcionando (qué abrir, qué hacer, qué debería aparecer) y **para**. La
siguiente fila empieza con el visto bueno del usuario, salvo que te pida avanzar varias seguidas.

Así el usuario revisa trozos que puede comprobar, y un error en el requisito 2 no se descubre
cuando ya está construido encima el 5. Los tests van después, en su propia pasada, como dice
`docs/testing.md`.

Mantén el estado al día durante el trabajo, no al final: es lo que permite retomar la feature en
otra sesión sin reconstruir el contexto.
