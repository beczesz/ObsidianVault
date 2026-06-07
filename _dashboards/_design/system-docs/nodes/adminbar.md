---
id: adminbar
title: AdminBar
layer: client
purpose: |
  WordPress-stílusú, 34px magas, mindig sötét fixed top bar, amely
  minden dashboardon megjelenik. Öt kompakt status pillt, egy Agent
  Quick-Nav popupot és egy System drawer gombot tartalmaz.
  A _design/admin-bar.js shared helper valósítja meg.
depends_on: [http]
status_endpoint: /health (component: adminbar)
index_schema_version: 1
---

## Miért létezik

Az AdminBar a BDOS operacionális "idegrendszerének" felszíni rétege: bármely
dashboardon egy pillantással látható, hogy a szerver fut-e, az index friss-e,
a scheduler aktív-e. Nem per-dashboard fejleszthető — shared layer, amit a
Curator promote mód tart karban.

## Öt status pill

| Pill | Mit ellenőriz |
|------|---------------|
| Watchdog | `events_server.py` /health (port 4322) |
| Server | `dash-server.mjs` HEAD / (port 4321) |
| DB | `agent_logs.json` freshness + row count |
| Scheduler | utolsó `scheduled_jobs[].last_run_at` |
| Index | `agent_logs.json` generated_at within 24h |

## Agent Quick-Nav

Az `A` billentyű (input guarddal) megnyitja az Agent Quick-Nav popupot —
6-7 agent mini-kártya emoji + névvel + 1-soros leírással. Betű-gyorsbillentyűk
(L/M/C/P/B/F) az adott agent dashboardjára navigálnak. Az `S` billentyű a
System dashboardra navigál.

## Kapcsolódó fájlok

- `/_dashboards/_design/admin-bar.js` — a shared implementation
- [System dashboard](/_dashboards/system.html)
