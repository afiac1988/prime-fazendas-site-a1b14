# Prime Fazendas — site

Site institucional e comercial da Prime Fazendas: imobiliária rural especializada em compra, venda
e arrendamento de propriedades no MATOPIBA.

Site estático, sem banco de dados e sem build no servidor. O conteúdo vive em arquivos JSON,
separado do código.

---

## Estrutura

```
index.html               Início
oportunidades.html       Catálogo com filtros
arrendamentos.html       Áreas para arrendar
propriedade.html         Ficha da propriedade (?id=PF-0001)
radar-agro.html          Editorial
agenda-agro.html         Eventos
quem-somos.html          Institucional
contato.html             Formulário de contato
anuncie.html             Formulário do proprietário
privacidade.html         LGPD (revisar com jurídico)
termos.html              Termos (revisar com jurídico)
404.html
en/                      Versão em inglês
data/                    ← É AQUI QUE VOCÊ EDITA O CONTEÚDO
assets/css/site.css      Design system
assets/js/site.js        Comportamento
assets/img/              Imagens
tools/                   Geradores (build.py, pages.py, make-art.py, extract-logo.js, make-og.js)
```

---

## Como atualizar o conteúdo (sem mexer em código)

Tudo em `data/`. Salve o arquivo, faça commit e o site atualiza sozinho.

### `data/site.json` — dados institucionais

Preencha os campos vazios: `telefone`, `whatsapp`, `creci`, `cnpj` e o LinkedIn.

**O site esconde automaticamente o que ainda está vazio** em vez de mostrar campo em branco ou
informação inventada. O botão de WhatsApp só aparece depois que o número for preenchido.

Formato do WhatsApp: `5563999999999` (país + DDD + número, só dígitos).

### `data/properties.json` — as propriedades

**Este arquivo é gerado, não digitado.** As 23 fazendas vieram dos one-pagers oficiais do Google
Drive. Para acrescentar uma nova, veja "Importar uma fazenda nova", mais abaixo.

Pode editar à mão à vontade — o site lê este arquivo direto. Só lembre que rodar o montador de novo
sobrescreve o que estiver aqui; a fonte da verdade são as fichas.

Campos de cada imóvel:

| Campo | O que é |
|---|---|
| `id` | Identificador e endereço da ficha: `propriedade.html?id=rubi-negro` |
| `codigo` | Código Prime, quando o documento traz |
| `nome` | Nome da fazenda |
| `municipio`, `estado` | Em geral vazios, de propósito — ver "Por que só a região" |
| `regiao` | "Região Sudeste do Pará", como escrito no one-pager |
| `finalidade` | `venda` ou `arrendamento` |
| `tipo` | `agricola`, `pecuaria`, `integracao`, `florestal`, `investimento` |
| `aptidao` | Texto do documento: "Lavoura e Pecuária" |
| `area_ha` | Número em hectares. `null` quando a área está em alqueires |
| `area_texto` | Área como escrita: "402,66 alqueires" |
| `area_aberta` | Área aberta declarada |
| `preco` | Número em reais. `null` quando não há valor |
| `imagem` | Capa do cartão |
| `fotos` | As 3 fotos da ficha |
| `resumo`, `descricao_blocos` | Descrição, transcrita do documento |
| `infraestrutura`, `logistica`, `agua`, `opcional` | Ficha técnica |
| `localizacao_reservada` | `true` quando só a região é divulgada — o padrão da carteira |
| `revisar` | **Interno.** Campos que faltam confirmar. Não aparece para o visitante |
| `observacoes_internas` | **Interno.** Ressalvas anotadas na importação |

### `data/articles.json` — Radar Agro

Publique apenas texto revisado, com `autor`, `fonte` e `data` verificados. Quando terminar de montar
a seção, mude `"secao_em_preparacao"` para `false` e remova os modelos de pauta.

### `data/events.json` — Agenda Agro

Comece com a lista vazia — é proposital: melhor uma agenda em montagem do que uma data errada
publicada. Cada evento precisa de:

```json
{
  "nome": "Nome oficial do evento",
  "inicio": "2026-09-15",
  "fim": "2026-09-18",
  "cidade": "Luís Eduardo Magalhães",
  "estado": "BA",
  "segmento": "Agronegócio",
  "url": "https://site-oficial-do-evento.com.br",
  "prime": true
}
```

`"prime": true` marca os eventos em que a Prime estará presente. **Eventos com data passada somem
da lista sozinhos** — não é preciso limpar nada.

---

## Fotografia

As imagens em `assets/img/` são composições feitas para a marca, ocupando o lugar da fotografia
real. Cada arquivo tem um equivalente fotográfico a ser produzido:

| Arquivo | Substituir por |
|---|---|
| `hero-matopiba.svg` | Fotografia aérea ampla de uma propriedade — a melhor imagem que a Prime tiver |
| `estado-ma/to/pi/ba` | Uma imagem característica de cada estado |
| `fundador.webp` | Foto de André, extraída do Prime Vision. Se tiver uma em alta resolução, troque |
| `radar-01/02/03` | Imagens das matérias |
| `og.svg` | Já traz o brasão sobre a paisagem. Só troque a paisagem de fundo. |

Ao trocar, prefira `.webp` (qualidade 80) com no máximo 2400px de largura no banner e 1600px nos
cartões. Depois é só apontar o novo caminho no JSON ou no HTML.

## A marca

O site usa o **brasão** — o emblema redondo com as três estrelas, "PRIME FAZENDAS BRASIL" e os
talhões verdes. Ele foi extraído dos one-pagers oficiais de fazendas que estão no Google Drive da
Prime, onde aparece embutido em alta definição com fundo transparente.

| Arquivo | Onde é usado |
|---|---|
| `brasao.webp` (392px) | imagem de compartilhamento |
| `brasao-320.webp` | cabeçalho e rodapé |
| `brasao-96.png` | favicon e ícone de aplicativo |

Fica em WebP de propósito: o brasão tem gradiente, relevo e brilho metálico. Vetorizar achataria o
acabamento. Se um dia surgir o arquivo vetorial original (`.ai`, `.eps` ou `.pdf` editável),
substitua — aí sim vale.

**Logotipo anterior, do sol.** `marca-simbolo.svg`, `marca-inline.svg` e `marca-completa.svg` são o
logotipo do sol sobre as cristas, extraído em vetor do `PrimeFazendas.pdf` do seu material. Não
estão em uso, mas ficaram no projeto por serem vetor de verdade — úteis para marca-d'água, papelaria
ou qualquer aplicação que precise escalar sem perda. Para refazer:

```bash
pdftocairo -svg PrimeFazendas.pdf /tmp/logo-raw.svg
node tools/extract-logo.js
```

`mapa-matopiba.svg` também é elemento da identidade — mantenha.

---

## Publicação

Hospedagem estática (Netlify, Vercel, Cloudflare Pages). Basta subir a pasta: não há build.
O `netlify.toml` já traz cabeçalhos de segurança, cache dos assets e URLs limpas
(`/oportunidades` funciona além de `/oportunidades.html`).

### Onde o site vive hoje

| Item | Valor |
|---|---|
| Projeto Netlify | `super-gumption-758fa9` |
| Endereço | https://super-gumption-758fa9.netlify.app |
| Time Netlify | `primefazendasto` (conta primefazendasto@gmail.com) |
| Repositório ligado | `github.com/afiac1988/prime-fazendas-site-a1b14` |

**Atenção ao repositório.** Existem dois no GitHub com nome parecido:
`prime-fazendas-site` e `prime-fazendas-site-a1b14`. O Netlify está ligado ao **segundo**,
com o sufixo. Commit no primeiro não publica nada — foi o que aconteceu antes.

### Como publicar

Por estar ligado ao Git, o projeto não aceita arrastar-e-soltar: todo deploy sai de um push.

```bash
git clone https://github.com/afiac1988/prime-fazendas-site-a1b14.git
cd prime-fazendas-site-a1b14
# copie o conteúdo desta pasta por cima (exceto tools/ e LEIA-ME.md, se preferir)
git add -A && git commit -m "Site novo: 23 fazendas, marca e catálogo" && git push
```

O Netlify detecta o push e publica em cerca de um minuto.

---

## Formulários

Os formulários hoje validam e confirmam na tela, mas **não enviam para lugar nenhum** — falta
apontar o destino. Duas opções:

1. **Netlify Forms** — acrescente `netlify` e `name="contato"` na tag `<form>`. Zero backend.
2. **Serviço externo** (Formspree, Basin) — troque `action="#"` pelo endereço do serviço.

Enquanto o `action` for `#`, o JavaScript mostra a confirmação na tela. Assim que houver um destino
real, o envio passa a ser feito pelo próprio navegador.

Falta ainda proteção contra spam (honeypot ou captcha do serviço escolhido).

---

## Antes de publicar — pendências

- [ ] LinkedIn em `data/site.json`, se quiser exibir
- [ ] CNPJ é opcional: para imobiliária o registro que importa no site é o CRECI, e ele já está lá.
      Se quiser exibir, preencha o campo — o site mostra sozinho
- [ ] **Corrigir dois one-pagers do Drive** — ver "CRECI errado no material", abaixo
- [ ] Resolver a data: o material da marca diz fundação em 2025, o texto do site diz "mais de três anos"
- [ ] Trocar o banner por uma fotografia aérea real de uma das fazendas
- [ ] Publicar três textos revisados no Radar Agro
- [ ] Cadastrar eventos confirmados na Agenda Agro
- [ ] Ligar o envio dos formulários
- [ ] Revisar `privacidade.html` e `termos.html` com assessoria jurídica
- [ ] Revisar a versão em inglês com alguém fluente

---

## Por que só a região

O catálogo mostra a região da fazenda, não o município nem o endereço. **Isso é decisão comercial,
não dado faltando.**

No mercado de terras, endereço circulando cedo demais atrai atravessador: multiplica interlocutores,
enche o proprietário de contato repetido e tira dele o controle da negociação. A região, junto com
aptidão, escala, logística e recurso hídrico, é o bastante para um comprador sério decidir se vale a
visita. Endereço, matrícula e agendamento entram depois, no atendimento.

Por isso o montador **não** trata município e estado como pendência, e o filtro do catálogo agrupa
por estado quando o documento o declara e por região quando não. Se um dia quiser publicar o
município de algum imóvel, é só preencher o campo na ficha — o site passa a mostrar.

---

## Importar uma fazenda nova

O caminho inteiro, do PDF ao site, são quatro comandos:

```bash
# 1. baixe o one-pager do Drive e salve em /tmp/pdfs/rubi-do-cerrado.pdf

# 2. extraia texto e fotos (as fotos já saem otimizadas em WebP)
python3 tools/importar-fazenda.py /tmp/pdfs/rubi-do-cerrado.pdf rubi-do-cerrado --fotos 3

# 3. crie a ficha em /tmp/fichas/rubi-do-cerrado.json, copiando o formato de outra
#    e transcrevendo o texto que o comando acima imprimiu

# 4. remonte o catálogo
python3 tools/montar-catalogo.py /tmp/fichas
```

O passo 4 imprime um relatório do que ficou pendente — quantos imóveis estão sem estado, sem
município, sem área numérica ou sem as 3 fotos.

**Se a capa não ficar boa** (o importador escolhe a maior foto, que às vezes é um mapa):

```bash
python3 tools/definir-capa.py rubi-do-cerrado 3     # usa a foto 3 como capa
python3 tools/definir-capa.py                        # reaplica todas as escolhas salvas
```

**Se o modelo do one-pager mudar**, remapeie as peças de template para que elas voltem a ser
descartadas:

```bash
python3 tools/mapear-imagens-do-modelo.py /tmp/pdfs
```

Esse script compara todos os PDFs e trata como elemento de modelo qualquer imagem que apareça em
dois ou mais documentos — foi assim que o brasão e a foto de capa de banco de imagens pararam de
entrar como se fossem foto de fazenda.

### As ferramentas

| Arquivo | Função |
|---|---|
| `tools/pages.py` | Gera as 17 páginas HTML |
| `tools/build.py` | Cabeçalho, rodapé e `<head>`, num lugar só |
| `tools/importar-fazenda.py` | PDF → texto + 3 fotos otimizadas |
| `tools/montar-catalogo.py` | Fichas → `data/properties.json` + relatório de pendências |
| `tools/definir-capa.py` | Troca a capa do cartão |
| `tools/mapear-imagens-do-modelo.py` | Descobre as peças do template a descartar |
| `tools/decodificar-drive.py` | Converte o retorno do Google Drive em arquivo |
| `tools/extract-logo.js` | Extrai a marca vetorial do PDF original |
| `tools/make-og.js` | Gera a imagem de compartilhamento |
| `tools/make-art.py` | Gera as paisagens SVG de apoio |

---

## Regenerar as páginas

Cabeçalho, rodapé e `<head>` ficam num lugar só. Para alterá-los:

```bash
python3 tools/pages.py     # regenera todas as páginas HTML
python3 tools/make-art.py  # regenera as composições SVG
```

Edite `tools/build.py` (estrutura) ou `tools/pages.py` (conteúdo de cada página) e rode de novo.
Não edite os `.html` da raiz diretamente — eles são sobrescritos.

---

## Decisões de projeto

- **Nada fictício publicado como verdadeiro.** Exemplos vêm marcados como exemplo; a agenda vazia
  fica vazia; campos não preenchidos somem.
- **Sem urgência artificial.** Nada de "últimas unidades", contadores de interessados ou selos "hot".
- **Sem localização exata de propriedade confidencial.**
- **Sem promessa de rentabilidade, aprovação documental ou segurança jurídica.**
- **Acessibilidade:** navegação por teclado, foco visível, contraste AA, campos com rótulo real e
  respeito a `prefers-reduced-motion`.
- **Desempenho:** SVG leve, carregamento tardio fora da primeira dobra, sem framework, sem vídeo.


---

## O que a busca nos seus arquivos encontrou

Varredura em 279 arquivos de `ANDAR_07 — Prime Fazendas`, 4 de `EXT-07-01_CEO_PRIME_FAZENDAS` e
65 de `Downloads`, mais os documentos desta sessão.

### Encontrado e já aplicado ao site

| Dado | Onde estava |
|---|---|
| **Brasão** (marca atual) | Google Drive, embutido nos one-pagers de fazendas — extraído e integrado |
| Logotipo do sol, em vetor | `conteudo/midia/geral/marca-original/PrimeFazendas.pdf` — extraído, guardado |
| E-mail `contato@primefazendas.com` | `conteudo/config.json` |
| Base em Palmas, Tocantins | `conteudo/config.json` |
| Fundador: André Amorim | `conteudo/config.json` |
| Instagram `@primefazendas` | citado 20 vezes; o próprio arquivo pede confirmação |
| Assinatura original da marca | está no logotipo; registrada em `data/site.json`, **não publicada** |

### Não encontrado — precisa vir de você

**Telefone, WhatsApp, CRECI e CNPJ não existem em nenhum arquivo.** O que há são valores de teste:
telefone `(63) 99999-9999` e `CRECI 12345/TO`, repetidos em 20 páginas do site anterior. Aquele
projeto, aliás, bloqueava a própria publicação por causa disso — a nota em `config.json` diz, com
todas as letras, que os valores são de teste e travam o build.

Apareceu ainda um `CRECI Jurídico: J-037900` num arquivo de contexto. **Não foi usado.** Esse número
existe em um único lugar: um arquivo gerado por uma sessão de IA anterior, na nuvem, sem cópia no seu
disco e sem nenhuma outra fonte que o confirme. CRECI é registro regulado; publicar um número não
verificado é risco jurídico, não detalhe de layout. Confirme no CRECI-TO antes de usar.

### Divergência a resolver

`conteudo/config.json` registra `ano_fundacao: 2025`. O texto do site afirma "mais de três anos de
atuação", conforme o briefing. As duas coisas não fecham. Defina qual é a correta — o site herda a
sua decisão, mas a afirmação precisa se sustentar.


---

## Ainda no Google Drive: material real da carteira

A conta `primefazendasto@gmail.com` guarda dezenas de one-pagers de fazendas em PDF — por código
(`Prime - Cód. 87`) e por nome (`Fazenda Pérola do Araguaia — 10.164 ha`, `Fazenda Opala do Norte —
12.000 ha`, `Fazenda Rubi do Araguaia — 3.500 ha`, `Fazenda Obsidiana do Cerrado — 7.260 ha`, entre
outros). Cada um traz fotos, área e dados da propriedade.

**É daí que sai o catálogo real.** Quando você autorizar, dá para ler esses PDFs, extrair as fotos e
os dados de cada fazenda e montar o `data/properties.json` com a carteira de verdade — no lugar dos
exemplos. É o passo que tira o aviso de "catálogo em preparação" do ar.


---

## CRECI errado no material

O site publica os registros corretos, informados por André:

- **CRECI/TO J-5807** — pessoa jurídica, Prime Fazendas
- **CRECI/TO 2122** — André Felipe Izaguirre Amorim Crewe, responsável técnico

Aparecem no rodapé de todas as páginas e na página de contato.

**Mas dois one-pagers que circulam trazem outro número:** `CRECI 037900-J`, em **Opala do Norte** e
**Obsidiana do Cerrado**. Esse registro não é o da Prime. Vale corrigir os dois PDFs antes de
continuarem sendo enviados a clientes — CRECI é registro regulado e número errado em peça comercial
é exposição desnecessária.

---

## O que foi corrigido na importação das 23 fazendas

Três defeitos reais apareceram e foram tratados no código, não à mão:

**A capa era a mesma foto de banco em 22 fazendas.** O modelo de one-pager abre com uma imagem de
colheitadeira em campo de trigo, que não é de nenhuma propriedade. O `mapear-imagens-do-modelo.py`
compara todos os PDFs e descarta qualquer imagem repetida em dois ou mais — foi assim que essa capa
e o brasão pararam de entrar como se fossem foto de fazenda.

**Fotos verticais eram rejeitadas.** Várias sedes e currais foram fotografados em retrato, e o
filtro de proporção só aceitava paisagem. Corrigido.

**A ficha tinha um bloco "Destaques" vazio**, resquício do esquema anterior. Removido.

### Ressalvas anotadas, que dependem de você

- **Angelita**: o nome do arquivo diz 1.500 ha, o documento diz 620 ha. Vale o documento.
- **Pedra do Sol**: arquivo diz 2.521,64 ha, documento diz 2.153 ha. Vale o documento.
- **Obsidiana do Araguaia**: 4.153 ha + 1.200 ha de reserva averbada fora da propriedade não fecham
  com os 5.300 ha anunciados.
- **Água-marinha**: o texto diz 1.877 ha de área aberta e o mapa da página 3 diz 1.886 ha.
- **Quatro fazendas em alqueires** (Jaspe Azul, Esmeralda do Cerrado, Topázio Imperial, Turmalina
  Negra) ficaram com `area_ha` nulo de propósito — a medida do alqueire varia por região e não cabe
  a nós converter. O site exibe o valor original.

Tudo isso está em `observacoes_internas` de cada imóvel, que não aparece para o visitante.
