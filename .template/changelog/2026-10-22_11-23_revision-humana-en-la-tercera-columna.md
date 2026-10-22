# La tercera columna admite la revisión humana como forma propia

**Fecha:** 2026-10-22 11:23
**Tipo:** Refactor
**Requisitos:** Ninguno (cambio sobre el andamiaje de la plantilla)

## Qué se hizo

La tercera columna de la tabla de cobertura pasa de dos formas válidas a tres:

1. La ruta del test que lo valida.
2. **`revisión humana: <qué se mira>; <qué tiene que verse>`** (nueva).
3. `no verificable por interfaz: <razón concreta>` y cómo se comprueba entonces.

`scripts/verificar-cobertura.mjs` acepta la nueva forma (con o sin tilde y sin distinguir
mayúsculas) y falla si no trae las dos partes separadas por punto y coma, o si alguna tiene menos
de 8 caracteres. Igual que con la excepción, la comprobación es estructural: el script no puede
saber si la revisión se hizo, así que la plantilla de PR pide declararla (quién la hizo, qué se
miró y qué se vio).

## Qué se modificó

- `scripts/verificar-cobertura.mjs`: la forma `revisión humana:` y su comprobación; mensajes de
  error que nombran las tres formas
- `docs/features/README.md`: tres formas válidas, una fila de ejemplo y qué detecta el script
- `AGENTS.md`: la regla de la tercera columna y el tiempo "Validar"
- `.claude/skills/feature/SKILL.md`: paso 4, con las tres formas y cuándo no usar la revisión humana
- `docs/testing.md`: las revisiones humanas se hacen en la misma pasada que los tests
- `.github/pull_request_template.md`: cómo se declara una revisión humana en la evidencia
- `README.md`: la regla en el protocolo y en "La regla que lo sostiene"

## Por qué

Hay requisitos que se comprueban mejor con los ojos que con un test: que una pantalla se lea en el
móvil, que una conversación con un agente fluya como se acordó, que algo se vea como dice el design
system. Hasta ahora entraban como `no verificable por interfaz`, y el nombre decía lo contrario de
lo que pasaba: esa comprobación se hace precisamente mirando la interfaz. La excepción vuelve a
servir para lo que su nombre dice (lo que no tiene interfaz que mirar: un índice, una variable de
entorno).

Lo que hace válida una revisión humana es que sea repetible: qué se mira y qué tiene que verse. "Lo
he mirado y está bien" no lo es, igual que "los tests pasan" no es evidencia. Por eso el formato
obliga a escribir las dos partes. Y para que no se convierta en la salida fácil, `/feature` avisa:
lo que un test cubre bien va con test, porque el test se repite solo en cada PR y la revisión
depende de que alguien la haga.

Sale de preparar el curso de SDD, al explicar la validación de un agente conversacional.

## Verificado

- `node scripts/verificar-cobertura.mjs` en la plantilla → `Sin fichas de feature todavía: nada
  que verificar.` (exit 0)
- Con fichas de prueba en una copia aparte:
  - Ficha Verificada con un test existente, una revisión humana completa y una excepción → `Todo en
    orden.` (exit 0)
  - `revisión humana: lo he mirado y está bien` (sin punto y coma) y `revisión humana: el chat en el
    móvil; ok` (segunda parte corta) → un fallo cada una (exit 1)
  - `Revision Humana: …` sin tilde y con mayúsculas, con las dos partes → aceptada
