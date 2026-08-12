#!/usr/bin/env python3
"""
Escolhe qual foto da fazenda vira a capa do cartão.

O importador usa a foto 1 por padrão. Quando ela não é a melhor vitrine —
um mapa de uso do solo, por exemplo — troque a capa:

    python3 tools/definir-capa.py cristal-de-carolina 3

Registra a escolha em data/capas.json, para que a reimportação a preserve.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOTOS = os.path.join(RAIZ, "assets", "img", "fazendas")
REGISTRO = os.path.join(RAIZ, "data", "capas.json")
LARGURA = 900


def aplicar(slug, n):
    from PIL import Image

    origem = os.path.join(FOTOS, f"{slug}-{n}.webp")
    if not os.path.exists(origem):
        sys.exit(f"não existe: {origem}")

    im = Image.open(origem).convert("RGB")
    larg = min(LARGURA, im.width)
    im.resize((larg, round(larg * im.height / im.width)), Image.LANCZOS).save(
        os.path.join(FOTOS, f"{slug}-card.webp"), "WEBP", quality=80, method=6
    )


def main():
    if len(sys.argv) == 1:                       # reaplica tudo o que está registrado
        if not os.path.exists(REGISTRO):
            sys.exit("nada registrado em data/capas.json")
        registro = json.load(open(REGISTRO, encoding="utf-8"))
        for slug, n in registro.get("capas", {}).items():
            aplicar(slug, n)
            print(f"{slug}: capa = foto {n}")
        return

    if len(sys.argv) != 3:
        sys.exit("uso: definir-capa.py <slug> <numero-da-foto>   |   sem argumentos, reaplica tudo")

    slug, n = sys.argv[1], int(sys.argv[2])
    aplicar(slug, n)

    registro = {"_leia_me": "Capa escolhida à mão para cada fazenda. "
                            "Rode `python3 tools/definir-capa.py` sem argumentos "
                            "depois de reimportar, para reaplicar.", "capas": {}}
    if os.path.exists(REGISTRO):
        registro = json.load(open(REGISTRO, encoding="utf-8"))
    registro.setdefault("capas", {})[slug] = n
    with open(REGISTRO, "w", encoding="utf-8") as f:
        json.dump(registro, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"{slug}: capa = foto {n}")


if __name__ == "__main__":
    main()
