// Pobiera widoczny tekst stron przez Chromium (Playwright) i proxy sesji.
// Użycie: NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt node tools/pw_text.js <url> [url...] [--full]
const { chromium } = require('playwright');
(async () => {
  const args = process.argv.slice(2);
  const full = args.includes('--full');
  const urls = args.filter(a => a !== '--full');
  const browser = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await browser.newContext();
  for (const url of urls) {
    const page = await ctx.newPage();
    try {
      const r = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await page.waitForTimeout(3000);
      const t = (await page.innerText('body')).replace(/\s+/g, ' ');
      console.log(`== ${url} | status=${r && r.status()} | title="${await page.title()}" | checked=${new Date().toISOString()}`);
      console.log(full ? t : t.slice(0, 500));
    } catch (e) {
      console.log(`== ${url} | ERROR ${e.message.split('\n')[0]}`);
    }
    await page.close();
  }
  await browser.close();
})();
