Revisa el estado del proyecto y del entorno, y da un parte de qué está bien, qué falta y cómo
arreglarlo. **Solo diagnostica: no arregla nada por su cuenta.** Al terminar, propón las
correcciones y deja que el usuario decida cuáles aplicar.

Ejecútalo cuando alguien entra al proyecto por primera vez, cuando algo falla sin motivo aparente
o antes de una sesión larga, para no descubrir a mitad que faltaba media configuración.

## Qué comprobar

### 1. Documentación

- ¿Existen todos los archivos que `CLAUDE.md` marca como obligatorios para este proyecto? (La
  obligatoriedad depende del tamaño: mira la tabla "Qué documentación necesita cada proyecto".)
- ¿Alguno está vacío — solo comentarios `<!-- -->`, sin contenido real?
- ¿Sigue existiendo `.template/`? Entonces la inicialización quedó a medias.

### 2. Fichas de feature

Ejecuta la verificación de cobertura y reporta su salida tal cual:

```bash
node scripts/verificar-cobertura.mjs
```

Comprueba las tablas contra `docs/prd.md`: filas sin validación declarada, excepciones que no
explican nada, identificadores inexistentes y tests prometidos que no existen en fichas
**Verificada**. Sus FALLO son FALLO aquí; sus ATENCIÓN son ATENCIÓN.

Añade a mano lo que el script no mira, porque requiere criterio:

- Fichas en **En construcción**: son trabajo a medias. Di cuáles y desde cuándo.
- Tests declarados que existen pero están vacíos o sin aserciones reales. El script solo comprueba
  que el archivo esté ahí; si te cruzas con uno hueco, es un FALLO aunque la verificación pase.

### 3. Entorno

- Versión de Node y de pnpm frente a lo que declare `CLAUDE.md`. Si no coinciden, dilo: la mayoría
  de fallos raros de instalación son esto.
- ¿Están las dependencias instaladas (`node_modules/`)? ¿El lockfile está al día respecto a
  `package.json`?
- Variables: compara los nombres de `.env.example` con los que hay definidos en el entorno o en
  `.env.local`. Reporta **solo los nombres que faltan**. Nunca imprimas un valor, ni completo ni
  parcial, ni siquiera para confirmar que es correcto.

### 4. Servidores MCP

Ejecuta `claude mcp list`. Contrasta el resultado con la tabla "MCPs del proyecto" de
`docs/architecture.md`:

- Servidores documentados que no arrancan o no aparecen.
- Servidores configurados que no están documentados.

### 5. Tests

- ¿Existe el comando de test que declara `docs/testing.md`? ¿Arranca?
- Si es barato, ejecútalo y reporta el resultado real. Si tarda o necesita servicios levantados, no
  lo lances: di que no se ha ejecutado y por qué. **No des por bueno lo que no has visto pasar.**

## Cómo reportar

Una tabla, un renglón por comprobación:

| Comprobación | Estado | Detalle |
|--------------|--------|---------|
| Documentación | OK | 6 de 6 archivos con contenido |
| Fichas de feature | ATENCIÓN | `registro-usuarios` lleva 3 semanas En construcción |
| Node / pnpm | FALLO | pnpm 10.4 instalado, el proyecto pide v11 |

Tres estados y nada más: **OK**, **ATENCIÓN** (funciona pero hay deuda) y **FALLO** (algo está roto
o falta). Para cada FALLO, di el comando exacto que lo arregla.

Si todo está en orden, dilo en una línea y no adornes el informe.
