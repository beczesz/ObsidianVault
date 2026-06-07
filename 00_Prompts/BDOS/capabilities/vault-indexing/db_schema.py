#!/usr/bin/env python3
"""
db_schema.py — read-only schema + row-count introspection for the BDOS SQLite DBs.
Used by the System Architecture dashboard (dash-server.mjs GET /api/db/schema).

Outputs JSON:
  { "ok": true, "databases": [
      { "name": "vault.db", "path": "...", "exists": true, "size_bytes": N,
        "tables": [ { "name": "notes", "rows": 3304,
                      "columns": [ {"name":"id","type":"INTEGER","pk":1}, ... ] }, ... ] },
      ... ] }

Pure stdlib. Read-only (opens DBs in immutable/read-only mode). Never writes.
"""
from __future__ import annotations
import json
import sys
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import sqlite3

# vault.db is per-machine (runtime.py); agent_observability.db is the synced cache copy.
try:
    import runtime
    VAULT_DB = runtime.db_read_path()
except Exception:
    VAULT_DB = SCRIPT_DIR / "cache" / "vault.db"
OBS_DB = SCRIPT_DIR / "cache" / "agent_observability.db"


def introspect(path: Path) -> dict:
    p = Path(path)
    out = {"name": p.name, "path": str(p), "exists": p.exists(), "size_bytes": 0, "tables": []}
    if not p.exists():
        return out
    out["size_bytes"] = p.stat().st_size
    try:
        con = sqlite3.connect(f"file:{p}?mode=ro", uri=True, timeout=5)
    except Exception as e:
        out["error"] = str(e)
        return out
    try:
        con.execute("PRAGMA busy_timeout=3000")
        names = [r[0] for r in con.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        ).fetchall()]
        for name in names:
            cols = []
            for cid, cname, ctype, notnull, dflt, pk in con.execute(f'PRAGMA table_info("{name}")').fetchall():
                cols.append({"name": cname, "type": ctype or "", "pk": int(pk), "notnull": int(notnull)})
            try:
                rows = con.execute(f'SELECT COUNT(*) FROM "{name}"').fetchone()[0]
            except Exception:
                rows = None  # FTS shadow / virtual table edge cases
            out["tables"].append({"name": name, "rows": rows, "columns": cols})
    finally:
        con.close()
    return out


def main():
    result = {"ok": True, "databases": [introspect(VAULT_DB), introspect(OBS_DB)]}
    sys.stdout.write(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
