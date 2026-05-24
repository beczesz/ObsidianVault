---
title: 00_DECISIONS_INDEX
generated_by: librarian v0.3
generated_at: 2026-05-11
scope: global
mode: index
file_count: 1608
id: 811d5e04-52a2-489f-8b48-8de69b8b2f1f
index_schema_version: 1
---

# Decisions Index — global (tier-1)

> **Cross-domain layer.** Per-unit decisions live in tier-2 indexes (linked below). This file lists only **vault-level** decisions (BDOS, conventions, cross-domain reorganizations) plus links into tier-2 indexes with a one-line summary each.
>
> The Librarian does NOT summarize decision content — it points to the source.

---

## Tier-2 drill-down

For per-bullet, per-section decision listings inside a unit, open its scoped `00_DECISIONS_INDEX.md`.

| Tier-2 decisions index | One-line summary |
|---|---|
| `02_Areas/Deák Húsüzlet/00_DECISIONS_INDEX.md` | Sprint-level, brainstorm-level, BMC, pricing, retention loop, founding 50, brand voice, partnership decisions — the densest decision cluster in the vault. |
| `02_Areas/Navigátor Podcast/00_DECISIONS_INDEX.md` | Channel audit Fázis 4a decisions, episode metadata standards, plan.md döntésnapló, csatorna-intelligencia. |
| `02_Areas/Sonrisa/00_DECISIONS_INDEX.md` | CPS sales-strategy, AI-platform comparison, copilot-vs-n8n; Oracle partnership; Vision Corner. |
| `03_Resources/00_DECISIONS_INDEX.md` | Reference-layer decisions (mostly speed-reader output choices, atomic/contrast conventions). |
| `04_Archive/00_DECISIONS_INDEX.md` | Historical decisions kept for traceability; not actionable. |

---

## Vault-level decisions (not unit-scoped)

These decisions shape the vault itself or cross multiple units. They do **not** belong to any single tier-2 index.

### Vault conventions / BDOS

| Decision | Where | Date | Note |
|---|---|---|---|
| **Areas-dominant PARA** — Projects nearly empty; "projects" treated as long-running Areas | `CLAUDE.md` §1 (vault root) | 2026-05-11 | Codifies pre-existing practice. |
| **Two-tier indexing** — tier-1 (vault root) + tier-2 (per substantial Area) | `CLAUDE.md` §3 | 2026-05-11 | Locality > completeness in retrieve. |
| **Tier-2 threshold** — ≥ 30 files OR has `01_PROJECT_STATE.md` OR active sprint | `CLAUDE.md` §3 | 2026-05-11 | — |
| **Agent two-file architecture** — canonical (`00_Prompts/BDOS/agents/<name>.md`) + registration (`.claude/agents/<name>.md`), versions synced | `00_Prompts/BDOS/agents/librarian.md` §11; `CLAUDE.md` §2 | 2026-05-11 | Audit mode detects mismatch. |
| **Sprint 3 cadence + caution** — destructive actions need explicit confirmation while sprint active | `CLAUDE.md` §5 | 2026-05-11 | Beta launch ~2026-05-15. |
| **Frontmatter convention** — title/date/author/status/description (+ version when applicable) | `CLAUDE.md` §4 | 2026-05-11 | — |

### Librarian agent evolution

| Decision | Where | Date | Note |
|---|---|---|---|
| **v0.1 → v0.2:** Knowledge Manager reframe; 4 explicit modes (index/retrieve/tidy/audit); context-protection as core principle | `00_Prompts/BDOS/agents/librarian.md` §9 changelog | 2026-05-11 | — |
| **v0.2 → v0.3:** two-tier retrieve algorithm; `03_Resources/` + `04_Archive/` indexable | `00_Prompts/BDOS/agents/librarian.md` §9 | 2026-05-11 | — |

### Cross-domain reorganizations

| Decision | Where | Date | Note |
|---|---|---|---|
| **Sonrisa unification** — `01_Projects/Sonrisa/` removed, merged into `02_Areas/Sonrisa/` | (folder state) | 2026-05-10 → 11 | Only 1 file moved; most material already in Areas. Resolves the 2026-05-10 GAPS flag "Two Sonrisa units". |

### Pending vault-level decisions (cross-domain)

These are open decisions that touch multiple units and so don't fit into any single tier-2 index.

- **DH 24-month roadmap canonical home** — currently mirrored at `02_Areas/Deák Húsüzlet/Business Development/strategy/24-month-roadmap.md` AND `02_Areas/ExarLabs/resources/Deák Platform/24-month-roadmap.md`. Owner: decide DH or ExarLabs. Tracked in `00_GAPS.md`.
- **`Personal Growth` → `Personal Growth`** rename — touches ~31 files. Not yet decided.
- **`Szervezet fejlesztés` consolidation** — Projects-side (lowercase f, 1 active sub-folder) vs Areas-side (uppercase F). Tracked in `00_GAPS.md`.

---

## Coverage notes

- Per-unit (tier-2) decision indexes are the authoritative source for unit-scoped decisions. This file is intentionally short.
- Files containing decision-keyword patterns globally: **151+** (2026-05-10 figure). Tier-2 indexes have already extracted these by unit.
- For comprehensive per-bullet decisions inside a unit, open its tier-2 `00_DECISIONS_INDEX.md`.
