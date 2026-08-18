#!/usr/bin/env python3
"""Renderiza una sesión de terminal a GIF. Frames con Pillow, ensamblado con ffmpeg."""
import subprocess, sys, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FUENTE = "/System/Library/Fonts/SFNSMono.ttf"
TAM = 15
INTERLINEA = 24
PAD_X, PAD_Y = 26, 20
CHROME = 38

C = {
    "fondo":   "#151723",
    "chrome":  "#1d2030",
    "borde":   "#2a2e42",
    "texto":   "#c5cee0",
    "tenue":   "#6b7594",
    "prompt":  "#4fd6be",
    "cmd":     "#eef1f8",
    "fallo":   "#ff757f",
    "aviso":   "#ffc777",
    "ok":      "#c3e88d",
    "ruta":    "#82aaff",
}

fuente = ImageFont.truetype(FUENTE, TAM)
_probe = Image.new("RGB", (10, 10)); _d = ImageDraw.Draw(_probe)
CHAR_W = _d.textlength("M", font=fuente)


def estilar(linea):
    """Una línea de salida real -> tramos coloreados. No altera el texto."""
    t = linea
    if t.startswith("$ "):
        resto = t[2:]
        if resto.startswith("#"):
            return [("$ ", C["prompt"]), (resto, C["tenue"])]
        return [("$ ", C["prompt"]), (resto, C["cmd"])]
    s = t.strip()
    if s.startswith("FALLO"):
        i = t.index("FALLO")
        return [(t[:i], C["texto"]), ("FALLO", C["fallo"]), (t[i + 5:], C["texto"])]
    if s.startswith("ATENCIÓN"):
        i = t.index("ATENCIÓN")
        return [(t[:i], C["texto"]), ("ATENCIÓN", C["aviso"]), (t[i + 8:], C["texto"])]
    if s.startswith("docs/") or s.startswith("scripts/"):
        return [(t, C["ruta"])]
    if s.startswith("Todo en orden") or s.startswith("Sin fallos"):
        return [(t, C["ok"])]
    if s.endswith("fallo(s).") or " fallo(s)" in s:
        return [(t, C["fallo"])]
    if s.startswith("Verificación de cobertura"):
        return [(t, C["tenue"])]
    return [(t, C["texto"])]


def pintar(lineas, cursor_en=None, ancho=None, alto=None):
    img = Image.new("RGB", (ancho, alto), C["fondo"])
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, ancho, CHROME], fill=C["chrome"])
    d.line([(0, CHROME), (ancho, CHROME)], fill=C["borde"])
    for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        cx = 22 + i * 20
        d.ellipse([cx - 6, CHROME // 2 - 6, cx + 6, CHROME // 2 + 6], fill=col)

    y = CHROME + PAD_Y
    for li, linea in enumerate(lineas):
        x = PAD_X
        for texto, color in estilar(linea):
            d.text((x, y), texto, font=fuente, fill=color)
            x += d.textlength(texto, font=fuente)
        if cursor_en == li:
            d.rectangle([x + 1, y + 2, x + CHAR_W, y + TAM + 4], fill=C["texto"])
        y += INTERLINEA
    return img


def render(guion, salida, fps=16):
    """guion: lista de ('cmd', txt) | ('out', [lineas]) | ('esperar', frames)"""
    todas = []
    for tipo, val in guion:
        if tipo == "cmd":
            todas.append("$ " + val)
        elif tipo == "out":
            todas.extend(val)
    max_chars = max((len(l) for l in todas), default=60)
    ancho = int(PAD_X * 2 + max_chars * CHAR_W) + 8
    alto = CHROME + PAD_Y * 2 + len(todas) * INTERLINEA

    frames, lineas = [], []
    for tipo, val in guion:
        if tipo == "cmd":
            lineas.append("$ ")
            for i in range(0, len(val) + 1, 2):
                lineas[-1] = "$ " + val[:i]
                frames.append(pintar(lineas, len(lineas) - 1, ancho, alto))
            lineas[-1] = "$ " + val
            for _ in range(5):
                frames.append(pintar(lineas, len(lineas) - 1, ancho, alto))
        elif tipo == "out":
            for linea in val:
                lineas.append(linea)
                frames.append(pintar(lineas, None, ancho, alto))
        elif tipo == "esperar":
            for _ in range(val):
                frames.append(pintar(lineas, None, ancho, alto))
    return frames, ancho, alto, fps


def a_gif(frames, destino, fps):
    tmp = Path(destino).parent / "_frames"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    for i, f in enumerate(frames):
        f.save(tmp / f"{i:04d}.png")
    paleta = tmp / "pal.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps),
                    "-i", str(tmp / "%04d.png"),
                    "-vf", "palettegen=max_colors=128:stats_mode=diff", str(paleta)], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps),
                    "-i", str(tmp / "%04d.png"), "-i", str(paleta),
                    "-lavfi", "paletteuse=dither=none:diff_mode=rectangle",
                    "-loop", "0", str(destino)], check=True)
    subprocess.run(["magick", str(destino), "-layers", "Optimize", str(destino)], check=True)
    shutil.rmtree(tmp)
