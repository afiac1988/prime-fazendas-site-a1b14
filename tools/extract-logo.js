/**
 * Prime Fazendas — extração da marca original.
 *
 * O PDF da marca traz quatro versões do logotipo empilhadas numa página A4.
 * Este script mede cada caminho, agrupa símbolo + tipografia em pares,
 * escolhe o par mais bem desenhado e grava dois SVGs recortados:
 *
 *   assets/img/marca-simbolo.svg   símbolo em dourado (favicon, uso solto)
 *   assets/img/marca-inline.svg    símbolo em currentColor (embutido no HTML)
 *   assets/img/marca-completa.svg  símbolo + tipografia, em dourado
 *
 * Uso:  pdftocairo -svg PrimeFazendas.pdf /tmp/logo-raw.svg && node tools/extract-logo.js
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const RAIZ = path.dirname(__dirname);
const IMG = path.join(RAIZ, 'assets', 'img');
const DOURADO = '#B79A5B';
const PAD = 4;

(async () => {
  const bruto = fs.readFileSync('/tmp/logo-raw.svg', 'utf8');
  const paths = bruto.match(/<path[^>]*\/>/g)
    .filter(p => !p.includes('rgb(100%, 100%, 100%)'));      // fora o fundo da página

  const doc = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 595.2756 841.8898">${
    paths.map((p, i) => p.replace('<path', `<path id="p${i}"`)).join('')}</svg>`;
  fs.writeFileSync('/tmp/_bb.svg', doc);

  const b = await chromium.launch();
  const pg = await b.newPage();
  await pg.goto('file:///tmp/_bb.svg');
  const cx = await pg.evaluate(n => {
    const r = [];
    for (let i = 0; i < n; i++) {
      const bb = document.getElementById('p' + i).getBBox();
      r.push({ i, x: bb.x, y: bb.y, w: bb.width, h: bb.height });
    }
    return r;
  }, paths.length);
  await b.close();

  // símbolo: proporção quase quadrada · tipografia: larga e baixa
  const simbolos = cx.filter(o => o.w / o.h > 0.8 && o.w / o.h < 1.25 && o.w > 60);
  const textos = cx.filter(o => o.w / o.h > 5);

  const pares = simbolos.map(s => {
    const abaixo = textos
      .filter(t => t.y > s.y && t.y - (s.y + s.h) < s.h)
      .sort((a, b) => a.y - b.y)[0];
    return abaixo ? { s, t: abaixo } : null;
  }).filter(Boolean);

  if (!pares.length) throw new Error('nenhum par símbolo+tipografia encontrado');

  // o par cuja tipografia é mais larga é o desenho em maior resolução
  const melhor = pares.sort((a, b) => b.t.w - a.t.w)[0];
  console.log(`${pares.length} versões no PDF; usando a que começa em y=${melhor.s.y.toFixed(0)}`);

  const caixa = (...os) => {
    const x0 = Math.min(...os.map(o => o.x)), y0 = Math.min(...os.map(o => o.y));
    const x1 = Math.max(...os.map(o => o.x + o.w)), y1 = Math.max(...os.map(o => o.y + o.h));
    return `${(x0 - PAD).toFixed(2)} ${(y0 - PAD).toFixed(2)} ${(x1 - x0 + PAD * 2).toFixed(2)} ${(y1 - y0 + PAD * 2).toFixed(2)}`;
  };

  const monta = (indices, viewBox, cor, arquivo) => {
    const corpo = indices
      .map(i => paths[i].replace(/fill="rgb\([^)]*\)"/, `fill="${cor}"`))
      .join('\n');
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${viewBox}" role="img" aria-label="Prime Fazendas">\n${corpo}\n</svg>\n`;
    fs.writeFileSync(path.join(IMG, arquivo), svg);
    console.log(`  ${arquivo}  ${(svg.length / 1024).toFixed(0)} KB`);
  };

  // dourado: uso solto (favicon, <img>), onde currentColor não é herdado
  monta([melhor.s.i], caixa(melhor.s), DOURADO, 'marca-simbolo.svg');
  // currentColor: para ser embutido no HTML e acompanhar a cor do texto
  monta([melhor.s.i], caixa(melhor.s), 'currentColor', 'marca-inline.svg');
  monta([melhor.s.i, melhor.t.i], caixa(melhor.s, melhor.t), DOURADO, 'marca-completa.svg');
})();
