---
from: fs_watch
to: sse
protocol: event push
direction: internal (server → SSE broadcast)
payload: vault-update event
id: 70b6a38a-349a-469d-91f6-220f53b07743
index_schema_version: 1
---

## Kapcsolat

A dash-server.mjs beépített `fs.watch` modulja vault fájlváltozást érzékel,
és az SSE broadcast mechanizmusán keresztül azonnali push értesítést küld
minden csatlakozott dashboard kliensnek.

## Belső flow (dash-server.mjs)

```js
// Kliensek listája (minden SSE kapcsolat)
const sseClients = new Set();

// fs.watch beállítás
const watcher = fs.watch(VAULT_PATH, { recursive: true }, debounce((event, filename) => {
  if (!filename || !filename.endsWith('.md')) return;
  broadcastVaultUpdate();
}, 100));

function broadcastVaultUpdate() {
  const msg = `data: ${JSON.stringify({ type: 'vault-update', ts: Date.now() })}\n\n`;
  sseClients.forEach(res => {
    try { res.write(msg); }
    catch { sseClients.delete(res); }
  });
}
```

## SSE kapcsolat kezelés

Amikor egy kliens csatlakozik a `/__events` végpontra:

```js
app.get('/__events', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Access-Control-Allow-Origin': '*'
  });
  sseClients.add(res);
  req.on('close', () => sseClients.delete(res));

  // Heartbeat 15s-enként
  const heartbeat = setInterval(() => res.write(': heartbeat\n\n'), 15000);
  req.on('close', () => clearInterval(heartbeat));
});
```
