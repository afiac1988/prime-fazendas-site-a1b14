#!/usr/bin/env python3
"""
Prime Fazendas — gerador de arte SVG.

Produz paisagens editoriais em camadas, na paleta da marca, para ocupar
os espaços de fotografia enquanto o material fotográfico real não entra.
Cada arquivo tem um equivalente fotográfico documentado no README.
"""
import math
import os
import random

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
os.makedirs(OUT, exist_ok=True)

AZUL = "#0B1D2A"
VERDE = "#263B32"
MARFIM = "#F4F1E9"
DOURADO = "#B79A5B"


def catmull(points, closed=True, tension=1.0):
    """Converte uma lista de pontos numa curva suave (Catmull-Rom -> Bezier)."""
    n = len(points)
    if n < 3:
        return ""
    d = [f"M {points[0][0]:.1f} {points[0][1]:.1f}"]
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = points[(i - 1) % n] if closed else points[max(i - 1, 0)]
        p1 = points[i % n]
        p2 = points[(i + 1) % n]
        p3 = points[(i + 2) % n] if closed else points[min(i + 2, n - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6 * tension, p1[1] + (p2[1] - p0[1]) / 6 * tension)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6 * tension, p2[1] - (p3[1] - p1[1]) / 6 * tension)
        d.append(
            f"C {c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
        )
    if closed:
        d.append("Z")
    return " ".join(d)


def ridge(w, y_base, amp, seed, steps=14, drop=0.0):
    """Silhueta de relevo suave para o horizonte."""
    rnd = random.Random(seed)
    pts = [(0, y_base + rnd.uniform(-amp, amp))]
    for i in range(1, steps + 1):
        x = w * i / steps
        y = y_base + rnd.uniform(-amp, amp) + drop * (i / steps)
        pts.append((x, y))
    d = [f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"]
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        mx = (x0 + x1) / 2
        d.append(f"C {mx:.1f} {y0:.1f} {mx:.1f} {y1:.1f} {x1:.1f} {y1:.1f}")
    d.append(f"L {w} {y_base + 4000} L 0 {y_base + 4000} Z")
    return " ".join(d)


def furrows(w, h, horizon, seed, rows=26, color="#000", op=0.16):
    """Linhas de plantio em perspectiva, convergindo para o ponto de fuga."""
    rnd = random.Random(seed)
    vx = w * 0.52
    out = []
    for i in range(rows):
        t = i / (rows - 1)
        # distribuição não linear: mais densa perto do horizonte
        base_x = -w * 0.9 + (w * 2.8) * (t ** 1.35 if t < 0.5 else 1 - (1 - t) ** 1.35)
        jitter = rnd.uniform(-6, 6)
        d = (
            f"M {vx:.1f} {horizon:.1f} "
            f"L {base_x + jitter:.1f} {h + 40:.1f} "
            f"L {base_x + jitter + w * 0.035:.1f} {h + 40:.1f} Z"
        )
        out.append(f'<path d="{d}" fill="{color}" opacity="{op:.3f}"/>')
    return "\n".join(out)


def tree(x, y, s, color, op, rnd=None):
    """Silhueta de árvore de cerrado — copa irregular, tronco levemente inclinado."""
    r = rnd or random.Random(int(x * 7 + y * 13 + s))
    lean = r.uniform(-0.09, 0.09) * s
    ch = s * r.uniform(0.62, 0.82)
    parts = [
        f'<g opacity="{op:.2f}" fill="{color}">',
        f'<path d="M {x - s*0.045:.1f} {y:.1f} L {x - s*0.03 + lean:.1f} {y - ch:.1f} '
        f'L {x + s*0.03 + lean:.1f} {y - ch:.1f} L {x + s*0.045:.1f} {y:.1f} Z"/>',
    ]
    cx = x + lean
    cy = y - ch
    for i in range(r.randint(3, 5)):
        ox = r.uniform(-0.38, 0.38) * s
        oy = r.uniform(-0.16, 0.10) * s
        rx = r.uniform(0.24, 0.42) * s
        ry = rx * r.uniform(0.52, 0.74)
        parts.append(f'<ellipse cx="{cx+ox:.1f}" cy="{cy+oy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}"/>')
    parts.append("</g>")
    return "".join(parts)


def eucalipto(x, y, s, color, op):
    """Silhueta colunar, para talhões de reflorestamento."""
    return (
        f'<g opacity="{op:.2f}" fill="{color}">'
        f'<rect x="{x - s*0.022:.1f}" y="{y - s*0.98:.1f}" width="{s*0.044:.1f}" height="{s*0.98:.1f}"/>'
        f'<path d="M {x:.1f} {y - s*1.12:.1f} C {x + s*0.17:.1f} {y - s*0.86:.1f} {x + s*0.13:.1f} {y - s*0.5:.1f} '
        f'{x:.1f} {y - s*0.36:.1f} C {x - s*0.13:.1f} {y - s*0.5:.1f} {x - s*0.17:.1f} {y - s*0.86:.1f} '
        f'{x:.1f} {y - s*1.12:.1f} Z"/>'
        f"</g>"
    )


def defs(uid, sky, glow_x, glow_y, glow_r, warm):
    return f"""
  <defs>
    <linearGradient id="sky{uid}" x1="0" y1="0" x2="0" y2="1">
      {sky}
    </linearGradient>
    <radialGradient id="sun{uid}" cx="{glow_x}" cy="{glow_y}" r="{glow_r}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{warm}" stop-opacity=".95"/>
      <stop offset=".45" stop-color="{warm}" stop-opacity=".38"/>
      <stop offset="1" stop-color="{warm}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="haze{uid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{warm}" stop-opacity=".28"/>
      <stop offset="1" stop-color="{warm}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="deep{uid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{AZUL}" stop-opacity="0"/>
      <stop offset="1" stop-color="{AZUL}" stop-opacity=".55"/>
    </linearGradient>
    <linearGradient id="chao{uid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4C5940"/>
      <stop offset=".22" stop-color="#33452F"/>
      <stop offset=".6" stop-color="#22332A"/>
      <stop offset="1" stop-color="#13201B"/>
    </linearGradient>
    <filter id="grain{uid}" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="{uid}" result="n"/>
      <feColorMatrix type="saturate" values="0" in="n" result="g"/>
      <feComponentTransfer in="g" result="g2">
        <feFuncA type="linear" slope="0.14"/>
      </feComponentTransfer>
      <feBlend in="SourceGraphic" in2="g2" mode="overlay"/>
    </filter>
    <filter id="soft{uid}" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="14"/>
    </filter>
  </defs>"""


def landscape(path, w, h, *, uid, mood, motif, seed):
    """
    mood: 'aurora' (amanhecer), 'tarde' (fim de tarde), 'sereno' (dia claro)
    motif: 'lavoura' | 'pasto' | 'floresta' | 'agua' | 'planalto' | 'integracao'
    """
    rnd = random.Random(seed)
    horizon = h * (0.56 if motif != "planalto" else 0.52)

    if mood == "aurora":
        sky = (
            f'<stop offset="0" stop-color="{AZUL}"/>'
            f'<stop offset=".42" stop-color="#20415A"/>'
            f'<stop offset=".74" stop-color="#8C8267"/>'
            f'<stop offset="1" stop-color="#E8D6AE"/>'
        )
        warm = "#F0D9A6"
    elif mood == "tarde":
        sky = (
            f'<stop offset="0" stop-color="#122A3B"/>'
            f'<stop offset=".38" stop-color="#3C5163"/>'
            f'<stop offset=".72" stop-color="#B08F60"/>'
            f'<stop offset="1" stop-color="#EBCF9C"/>'
        )
        warm = "#E5BE7E"
    else:
        sky = (
            f'<stop offset="0" stop-color="#17394E"/>'
            f'<stop offset=".5" stop-color="#5C7A85"/>'
            f'<stop offset="1" stop-color="#DCD9C8"/>'
        )
        warm = "#EFE6CE"

    gx = w * rnd.uniform(0.28, 0.72)
    gy = horizon - h * 0.04
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">',
        defs(uid, sky, gx, gy, h * 0.72, warm),
        f'<g filter="url(#grain{uid})">',
        f'<rect width="{w}" height="{h}" fill="url(#sky{uid})"/>',
        f'<rect width="{w}" height="{h}" fill="url(#sun{uid})"/>',
    ]

    # nuvens longas e discretas
    for i in range(5):
        cy = horizon - h * rnd.uniform(0.12, 0.42)
        cw = w * rnd.uniform(0.22, 0.5)
        cx = w * rnd.uniform(0.0, 1.0)
        ch = h * rnd.uniform(0.006, 0.016)
        parts.append(
            f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{cw:.0f}" ry="{ch:.0f}" '
            f'fill="{MARFIM}" opacity="{rnd.uniform(0.06,0.16):.2f}" filter="url(#soft{uid})"/>'
        )

    # sol baixo
    parts.append(
        f'<circle cx="{gx:.0f}" cy="{gy:.0f}" r="{h*0.045:.0f}" fill="{warm}" opacity=".75" filter="url(#soft{uid})"/>'
    )

    # cadeias de relevo, com perspectiva atmosférica
    layers = [
        (horizon - h * 0.055, h * 0.012, "#6E7E7C", 0.42),
        (horizon - h * 0.022, h * 0.016, "#4A5C5A", 0.62),
        (horizon + h * 0.012, h * 0.020, "#33463F", 0.85),
    ]
    if motif == "planalto":
        layers.insert(0, (horizon - h * 0.10, h * 0.006, "#8996941", 0.0))
        layers = [l for l in layers if l[3] > 0]
    for i, (yb, amp, col, op) in enumerate(layers):
        parts.append(
            f'<path d="{ridge(w, yb, amp, seed + i * 7, steps=10 + i * 3)}" fill="{col}" opacity="{op}"/>'
        )

    # névoa junto ao horizonte
    parts.append(
        f'<rect x="0" y="{horizon - h*0.09:.0f}" width="{w}" height="{h*0.14:.0f}" fill="url(#haze{uid})"/>'
    )

    # chão, com gradiente e uma linha quente de luz rasante no horizonte
    parts.append(f'<rect x="0" y="{horizon:.0f}" width="{w}" height="{h - horizon:.0f}" fill="url(#chao{uid})"/>')
    parts.append(
        f'<rect x="0" y="{horizon - h*0.004:.1f}" width="{w}" height="{h*0.007:.1f}" fill="{warm}" opacity=".30"/>'
    )
    # talhões: parcelas de tonalidade ligeiramente distinta, quebrando a chapa
    for i in range(7):
        t0 = rnd.uniform(0.02, 0.75)
        t1 = min(t0 + rnd.uniform(0.06, 0.24), 0.98)
        y0 = horizon + (h - horizon) * (t0 ** 1.5)
        y1 = horizon + (h - horizon) * (t1 ** 1.5)
        sx = rnd.uniform(-0.15, 0.9)
        parts.append(
            f'<path d="M {w*sx:.0f} {y0:.0f} L {w*(sx+rnd.uniform(.25,.7)):.0f} {y0:.0f} '
            f'L {w*(sx+rnd.uniform(.3,.95)):.0f} {y1:.0f} L {w*(sx-rnd.uniform(.05,.3)):.0f} {y1:.0f} Z" '
            f'fill="{"#4E5B41" if i % 2 else "#1A2A22"}" opacity="{rnd.uniform(0.07,0.16):.2f}"/>'
        )

    if motif in ("lavoura", "integracao"):
        parts.append(furrows(w, h, horizon + h * 0.005, seed, rows=32, color="#0E1E19", op=0.22))
        parts.append(furrows(w, h, horizon + h * 0.005, seed + 3, rows=15, color=warm, op=0.06))
        if motif == "integracao":
            for i in range(6):
                t = rnd.uniform(0.2, 0.9)
                parts.append(
                    tree(rnd.uniform(0, w), horizon + (h - horizon) * (t ** 1.5),
                         28 + 120 * t, "#16261F", 0.5 + 0.4 * t, rnd)
                )
    elif motif == "pasto":
        for i in range(110):
            x = rnd.uniform(0, w)
            t = rnd.uniform(0, 1)
            y = horizon + (h - horizon) * (t ** 1.8)
            s = 2 + 18 * (t ** 1.6)
            parts.append(
                f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{s:.1f}" ry="{s*0.42:.1f}" fill="#16261F" opacity="{0.14+0.3*t:.2f}"/>'
            )
        for i in range(9):
            t = rnd.uniform(0.12, 0.95)
            parts.append(
                tree(rnd.uniform(0, w), horizon + (h - horizon) * (t ** 1.5),
                     30 + 150 * t, "#16261F", 0.5 + 0.4 * t, rnd)
            )
    elif motif == "floresta":
        for row in range(7):
            t = (row + 0.6) / 7
            y = horizon + (h - horizon) * (t ** 1.45)
            s = 30 + 210 * t
            n = max(int(30 / (1 + row * 0.6)), 4)
            for i in range(n + 1):
                x = (i + rnd.uniform(-0.22, 0.22)) * (w / max(n, 1))
                parts.append(eucalipto(x, y, s * rnd.uniform(0.88, 1.12), "#16261F", 0.32 + 0.55 * t))
    elif motif == "agua":
        parts.append(furrows(w, h, horizon + h * 0.005, seed, rows=18, color="#0E1E19", op=0.14))
        rw = h * 0.5
        pts = [
            (w * 1.05, horizon + h * 0.02),
            (w * 0.62, horizon + h * 0.10),
            (w * 0.44, horizon + h * 0.22),
            (w * 0.36, h * 1.05),
            (w * 0.62, h * 1.05),
            (w * 0.60, horizon + h * 0.24),
            (w * 0.74, horizon + h * 0.11),
            (w * 1.05, horizon + h * 0.05),
        ]
        d = "M " + " L ".join(f"{x:.0f} {y:.0f}" for x, y in pts) + " Z"
        parts.append(f'<path d="{d}" fill="{warm}" opacity=".30"/>')
        parts.append(f'<path d="{d}" fill="#8FA9B0" opacity=".45"/>')
    elif motif == "planalto":
        parts.append(furrows(w, h, horizon + h * 0.005, seed, rows=20, color="#0E1E19", op=0.15))
        for i in range(5):
            t = rnd.uniform(0.2, 0.9)
            parts.append(
                tree(rnd.uniform(0, w), horizon + (h - horizon) * (t ** 1.5),
                     26 + 120 * t, "#16261F", 0.5 + 0.4 * t, rnd)
            )

    # vinheta inferior, para o texto respirar sobre a imagem
    parts.append(f'<rect x="0" y="{h*0.45:.0f}" width="{w}" height="{h*0.55:.0f}" fill="url(#deep{uid})"/>')
    parts.append("</g></svg>")

    with open(os.path.join(OUT, path), "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    return path


# ---------------------------------------------------------------- marca
LOGO = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44" width="44" height="44" role="img" aria-label="Prime Fazendas">
  <rect x="1.6" y="1.6" width="40.8" height="40.8" rx="3" fill="none" stroke="{DOURADO}" stroke-width="1.1"/>
  <path d="M8 27.5c4.2-3.4 7.4-5.1 9.6-5.1 3.3 0 5 3.2 8.2 3.2 2.2 0 5.2-1.6 9-4.8" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
  <path d="M8 32.6h28" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" opacity=".55"/>
  <circle cx="29.4" cy="14.6" r="4.1" fill="none" stroke="{DOURADO}" stroke-width="1.1"/>
  <path d="M11 19.4V9.6h4.3a2.9 2.9 0 0 1 0 5.8H11" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

with open(os.path.join(OUT, "marca.svg"), "w", encoding="utf-8") as f:
    f.write(LOGO)

# ---------------------------------------------------------------- mapa
# Contorno derivado de coordenadas geográficas reais (projeção equirretangular).
# Longitude -74,0 a -34,8 / latitude +5,3 a -33,8.
LON0, LON1, LAT0, LAT1 = -74.0, -34.5, 5.4, -33.9
MW, MH = 560.0, 600.0


def proj(lon, lat):
    x = (lon - LON0) / (LON1 - LON0) * MW + 20
    y = (LAT0 - lat) / (LAT0 - LAT1) * MH + 20
    return (x, y)


brasil_geo = [
    (-60.2, 5.27), (-59.8, 4.60), (-59.0, 3.90), (-57.0, 2.00), (-55.9, 2.50),
    (-54.2, 2.20), (-51.9, 4.20), (-51.1, 3.90), (-50.4, 1.50), (-48.5, -1.40),
    (-46.5, -1.10), (-44.3, -2.50), (-41.8, -2.90), (-38.5, -3.70), (-37.0, -4.90),
    (-35.0, -5.20), (-34.8, -7.15), (-34.9, -8.05), (-35.7, -9.70), (-37.1, -11.0),
    (-38.5, -13.00), (-39.0, -14.80), (-39.25, -17.70), (-40.3, -20.30),
    (-41.0, -21.6), (-43.2, -23.00), (-46.3, -24.00), (-48.5, -25.50),
    (-48.5, -27.60), (-49.7, -29.30), (-52.1, -32.00), (-53.4, -33.75),
    (-55.6, -30.90), (-56.4, -29.4), (-54.6, -25.60),
    (-54.3, -24.00), (-55.7, -22.50), (-57.6, -19.00), (-58.4, -16.30),
    (-58.2, -14.50), (-60.2, -13.6), (-62.8, -12.5), (-65.3, -10.80),
    (-68.0, -10.90), (-70.0, -11.00), (-72.2, -9.5), (-73.98, -7.50),
    (-72.9, -5.10), (-69.9, -4.20), (-69.6, -1.20), (-67.1, 1.00),
    (-66.9, 1.20), (-64.6, 0.80), (-63.4, 2.20), (-61.4, 4.50),
]
matopiba_geo = [
    (-47.3, -2.60), (-45.3, -3.00), (-43.2, -5.60), (-41.6, -8.00),
    (-42.9, -10.60), (-43.4, -13.40), (-44.0, -15.40), (-46.2, -14.60),
    (-47.9, -13.40), (-48.9, -12.90), (-49.7, -11.00), (-50.3, -9.00),
    (-48.7, -6.40), (-47.8, -5.00), (-47.5, -3.60),
]
brasil = [proj(a, b) for a, b in brasil_geo]
matopiba = [proj(a, b) for a, b in matopiba_geo]
rot_ma = proj(-45.6, -5.4)
rot_pi = proj(-43.3, -8.4)
rot_to = proj(-48.4, -10.2)
rot_ba = proj(-45.2, -13.2)
def rotulo(p, texto, dx=0, dy=-11):
    return (
        f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="3.2" fill="{DOURADO}"/>'
        f'<text x="{p[0]+dx:.1f}" y="{p[1]+dy:.1f}">{texto}</text>'
    )


MAPA = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 640" role="img"
     aria-label="Representação esquemática do Brasil com a região do MATOPIBA destacada">
  <path d="{catmull(brasil, tension=0.5)}" fill="{VERDE}" fill-opacity=".07"
        stroke="{VERDE}" stroke-opacity=".38" stroke-width="1.3" stroke-linejoin="round"/>
  <path d="{catmull(matopiba, tension=0.5)}" fill="{DOURADO}" fill-opacity=".22"
        stroke="{DOURADO}" stroke-width="1.8" stroke-linejoin="round"/>
  <g font-family="Manrope, system-ui, sans-serif" font-size="15" font-weight="700"
     fill="{AZUL}" text-anchor="middle" letter-spacing=".5">
    {rotulo(rot_ma, "MA")}
    {rotulo(rot_pi, "PI", dx=10)}
    {rotulo(rot_to, "TO", dx=-10)}
    {rotulo(rot_ba, "BA")}
  </g>
</svg>"""
with open(os.path.join(OUT, "mapa-matopiba.svg"), "w", encoding="utf-8") as f:
    f.write(MAPA)

# ---------------------------------------------------------------- cenas
scenes = [
    ("hero-matopiba.svg", 2400, 1240, "aurora", "lavoura", 11),
    ("estado-ma.svg", 900, 700, "aurora", "lavoura", 31),
    ("estado-to.svg", 900, 700, "sereno", "pasto", 32),
    ("estado-pi.svg", 900, 700, "tarde", "planalto", 33),
    ("estado-ba.svg", 900, 700, "aurora", "integracao", 34),
    ("og.svg", 1200, 630, "aurora", "lavoura", 61),
]
for i, (name, w, h, mood, motif, seed) in enumerate(scenes):
    landscape(name, w, h, uid=100 + i, mood=mood, motif=motif, seed=seed)

print(f"{len(scenes) + 2} arquivos gerados em {OUT}")
