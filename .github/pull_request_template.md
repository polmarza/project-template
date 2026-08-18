<!-- 💡 Si usas el agente (Claude Code), pídele que abra el PR — él rellena esta plantilla automáticamente.
     Si lo abres tú manualmente desde GitHub, rellena los campos a continuación. -->

## ¿Qué se hizo?
<!-- Describe el cambio en una o dos frases -->

## Motivación
<!-- Por qué es necesario este cambio -->

## Requisitos que cierra
<!-- IDs del PRD que este cambio deja terminados: M-01, S-02…
     Escribe "ninguno" si es un cambio interno (refactor, tooling, documentación). -->

## Tipo de cambio
- [ ] Feature
- [ ] Fix
- [ ] Refactor
- [ ] Migración
- [ ] Documentación
- [ ] Configuración

## Evidencia

<!-- Pega aquí el comando que has ejecutado y su salida real, recortada a lo relevante.
     No lo parafrasees: "los tests pasan" no es evidencia, la salida de los tests sí.
     Si algo no se ha ejecutado, dilo y explica por qué en lugar de omitirlo.

     Repasa lo que pegas antes de enviarlo: la salida de un comando puede arrastrar tokens,
     cadenas de conexión o rutas locales. Un PR es público o, como mínimo, permanente.
     Sustituye cualquier valor sensible por su nombre de variable. -->

```
$ pnpm test
...
```

**Verificación de los requisitos:**

<!-- Un renglón por cada requisito de la sección anterior. Si el requisito no se valida con un
     test, di con qué se ha comprobado. Copia lo que ya declaraste en la ficha de docs/features/. -->

| Requisito | Se validó con | Resultado |
|-----------|---------------|-----------|
|           |               |           |

## Checklist

<!-- Marca solo lo que hayas verificado de verdad. Si un punto no aplica, déjalo sin marcar y
     explica por qué en la descripción: un punto sin marcar y justificado es información útil;
     uno marcado a ciegas es ruido que además tapa el problema. -->

- [ ] Los documentos afectados en `docs/` están actualizados
- [ ] La ficha de `docs/features/` está en estado **Verificada** (si este PR cierra una feature)
- [ ] Hay una entrada en `changelog/` con este cambio
- [ ] La sección "Evidencia" contiene salida real de comandos, no una descripción de lo que pasaría
- [ ] Se ha ejecutado `/security-review` si hay cambios sensibles
