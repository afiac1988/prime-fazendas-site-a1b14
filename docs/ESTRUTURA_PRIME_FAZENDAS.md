# Estrutura oficial da Prime Fazendas

Este documento define o caminho único para manter a Prime Fazendas organizada.

## Origem

A pasta-base informada por você é esta:

https://drive.google.com/drive/folders/1VvjtTjSDSV-zSzvJVFK1ilx6tDobQg-X?usp=drive_link

Essa pasta deve funcionar como origem de organização dos imóveis, documentos e mídias.

## Regra principal

- o Drive organiza
- o repositório local publica
- o site lê do repositório local

## Estrutura recomendada no Drive

```text
Prime Fazendas
├── Imoveis
│   ├── fazenda-rio-formoso
│   │   ├── ficha.json
│   │   ├── fotos
│   │   ├── documentos
│   │   └── mapa
│   ├── fazenda-serra-do-lajeado
│   │   ├── ficha.json
│   │   ├── fotos
│   │   ├── documentos
│   │   └── mapa
│   └── ...
├── Documentos
│   ├── Contratos
│   ├── Matriculas
│   ├── CAR
│   ├── CCIR-ITR
│   └── Georreferenciamento
├── Midias
│   ├── Fotos
│   ├── Videos
│   └── Logos
└── Andares
    ├── ANDAR_07_Prime_Fazendas
    └── Andares_Externos
```

## Mapeamento para o repositório local

Cada imóvel do Drive deve virar isto no projeto:

```text
conteudo/imoveis/<slug>.json
conteudo/midia/imoveis/<slug>/
```

Cada notícia do blog deve ficar em:

```text
conteudo/noticias/<data>-<slug>.md
```

Textos institucionais ficam em:

```text
conteudo/paginas.json
conteudo/config.json
conteudo/dados-agro.json
conteudo/depoimentos.json
```

## Fluxo de trabalho

1. a pasta certa nasce ou é atualizada no Drive
2. o material é copiado para o repositório local
3. o JSON do imóvel é preenchido
4. as fotos vão para `conteudo/midia/imoveis/<slug>/`
5. roda `.\ver.ps1`
6. confere no navegador
7. commita e publica

## O que não fazer

- não espalhar fotos em pastas genéricas
- não criar versões paralelas sem nome canônico
- não publicar imóvel sem slug definido
- não editar `site/` manualmente

## Finalidade

Essa estrutura existe para:

- evitar perda de arquivo
- evitar pasta solta
- evitar imóvel sem mídia
- deixar o caminho curto para atualização do site
- permitir que o Drive e o repositório fiquem alinhados
