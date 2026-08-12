#!/usr/bin/env python3
"""
Converte o resultado salvo do conector do Google Drive num arquivo binário.

O `download_file_content` devolve o arquivo em base64. Quando o retorno é
grande demais para caber na conversa, ele é gravado num .txt com o JSON
{content, id, mimeType, title}. Este utilitário lê esse .txt e escreve o
PDF (ou o que for) no destino.

    python3 tools/decodificar-drive.py resultado.txt destino.pdf
"""
import base64
import json
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("uso: decodificar-drive.py <resultado.txt> <destino>")

    origem, destino = sys.argv[1], sys.argv[2]
    with open(origem, encoding="utf-8") as f:
        dados = json.load(f)

    bruto = base64.b64decode(dados["content"])
    with open(destino, "wb") as f:
        f.write(bruto)

    print(json.dumps({
        "titulo": dados.get("title"),
        "mime": dados.get("mimeType"),
        "bytes": len(bruto),
        "destino": destino,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
