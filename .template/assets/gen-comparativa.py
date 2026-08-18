#!/usr/bin/env python3
"""Genera el diagrama 'sin plantilla / con plantilla' en SVG."""

W, H = 1200, 560
BG = "#faf8f5"
CARRIL_MAL = "#f3efe9"; BORDE_MAL = "#e7e0d5"
CARRIL_BIEN = "#eef1f8"; BORDE_BIEN = "#dde3f2"
TARJETA = "#ffffff"; BORDE_T = "#e8e3da"
TINTA = "#2c2c33"; TENUE = "#938d80"
ROJO = "#c8635c"; AZUL = "#4a63c8"; VERDE = "#4f9563"
FAM = "Helvetica Neue, Helvetica, Arial, sans-serif"

MAL = [
    ("chat",  "Sesión nueva",        "CONTEXTO CERO",        None),
    ("doc",   "Le explicas todo",    "OTRA VEZ",             None),
    ("code",  "Escribe a ciegas",    "SIN PREGUNTAR",        None),
    ("x",     "No era eso",          "REHACER",              ROJO),
    ("quest", "Decisiones perdidas", "NADIE SE ACUERDA",     None),
    ("box",   "Entregado",           "SIN SABER SI CUMPLE",  None),
]
BIEN = [
    ("doc",   "Sesión nueva",          "LEE docs/",                  None),
    ("ficha", "Ficha de feature",      "QUÉ Y CÓMO SE VALIDA",       None),
    ("code",  "Construye",             "SOBRE LO ACORDADO",          None),
    ("test",  "Tests del código",      "TRAS IMPLEMENTAR",           None),
    ("pr",    "PR con evidencia",      "SALIDA REAL PEGADA",         None),
    ("check", "Mergeado",              "COBERTURA VERIFICADA",       VERDE),
]


def icono(tipo, x, y, c):
    """Icono de línea 22x22 dibujado desde (x,y). Trazo fino, sin relleno."""
    s = f'<g stroke="{c}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round">'
    if tipo == "chat":
        s += f'<path d="M{x+2} {y+4} h18 v12 h-9 l-5 4 v-4 h-4 z"/>'
    elif tipo == "doc":
        s += f'<path d="M{x+4} {y+2} h9 l5 5 v13 h-14 z"/><path d="M{x+7} {y+11} h7 M{x+7} {y+15} h7"/>'
    elif tipo == "code":
        s += f'<path d="M{x+8} {y+6} l-5 5 l5 5 M{x+14} {y+6} l5 5 l-5 5"/>'
    elif tipo == "x":
        s += f'<circle cx="{x+11}" cy="{y+11}" r="8"/><path d="M{x+8} {y+8} l6 6 M{x+14} {y+8} l-6 6"/>'
    elif tipo == "quest":
        s += f'<circle cx="{x+11}" cy="{y+11}" r="8"/><path d="M{x+8.5} {y+8.5} a2.5 2.5 0 1 1 2.5 3 v1.5"/><path d="M{x+11} {y+15.5} v0.5"/>'
    elif tipo == "box":
        s += f'<path d="M{x+3} {y+6} h16 v12 h-16 z"/><path d="M{x+3} {y+10} h16"/>'
    elif tipo == "ficha":
        s += f'<path d="M{x+4} {y+3} h14 v16 h-14 z"/><path d="M{x+7} {y+8} h8 M{x+7} {y+12} h8 M{x+7} {y+15.5} h4"/>'
    elif tipo == "test":
        s += f'<path d="M{x+4} {y+11} l4 4 l9 -9"/><path d="M{x+3} {y+4} h16" opacity="0.35"/>'
    elif tipo == "pr":
        s += f'<circle cx="{x+6}" cy="{y+6}" r="2.6"/><circle cx="{x+6}" cy="{y+17}" r="2.6"/><circle cx="{x+16}" cy="{y+6}" r="2.6"/><path d="M{x+6} {y+8.6} v5.8 M{x+16} {y+8.6} v3 a3 3 0 0 1 -3 3 h-4"/>'
    elif tipo == "check":
        s += f'<circle cx="{x+11}" cy="{y+11}" r="8"/><path d="M{x+7.5} {y+11} l2.5 2.5 l5 -5.5"/>'
    return s + "</g>"


def tarjeta(x, y, w, h, ic, titulo, sub, acento):
    col = acento or TINTA
    fondo_ic = "#fdf1f0" if acento == ROJO else ("#eef7f1" if acento == VERDE else "#f6f4f0")
    borde = "#f0d9d7" if acento == ROJO else ("#d8ebdf" if acento == VERDE else BORDE_T)
    s = f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" fill="{TARJETA}" stroke="{borde}"/>'
    s += f'<rect x="{x+16}" y="{y+16}" width="34" height="34" rx="9" fill="{fondo_ic}"/>'
    s += icono(ic, x + 22, y + 22, col)
    s += (f'<text x="{x+16}" y="{y+72}" font-family="{FAM}" font-size="12.5" font-weight="600" '
          f'fill="{col}">{titulo}</text>')
    s += (f'<text x="{x+16}" y="{y+90}" font-family="{FAM}" font-size="8.5" font-weight="600" '
          f'letter-spacing="0.9" fill="{TENUE}">{sub}</text>')
    return s + "</g>"


def carril(y0, etiqueta, pasos, fondo, borde, color_et, texto_et, pie, color_pie, revelados=None):
    n = len(pasos)
    x0, ancho_c = 50, W - 100
    s = f'<rect x="{x0}" y="{y0}" width="{ancho_c}" height="212" rx="20" fill="{fondo}" stroke="{borde}"/>'
    s += f'<rect x="{x0+22}" y="{y0-13}" width="{len(etiqueta)*7.4+30:.0f}" height="26" rx="13" fill="{color_et}"/>'
    s += (f'<text x="{x0+37}" y="{y0+4}" font-family="{FAM}" font-size="10" font-weight="700" '
          f'letter-spacing="1.1" fill="{texto_et}">{etiqueta}</text>')

    tw, hueco = 168, 18
    total = n * tw + (n - 1) * hueco
    sx = x0 + (ancho_c - total) / 2
    ty = y0 + 46
    for i, (ic, tit, sub, ac) in enumerate(pasos):
        tx = sx + i * (tw + hueco)
        vis = revelados is None or i < revelados
        op = 1 if vis else 0.13
        s += f'<g opacity="{op}">' + tarjeta(tx, ty, tw, 108, ic, tit, sub, ac) + "</g>"
        if i < n - 1:
            cx1, cx2 = tx + tw, tx + tw + hueco
            conec = revelados is None or i < revelados - 1
            s += (f'<line x1="{cx1+2}" y1="{ty+54}" x2="{cx2-2}" y2="{ty+54}" stroke="{borde}" '
                  f'stroke-width="1.4" opacity="{1 if conec else 0.13}"/>')
            s += (f'<circle cx="{(cx1+cx2)/2}" cy="{ty+54}" r="2.4" fill="{color_et}" '
                  f'opacity="{0.85 if conec else 0.13}"/>')

    py = ty + 132
    completo = revelados is None or revelados >= n
    s += f'<g opacity="{1 if completo else 0.13}">'
    if pie[0] == "loop":
        s += (f'<line x1="{sx+52}" y1="{py+2}" x2="{sx+total-30}" y2="{py+2}" stroke="{color_pie}" '
              f'stroke-width="1.4" stroke-dasharray="5 4"/>')
        s += (f'<path d="M{sx+44} {py+2} l8 -4.5 l0 9 z" fill="{color_pie}"/>')
    else:
        s += f'<line x1="{sx+40}" y1="{py+2}" x2="{sx+total-40}" y2="{py+2}" stroke="{color_pie}" stroke-width="1.4"/>'
    s += (f'<rect x="{W/2 - len(pie[1])*3.3 - 14:.0f}" y="{py-8}" width="{len(pie[1])*6.6+28:.0f}" height="20" '
          f'rx="10" fill="{BG}"/>')
    s += (f'<text x="{W/2}" y="{py+5}" text-anchor="middle" font-family="{FAM}" font-size="9" '
          f'font-weight="700" letter-spacing="1.1" fill="{color_pie}">{pie[1]}</text>')
    return s + "</g>"


def svg(rev_mal=None, rev_bien=None):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
         f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    s += carril(56, "SIN PLANTILLA", MAL, CARRIL_MAL, BORDE_MAL, "#6f6759", "#ffffff",
                ("loop", "SE REPITE EN CADA SESIÓN, CON CADA AGENTE"), ROJO, rev_mal)
    s += carril(330, "CON PLANTILLA", BIEN, CARRIL_BIEN, BORDE_BIEN, AZUL, "#ffffff",
                ("linea", "EL CONTEXTO VIVE EN EL REPO, NO EN LA CONVERSACIÓN"), AZUL, rev_bien)
    return s + "</svg>"


if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w", encoding="utf-8").write(svg())
