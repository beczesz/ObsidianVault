---
from: gdrive
to: vault_md
protocol: file sync
direction: bi-directional
payload: markdown files
label: bi-directional
id: 8ad47399-90f7-4f24-9446-505d332a2bc1
index_schema_version: 1
---

## Kapcsolat

A Google Drive Desktop client szinkronizálja a vault markdown fájljait
a Mac és Windows gép között. Minden fájlmódosítás (bármelyik gépen)
automatikusan propagálódik a másikra, általában 5-30 másodpercen belül.

## Hogyan működik

A vault fizikailag a Google Drive "My Drive" mappájában él:

- **Mac:** `~/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/`
- **Windows:** `G:\My Drive\0. Ideas Vault\` (vagy platform-specifikus)

A Google Drive client FUSE mount-ként (Mac) vagy shell extension-ként
(Windows) integrálódik az OS-be. A fájlrendszer-szintű változások
automatikusan feltöltődnek és letöltődnek.

## Conflict kezelés

Google Drive a "last-write-wins" policy-t alkalmazza. Ha mindkét gépen
ugyanaz a fájl módosul egyszerre, a régebbi változat `.konfliktus` suffix-szel
mentődik el. Ez ritka, mert a felhasználó általában csak az egyik gépen
szerkeszt aktívan egyszerre.

## Kizárások

Az alábbi mappák **nem szinkronizálódnak** (gitignore / Drive exclusion):

- `.claude/` — Claude Code session adatok
- `.obsidian/` — Obsidian workspace konfig
- `.smart-env/` — Smart Connections cache
- `_dashboards/_tools/node_modules/` (ha létezne)

## Latency hatása a BDOS-ra

A 5-30s szinkronizációs latency azt jelenti, hogy Windows-on elvégzett
vault változások ~5-30 másodperccel később jelennek meg a Mac
dash-server-en és a dashboardokban (fs.watch → SSE chain után).
