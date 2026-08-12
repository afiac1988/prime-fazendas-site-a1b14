#!/usr/bin/env python3
"""
Descobre quais imagens são do MODELO do one-pager, e não das fazendas.

O material da Prime usa um template: brasão, faixas, ícones e uma foto de
capa de banco de imagens. Essas peças se repetem, idênticas, em vários
documentos — enquanto a fotografia de uma fazenda só aparece na dela.

O script varre uma pasta de PDFs, calcula o hash de cada imagem embutida e
grava em tools/imagens-do-modelo.txt os hashes que aparecem em dois ou mais
documentos. O importador lê essa lista e descarta essas imagens.

    python3 tools/mapear-imagens-do-modelo.py /tmp/pdfs
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTA = os.path.join(RAIZ, "tools", "imagens-do-modelo.txt")


def hashes_do_pdf(pdf):
    achados = set()
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["pdfimages", "-png", "-all", pdf, os.path.join(tmp, "i")],
            capture_output=True, timeout=180
        )
        for nome in sorted(os.listdir(tmp)):
            caminho = os.path.join(tmp, nome)
            with open(caminho, "rb") as f:
                achados.add(hashlib.md5(f.read()).hexdigest())
    return achados


def main():
    pasta = sys.argv[1] if len(sys.argv) > 1 else "/tmp/pdfs"
    pdfs = sorted(
        os.path.join(pasta, f) for f in os.listdir(pasta) if f.lower().endswith(".pdf")
    )
    if not pdfs:
        sys.exit(f"nenhum PDF em {pasta}")

    ocorrencias = defaultdict(int)
    for pdf in pdfs:
        for h in hashes_do_pdf(pdf):
            ocorrencias[h] += 1

    repetidas = sorted(h for h, n in ocorrencias.items() if n >= 2)

    with open(LISTA, "w", encoding="utf-8") as f:
        f.write("# Imagens do modelo do one-pager — descartadas na importação.\n")
        f.write("# Gerado por tools/mapear-imagens-do-modelo.py\n")
        f.write(f"# {len(pdfs)} documentos analisados.\n")
        for h in repetidas:
            f.write(f"{h}  # aparece em {ocorrencias[h]} documentos\n")

    print(f"{len(pdfs)} PDFs · {len(ocorrencias)} imagens distintas · "
          f"{len(repetidas)} são do modelo")


if __name__ == "__main__":
    main()
