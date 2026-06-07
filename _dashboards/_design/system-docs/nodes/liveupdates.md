---
id: liveupdates
title: LiveUpdates (SSE)
layer: client
purpose: |
  A _design/live-updates.js shared helper — SSE EventSource kapcsolatot
  tart fenn az events_server.py felé (port 4322), és vault változáskor
  azonnal triggereli a dashboard refetch+render ciklust. Ha az SSE
  nem elérhető, 8s poll fallbackre vált automatikusan.
depends_on: [sse]
status_endpoint: /health (component: liveupdates)
index_schema_version: 1
---

## Miért létezik

A dashboardok élőek — ha a vault változik (egy ügynök ír egy fájlt, a
felhasználó szerkeszt valamit), a dashboard azonnal frissüljön anélkül,
hogy a felhasználónak F5-öt kellene nyomnia. A LiveUpdates ezt oldja meg
push alapon, SSE-n keresztül.

## Architektúra

- **Primary:** `EventSource('http://localhost:4322/events')` → `events_server.py`
  figyeli a `vault.db` mtime-ját. Változáskor broadcast: `data: {"type":"vault-update","ts":...}`
- **Fallback:** ha 3 másodpercen belül nem nyílik SSE, automatikusan
  `setInterval(8000)` polling aktiválódik. Status pill: "polling (fallback)"
- **Heartbeat:** `events_server.py` 15 másodpercenként küld `: heartbeat` sort

## Integráció

```js
LiveUpdates.subscribe(refetchAndRender);  // per-dashboard boot
LiveUpdates.mountStatusIndicator(document.querySelector('.masthead-toprow'));
```

## Kapcsolódó fájl

- `/_dashboards/_design/live-updates.js`
