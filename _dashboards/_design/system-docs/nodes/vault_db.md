---
id: vault_db
title: vault.db (FTS5)
layer: data
purpose: |
  SQLite adatbázis a vault markdown fájlok frontmatter-ének és
  tartalmának FTS5 full-text indexével. A Librarian agent cache-first
  retrieve módja és az /api/search végpont ebből dolgozik.
  Regenerálható — ha elvész vagy sérül, a daemon újraépíti.
depends_on: []
status_endpoint: /health (component: vault_db)
index_schema_version: 1
---

## Miért létezik

3000+ markdown fájlon grep-elni minden kérésnél 100-1000ms lenne.
Az FTS5 index millisecunder belül ad vissza relevancia-sorrendbe rendezett
találatokat a `description` és `title` mezőkre. Ez az alap a Librarian
10-100x token megtakarításához (cache-first retrieve mód).

## Séma

Főbb táblák (a DB schema modal teljes listát ad):

- `vault_files` — path, title, description, status, date, tags, mtime
- `vault_files_fts` — FTS5 virtual table (title + description)
- `backlinks` — from_path → to_path link graph
- `orphans` — fájlok incoming link nélkül

## Méret és teljesítmény

~3295 fájl indexelve, ~2.4 MB DB méret, ~4 mp teljes újraindexelés.
Inkrementális frissítés a daemon által: csak a módosított fájlok
kerülnek újraindexelésre (mtime alapon).

## Reindex

```bash
curl -s -X POST http://localhost:4321/api/reindex
# {"ok": true, "message": "reindex started"}
```

Vagy a System dashboard node popup-jából: "Reindex" gomb.

## Kapcsolódó

- [Librarian dashboard](/_dashboards/librarian/index.html)
