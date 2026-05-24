---
title: 00_INTEGRATE_PROPOSALS
generated_by: librarian v0.4
generated_at: 2026-05-11T00:00:00
mode: integrate
external_scope: /Users/becze-mac/Downloads/Work/IgnisAcedemy
file_count_total: 4
file_count_md_txt: 0
file_count_other: 4
breakdown:
  pdf: 2
  srt: 2
privacy_filter_triggered: false
notes: |
  Source folder spelled "IgnisAcedemy" (likely typo for "Academy"). No nested .git, node_modules, .app, or other privacy-sensitive paths. .DS_Store ignored. No md/txt files; PDFs not text-extractable (pdftotext/poppler not installed) — proposals based on filename + folder + mtime metadata only (content_inspected: false for PDFs). SRT files inspected (first 15 lines): confirmed YC Startup School transcripts.
id: c5a86739-a87e-4ed8-892e-165258141d02
index_schema_version: 1
---

# Integrate Proposals — IgnisAcedemy external scope

## Summary

- **Files scanned:** 4 (plus 1 .DS_Store ignored)
- **Breakdown:** 2 PDFs, 2 SRT files
- **Md/Txt count:** 0 (v0.4 default type filter would skip everything; included per user instruction to surface pályázat artifacts)
- **Topic clusters:**
  1. **EU/Romanian pályázat artifact** (`Pályázat/DECIZIE_APROBARE_PROPUNERE_APROBARE_2025-11-06_12-11-47.pdf`, ~4.4 MB, mtime 2025-12-03) — Romanian "approval decision" document, dated 2025-11-06. Strong candidate for the ExarLabs ~275k EUR / 24 hónap pályázat referenced in vault strategy. Could equally belong to a project under Ignis/Ignis Academy if that's what the funding targets.
  2. **YC Startup School transcripts** (`YC/*.srt`, 25 KB + 49 KB, mtime 2025-11-09) — auto-generated subtitles for "B2B Startup Metrics" and "Should Your Startup Bootstrap or Raise Venture Capital". Clean fit for `02_Areas/Ignis Academy/Startup Learning/` (which already contains `BMC upgrade based on YCombinator.md`, `Learning.md`).
  3. **Unknown technical PDF** `HB067WP15.pdf` (~525 KB, mtime 2025-09-05) — filename pattern resembles a Horizon / EU work-package code (HB067 WP15) but unverified. Could be related to pályázat (work-package document) or unrelated research.

Folder naming "IgnisAcedemy" + presence of both Pályázat and YC subfolders suggests the user is collecting **Ignis Academy related** material AND a separate **pályázat** in the same staging folder. Most likely interpretation: the pályázat is what funds (or relates to) Ignis Academy — but this should be confirmed (see Open Questions).

---

## High-confidence proposals (H)

| src | suggested_dst | topic | mtime | size | action |
|---|---|---|---|---|---|
| `/Users/becze-mac/Downloads/Work/IgnisAcedemy/YC/B2B Startup Metrics Startup School [English (auto-generated)] [DownloadYoutubeSubtitles.com].srt` | `02_Areas/Ignis Academy/Startup Learning/transcripts/B2B Startup Metrics — YC Startup School.srt` | YC Startup School — clean match to existing Startup Learning subfolder (already references YCombinator) | 2025-11-09 | 49 KB | import (file copy only; consider rename to drop the "[DownloadYoutubeSubtitles.com]" tag) |
| `/Users/becze-mac/Downloads/Work/IgnisAcedemy/YC/Should Your Startup Bootstrap or Raise Venture Capital  [English (auto-generated)] [DownloadYoutubeSubtitles.com].srt` | `02_Areas/Ignis Academy/Startup Learning/transcripts/Bootstrap or Raise VC — YC Startup School.srt` | YC Startup School — same fit as above | 2025-11-09 | 25 KB | import (file copy only; rename suggested) |

---

## Medium-confidence proposals (M)

| src | suggested_dst | topic | mtime | size | action |
|---|---|---|---|---|---|
| `/Users/becze-mac/Downloads/Work/IgnisAcedemy/Pályázat/DECIZIE_APROBARE_PROPUNERE_APROBARE_2025-11-06_12-11-47.pdf` | **Primary candidate:** `02_Areas/ExarLabs/Stratégia/pályázat/DECIZIE_APROBARE_2025-11-06.pdf` — **Alternative:** `02_Areas/Pályázat/DECIZIE_APROBARE_2025-11-06.pdf` or `02_Areas/Ignis Academy/Pályázat/...` | Romanian "approval decision" — pályázat artifact. Existing vault `Pályázat/` unit is sparse (1 file, `Szövetségesek.md`); ExarLabs has `Stratégia/` with pályázat reference (~275k EUR). Most plausible: ExarLabs/Ignis Academy as funding target. Confidence M because we cannot read PDF content. | 2025-12-03 | 4.4 MB | import_as_resource (file copy only; content_inspected: false) — **needs user confirmation of which unit owns this pályázat** |

---

## Low-confidence / review needed (L)

| src | suggested_dst | topic | mtime | size | action |
|---|---|---|---|---|---|
| `/Users/becze-mac/Downloads/Work/IgnisAcedemy/HB067WP15.pdf` | **Candidate A:** `02_Areas/Ignis Academy/Research/HB067WP15.pdf` — **Candidate B:** `02_Areas/Pályázat/HB067WP15.pdf` — **Candidate C:** `03_Resources/papers/HB067WP15.pdf` | Filename `HB067WP15` resembles a code (possibly Horizon project / work-package, or a paper code). Mtime 2025-09 (older than the others). Could be reference material for either the pályázat or Ignis Academy research. Cannot infer topic without reading content. | 2025-09-05 | 525 KB | review — ask user what HB067WP15 refers to before deciding destination |

---

## Skip recommendations

None. All 4 files are plausibly vault-relevant. `.DS_Store` ignored automatically (not listed).

---

## Open questions for user

1. **Pályázat ownership:** Is `DECIZIE_APROBARE_PROPUNERE_APROBARE_2025-11-06` the **ExarLabs ~275k EUR / 24 hónap** pályázat referenced in ExarLabs Stratégia? Or is it specifically for **Ignis Academy** (which would explain why both Pályázat and YC content sit in a folder named "IgnisAcedemy")? The destination depends on this answer.
2. **Folder name "IgnisAcedemy":** typo for "Academy"? If yes, is this staging folder the working area for Ignis Academy material? Should YC transcripts under `02_Areas/Ignis Academy/Startup Learning/` get a new `transcripts/` subfolder, or live flat?
3. **HB067WP15.pdf:** what is this? (Filename code only — could be Horizon project document, EU work-package, academic paper, internal code.) Without poppler/pdftotext installed I cannot inspect the content. Two options:
   - User tells me what it is → exact destination decided.
   - Install `brew install poppler` and re-run librarian in integrate mode with PDF inspection enabled (would benefit any future PDF triage too).
4. **Ignis Academy vs Ignis:** vault has both `02_Areas/Ignis/` and `02_Areas/Ignis Academy/`. GAP G3 in `02_Areas/Ignis/00_GAPS.md` flags the relationship as unclear. YC startup content here clearly belongs to **Ignis Academy** (its `Startup Learning/` subfolder is the obvious home), but please confirm before importing.

---

## Recommended next action

1. **Approve H-confidence batch first** — the 2 YC SRT files are clear imports to `02_Areas/Ignis Academy/Startup Learning/transcripts/`. Low risk, no ambiguity.
2. **Answer Open Question #1** (pályázat ownership) → then approve M-confidence proposal for the Decizie PDF.
3. **Answer Open Question #3** (HB067WP15) → either user tells me what it is, or install poppler so I can inspect. Then re-classify as H or skip.
4. After approval, hand off to **tidy mode** (or manual `cp`) to perform the actual file moves. Per librarian v0.4 §4.5, integrate mode itself never moves files. Source path `/Users/becze-mac/Downloads/Work/IgnisAcedemy` remains read-only and untouched.

*Note: PDFs were NOT inspected at content level (pdftotext/poppler unavailable). All PDF placements are based on filename + folder name + mtime only. SRTs were content-sampled (first ~15 lines) and confirmed as YC Startup School transcripts.*
