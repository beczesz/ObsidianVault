---
id: fs_watch
title: fs.watch
layer: server
purpose: |
  A dash-server.mjs beépített Node.js `fs.watch` alapú fájlfigyelője.
  A vault markdown mappáját figyeli rekurzívan; változás esetén SSE
  broadcast-ot küld az összes csatlakozott kliensnek.
depends_on: [server, sse]
status_endpoint: /health (component: fs_watch)
index_schema_version: 1
---

## Miért létezik

Az SSE-alapú live update mechanizmus szív-dobbanása. Amikor egy agent
ír valamit a vaultba (pl. Alfred todos.md frissítése), az fs.watch
azonnal észleli és a megnyitott SSE streameken keresztül értesíti
a dashboard-okat — nincs polling overhead, azonnali push.

## Figyelt útvonalak

- `02_Areas/**/*.md` — area markdown fájlok
- `00_Prompts/**/*.md` — agent fájlok (AGENTS_INDEX, agent specs)
- `05_DailyNotes/**/*.md` — napi jegyzetek

## Debounce

Gyors egymás utáni változások (pl. git checkout több fájlt módosít)
100ms debounce-szal összevonódnak — nem okoznak N broadcast-ot.

## Megjegyzés

A Node `fs.watch` macOS-on `kqueue` alapú, nagyon hatékony. Vault
mérete (3000+ fájl) nem jelent problémát, mert a watch rekurzív
könyvtárfigyelést használ, nem per-fájl watch-ot.
