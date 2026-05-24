---
title: 00_OPEN_QUESTIONS
generated_by: librarian v0.3
generated_at: 2026-05-11
scope: global
mode: index
file_count: 1608
id: 7ad32128-dc15-4397-96ba-2ccdf000f213
index_schema_version: 1
---

# Open Questions — global (tier-1)

> **Cross-domain layer.** Unit-scoped open questions live in tier-2 indexes (linked below). This file lists only **vault-level / cross-domain** open questions — items that touch BDOS, conventions, or more than one unit.

---

## Tier-2 drill-down

For per-section open-question listings inside a unit, open its scoped `00_OPEN_QUESTIONS.md`.

| Tier-2 open-questions index | One-line summary |
|---|---|
| `02_Areas/Deák Húsüzlet/00_OPEN_QUESTIONS.md` | Brainstorm-level open questions across BMC, brand voice, falusi hazhozszallitas, founding 50, pre-launch fears, retention loop, zóna detekció, pricing, partnership, etc. |
| `02_Areas/Navigátor Podcast/00_OPEN_QUESTIONS.md` | Episode-level (EP42 webinar levels), audit Fázis 4a kérdések. |
| `02_Areas/Sonrisa/00_OPEN_QUESTIONS.md` | CPS AI-platform comparison, sales strategy, copilot vs n8n, Oracle partnership, Units koncepció. |
| `03_Resources/00_OPEN_QUESTIONS.md` | Reading/research-layer questions (mostly atomic-notes follow-ups). |
| `04_Archive/00_OPEN_QUESTIONS.md` | Historical — kept for traceability; not actionable. |

---

## Vault-level open questions (cross-domain)

These items do not belong to any single unit.

### Vault structure / conventions

- **Personal Growth typo:** keep as-is, or rename to `Personal Growth`? Touches ~31 files of internal links. (See `00_GAPS.md`.)
- **`Szervezet fejlesztés` consolidation:** merge `01_Projects/Szervezet fejlesztés/` into `02_Areas/Szervezet Fejlesztés/`, or keep separate (project-side vs area-side)?
- **`01_Projects/` policy:** with only 1 residual unit, should `01_Projects/` be eliminated entirely and folded into `02_Areas/`? Or kept as a deliberate near-empty placeholder per Areas-dominant PARA?
- **`02_Areas/Pályázat/`:** stub (1 file). Merge with DH or ExarLabs grant material, or keep as standalone scaffold?
- **`02_Areas/Ignis/` orientation:** no top-level CLAUDE.md or README at the unit root (only inside `AI Kurzus/`). Should it get one?

### BDOS / agent system

- **Agent backlog priorities:** Librarian v0.3 backlog (§9 of canonical) lists incremental refresh, broken-link auto-fix, semantic retrieve (embeddings), backlink extraction, tag taxonomy, etc. Order / priority not yet decided.
- **Hierarchical agent rollout:** when does the flat agent model elevate to Domain Managers (Knowledge / Product / Operations / etc.)? Trigger threshold per `CLAUDE.md` §7 = "3+ worker agents per domain". Not yet decided which domain hits this first.
- **Other agents to spawn next:** product strategist, operations steward, exploration agent, validator, curator — none active yet (`00_AGENTS_INDEX.md` lists them as "Planned").

### Cross-unit content ownership

- **DH 24-month roadmap:** DH version vs ExarLabs version — which is canonical? (Also in `00_DECISIONS_INDEX.md`.)
- **`brainstorm_copilot-studio-vs-n8n.md` duplicate:** the Sonrisa/CPS pair (`MelindaSteel/brainstorm/` and `MelindaSteel/n8n Part 2/brainstorm/`). Decide canonical location.

### Vault hygiene

- **Empty root files** (`Untitled.md`, `Navigator reggeli email osszefoglalas.md`) — delete or fill?
- **`02_Areas/Main TODO.md`** (0 bytes, Oct 2025) — delete?
- **Templates `.bak` files** — when can the daily-note template be considered stable enough to delete the backups?

---

## TODO marker scan (counts only)

Globally **~321 markdown files** contain a `TODO:` marker (per 2026-05-10 scan). Tier-2 indexes own these listings per unit. Hot-spots:

- `02_Areas/Deák Húsüzlet/` — largest concentration.
- `02_Areas/Navigátor Podcast/` — episode-level synthesis TODOs.
- `02_Areas/Sonrisa/CPS/` — account-level TODOs.

---

## Coverage notes

- Per-unit (tier-2) open-question indexes are the authoritative source for unit-scoped questions. This file is intentionally short.
- Per-bullet open-question content is intentionally NOT extracted globally — that produces hundreds of items and is the job of tier-2 indexes.
- `Templates/Daily_Note_Template.md` reflection prompts are templated content, not real open questions.
