---
from: daemon
to: vault_db
protocol: SQL write
direction: daemon → SQLite
payload: file frontmatter rows
label: incremental reindex
id: 34556663-7b07-4153-8db3-0d3c7a27ee3b
index_schema_version: 1
---

## Kapcsolat

Az `events_server.py` daemon SQLite write műveletekkel tartja frissen a
`vault.db` FTS5 indexét. Egy módosított fájl esetén UPSERT-et hajt végre
a `vault_files` táblán, majd frissíti a `vault_files_fts` virtuális táblát.

## Inkrementális logika

```python
def reindex_file(path):
    fm = parse_frontmatter(path)
    body = read_body(path)
    mtime = os.stat(path).st_mtime

    conn.execute("""
        INSERT INTO vault_files (path, title, description, status, tags, mtime, body)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(path) DO UPDATE SET
            title=excluded.title,
            description=excluded.description,
            mtime=excluded.mtime,
            body=excluded.body
        WHERE excluded.mtime > vault_files.mtime
    """, (path, fm.get('title'), fm.get('description'), fm.get('status'),
          ','.join(fm.get('tags', [])), mtime, body))
```

A `WHERE mtime >` feltétel kizárja az ismételt írást változatlan fájloknál.

## Teljes reindex

```bash
curl -X POST http://localhost:4321/api/reindex
# Ez a dash-server-en keresztül triggereli a Python full reindex-et
# (~3295 fájl, ~4 másodperc)
```

## Sidecar trigger

Minden sikeres UPSERT után a daemon frissíti a `vault_stats.json` sidecar-t:
```json
{ "indexed": 3295, "total": 3301, "pct": 99.8, "tier2_active_count": 3, "generated_at": "..." }
```
