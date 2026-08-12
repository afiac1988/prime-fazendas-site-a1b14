#!/usr/bin/env python3
"""
Prime Fazendas — validação dos dados antes de publicar.

Roda a cada envio para o GitHub. Se algo estiver quebrado, o envio falha e
o site NO AR continua intacto — em vez de publicar uma página com erro.

Confere:
  · se os JSON estão bem formados;
  · se cada imóvel tem os campos que o site usa para montar o cartão;
  · se as fotos citadas existem mesmo na pasta;
  · se as datas dos eventos são válidas;
  · se sobrou dado de teste (99999-9999, CRECI 12345, lorem ipsum).

    python3 scripts/validar-dados.py
"""
import json
import os
import re
import sys
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(RAIZ, "data")

erros = []
alertas = []


def erro(msg):
    erros.append(msg)


def alerta(msg):
    alertas.append(msg)


def ler(nome):
    caminho = os.path.join(DADOS, nome)
    if not os.path.exists(caminho):
        erro(f"{nome}: arquivo não encontrado")
        return None
    try:
        with open(caminho, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        erro(f"{nome}: JSON inválido na linha {e.lineno}, coluna {e.colno} — {e.msg}")
        return None


def existe(rel):
    return bool(rel) and os.path.exists(os.path.join(RAIZ, rel))


# ------------------------------------------------------------ propriedades
props = ler("properties.json")
if props is not None:
    imoveis = props.get("imoveis")
    if not isinstance(imoveis, list):
        erro("properties.json: falta a lista 'imoveis'")
        imoveis = []

    vistos = set()
    for i, im in enumerate(imoveis):
        rot = im.get("id") or f"imóvel #{i + 1}"

        for campo in ("id", "nome"):
            if not im.get(campo):
                erro(f"{rot}: falta '{campo}'")

        ident = im.get("id", "")
        if ident in vistos:
            erro(f"{rot}: id repetido — cada imóvel precisa de um id único")
        vistos.add(ident)
        if ident and not re.fullmatch(r"[a-z0-9-]+", ident):
            erro(f"{rot}: id só pode ter letras minúsculas, números e hífen")

        if im.get("finalidade") not in ("venda", "arrendamento"):
            erro(f"{rot}: finalidade deve ser 'venda' ou 'arrendamento'")

        tipos = ("agricola", "pecuaria", "integracao", "florestal", "investimento", "")
        if im.get("tipo") not in tipos:
            erro(f"{rot}: tipo inválido — use {', '.join(t for t in tipos if t)}")

        if im.get("area_ha") is not None and not isinstance(im["area_ha"], (int, float)):
            erro(f"{rot}: area_ha deve ser número ou null")
        if im.get("preco") is not None and not isinstance(im["preco"], (int, float)):
            erro(f"{rot}: preco deve ser número ou null")
        if im.get("preco") is None and not im.get("preco_texto"):
            alerta(f"{rot}: sem preço e sem preco_texto — o cartão vai dizer 'Sob consulta'")

        if not existe(im.get("imagem")):
            erro(f"{rot}: imagem do cartão não existe — {im.get('imagem') or '(vazio)'}")
        for foto in im.get("fotos", []):
            if not existe(foto):
                erro(f"{rot}: foto não existe — {foto}")
        if len(im.get("fotos", [])) == 0:
            alerta(f"{rot}: sem fotos na ficha")

        if not im.get("municipio") and not im.get("estado") and not im.get("regiao"):
            alerta(f"{rot}: sem município, estado nem região — o cartão fica sem localização")

    print(f"properties.json: {len(imoveis)} imóveis")

# ----------------------------------------------------------------- artigos
arts = ler("articles.json")
if arts is not None:
    for a in arts.get("artigos", []):
        rot = a.get("id") or a.get("titulo", "artigo sem título")
        if not a.get("titulo"):
            erro(f"{rot}: falta título")
        if a.get("imagem") and not existe(a["imagem"]):
            erro(f"{rot}: imagem não existe — {a['imagem']}")
        if not arts.get("secao_em_preparacao") and not a.get("exemplo"):
            if not a.get("data"):
                erro(f"{rot}: artigo publicado precisa de data")
            if not (a.get("autor") or a.get("fonte")):
                erro(f"{rot}: artigo publicado precisa de autor ou fonte")
    print(f"articles.json: {len(arts.get('artigos', []))} artigos")

# ----------------------------------------------------------------- eventos
evs = ler("events.json")
if evs is not None:
    hoje = date.today().isoformat()
    futuros = 0
    for e in evs.get("eventos", []):
        rot = e.get("nome", "evento sem nome")
        if not e.get("nome"):
            erro("evento sem nome")
        ini = e.get("inicio", "")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", ini or ""):
            erro(f"{rot}: data de início deve ser AAAA-MM-DD — veio '{ini}'")
        elif (e.get("fim") or ini) >= hoje:
            futuros += 1
        if e.get("url") and not e["url"].startswith("http"):
            erro(f"{rot}: o link deve começar com http")
    print(f"events.json: {len(evs.get('eventos', []))} eventos ({futuros} ainda por vir)")

# ------------------------------------------------------------ institucional
site = ler("site.json")
if site is not None:
    zap = re.sub(r"\D", "", site.get("whatsapp") or "")
    if zap and not (12 <= len(zap) <= 13):
        erro(f"site.json: whatsapp deve ter 12 ou 13 dígitos com o país — veio {len(zap)}")
    if not site.get("creci"):
        alerta("site.json: sem CRECI — o rodapé fica sem o registro")
    print("site.json: ok")

# -------------------------------------------------------- resíduo de teste
SUSPEITOS = [
    (r"99999.?9999", "telefone de teste"),
    (r"\b12345/TO\b", "CRECI de teste"),
    (r"lorem ipsum", "texto de preenchimento"),
    (r"5511987654321", "WhatsApp de exemplo"),
]
for nome in ("properties.json", "articles.json", "events.json", "site.json"):
    caminho = os.path.join(DADOS, nome)
    if not os.path.exists(caminho):
        continue
    conteudo = open(caminho, encoding="utf-8").read().lower()
    for padrao, oque in SUSPEITOS:
        if re.search(padrao, conteudo):
            erro(f"{nome}: {oque} ainda está no arquivo")

# ------------------------------------------------------------------ saída
print()
for a in alertas:
    print(f"  aviso  {a}")
for e in erros:
    print(f"  ERRO   {e}")

print()
if erros:
    print(f"{len(erros)} erro(s). A publicação foi interrompida — o site no ar continua como está.")
    sys.exit(1)

print("Tudo certo." + (f" {len(alertas)} aviso(s), nenhum impede a publicação." if alertas else ""))
