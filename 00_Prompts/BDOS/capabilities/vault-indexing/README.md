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

## What IS indexed (coverage policy, 2026-06-07)

The single source of truth is [`policy.py`](policy.py). The index ingests two
classes of knowledge file:

- **Full-text** (`.md`, `.srt`, `.txt`, `.vtt`): body goes into the FTS lane.
  Transcripts have their timestamps stripped so only spoken text is indexed.
- **Metadata stub** (`.pdf`, `.docx`, `.xlsx`, `.pptx`, `.epub`, `.csv`, `.rtf`):
  path, filename-title, area, type, size, mtime, so the file is discoverable by
  structured query (`--content-class metadata`, `--ext .pdf`) even though its
  binary body is not extracted.

The `notes` table carries `ext` and `content_class` columns; query them with
`query.py --ext .srt` or `--content-class metadata`.

## What's NOT indexed

By policy (`policy.EXCLUDE_DIRS` + extension classes):
- `.smart-env/`, `.obsidian/`, `.smart-connections/` (vault metadata)
- `04_Archive/`, `_archive_old/` (inactive content, dark on purpose)
- `node_modules/`, `.git/`, `.trash/`
- `ExarSharedBrain/` (nested git repo of vault-mirrored duplicates)
- Media (`.mp3`, `.mp4`, images), assets (`.html`, `.js`, `.json`, `.py`), and
  binary noise (`.zip`, `.tmp`, ...)
- Binary document bodies (pdf/docx are stubs, not text-extracted, yet)

## Reach (the trust instrument)

`coverage_pct` from `emit_stats.py` used to be `indexed / total_md_files` where
both came from the index table, so it measured the index against itself and
could never report a miss. [`reach.py`](reach.py) fixes this: it compares the
index against the FILESYSTEM ground truth plus the coverage policy, and reports
three falsifiable failure modes (format gap, completeness gap, drift).

```bash
python3 reach.py            # writes 00_REACH_REPORT.md at the vault root + prints a summary
python3 reach.py --json     # machine-readable
```

`emit_stats.py` now sources its `coverage_pct` (and a `reach` block) from
reach.py, so the dashboard shows the real number.

### Growth guarantee

An incremental watcher can miss events (crash, sleep, Drive sync lag); an
event-based one never re-checks. So a scheduled backstop, [`reconcile.sh`](reconcile.sh)
(scheduler job `vault-index-reconcile`, interval 30 min), runs a full
disk-vs-index reconciliation independent of the live watcher and refreshes the
reach sidecar. Seed it with `python3 scheduler.py --seed-reach`. This is what
guarantees that anything you add becomes reachable even if the watcher hiccuped.

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
