---
id: gdrive
title: Google Drive sync
layer: external
purpose: |
  A Google Drive Desktop client, amely a vault markdown fájlokat
  szinkronizálja a Mac és a Windows gép között. Bi-directional,
  conflict-free szinkronizáció (last-write-wins). A vault fizikailag
  a Google Drive "My Drive" mappájában él.
depends_on: []
status_endpoint: /health (component: gdrive)
index_schema_version: 1
---

## Miért létezik

A BDOS vault két gépen él párhuzamosan — a Mac-en ahol a szerver fut,
és egy Windows gépen ahol a felhasználó szerkeszt. A Google Drive
biztosítja, hogy mindkét gépen ugyanaz a vault tartalom legyen elérhető,
valós időben szinkronizálva.

## Szinkronizáció részletei

- **Protocol:** Google Drive REST API (Drive Desktop client)
- **Irány:** bi-directional
- **Conflict resolution:** last-write-wins (legutolsó módosítás nyer)
- **Latency:** általában 1-30s a változás után
- **Vault path Mac-en:** `~/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/`
- **Vault path Windows-on:** `G:\My Drive\0. Ideas Vault\` (vagy hasonló)

## Biztonsági megjegyzés

A `.gitignore` és `.claude/` mappák szándékosan ki vannak zárva a sync-ből.
Az OAuth tokenek és API kulcsok soha nem kerülnek a vault-ba.

## Kapcsolódó node

- `windows_peer` — a szinkronizáció másik végpontja
