#!/usr/bin/env node
// Check a resume page the way it will be used: printed to a Letter PDF and
// read by an applicant-tracking system.
//
//   node .claude/skills/tailor-resume/check.js resume/<slug>/index.html
//
// Prints the page count under two font setups (Fred prints from a Mac, where
// the page uses Helvetica Neue; it is emulated here with Arial-metric
// Liberation Sans at +3.5% size, which matches its widths), then the PDF text
// in the order a parser reads it (needs `pdftotext` from poppler-utils).
// Exits 1 if the resume runs past one page.

const fs = require('fs');
const os = require('os');
const path = require('path');
const { spawnSync } = require('child_process');

function loadPlaywright() {
  for (const p of ['playwright', '/opt/node-tools/node_modules/playwright']) {
    try { return require(p); } catch (e) { /* try the next one */ }
  }
  console.error('Playwright not found. Install it (npm i -D playwright) or run where it is available.');
  process.exit(2);
}

const pageCount = (file) =>
  (fs.readFileSync(file, 'latin1').match(/\/Type\s*\/Page[^s]/g) || []).length;

(async () => {
  const target = process.argv[2];
  if (!target) { console.error('usage: node check.js <resume html file>'); process.exit(2); }
  const url = 'file://' + path.resolve(target);
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const out = fs.mkdtempSync(path.join(os.tmpdir(), 'resume-check-'));
  const setups = [
    ['Helvetica Neue widths (Mac)', 'body{font-family:"Liberation Sans",Arial,sans-serif!important}' +
                                    '@media print{.sheet{font-size:10.35pt!important}}'],
    ['this machine\'s default fonts', ''],
  ];
  let worst = 0, macPdf = null;
  for (const [label, css] of setups) {
    const page = await browser.newPage();
    await page.goto(url);
    if (css) await page.addStyleTag({ content: css });
    const file = path.join(out, label.replace(/\W+/g, '_') + '.pdf');
    await page.pdf({ path: file, preferCSSPageSize: true, printBackground: false });
    const n = pageCount(file);
    worst = Math.max(worst, n);
    if (!macPdf) macPdf = file;
    console.log(`${n === 1 ? 'OK  ' : 'FAIL'} ${n} page${n === 1 ? '' : 's'} with ${label}`);
    await page.close();
  }
  await browser.close();

  const text = spawnSync('pdftotext', ['-raw', macPdf, '-'], { encoding: 'utf8' });
  if (text.status === 0) {
    console.log('\n--- PDF text, in the order a resume parser reads it ---\n' + text.stdout);
  } else {
    console.log('\n(pdftotext not available; skipped the reading-order check)');
  }
  console.log(`PDFs written to ${out}`);
  process.exit(worst > 1 ? 1 : 0);
})();
