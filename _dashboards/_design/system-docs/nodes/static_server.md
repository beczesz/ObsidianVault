---
id: static_server
title: Static server
layer: server
purpose: |
  A dash-server beépített statikus fájlszolgáltató logikája. A
  /_dashboards/ URL prefix-szel érkező kéréseket a vault _dashboards/
  mappájából szolgálja ki. Nincs külön szerver — a routing a
  dash-server.mjs main request handler-ében él.
depends_on: [server]
status_endpoint: /health (component: static_server)
index_schema_version: 1
---

## Miért létezik

A dashboardok HTML, CSS és JS fájljait a böngészőnek kell letöltenie.
A static server handler gondoskodik arról, hogy a `/_dashboards/system.html`
URL a megfelelő fizikai fájlt (`_dashboards/system.html`) adja vissza,
helyes Content-Type fejléccel.

## Működés

- URL `/_dashboards/` prefix → fájl a vault `_dashboards/` mappájából
- URL `/` → redirect a `/_dashboards/index.html`-re (launcher)
- MIME type inferálás: `.html` → `text/html`, `.js` → `application/javascript`,
  `.css` → `text/css`, `.json` → `application/json`, `.md` → `text/plain`

## Megjegyzés

A markdown fájlok (`system-docs/nodes/*.md`) is ezen a static server-en
keresztül töltődnek le a dashboard drawer-ébe. Ez az oka, hogy az
absolute URL (`/_dashboards/_design/system-docs/...`) működik fetch-ből.
