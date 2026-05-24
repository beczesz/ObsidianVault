#!/usr/bin/env node
/* ===========================================================================
   Ideas Vault dashboard server.
   Zero-dependency static server + file-watcher push channel (SSE).
   ===========================================================================
   - Serves the whole vault root, so dashboards fetch any markdown via absolute
     paths like /02_Areas/Sonrisa/CPS/Sales/Pipeline.md
   - Watches 02_Areas for *.md changes and pushes a "change" Server-Sent Event
     on /__events, so connected dashboards refresh sub-second.
   - Routes / to the launcher at /_dashboards/index.html
   - Pure Node (http + fs.watch), no npm install. fs.watch recursive works on
     Windows and macOS.

   Run:
     node dash-server.mjs            (default port 4321)
     PORT=8000 node dash-server.mjs  (override port)
   Or use the start.ps1 / start.bat / start.sh wrappers in this folder.
   =========================================================================== */

import http from 'http';
import { stat, readFile } from 'fs/promises';
import { watch } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, resolve, join, extname, normalize } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const VAULT_ROOT = resolve(__dirname, '..', '..');   // _dashboards/_tools -> vault root
const LAUNCHER = '/_dashboards/index.html';
const PORT = Number(process.env.PORT || process.argv[2] || 4321);

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.md':   'text/markdown; charset=utf-8',
  '.css':  'text/css; charset=utf-8',
  '.js':   'text/javascript; charset=utf-8',
  '.mjs':  'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg':  'image/svg+xml',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif':  'image/gif',
  '.ico':  'image/x-icon',
  '.woff2':'font/woff2',
  '.txt':  'text/plain; charset=utf-8',
};

/* ---- SSE clients ---- */
const clients = new Set();
function broadcast(eventName, dataObj) {
  const payload = `event: ${eventName}\ndata: ${JSON.stringify(dataObj)}\n\n`;
  for (const res of clients) {
    try { res.write(payload); } catch { /* dropped client */ }
  }
}

/* ---- file watcher (debounced) ---- */
let debounceTimer = null;
const pending = new Set();
function onChange(filename) {
  if (!filename) pending.add('*');
  else if (/\.md$/i.test(filename)) pending.add(filename);
  else return;
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    const files = [...pending];
    pending.clear();
    broadcast('change', { files, ts: Date.now() });
    console.log(`[watch] change -> ${files.join(', ')}`);
  }, 150);
}
// Watch only the subtrees the live dashboards actually read. Watching all of
// 02_Areas is a trap: a vault-wide event (OneDrive / git re-sync touching
// thousands of files) floods the event loop and the server stops responding.
// Override with WATCH_DIRS="a,b,c" (comma-separated, vault-root-relative).
const WATCH_DIRS = (process.env.WATCH_DIRS || '02_Areas/Sonrisa/CPS,02_Areas/Navigátor Podcast')
  .split(',').map(s => s.trim()).filter(Boolean);
for (const d of WATCH_DIRS) {
  try {
    watch(join(VAULT_ROOT, d), { recursive: true }, (_e, filename) => onChange(filename));
    console.log(`[watch] watching ${d} (recursive) for *.md changes`);
  } catch (e) {
    console.warn(`[watch] cannot watch ${d}:`, e.message);
  }
}

/* ---- request handling ---- */
function decodePath(p) { try { return decodeURIComponent(p); } catch { return p; } }
function safeResolve(urlPath) {
  const rel = normalize(decodePath(urlPath)).replace(/^([\\/]|\.\.[\\/])+/, '');
  const abs = resolve(VAULT_ROOT, rel);
  if (abs !== VAULT_ROOT && !abs.startsWith(VAULT_ROOT)) return null; // traversal guard
  return abs;
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  let pathname = url.pathname;

  if (pathname === '/__events') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': '*',
    });
    res.write('retry: 3000\n\n');
    clients.add(res);
    const ping = setInterval(() => { try { res.write(': ping\n\n'); } catch {} }, 25000);
    req.on('close', () => { clearInterval(ping); clients.delete(res); });
    return;
  }

  if (pathname === '/' || pathname === '') pathname = LAUNCHER;

  const abs = safeResolve(pathname);
  if (!abs) { res.writeHead(403); res.end('Forbidden'); return; }

  try {
    let s = await stat(abs);
    let filePath = abs;
    if (s.isDirectory()) { filePath = join(abs, 'index.html'); s = await stat(filePath); }
    const type = MIME[extname(filePath).toLowerCase()] || 'application/octet-stream';
    const body = await readFile(filePath);
    res.writeHead(200, { 'Content-Type': type, 'Cache-Control': 'no-store' });
    res.end(body);
  } catch {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Not found: ' + pathname);
  }
});

server.listen(PORT, () => {
  console.log('Ideas Vault dashboards');
  console.log(`  serving:  ${VAULT_ROOT}`);
  console.log(`  open:     http://localhost:${PORT}/`);
  console.log(`  launcher: http://localhost:${PORT}${LAUNCHER}`);
  console.log(`  live:     editing ${WATCH_DIRS.join(', ')}/**/*.md pushes updates via /__events`);
});
