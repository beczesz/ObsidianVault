---
title: 00_GAPS
generated_by: librarian v0.3
generated_at: 2026-05-11T00:00:00
scope: /02_Areas/Personal Growth/
mode: index
file_count: 31
id: 73154bc2-91b4-4983-8a75-f424b313f989
index_schema_version: 1
---

# 00_GAPS — Personal Growth

## Naming inconsistencies

> **PROMINENT FLAG — folder name typo**
>
> The scope folder is named **`Personal Growth`** (missing the **`t`** in "Growth"). This is a top-level Area folder used by Claude MOC, dashboards, and external references. The misspelling is canonical inside `PKM/Claude/Claude MOC.md:38` (`PKM helye: Personal Growth/PKM`), so any rename must update that reference too.
>
> **Recommendation:** rename `Personal Growth/` → `Personal Growth/` via a future **tidy mode** run. Update at minimum:
> - `PKM/Claude/Claude MOC.md` line referencing the path
> - Any backlinks from outside this scope (Librarian must verify in a global retrieve before renaming)
> - Dashboard Dataview queries (currently target `05_DailyNotes`, not affected, but verify)

## Empty / stub files

- `Habits.md` — 0 bytes
- `Habits 1.md` — 0 bytes
- `Habits 2.md` — 0 bytes
- `Habits 3.md` — 0 bytes
- `Movies/TASKS.md` — only section headers, no content
- `Movies/memory/context/` — empty directory

**Likely cause for `Habits.md` + `Habits 1..3.md`:** Obsidian sync conflict copies or accidental creations. The real content lives in `Habits/` (folder). Candidate for tidy-mode deletion.

## Backup files

- 6× `Personal Areas.md.bak.*` files (timestamps 1778122363..1778123264, dated 2025-05-07). These are auto-snapshot backups of a single editing session. Safe to archive or delete in tidy mode if user confirms.

## Broken / unresolved links

From `PKM/Claude/Claude MOC.md:10-11`:
- `[[Prompt Tippek]]` — no target file in scope
- `[[Cowork Munkamenet Sablonok]]` — no target file in scope

## Potential duplicates (NOT byte-identical — do NOT auto-merge)

- `Spiritual/Domb utca/Prophecy.md` vs. `Prophecy v2.md` — v2 is an evolution (adds $36k ask + payment table). Keep both, but consider archiving v1.
- `Spiritual/Domb utca/Prófécia.md` (HU) vs. `Prophecy.md`/`Prophecy v2.md` (EN) — language variants, both valid.
- Two reading-related habits: `Habits/#5 📖.md` and `Habits/#7 📚.md` — same theme, may be intentional (e.g. spiritual reading vs. general reading) but confirm.

## Missing frontmatter

Most root-level files (`Personal Areas.md`, `Personal Dashboard.md`, `Reggeli rutin.md`, `Claude Cowork.md`, `Személyes Napló.md`, `Édesapámról emlékek.md`, `Ideas/Gondolatok.md`, `Spiritual/*` files, `Movies/CLAUDE.md`, `Movies/TASKS.md`, `PKM/*.md`) have **no YAML frontmatter**. Only `Habits/#1..#7` use frontmatter (date-list entries).

Recommendation: standardize a minimal frontmatter (`type`, `status`, `updated`) via tidy mode or a dedicated frontmatter-normalize pass.

## Cross-area leakage

- `Ideas/Gondolatok.md` contains a long Deák Húsüzlet (DHOP) business-strategic entry (2026-04-11). This is content that arguably belongs in `02_Areas/Deák Húsüzlet/` rather than Personal Growth. Flag — no auto-move (tidy mode constraint: folder reorganization forbidden).

## Out-of-scope dependencies

- Both dashboard files (`Personal Areas.md`, `Personal Dashboard.md`) depend on `05_DailyNotes/` (Dataview source). If the daily-notes folder is moved or renamed, both dashboards silently break.

## Librarian action log

- **2026-05-11** — generated 5 tier-2 index files for scope `Personal Growth/` (mode: index, v0.3). No content modified. No files moved or deleted.
