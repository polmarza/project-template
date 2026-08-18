Crea una nueva entrada en `changelog/` siguiendo el protocolo del proyecto.

1. Usa la fecha y hora actuales para nombrar el archivo: `YYYY-MM-DD_HH-MM_descripcion-breve.md`
2. Si el usuario no ha indicado qué cambio registrar, pregúntale.
3. Rellena las tres secciones obligatorias: qué se hizo, qué archivos se modificaron, por qué.
4. Rellena el campo `Requisitos` con los IDs del PRD que este cambio deja terminados (`M-01`, `S-02`…). Si es un cambio interno —refactor, tooling, documentación— escribe "ninguno"; no lo dejes en blanco.
5. Si el cambio cierra una feature, comprueba que su ficha de `docs/features/` está en estado **Verificada** antes de escribir la entrada.
6. Si el cambio afecta algún documento de `docs/`, recuérdale al usuario que hay que actualizarlo en esta misma sesión.

Si existe la carpeta `.template/` y el cambio es sobre la plantilla en sí (CLAUDE.md, docs vacíos, comandos, plantillas de GitHub), escribe la entrada en `.template/changelog/` en lugar de `changelog/`. La carpeta `changelog/` se reserva para el proyecto que use la plantilla.
