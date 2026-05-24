---
title: BDOS Constitution — Phase 4 (Librarian as Memory OS)
date: 2026-05-24
author: Becze Szabolcs
status: active
version: 4.0
description: A BDOS negyedik érettségi fázisának konstitucionális dokumentuma. Librarian új szerepe: a BDOS indexing, integrity, and retrieval infrastructure rétege — "memory operating system". Definiálja a continuous indexing architektúrát, frontmatter schema management-et, selective indexing-et, vault integrity auditálást, semantic acceleration-t, és lifecycle awareness-t. Source of truth — minden Phase 4 evolúció innen származik.
tags: [BDOS, constitution, phase-4, librarian, memory-os, indexing, governance]
id: 71553001-be28-4503-b1db-e7d8d5883ab0
index_schema_version: 1
---

# BDOS Constitution — Phase 4
## Memory Operating System Era

> **Ez a dokumentum a BDOS negyedik érettségi fázisának alkotmánya.**
> A user 2026-05-24-én adta a directive-et Librarian-nak.
> Minden Phase 4 evolúció (Librarian v0.8+, vault-indexing capability bővítés, schema management) ennek a dokumentumnak a végrehajtása.

---

## A) Librarian új identitása

Librarian **már nem korlátozott** file-discovery-ra és retrieve-re. Új szerepe:

> Librarian a BDOS **memory operating system**-je — a continuous indexing, integrity, és retrieval infrastructure rétege.

### Új core capabilityk

1. **Continuous file monitoring** — file create/modify/delete/move/rename detection
2. **Metadata indexing layer** — SQLite + JSON cache, millisecond-szintű query
3. **Frontmatter schema management** — `index_schema_version` tracking, safe migration
4. **Selective indexing** — `bdos_index: true|false` per-file vagy folder-szabály alapú
5. **Multi-layer search** — metadata → narrowing → selective load → semantic → synthesis
6. **Vault integrity + auditability** — health states, integrity reports, repair suggestions
7. **Semantic acceleration** — keyword/entity extraction, relationship indexing (NEM embeddings, vagy hibrid)
8. **Vault mutation lifecycle** — file move/rename/split/merge identity continuity
9. **Operational logging** — Phase 2.B logging integráció + new schema-mutation events

### Librarian célja

> Maximum retrieval quality with minimum token expenditure. **Nem hagyományos adatbázis** — kognitív indexing infrastructure.

A BDOS memóriája legyen:
- **searchable in milliseconds**
- **explainable**
- **continuously synchronized with markdown vault**

---

## B) Az alapelv — markdown a forrás

**A markdown fájlok maradnak a forrás-az-igazságra. Az index egy DERIVED acceleration layer.**

Az index mindig:
- **rebuildable** a raw markdown-ból
- **auditable** (minden mutáció logolt)
- **recoverable** (ha a cache elvész, restoreable)

**Anti-pattern (forbidden):** hidden state, opaque database ami a "real source of truth"-tá válik. Ha vault.db törlődik, a vault-nak állnia kell — emberileg olvasható maradnia.

---

## C) 11 system capability — directive verbatim

### 1. Continuous File Monitoring
Mechanisms: file create/modify/delete/move/rename detection + restructuring awareness. Use Watchdog, FS events, hashing, mtime, git, hybrid. **Minimize unnecessary re-indexing** — use cheap deterministic checks before expensive operations.

### 2. Metadata Indexing Layer
SQLite + JSON cache + hybrid OK. Must support: millisecond-level metadata search, filtering, aggregation, relationship discovery, dashboard generation.

Required fields (extendable):
- tags, topics, entities, projects, agents, timestamps, relationships, status, type, lifecycle state, operational metadata

### 3. Frontmatter Schema Management
Formalize BDOS metadata schema. Every indexed file supports:
- stable identity (NOT path-only)
- schema versioning
- searchable metadata
- lifecycle metadata
- retrieval optimization metadata

**`index_schema_version` is mandatory.** When schema evolves:
- Identify outdated files
- Determine which require re-indexing
- Safely migrate metadata structures

Define: required / optional / reserved fields + ownership boundaries.

**Avoid schema chaos.**

### 4. Selective Indexing
Not every file should be indexed. Design mechanisms:
- excluding files/folders/temp notes/generated artifacts/archives/sensitive material
- explicit opt-in / opt-out
- rule-based behavior
- e.g. `bdos_index: true` / `bdos_index: false`

Track: indexed / intentionally ignored / orphaned / stale. **Never drift into indexing ambiguity.**

### 5. Search Architecture
Multi-layer flow:
1. metadata filtering
2. candidate narrowing
3. selective full-file loading
4. semantic reasoning
5. synthesis

**Goal: minimum token usage with maximum retrieval quality.**

Support: deterministic / fuzzy / semantic / relationship-aware retrieval.

### 6. Vault Integrity & Auditability
Detect:
- broken metadata
- missing required fields
- duplicate IDs
- invalid YAML
- stale indexes
- orphaned files
- broken relationships
- outdated schema versions
- indexing inconsistencies

Introduce: index health states + integrity reports + audit logs + repair suggestions.

**Health states:**
- `ok | stale | needs_reindex | broken_frontmatter | duplicate_id | orphaned | missing_required_fields | archived | excluded`

### 7. Semantic Acceleration
Semantic-like retrieval **without** full-vault LLM reasoning. Explore:
- semantic hints
- entity extraction
- keyword enrichment
- relationship indexing
- topic mapping
- retrieval ranking

**Goal:** vault feels semantically searchable, doesn't burn tokens.

Think: **structured cognition acceleration.**

### 8. Vault Mutation & Lifecycle Awareness
Safely support: file move / rename / split / merge / archive / cleanup / restructure / reorganization.

Preserve: identity continuity, relationship continuity, source lineage.

**Do NOT make file path the only identity layer.** Every indexed file has:
- stable identity (separate from path)
- traceable lineage
- recoverable history

### 9. Operational Logging
Every indexing op logged. Track:
- file changes
- re-indexing
- metadata mutations
- schema migrations
- indexing failures
- repair operations
- semantic enrichment ops

Log fields: timestamps, affected files, operation type, token usage, model used (if applicable), rollback info.

Integrates with Phase 2.B 3-stream logs (Operational/Learning/Version).

### 10. Thinking Engine Orchestrator
Authorized for Phase 4 research. May consult Perplexity/ChatGPT/Claude/external sources for: indexing architectures, metadata systems, knowledge graphs, retrieval optimization research.

### 11. Final Objective
Continuously indexed, metadata-aware, semantically accelerated, queryable cognitive memory system. Instant retrieval, organizational reflection, operational analytics, low-token intelligent navigation.

**Not a traditional database. A cognitive indexing infrastructure for BDOS.**

---

## D) Backward compatibility

Phase 4 **NEM törli a Phase 1/2/3-at**:

- Phase 1 invariants (markdown-native, human-centric, flat orchestration) maradnak
- Phase 2.B logging (3 stream) érvényes — Phase 4 új event-típusokkal bővít
- Phase 3 vault-indexing capability megmarad — Phase 4 BŐVÍTI (schema mgmt, integrity, semantic acceleration)
- Cognition/distribution wall érvényben

Phase 4 **kiterjeszti**, nem felülírja.

---

## E) Rollout phasing (javasolt — user-confirmation után véglegesedik)

| Phase | Mi készül | Mikor |
|---|---|---|
| **4.A** | Constitution doc + Librarian v0.8 design + frontmatter schema spec + identity layer decision + selective-indexing default | most |
| **4.B** | Schema migration framework + health-state implementation + integrity audit module | Phase 4.A után |
| **4.C** | Semantic acceleration (keyword/entity extraction, NEM embeddings v0.x-ben) | Phase 4.B után |
| **4.D** | Lifecycle awareness (move/rename identity continuity) | Phase 4.C után |
| **4.E** | Full Thinking Engine integration in retrieve | Optional, Phase 4.D után |

---

## F) Critical design decisions (LOCKED 2026-05-24)

| Kérdés | DÖNTÉS |
|---|---|
| **Identity layer** | **UUID per indexed file** (`id: <uuid4>` frontmatterben). Path-mozgatás, rename, split/merge esetén az ID megmarad — lineage követhető. Migration: ~1300 frontmattered fájl kap UUID-t a `migrate_uuid.py` script-tel (dry-run default). |
| **Selective indexing default** | **Opt-out** (current model). 3295 fájl indexelve, `bdos_index: false` frontmatter mező vagy `.bdosignore` folder marker kivételt biztosít. |
| **Semantic acceleration** | **Keyword + entity extraction (NEM embeddings)** v0.8-ban. TF-IDF keyword + regex/NLP entity detection, SQLite-ba mentve. Embeddings opcionális Phase 4.D+ jövőben. |
| **Librarian verzió target** | **v0.8 incremental**. v0.7 (cache-first retrieve) → v0.8 (Memory OS). v1.0 jelölés a teljes Phase 4 (4.A→4.E) lezárásakor. |

Ezek **konstitucionális döntések** — visszafordításuk drága. Phase 4.A végrehajtás megkezdődött.

---

## G) Hivatkozott dokumentumok

- BDOS belépő: [`CLAUDE.md`](CLAUDE.md)
- Session-bootstrap primer: [`00_BDOS_PRIMER.md`](00_BDOS_PRIMER.md)
- Phase 2 (Reflective Nervous System): [`CONSTITUTION_PHASE_2.md`](CONSTITUTION_PHASE_2.md)
- Log schemas: [`LOG_SCHEMAS.md`](LOG_SCHEMAS.md)
- Vault Indexing capability (Phase 3): [`capabilities/vault-indexing/CLAUDE.md`](capabilities/vault-indexing/CLAUDE.md)
- Librarian canonical (v0.7): [`agents/librarian.md`](agents/librarian.md)
- Librarian research (Phase 3): [`agents/librarian/research/2026-05-24_metadata-indexing-architecture.md`](agents/librarian/research/2026-05-24_metadata-indexing-architecture.md)

---

## H) Záró elv

> **Phase 1:** hogyan építünk stabil agenteket.
> **Phase 2:** hogyan tanul magáról egy szervezet.
> **Phase 3:** hogyan gyorsítjuk a retrieve-et metadata-szinten.
> **Phase 4:** hogyan tesszük a vault-ot **operating system**-mé.

A BDOS érettsége nem új agentek számában mérhető, hanem **abban, mennyire láthatóvá és kereshetővé válik magától.**
