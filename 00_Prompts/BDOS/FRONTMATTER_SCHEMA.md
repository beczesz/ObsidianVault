---
title: BDOS Frontmatter Schema — Canonical
date: 2026-05-24
author: Becze Szabolcs + Librarian Phase 4
status: active
version: 1.0
schema: bdos.frontmatter.v1
description: A BDOS-vault frontmatter szabványa. Definiálja a kötelező / opcionális / reserved mezőket, a Librarian indexing-rétegéhez szükséges metadata-struktúrát. Source of truth — minden új fájl ezt követi. Schema-evolúció = új major bump.
tags: [BDOS, schema, frontmatter, indexing, canonical, librarian]
id: 0c16c484-a4c8-4d54-b0d8-385dc974f2cf
index_schema_version: 1
---

# BDOS Frontmatter Schema v1

> **Single source of truth** a BDOS-vault frontmatter konvencióira.
> Librarian indexing-réteg (Phase 4) erre épít.
> Schema-evolúció = új major bump (v2, v3, ...) — fields not deleted, just deprecated.

---

## 1. Két tier — required vs optional

A schema **tier**-ekre van bontva. Minden indexelt fájl minimum a **Tier 0**-t teljesíti.

### Tier 0 — Required for ANY indexed file

```yaml
---
title: <string>                # 1-line human title
description: <string>          # 1-2 sentence content-driven summary (Phase 3.1 mandate)
date: <YYYY-MM-DD>             # creation or last-major-update
status: active|draft|done|archived
---
```

### Tier 1 — Phase 4 indexing additions (MANDATORY for new files from 2026-05-24)

```yaml
id: <uuid4>                    # stable identity — survives path moves/renames
index_schema_version: 1        # this schema version
bdos_index: true|false         # default true; explicit false excludes
```

### Tier 2 — Optional, content-type-specific

```yaml
schema: <schema-id>            # e.g. sage.thought.v1, bdos.operational.log.v1
version: <semver>              # for versioned files (agents, project state)
author: Becze Szabolcs
tags: [<list>]                 # free tags
category: <single>             # primary topical category
subcategory: <single>          # secondary
area: <area-name>              # derived from path normally, but explicit OK
agent: <agent-name>            # which BDOS agent owns/produced this
related: [<wikilinks>]         # explicit relationships
```

### Tier 3 — Reserved for Librarian internal use (NOT user-editable)

```yaml
_index_health: ok|stale|needs_reindex|broken|orphaned|duplicate_id|missing_fields|archived|excluded
_indexed_at: <ISO 8601>        # last successful indexing timestamp
_index_keywords: [<list>]      # extracted keywords (Phase 4.C)
_index_entities: [<list>]      # extracted entities (Phase 4.C)
```

The `_`-prefixed fields are managed by Librarian — users don't edit them.

---

## 2. Health states (Tier 3 `_index_health` enum)

| State | Mit jelent | Mit tegyen Librarian |
|---|---|---|
| `ok` | Index up-to-date, frontmatter valid | Continue |
| `stale` | File mtime > _indexed_at, needs re-index | `index_file()` re-run |
| `needs_reindex` | Schema version mismatch | Migration + re-index |
| `broken_frontmatter` | YAML parse error | Flag to user, lenient parser fallback already in place |
| `duplicate_id` | Another file has the same `id` | Audit alert — manual resolution |
| `orphaned` | No backlinks AND no description AND not on any index | Phase 4.B audit candidate |
| `missing_required_fields` | Tier 0 incomplete | Audit + user notification |
| `archived` | In `04_Archive/` or `_archive/` | Excluded from active queries by default |
| `excluded` | `bdos_index: false` set explicitly | Skip indexing |

---

## 3. ID layer — UUID generation rules

**ID format:** UUID4 (RFC 4122), lowercase hex with dashes.
**Example:** `id: 7c9e6f0a-3d4b-4c8e-9f1a-2b5c6d7e8f9a`

**Generation rules:**
- Once assigned, **never change**, even if file is renamed/moved
- If a file is split into two, the original ID stays with one; the new gets a fresh UUID + `lineage: { split_from: <original-uuid> }`
- If two files merge, the merged file gets a fresh UUID + `lineage: { merged_from: [<uuid1>, <uuid2>] }`
- Migration: `migrate_uuid.py` adds `id:` to existing files (Phase 4.A initial run)

**`id` is the cross-file relationship anchor.** Wikilinks resolve to paths AND IDs both — Librarian backlink index uses ID first, falls back to path matching.

---

## 4. Bdos_index — opt-out mechanism

**Default:** all `.md` files indexed.

**Per-file opt-out:**
```yaml
bdos_index: false
```
Use cases: drafts, sensitive content, temporary scratch, files you don't want surfaced.

**Folder-level opt-out:** create a `.bdosignore` file in a folder. Format: glob patterns (like `.gitignore`):
```
# .bdosignore
*.draft.md
private/
```

**Auto-excluded (built-in):**
- `.smart-env/`, `.obsidian/`, `04_Archive/`, `node_modules/`, `.git/`, `.trash/`
- Files starting with `_` in private folders

---

## 5. Per-content-type tier definitions

### 5.1 Agent canonical (`00_Prompts/BDOS/agents/<name>.md`)

```yaml
name: <agent>                 # not "title"
version: <semver>
description: <required>
status: active
schema: bdos.agent.canonical.v1   # NEW Phase 4
id: <uuid>                    # NEW Phase 4
index_schema_version: 1       # NEW Phase 4
bdos_index: true              # NEW Phase 4 (explicit)
```

### 5.2 Sage thought (`02_Areas/Personal Growth/Ideas/thoughts/*.md`)

```yaml
schema: sage.thought.v1       # existing
title: <required>
description: <required>       # Phase 3.1 mandate
date: <required>
status: new|reviewed|archived
category: <required>
distribution_hints: [<list>]
source_chat_title: <string>
source_chat_url: <url>
atomic_links: [<wikilinks>]
id: <uuid>                    # NEW Phase 4
index_schema_version: 1       # NEW Phase 4
```

### 5.3 Operational log (`agents/*/logs/operational/<YYYY-MM>.md`)

```yaml
schema: bdos.operational.log.v1
agent: <agent>
month: <YYYY-MM>
bdos_index: false             # logs not user-searchable — Maestro observe queries them directly
id: <uuid>
index_schema_version: 1
```

### 5.4 Daily note (`05_DailyNotes/<YYYY/MM/YYYY-MM-DD>.md`)

```yaml
title: <date>
date: <YYYY-MM-DD>
status: active
bdos_index: true              # important — daily notes are searchable
# id: <uuid>                  # optional — daily notes are path-stable
```

---

## 6. Schema migration (Phase 4.B preview)

When schema evolves (v1 → v2):

1. **Detection:** Librarian audit scans `index_schema_version` per file. Anything < current → `needs_reindex`.
2. **Migration script:** per-major-bump migration script in `capabilities/vault-indexing/migrations/v1_to_v2.py`
3. **Dry-run default:** every migration runs with `--apply` flag to actually write
4. **Rollback path:** every migration logs what it changed; rollback script can revert

---

## 7. Reserved fields (Librarian-only, NEVER edit manually)

| Field | Owner | Updated by |
|---|---|---|
| `_index_health` | Librarian | Indexing cycle |
| `_indexed_at` | Librarian | Indexing cycle |
| `_index_keywords` | Librarian | Phase 4.C semantic enrich |
| `_index_entities` | Librarian | Phase 4.C semantic enrich |
| `_lineage` | Librarian | When file split/merged |

Users / agents may inspect these, but **never edit**. Editing breaks consistency.

---

## 8. Anti-patterns

**❌ Path as primary identity** — phase 4 explicitly forbids.
**❌ Frontmatter as place to dump random fields** — Tier 2 lists allowed fields. Unknown fields preserved but warned by audit.
**❌ Multi-line description with newlines** — keep description 1-2 lines, no `>` block scalars.
**❌ Description-less files** — Phase 3.1 invariant. New files MUST have description.

---

## 9. Migration plan (Phase 4.A initial run)

**File counts:**
- ~3295 total `.md` files in vault
- ~1300 have frontmatter currently
- Of those: 256 have description, ~50 have schema field

**Phased migration order:**
1. **BDOS-system files** (~50) — agent canonicals, capability docs, logs — add UUID + index_schema_version + bdos_index
2. **Sage outputs** (~5 currently) — same
3. **Active 02_Areas/ frontmattered files** (~500) — UUID + index_schema_version
4. **02_Areas/ unfrontmattered files** (~1700) — SKIP for now (no frontmatter to migrate; would need full frontmatter creation, that's bigger Phase 4.B work)
5. **DailyNotes** (~800) — UUID optional; path-stable historically

Phase 4.A migration script: `migrate_uuid.py` with `--apply` gate. Dry-run by default.

---

## 10. Hivatkozott dokumentumok

- BDOS belépő: [`CLAUDE.md`](CLAUDE.md)
- Phase 4 alkotmány: [`CONSTITUTION_PHASE_4.md`](CONSTITUTION_PHASE_4.md)
- Log schemas (Phase 2): [`LOG_SCHEMAS.md`](LOG_SCHEMAS.md)
- Vault-indexing capability: [`capabilities/vault-indexing/CLAUDE.md`](capabilities/vault-indexing/CLAUDE.md)
- Librarian canonical (v0.8): [`agents/librarian.md`](agents/librarian.md)
