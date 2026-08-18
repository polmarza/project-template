#!/usr/bin/env python3
"""De la conversación al producto: el repositorio montándose solo."""

W, H = 1200, 620
BG = "#faf8f5"; TARJETA = "#ffffff"; BORDE = "#e8e3da"
TINTA = "#2c2c33"; TENUE = "#938d80"; SUAVE = "#b8b2a5"
AZUL = "#4a63c8"; VERDE = "#4f9563"; AMBAR = "#c8933f"; ROJO = "#c8635c"
FAM = "Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "Menlo, monospace"

FASES = [
    ("Conversación",   "EL AGENTE PREGUNTA ANTES DE ESCRIBIR"),
    ("Inicialización", "DEJA DE SER UNA PLANTILLA"),
    ("Acuerdo",        "QUÉ SE CONSTRUYE Y CÓMO SE VALIDA"),
    ("Construcción",   "SOBRE LO ACORDADO"),
    ("Validación",     "TESTS SOBRE EL CÓDIGO REAL"),
    ("Cierre",         "PR CON EVIDENCIA, CI EN VERDE"),
]

# (sangría, nombre, tipo, nace, muere, nota_por_fase)
FILAS = [
    (0, ".template/",              "dir",  0, 2, {}),
    (0, "CLAUDE.md",               "file", 0, 9, {2: ("rellenado", AZUL)}),
    (0, "README.md",               "file", 0, 9, {2: ("reescrito", AZUL)}),
    (0, "changelog/",              "dir",  6, 9, {}),
    (1, "2026-08-18_exportar.md",  "file", 6, 9, {}),
    (0, "docs/",                   "dir",  0, 9, {}),
    (1, "prd.md",                  "file", 0, 9, {0: ("vacío", SUAVE), 1: ("M-01 · M-02 · M-03", AZUL)}),
    (1, "architecture.md",         "file", 0, 9, {0: ("vacío", SUAVE), 1: None}),
    (1, "design-system.md",        "file", 0, 9, {0: ("vacío", SUAVE), 1: None}),
    (1, "data-model.md",           "file", 0, 9, {0: ("vacío", SUAVE), 1: None}),
    (1, "features/",               "dir",  3, 9, {}),
    (2, "exportar-coleccion.md",   "ficha",3, 9, {}),
    (0, "src/app/exportar/",       "dir",  4, 9, {}),
    (1, "route.ts",                "file", 4, 9, {}),
    (0, "tests/",                  "dir",  5, 9, {}),
    (1, "exportar.spec.ts",        "file", 5, 9, {}),
]
PILL = {3: ("Acordada", TENUE, "#f2efe9"), 4: ("En construcción", AMBAR, "#fbf4e6"),
        5: ("Verificada", VERDE, "#eef7f1"), 6: ("Verificada", VERDE, "#eef7f1")}


def glifo(tipo, x, y, c):
    g = f'<g stroke="{c}" stroke-width="1.3" fill="none" stroke-linejoin="round">'
    if tipo == "dir":
        g += f'<path d="M{x} {y+2} h5 l1.6 2 h6.4 v8 h-13 z"/>'
    elif tipo == "ficha":
        g += f'<path d="M{x+1} {y} h9 l2.5 2.5 v9.5 h-11.5 z"/><path d="M{x+3.5} {y+5} h6 M{x+3.5} {y+8} h6"/>'
    else:
        g += f'<path d="M{x+1} {y} h7 l3 3 v9 h-10 z"/>'
    return g + "</g>"


def pastilla(x, y, texto, color, fondo, tam=9):
    an = len(texto) * tam * 0.6 + 18
    return (f'<g><rect x="{x}" y="{y-10}" width="{an:.0f}" height="17" rx="8.5" fill="{fondo}" '
            f'stroke="{color}" stroke-opacity="0.28"/>'
            f'<text x="{x+an/2:.0f}" y="{y+2}" text-anchor="middle" font-family="{FAM}" '
            f'font-size="{tam}" font-weight="600" letter-spacing="0.4" fill="{color}">{texto}</text></g>')


def svg(fase=6):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
         f'<rect width="{W}" height="{H}" fill="{BG}"/>')

    # ── Raíl de fases ──
    rx, ry, paso = 92, 108, 74
    s += f'<line x1="{rx}" y1="{ry}" x2="{rx}" y2="{ry + paso*5}" stroke="{BORDE}" stroke-width="2"/>'
    if fase >= 1:
        s += (f'<line x1="{rx}" y1="{ry}" x2="{rx}" y2="{ry + paso*min(fase-1,5)}" '
              f'stroke="{AZUL}" stroke-width="2"/>')
    for i, (tit, sub) in enumerate(FASES):
        y = ry + i * paso
        act, hecha = (fase == i + 1), (fase > i + 1)
        col = AZUL if (act or hecha) else SUAVE
        s += f'<circle cx="{rx}" cy="{y}" r="{8 if act else 5.5}" fill="{TARJETA}" stroke="{col}" stroke-width="2"/>'
        if act or hecha:
            s += f'<circle cx="{rx}" cy="{y}" r="{3.5 if act else 2.5}" fill="{col}"/>'
        s += (f'<text x="{rx+26}" y="{y+1}" font-family="{FAM}" font-size="14.5" '
              f'font-weight="{700 if act else 500}" fill="{TINTA if (act or hecha) else SUAVE}">{tit}</text>')
        s += (f'<text x="{rx+26}" y="{y+17}" font-family="{FAM}" font-size="8.5" font-weight="600" '
              f'letter-spacing="0.9" fill="{TENUE if act else SUAVE}" '
              f'opacity="{1 if act else 0.55}">{sub}</text>')

    # ── El repositorio ──
    cx, cy, cw = 450, 62, 660
    visibles = [f for f in FILAS if f[3] <= fase and (f[4] > fase or f[4] == fase)]
    ch = 44 + len(visibles) * 27 + 20
    s += f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="14" fill="{TARJETA}" stroke="{BORDE}"/>'
    s += f'<line x1="{cx}" y1="{cy+36}" x2="{cx+cw}" y2="{cy+36}" stroke="{BORDE}"/>'
    for i, c in enumerate(["#e8a49f", "#e5c98a", "#a8cdb0"]):
        s += f'<circle cx="{cx+22+i*17}" cy="{cy+18}" r="4.5" fill="{c}"/>'
    s += (f'<text x="{cx+cw-20}" y="{cy+22}" text-anchor="end" font-family="{MONO}" font-size="10" '
          f'fill="{SUAVE}">mi-proyecto</text>')

    y = cy + 62
    for sang, nom, tipo, nace, muere, notas in visibles:
        muriendo = (muere == fase)
        nuevo = (nace == fase and fase > 0)
        col = ROJO if muriendo else (TINTA if tipo != "dir" else TENUE)
        x = cx + 24 + sang * 20
        if nuevo:
            s += f'<rect x="{cx+12}" y="{y-14}" width="{cw-24}" height="24" rx="6" fill="#eef1f8"/>'
            s += f'<rect x="{cx+12}" y="{y-14}" width="2.5" height="24" rx="1.2" fill="{AZUL}"/>'
        s += glifo(tipo, x, y - 9, ROJO if muriendo else (TENUE if tipo == "dir" else SUAVE))
        s += (f'<text x="{x+20}" y="{y}" font-family="{MONO}" font-size="12.5" fill="{col}" '
              f'{"text-decoration=" + chr(34) + "line-through" + chr(34) if muriendo else ""}>{nom}</text>')
        if muriendo:
            an = len(nom) * 7.5
            s += f'<line x1="{x+20}" y1="{y-4}" x2="{x+20+an}" y2="{y-4}" stroke="{ROJO}" stroke-width="1.2"/>'
            s += pastilla(x + 26 + an, y - 4, "se borra", ROJO, "#fdf1f0", 8.5)
        elif tipo == "ficha" and fase in PILL:
            t, c1, c2 = PILL[fase]
            s += pastilla(x + 26 + len(nom) * 7.5, y - 4, t, c1, c2)
        else:
            claves = [k for k in notas if k <= fase]
            nota = notas[max(claves)] if claves else None
            if nota:
                s += (f'<text x="{x+26+len(nom)*7.5:.0f}" y="{y}" font-family="{FAM}" font-size="10" '
                      f'font-style="italic" fill="{nota[1]}">{nota[0]}</text>')
        y += 27

    if fase >= 6:
        s += pastilla(cx + 24, cy + ch + 26, "CI  ·  cobertura verificada", VERDE, "#eef7f1", 10.5)
    return s + "</svg>"


if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w", encoding="utf-8").write(svg(int(sys.argv[2]) if len(sys.argv) > 2 else 6))
