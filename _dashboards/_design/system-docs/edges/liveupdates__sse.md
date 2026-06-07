---
from: liveupdates
to: sse
protocol: SSE
direction: client → server (connect) + server → client (events)
payload: text/event-stream
id: dfe449c0-8978-49b5-8935-daa70053f853
index_schema_version: 1
---

## Kapcsolat

A `live-updates.js` helper `EventSource` objektumot nyit a dash-server
`/__events` végpontjára. Ez egy hosszú életű HTTP kapcsolat, amelyen
a szerver push-olja a vault változásokat minden csatlakozott kliensnek.

## Kliens-oldali kód

```js
// live-updates.js belső logika (kivonatos):
const es = new EventSource('http://localhost:4321/__events');

es.addEventListener('message', function(e) {
  const ev = JSON.parse(e.data);
  if (ev.type === 'vault-update') {
    subscribers.forEach(fn => fn());  // triggereli a refetch+render-t
  }
});

es.addEventListener('error', function() {
  // 3s timeout után fallback: setInterval(8000)
  activatePollFallback();
});
```

## Szerver-oldali üzenet formátum

```
data: {"type":"vault-update","ts":1748611234}

: heartbeat
```

A heartbeat 15 másodpercenként megy, hogy a kapcsolat életben maradjon
proxy-k és tűzfalak mögött is.

## Fallback mechanizmus

Ha az SSE 3 másodpercen belül nem nyílik (events_server nem fut, file://
kontextus), a `live-updates.js` automatikusan `setInterval(8000)` polling
fallback-re vált. A status indicator pillen ezt "polling (fallback)" szöveg jelzi.

## Integration a dashboardba

```js
// Minden dashboard boot section-jában:
LiveUpdates.subscribe(refetchAndRender);
```
