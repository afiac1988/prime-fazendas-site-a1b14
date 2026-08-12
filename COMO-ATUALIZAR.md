# Como atualizar o site

Uma página. Se ler só esta, já dá conta de tudo.

**O site publica sozinho.** Você não sobe arquivo, não roda programa, não mexe em
servidor. Salvou aqui no GitHub, o site está no ar em cerca de um minuto.

---

## Trocar o preço de uma fazenda, corrigir um texto, tirar do ar

1. Abra **`data/properties.json`** aqui no GitHub.
2. Clique no lápis, no canto superior direito.
3. Ache a fazenda pelo nome, mude o que quiser.
4. Role até o fim e clique em **Commit changes**.

Pronto. Um minuto depois está no ar.

Para tirar uma fazenda sem apagá-la, coloque `"confidencial": true`. Ela sai da
listagem pública e passa a ser tratada só no atendimento.

---

## Colocar uma fazenda nova

1. Entre na pasta **`entrada`**.
2. **Add file → Upload files**, solte o PDF do one-pager, salve.
3. Espere alguns minutos. Um robô recorta as 3 melhores fotos, lê o documento e
   abre uma **proposta de alteração** (aba *Pull requests*) com a ficha quase pronta.
4. Abra a ficha em `fichas/`, preencha os campos com o texto do próprio documento
   — que está no fim do arquivo — e aprove.

O robô transcreve o que dá e deixa em branco o que o documento não traz. Não
invente o que falta: campo vazio o site simplesmente não mostra.

---

## Publicar um texto no Radar Agro

Edite **`data/articles.json`**. Cada texto precisa de título, resumo, autor ou
fonte, e data. Quando tiver três textos de verdade publicados, troque
`"secao_em_preparacao": true` para `false` e o aviso de seção em preparação some.

As **manchetes do mercado** que aparecem ao lado são outra coisa: o robô as busca
sozinho todo dia às 9h, em veículos do setor, e mostra só título, veículo e link.
Não precisa fazer nada. Para trocar as fontes, edite `data/noticias-fontes.json`.

---

## Colocar um evento na Agenda Agro

Edite **`data/events.json`**:

```json
{
  "nome": "Bahia Farm Show",
  "inicio": "2027-06-08",
  "fim": "2027-06-12",
  "cidade": "Luís Eduardo Magalhães",
  "estado": "BA",
  "segmento": "Agronegócio",
  "url": "https://endereco-oficial-do-evento.com.br",
  "prime": true
}
```

`"prime": true` marca os eventos em que a Prime estará presente. **Evento que já
passou some sozinho** — não precisa limpar nada.

Enquanto `events.json` estiver vazio, a página avisa que a agenda está em
montagem. Isso é proposital: melhor uma agenda vazia do que uma data errada.

Há um ponto de partida pronto em **`data/events-rascunho.json`** — dez feiras
com data e link oficial já levantados. O site não lê esse arquivo. Confira a
data no link `_fonte` de cada uma e, ao confirmar, copie o evento para
`events.json` apagando os campos que começam com `_`.

---

## Trocar telefone, e-mail, CRECI, Instagram

Tudo em **`data/site.json`**. Campo vazio some do site: se apagar o WhatsApp, o
botão flutuante desaparece.

---

## Se você errar

Existe uma conferência automática. Antes de publicar, ela verifica se os arquivos
estão bem formados, se as fotos citadas existem de fato e se não sobrou dado de
teste. **Se algo estiver errado, a publicação para e o site no ar continua
intacto** — você recebe um e-mail dizendo o que corrigir.

Para ver o que aconteceu, entre na aba **Actions**.

---

## O que roda sozinho

| Quando | O quê |
|---|---|
| A cada alteração | Conferência dos dados; publicação no Netlify |
| Todo dia, 9h | Manchetes do mercado no Radar Agro |
| Ao subir um PDF | Fotos recortadas e ficha preparada para revisão |
| Sempre | Evento vencido sai da agenda |

---

## Onde o site vive

| | |
|---|---|
| Endereço | https://primefazendas.com |
| Netlify | projeto `super-gumption-758fa9`, conta primefazendasto@gmail.com |
| Repositório | `afiac1988/prime-fazendas-site-a1b14` |

**Cuidado com o repositório.** Existe outro parecido, `prime-fazendas-site`, sem o
sufixo. Aquele não publica nada. É este, com `-a1b14`.

---

## Uma coisa que não dá para fazer aqui

Não edite os arquivos `.html` na mão. Eles são gerados a partir de `tools/`, e a
conferência automática recusa a publicação se eles não baterem. Texto de página
se muda em `tools/pages.py`.

Conteúdo — fazenda, notícia, evento, contato — é tudo em `data/`, e esse você
mexe à vontade.
