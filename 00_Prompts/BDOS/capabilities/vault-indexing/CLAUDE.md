---
title: Vault Indexing — SQLite-backed metadata read-cache for BDOS
date: 2026-05-24
author: Becze Szabolcs + Librarian research
status: active
version: 0.1
description: Lightweight SQLite read-cache a vault markdown frontmatterjeire és wikilinkjeire. A markdown a forrás-az-igazságra — az SQLite egy REGENERÁLHATÓ cache, NEM write-target. Agentek (különösen Librarian retrieve módja és Maestro observe) ezen át queryelnek metadata-szintű találatokat ~10-100x token-takarékossággal a full-context scan helyett.
tags: [BDOS, capability, indexing, sqlite, metadata, librarian]
id: b853bfe0-b23a-4146-9f5a-a881800afb39
index_schema_version: 1
---

# Vault Indexing (v0.1)

> **A markdown a forrás-az-igazságra.** Az SQLite egy READ-CACHE, mindig regenerálható a vault-ból. Az agentek a markdown fájlokba írnak — az indexerre nincs write-flow.

## Mit ad

- Frontmatter mezők lekérdezése `<50ms`-ben (3304 fájl → 1-2 sec)
- Wikilink-graph + backlinks + orphan detection
- FTS5 full-text keresés a `description` és `title` mezőkön (NEM a body-n — szándékosan)
- Token-takarékos retrieve: 80% relevance assessment a body-olvasás nélkül

## Fájlok

| Fájl | Mit ad |
|---|---|
| `schema.sql` | SQLite DDL — `notes` + `backlinks` + `notes_fts` táblák |
| `build_index.py` | Full-rebuild script. Walk + parse + insert. Idempotens. |
| `query.py` | Python query API + CLI az agentek számára |
| `cache/vault.db` | A generált SQLite database (gitignore-olt) |
| `README.md` | Setup + usage |

## Anti-pattern (Librarian research §architectural recommendations)

**NE használd write-targetnek.** A markdown fájlok soha nem válhatnak stub-bé. Ha a cache törlődik, a vault-nak állnia kell — emberileg olvasható maradnia.

## Használat

```bash
# Full rebuild (futtass amikor sok változás van vagy schema változik)
python3 build_index.py

# Query CLI
python3 query.py --category philosophy --status maturing
python3 query.py --area "Personal Growth" --tag ai-native
python3 query.py --orphans  # fájlok, ahova semmi nem mutat
python3 query.py --fts "middle management"  # FTS5 a description-on
```

## Roadmap

- **v0.1 (most):** full-rebuild + query CLI + Python API
- **v0.2:** filesystem watcher (incremental update via `watchdog`)
- **v0.3:** Librarian retrieve módba integrálva — automatikus cache-first lookup
- **v0.4:** Maestro observe módba integrálva — log-aggregálás cache-en át
- **v0.5:** networkx PageRank a backlink graph-on retrieve scoring-hoz
