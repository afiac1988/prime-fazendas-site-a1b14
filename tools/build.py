#!/usr/bin/env python3
"""
Prime Fazendas — montagem das páginas estáticas.

O cabeçalho, o rodapé e o <head> vivem aqui, num só lugar. Cada página
declara apenas o próprio conteúdo. A saída é HTML puro, sem dependência
de build no servidor.

    python3 tools/build.py
"""
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://primefazendas.com"

# O brasão é a marca atual. Vem em WebP porque tem gradiente e brilho —
# vetor perderia o acabamento. Extraído dos one-pagers oficiais da Prime.
MARCA_IMG = (
    '<img class="marca__brasao" src="{base}assets/img/brasao-320.webp" alt="" '
    'width="320" height="326" decoding="async" fetchpriority="high">'
)

ZAP_SVG = """<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.15h-.01a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 2.2 0 4.27.86 5.83 2.42a8.19 8.19 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.79.97-.14.16-.29.18-.54.06-.25-.13-1.05-.39-1.99-1.23-.74-.66-1.24-1.47-1.38-1.72-.15-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.41.09-.17.04-.31-.02-.43-.06-.12-.56-1.35-.77-1.84-.2-.49-.4-.42-.55-.43h-.47c-.16 0-.43.06-.65.31-.22.25-.85.83-.85 2.03s.87 2.35.99 2.51c.12.16 1.71 2.61 4.15 3.66.58.25 1.03.4 1.38.51.58.19 1.11.16 1.53.1.47-.07 1.44-.59 1.64-1.16.2-.57.2-1.05.14-1.16-.06-.1-.22-.16-.47-.28Z"/></svg>"""

NAV_PT = [
    ("index.html", "Início"),
    ("oportunidades.html", "Oportunidades"),
    ("arrendamentos.html", "Arrendamentos"),
    ("radar-agro.html", "Radar Agro"),
    ("agenda-agro.html", "Agenda Agro"),
    ("quem-somos.html", "Quem Somos"),
    ("contato.html", "Contato"),
]

NAV_EN = [
    ("index.html", "Home"),
    ("opportunities.html", "Opportunities"),
    ("leases.html", "Leases"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

TXT = {
    "pt": {
        "pular": "Ir para o conteúdo",
        "menu": "Menu",
        "nav_rotulo": "Navegação principal",
        "cta": "Anuncie sua propriedade",
        "cta_href": "anuncie.html",
        "marca_aria": "Prime Fazendas, página inicial",
        "sobre": "Imobiliária rural especializada em compra, venda e arrendamento de propriedades no MATOPIBA e nas fronteiras agrícolas vizinhas.",
        "nav_titulo": "Navegação",
        "empresa": "Empresa",
        "contato": "Contato",
        "direitos": "Todos os direitos reservados.",
        "privacidade": "Privacidade",
        "termos": "Termos de uso",
        "outro_idioma": "English",
        "zap_msg": "Olá! Vim pelo site da Prime Fazendas e gostaria de falar com um especialista.",
    },
    "en": {
        "pular": "Skip to content",
        "menu": "Menu",
        "nav_rotulo": "Main navigation",
        "cta": "List your property",
        "cta_href": "contact.html",
        "marca_aria": "Prime Fazendas, home",
        "sobre": "Rural real estate firm specialised in the purchase, sale and lease of properties across Brazil\u2019s MATOPIBA region and neighbouring agricultural frontiers.",
        "nav_titulo": "Navigation",
        "empresa": "Company",
        "contato": "Contact",
        "direitos": "All rights reserved.",
        "privacidade": "Privacy",
        "termos": "Terms",
        "outro_idioma": "Português",
        "zap_msg": "Hello! I came from the Prime Fazendas website and would like to speak with a specialist.",
    },
}


def marca(base, href, aria, classe="marca"):
    return f"""<a class="{classe}" href="{base}{href}" aria-label="{aria}">
      {MARCA_IMG.format(base=base)}
      <span class="marca__texto">
        <span class="marca__nome">Prime Fazendas</span>
        <span class="marca__cauda">MATOPIBA</span>
      </span>
    </a>"""


def cabecalho(lang, atual, base):
    """`base` posiciona os assets. Os links de navegação são relativos à
    pasta do próprio idioma, por isso não recebem prefixo."""
    t = TXT[lang]
    itens = NAV_PT if lang == "pt" else NAV_EN
    home = "index.html"

    if lang == "pt":
        troca = "en/index.html"
        idioma = f'<span class="idioma"><a href="{base}index.html" aria-current="true">PT</a> <span aria-hidden="true">/</span> <a href="{base}en/index.html">EN</a></span>'
    else:
        troca = "../index.html"
        idioma = '<span class="idioma"><a href="../index.html">PT</a> <span aria-hidden="true">/</span> <a href="index.html" aria-current="true">EN</a></span>'

    links = "\n".join(
        f'        <li><a href="{href}"'
        + (' aria-current="page"' if href == atual else "")
        + f">{rotulo}</a></li>"
        for href, rotulo in itens
    )

    marca_topo = marca(base, home, t["marca_aria"]).replace(
        f'href="{base}{home}"', f'href="{home}"'
    )

    return f"""<header class="topo">
  <div class="env topo__int">
    {marca_topo}

    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-principal">
      <span class="menu-btn__barras" aria-hidden="true"><span></span><span></span><span></span></span>
      {t['menu']}
    </button>

    <nav class="nav" id="nav-principal" aria-label="{t['nav_rotulo']}">
      <ul class="nav__lista">
{links}
      </ul>
      <div class="nav__rodape">
        {idioma}
        <a class="btn" href="{t['cta_href']}">{t['cta']}</a>
      </div>
    </nav>

    <div class="topo__acoes">
      {idioma}
      <a class="btn" href="{t['cta_href']}">{t['cta']}</a>
    </div>
  </div>
</header>"""


def rodape(lang, base):
    t = TXT[lang]
    if lang == "pt":
        col_nav = """<li><a href="oportunidades.html">Oportunidades</a></li>
          <li><a href="arrendamentos.html">Arrendamentos</a></li>
          <li><a href="radar-agro.html">Radar Agro</a></li>
          <li><a href="agenda-agro.html">Agenda Agro</a></li>"""
        col_emp = """<li><a href="quem-somos.html">Quem Somos</a></li>
          <li><a href="anuncie.html">Anuncie sua propriedade</a></li>
          <li><a href="contato.html">Contato</a></li>
          <li><a href="en/index.html">English</a></li>"""
        legais = """<li><a href="privacidade.html">Privacidade</a></li>
        <li><a href="termos.html">Termos de uso</a></li>"""
    else:
        col_nav = """<li><a href="opportunities.html">Opportunities</a></li>
          <li><a href="leases.html">Leases</a></li>
          <li><a href="../radar-agro.html">Radar Agro</a></li>
          <li><a href="../agenda-agro.html">Agenda Agro</a></li>"""
        col_emp = """<li><a href="about.html">About</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="../index.html">Português</a></li>"""
        legais = """<li><a href="../privacidade.html">Privacy</a></li>
        <li><a href="../termos.html">Terms</a></li>"""

    return f"""<footer class="rodape">
  <div class="env">
    <div class="rodape__grade">
      <div>
        <a class="rodape__marca" href="index.html" aria-label="{t['marca_aria']}">
          <img src="{base}assets/img/brasao-320.webp" alt="Prime Fazendas" width="320" height="326" loading="lazy" decoding="async">
        </a>
        <p class="rodape__sobre">{t['sobre']}</p>
      </div>

      <div>
        <p class="rodape__titulo">{t['nav_titulo']}</p>
        <ul class="rodape__lista">
          {col_nav}
        </ul>
      </div>

      <div>
        <p class="rodape__titulo">{t['empresa']}</p>
        <ul class="rodape__lista">
          {col_emp}
        </ul>
      </div>

      <div>
        <p class="rodape__titulo">{t['contato']}</p>
        <ul class="rodape__lista">
          <li data-bloco><a data-campo="email" data-esconder-vazio href="#">&nbsp;</a></li>
          <li data-bloco><a data-campo="telefone" data-esconder-vazio href="#">&nbsp;</a></li>
          <li data-bloco><span data-campo="creci" data-esconder-vazio>&nbsp;</span></li>
          <li data-bloco><span data-campo="creci_responsavel" data-esconder-vazio>&nbsp;</span> &middot;
              <span data-campo="fundador" data-esconder-vazio>&nbsp;</span></li>
        </ul>
      </div>
    </div>

    <div class="rodape__base">
      <p>&copy; <span data-ano>2026</span> Prime Fazendas. {t['direitos']}</p>
      <ul class="rodape__legais">
        {legais}
      </ul>
    </div>
  </div>
</footer>

<a class="zap" data-zap="{t['zap_msg']}" href="#" rel="noopener">
  {ZAP_SVG}
  <span>WhatsApp</span>
</a>"""


def pagina(*, arquivo, lang, titulo, descricao, conteudo, atual="", canonico="",
           alternativo="", og_titulo="", corpo_extra="", head_extra=""):
    t = TXT[lang]
    base = "../" if "/" in arquivo else ""
    prof = base
    canonico = canonico or (SITE + "/" + arquivo.replace("index.html", ""))
    og_titulo = og_titulo or titulo

    if lang == "pt":
        alt = f'<link rel="alternate" hreflang="pt-BR" href="{canonico}">\n<link rel="alternate" hreflang="en" href="{alternativo}">' if alternativo else ""
    else:
        alt = f'<link rel="alternate" hreflang="en" href="{canonico}">\n<link rel="alternate" hreflang="pt-BR" href="{alternativo}">' if alternativo else ""

    html = f"""<!DOCTYPE html>
<html lang="{'pt-BR' if lang == 'pt' else 'en'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<link rel="canonical" href="{canonico}">
{alt}
<meta property="og:type" content="website">
<meta property="og:locale" content="{'pt_BR' if lang == 'pt' else 'en_US'}">
<meta property="og:site_name" content="Prime Fazendas">
<meta property="og:title" content="{og_titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:url" content="{canonico}">
<meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1D2A">
<link rel="icon" href="{prof}assets/img/brasao-96.png" sizes="96x96">
<link rel="apple-touch-icon" href="{prof}assets/img/brasao-96.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,300;6..72,400;6..72,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prof}assets/css/site.css">
{head_extra}</head>

<body data-base="{prof}">
<a class="pular" href="#conteudo">{t['pular']}</a>

{cabecalho(lang, atual, prof)}

<main id="conteudo">
{conteudo}
</main>

{rodape(lang, prof)}

<script src="{prof}assets/js/site.js" defer></script>
{corpo_extra}</body>
</html>
"""
    destino = os.path.join(RAIZ, arquivo)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(html)
    return arquivo


def capa(olho, titulo, apoio, migalhas):
    itens = "".join(
        f'<li><a href="{href}">{rotulo}</a></li>' if href else f"<li>{rotulo}</li>"
        for href, rotulo in migalhas
    )
    return f"""  <section class="capa">
    <div class="env">
      <nav class="migalhas" aria-label="Trilha de navegação"><ol>{itens}</ol></nav>
      <p class="olho">{olho}</p>
      <h1 class="titulo">{titulo}</h1>
      <p class="subtitulo" style="margin-top:1.1rem">{apoio}</p>
    </div>
  </section>
"""
