/* =========================================================================
   Prime Fazendas — comportamento do site
   Sem dependências externas. Tudo degrada bem quando o JavaScript falha.
   ========================================================================= */
(function () {
  "use strict";

  var base = document.body.getAttribute("data-base") || "";
  var idioma = document.documentElement.lang === "en" ? "en" : "pt";

  var T = {
    pt: {
      venda: "Venda",
      arrendamento: "Arrendamento",
      hectares: "ha",
      sobConsulta: "Sob consulta",
      verPropriedade: "Ver propriedade",
      exemplo: "Exemplo",
      confidencial: "Confidencial",
      areaNaoInformada: "Área sob consulta",
      nenhum: "Nenhuma propriedade corresponde a esses filtros.",
      nenhumApoio: "Ajuste os filtros ou fale com a equipe: podemos ter opções ainda não publicadas.",
      contagem: function (n) {
        return n === 1 ? "1 propriedade" : n + " propriedades";
      },
      agendaVazia: "A agenda está sendo montada.",
      agendaApoio:
        "Publicamos apenas eventos confirmados, com data e link oficial verificados.",
      radarVazio: "O Radar Agro está sendo preparado.",
      enviado: "Recebemos sua mensagem. Retornamos em até 2 dias úteis.",
      erroEnvio: "Não foi possível enviar agora. Tente novamente ou fale conosco pelo WhatsApp."
    },
    en: {
      venda: "For sale",
      arrendamento: "For lease",
      hectares: "ha",
      sobConsulta: "Price on request",
      verPropriedade: "View property",
      exemplo: "Sample",
      confidencial: "Confidential",
      areaNaoInformada: "Area on request",
      nenhum: "No property matches these filters.",
      nenhumApoio: "Adjust the filters or contact us — we may hold unpublished options.",
      contagem: function (n) {
        return n === 1 ? "1 property" : n + " properties";
      },
      agendaVazia: "The calendar is being prepared.",
      agendaApoio: "We only publish confirmed events with verified dates and official links.",
      radarVazio: "Radar Agro is being prepared.",
      enviado: "We have received your message. We reply within 2 business days.",
      erroEnvio: "We could not send it right now. Please try again or reach us on WhatsApp."
    }
  }[idioma];

  var ESTADOS = {
    MA: "Maranhão", TO: "Tocantins", PI: "Piauí", BA: "Bahia",
    GO: "Goiás", PA: "Pará", MT: "Mato Grosso", MS: "Mato Grosso do Sul",
    MG: "Minas Gerais", SP: "São Paulo", RO: "Rondônia"
  };
  var TIPOS = {
    agricola: idioma === "en" ? "Cropland" : "Agrícola",
    pecuaria: idioma === "en" ? "Livestock" : "Pecuária",
    integracao: idioma === "en" ? "Crop-livestock" : "Integração lavoura-pecuária",
    florestal: idioma === "en" ? "Forestry" : "Reflorestamento",
    investimento: idioma === "en" ? "Investment" : "Investimento e patrimônio"
  };

  /* ------------------------------------------------------------ utilidades */
  function $(sel, ctx) {
    return (ctx || document).querySelector(sel);
  }

  function $$(sel, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(sel));
  }

  function esc(valor) {
    return String(valor == null ? "" : valor).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function numero(n) {
    return new Intl.NumberFormat(idioma === "en" ? "en-US" : "pt-BR").format(n);
  }

  function carregar(arquivo) {
    return fetch(base + "data/" + arquivo, { cache: "no-cache" }).then(function (r) {
      if (!r.ok) throw new Error(arquivo);
      return r.json();
    });
  }

  /* --------------------------------------------------------------- menu */
  var botaoMenu = $(".menu-btn");
  var nav = $("#nav-principal");

  if (botaoMenu && nav) {
    botaoMenu.addEventListener("click", function () {
      var aberto = botaoMenu.getAttribute("aria-expanded") === "true";
      botaoMenu.setAttribute("aria-expanded", String(!aberto));
      nav.setAttribute("data-aberto", String(!aberto));
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && botaoMenu.getAttribute("aria-expanded") === "true") {
        botaoMenu.setAttribute("aria-expanded", "false");
        nav.setAttribute("data-aberto", "false");
        botaoMenu.focus();
      }
    });

    $$("a", nav).forEach(function (a) {
      a.addEventListener("click", function () {
        botaoMenu.setAttribute("aria-expanded", "false");
        nav.setAttribute("data-aberto", "false");
      });
    });
  }

  /* --------------------------------------------------------- ano corrente */
  $$("[data-ano]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ----------------------------------------------------- revelar ao rolar */
  var reduzido = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var alvos = $$("[data-revela]");

  if (alvos.length) {
    if (reduzido || !("IntersectionObserver" in window)) {
      alvos.forEach(function (el) {
        el.setAttribute("data-revela", "visivel");
      });
    } else {
      var obs = new IntersectionObserver(
        function (entradas) {
          entradas.forEach(function (entrada) {
            if (entrada.isIntersecting) {
              entrada.target.setAttribute("data-revela", "visivel");
              obs.unobserve(entrada.target);
            }
          });
        },
        { rootMargin: "0px 0px -8% 0px", threshold: 0.06 }
      );
      alvos.forEach(function (el) {
        obs.observe(el);
      });
    }
  }

  /* -------------------------------------------------- contato configurável */
  carregar("site.json")
    .then(function (cfg) {
      var zap = cfg.whatsapp ? String(cfg.whatsapp).replace(/\D/g, "") : "";

      $$("[data-zap]").forEach(function (el) {
        if (!zap) {
          el.remove();
          return;
        }
        var msg = el.getAttribute("data-zap") || "";
        el.setAttribute(
          "href",
          "https://wa.me/" + zap + (msg ? "?text=" + encodeURIComponent(msg) : "")
        );
      });

      $$("[data-campo]").forEach(function (el) {
        var chave = el.getAttribute("data-campo");
        var valor = chave.split(".").reduce(function (o, k) {
          return o && o[k];
        }, cfg);
        if (valor) {
          if (el.tagName === "A") {
            el.setAttribute(
              "href",
              /@/.test(valor) ? "mailto:" + valor : valor.indexOf("http") === 0 ? valor : "#"
            );
          }
          el.textContent = valor;
        } else if (el.hasAttribute("data-esconder-vazio")) {
          var pai = el.closest("[data-bloco]") || el;
          pai.remove();
        }
      });
    })
    .catch(function () {
      $$("[data-zap]").forEach(function (el) {
        el.remove();
      });
    });

  /* ------------------------------------------------------ cartão de imóvel */
  function areaTexto(imovel) {
    if (imovel.area_ha) return numero(imovel.area_ha) + " " + T.hectares;
    if (imovel.area_texto) return imovel.area_texto;
    return T.areaNaoInformada;
  }

  /* Muitos documentos não declaram município nem estado — trazem só a região.
     Mostramos o dado mais preciso disponível, sem deduzir o que falta. */
  function localTexto(imovel) {
    var uf = ESTADOS[imovel.estado] || imovel.estado;
    if (imovel.municipio && uf) return imovel.municipio + " \u00b7 " + uf;
    if (imovel.municipio) return imovel.municipio;
    if (uf) return uf;
    return capitalizar(imovel.regiao || "");
  }

  /* Os documentos escrevem a região em caixa alta ("REGIÃO NORTE").
     Na página isso vira grito — normalizamos para caixa de título. */
  function capitalizar(txt) {
    if (!txt || txt !== txt.toUpperCase()) return txt;
    var minusculas = { de: 1, do: 1, da: 1, dos: 1, das: 1, e: 1 };
    return txt.toLowerCase().replace(/[a-zà-ú]+/g, function (palavra, i) {
      if (i > 0 && minusculas[palavra]) return palavra;
      return palavra.charAt(0).toUpperCase() + palavra.slice(1);
    });
  }

  function precoTexto(imovel) {
    if (typeof imovel.preco === "number") {
      return new Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL",
        maximumFractionDigits: 0
      }).format(imovel.preco);
    }
    return imovel.preco_texto || T.sobConsulta;
  }

  function cartao(imovel) {
    var url = base + "propriedade.html?id=" + encodeURIComponent(imovel.id);
    var finalidade = imovel.finalidade === "arrendamento" ? T.arrendamento : T.venda;
    var selos = '<span class="selo">' + esc(finalidade) + "</span>";
    if (imovel.exemplo) {
      selos += '<span class="selo selo--exemplo">' + T.exemplo + "</span>";
    } else if (imovel.confidencial) {
      selos += '<span class="selo selo--exemplo">' + T.confidencial + "</span>";
    }

    return (
      '<article class="imovel" data-revela>' +
      '<div class="imovel__figura">' +
      selos +
      '<img src="' +
      esc(base + imovel.imagem) +
      '" alt="" loading="lazy" decoding="async" width="1600" height="1067">' +
      "</div>" +
      '<div class="imovel__corpo">' +
      '<p class="imovel__local">' +
      esc(localTexto(imovel)) +
      (imovel.codigo ? ' <span class="imovel__codigo">C\u00f3d. ' + esc(imovel.codigo) + "</span>" : "") +
      "</p>" +
      '<h3 class="imovel__nome"><a href="' +
      esc(url) +
      '">' +
      esc(imovel.nome) +
      "</a></h3>" +
      '<ul class="ficha">' +
      "<li>" +
      esc(areaTexto(imovel)) +
      "</li>" +
      "<li>" +
      esc(imovel.aptidao || TIPOS[imovel.tipo] || "") +
      "</li>" +
      "</ul>" +
      '<p class="imovel__preco">' +
      esc(precoTexto(imovel)) +
      "<span>" +
      esc(finalidade) +
      "</span></p>" +
      "</div>" +
      "</article>"
    );
  }

  function miniatura(imovel) {
    var url = base + "propriedade.html?id=" + encodeURIComponent(imovel.id);
    return (
      "<li>" +
      '<a class="mini" href="' +
      esc(url) +
      '">' +
      '<img src="' +
      esc(base + imovel.imagem) +
      '" alt="" loading="lazy" decoding="async" width="68" height="52">' +
      "<span>" +
      '<span class="mini__nome">' +
      esc(imovel.nome) +
      "</span>" +
      '<span class="mini__meta">' +
      esc(localTexto(imovel)) +
      " &middot; " +
      esc(areaTexto(imovel)) +
      " &middot; " +
      esc(imovel.finalidade === "arrendamento" ? T.arrendamento : T.venda) +
      "</span>" +
      "</span>" +
      "</a>" +
      "</li>"
    );
  }

  /* ------------------------------------------------------- render: imóveis */
  var alvoDestaques = $("[data-imoveis-destaque]");
  var alvoPainel = $("[data-imoveis-painel]");
  var alvoCatalogo = $("[data-imoveis-catalogo]");

  if (alvoDestaques || alvoPainel || alvoCatalogo) {
    carregar("properties.json")
      .then(function (dados) {
        var todos = dados.imoveis || [];

        $$("[data-preparacao]").forEach(function (el) {
          if (!dados.catalogo_em_preparacao) el.remove();
        });

        if (alvoPainel) {
          var painel = todos.slice(0, 3);
          alvoPainel.innerHTML = painel.map(miniatura).join("");
          var contagem = $("[data-painel-contagem]");
          if (contagem) contagem.textContent = T.contagem(todos.length);
        }

        if (alvoDestaques) {
          var filtroInicial = alvoDestaques.getAttribute("data-imoveis-destaque");
          var lista = todos;
          if (filtroInicial === "arrendamento" || filtroInicial === "venda") {
            lista = todos.filter(function (i) {
              return i.finalidade === filtroInicial;
            });
          }
          alvoDestaques.innerHTML = lista.slice(0, 6).map(cartao).join("");
          reobservar();
        }

        if (alvoCatalogo) montarCatalogo(todos, dados);
      })
      .catch(function () {
        [alvoDestaques, alvoCatalogo].forEach(function (el) {
          if (el) {
            el.innerHTML =
              '<div class="vazio"><h3>' + T.nenhum + "</h3><p>" + T.nenhumApoio + "</p></div>";
          }
        });
      });
  }

  function reobservar() {
    var novos = $$("[data-revela]:not([data-revela='visivel'])");
    if (reduzido || !("IntersectionObserver" in window)) {
      novos.forEach(function (el) {
        el.setAttribute("data-revela", "visivel");
      });
      return;
    }
    var o = new IntersectionObserver(
      function (ent) {
        ent.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.setAttribute("data-revela", "visivel");
            o.unobserve(e.target);
          }
        });
      },
      { rootMargin: "0px 0px -6% 0px", threshold: 0.05 }
    );
    novos.forEach(function (el) {
      o.observe(el);
    });
  }

  /* ------------------------------------------------------------- catálogo */
  function montarCatalogo(todos, dados) {
    var form = $("[data-filtros]");
    var info = $("[data-resultado-info]");
    var params = new URLSearchParams(location.search);
    var travaFinalidade = alvoCatalogo.getAttribute("data-finalidade") || "";

    /* Localização: o catálogo trabalha por região, e não por município.
       O seletor lista o estado quando o documento o declara e a região
       quando não — sem inventar precisão que a Prime não divulga. */
    if (form && form.elements.estado) {
      var sel = form.elements.estado;
      var ufs = {}, regioes = {};
      todos.forEach(function (i) {
        if (i.estado) ufs[i.estado] = (ufs[i.estado] || 0) + 1;
        else if (i.regiao) {
          var r = capitalizar(i.regiao);
          regioes[r] = (regioes[r] || 0) + 1;
        }
      });

      var primeira = sel.options[0];
      sel.innerHTML = "";
      sel.appendChild(primeira);

      function grupo(rotulo, itens, prefixo) {
        var chaves = Object.keys(itens).sort();
        if (!chaves.length) return;
        var g = document.createElement("optgroup");
        g.label = rotulo;
        chaves.forEach(function (k) {
          var o = document.createElement("option");
          o.value = prefixo + k;
          o.textContent = (prefixo === "uf:" ? ESTADOS[k] || k : k) + " (" + itens[k] + ")";
          g.appendChild(o);
        });
        sel.appendChild(g);
      }

      grupo(idioma === "en" ? "State" : "Estado", ufs, "uf:");
      grupo(idioma === "en" ? "Region" : "Região", regioes, "reg:");
    }

    if (form) {
      ["finalidade", "estado", "tipo", "area", "ordem"].forEach(function (campo) {
        var el = form.elements[campo];
        if (el && params.get(campo)) el.value = params.get(campo);
      });
    }

    function aplicar() {
      var f = form ? new FormData(form) : new FormData();
      var finalidade = travaFinalidade || f.get("finalidade") || "";
      var estado = f.get("estado") || "";
      var tipo = f.get("tipo") || "";
      var area = f.get("area") || "";
      var ordem = f.get("ordem") || "";

      var lista = todos.filter(function (i) {
        if (finalidade && i.finalidade !== finalidade) return false;
        if (estado) {
          if (estado.indexOf("uf:") === 0) {
            if (i.estado !== estado.slice(3)) return false;
          } else if (estado.indexOf("reg:") === 0) {
            if (capitalizar(i.regiao || "") !== estado.slice(4)) return false;
          } else if (i.estado !== estado) {
            return false;
          }
        }
        if (tipo && i.tipo !== tipo) return false;
        if (area) {
          var ha = i.area_ha || 0;
          if (area === "ate500" && !(ha > 0 && ha <= 500)) return false;
          if (area === "500a1500" && !(ha > 500 && ha <= 1500)) return false;
          if (area === "acima1500" && !(ha > 1500)) return false;
        }
        return true;
      });

      if (ordem === "area-desc") {
        lista.sort(function (a, b) {
          return (b.area_ha || 0) - (a.area_ha || 0);
        });
      } else if (ordem === "area-asc") {
        lista.sort(function (a, b) {
          return (a.area_ha || 0) - (b.area_ha || 0);
        });
      }

      alvoCatalogo.innerHTML = lista.length
        ? lista.map(cartao).join("")
        : '<div class="vazio"><h3>' + T.nenhum + "</h3><p>" + T.nenhumApoio + "</p></div>";

      if (info) info.textContent = T.contagem(lista.length);
      reobservar();
    }

    if (form) {
      form.addEventListener("change", aplicar);
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        aplicar();
      });
      var limpar = $("[data-limpar]", form);
      if (limpar) {
        limpar.addEventListener("click", function () {
          form.reset();
          aplicar();
        });
      }
    }

    aplicar();
  }

  /* -------------------------------------------------- página da propriedade */
  var alvoDetalhe = $("[data-propriedade]");

  if (alvoDetalhe) {
    var id = new URLSearchParams(location.search).get("id");
    carregar("properties.json").then(function (dados) {
      var imovel = (dados.imoveis || []).filter(function (i) {
        return i.id === id;
      })[0];

      if (!imovel) {
        alvoDetalhe.innerHTML =
          '<div class="vazio"><h3>' +
          (idioma === "en" ? "Property not found" : "Propriedade não encontrada") +
          "</h3><p>" +
          (idioma === "en"
            ? "It may have been withdrawn. See the current opportunities."
            : "Ela pode ter saído da carteira. Veja as oportunidades disponíveis.") +
          '</p><p><a class="btn" href="' +
          base +
          'oportunidades.html">' +
          (idioma === "en" ? "See opportunities" : "Ver oportunidades") +
          "</a></p></div>";
        return;
      }

      document.title = imovel.nome + " — Prime Fazendas";
      $$("[data-slot]").forEach(function (el) {
        var chave = el.getAttribute("data-slot");
        var valor;
        if (chave === "area") valor = areaTexto(imovel);
        else if (chave === "preco") valor = precoTexto(imovel);
        else if (chave === "finalidade")
          valor = imovel.finalidade === "arrendamento" ? T.arrendamento : T.venda;
        else if (chave === "estado") valor = ESTADOS[imovel.estado] || imovel.estado;
        else if (chave === "local") valor = localTexto(imovel);
        else if (chave === "area_aberta") valor = imovel.area_aberta;
        else if (chave === "tipo") valor = TIPOS[imovel.tipo] || imovel.tipo;
        else valor = imovel[chave];

        if (valor) el.textContent = valor;
        else if (el.hasAttribute("data-esconder-vazio")) {
          (el.closest("[data-bloco]") || el).remove();
        }
      });

      montarGaleria(imovel);

      var descricao = $("[data-slot-descricao]");
      if (descricao) {
        var blocos = (imovel.descricao_blocos && imovel.descricao_blocos.length)
          ? imovel.descricao_blocos
          : (imovel.resumo ? [imovel.resumo] : []);
        if (blocos.length) {
          descricao.innerHTML = blocos.map(function (b) {
            return "<p>" + esc(b) + "</p>";
          }).join("");
        } else {
          (descricao.closest("[data-bloco]") || descricao).remove();
        }
      }

      var aviso = $("[data-slot-exemplo]");
      if (aviso && !imovel.exemplo) aviso.remove();

      var assunto = $("[data-slot-assunto]");
      if (assunto) assunto.value = imovel.id + " — " + imovel.nome;

      var relacionadas = $("[data-relacionadas]");
      if (relacionadas) {
        var outras = (dados.imoveis || [])
          .filter(function (i) {
            return i.id !== imovel.id;
          })
          .slice(0, 3);
        relacionadas.innerHTML = outras.map(cartao).join("");
        reobservar();
      }
    });
  }

  /* --------------------------------------------------------------- galeria */
  function montarGaleria(imovel) {
    var caixa = $("[data-galeria]");
    if (!caixa) return;

    var fotos = (imovel.fotos && imovel.fotos.length) ? imovel.fotos
              : (imovel.imagem ? [imovel.imagem] : []);
    if (!fotos.length) {
      caixa.remove();
      return;
    }

    var rotulo = idioma === "en" ? "Photo" : "Foto";
    caixa.innerHTML =
      '<figure class="galeria__principal">' +
      '<img id="galeria-foto" src="' + esc(base + fotos[0]) + '" alt="' +
      esc(imovel.nome + " \u2014 " + rotulo + " 1") + '" width="1600" height="1067" ' +
      'fetchpriority="high" decoding="async">' +
      "</figure>" +
      (fotos.length > 1
        ? '<ul class="galeria__tiras" role="list">' +
          fotos.map(function (f, i) {
            return "<li>" +
              '<button type="button" class="galeria__tira" data-foto="' + esc(base + f) + '"' +
              (i === 0 ? ' aria-current="true"' : "") + ">" +
              '<img src="' + esc(base + f) + '" alt="" width="200" height="134" loading="lazy" decoding="async">' +
              '<span class="vis-oculto">' + rotulo + " " + (i + 1) + "</span>" +
              "</button></li>";
          }).join("") +
          "</ul>"
        : "");

    var principal = $("#galeria-foto", caixa);
    var tiras = $$(".galeria__tira", caixa);

    function mostrar(i) {
      if (i < 0 || i >= tiras.length) return;
      principal.src = tiras[i].getAttribute("data-foto");
      principal.alt = imovel.nome + " \u2014 " + rotulo + " " + (i + 1);
      tiras.forEach(function (t, j) {
        if (j === i) t.setAttribute("aria-current", "true");
        else t.removeAttribute("aria-current");
      });
    }

    tiras.forEach(function (tira, i) {
      tira.addEventListener("click", function () {
        mostrar(i);
      });
      tira.addEventListener("keydown", function (e) {
        if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
          e.preventDefault();
          var alvo = i + (e.key === "ArrowRight" ? 1 : -1);
          if (alvo >= 0 && alvo < tiras.length) {
            tiras[alvo].focus();
            mostrar(alvo);
          }
        }
      });
    });
  }

  /* ------------------------------------------------------------ Radar Agro */
  var alvoRadar = $("[data-radar]");

  if (alvoRadar) {
    var limiteRadar = parseInt(alvoRadar.getAttribute("data-radar"), 10) || 3;
    var artigosPorId = {};

    var abrirArtigoModal = function (id) {
      var a = artigosPorId[id];
      var modal = document.getElementById("modal-artigo");
      if (!a || !modal) return;
      modal.querySelector("[data-modal-img]").src = base + a.imagem;
      modal.querySelector("[data-modal-img]").alt = a.titulo || "";
      modal.querySelector("[data-modal-categoria]").textContent = a.categoria || "";
      modal.querySelector("[data-modal-titulo]").textContent = a.titulo || "";
      var metaPartes = [];
      if (a.autor) metaPartes.push(a.autor);
      if (a.data) metaPartes.push(a.data);
      if (a.fonte) metaPartes.push("Fonte: " + a.fonte);
      modal.querySelector("[data-modal-meta]").textContent = metaPartes.join(" · ");
      modal.querySelector("[data-modal-resumo]").textContent = a.resumo || "";
      var caixaTexto = modal.querySelector("[data-modal-texto]");
      caixaTexto.innerHTML = "";
      (a.corpo || []).forEach(function (paragrafo) {
        var ehTitulo = paragrafo.indexOf("## ") === 0;
        var el = document.createElement(ehTitulo ? "h3" : "p");
        el.className = ehTitulo ? "modal-artigo__subtitulo" : "modal-artigo__paragrafo";
        el.textContent = ehTitulo ? paragrafo.slice(3) : paragrafo;
        caixaTexto.appendChild(el);
      });
      var caixaTags = modal.querySelector("[data-modal-tags]");
      caixaTags.textContent = (a.palavras_chave || []).length ? a.palavras_chave.join(" · ") : "";
      modal.classList.add("modal-artigo--aberto");
      document.documentElement.classList.add("scroll-travado");
      modal.setAttribute("aria-hidden", "false");
      try { history.replaceState(null, "", "#" + id); } catch (e) {}
    };

    var fecharArtigoModal = function () {
      var modal = document.getElementById("modal-artigo");
      if (!modal) return;
      modal.classList.remove("modal-artigo--aberto");
      document.documentElement.classList.remove("scroll-travado");
      modal.setAttribute("aria-hidden", "true");
    };

    if (!document.getElementById("modal-artigo")) {
      var modalEl = document.createElement("div");
      modalEl.id = "modal-artigo";
      modalEl.className = "modal-artigo";
      modalEl.setAttribute("aria-hidden", "true");
      modalEl.innerHTML =
        '<div class="modal-artigo__fundo" data-modal-fechar></div>' +
        '<div class="modal-artigo__caixa" role="dialog" aria-modal="true" aria-label="Artigo">' +
        '<button type="button" class="modal-artigo__fechar" data-modal-fechar aria-label="Fechar">×</button>' +
        '<img data-modal-img class="modal-artigo__img" src="" alt="">' +
        '<div class="modal-artigo__corpo">' +
        '<p class="artigo__categoria" data-modal-categoria></p>' +
        '<h2 class="modal-artigo__titulo" data-modal-titulo></h2>' +
        '<p class="carimbo" data-modal-meta></p>' +
        '<p class="modal-artigo__resumo" data-modal-resumo></p>' +
        '<div class="modal-artigo__texto" data-modal-texto></div>' +
        '<p class="modal-artigo__tags" data-modal-tags></p>' +
        "</div>" +
        "</div>";
      document.body.appendChild(modalEl);
      modalEl.addEventListener("click", function (ev) {
        if (ev.target && ev.target.hasAttribute("data-modal-fechar")) fecharArtigoModal();
      });
      document.addEventListener("keydown", function (ev) {
        if (ev.key === "Escape") fecharArtigoModal();
      });
    }

    carregar("articles.json")
      .then(function (dados) {
        var artigos = (dados.artigos || []).slice(0, limiteRadar);
        $$("[data-radar-preparacao]").forEach(function (el) {
          if (!dados.secao_em_preparacao) el.remove();
        });

        if (!artigos.length) {
          alvoRadar.innerHTML = '<div class="vazio"><h3>' + T.radarVazio + "</h3></div>";
          return;
        }

        artigos.forEach(function (a) {
          artigosPorId[a.id] = a;
        });

        var reaisParaSEO = artigos.filter(function (a) {
          return !a.exemplo;
        });
        if (reaisParaSEO.length && !document.getElementById("ld-radar-agro")) {
          var itensLD = reaisParaSEO.map(function (a, i) {
            return {
              "@type": "ListItem",
              position: i + 1,
              item: {
                "@type": "NewsArticle",
                headline: a.titulo,
                description: a.resumo,
                image: [new URL(base + a.imagem, location.href).href],
                datePublished: a.data,
                author: { "@type": "Organization", name: a.autor || "Prime Fazendas" },
                publisher: {
                  "@type": "Organization",
                  name: "Prime Fazendas",
                  logo: { "@type": "ImageObject", url: new URL(base + "assets/img/brasao-320.webp", location.href).href }
                },
                mainEntityOfPage: new URL(base + "radar-agro.html#" + a.id, location.href).href,
                keywords: (a.palavras_chave || []).join(", ")
              }
            };
          });
          var ld = document.createElement("script");
          ld.type = "application/ld+json";
          ld.id = "ld-radar-agro";
          ld.textContent = JSON.stringify({
            "@context": "https://schema.org",
            "@type": "ItemList",
            itemListElement: itensLD
          });
          document.head.appendChild(ld);
        }

        alvoRadar.innerHTML = artigos
          .map(function (a, i) {
            var classe = i === 0 && limiteRadar > 1 ? "artigo" : "artigo artigo--lista";
            return (
              '<a class="' +
              classe +
              '" href="radar-agro.html#' +
              esc(a.id) +
              '" data-artigo-id="' +
              esc(a.id) +
              '">' +
              '<div class="artigo__figura"><img src="' +
              esc(base + a.imagem) +
              '" alt="" loading="eager" decoding="async" width="1200" height="800"></div>' +
              "<div>" +
              '<p class="artigo__meta"><span class="artigo__categoria">' +
              esc(a.categoria) +
              "</span>" +
              (a.exemplo ? "<span>" + T.exemplo + "</span>" : "") +
              "</p>" +
              '<h3 class="artigo__titulo">' +
              esc(a.titulo) +
              "</h3>" +
              "<p>" +
              esc(a.resumo) +
              "</p>" +
              "</div>" +
              "</a>"
            );
          })
          .join("");

        alvoRadar.addEventListener("click", function (ev) {
          var alvo = ev.target.closest("[data-artigo-id]");
          if (!alvo) return;
          ev.preventDefault();
          abrirArtigoModal(alvo.getAttribute("data-artigo-id"));
        });

        if (location.hash && artigosPorId[location.hash.slice(1)]) {
          abrirArtigoModal(location.hash.slice(1));
        }

        reobservar();
      })
      .catch(function () {
        alvoRadar.innerHTML = '<div class="vazio"><h3>' + T.radarVazio + "</h3></div>";
      });
  }

  /* ------------------------------------------- Radar Agro: últimas do mercado */
  var alvoMercado = $("[data-mercado]");

  if (alvoMercado) {
    var limiteMercado = parseInt(alvoMercado.getAttribute("data-mercado"), 10) || 6;
    carregar("noticias.json")
      .then(function (dados) {
        var itens = (dados.noticias || []).slice(0, limiteMercado);
        if (!itens.length) {
          (alvoMercado.closest("[data-bloco]") || alvoMercado).remove();
          return;
        }

        alvoMercado.innerHTML = itens.map(function (n) {
          return '<li><a class="manchete" href="' + esc(n.url) +
            '" target="_blank" rel="noopener noreferrer">' +
            '<span class="manchete__titulo">' + esc(n.titulo) + "</span>" +
            '<span class="manchete__fonte">' + esc(n.fonte || "") +
            (n.data ? " &middot; " + esc(dataCurta(n.data)) : "") + "</span></a></li>";
        }).join("");

        var carimbo = $("[data-mercado-atualizado]");
        if (carimbo && dados.atualizado_em) {
          carimbo.textContent = (idioma === "en" ? "Updated " : "Atualizado em ") +
            dataCurta(dados.atualizado_em.slice(0, 10));
        }
      })
      .catch(function () {
        (alvoMercado.closest("[data-bloco]") || alvoMercado).remove();
      });
  }

  function dataCurta(iso) {
    var p = String(iso).split("-");
    if (p.length < 3) return iso;
    var meses = idioma === "en"
      ? ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
      : ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"];
    return parseInt(p[2], 10) + " " + meses[parseInt(p[1], 10) - 1] + " " + p[0];
  }

  /* ----------------------------------------------------------- Agenda Agro */
  var alvoAgenda = $("[data-agenda]");

  if (alvoAgenda) {
    var limiteAgenda = parseInt(alvoAgenda.getAttribute("data-agenda"), 10) || 3;
    carregar("events.json")
      .then(function (dados) {
        var hoje = new Date();
        hoje.setHours(0, 0, 0, 0);

        var eventos = (dados.eventos || [])
          .filter(function (e) {
            var fim = new Date(e.fim || e.inicio);
            return !isNaN(fim) && fim >= hoje;
          })
          .sort(function (a, b) {
            return new Date(a.inicio) - new Date(b.inicio);
          })
          .slice(0, limiteAgenda);

        if (!eventos.length) {
          alvoAgenda.innerHTML =
            '<div class="vazio"><h3>' + T.agendaVazia + "</h3><p>" + T.agendaApoio + "</p></div>";
          return;
        }

        var meses = idioma === "en"
          ? ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
          : ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];

        alvoAgenda.innerHTML = eventos
          .map(function (e) {
            var d = new Date(e.inicio);
            var tag = e.url ? "a" : "div";
            return (
              "<" +
              tag +
              ' class="evento"' +
              (e.url ? ' href="' + esc(e.url) + '" rel="noopener"' : "") +
              ">" +
              '<span class="evento__data"><span class="evento__dia">' +
              d.getUTCDate() +
              '</span><span class="evento__mes">' +
              meses[d.getUTCMonth()] +
              "</span></span>" +
              "<span>" +
              '<span class="evento__nome">' +
              esc(e.nome) +
              "</span>" +
              '<span class="evento__meta">' +
              esc([e.cidade, e.estado, e.segmento].filter(Boolean).join(" · ")) +
              "</span>" +
              (e.prime ? '<span class="marcador">' + (idioma === "en" ? "Prime attending" : "Prime presente") + "</span>" : "") +
              "</span>" +
              "</" +
              tag +
              ">"
            );
          })
          .join("");
      })
      .catch(function () {
        alvoAgenda.innerHTML = '<div class="vazio"><h3>' + T.agendaVazia + "</h3></div>";
      });
  }

  /* ------------------------------------------------------------ formulários */
  $$("form[data-formulario]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      if (!form.checkValidity()) return;
      var acao = form.getAttribute("action");
      if (acao && acao !== "#") return; // deixa o backend responder

      e.preventDefault();
      var retorno = $(".retorno", form);
      if (retorno) {
        retorno.setAttribute("data-visivel", "true");
        retorno.textContent = T.enviado;
        retorno.setAttribute("role", "status");
        retorno.scrollIntoView({ block: "center", behavior: reduzido ? "auto" : "smooth" });
      }
      form.reset();
    });
  });

  /* ------------------------------------------------------- busca da home */
  var buscaHome = $("[data-busca-home]");
  if (buscaHome) {
    buscaHome.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(buscaHome);
      var q = new URLSearchParams();
      ["finalidade", "estado", "tipo", "area"].forEach(function (k) {
        if (f.get(k)) q.set(k, f.get(k));
      });
      var destino =
        f.get("finalidade") === "arrendamento" ? "arrendamentos.html" : "oportunidades.html";
      location.href = base + destino + (q.toString() ? "?" + q.toString() : "");
    });
  }
})();
