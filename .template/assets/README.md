# Imágenes del README

Los GIF que ilustran el `README.md` de la plantilla, y los scripts que los generan.

Viven aquí, dentro de `.template/`, por el mismo motivo que el changelog de la plantilla: son
material del andamiaje, no del producto. Al inicializar un proyecto esta carpeta se borra entera y
el README se reescribe, así que las imágenes y sus referencias desaparecen juntas.

| Archivo | Qué muestra |
|---------|-------------|
| `comparativa.gif` | Sin plantilla frente a con plantilla |
| `flujo.gif` | El repositorio montándose fase a fase |
| `cobertura.gif` | El script bloqueando un test prometido que no existe |
| `excepcion.gif` | El script rechazando una excepción sin justificar |

## Regenerarlos

Hace falta Python con Pillow, `rsvg-convert` y `ffmpeg`. Los dos diagramas se dibujan en SVG y se
rasterizan; los de terminal se componen frame a frame a partir de **salida real** del script.

```bash
python3 gen-comparativa.py salida.svg   # diagrama de carriles
python3 gen-flujo.py salida.svg [fase]  # repositorio por fases (0-6)
```

`gen-terminal.py` es una librería: se importa y se le pasa un guion de comandos y su salida.

**Regla al tocarlos:** el texto que aparece en los GIF de terminal se copia de una ejecución de
verdad. Si cambias el script y cambian sus mensajes, hay que volver a ejecutarlo y regenerar el
GIF, no editar el texto a mano. Un GIF que enseña una salida que el programa ya no produce miente
igual que una casilla marcada sin comprobar.
