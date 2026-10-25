// Render an HTML file to PDF with page numbers: node render_pdf.js in.html out.pdf
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [src, dst] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(src), { waitUntil: 'load' });
  await page.pdf({
    path: dst,
    format: 'A4',
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate:
      '<div style="width:100%;text-align:center;font-size:8px;color:#999;font-family:NanumGothic,sans-serif">THE BOOK · <span class="pageNumber"></span></div>',
  });
  await browser.close();
})();
