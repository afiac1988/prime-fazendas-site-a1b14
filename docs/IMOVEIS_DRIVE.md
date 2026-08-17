# Base oficial de imóveis e mídia

Este projeto precisa de um único lugar de entrada para os imóveis.
O site publica a partir do repositório local, mas a organização pode nascer no Drive da Prime.

## Regra simples

- o cadastro do imóvel fica em `conteudo/imoveis/<slug>.json`
- as fotos ficam em `conteudo/midia/imoveis/<slug>/`
- o Drive pode ser o depósito organizado de origem
- o repositório local continua sendo a fonte que publica no site

## Estrutura recomendada no Drive

Crie esta árvore no Drive da Prime Fazendas:

```text
Prime Fazendas
└── Imoveis
    ├── fazenda-exemplo-01
    │   ├── ficha.json
    │   ├── fotos
    │   ├── documentos
    │   └── mapa
    └── fazenda-exemplo-02
        ├── ficha.json
        ├── fotos
        ├── documentos
        └── mapa
```

## Mapeamento para o repositório

Cada pasta do Drive deve refletir no repositório assim:

```text
Drive/Prime Fazendas/Imoveis/fazenda-exemplo-01/
→
prime-fazendas-a1b14-sync/conteudo/imoveis/fazenda-exemplo-01.json
prime-fazendas-a1b14-sync/conteudo/midia/imoveis/fazenda-exemplo-01/
```

## Convenções de nome

- use slug simples, sem acento e sem espaço
- exemplo: `fazenda-rio-formoso`
- fotos numeradas para ordem estável:
  - `01-aerea.jpg`
  - `02-sede.jpg`
  - `03-pasto.jpg`

## Ordem de publicação

1. organizar a pasta no Drive
2. copiar os arquivos para o repositório local
3. atualizar o JSON do imóvel
4. rodar `.\ver.ps1`
5. conferir no navegador
6. commitar e dar push

## O que este arquivo resolve

- evita pastas soltas
- evita foto sem dono
- cria um ponto único para cada imóvel
- facilita conexão futura com Drive, sem bagunçar o site
