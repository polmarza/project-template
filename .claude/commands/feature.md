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
o la ruta del test que lo validará, o `no verificable por interfaz: <razón concreta>` seguido de
cómo se comprobará entonces. Si no sabes cuál de las dos poner, pregunta — no lo dejes en blanco
ni escribas un test que sabes que no vas a escribir.

## 5. Confirma antes de construir

Enseña la ficha al usuario y pregunta si el acuerdo es correcto. Con su visto bueno, cambia el
estado a **En construcción** y empieza.

Mantén el estado al día durante el trabajo, no al final: es lo que permite retomar la feature en
otra sesión sin reconstruir el contexto.
