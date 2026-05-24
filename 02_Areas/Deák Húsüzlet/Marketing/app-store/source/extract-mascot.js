// Extract pig mascot from deak_face_logo.png to a transparent PNG via headless Chrome + canvas.toDataURL.
// Outputs source/pig-mascot.png with alpha channel.

const { execFileSync, spawnSync } = require('node:child_process');
const path = require('node:path');
const fs = require('node:fs');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HERE = __dirname;

// We use the DevTools Protocol via --remote-debugging-port to capture toDataURL output.
// Simpler approach: write a HTML page that processes the image and dumps the base64 PNG to
// a hidden <textarea>. Then read it from disk via a different trick: have the page write
// to localStorage / file via fetch? — no, file:// can't do that.
//
// Actually cleanest: have the HTML page render the processed canvas as an <img> with the
// extracted data URL, and screenshot the page. But Chrome screenshots have non-trivial
// alpha handling.
//
// Pivot to a yet-simpler path: skip transparency entirely.
// Use jimp via dynamic require — let's try installing it locally first.

console.log('Trying pure-JS image processing via jimp...');
const localJimpPath = path.join(HERE, 'node_modules', 'jimp');
if (!fs.existsSync(localJimpPath)) {
  console.log('Installing jimp locally...');
  const install = spawnSync('npm', ['install', '--no-save', '--prefix', HERE, 'jimp@0.22.12'], {
    stdio: 'inherit',
    shell: true,
  });
  if (install.status !== 0) {
    console.error('npm install jimp failed');
    process.exit(1);
  }
}

const Jimp = require(localJimpPath);

(async () => {
  const inputPath = path.join(HERE, 'deak_face_logo.png');
  const outputPath = path.join(HERE, 'pig-mascot.png');
  console.log(`Loading: ${inputPath}`);

  const img = await Jimp.read(inputPath);
  const w = img.getWidth();
  const h = img.getHeight();
  console.log(`Loaded ${w}x${h}`);

  // Build a visited mask via flood fill from the four edges.
  const visited = new Uint8Array(w * h);
  const stack = [];

  const isWhiteish = (x, y) => {
    const idx = (y * w + x) * 4;
    const r = img.bitmap.data[idx];
    const g = img.bitmap.data[idx + 1];
    const b = img.bitmap.data[idx + 2];
    return r >= 240 && g >= 240 && b >= 240;
  };

  const tryEnqueue = (x, y) => {
    if (x < 0 || y < 0 || x >= w || y >= h) return;
    const p = y * w + x;
    if (visited[p]) return;
    if (!isWhiteish(x, y)) return;
    visited[p] = 1;
    stack.push(p);
  };

  for (let x = 0; x < w; x++) { tryEnqueue(x, 0); tryEnqueue(x, h - 1); }
  for (let y = 0; y < h; y++) { tryEnqueue(0, y); tryEnqueue(w - 1, y); }

  while (stack.length) {
    const p = stack.pop();
    const x = p % w;
    const y = (p - x) / w;
    tryEnqueue(x - 1, y);
    tryEnqueue(x + 1, y);
    tryEnqueue(x, y - 1);
    tryEnqueue(x, y + 1);
  }

  // Apply alpha — background pixels fully transparent.
  let transparentCount = 0;
  for (let p = 0; p < w * h; p++) {
    if (visited[p]) {
      img.bitmap.data[p * 4 + 3] = 0;
      transparentCount++;
    }
  }

  // Anti-alias edge cleanup: near-white non-visited pixels adjacent to visited get faded alpha.
  for (let p = 0; p < w * h; p++) {
    if (visited[p]) continue;
    const idx = p * 4;
    const r = img.bitmap.data[idx];
    const g = img.bitmap.data[idx + 1];
    const b = img.bitmap.data[idx + 2];
    if (r >= 220 && g >= 220 && b >= 220) {
      const x = p % w;
      const y = (p - x) / w;
      let bgNeighbors = 0;
      if (x > 0 && visited[p - 1]) bgNeighbors++;
      if (x < w - 1 && visited[p + 1]) bgNeighbors++;
      if (y > 0 && visited[p - w]) bgNeighbors++;
      if (y < h - 1 && visited[p + w]) bgNeighbors++;
      if (bgNeighbors > 0) {
        const lum = (r + g + b) / 3;
        const fade = Math.max(0, Math.min(255, Math.round((255 - lum) * 8)));
        img.bitmap.data[idx + 3] = fade;
      }
    }
  }

  console.log(`Transparent pixels: ${transparentCount} / ${w * h} (${((transparentCount / (w * h)) * 100).toFixed(1)}%)`);
  await img.writeAsync(outputPath);
  console.log(`Wrote: ${outputPath}`);
})();
