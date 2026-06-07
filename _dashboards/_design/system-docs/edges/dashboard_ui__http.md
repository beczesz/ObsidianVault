---
from: dashboard_ui
to: http
protocol: HTTP fetch
direction: client → server
payload: JSON
id: 72783186-341f-4eb8-a2a8-b1cdced0a68f
index_schema_version: 1
---

## Kapcsolat

A dashboardok JS-ből `fetch()` API-val hívják a localhost:4321-en futó
dash-server REST endpoint-jait. Minden nem-SSE interakció ezen az élen
megy keresztül: health polling, vault keresés, capture kérések, CLI
invokációk, DB schema lekérdezések.

A válasz mindig JSON (kivéve statikus fájlszolgáltatásnál). A `live-updates.js`
SSE-vel kombinálja a 8s polling-ot, hogy SSE-disconnect alatt is friss
adat legyen.

## Példa — health polling

```js
const r = await fetch('/health', { cache: 'no-store' });
const data = await r.json();
// { overall: 'ok', components: { server: {status:'ok',...}, ... } }
```

```bash
curl -s http://localhost:4321/health | jq .overall
# "ok"
```

## Példa — vault keresés

```js
const r = await fetch('/api/search?q=Alfred+capture', { cache: 'no-store' });
const { results } = await r.json();
// results[0] = { path: '...', title: 'Alfred', description: '...', score: 4.2 }
```

## Hibakezelés

Ha a szerver nem fut, a `fetch()` `TypeError: Failed to fetch`-et dob.
A dashboardok ezt úgy kezelik, hogy `gap` státuszt állítanak és egy
"Szerver nem elérhető" üzenetet mutatnak. Automatikus retry nincs —
a 5s/8s poll loop próbálkozik újra a következő ciklusban.
