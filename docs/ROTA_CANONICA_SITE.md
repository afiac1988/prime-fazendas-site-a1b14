# Rota canônica do site Prime Fazendas

> Este documento pertence ao checkout espelho `prime-fazendas-a1b14-sync`.
> O caminho oficial único de edição e publicação é `prime-fazendas-website`.

Este documento é a memória curta e confiável do site.  
Se alguém chegar novo ao projeto, é por aqui que começa.

## 1) Regra central

O fluxo oficial é:

`conteudo/` ou `tema/assets/` → `ver.ps1` → commit em `main` → push → Vercel publica

Não usar caminhos paralelos para o dia a dia.

## 2) O que editar em cada caso

### Conteúdo

- `conteudo/config.json` — contatos, redes, domínio, avisos legais e configurações do site
- `conteudo/paginas.json` — textos institucionais e blocos de página
- `conteudo/dados-agro.json` — indicadores do setor
- `conteudo/depoimentos.json` — prova social
- `conteudo/imoveis/*.json` — propriedades
- `conteudo/noticias/*.md` — blog e notícias

### Visual e comportamento

- `tema/assets/estilo.css` — aparência
- `tema/assets/site.js` — menus, filtros e interações
- `tema/assets/marca.svg` — marca vetorial
- `tema/assets/og-prime-fazendas.png` — imagem de compartilhamento

### Geração e publicação

- `build.py` — gera a saída final em `site/`
- `ver.ps1` — preview local sem publicar
- `vercel.json` — diz para a Vercel publicar a pasta `site/`

## 3) Templates oficiais

### Blog

Modelo canônico:

- `conteudo/noticias/_MODELO.md`

Como usar:

1. Copie o arquivo
2. Renomeie com data e assunto
3. Preencha front matter e corpo
4. Rode `ver.ps1`

### Imóveis

Modelo canônico:

- `conteudo/imoveis/_MODELO.json`

Como usar:

1. Copie o arquivo
2. Renomeie com o slug do imóvel
3. Preencha dados, fotos, documentação e vídeo se houver
4. Rode `ver.ps1`

## 4) Caminho curto para publicar uma mudança

1. editar o arquivo certo
2. salvar
3. rodar `ver.ps1`
4. conferir no navegador
5. commitar na `main`
6. dar push
7. a Vercel publica automaticamente

## 5) Modo de verificação local

### Preview normal

```powershell
.\ver.ps1
```

### Preview com rascunhos visíveis

```powershell
.\ver.ps1 -Demo
```

Esse modo mostra também o que está com `publicado=false`, sem misturar com a saída final.

## 6) Regras de segurança editorial

- preços, áreas e disponibilidade devem ser confirmados antes de proposta
- contatos de teste precisam ser trocados pelos reais em `conteudo/config.json`
- se `manutencao.local.json` estiver ativo, a senha e o caminho do `.htpasswd` precisam estar corretos
- `site/` é saída gerada; não editar à mão

## 7) Estrutura curta do repositório

```text
prime-fazendas-a1b14-sync/
├── conteudo/
├── tema/assets/
├── build.py
├── ver.ps1
├── vercel.json
├── site/
└── docs/ROTA_CANONICA_SITE.md
```

## 8) Como saber se está tudo certo

Checklist mínimo:

- os arquivos em `conteudo/` existem e estão no formato esperado
- os templates `conteudo/noticias/_MODELO.md` e `conteudo/imoveis/_MODELO.json` existem
- `build.py` roda sem erro
- `ver.ps1` abre o preview local
- `vercel.json` aponta para `site/`
- o `git status` está limpo antes do push

## 9) Quando houver dúvida

Se for conteúdo, mexa em `conteudo/`.  
Se for visual, mexa em `tema/assets/`.  
Se for geração, mexa em `build.py`.  
Se for preview, use `ver.ps1`.  
Se for publicação, o caminho é `main` → push → Vercel.
