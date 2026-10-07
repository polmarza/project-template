---
name: mejora
description: Añade una idea al backlog de mejoras/backlog.md sin interrumpir el trabajo en curso. Úsala cuando surja una idea que no entra en la tarea o el sprint actual y no se quiere perder.
argument-hint: "[título de la mejora]"
---

Añade una nueva idea al backlog en `mejoras/backlog.md`.

Pregunta al usuario lo siguiente si no lo ha indicado ya:
1. ¿Cuál es el título de la mejora?
2. ¿A qué área pertenece? (Frontend / Backend / UX / Infraestructura / Negocio)
3. ¿Cuál es la prioridad estimada? (Alta / Media / Baja)
4. ¿De dónde surgió la idea?

Lee el archivo para determinar el número correlativo del siguiente `[MEJORA-XX]`.

Añade la entrada al final del archivo con este formato:

### [MEJORA-XX] Título
**Área:** ...
**Prioridad estimada:** ...
**Origen:** ...

Descripción breve de la mejora y por qué aportaría valor.
