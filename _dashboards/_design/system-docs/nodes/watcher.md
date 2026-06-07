---
id: watcher
title: watch_event.py
layer: daemon
purpose: |
  Python watchdog script, amely a vault markdown fájlok változásait
  érzékeli (inotify/kqueue alapon) és IPC-n keresztül értesíti az
  events_server.py daemon-t, amely elvégzi az inkrementális reindexelést.
  Opcionális komponens — a szerver nélküle is fut.
depends_on: []
status_endpoint: /health (component: watcher)
index_schema_version: 1
---

## Miért létezik

A valós idejű vault indexelés alapja. Ahelyett hogy 5 másodpercenként
teljes reindexet futtatna (lassú, CPU-intenzív), a watcher csak a ténylegesen
megváltozott fájlokat jelzi az indexelő daemon-nak — inkrementális,
hatékony.

## Indítás

```bash
cd 00_Prompts/BDOS/capabilities/vault-indexing
python3 launch.py start
```

A PID a `cache/watch.pid` fájlba kerül.

## Státusz

Az `idle` státusz normális, ha a daemon nem fut. A watcher opcionális —
a rendszer teljes mértékben működik nélküle is (manuális reindex-szel).

## [TODO: pontosítás]

A watcher és daemon közötti IPC mechanizmus pontos protokollja
(Unix socket vs. pipe vs. signal) pontosítandó a dash-server.mjs
forráskódjából.
