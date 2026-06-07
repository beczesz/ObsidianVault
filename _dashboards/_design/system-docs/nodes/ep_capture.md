---
id: ep_capture
title: /api/alfred/capture
layer: server
purpose: |
  Egyszerű inbox append végpont. A beérkező szöveget formázás/AI-parse
  nélkül hozzáfűzi az `inbox.md` fájlhoz timestamp-pel. A capture_box
  fallback útja, és az Alfred Alfred Inbox csatornájának belépőpontja.
depends_on: [server, vault_md]
status_endpoint: /health (component: ep_capture)
index_schema_version: 1
---

## Miért létezik

Néha az egyszerű, gyors rögzítés a cél — nincs szükség AI parse-ra,
elég hogy a gondolat ne vesszen el. A `/api/alfred/capture` ezt biztosítja:
minimális latency, nincs external dependency, 100% megbízható.

## Működés

```json
POST /api/alfred/capture
{"message": "Megnézni a Deák havi számokat"}

// vault-ba kerül:
// - 2026-05-30T14:32:00 Megnézni a Deák havi számokat
```

A markdown fájl elérési útja: `02_Areas/Personal Growth/Alfred/inbox.md`

## Biztonsági korlátok

- Csak localhost-ról elérhető
- Csak append — nem olvas, nem töröl, nem módosít meglévő tartalmat
- A fájlnév hardcoded (`inbox.md`) — nincs path traversal lehetőség
