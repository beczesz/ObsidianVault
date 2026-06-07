---
id: sse
title: SSE /__events
layer: transport
purpose: |
  Server-Sent Events endpoint a dash-server-en belül (`/__events`).
  A fs.watch modul vault-változást érzékel, és az SSE streamen keresztül
  push-olja a kapcsolódó kliens-eknek (LiveUpdates). A kliens EventSource
  objektumot tart fenn erre a végpontra.
depends_on: [server, fs_watch]
status_endpoint: /health (component: sse)
index_schema_version: 1
---

## Miért létezik

Az SSE (Server-Sent Events) a legegyszerűbb push mechanizmus a böngésző
és a szerver között — egyirányú, hosszú életű HTTP kapcsolat, amit a
böngésző natívan kezel, reconnect logikával együtt. Nincs WebSocket
komplexitás, nincs külön protocol — egy sima `text/event-stream` response.

## Hogyan működik

1. A dashboard betöltésekor a `LiveUpdates` helper megnyit egy
   `EventSource('http://localhost:4321/__events')` kapcsolatot.
2. A dash-server a `/__events` kérésre `Content-Type: text/event-stream`
   fejléccel válaszol, és nyitva tartja a kapcsolatot.
3. Ha a `fs.watch` egy vault fájl változását érzékeli, a szerver
   `data: {"type":"vault-update","ts":...}` eseményt küld minden
   csatlakozott kliensnek.
4. A kliens eventlistener triggereli a `refetchAndRender()` hívást.

## Példa kliens-oldal

```js
const es = new EventSource('http://localhost:4321/__events');
es.onmessage = (e) => {
  const ev = JSON.parse(e.data);
  if (ev.type === 'vault-update') refetchAndRender();
};
es.onerror = () => {
  // LiveUpdates auto-fallback: 8s setInterval polling
};
```

## Heartbeat

A szerver 15 másodpercenként küld egy `: heartbeat` kommentárt, hogy
a kapcsolat életben maradjon proxy-k és load balancerek mögött is.
