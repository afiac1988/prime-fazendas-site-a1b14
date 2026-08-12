#!/usr/bin/env python3
"""Conteúdo de cada página. Rode `python3 tools/pages.py` para gerar o site."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import pagina, capa, SITE  # noqa: E402

feitos = []

# =========================================================================== #
#  INÍCIO                                                                     #
# =========================================================================== #
HOME = """
  <section class="hero">
    <div class="hero__fundo">
      <img src="assets/img/hero-matopiba.svg" alt="" width="2400" height="1240" fetchpriority="high" decoding="async">
    </div>

    <div class="env hero__grade">
      <div class="hero__texto">
        <p class="olho">Imobiliária rural &middot; MATOPIBA</p>
        <h1 class="display hero__titulo">Terras que produzem.<em>Oportunidades que conectam.</em></h1>
        <p class="hero__apoio">
          Compra, venda e arrendamento de propriedades rurais no MATOPIBA e nas fronteiras
          agrícolas vizinhas, com experiência imobiliária, conhecimento regional e atendimento a
          investidores do Brasil e do exterior.
        </p>
        <div class="acoes">
          <a class="btn btn--claro" href="oportunidades.html">Explorar oportunidades</a>
          <a class="btn btn--fantasma" href="contato.html">Falar com a Prime</a>
        </div>
      </div>

      <aside class="painel" aria-label="Seleção atual de propriedades">
        <div class="painel__topo">
          <p class="painel__titulo">Seleção atual</p>
          <p class="painel__contagem" data-painel-contagem>&nbsp;</p>
        </div>
        <ul class="painel__lista" data-imoveis-painel>
          <li><a class="mini" href="oportunidades.html"><span><span class="mini__nome">Carregando a seleção&hellip;</span></span></a></li>
        </ul>
        <div class="painel__pe">
          <a class="elo" href="oportunidades.html">Ver todas as oportunidades</a>
        </div>
      </aside>
    </div>
  </section>

  <section class="busca-faixa" aria-label="Busca de propriedades">
    <div class="env">
      <form class="busca" data-busca-home>
        <div class="campo">
          <label for="b-finalidade">Finalidade</label>
          <select id="b-finalidade" name="finalidade">
            <option value="">Comprar ou arrendar</option>
            <option value="venda">Comprar</option>
            <option value="arrendamento">Arrendar</option>
          </select>
        </div>
        <div class="campo">
          <label for="b-estado">Estado</label>
          <select id="b-estado" name="estado">
            <option value="">Todos os estados</option>
            <option value="MA">Maranhão</option>
            <option value="TO">Tocantins</option>
            <option value="PI">Piauí</option>
            <option value="BA">Bahia</option>
          </select>
        </div>
        <div class="campo">
          <label for="b-tipo">Tipo</label>
          <select id="b-tipo" name="tipo">
            <option value="">Todos os tipos</option>
            <option value="agricola">Agrícola</option>
            <option value="pecuaria">Pecuária</option>
            <option value="integracao">Integração lavoura-pecuária</option>
            <option value="florestal">Reflorestamento</option>
            <option value="investimento">Investimento e patrimônio</option>
          </select>
        </div>
        <div class="campo">
          <label for="b-area">Área</label>
          <select id="b-area" name="area">
            <option value="">Qualquer área</option>
            <option value="ate500">Até 500 ha</option>
            <option value="500a1500">500 a 1.500 ha</option>
            <option value="acima1500">Acima de 1.500 ha</option>
          </select>
        </div>
        <button class="btn" type="submit">Buscar</button>
      </form>
    </div>
  </section>

  <section class="secao" aria-labelledby="t-oportunidades">
    <div class="env">
      <div class="cabeca-secao cabeca-secao--dupla">
        <p class="olho"><span class="numero-secao">01</span> Carteira</p>
        <h2 class="titulo" id="t-oportunidades">Oportunidades selecionadas</h2>
        <p class="subtitulo">
          Cada fazenda da carteira leva o nome de uma pedra — são ativos únicos, apresentados com
          clareza para objetivos produtivos, patrimoniais e de investimento.
        </p>
      </div>

      <div class="grade grade--3" data-imoveis-destaque></div>

      <p style="margin-top:2.5rem"><a class="elo" href="oportunidades.html">Ver todas as oportunidades</a></p>
    </div>
  </section>

  <section class="secao secao--escura" aria-labelledby="t-experiencia">
    <div class="env">
      <div class="numeros">
        <div class="numero" data-revela>
          <span class="numero__valor">3+</span>
          <span class="numero__rotulo">anos de atuação da Prime Fazendas</span>
        </div>
        <div class="numero" data-revela>
          <span class="numero__valor">18</span>
          <span class="numero__rotulo">anos de experiência do fundador no mercado imobiliário</span>
        </div>
        <div data-revela>
          <h2 class="titulo-menor" id="t-experiencia" style="margin-bottom:.8rem">
            Experiência construída no relacionamento
          </h2>
          <p class="subtitulo">
            No conhecimento do mercado e na condução responsável de cada negociação — do primeiro
            contato à assinatura.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="secao" aria-labelledby="t-matopiba">
    <div class="env">
      <div class="regiao">
        <div class="regiao__mapa" data-revela>
          <img src="assets/img/mapa-matopiba.svg" alt="Mapa esquemático do Brasil com a região do MATOPIBA destacada, abrangendo Maranhão, Tocantins, Piauí e Bahia." width="600" height="640" loading="lazy" decoding="async">
          <p class="regiao__nota">Representação esquemática, sem finalidade cartográfica.</p>
        </div>

        <div>
          <p class="olho"><span class="numero-secao">02</span> Região</p>
          <h2 class="titulo" id="t-matopiba" style="margin-bottom:1.1rem">
            Conhecimento regional para decisões de alcance global.
          </h2>
          <p class="subtitulo">
            Com atuação no Maranhão, Tocantins, Piauí e Bahia — e nas fronteiras agrícolas
            vizinhas — a Prime Fazendas aproxima o conhecimento local dos interesses de produtores,
            empresas e investidores nacionais e internacionais.
          </p>

          <div class="estados">
            <a class="estado" href="oportunidades.html?estado=MA">
              <img src="assets/img/estado-ma.svg" alt="" width="900" height="700" loading="lazy" decoding="async">
              <span class="estado__texto"><span class="estado__sigla">MA</span><span class="estado__nome">Maranhão</span></span>
            </a>
            <a class="estado" href="oportunidades.html?estado=TO">
              <img src="assets/img/estado-to.svg" alt="" width="900" height="700" loading="lazy" decoding="async">
              <span class="estado__texto"><span class="estado__sigla">TO</span><span class="estado__nome">Tocantins</span></span>
            </a>
            <a class="estado" href="oportunidades.html?estado=PI">
              <img src="assets/img/estado-pi.svg" alt="" width="900" height="700" loading="lazy" decoding="async">
              <span class="estado__texto"><span class="estado__sigla">PI</span><span class="estado__nome">Piauí</span></span>
            </a>
            <a class="estado" href="oportunidades.html?estado=BA">
              <img src="assets/img/estado-ba.svg" alt="" width="900" height="700" loading="lazy" decoding="async">
              <span class="estado__texto"><span class="estado__sigla">BA</span><span class="estado__nome">Bahia</span></span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="secao secao--marfim" aria-labelledby="t-frentes">
    <div class="env">
      <div class="cabeca-secao">
        <p class="olho"><span class="numero-secao">03</span> Como atuamos</p>
        <h2 class="titulo" id="t-frentes">Comprar, vender e arrendar</h2>
      </div>

      <div class="frentes">
        <article class="frente" data-revela>
          <p class="frente__indice">01</p>
          <h3>Comprar</h3>
          <p>Áreas apresentadas com aptidão, escala, logística e recurso hídrico à mostra — o que
          basta para você decidir se vale a visita.</p>
          <p><a class="elo" href="oportunidades.html">Explorar oportunidades</a></p>
        </article>
        <article class="frente" data-revela>
          <p class="frente__indice">02</p>
          <h3>Vender</h3>
          <p>Sua propriedade chega ao comprador certo sem circular de mão em mão. Você decide o
          que é publicado e quando.</p>
          <p><a class="elo" href="anuncie.html">Anunciar propriedade</a></p>
        </article>
        <article class="frente" data-revela>
          <p class="frente__indice">03</p>
          <h3>Arrendar</h3>
          <p>Áreas disponíveis conectadas a produtores e empresas em expansão, com prazo e
          condições acertados entre as partes.</p>
          <p><a class="elo" href="arrendamentos.html">Ver arrendamentos</a></p>
        </article>
      </div>
    </div>
  </section>

  <section class="secao" aria-labelledby="t-verticais">
    <div class="env">
      <div class="cabeca-secao cabeca-secao--dupla">
        <p class="olho"><span class="numero-secao">04</span> Verticais</p>
        <h2 class="titulo" id="t-verticais">Frentes de atuação</h2>
        <p class="subtitulo">
          Cada área é apresentada pela vocação que já tem — lavoura consolidada, pastagem formada,
          integração, projeto florestal ou patrimônio. Sem forçar o imóvel a um rótulo que não é o dele.
        </p>
      </div>

      <div class="verticais">
        <a class="pilula" href="oportunidades.html?tipo=agricola">Agricultura</a>
        <a class="pilula" href="oportunidades.html?tipo=pecuaria">Pecuária</a>
        <a class="pilula" href="oportunidades.html?tipo=integracao">Integração lavoura-pecuária</a>
        <a class="pilula" href="oportunidades.html?tipo=florestal">Reflorestamento e ativos florestais</a>
        <a class="pilula" href="oportunidades.html?tipo=investimento">Investimento e patrimônio rural</a>
      </div>
    </div>
  </section>

  <section class="secao secao--marfim" aria-labelledby="t-radar">
    <div class="env">
      <div class="editorial">
        <div>
          <div class="cabeca-secao">
            <p class="olho"><span class="numero-secao">05</span> Radar Agro</p>
            <h2 class="titulo" id="t-radar">Informação para quem decide sobre a terra.</h2>
          </div>

          <div class="aviso" data-radar-preparacao>
            <p><strong>Seção em preparação.</strong> Os textos abaixo são modelos de pauta. Publicamos
            apenas conteúdo revisado, com fonte e data verificadas.</p>
          </div>

          <div data-radar="3"></div>
          <p style="margin-top:2rem"><a class="elo" href="radar-agro.html">Ver o Radar Agro</a></p>
        </div>

        <div style="display:grid;gap:clamp(2rem,4vw,3rem);align-content:start">
          <div data-bloco>
            <div class="cabeca-secao" style="margin-bottom:1.25rem">
              <p class="olho">Últimas do mercado</p>
              <h2 class="titulo-menor">O que saiu hoje</h2>
            </div>
            <ul class="manchetes" data-mercado="5"></ul>
            <p class="carimbo" data-mercado-atualizado></p>
          </div>

          <div>
            <div class="cabeca-secao" style="margin-bottom:1.25rem">
              <p class="olho">Agenda Agro</p>
              <h2 class="titulo-menor">Próximos eventos</h2>
            </div>
            <div data-agenda="3"></div>
            <p style="margin-top:1.5rem"><a class="elo" href="agenda-agro.html">Ver a agenda</a></p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="secao" aria-labelledby="t-quem">
    <div class="env">
      <div class="retrato">
        <figure class="retrato__figura" data-revela style="margin:0">
          <img src="assets/img/fundador.webp" alt="André Amorim, fundador da Prime Fazendas." width="1100" height="1159" loading="lazy" decoding="async">
          <figcaption class="retrato__legenda">André Amorim &middot; fundador da Prime Fazendas</figcaption>
        </figure>

        <div>
          <p class="olho"><span class="numero-secao">06</span> Quem somos</p>
          <h2 class="titulo" id="t-quem" style="margin-bottom:1.1rem">Experiência imobiliária. Presença no campo.</h2>
          <p class="subtitulo">
            A Prime Fazendas atua há mais de três anos na conexão de oportunidades de compra, venda e
            arrendamento de propriedades rurais. À frente da empresa, seu fundador reúne 18 anos de
            experiência no mercado imobiliário, conduzindo relacionamentos e negociações com
            proximidade, discrição e responsabilidade.
          </p>

          <div class="pilares">
            <div class="pilar"><p class="pilar__nome">Experiência</p><p class="pilar__texto">Mais de três anos de Prime Fazendas e 18 anos de mercado imobiliário à frente da empresa.</p></div>
            <div class="pilar"><p class="pilar__nome">Conhecimento regional</p><p class="pilar__texto">Atuação concentrada no MATOPIBA e nas suas características produtivas e logísticas.</p></div>
            <div class="pilar"><p class="pilar__nome">Conexão</p><p class="pilar__texto">Aproximação entre proprietários, produtores, empresas e investidores do Brasil e do exterior.</p></div>
            <div class="pilar"><p class="pilar__nome">Curadoria</p><p class="pilar__texto">Oportunidades apresentadas com informações objetivas e atendimento especializado.</p></div>
            <div class="pilar"><p class="pilar__nome">Discrição</p><p class="pilar__texto">A região é pública; endereço, matrícula e visita são tratados no atendimento — quem vende mantém o controle da negociação.</p></div>
          </div>

          <p style="margin-top:2rem"><a class="elo" href="quem-somos.html">Conheça a Prime Fazendas</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="secao chamada" aria-labelledby="t-cta">
    <div class="chamada__fundo">
      <img src="assets/img/hero-matopiba.svg" alt="" width="2400" height="1240" loading="lazy" decoding="async">
    </div>
    <div class="env env-estreito">
      <p class="olho olho--centro">Contato</p>
      <h2 class="titulo" id="t-cta" style="margin-bottom:1rem">Toda boa negociação começa com a conversa certa.</h2>
      <p class="subtitulo" style="margin:0 auto 2rem;color:rgba(244,241,233,.8)">
        Seja para comprar, vender ou arrendar, converse com quem conhece o mercado, a região e o
        peso de cada informação que circula.
      </p>
      <div class="acoes">
        <a class="btn btn--claro" href="contato.html">Falar com um especialista</a>
        <a class="btn btn--fantasma" href="anuncie.html">Anunciar propriedade</a>
      </div>
    </div>
  </section>
"""

LD_HOME = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"RealEstateAgent","name":"Prime Fazendas","url":"https://primefazendas.com/","slogan":"Terras que produzem. Oportunidades que conectam.","description":"Imobiliária rural especializada em compra, venda e arrendamento de propriedades no MATOPIBA.","areaServed":[{"@type":"State","name":"Maranhão"},{"@type":"State","name":"Tocantins"},{"@type":"State","name":"Piauí"},{"@type":"State","name":"Bahia"}],"knowsLanguage":["pt-BR","en"]}
</script>
<link rel="preload" as="image" href="assets/img/hero-matopiba.svg" fetchpriority="high">
"""

feitos.append(pagina(
    arquivo="index.html", lang="pt", atual="index.html",
    titulo="Prime Fazendas — Compra, venda e arrendamento de propriedades rurais no MATOPIBA",
    og_titulo="Prime Fazendas — Terras que produzem. Oportunidades que conectam.",
    descricao="Imobiliária rural especializada no MATOPIBA. Conectamos proprietários, produtores e investidores nacionais e internacionais a oportunidades de compra, venda e arrendamento.",
    canonico=SITE + "/", alternativo=SITE + "/en/",
    head_extra=LD_HOME, conteudo=HOME,
))


# =========================================================================== #
#  FILTROS reaproveitados                                                     #
# =========================================================================== #
def filtros(com_finalidade=True, rotulo_tipo="Tipo de propriedade"):
    fin = """
        <div class="campo">
          <label for="f-finalidade">Finalidade</label>
          <select id="f-finalidade" name="finalidade">
            <option value="">Comprar ou arrendar</option>
            <option value="venda">Comprar</option>
            <option value="arrendamento">Arrendar</option>
          </select>
        </div>""" if com_finalidade else ""

    return f"""      <form class="filtros" data-filtros>{fin}
        <div class="campo">
          <label for="f-estado">Localização</label>
          <select id="f-estado" name="estado">
            <option value="">Todas as localizações</option>
          </select>
        </div>
        <div class="campo">
          <label for="f-tipo">{rotulo_tipo}</label>
          <select id="f-tipo" name="tipo">
            <option value="">Todos os tipos</option>
            <option value="agricola">Agrícola</option>
            <option value="pecuaria">Pecuária</option>
            <option value="integracao">Integração lavoura-pecuária</option>
            <option value="florestal">Reflorestamento</option>
            <option value="investimento">Investimento e patrimônio</option>
          </select>
        </div>
        <div class="campo">
          <label for="f-area">Área</label>
          <select id="f-area" name="area">
            <option value="">Qualquer área</option>
            <option value="ate500">Até 500 ha</option>
            <option value="500a1500">500 a 1.500 ha</option>
            <option value="acima1500">Acima de 1.500 ha</option>
          </select>
        </div>
        <div class="campo">
          <label for="f-ordem">Ordenar por</label>
          <select id="f-ordem" name="ordem">
            <option value="">Relevância</option>
            <option value="area-desc">Maior área</option>
            <option value="area-asc">Menor área</option>
          </select>
        </div>
        <div class="filtros__acoes">
          <button class="btn" type="submit">Aplicar filtros</button>
          <button class="btn btn--linha" type="button" data-limpar>Limpar</button>
        </div>
      </form>
"""


AVISO_CATALOGO = """      <div class="aviso">
        <p><strong>Apresentamos a região, não o endereço.</strong> É deliberado: protege o
        proprietário da intermediação indesejada. Endereço, matrícula e visita são tratados no
        atendimento. <a href="contato.html">Fale com a equipe</a> — parte da carteira nunca é publicada.</p>
      </div>
"""

# =========================================================================== #
#  OPORTUNIDADES                                                              #
# =========================================================================== #
feitos.append(pagina(
    arquivo="oportunidades.html", lang="pt", atual="oportunidades.html",
    titulo="Oportunidades — Fazendas à venda no MATOPIBA | Prime Fazendas",
    descricao="Propriedades rurais para compra no Maranhão, Tocantins, Piauí e Bahia. Filtre por estado, tipo de propriedade e área.",
    alternativo=SITE + "/en/opportunities.html",
    conteudo=capa(
        "Carteira", "Oportunidades",
        "Cada fazenda leva o nome de uma pedra — são ativos únicos. Área, aptidão, infraestrutura, logística e recurso hídrico conforme informado pelo proprietário.",
        [("index.html", "Início"), ("", "Oportunidades")],
    ) + f"""
  <section class="secao">
    <div class="env">
{AVISO_CATALOGO}{filtros()}
      <div class="resultado-info"><span data-resultado-info></span></div>
      <div class="grade grade--3" data-imoveis-catalogo></div>

      <div class="aviso" style="margin-top:3rem">
        <p><strong>Por que apresentamos a região, e não o endereço.</strong> Publicar a localização
        exata de uma fazenda expõe o proprietário a intermediação indesejada e tira dele o controle
        da negociação. A região basta para você avaliar aptidão, logística e escala; o endereço, a
        matrícula e a visita são tratados no atendimento, com o proprietário ciente.</p>
      </div>

      <div class="aviso">
        <p>Nem toda oportunidade é publicada. Parte da carteira é apresentada apenas em contato
        direto, por solicitação do proprietário. <a href="contato.html">Fale com a equipe</a> para
        conhecer o que não está listado aqui.</p>
      </div>
    </div>
  </section>
""",
))

# =========================================================================== #
#  ARRENDAMENTOS                                                              #
# =========================================================================== #
feitos.append(pagina(
    arquivo="arrendamentos.html", lang="pt", atual="arrendamentos.html",
    titulo="Arrendamentos — Áreas rurais para arrendar no MATOPIBA | Prime Fazendas",
    descricao="Áreas disponíveis para arrendamento agrícola e pecuário no MATOPIBA. Condições, prazo e safra definidos entre as partes.",
    alternativo=SITE + "/en/leases.html",
    conteudo=capa(
        "Arrendamentos", "Áreas para arrendamento",
        "Conectamos áreas disponíveis a produtores e empresas que buscam ampliar suas operações. Prazo, safra e condições são definidos entre as partes.",
        [("index.html", "Início"), ("", "Arrendamentos")],
    ) + f"""
  <section class="secao">
    <div class="env">
{AVISO_CATALOGO}{filtros(com_finalidade=False, rotulo_tipo="Atividade")}
      <div class="resultado-info"><span data-resultado-info></span></div>
      <div class="grade grade--3" data-imoveis-catalogo data-finalidade="arrendamento"></div>
    </div>
  </section>

  <section class="secao secao--marfim">
    <div class="env">
      <div class="cabeca-secao">
        <p class="olho">Como funciona</p>
        <h2 class="titulo">O que definimos antes de aproximar as partes</h2>
      </div>
      <div class="frentes">
        <article class="frente">
          <p class="frente__indice">01</p>
          <h3>Área e atividade</h3>
          <p>Extensão disponível, aptidão da área e atividade pretendida pelo arrendatário.</p>
        </article>
        <article class="frente">
          <p class="frente__indice">02</p>
          <h3>Prazo e safra</h3>
          <p>Horizonte do contrato e safras contempladas, conforme o interesse do proprietário.</p>
        </article>
        <article class="frente">
          <p class="frente__indice">03</p>
          <h3>Condições</h3>
          <p>Valores e demais condições são tratados caso a caso, com discrição, entre as partes.</p>
        </article>
      </div>
      <p style="margin-top:2.5rem"><a class="btn" href="contato.html">Falar sobre arrendamento</a></p>
    </div>
  </section>
""",
))

# =========================================================================== #
#  PÁGINA DA PROPRIEDADE                                                      #
# =========================================================================== #
feitos.append(pagina(
    arquivo="propriedade.html", lang="pt", atual="oportunidades.html",
    titulo="Propriedade | Prime Fazendas",
    descricao="Ficha da propriedade rural: área, finalidade, aptidão, infraestrutura e contato com a equipe da Prime Fazendas.",
    head_extra='<meta name="robots" content="noindex">\n',
    conteudo="""
  <section class="capa">
    <div class="env">
      <nav class="migalhas" aria-label="Trilha de navegação"><ol>
        <li><a href="index.html">Início</a></li>
        <li><a href="oportunidades.html">Oportunidades</a></li>
        <li><span data-slot="nome">Propriedade</span></li>
      </ol></nav>
      <p class="olho"><span data-slot="finalidade">&nbsp;</span> &middot; <span data-slot="local">&nbsp;</span></p>
      <h1 class="titulo" data-slot="nome">&nbsp;</h1>
      <p class="subtitulo" style="margin-top:1.1rem" data-slot="resumo">&nbsp;</p>
    </div>
  </section>

  <div data-propriedade>
    <section style="padding-block:clamp(1.5rem,3vw,2.5rem)">
      <div class="env">
        <div class="galeria" data-galeria></div>
      </div>
    </section>

    <section style="padding-bottom:var(--secao)">
      <div class="env">
        <div class="aviso" data-slot-exemplo>
          <p><strong>Ficha de exemplo.</strong> Este registro demonstra a apresentação padrão das
          propriedades. Os dados serão substituídos pelas informações reais autorizadas pelo proprietário.</p>
        </div>

        <div class="dados" style="margin-bottom:clamp(2rem,4vw,3rem)">
          <div class="dado"><p class="dado__rotulo">Área total</p><p class="dado__valor" data-slot="area">&nbsp;</p></div>
          <div class="dado" data-bloco><p class="dado__rotulo">Área aberta</p><p class="dado__valor" data-slot="area_aberta" data-esconder-vazio>&nbsp;</p></div>
          <div class="dado"><p class="dado__rotulo">Aptidão</p><p class="dado__valor" data-slot="aptidao">&nbsp;</p></div>
          <div class="dado"><p class="dado__rotulo">Finalidade</p><p class="dado__valor" data-slot="finalidade">&nbsp;</p></div>
          <div class="dado"><p class="dado__rotulo">Valor</p><p class="dado__valor" data-slot="preco">&nbsp;</p></div>
        </div>

        <div class="detalhe">
          <div class="conteudo">
            <h2>Sobre a propriedade</h2>
            <div data-slot-descricao></div>

            <div data-bloco>
              <h3>Infraestrutura</h3>
              <p data-slot="infraestrutura" data-esconder-vazio>&nbsp;</p>
            </div>

            <div data-bloco>
              <h3>Recurso hídrico</h3>
              <p data-slot="agua" data-esconder-vazio>&nbsp;</p>
            </div>

            <div data-bloco>
              <h3>Logística</h3>
              <p data-slot="logistica" data-esconder-vazio>&nbsp;</p>
            </div>

            <div data-bloco>
              <h3>Itens negociáveis à parte</h3>
              <p data-slot="opcional" data-esconder-vazio>&nbsp;</p>
            </div>

            <h3>Localização</h3>
            <p><span data-slot="local">&nbsp;</span>.</p>
            <p style="color:var(--tinta-2);font-size:.94rem">
              Apresentamos a região. O endereço exato, a matrícula e o agendamento de visita são
              tratados no atendimento, com o proprietário ciente — prática que protege quem vende
              da intermediação indesejada e mantém a negociação entre as partes.
            </p>

            <h3>Documentação</h3>
            <p data-slot="documentacao">&nbsp;</p>
            <p style="color:var(--tinta-2);font-size:.94rem">
              Os dados desta ficha vêm do proprietário. Acompanhamos a negociação do começo ao fim,
              e a conferência documental cabe às partes e aos seus assessores — é assim que deve ser.
            </p>
          </div>

          <aside class="lado">
            <p class="olho">Interesse</p>
            <h2 class="titulo-menor" style="margin-bottom:1rem">Fale sobre esta propriedade</h2>
            <form class="formulario" data-formulario action="#" method="post" novalidate>
              <input type="hidden" name="propriedade" data-slot-assunto value="">
              <div class="campo">
                <label for="p-nome">Nome</label>
                <input id="p-nome" name="nome" type="text" autocomplete="name" required>
              </div>
              <div class="campo">
                <label for="p-contato">Telefone ou WhatsApp</label>
                <input id="p-contato" name="telefone" type="tel" autocomplete="tel" required>
              </div>
              <div class="campo">
                <label for="p-email">E-mail</label>
                <input id="p-email" name="email" type="email" autocomplete="email" required>
              </div>
              <div class="campo">
                <label for="p-msg">Mensagem</label>
                <textarea id="p-msg" name="mensagem" rows="4"></textarea>
              </div>
              <label class="consentimento">
                <input type="checkbox" name="consentimento" required>
                <span>Autorizo o contato da Prime Fazendas e o tratamento dos meus dados conforme a
                <a href="privacidade.html">política de privacidade</a>.</span>
              </label>
              <button class="btn btn--bloco" type="submit">Enviar</button>
              <p class="retorno"></p>
            </form>
          </aside>
        </div>
      </div>
    </section>

    <section class="secao secao--marfim">
      <div class="env">
        <div class="cabeca-secao">
          <p class="olho">Também disponíveis</p>
          <h2 class="titulo-menor">Outras oportunidades</h2>
        </div>
        <div class="grade grade--3" data-relacionadas></div>
      </div>
    </section>
  </div>
""",
))

# =========================================================================== #
#  RADAR AGRO                                                                 #
# =========================================================================== #
feitos.append(pagina(
    arquivo="radar-agro.html", lang="pt", atual="radar-agro.html",
    titulo="Radar Agro — Informação para quem decide sobre a terra | Prime Fazendas",
    descricao="Mercado de terras, infraestrutura e logística, expansão agrícola, reflorestamento, crédito rural e legislação no MATOPIBA.",
    conteudo=capa(
        "Radar Agro", "Informação para quem decide sobre a terra.",
        "Leitura objetiva sobre mercado de terras, infraestrutura, expansão agrícola, reflorestamento, crédito e legislação relevante para o MATOPIBA.",
        [("index.html", "Início"), ("", "Radar Agro")],
    ) + """
  <section class="secao">
    <div class="env">
      <div class="aviso" data-radar-preparacao>
        <p><strong>Seção em preparação.</strong> Os itens abaixo são modelos de pauta. Publicamos apenas
        conteúdo revisado, com autoria, fonte e data verificadas — nunca reprodução automática de terceiros.</p>
      </div>

      <div class="verticais" style="margin-bottom:2.5rem">
        <span class="pilula">Mercado de terras</span>
        <span class="pilula">Infraestrutura e logística</span>
        <span class="pilula">Expansão agrícola</span>
        <span class="pilula">Reflorestamento</span>
        <span class="pilula">Crédito e investimento rural</span>
        <span class="pilula">Legislação</span>
      </div>

      <div class="editorial">
        <div data-radar="6"></div>
        <aside style="display:grid;gap:1.5rem;align-content:start">
          <div class="lado" data-bloco>
            <p class="olho">Últimas do mercado</p>
            <h2 class="titulo-menor" style="margin-bottom:1rem">O que saiu hoje</h2>
            <ul class="manchetes" data-mercado="8"></ul>
            <p class="carimbo" data-mercado-atualizado></p>
            <p class="carimbo">Manchetes de veículos do setor, com link para a publicação
            original. Conteúdo de terceiros, não da Prime.</p>
          </div>
          <div class="lado">
            <p class="olho">Agenda Agro</p>
            <h2 class="titulo-menor" style="margin-bottom:1rem">Próximos eventos</h2>
            <div data-agenda="4"></div>
            <p style="margin-top:1.5rem"><a class="elo" href="agenda-agro.html">Ver a agenda</a></p>
          </div>
        </aside>
      </div>
    </div>
  </section>
""",
))

# =========================================================================== #
#  AGENDA AGRO                                                                #
# =========================================================================== #
feitos.append(pagina(
    arquivo="agenda-agro.html", lang="pt", atual="agenda-agro.html",
    titulo="Agenda Agro — Feiras e eventos do agronegócio | Prime Fazendas",
    descricao="Próximos eventos e feiras do agronegócio com data, local, segmento e link oficial. Eventos encerrados saem da lista automaticamente.",
    conteudo=capa(
        "Agenda Agro", "Feiras e eventos do setor",
        "Publicamos apenas eventos confirmados, com data, local e link oficial verificados. Eventos encerrados saem da lista automaticamente.",
        [("index.html", "Início"), ("", "Agenda Agro")],
    ) + """
  <section class="secao">
    <div class="env">
      <div style="max-width:820px">
        <div data-agenda="20"></div>
      </div>

      <div class="aviso" style="margin-top:3rem">
        <p>Organiza um evento do setor no MATOPIBA e quer vê-lo aqui?
        <a href="contato.html">Envie as informações</a> com data, local e link oficial.</p>
      </div>
    </div>
  </section>
""",
))

# =========================================================================== #
#  QUEM SOMOS                                                                 #
# =========================================================================== #
feitos.append(pagina(
    arquivo="quem-somos.html", lang="pt", atual="quem-somos.html",
    titulo="Quem Somos — Prime Fazendas, imobiliária rural no MATOPIBA",
    descricao="Mais de três anos de atuação e um fundador com 18 anos de experiência no mercado imobiliário, com atuação concentrada no MATOPIBA.",
    alternativo=SITE + "/en/about.html",
    conteudo=capa(
        "Quem somos", "Experiência imobiliária. Presença no campo.",
        "A Prime Fazendas conecta proprietários, produtores e investidores a oportunidades de compra, venda e arrendamento de propriedades rurais.",
        [("index.html", "Início"), ("", "Quem Somos")],
    ) + """
  <section class="secao">
    <div class="env">
      <div class="retrato">
        <figure class="retrato__figura" style="margin:0" data-revela>
          <img src="assets/img/fundador.webp" alt="André Amorim, fundador da Prime Fazendas." width="1100" height="1159" loading="lazy" decoding="async">
          <figcaption class="retrato__legenda">André Amorim &middot; fundador da Prime Fazendas</figcaption>
        </figure>

        <div class="conteudo">
          <p>
            A Prime Fazendas atua há mais de três anos na conexão de oportunidades de compra, venda e
            arrendamento de propriedades rurais. À frente da empresa, seu fundador reúne 18 anos de
            experiência no mercado imobiliário, conduzindo relacionamentos e negociações com
            proximidade, discrição e responsabilidade.
          </p>
          <p>
            Com atuação estratégica no MATOPIBA e nas fronteiras agrícolas vizinhas, aproximamos
            proprietários, produtores, empresas e investidores nacionais e internacionais de
            propriedades alinhadas aos seus objetivos.
          </p>

          <h2>O fundador</h2>
          <p>
            <strong>André Amorim</strong> é CEO e sócio do Grupo Costa do Sol, casa com quatro
            décadas de trajetória, e responde hoje por mais de 10 mil hectares em ativos rurais no
            Tocantins. São 18 anos de mercado imobiliário, mais de uma década dedicada à
            estruturação de propriedades rurais de alto valor e sociedade em imobiliárias em São
            Paulo e no Tocantins. Corretor inscrito no CRECI/TO sob o nº 2122.
          </p>

          <h2>Discrição não é formalidade — é o método</h2>
          <p>
            No mercado de terras, uma informação solta na hora errada custa caro ao proprietário.
            Endereço exato circulando antes da hora atrai intermediação indesejada, multiplica
            interlocutores e tira de quem vende o controle da própria negociação.
          </p>
          <p>
            Por isso o catálogo apresenta a região, a aptidão, a escala, a logística e o recurso
            hídrico — o suficiente para um comprador sério avaliar se faz sentido. Endereço,
            matrícula e visita entram depois, no atendimento, com o proprietário ciente de cada
            passo. Quem procura terra de verdade não perde nada com isso. Quem procura repassar
            contato, sim.
          </p>

          <h2>Como trabalhamos</h2>
          <ul>
            <li>Entendimento do objetivo antes da apresentação de qualquer área.</li>
            <li>Levantamento das informações disponíveis junto ao proprietário.</li>
            <li>Apresentação objetiva, com o que está confirmado e o que ainda depende de verificação.</li>
            <li>Condução da conversa entre as partes, com confidencialidade quando solicitada.</li>
            <li>Acompanhamento até a conclusão, respeitando o papel dos assessores jurídicos de cada lado.</li>
          </ul>

          <h2>O que não fazemos</h2>
          <ul>
            <li>Não divulgamos informação não confirmada como se fosse verificada.</li>
            <li>Não publicamos a localização exata das propriedades da carteira.</li>
            <li>Não prometemos rentabilidade, aprovação documental ou segurança jurídica.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="secao secao--escura">
    <div class="env">
      <div class="cabeca-secao">
        <p class="olho">Pilares</p>
        <h2 class="titulo">O que sustenta cada negociação</h2>
      </div>
      <div class="pilares">
        <div class="pilar"><p class="pilar__nome">Experiência</p><p class="pilar__texto">Mais de três anos de Prime Fazendas e 18 anos de mercado imobiliário à frente da empresa.</p></div>
        <div class="pilar"><p class="pilar__nome">Conhecimento regional</p><p class="pilar__texto">Atuação concentrada no MATOPIBA e nas suas características produtivas, logísticas e imobiliárias.</p></div>
        <div class="pilar"><p class="pilar__nome">Conexão</p><p class="pilar__texto">Aproximação entre proprietários, produtores, empresas e investidores do Brasil e do exterior.</p></div>
        <div class="pilar"><p class="pilar__nome">Curadoria</p><p class="pilar__texto">Oportunidades apresentadas com informações objetivas e atendimento especializado.</p></div>
        <div class="pilar"><p class="pilar__nome">Discrição</p><p class="pilar__texto">A região é pública; o endereço, a matrícula e a visita são tratados no atendimento, com o proprietário ciente.</p></div>
        <div class="pilar"><p class="pilar__nome">Confiança</p><p class="pilar__texto">Condução profissional e clareza durante todo o relacionamento comercial.</p></div>
      </div>
    </div>
  </section>

  <section class="secao secao--marfim">
    <div class="env env-estreito" style="text-align:center">
      <h2 class="titulo" style="margin-bottom:1rem">Vamos conversar</h2>
      <p class="subtitulo" style="margin:0 auto 2rem">
        Conte o que procura ou o que pretende negociar. A conversa é o começo de tudo.
      </p>
      <div class="acoes" style="justify-content:center">
        <a class="btn" href="contato.html">Falar com um especialista</a>
        <a class="btn btn--linha" href="anuncie.html">Anunciar propriedade</a>
      </div>
    </div>
  </section>
""",
))

# =========================================================================== #
#  CONTATO                                                                    #
# =========================================================================== #
feitos.append(pagina(
    arquivo="contato.html", lang="pt", atual="contato.html",
    titulo="Contato — Prime Fazendas",
    descricao="Fale com a equipe da Prime Fazendas sobre compra, venda ou arrendamento de propriedades rurais no MATOPIBA.",
    alternativo=SITE + "/en/contact.html",
    conteudo=capa(
        "Contato", "Toda boa negociação começa com a conversa certa.",
        "Conte o que procura ou o que pretende negociar. Quanto mais claro o objetivo, mais direta é a resposta. Retornamos em até dois dias úteis.",
        [("index.html", "Início"), ("", "Contato")],
    ) + """
  <section class="secao">
    <div class="env">
      <div class="detalhe">
        <div>
          <form class="formulario formulario--duplo" data-formulario action="#" method="post" novalidate>
            <div class="campo">
              <label for="c-nome">Nome</label>
              <input id="c-nome" name="nome" type="text" autocomplete="name" required>
            </div>
            <div class="campo">
              <label for="c-tel">Telefone ou WhatsApp</label>
              <input id="c-tel" name="telefone" type="tel" autocomplete="tel" required>
            </div>
            <div class="campo">
              <label for="c-email">E-mail</label>
              <input id="c-email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="campo">
              <label for="c-assunto">Assunto</label>
              <select id="c-assunto" name="assunto">
                <option value="comprar">Quero comprar</option>
                <option value="vender">Quero vender</option>
                <option value="arrendar">Quero arrendar</option>
                <option value="investir">Investimento</option>
                <option value="outro">Outro assunto</option>
              </select>
            </div>
            <div class="campo campo--largo">
              <label for="c-msg">Mensagem</label>
              <textarea id="c-msg" name="mensagem" rows="6" required></textarea>
              <p class="campo__dica">Quanto mais claro o objetivo, mais direta a resposta.</p>
            </div>
            <label class="consentimento">
              <input type="checkbox" name="consentimento" required>
              <span>Autorizo o contato da Prime Fazendas e o tratamento dos meus dados conforme a
              <a href="privacidade.html">política de privacidade</a>.</span>
            </label>
            <div class="campo--largo">
              <button class="btn" type="submit">Enviar mensagem</button>
            </div>
            <p class="retorno"></p>
          </form>
        </div>

        <aside class="lado">
          <p class="olho">Canais</p>
          <h2 class="titulo-menor" style="margin-bottom:1.2rem">Fale direto</h2>
          <ul class="rodape__lista" style="color:var(--tinta)">
            <li data-bloco><strong>E-mail:</strong> <a data-campo="email" data-esconder-vazio href="#">&nbsp;</a></li>
            <li data-bloco><strong>Telefone:</strong> <a data-campo="telefone" data-esconder-vazio href="#">&nbsp;</a></li>
            <li data-bloco><strong>CRECI jurídico:</strong> <span data-campo="creci" data-esconder-vazio>&nbsp;</span></li>
            <li data-bloco><strong>Responsável técnico:</strong> <span data-campo="responsavel_tecnico" data-esconder-vazio>&nbsp;</span> — <span data-campo="creci_responsavel" data-esconder-vazio>&nbsp;</span></li>
            <li data-bloco><strong>Endereço:</strong> <span data-campo="endereco" data-esconder-vazio>&nbsp;</span></li>
          </ul>
          <p style="margin-top:1.5rem;color:var(--tinta-2);font-size:.9rem">
            Atendemos em português e inglês. Conversas sobre propriedades sob confidencialidade são
            conduzidas apenas por contato direto.
          </p>
          <p style="margin-top:1.5rem">
            <a class="btn btn--linha btn--bloco" data-zap="Olá! Gostaria de falar com a Prime Fazendas." href="#">Falar pelo WhatsApp</a>
          </p>
        </aside>
      </div>
    </div>
  </section>
""",
))

# =========================================================================== #
#  ANUNCIE SUA PROPRIEDADE                                                    #
# =========================================================================== #
feitos.append(pagina(
    arquivo="anuncie.html", lang="pt", atual="",
    titulo="Anuncie sua propriedade — Prime Fazendas",
    descricao="Apresente sua propriedade rural ao mercado com estratégia, discrição e atendimento especializado no MATOPIBA.",
    conteudo=capa(
        "Proprietários", "Anuncie sua propriedade",
        "Sua fazenda chega ao comprador certo sem circular de mão em mão. Você decide o que é publicado, quando e para quem.",
        [("index.html", "Início"), ("", "Anuncie sua propriedade")],
    ) + """
  <section class="secao">
    <div class="env">
      <div class="detalhe">
        <div>
          <form class="formulario formulario--duplo" data-formulario action="#" method="post" enctype="multipart/form-data" novalidate>
            <div class="campo">
              <label for="a-nome">Nome</label>
              <input id="a-nome" name="nome" type="text" autocomplete="name" required>
            </div>
            <div class="campo">
              <label for="a-tel">Telefone ou WhatsApp</label>
              <input id="a-tel" name="telefone" type="tel" autocomplete="tel" required>
            </div>
            <div class="campo">
              <label for="a-email">E-mail</label>
              <input id="a-email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="campo">
              <label for="a-negocio">Tipo de negócio</label>
              <select id="a-negocio" name="negocio" required>
                <option value="venda">Venda</option>
                <option value="arrendamento">Arrendamento</option>
                <option value="ambos">Venda ou arrendamento</option>
              </select>
            </div>
            <div class="campo">
              <label for="a-municipio">Município</label>
              <input id="a-municipio" name="municipio" type="text" required>
            </div>
            <div class="campo">
              <label for="a-estado">Estado</label>
              <select id="a-estado" name="estado" required>
                <option value="">Selecione</option>
                <option value="MA">Maranhão</option>
                <option value="TO">Tocantins</option>
                <option value="PI">Piauí</option>
                <option value="BA">Bahia</option>
                <option value="outro">Outro estado</option>
              </select>
            </div>
            <div class="campo">
              <label for="a-area">Área aproximada (hectares)</label>
              <input id="a-area" name="area" type="number" min="1" step="1" inputmode="numeric">
            </div>
            <div class="campo">
              <label for="a-tipo">Tipo de propriedade</label>
              <select id="a-tipo" name="tipo">
                <option value="agricola">Agrícola</option>
                <option value="pecuaria">Pecuária</option>
                <option value="integracao">Integração lavoura-pecuária</option>
                <option value="florestal">Reflorestamento</option>
                <option value="investimento">Investimento e patrimônio</option>
              </select>
            </div>
            <div class="campo campo--largo">
              <label for="a-msg">Sobre a propriedade</label>
              <textarea id="a-msg" name="mensagem" rows="6"></textarea>
              <p class="campo__dica">Aptidão, água, infraestrutura, acesso e o que mais julgar relevante.</p>
            </div>
            <div class="campo campo--largo">
              <label for="a-arquivo">Material da propriedade (opcional)</label>
              <input id="a-arquivo" name="material" type="file" accept=".pdf,.jpg,.jpeg,.png,.doc,.docx" multiple>
              <p class="campo__dica">Fotos, mapas ou documentos que ajudem na avaliação. Máximo de 10 MB por arquivo.</p>
            </div>
            <label class="consentimento">
              <input type="checkbox" name="consentimento" required>
              <span>Autorizo o contato da Prime Fazendas e o tratamento dos meus dados conforme a
              <a href="privacidade.html">política de privacidade</a>.</span>
            </label>
            <div class="campo--largo">
              <button class="btn" type="submit">Enviar informações</button>
            </div>
            <p class="retorno"></p>
          </form>
        </div>

        <aside class="lado">
          <p class="olho">O que acontece depois</p>
          <ol style="display:grid;gap:1.1rem;padding-left:1.1rem;margin:0;color:var(--tinta-2)">
            <li>Analisamos as informações enviadas.</li>
            <li>Entramos em contato em até 2 dias úteis.</li>
            <li>Definimos com você a forma de apresentação — pública ou confidencial.</li>
            <li>Apresentamos a propriedade ao público adequado ao perfil da área.</li>
          </ol>
          <p style="margin-top:1.5rem;color:var(--tinta-2);font-size:.9rem">
            Nada é publicado sem sua autorização. O anúncio mostra a região, nunca o endereço — e
            há propriedades que apresentamos apenas em contato direto, a interessados qualificados.
          </p>
        </aside>
      </div>
    </div>
  </section>
""",
))

# =========================================================================== #
#  LEGAIS                                                                     #
# =========================================================================== #
feitos.append(pagina(
    arquivo="privacidade.html", lang="pt", atual="",
    titulo="Política de privacidade — Prime Fazendas",
    descricao="Como a Prime Fazendas trata os dados pessoais enviados pelos formulários do site, conforme a LGPD.",
    head_extra='<meta name="robots" content="noindex">\n',
    conteudo=capa(
        "Legal", "Política de privacidade",
        "Como tratamos os dados pessoais enviados pelo site, conforme a Lei Geral de Proteção de Dados (Lei 13.709/2018).",
        [("index.html", "Início"), ("", "Privacidade")],
    ) + """
  <section class="secao">
    <div class="env conteudo">
      <div class="aviso">
        <p><strong>Documento a validar.</strong> Este texto é uma base e deve ser revisado por assessoria
        jurídica antes da publicação definitiva, com a razão social, o CNPJ e o encarregado de dados da empresa.</p>
      </div>

      <h2>Quais dados coletamos</h2>
      <p>Coletamos apenas os dados que você informa nos formulários: nome, telefone, e-mail, dados da
      propriedade e a mensagem enviada. Arquivos anexados são recebidos apenas quando você os envia.</p>

      <h2>Para que usamos</h2>
      <ul>
        <li>Responder ao seu contato e conduzir a negociação pretendida.</li>
        <li>Apresentar propriedades ou interessados compatíveis com o que você informou.</li>
        <li>Cumprir obrigações legais aplicáveis à intermediação imobiliária.</li>
      </ul>

      <h2>Com quem compartilhamos</h2>
      <p>Compartilhamos dados apenas quando necessário à negociação que você solicitou e com o seu
      conhecimento. Não vendemos dados pessoais.</p>

      <h2>Por quanto tempo guardamos</h2>
      <p>Mantemos os dados pelo tempo necessário ao atendimento e ao cumprimento de obrigações legais.</p>

      <h2>Seus direitos</h2>
      <p>Você pode solicitar confirmação de tratamento, acesso, correção, portabilidade, anonimização ou
      exclusão dos seus dados, além de revogar o consentimento. Para isso, entre em
      <a href="contato.html">contato</a>.</p>

      <h2>Cookies</h2>
      <p>Este site não utiliza cookies de rastreamento ou publicidade. Caso ferramentas de medição sejam
      adotadas no futuro, esta política será atualizada e o consentimento será solicitado.</p>
    </div>
  </section>
""",
))

feitos.append(pagina(
    arquivo="termos.html", lang="pt", atual="",
    titulo="Termos de uso — Prime Fazendas",
    descricao="Condições de uso do site da Prime Fazendas e natureza das informações publicadas.",
    head_extra='<meta name="robots" content="noindex">\n',
    conteudo=capa(
        "Legal", "Termos de uso",
        "Condições de uso do site e natureza das informações aqui publicadas.",
        [("index.html", "Início"), ("", "Termos de uso")],
    ) + """
  <section class="secao">
    <div class="env conteudo">
      <div class="aviso">
        <p><strong>Documento a validar.</strong> Este texto é uma base e deve ser revisado por assessoria
        jurídica antes da publicação definitiva.</p>
      </div>

      <h2>Natureza das informações</h2>
      <p>As informações sobre propriedades são fornecidas pelos anunciantes e podem sofrer alteração sem
      aviso. Área, aptidão, infraestrutura, situação documental e condições comerciais devem ser
      confirmadas diretamente e verificadas pelos assessores das partes antes de qualquer decisão.</p>

      <h2>Ausência de garantia</h2>
      <p>Nada neste site constitui promessa de rentabilidade, garantia de aprovação documental ou parecer
      jurídico, contábil ou de investimento.</p>

      <h2>Confidencialidade</h2>
      <p>Parte da carteira não é publicada. Informações sobre essas propriedades são apresentadas apenas
      a interessados qualificados, mediante autorização do proprietário.</p>

      <h2>Propriedade intelectual</h2>
      <p>Marca, textos e imagens deste site pertencem à Prime Fazendas ou aos respectivos titulares e não
      podem ser reproduzidos sem autorização.</p>

      <h2>Contato</h2>
      <p>Dúvidas sobre estes termos: <a href="contato.html">fale conosco</a>.</p>
    </div>
  </section>
""",
))

feitos.append(pagina(
    arquivo="404.html", lang="pt", atual="",
    titulo="Página não encontrada — Prime Fazendas",
    descricao="A página procurada não existe ou foi movida.",
    head_extra='<meta name="robots" content="noindex">\n',
    conteudo="""
  <section class="secao" style="min-height:60vh;display:grid;place-content:center;text-align:center">
    <div class="env env-estreito">
      <p class="olho olho--centro">Erro 404</p>
      <h1 class="titulo" style="margin-bottom:1rem">Esta página não existe.</h1>
      <p class="subtitulo" style="margin:0 auto 2rem">
        O endereço pode ter mudado ou a propriedade pode ter saído da carteira.
      </p>
      <div class="acoes" style="justify-content:center">
        <a class="btn" href="index.html">Ir para o início</a>
        <a class="btn btn--linha" href="oportunidades.html">Ver oportunidades</a>
      </div>
    </div>
  </section>
""",
))

# =========================================================================== #
#  VERSÃO EM INGLÊS                                                           #
# =========================================================================== #
EN_HOME = """
  <section class="hero">
    <div class="hero__fundo">
      <img src="../assets/img/hero-matopiba.svg" alt="" width="2400" height="1240" fetchpriority="high" decoding="async">
    </div>

    <div class="env hero__grade">
      <div class="hero__texto">
        <p class="olho">Rural real estate &middot; MATOPIBA, Brazil</p>
        <h1 class="display hero__titulo">Productive land.<em>Meaningful opportunities.</em></h1>
        <p class="hero__apoio">
          Prime Fazendas connects landowners, producers and investors with selected opportunities
          to buy, sell and lease rural properties across Brazil's MATOPIBA region and the
          neighbouring agricultural frontiers.
        </p>
        <div class="acoes">
          <a class="btn btn--claro" href="opportunities.html">View opportunities</a>
          <a class="btn btn--fantasma" href="contact.html">Talk to Prime</a>
        </div>
      </div>

      <aside class="painel" aria-label="Current selection">
        <div class="painel__topo">
          <p class="painel__titulo">Current selection</p>
          <p class="painel__contagem" data-painel-contagem>&nbsp;</p>
        </div>
        <ul class="painel__lista" data-imoveis-painel></ul>
        <div class="painel__pe"><a class="elo" href="opportunities.html">View all opportunities</a></div>
      </aside>
    </div>
  </section>

  <section class="secao" aria-labelledby="t-what">
    <div class="env">
      <div class="cabeca-secao cabeca-secao--dupla">
        <p class="olho"><span class="numero-secao">01</span> The region</p>
        <h2 class="titulo" id="t-what">What MATOPIBA is</h2>
        <p class="subtitulo">
          MATOPIBA is the acronym for a region formed by parts of four Brazilian states — Maranhão,
          Tocantins, Piauí and Bahia. It comprises some of the country's most recently developed
          agricultural frontiers, with large contiguous areas, mechanised grain production, livestock
          and forestry operations.
        </p>
      </div>

      <div class="regiao">
        <div class="regiao__mapa" data-revela>
          <img src="../assets/img/mapa-matopiba.svg" alt="Schematic map of Brazil highlighting the MATOPIBA region across Maranhão, Tocantins, Piauí and Bahia." width="600" height="640" loading="lazy" decoding="async">
          <p class="regiao__nota">Schematic representation, not for cartographic use.</p>
        </div>
        <div>
          <div class="pilares" style="margin-top:0">
            <div class="pilar"><p class="pilar__nome">Scale</p><p class="pilar__texto">Large contiguous areas, suited to mechanised operations and long-horizon projects.</p></div>
            <div class="pilar"><p class="pilar__nome">Activities</p><p class="pilar__texto">Grain production, livestock, integrated crop-livestock systems and forestry assets.</p></div>
            <div class="pilar"><p class="pilar__nome">Logistics</p><p class="pilar__texto">Distance to terminals and road conditions materially affect operating cost and must be assessed per property.</p></div>
            <div class="pilar"><p class="pilar__nome">Local knowledge</p><p class="pilar__texto">Prime Fazendas operates in the region and presents what is confirmed, separately from what still requires verification.</p></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="secao secao--escura">
    <div class="env">
      <div class="numeros">
        <div class="numero" data-revela>
          <span class="numero__valor">3+</span>
          <span class="numero__rotulo">years of Prime Fazendas</span>
        </div>
        <div class="numero" data-revela>
          <span class="numero__valor">18</span>
          <span class="numero__rotulo">years of the founder's experience in real estate</span>
        </div>
        <div data-revela>
          <h2 class="titulo-menor" style="margin-bottom:.8rem">Experience built on relationships</h2>
          <p class="subtitulo">
            On market knowledge and on conducting each negotiation responsibly — from the first
            conversation to signing.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="secao secao--marfim">
    <div class="env">
      <div class="cabeca-secao">
        <p class="olho"><span class="numero-secao">02</span> How we work</p>
        <h2 class="titulo">Buy, sell and lease</h2>
      </div>
      <div class="frentes">
        <article class="frente"><p class="frente__indice">01</p><h3>Buy</h3>
          <p>Each listing states suitability, scale, logistics and water — enough to judge whether
          a visit is worth your time.</p>
          <p><a class="elo" href="opportunities.html">View opportunities</a></p></article>
        <article class="frente"><p class="frente__indice">02</p><h3>Sell</h3>
          <p>Your property reaches the right buyer without being passed from hand to hand. You
          decide what is published, and when.</p>
          <p><a class="elo" href="contact.html">Talk to us</a></p></article>
        <article class="frente"><p class="frente__indice">03</p><h3>Lease</h3>
          <p>Available land matched with producers and companies expanding operations, on terms
          agreed between the parties.</p>
          <p><a class="elo" href="leases.html">View leases</a></p></article>
      </div>
    </div>
  </section>

  <section class="secao secao--marfim">
    <div class="env env-estreito">
      <p class="olho">Why we publish the region, not the address</p>
      <h2 class="titulo" style="margin-bottom:1.2rem">Discretion is the method, not a formality</h2>
      <div class="conteudo">
        <p>
          In the Brazilian land market, an address circulating too early exposes the seller to
          unwanted intermediation, multiplies interlocutors and takes control of the negotiation
          away from the person who owns the land.
        </p>
        <p>
          So the catalogue states the region, the suitability, the scale, the logistics and the
          water — enough for a serious buyer to judge whether a property fits. Address, title
          records and site visits come next, during the conversation, with the owner aware of every
          step. A buyer looking for land loses nothing. A broker looking to pass the contact along
          does.
        </p>
      </div>
    </div>
  </section>

  <section class="secao">
    <div class="env env-estreito">
      <p class="olho"><span class="numero-secao">04</span> For international buyers</p>
      <h2 class="titulo" style="margin-bottom:1.2rem">Acquiring rural land in Brazil</h2>
      <div class="conteudo">
        <p>
          Brazilian law places specific restrictions on the acquisition and leasing of rural land by
          foreign individuals and by Brazilian companies under foreign control. Rules cover area
          limits, registration requirements and, in certain cases, prior authorisation.
        </p>
        <div class="aviso">
          <p><strong>Informational only.</strong> The above is general information, not legal advice.
          Requirements change and depend on the buyer's structure and on the specific property. Engage
          specialised Brazilian legal counsel before committing to any transaction. Prime Fazendas does
          not provide legal opinions and does not guarantee approvals.</p>
        </div>
        <h3>How Prime Fazendas supports the process</h3>
        <ul>
          <li>Presenting properties that match the stated objective, in English.</li>
          <li>Gathering the information made available by the owner, stating what is confirmed.</li>
          <li>Coordinating visits and conversations between the parties.</li>
          <li>Working alongside the advisers appointed by each side, without replacing them.</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="secao chamada">
    <div class="chamada__fundo">
      <img src="../assets/img/hero-matopiba.svg" alt="" width="2400" height="1240" loading="lazy" decoding="async">
    </div>
    <div class="env env-estreito">
      <p class="olho olho--centro">Contact</p>
      <h2 class="titulo" style="margin-bottom:1rem">Every good deal starts with the right conversation.</h2>
      <p class="subtitulo" style="margin:0 auto 2rem;color:rgba(244,241,233,.8)">
        Whether buying, selling or leasing, talk to a team that knows the market and the region.
      </p>
      <div class="acoes"><a class="btn btn--claro" href="contact.html">Talk to a specialist</a></div>
    </div>
  </section>
"""

feitos.append(pagina(
    arquivo="en/index.html", lang="en", atual="index.html",
    titulo="Prime Fazendas — Rural properties for sale and lease in Brazil's MATOPIBA",
    og_titulo="Prime Fazendas — Productive land. Meaningful opportunities.",
    descricao="Rural real estate firm operating across Brazil's MATOPIBA region. We connect landowners, producers and international investors with selected opportunities to buy, sell and lease.",
    canonico=SITE + "/en/", alternativo=SITE + "/",
    conteudo=EN_HOME,
))

feitos.append(pagina(
    arquivo="en/opportunities.html", lang="en", atual="opportunities.html",
    titulo="Opportunities — Farms for sale in MATOPIBA, Brazil | Prime Fazendas",
    descricao="Rural properties for sale across Maranhão, Tocantins, Piauí and Bahia. Filter by state, property type and area.",
    alternativo=SITE + "/oportunidades.html",
    conteudo=capa(
        "Portfolio", "Opportunities",
        "Each property is named after a stone — they are singular assets. Region, suitability, scale, logistics and water as stated by the owner.",
        [("index.html", "Home"), ("", "Opportunities")],
    ) + """
  <section class="secao">
    <div class="env">
      <div class="aviso">
        <p><strong>We publish the region, not the address.</strong> That is deliberate: it protects
        the owner from unwanted intermediation. Address, title records and visits are handled during
        the conversation. <a href="contact.html">Contact us</a> — part of the portfolio is never published.</p>
      </div>

      <form class="filtros" data-filtros>
        <div class="campo">
          <label for="f-finalidade">Purpose</label>
          <select id="f-finalidade" name="finalidade">
            <option value="">Buy or lease</option>
            <option value="venda">Buy</option>
            <option value="arrendamento">Lease</option>
          </select>
        </div>
        <div class="campo">
          <label for="f-estado">Location</label>
          <select id="f-estado" name="estado">
            <option value="">All locations</option>
          </select>
        </div>
        <div class="campo">
          <label for="f-tipo">Property type</label>
          <select id="f-tipo" name="tipo">
            <option value="">All types</option>
            <option value="agricola">Cropland</option>
            <option value="pecuaria">Livestock</option>
            <option value="integracao">Crop-livestock</option>
            <option value="florestal">Forestry</option>
            <option value="investimento">Investment</option>
          </select>
        </div>
        <div class="campo">
          <label for="f-area">Area</label>
          <select id="f-area" name="area">
            <option value="">Any area</option>
            <option value="ate500">Up to 500 ha</option>
            <option value="500a1500">500 to 1,500 ha</option>
            <option value="acima1500">Over 1,500 ha</option>
          </select>
        </div>
        <div class="campo">
          <label for="f-ordem">Sort by</label>
          <select id="f-ordem" name="ordem">
            <option value="">Relevance</option>
            <option value="area-desc">Largest area</option>
            <option value="area-asc">Smallest area</option>
          </select>
        </div>
        <div class="filtros__acoes">
          <button class="btn" type="submit">Apply filters</button>
          <button class="btn btn--linha" type="button" data-limpar>Clear</button>
        </div>
      </form>

      <div class="resultado-info"><span data-resultado-info></span></div>
      <div class="grade grade--3" data-imoveis-catalogo></div>
    </div>
  </section>
""",
))

feitos.append(pagina(
    arquivo="en/leases.html", lang="en", atual="leases.html",
    titulo="Leases — Rural land to lease in MATOPIBA, Brazil | Prime Fazendas",
    descricao="Areas available for agricultural and livestock leasing across Brazil's MATOPIBA region. Term, crop season and conditions agreed between the parties.",
    alternativo=SITE + "/arrendamentos.html",
    conteudo=capa(
        "Leases", "Areas available to lease",
        "We connect available land with producers and companies seeking to expand operations. Term, crop season and conditions are agreed between the parties.",
        [("index.html", "Home"), ("", "Leases")],
    ) + """
  <section class="secao">
    <div class="env">
      <div class="aviso">
        <p>Lease availability changes with the crop season. <a href="contact.html">Contact us</a>
        for what is open right now.</p>
      </div>
      <div class="resultado-info"><span data-resultado-info></span></div>
      <div class="grade grade--3" data-imoveis-catalogo data-finalidade="arrendamento"></div>
    </div>
  </section>
""",
))

feitos.append(pagina(
    arquivo="en/about.html", lang="en", atual="about.html",
    titulo="About — Prime Fazendas, rural real estate in MATOPIBA",
    descricao="Over three years of operation and a founder with 18 years of experience in real estate, focused on Brazil's MATOPIBA region.",
    alternativo=SITE + "/quem-somos.html",
    conteudo=capa(
        "About", "Real estate experience. Presence in the field.",
        "Prime Fazendas connects landowners, producers and investors with opportunities to buy, sell and lease rural properties.",
        [("index.html", "Home"), ("", "About")],
    ) + """
  <section class="secao">
    <div class="env">
      <div class="retrato">
        <figure class="retrato__figura" style="margin:0" data-revela>
          <img src="../assets/img/fundador.webp" alt="André Amorim, founder of Prime Fazendas." width="1100" height="1159" loading="lazy" decoding="async">
          <figcaption class="retrato__legenda">André Amorim &middot; founder of Prime Fazendas</figcaption>
        </figure>
        <div class="conteudo">
          <p>
            Prime Fazendas has been operating for more than three years, connecting opportunities to
            buy, sell and lease rural properties. The founder brings 18 years of experience in real
            estate, conducting relationships and negotiations with proximity, discretion and
            responsibility.
          </p>
          <p>
            With a focus on the MATOPIBA region, we bring landowners, producers, companies and both
            Brazilian and international investors closer to properties aligned with their objectives.
          </p>

          <h2>How we work</h2>
          <ul>
            <li>Understanding the objective before presenting any area.</li>
            <li>Collecting the information made available by the owner.</li>
            <li>Presenting clearly what is confirmed and what still requires verification.</li>
            <li>Conducting the conversation between the parties, confidentially when requested.</li>
            <li>Working alongside each side's legal counsel, without replacing them.</li>
          </ul>

          <h2>What we do not do</h2>
          <ul>
            <li>We do not present unverified information as confirmed.</li>
            <li>We do not publish the exact location of any property in the portfolio.</li>
            <li>We do not promise returns, document approval or legal certainty.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
""",
))

feitos.append(pagina(
    arquivo="en/contact.html", lang="en", atual="contact.html",
    titulo="Contact — Prime Fazendas",
    descricao="Talk to the Prime Fazendas team about buying, selling or leasing rural properties in Brazil's MATOPIBA region.",
    alternativo=SITE + "/contato.html",
    conteudo=capa(
        "Contact", "Every good deal starts with the right conversation.",
        "Tell us what you are looking for. We reply within two business days, in English or Portuguese.",
        [("index.html", "Home"), ("", "Contact")],
    ) + """
  <section class="secao">
    <div class="env">
      <div class="detalhe">
        <div>
          <form class="formulario formulario--duplo" data-formulario action="#" method="post" novalidate>
            <div class="campo"><label for="e-nome">Name</label>
              <input id="e-nome" name="name" type="text" autocomplete="name" required></div>
            <div class="campo"><label for="e-tel">Phone or WhatsApp</label>
              <input id="e-tel" name="phone" type="tel" autocomplete="tel" required></div>
            <div class="campo"><label for="e-email">Email</label>
              <input id="e-email" name="email" type="email" autocomplete="email" required></div>
            <div class="campo"><label for="e-assunto">Subject</label>
              <select id="e-assunto" name="subject">
                <option value="buy">I want to buy</option>
                <option value="sell">I want to sell</option>
                <option value="lease">I want to lease</option>
                <option value="invest">Investment</option>
                <option value="other">Other</option>
              </select></div>
            <div class="campo campo--largo"><label for="e-msg">Message</label>
              <textarea id="e-msg" name="message" rows="6" required></textarea></div>
            <label class="consentimento">
              <input type="checkbox" name="consent" required>
              <span>I authorise Prime Fazendas to contact me and to process my data as described in the
              <a href="../privacidade.html">privacy policy</a>.</span>
            </label>
            <div class="campo--largo"><button class="btn" type="submit">Send message</button></div>
            <p class="retorno"></p>
          </form>
        </div>

        <aside class="lado">
          <p class="olho">Channels</p>
          <h2 class="titulo-menor" style="margin-bottom:1.2rem">Reach us directly</h2>
          <ul class="rodape__lista" style="color:var(--tinta)">
            <li data-bloco><strong>Email:</strong> <a data-campo="email" data-esconder-vazio href="#">&nbsp;</a></li>
            <li data-bloco><strong>Phone:</strong> <a data-campo="telefone" data-esconder-vazio href="#">&nbsp;</a></li>
          </ul>
          <p style="margin-top:1.5rem;color:var(--tinta-2);font-size:.9rem">
            Information about acquiring rural land in Brazil by foreign buyers is provided for
            orientation only and does not constitute legal advice.
          </p>
        </aside>
      </div>
    </div>
  </section>
""",
))

print("Páginas geradas:")
for f in feitos:
    print("  •", f)
