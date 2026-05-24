---
title: Vault Indexing — Quick Start
date: 2026-05-24
status: active
description: Quick start guide a vault-indexing capability SQLite cache build+query CLI-jéhez. Tartalmazza az első build parancsát, query példákat és az ismert edge case-eket. A capabilities/vault-indexing/CLAUDE.md olvasandó a teljes architektúráért.
id: 11271a6d-aeb0-458c-b224-1927ccf1f2e3
index_schema_version: 1
---

# Vault Indexing — Quick Start

## Build the index (first time + after major changes)

```bash
cd "00_Prompts/BDOS/capabilities/vault-indexing"
python3 build_index.py
```

Expected: ~3000+ files indexed in <10 seconds. Output shows stats.

## Query examples

```bash
# All philosophy-category notes
python3 query.py --category philosophy

# All Sage thoughts (by schema)
python3 query.py --schema sage.thought.v1

# Personal Growth Area, only active/maturing
python3 query.py --area "Personal Growth" --status maturing

# Full-text on title + description (NOT body — by design, for token efficiency)
python3 query.py --fts "middle management"

# Orphans (files with no incoming and no outgoing wikilinks)
python3 query.py --orphans

# Backlinks to a specific atomic
python3 query.py --backlinks "cognition-replaces-middle-management"

# Vault stats
python3 query.py --stats

# JSON output for agent consumption
python3 query.py --category philosophy --json
```

## Python API

```python
import sys
sys.path.insert(0, "00_Prompts/BDOS/capabilities/vault-indexing")
import query

# Same params as CLI flags
results = query.query_notes(category='philosophy', status='maturing')
hits = query.fts_search('middle management', limit=10)
orphans = query.find_orphans()
stats = query.stats()
```

## What's NOT indexed

By design:
- `.smart-env/`, `.obsidian/` (vault metadata)
- `04_Archive/` (inactive content)
- `node_modules/`, `.git/`, `.trash/`
- Body full-text (only `title` + `description` in FTS — keeps the index tight, agents read full files only when relevant)

## Performance target (v0.1)

- Build: ~10 sec for 3K+ files
- Single-predicate query: <50ms
- FTS query: <100ms
- DB size: ~5-10 MB

---

## Watcher (incremental, v0.2)

```bash
./start.sh    # idempotens — ha már fut, semmi nem történik. Ha nem, indul + initial build ha kell.
./status.sh   # status check
./stop.sh     # clean stop
```

Polls vault every 5 seconds, applies incremental updates to changed files only. Log: `cache/watch.log`.

**stdlib only — nincs `watchdog` pip-dep szükséges.**

(Optionally upgrade to event-based sub-second updates: `pip3 install watchdog`, akkor egy v0.3 watch_event.py készíthető.)
