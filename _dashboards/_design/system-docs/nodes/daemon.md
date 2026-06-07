---
id: daemon
title: events_server.py
layer: daemon
purpose: |
  Python daemon, amely a vault.db inkrementális reindexelését végzi
  a watcher jelzései alapján. Opcionális komponens — a dash-server
  és a dashboardok enélkül is működnek, de a vault index csak manuálisan
  frissíthető.
depends_on: [vault_db, vault_md]
status_endpoint: /health (component: daemon)
index_schema_version: 1
---

## Miért létezik

A vault folyamatosan változik: agentek írnak, a felhasználó szerkeszt.
Az events_server.py gondoskodik arról, hogy a vault.db FTS5 index
mindig naprakész legyen, anélkül hogy teljes reindexet kellene futtatni.

## Működés

1. A watcher.py küld egy IPC jelzést egy megváltozott fájl path-jával
2. A daemon parse-olja az új/módosított markdown frontmatter-t
3. Az `UPDATE OR INSERT` SQL paranccsal frissíti a vault_files táblát
4. Frissíti a backlink graph-ot (ha wikilinkek változtak)
5. Triggereli a sidecar JSON refresh-t

## Indítás (opcionális)

```bash
cd 00_Prompts/BDOS/capabilities/vault-indexing
python3 launch.py start
# events_server.py listening on /tmp/bdos-events.sock
```

## Megjegyzés

Ha a daemon nem fut, a vault.db csak a `/api/reindex` POST-ra frissül
(teljes reindex, ~4mp). Ez elfogadható ha az index staleness nem kritikus.
