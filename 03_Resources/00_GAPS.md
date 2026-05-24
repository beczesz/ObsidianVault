---
title: 00_GAPS
generated_by: librarian v0.3
generated_at: 2026-05-11
scope: /03_Resources/
mode: index
file_count: 73
id: 81d527f6-f38a-4a47-a746-e41aaf75ba8e
index_schema_version: 1
---

# Gaps, Inconsistencies, and Orphans — Resources

Read-only index run. No actions taken. Items flagged for a future `tidy` or `audit` mode run.

## 1. Duplicate / triplicate files

### Building a StoryBrand — three locations
- `02_Books/Building_a_StoryBrand_Donald_Miller_2017.md` — at Books root (appears empty / no frontmatter visible on first 15 lines)
- `02_Books/Building a Story Brand/Building_a_StoryBrand_Donald_Miller_2017.md` — in named subfolder (full content)
- `02_Books/Summaries/Building_a_StoryBrand_Donald_Miller_2017.md` — in legacy Summaries folder (full content, near-identical to above)

Action candidate (tidy): md5-compare the two non-empty copies; if byte-identical, delete one. Resolve which root is canonical.

### `Dignity_in_Defeat` atomic note — two locations
- `02_Books/Ernest Hemingway - The Old Man and the Sea/Atomic_Ideas/Dignity_in_Defeat.md`
- `02_Books/Anthony Weston - A Rulebook for Arguments/Atomic_Ideas/Dignity_in_Defeat.md`

Same concept name, two source books. Likely two **different** notes (each book's own framing) — NOT a duplicate to delete. Worth verifying. Could justify a cross-link or shared global atomic.

## 2. Frontmatter inconsistencies

### Heterogeneous schemas
Observed frontmatter shapes across files:
- Modern shape (most recent — Speed-Reader v0.2+): `title`, `type`, `author`, `year`, `source_url`, `file_refs`, `tags`, `status`, `confidence`, `created`, `processed_by`
- Older shape: `title`, `author`, `year`, `completed`, `tags`, `source`, `status` (no `type`, no `confidence`, no `processed_by`)
- Some files have `authors:` (array) instead of `author:` (e.g., Peterson/Pageau/Harrington podcast)
- Atomic / Contrast notes use a leaner shape: `title`, `type: atomic|contrast`, `tags`, `status`, `confidence`, `created`, `processed_by`

### Missing or malformed frontmatter
- `02_Books/Building_a_StoryBrand_Donald_Miller_2017.md` (root) — no frontmatter (file appears near-empty).
- `02_Books/Anthony Weston - A Rulebook for Arguments/A_Rulebook_for_Arguments_Anthony_Weston_1986.md` — opens with `SAVE-TO:` directive block BEFORE the YAML frontmatter (typical for several speed-reader outputs).
- `02_Books/Robert Lewis - Raising a Modern-Day Knight/Raising_a_Modern_Day_Knight_Robert_Lewis_1997.md` — same pattern (`SAVE-TO:` then `---`).
- `02_Books/Ernest Hemingway - The Old Man and the Sea/The_Old_Man_and_the_Sea_Ernest_Hemingway_1952.md` — same `SAVE-TO:` prefix.
- `02_Books/Andy Grove - High Output Management/High_Output_Management_Andy_Grove_1983.md` — same.
- `02_Books/Robert Greene - The 48 Laws of Power/The_48_Laws_of_Power_Robert_Greene_1998.md` — same.
- `02_Books/Tiago Forte - Building a Second Brain/Building_a_Second_Brain_Tiago_Forte_2022.md` — same.
- `02_Books/Lee Boonstra - Prompt Engineering/Prompt_Engineering_Lee_Boonstra_2024.md` — same.
- `02_Books/Matthieu Pageau - The Language of Creation/*.md` (3 variants) — same.
- `04_Articles/Erzsebet Dani - The HY-DE Model/HY_DE_Model_Erzsebet_Dani_2015.md` — `SAVE-TO:` prefix then frontmatter.

These `SAVE-TO:` blocks are residual instruction artifacts from the speed-reader generator. They confuse YAML parsers/dataview and obscure the frontmatter. Tidy candidate: strip them on a follow-up pass.

### Files missing frontmatter entirely
- `02_Books/Robert Greene - The 48 Laws of Power/Personal Notes.md`
- `02_Books/Robert Greene - The 48 Laws of Power/Personal Notes - 48 Laws.md`
- `02_Books/Robert Lewis - Raising a Modern-Day Knight/Knight - Personal notes.md`
- `02_Books/Újvári András - Az isteni axióma/Jegyzetek - Szabolcs.md`
- `04_Articles/Erzsebet Dani - The HY-DE Model/Personal Notes - Ideas.md`
- `04_Articles/ARC - Jonathan Pageau - Jordan Peterson/Summary.md`
- `02_Books/TO READ.md` (one-line file)
- `02_Books/TASKS.md` (has structure but no YAML)

### Inconsistent `status` vocabulary
Observed status values: `done`, `processed`, `triaged`, `deep-read`. No canonical taxonomy. Audit candidate.

### Inconsistent `tag` style
- Hyphenated vs. word-break: `self‑discipline` (non-breaking hyphen, U+2011) vs `self-discipline`
- camel-case-ish: `JerzyKosinski`, `festettmadár`
- spaces: `personal knowledge management`, `Christian leadership`
- Mixed languages within tag list

## 3. Structural inconsistencies

### Podcast atomic ideas placed under Books
Three notes physically under `02_Books/Atomic_Ideas/` were created from the **Dwarkesh / Amodei podcast** (not a book):
- `End_of_the_Exponential.md`
- `Big_Blob_of_Compute_Hypothesis.md`
- `Capability_vs_Product_Gap.md`

Same applies to:
- `02_Books/Contrasts/Amodei_vs_Sutton_on_Learning_Algorithms.md`
- `02_Books/Contrasts/Amodei_vs_LeCun_on_Scaling.md`

The Amodei podcast file's own `SAVE-TO` block specifies `/03_Podcasts/Atomic_Ideas/` etc. — but the actual files were written under `02_Books/`. There's a 4th planned file (`Country_of_Geniuses_in_a_Datacenter.md`) listed in the SAVE-TO block that does **not** appear to exist on disk — verify.

Similarly: `03_Podcasts/Steven Bartlett - Godfather of AI .../...md` lists `/03_Podcasts/Atomic_Ideas/AI_Existential_Risk.md`, `AI_Regulation_Challenges.md`, `AI_and_Cybersecurity.md`, `AI_and_Job_Displacement.md` in its SAVE-TO block — none of these were found on disk.

The Yampolskiy podcast file lists ~8 atomic ideas + 3 contrasts in its SAVE-TO block — none were found on disk.

### Empty directory
- `05_References/` — empty, purpose unclear.

### Naming variants for same book
- `02_Books/Building a Story Brand/` (folder with space, no author prefix) vs. convention `<Author> - <Title>/` used elsewhere.

## 4. Orphan files (no clear link in or out)

(Soft heuristic — not exhaustive without backlink graph.)
- `Utils/Admonition Cheatsheet.md` — utility file, no inbound links from the rest of Resources. Probably fine.
- `02_Books/Jordan_Peterson_100_Books.md` — reading list at root; no per-book entries link back to it.

## 5. Planned-but-missing files

Files referenced in SAVE-TO blocks of generated summaries but not found on disk:

From Amodei podcast:
- `02_Books/Atomic_Ideas/Country_of_Geniuses_in_a_Datacenter.md` — missing

From Hinton podcast (`Godfather_of_AI_Geoffrey_Hinton_Podcast_Summary.md`):
- `03_Podcasts/Atomic_Ideas/AI_Existential_Risk.md`
- `03_Podcasts/Atomic_Ideas/AI_Regulation_Challenges.md`
- `03_Podcasts/Atomic_Ideas/AI_and_Cybersecurity.md`
- `03_Podcasts/Atomic_Ideas/AI_and_Job_Displacement.md`
- `03_Podcasts/Contrasts/Godfather_of_AI_vs_Superintelligence.md`

From Yampolskiy podcast:
- `03_Podcasts/Atomic_Ideas/AGI_Timeline_2027.md`
- `03_Podcasts/Atomic_Ideas/Unemployment_99_Percent.md`
- `03_Podcasts/Atomic_Ideas/Human_Preference_Jobs.md`
- `03_Podcasts/Atomic_Ideas/AI_Safety_Control_Problem.md`
- `03_Podcasts/Atomic_Ideas/No_Plan_B.md`
- `03_Podcasts/Atomic_Ideas/Profit_vs_Ethics_in_AI.md`
- `03_Podcasts/Atomic_Ideas/Wealth_Abundance_vs_Meaning_Crisis.md`
- `03_Podcasts/Atomic_Ideas/Simulation_Hypothesis_Warning.md`
- `03_Podcasts/Contrasts/Yampolskiy_vs_Geoffrey_Hinton.md`
- `03_Podcasts/Contrasts/Yampolskiy_vs_Kai_Fu_Lee.md`
- `03_Podcasts/Contrasts/Yampolskiy_vs_Max_Tegmark.md`

These represent **planned atomic-idea / contrast extractions that were never executed** — possibly the largest single content gap in Resources.

## 6. Stale / outdated risk

No explicit `last_reviewed` field exists. `created` and `completed` dates are present in many files. No file appears actively stale; the oldest content is the source material (1952 Hemingway etc.), not the summaries.

## Librarian action log

| Timestamp | Action | Target | Reason |
|---|---|---|---|
| 2026-05-11 | index (read-only) | `/03_Resources/` | Bootstrap scoped index run, 5 output files generated |

No modifying actions were taken in this run.
