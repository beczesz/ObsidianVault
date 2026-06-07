---
id: dashboard_ui
title: Dashboard UI
layer: client
purpose: |
  A böngészőben futó HTML dashboard-ok összessége — a Vault Dashboards
  family minden tagja (sales.html, alfred/index.html, system.html stb.).
  Ezek fetch()-csel hívják a dash-server REST végpontjait, és SSE-n
  keresztül kapnak élő frissítést.
depends_on: [http, sse]
status_endpoint: /health (component: dashboard_ui)
index_schema_version: 1
---

## Miért létezik

A dashboard UI az a layer, ahol a vault markdown-tartalom láthatóvá és
interaktívvá válik. A markdownban tárolt adatot (frontmatter, section-ok)
a dashboard JS parserek dolgozzák fel, és renderelnek belőle áttekinthető
vizualizációkat — pipeline kanban, habit tracker, agent observatory stb.

A dashboard-ok **read-only** kontrakt szerint működnek: soha nem írnak
vissza a markdownba, csak olvassák azt a dash-server végpontjain keresztül.
Ez garantálja, hogy az egyetlen forrás-az-igazságra mindig a markdown marad.

## Technikai részletek

Minden dashboard az alábbi shared engine-t használja:

- `tokens.css` — kanonikus design tokenek (DS §1)
- `theme.js` — light/dark téma, localStorage sync
- `clipboard.js` — card copy-ref + panel anchor helpers
- `live-updates.js` — SSE primary + 8s poll fallback
- `admin-bar.js` — fixed dark top bar, 5 status pill, agent quick-nav

Az adatforrás-lekérés `fetch()` + `setInterval(8000)` fallback kombinációval
történik. Az SSE stream (`/__events`) azonnali push-ot biztosít vault változáskor.

## Kapcsolódó dashboardok

- [Launcher](/_dashboards/index.html)
- [Curator — Dashboard Family](/_dashboards/curator/index.html)
