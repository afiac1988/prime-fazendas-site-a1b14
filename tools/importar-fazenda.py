#!/usr/bin/env python3
"""
Prime Fazendas — importador de one-pager.

Recebe o PDF de apresentação de uma fazenda e devolve:

  1. o texto do documento, em ordem de leitura (para o cadastro);
  2. as melhores fotografias, recortadas do PDF, otimizadas e gravadas
     em assets/img/fazendas/<slug>-1.webp, -2.webp, -3.webp.

O brasão e demais elementos de marca são descartados: num PDF eles vêm
acompanhados de uma máscara de transparência do mesmo tamanho, coisa que
fotografia não tem. É esse o critério usado para separá-los.

    python3 tools/importar-fazenda.py caminho.pdf slug-da-fazenda [--fotos 3]

Saída: JSON em stdout, com o texto e a lista de fotos gravadas.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RAIZ, "assets", "img", "fazendas")

LARGURA = 1600      # largura máxima da foto grande
LARGURA_CARD = 900  # a primeira foto também sai em tamanho de cartão
QUALIDADE = 80


def texto_do_pdf(pdf):
    try:
        return subprocess.run(
            ["pdftotext", "-layout", pdf, "-"],
            capture_output=True, text=True, timeout=60, check=True
        ).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return f"[falha ao ler o texto: {e}]"


def catalogo_de_imagens(pdf):
    """Lê `pdfimages -list` e devolve uma linha por imagem."""
    saida = subprocess.run(
        ["pdfimages", "-list", pdf], capture_output=True, text=True, timeout=60
    ).stdout.splitlines()

    itens = []
    for linha in saida[2:]:
        campos = linha.split()
        if len(campos) < 5:
            continue
        try:
            itens.append({
                "pagina": int(campos[0]),
                "num": int(campos[1]),
                "tipo": campos[2],
                "larg": int(campos[3]),
                "alt": int(campos[4]),
            })
        except ValueError:
            continue
    return itens


def hashes_do_modelo():
    """Imagens do template — brasão, faixas e a foto de capa de banco."""
    caminho = os.path.join(RAIZ, "tools", "imagens-do-modelo.txt")
    if not os.path.exists(caminho):
        return set()
    with open(caminho, encoding="utf-8") as f:
        return {
            linha.split()[0]
            for linha in f
            if linha.strip() and not linha.startswith("#")
        }


def extrair_e_escolher(pdf, itens, quantas, tmp):
    """
    Extrai todas as imagens e escolhe as melhores fotografias da propriedade.

    Descarta, nesta ordem: peças do modelo (por hash), máscaras de
    transparência, imagens pequenas e formatos que não são fotografia.
    Aceita retrato — várias sedes e currais foram fotografados na vertical.
    """
    from PIL import Image

    ignorar = hashes_do_modelo()
    subprocess.run(
        ["pdfimages", "-png", "-all", pdf, os.path.join(tmp, "img")],
        capture_output=True, timeout=180
    )
    arquivos = sorted(
        f for f in os.listdir(tmp) if re.match(r"img-\d+\.(png|jpg|jpeg|tif|ppm)$", f)
    )

    candidatas = []
    for i, nome in enumerate(arquivos):
        caminho = os.path.join(tmp, nome)
        with open(caminho, "rb") as f:
            if hashlib.md5(f.read()).hexdigest() in ignorar:
                continue
        try:
            im = Image.open(caminho)
        except OSError:
            continue

        if im.mode in ("L", "1"):            # máscara de transparência
            continue
        if im.width < 380 or im.height < 260:
            continue
        prop = im.width / im.height
        if not (0.5 <= prop <= 2.8):         # descarta faixas e quadrados de marca
            continue

        pagina = itens[i]["pagina"] if i < len(itens) else 0
        candidatas.append((im.width * im.height, i, pagina, caminho))

    candidatas.sort(reverse=True)

    escolhidas, por_pagina = [], {}
    for _, i, pagina, caminho in candidatas:      # espalha entre as páginas
        if por_pagina.get(pagina, 0) < 2:
            escolhidas.append(caminho)
            por_pagina[pagina] = por_pagina.get(pagina, 0) + 1
        if len(escolhidas) == quantas:
            break
    for _, _, _, caminho in candidatas:           # completa, se faltou
        if len(escolhidas) == quantas:
            break
        if caminho not in escolhidas:
            escolhidas.append(caminho)

    return escolhidas[:quantas]


def gravar_fotos(pdf, slug, quantas, itens):
    from PIL import Image

    os.makedirs(DEST, exist_ok=True)
    gravadas = []

    with tempfile.TemporaryDirectory() as tmp:
        origens = extrair_e_escolher(pdf, itens, quantas, tmp)

        for ordem, origem in enumerate(origens, start=1):
            try:
                im = Image.open(origem).convert("RGB")
            except OSError:
                continue

            nome = f"{slug}-{ordem}.webp"
            larg = min(LARGURA, im.width)
            grande = im.resize((larg, round(larg * im.height / im.width)), Image.LANCZOS)
            grande.save(os.path.join(DEST, nome), "WEBP", quality=QUALIDADE, method=6)
            gravadas.append({
                "arquivo": f"assets/img/fazendas/{nome}",
                "largura": grande.width,
                "altura": grande.height,
            })

            if ordem == 1:                     # versão leve, para os cartões
                lc = min(LARGURA_CARD, im.width)
                card = im.resize((lc, round(lc * im.height / im.width)), Image.LANCZOS)
                card.save(
                    os.path.join(DEST, f"{slug}-card.webp"),
                    "WEBP", quality=QUALIDADE, method=6
                )

    return gravadas


def main():
    p = argparse.ArgumentParser(description="Importa um one-pager de fazenda.")
    p.add_argument("pdf")
    p.add_argument("slug")
    p.add_argument("--fotos", type=int, default=3)
    args = p.parse_args()

    if not os.path.exists(args.pdf):
        sys.exit(f"PDF não encontrado: {args.pdf}")
    if not shutil.which("pdfimages") or not shutil.which("pdftotext"):
        sys.exit("poppler-utils não está instalado (pdftotext / pdfimages)")

    itens = catalogo_de_imagens(args.pdf)
    fotos = gravar_fotos(args.pdf, args.slug, args.fotos, itens)

    print(json.dumps({
        "slug": args.slug,
        "texto": texto_do_pdf(args.pdf),
        "fotos": fotos,
        "imagens_no_pdf": len(itens),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
