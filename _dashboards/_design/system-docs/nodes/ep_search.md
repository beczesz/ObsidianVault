---
id: ep_search
title: /api/search
layer: server
purpose: |
  Vault full-text keresés végpont. Az SQLite FTS5 indexen (vault.db)
  fut BM25 relevancia-rangsorolással. A Librarian dashboard live
  search panelje és az Alfred agentek retrieval módja használja.
depends_on: [server, vault_db]
status_endpoint: /health (component: ep_search)
index_schema_version: 1
---

## Miért létezik

A vault 3000+ markdown fájlból áll. Nyers grep helyett az FTS5 index
millisecunder belül, relevancia-sorrendben adja vissza a találatokat,
a `description` és `title` frontmatter mezőkre fókuszálva (10-100x
token megtakarítás a teljes fájl olvasásához képest).

## API

```
GET /api/search?q=Alfred+capture
```

Válasz:
```json
{
  "query": "Alfred capture",
  "results": [
    { "path": "02_Areas/.../alfred.md", "title": "Alfred", "description": "...", "score": 4.2 }
  ],
  "duration_ms": 12
}
```

## Telemetria

Minden keresési kérés naplózódik az `agent_observability.db`-be
(agent_name=librarian, mode=retrieve, query_duration_ms, result_count, basis=FTS5 BM25),
és megjelenik a Librarian dashboard Logs paneljén.

## Kapcsolódó dashboard

- [Librarian — Knowledge Manager](/_dashboards/librarian/index.html)
