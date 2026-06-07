---
title: "CPS Monthly Process"
date: 2026-04-21
author: Becze Szabolcs
status: active
description: "Monthly workflow for CPS timesheets and billing. Szabolcs runs four phases: statistics processing via Cowork, brief generation and dashboard writing, TIG contractor review, with file uploads to SharePoint and progress tracking via Status column."
description_source: auto
description_hash: 0446466244c041d1
id: 002b1cf7-aa0c-416f-a4da-69665385906a
index_schema_version: 1
bdos_index: true
---
# CPS Monthly Process

**Owner:** Szabolcs
**Frequency:** Monthly, after Sontime period closes
**Last updated:** 2026-04-21

---

## Phase 1: Statistics Processing

**Tool:** Cowork (cps-statistics-v0.1 skill)
**Input:** Raw Sontime activity report (`activityreport_YYYY_MM (N).xlsx`)
**Output:** `_base.xlsx` (internal) + `_tam.xlsx` (for TAMs)

1. Download the raw activity report from Sontime/SharePoint
2. Say "process timesheets" in Cowork and provide the file
3. Cowork processes the export: parses data, builds pivot tables, generates both output files
4. Upload `_base.xlsx` to SharePoint (Sales > CPS > raports)
5. Upload `_tam.xlsx` to SharePoint (Cloud Guild > Technical > Raport > Raw timesheets)

Phase 1 is complete. The `_base.xlsx` feeds Phase 2.

---

## Phase 2a: Brief Generation

**Tool:** Cowork (sonrisa-cps-dashboard-update skill)
**Input:** `_base.xlsx` (Phase 1 output) + previous month's T&M Raw from dashboard
**Output:** Monthly Update Brief (structured markdown)

1. Say "update dashboard" or "Phase 2" in Cowork
2. Cowork reads the _base.xlsx pivot for this month's hours per person per project
3. Cowork reads T&M Raw from the local dashboard copy (OneDrive-synced) for last month's data
4. Cowork compares project by project:
   - Continuing projects: carry forward, flag hour/rate changes
   - New people: look up E-level and rate from historical data, or ask
   - Dropped projects/people: flag for attention
5. Cowork presents the full Monthly Update Brief in chat
6. Review and correct (wrong rate, skip a project, adjust billing type, etc.)
7. Brief is finalized -- copy it for Phase 2b

---

## Phase 2b: Dashboard Writing

**Tool:** Claude for Excel (sonrisa-cps-dashboard-update skill, same skill as 2a)
**Input:** Monthly Update Brief (pasted from Cowork) + open dashboard in Excel Online
**Target:** `CPS - Dashboard - v2.xlsx` on SharePoint

1. Open the dashboard in Excel Online (browser)
2. Open Claude for Excel sidebar
3. Paste the Monthly Update Brief into the chat
4. Claude for Excel processes projects one by one:
   - Announces: "Next: [Project]. Adding [N] rows for [people]. Ready?"
   - Wait for ACK
   - Writes rows: values in A-Q, formulas in C/N/R-X, Status = PREFILLED in AC
   - Changes visible immediately in the spreadsheet
   - Verify visually, say "ACK"
   - Claude updates Status from PREFILLED to ACK
   - Next project
5. After all T&M Raw projects: update Service Income rows
6. If applicable: Actual PSIC, Planned EDC, CPS Team updates
7. Final verification: check BU Dash1, CPS Dash V2, BU Dash2 for correct totals

**Resumability:** The Status column (AC) tracks progress. If you stop mid-way, next session Claude reads T&M Raw, sees which projects are ACK/PREFILLED/not started, and picks up from there.

---

## Phase 3: TIG Review

**Tool:** Cowork (tig-review-v0.1 skill)
**Input:** Contractor's TIG document + Sontime data from _base.xlsx
**Target:** AM sign-off email drafts in Gmail

1. Say "review TIG" in Cowork
2. Cowork navigates to Banfi Istvan's TIG folder on SharePoint
3. Cowork downloads and reads the TIG for the current month
4. Cross-references hours per project with the _base.xlsx Sontime data
5. Identifies the Account Manager for each project
6. Drafts Hungarian sign-off request emails (one per AM, grouped by project)
7. Creates Gmail drafts with proper CC (Finance + PM)
8. Review drafts and send

---

## Phase 4: (TBD)

*Reserved for additional monthly steps -- invoice verification, dashboard review meeting prep, etc.*

---

## State Tracking

T&M Raw columns AC-AD track the dashboard update progress:

| State | Meaning |
|-------|---------|
| PREFILLED | Claude added rows, not yet reviewed |
| ACK | Reviewed and confirmed |
| REVIEW | Needs discussion |
| ADJUSTED | Was ACK'd then manually corrected |
| SKIP | Intentionally excluded this month |

---

## Tools & Skills

| Skill | Where it runs | Purpose |
|-------|---------------|---------|
| cps-statistics-v0.1 | Cowork | Phase 1: raw timesheets to _base/_tam |
| sonrisa-cps-dashboard-update | Cowork + Claude for Excel | Phase 2: brief generation + dashboard writing |
| tig-review-v0.1 | Cowork | Phase 3: contractor TIG verification |

All three skills are bundled in the `sonrisa-management.plugin` (for Cowork).
The dashboard update skill is also available as a standalone `.skill` file (for Claude for Excel).

---

## File Locations

| File | Location |
|------|----------|
| Raw activity report | SharePoint: Sales > CPS > raports |
| _base.xlsx | Same as above (after Phase 1) |
| _tam.xlsx | SharePoint: Cloud Guild > Technical > Raport > Raw timesheets |
| Dashboard | SharePoint: Sales > General > Planning > Services > Cloud Platform Services |
| Dashboard (local) | `C:\Users\...\Sonrisa Kft\sales - Cloud Platform Services\CPS - Dashboard - v2.xlsx` |
| Plugin source | `00_Prompts\Claude\Plugins\Sonrisa Management Plugin\` |
| Skill file | `CPS\Administration\cps-dashboard-update-v0.1.skill` |
| Plugin file | `CPS\Administration\sonrisa-management.plugin` |
| Process memory | `CPS\memory\dashboard-update-process.md` |
