/**
 * Imagem de compartilhamento (Open Graph, 1200x630):
 * paisagem da marca + brasão da Prime Fazendas.
 */
const fs = require('fs');
const path = require('path');
const RAIZ = path.dirname(__dirname);
const IMG = path.join(RAIZ, 'assets', 'img');

const paisagem = fs.readFileSync(path.join(IMG, 'hero-matopiba.svg'), 'utf8');
const corpo = paisagem.replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '');
const brasao = fs.readFileSync(path.join(IMG, 'brasao.webp')).toString('base64');

const W = 1200, H = 630, L = 300;

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Prime Fazendas">
<svg x="0" y="0" width="${W}" height="${H}" viewBox="0 0 2400 1240" preserveAspectRatio="xMidYMid slice">
${corpo}
</svg>
<rect width="${W}" height="${H}" fill="#0B1D2A" opacity=".66"/>
<image href="data:image/webp;base64,${brasao}" x="${(W - L) / 2}" y="118" width="${L}" height="${L * 400 / 392}"/>
<text x="${W / 2}" y="${H - 96}" text-anchor="middle" font-family="Manrope, system-ui, sans-serif"
      font-size="26" font-weight="500" fill="#F4F1E9" opacity=".92">Terras que produzem. Oportunidades que conectam.</text>
<text x="${W / 2}" y="${H - 54}" text-anchor="middle" font-family="Manrope, system-ui, sans-serif"
      font-size="16" font-weight="700" letter-spacing="4.5" fill="#B79A5B">MATOPIBA</text>
</svg>
`;
fs.writeFileSync(path.join(IMG, 'og.svg'), svg);
console.log('og.svg', (svg.length / 1024).toFixed(0), 'KB');
