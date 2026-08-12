#!/usr/bin/env python3
"""
Prime Fazendas — montagem do catálogo.

Junta as fichas de /tmp/fichas (ou da pasta indicada) com as fotos já
importadas e grava data/properties.json, no formato que o site consome.

Nada é inventado: o que a ficha não traz vira campo vazio e entra na lista
`revisar` do imóvel, para aparecer no relatório de pendências.

    python3 tools/montar-catalogo.py            # usa a pasta fichas/
"""
import json
import os
import re
import sys
import unicodedata
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOTOS = os.path.join(RAIZ, "assets", "img", "fazendas")
SAIDA = os.path.join(RAIZ, "data", "properties.json")

# A aptidão escrita no documento define a vertical usada nos filtros do site.
# Mapa explícito: o que não casar fica sem tipo e entra em `revisar`.
TIPOS = [
    (r"pecu[áa]ria|cria|recria|engorda|gado|boi", "pecuaria"),
    (r"lavoura|soja|milho|gr[ãa]os?|agr[íi]cola|algod[ãa]o|arroz|sorgo", "agricola"),
    (r"integra[çc][ãa]o|lavoura\s*[e/&+-]*\s*pecu|pecu\w*\s*[e/&+-]+\s*lavoura|ilpf?\b", "integracao"),
    (r"floresta|reflorest|eucalipto|madeira", "florestal"),
    (r"investimento|patrim[óo]nio|reserva", "investimento"),
]

# Localização por região é prática de mercado, não falta de dado: expor
# município e coordenadas antes da qualificação do interessado abre a porta
# para o atravessador. O site mostra a região; o endereço exato é tratado no
# atendimento. Por isso município e estado NÃO entram na lista de pendências.
UF_VALIDAS = {"AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG",
              "PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"}


def sem_acento(txt):
    return "".join(
        c for c in unicodedata.normalize("NFD", txt) if unicodedata.category(c) != "Mn"
    )


def definir_tipo(aptidao, blocos):
    base = sem_acento(" ".join([aptidao] + list(blocos))).lower()
    casados = [tipo for padrao, tipo in TIPOS if re.search(sem_acento(padrao), base)]
    if "integracao" in casados:
        return "integracao"
    for preferido in ("agricola", "pecuaria", "florestal", "investimento"):
        if preferido in casados:
            return preferido
    return ""


def fotos_de(slug):
    achadas = []
    for i in (1, 2, 3, 4, 5, 6, 7):
        rel = f"assets/img/fazendas/{slug}-{i}.webp"
        if os.path.exists(os.path.join(RAIZ, rel)):
            achadas.append(rel)
    return achadas


def montar(ficha):
    slug = ficha["slug"]
    revisar = []

    tipo = definir_tipo(ficha.get("aptidao", ""), ficha.get("descricao_blocos", []))
    if not tipo:
        revisar.append("tipo")

    estado = (ficha.get("estado") or "").strip().upper()
    if estado and estado not in UF_VALIDAS:
        estado = ""
    municipio = (ficha.get("municipio") or "").strip()

    area = ficha.get("area_ha")
    if not isinstance(area, (int, float)):
        area = None
        revisar.append("area_ha")

    valor = ficha.get("valor")
    if not isinstance(valor, (int, float)):
        valor = None

    fotos = fotos_de(slug)
    if len(fotos) < 3:
        revisar.append("fotos")

    card = f"assets/img/fazendas/{slug}-card.webp"
    if not os.path.exists(os.path.join(RAIZ, card)):
        card = fotos[0] if fotos else ""

    return {
        "id": slug,
        "codigo": ficha.get("codigo", ""),
        "nome": ficha.get("nome", ""),
        "municipio": municipio,
        "estado": estado,
        "regiao": ficha.get("regiao_texto", ""),
        "finalidade": "venda",
        "tipo": tipo,
        "aptidao": ficha.get("aptidao", ""),
        "area_ha": area,
        "area_texto": ficha.get("area_total_texto", ""),
        "area_aberta": ficha.get("area_aberta_texto", ""),
        "preco": valor,
        "preco_texto": ficha.get("valor_texto", "") if valor is None else "",
        "imagem": card,
        "fotos": fotos,
        "resumo": (ficha.get("descricao_blocos") or [""])[0],
        "descricao_blocos": ficha.get("descricao_blocos", []),
        "infraestrutura": ficha.get("infraestrutura", ""),
        "logistica": ficha.get("logistica", ""),
        "agua": ficha.get("recurso_hidrico", ""),
        "opcional": ficha.get("opcional", ""),
        "documentacao": "Informações fornecidas pelo proprietário. "
                        "Documentação apresentada ao interessado mediante autorização.",
        "localizacao_reservada": not municipio,
        "confidencial": False,
        "exemplo": False,
        "revisar": revisar,
        "observacoes_internas": ficha.get("observacoes", ""),
    }


def main():
    pasta = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "fichas")
    arquivos = sorted(f for f in os.listdir(pasta) if f.endswith(".json"))
    if not arquivos:
        sys.exit(f"nenhuma ficha em {pasta}")

    imoveis = []
    for nome in arquivos:
        with open(os.path.join(pasta, nome), encoding="utf-8") as f:
            imoveis.append(montar(json.load(f)))

    imoveis.sort(key=lambda i: (i["area_ha"] is None, -(i["area_ha"] or 0)))

    catalogo = {
        "_leia_me": "Catálogo de oportunidades. Gerado por tools/montar-catalogo.py a "
                    "partir das fichas dos one-pagers. Editável à mão: o site lê este "
                    "arquivo diretamente. O campo 'revisar' lista o que ainda precisa "
                    "de confirmação e não é exibido ao visitante.",
        "catalogo_em_preparacao": False,
        "atualizado_em": date.today().isoformat(),
        "imoveis": imoveis,
    }

    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    with open(SAIDA, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # relatório
    print(f"{len(imoveis)} imóveis gravados em data/properties.json\n")
    pend = {}
    for i in imoveis:
        for campo in i["revisar"]:
            pend.setdefault(campo, []).append(i["id"])
    if pend:
        print("Pendências:")
        for campo, ids in sorted(pend.items()):
            print(f"  {campo}: {len(ids)} imóvel(is)")
            if len(ids) <= 6:
                print(f"    {', '.join(ids)}")
    com_preco = sum(1 for i in imoveis if i["preco"])
    print(f"\nCom valor declarado: {com_preco}/{len(imoveis)}")
    reservadas = sum(1 for i in imoveis if i["localizacao_reservada"])
    print(f"Com localização reservada: {reservadas}/{len(imoveis)} "
          f"(prática de mercado — a região aparece, o endereço é tratado no atendimento)")
    locais = sorted({i["estado"] for i in imoveis if i["estado"]})
    print(f"Estados declarados: {', '.join(locais) or 'nenhum'}")
    tipos = {}
    for i in imoveis:
        tipos[i["tipo"] or "(sem tipo)"] = tipos.get(i["tipo"] or "(sem tipo)", 0) + 1
    print("Tipos: " + ", ".join(f"{k} {v}" for k, v in sorted(tipos.items())))


if __name__ == "__main__":
    main()
