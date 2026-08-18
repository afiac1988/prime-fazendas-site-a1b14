# Pasta oficial de mídia dos imóveis

Coloque aqui as fotos e arquivos de cada imóvel, sempre separados por slug.

## Estrutura

```text
conteudo/midia/imoveis/
├── fazenda-exemplo-01/
│   ├── 01-aerea.jpg
│   ├── 02-sede.jpg
│   └── 03-documentacao.jpg
└── fazenda-exemplo-02/
    ├── 01-aerea.jpg
    └── 02-pasto.jpg
```

## Regra

- uma pasta por imóvel
- nomes curtos, consistentes e sem espaço
- a primeira imagem é a capa
- o JSON do imóvel em `conteudo/imoveis/<slug>.json` deve apontar para esta pasta

## Fluxo

1. salve as fotos aqui
2. atualize o JSON correspondente
3. rode `.\ver.ps1`
4. publique
