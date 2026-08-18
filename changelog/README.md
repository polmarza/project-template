# Changelog

Registro estructurado de cada cambio importante del proyecto: qué se hizo, qué se modificó y por qué.

Esta carpeta **empieza vacía a propósito**. La plantilla no arrastra aquí su propio historial:
los cambios de la plantilla viven en `.template/changelog/` y esa carpeta se borra al inicializar
el proyecto.

---

## Cómo añadir una entrada

Usa `/changelog`. El agente crea el archivo con la fecha y hora reales y rellena las secciones.

**Nombre del archivo:** `YYYY-MM-DD_HH-MM_descripcion-breve.md`

**Contenido mínimo:**

```markdown
# [Descripción breve del cambio]

**Fecha:** YYYY-MM-DD HH:MM
**Tipo:** Feature / Fix / Refactor / Migración / Documentación / Configuración
**Requisitos:** [IDs del PRD que cierra: M-01, S-02. "Ninguno" si es un cambio interno]

## Qué se hizo
[Descripción de lo que se implementó o modificó]

## Qué se modificó
[Lista de archivos afectados]

## Por qué
[Contexto o motivación del cambio]
```

---

Este archivo es la única excepción: no es una entrada, es la explicación del formato.
Puedes conservarlo o borrarlo cuando el changelog tenga entradas reales.
