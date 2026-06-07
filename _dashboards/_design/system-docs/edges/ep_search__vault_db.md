---
from: ep_search
to: vault_db
protocol: SQL FTS5
direction: server → SQLite
payload: SQL query + result rows
id: c56d6861-357e-4d62-ade1-222e43c72c65
index_schema_version: 1
---

## Kapcsolat

Az `/api/search` handler Better-SQLite3 (vagy Node sqlite3) modullal
csatlakozik a `vault.db`-hez és FTS5 BM25 keresést futtat a
`vault_files_fts` virtuális táblán.

## SQL lekérdezés (kivonatos)

```sql
SELECT
  vf.path,
  vf.title,
  vf.description,
  vf.status,
  vf.tags,
  bm25(vault_files_fts) as score
FROM vault_files_fts
JOIN vault_files vf ON vault_files_fts.rowid = vf.rowid
WHERE vault_files_fts MATCH ?
ORDER BY score
LIMIT 20;
```

## BM25 súlyozás

Az FTS5 BM25 implementáció a `title` mezőt 4x, a `description` mezőt 2x,
a `body` tartalmat 1x súlyozza. Ez azt jelenti, hogy egy találat, ahol
a keresett szó a title-ben van, magasabbra rangsorolódik.

## Teljesítmény

- Átlagos lekérdezési idő: 5-20ms (3295 fájl indexen)
- Maximális result count: 20 (configurable)

## Telemetria

```js
// Minden keresés után:
await logToDb({
  agent_name: 'librarian',
  mode: 'retrieve',
  message: `search: "${query}" → ${results.length} results`,
  duration_ms: elapsed,
  tags: ['search', 'fts5']
});
```

## Példa

```bash
curl -s "http://localhost:4321/api/search?q=sprint+deák" | jq '.results[].title'
```
