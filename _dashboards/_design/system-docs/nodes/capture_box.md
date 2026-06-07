---
id: capture_box
title: Capture box
layer: client
purpose: |
  Az Alfred dashboard gyors-beviteli textarea-ja. A felhasználó begépel
  egy gondolatot, feladatot vagy emlékeztetőt, és a POST /api/alfred/capture
  (vagy /api/alfred/process) végponton keresztül kerül a vaultba.
depends_on: [http]
status_endpoint: /health (component: capture_box)
index_schema_version: 1
---

## Miért létezik

A capture box az Alfred dashboard "inbox" kapuja. Lehetővé teszi, hogy a
felhasználó gyorsan rögzítsen bármit (ötlet, todo, reminder) anélkül, hogy
az Obsidian vault-ot kellene megnyitnia. A Cmd/Ctrl+Enter shortcut azonnali
küldést tesz lehetővé.

## Két feldolgozási út

1. **`/api/alfred/process`** (Haiku 4.5 immediate parse): az AI kinyeri a
   scope-ot, határidőt, prioritást, és közvetlenül a megfelelő
   `todos/<scope>.md` fájlba írja taskként.
2. **`/api/alfred/capture`** (fallback): ha az AI nem elérhető, az üzenet
   az `inbox.md` végére kerül append-eléssel — feldolgozás manualisan
   vagy következő Alfred sync-kor.

## Hibamódok

- AI timeout → capture fallback, amber chip visszajelzés
- HTTP hiba → piros chip + console.warn
- Üres bevitel → küldés tiltva (disabled state)

## Kapcsolódó dashboard

- [Alfred dashboard](/_dashboards/alfred/index.html)
