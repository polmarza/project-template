---
name: documentacion
description: Decide qué archivos de docs/ necesita el proyecto según su tamaño (sitio pequeño, producto, producto con negocio), en qué orden se rellenan y cuáles se borran. Úsala al empezar un proyecto, cuando docs/ esté vacío o incompleto, y cuando el proyecto crezca (un sitio pequeño que gana cuentas de usuario, un producto que empieza a cobrar).
---

`docs/` tiene ocho archivos, pero **no todos los proyectos necesitan los ocho**. Pedirlos siempre es
la forma más rápida de que el protocolo se abandone en la segunda semana: para una landing de una
página, rellenar un modelo de datos y un plan de negocio es burocracia, y la burocracia inútil
enseña a saltarse el proceso entero.

## 1. Decide el tamaño y dilo en voz alta

Antes de hacer ninguna pregunta de documentación, y con lo que el usuario te haya contado de qué
quiere construir y para quién:

- **Sitio pequeño:** landing, portfolio, sitio de contenido. Poca lógica, sin cuentas de usuario.
- **Producto:** hay usuarios, estado y datos que persisten.
- **Producto con negocio detrás:** además hay que cobrar, medir o justificar decisiones a alguien.

| Documento | Sitio pequeño | Producto | Producto con negocio detrás |
|-----------|:-------------:|:--------:|:---------------------------:|
| `prd.md` | Obligatorio | Obligatorio | Obligatorio |
| `architecture.md` | Obligatorio | Obligatorio | Obligatorio |
| `testing.md` | Si hay lógica | Obligatorio | Obligatorio |
| `design-system.md` | Recomendado | Obligatorio | Obligatorio |
| `data-model.md` | Si hay datos | Obligatorio | Obligatorio |
| `roadmap.md` | — | Obligatorio | Obligatorio |
| `user-flows.md` | — | Si hay flujos con estado | Obligatorio |
| `business.md` | — | Si se monetiza | Obligatorio |

`prd.md` y `architecture.md` no se saltan nunca: sin saber qué se construye y sobre qué, no hay
proyecto que documentar.

## 2. Rellena los que apliquen, en este orden

prd.md → business.md → design-system.md → architecture.md → data-model.md → roadmap.md →
user-flows.md. `testing.md` se ajusta cuando `architecture.md` fija el stack.

Confirma con el usuario antes de pasar al siguiente documento.

## 3. Borra los que no apliquen

Un documento que no aplica **se borra**, no se deja vacío. Un archivo con solo comentarios es
indistinguible de uno que se olvidó rellenar, y el arranque de cada sesión se para a preguntar por
él. Antes de borrar, enseña al usuario la lista exacta (límite 4 de `CLAUDE.md`).

## 4. Cuando el tamaño sube

Un sitio pequeño que empieza a tener cuentas de usuario, o un producto que empieza a cobrar, necesita
los documentos que le faltaban. Se crean en ese momento, no al final: vuelve a esta tabla, di qué
tamaño tiene ahora el proyecto y rellena lo que falte.
