#!/usr/bin/env python3
"""
Prime Fazendas — Radar Agro: últimas do mercado.

Roda todo dia no GitHub e atualiza data/noticias.json com as manchetes mais
recentes do agronegócio.

O que ele grava é apenas **título, fonte, data e link** — o site exibe isso
como remissão à publicação original, com o nome do veículo à vista. Não
copiamos o texto de ninguém: quem quiser ler, clica e vai à fonte.

Isso é diferente do Radar Agro editorial (data/articles.json), que é texto
escrito e revisado pela Prime. As duas coisas aparecem separadas na página.

Se uma fonte cair, ela é ignorada e as demais seguem. Se todas caírem, o
arquivo não é tocado — o site continua mostrando o que já tinha.

    python3 scripts/buscar-noticias.py
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "data", "noticias.json")
FONTES_ARQ = os.path.join(RAIZ, "data", "noticias-fontes.json")

LIMITE = 12          # manchetes guardadas
POR_FONTE = 4        # no máximo, de cada veículo
TIMEOUT = 20

FONTES_PADRAO = [
    {"nome": "Notícias Agrícolas", "url": "https://www.noticiasagricolas.com.br/rss/noticias/graos.xml"},
    {"nome": "Canal Rural", "url": "https://www.canalrural.com.br/feed/"},
    {"nome": "Globo Rural", "url": "https://revistagloborural.globo.com/rss/ultimas/feed.xml"},
    {"nome": "Embrapa", "url": "https://www.embrapa.br/rss/-/asset_publisher/noticias/rss"},
]

MESES = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def carregar_fontes():
    if os.path.exists(FONTES_ARQ):
        try:
            with open(FONTES_ARQ, encoding="utf-8") as f:
                fontes = json.load(f).get("fontes")
            if fontes:
                return fontes
        except (json.JSONDecodeError, OSError):
            pass
    return FONTES_PADRAO


def baixar(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "PrimeFazendasBot/1.0 (+https://primefazendas.com)",
        "Accept": "application/rss+xml, application/xml, text/xml, */*",
    })
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read()


def limpar(txt):
    if not txt:
        return ""
    txt = re.sub(r"<[^>]+>", "", txt)
    for de, para in [("&amp;", "&"), ("&quot;", '"'), ("&#39;", "'"),
                     ("&lt;", "<"), ("&gt;", ">"), ("&nbsp;", " ")]:
        txt = txt.replace(de, para)
    return re.sub(r"\s+", " ", txt).strip()


def data_iso(txt):
    """RSS costuma usar 'Tue, 12 Aug 2026 09:30:00 -0300'. Atom usa ISO."""
    if not txt:
        return ""
    txt = txt.strip()
    m = re.search(r"(\d{1,2})\s+([A-Za-z]{3})\w*\s+(\d{4})", txt)
    if m and m.group(2) in MESES:
        return f"{m.group(3)}-{MESES[m.group(2)]:02d}-{int(m.group(1)):02d}"
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", txt)
    return m.group(0) if m else ""


def itens_do_feed(bruto):
    raiz = ET.fromstring(bruto)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    achados = []

    for item in raiz.iter():
        tag = item.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue

        def campo(*nomes):
            for filho in item:
                if filho.tag.split("}")[-1] in nomes:
                    return filho.text or filho.get("href") or ""
            return ""

        titulo = limpar(campo("title"))
        link = campo("link").strip()
        if not link:
            for filho in item:
                if filho.tag.split("}")[-1] == "link":
                    link = filho.get("href", "")
                    break
        data = data_iso(campo("pubDate", "published", "updated"))

        if titulo and link.startswith("http"):
            achados.append({"titulo": titulo, "url": link, "data": data})

    return achados


def main():
    fontes = carregar_fontes()
    colhidas, falhas = [], []

    for fonte in fontes:
        try:
            itens = itens_do_feed(baixar(fonte["url"]))[:POR_FONTE]
            for it in itens:
                it["fonte"] = fonte["nome"]
            colhidas.extend(itens)
            print(f"  {fonte['nome']}: {len(itens)} manchetes")
        except (urllib.error.URLError, ET.ParseError, OSError, ValueError) as e:
            falhas.append(fonte["nome"])
            print(f"  {fonte['nome']}: falhou ({type(e).__name__}) — ignorada")

    if not colhidas:
        print("\nNenhuma fonte respondeu. O arquivo não foi alterado.")
        return 0

    vistos, unicas = set(), []
    for n in colhidas:
        chave = n["url"].split("?")[0]
        if chave not in vistos:
            vistos.add(chave)
            unicas.append(n)

    unicas.sort(key=lambda n: n.get("data") or "", reverse=True)
    unicas = unicas[:LIMITE]

    with open(SAIDA, "w", encoding="utf-8") as f:
        json.dump({
            "_leia_me": "Manchetes do mercado, atualizadas sozinhas todo dia. "
                        "São remissões: título, veículo e link para a publicação "
                        "original. O texto editorial da Prime fica em articles.json. "
                        "Para trocar as fontes, edite data/noticias-fontes.json.",
            "atualizado_em": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
            "fontes_que_falharam": falhas,
            "noticias": unicas,
        }, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"\n{len(unicas)} manchetes gravadas em data/noticias.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
