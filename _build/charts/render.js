// Render the chart SVGs to PNG at 2x. Run after zev_van_chart.py:
//   node _build/charts/render.js
// Needs Playwright with Chromium.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..', '..');
const jobs = [
  ['img/zev-van-sales-vs-target.svg', 'img/zev-van-sales-vs-target.png', 800, 480],
  ['_build/charts/out/zev-van-sales-vs-target-mobile.svg', 'img/zev-van-sales-vs-target-mobile.png', 400, 592],
];

(async () => {
  const browser = await chromium.launch();
  for (const [src, out, w, h] of jobs) {
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    const svg = fs.readFileSync(path.join(root, src), 'utf8');
    await page.setContent(`<!doctype html><style>html,body{margin:0;background:#0c1512}svg{display:block}</style>${svg}`);
    await page.screenshot({ path: path.join(root, out), omitBackground: false });
    await page.close();
    console.log('wrote', out);
  }
  await browser.close();
})();
