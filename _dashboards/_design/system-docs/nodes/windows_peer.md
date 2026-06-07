---
id: windows_peer
title: Windows peer
layer: external
purpose: |
  A Windows gép, ahol a felhasználó az Obsidian desktop app-pal szerkeszti
  a vault-ot. A szinkronizáció a Google Drive Desktop kliensen keresztül
  zajlik — a Windows peer nem kommunikál közvetlenül a Mac dash-server-rel.
depends_on: [gdrive]
status_endpoint: /health (component: windows_peer)
index_schema_version: 1
---

## Miért létezik

A felhasználó elsősorban Windows gépen szerkeszti a vault-ot Obsidian-nal,
míg a BDOS operacionális infrastruktúra (dash-server, agentek, Claude CLI)
a Mac-en fut. A két gép a Google Drive-on keresztül szinkronizál.

## Szerepe a rendszerben

A windows_peer "read-write" a vault_md szempontjából — Obsidian-on keresztül
módosíthat bármit. Ezért a vault.db és a dashboardok folyamatosan szinkronban
kell legyenek (daemon + fs.watch gondoskodik erről).

## Szinkronizációs latency

A Windows → Mac sync latency általában 5-30s. Ez azt jelenti, hogy egy
Windows-on elvégzett változás 5-30 másodpercen belül megjelenik a Mac
dashboardjain (SSE push a fs.watch érzékelése után).

## Státusz

Az `idle` státusz normális — a windows_peer nem direktben monitorozható
a dash-server-ről. A /health `windows_peer` komponense a gdrive sync
freshness-ét méri proxy-ként.
