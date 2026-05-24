// Render all DH app store assets from HTML → PNG via headless Chrome.
// Also handles the mascot extraction (transparent PNG) as the first job.

const { execFileSync } = require('node:child_process');
const path = require('node:path');
const fs = require('node:fs');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HERE = __dirname;                            // .../app-store/source
const OUT = path.resolve(HERE, '..', 'out');       // .../app-store/out

function fileUrlOf(absPath) {
  return 'file:///' + absPath.replaceAll('\\', '/').split('/').map(encodeURIComponent).join('/');
}

function renderJob(job) {
  const srcPath = path.join(job.dir || HERE, job.src);
  const outPath = path.resolve(job.outDir || OUT, job.out);
  if (!fs.existsSync(path.dirname(outPath))) fs.mkdirSync(path.dirname(outPath), { recursive: true });

  const args = [
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--hide-scrollbars',
    '--force-device-scale-factor=1',
    `--window-size=${job.w},${job.h}`,
    `--virtual-time-budget=${job.budget || 8000}`,
  ];
  if (job.transparent) args.push('--default-background-color=00000000');
  args.push(`--screenshot=${outPath}`, fileUrlOf(srcPath));

  console.log(`Rendering ${job.src} (${job.w}×${job.h}${job.transparent ? ', transparent' : ''}) → ${path.basename(outPath)}`);
  execFileSync(CHROME, args, { stdio: 'inherit' });

  if (!fs.existsSync(outPath)) throw new Error(`Render failed — no output at ${outPath}`);
  const buf = fs.readFileSync(outPath);
  const colorType = buf[25];
  const w = buf.readUInt32BE(16);
  const h = buf.readUInt32BE(20);
  console.log(`  ✓ ${path.basename(outPath)}  ${w}×${h}  color_type=${colorType}  (${(buf.length / 1024).toFixed(1)} KB)\n`);
  return { outPath, colorType, w, h };
}

// Mascot extraction is handled separately by ~/tmp-img-proc/extract-mascot.js
// (npm install jimp fails on Windows for the Unicode-named "Deák Húsüzlet" folder).
// Run: cd ~/tmp-img-proc && node extract-mascot.js

const jobs = [
  { src: 'icon.html',                        out: 'icon-512.png',                       w: 512,  h: 512 },
  { src: 'feature-graphic-cream-hu.html',    out: 'feature-graphic-cream-hu.png',       w: 1024, h: 500 },
  { src: 'feature-graphic-cream-ro.html',    out: 'feature-graphic-cream-ro.png',       w: 1024, h: 500 },
  { src: 'feature-graphic-burgundy-hu.html', out: 'feature-graphic-burgundy-hu.png',    w: 1024, h: 500 },
  { src: 'feature-graphic-burgundy-ro.html', out: 'feature-graphic-burgundy-ro.png',    w: 1024, h: 500 },
];

for (const job of jobs) renderJob(job);
console.log('All renders complete.');
