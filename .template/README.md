# Carpeta interna de la plantilla

Todo lo que hay aquí pertenece a **la plantilla en sí**, no a los proyectos que la usan.

Su contenido:

- `changelog/` — historial de cambios de la propia plantilla (cómo ha ido evolucionando este
  andamiaje). No es el changelog de tu proyecto: ese vive en `changelog/`, en la raíz.
- `assets/` — los GIF del `README.md` de la plantilla y los scripts que los generan.

## Si estás usando la plantilla para un proyecto

Esta carpeta **se borra durante la inicialización** (ver la sección "Inicialización del proyecto"
en `CLAUDE.md`, o ejecuta `/init-proyecto`). Su presencia es la señal de que el repo todavía es
una plantilla sin adaptar.

```bash
rm -rf .template
```

## Si estás manteniendo la plantilla

Los cambios que hagas sobre el andamiaje (CLAUDE.md, docs vacíos, comandos, plantillas de
GitHub…) se registran en `.template/changelog/`, con el mismo formato que el protocolo de
`CLAUDE.md`. Así `changelog/` se mantiene limpio y quien use la plantilla no arrastra tu
historial al suyo.
