---
title: "CPS Monthly Process v0.1"
date: 2026-04-21
author: Becze Szabolcs
status: active
description: "Szabolcs's monthly administrative workflow for CPS spanning three phases: Phase 1 processes raw timesheets in Cowork to produce base file, TAM report, and structured Monthly Update Brief; Phase 2 uses Claude for Excel with a skill to update the CPS dashboard project-by-project; Phase 3 cross-references contractor TIG documents for Account Manager verification emails."
description_source: auto
description_hash: 74854c15f0191487
id: 0e09788a-a6c9-465c-a81f-fa5996694b2f
index_schema_version: 1
bdos_index: true
---
# CPS Monthly Process v0.1

**Owner:** Szabolcs
**Frequency:** Monthly, after Sontime period closes
**Last updated:** 2026-04-21
**Status:** This is the single source of truth. Skills and plugins are derived from this document.

---

## Overview

The monthly CPS administration has three phases. Phase 1 runs entirely in Cowork and produces three outputs. Phase 2 runs in Claude for Excel using the MUB + the dashboard update skill. Phase 3 runs in Cowork for contractor verification.

```
Phase 1 (Cowork)              Phase 2 (Claude for Excel)       Phase 3 (Cowork)
================              =========================        ================
Raw Timesheet                 MUB + Dashboard                  TIG + _base
    |                              |                                |
    v                              v                                v
_base.xlsx (internal)         Skill reads MUB                  Cross-reference
_tam.xlsx  (for TAMs)         Updates project by project       Draft AM emails
MUB.md     (for Phase 2)     ACK loop per project             Gmail drafts
```

---

## Phase 1: Statistics Processing

**Tool:** Cowork + `cps-statistics-v0.1` skill
**Input:** Raw Sontime activity report (`activityreport_YYYY_MM (N).xlsx`)
**Outputs:**
1. `activityreport_YYYY_MM_base.xlsx` -- full workbook with raw data + pivot tables (internal)
2. `activityreport_YYYY_MM_tam.xlsx` -- CPS-only extract for Technical Account Managers
3. Monthly Update Brief (`MUB_YYYY_MM.md`) -- structured project-by-project data for Phase 2

### Steps

1. Download the raw activity report from Sontime/SharePoint
2. Say **"process timesheets"** in Cowork and provide the file
3. Cowork copies the example sheet template and replaces the data with the new raw timesheet
4. Cowork parses data, builds pivot tables, generates `_base.xlsx` and `_tam.xlsx`
5. Cowork reads the pivot table and converts it to structured text: the Monthly Update Brief (MUB)
   - One block per project with person, E-level, emp status, hours, daily rate, billing type, discount, fixed
   - Current month data only -- no comparison with previous months
6. Upload `_base.xlsx` to SharePoint (Sales > CPS > raports)
7. Upload `_tam.xlsx` to SharePoint (Cloud Guild > Technical > Raport > Raw timesheets)
8. Save MUB as `MUB_YYYY_MM.md` -- ready to attach or paste into Phase 2

### MUB Format

The MUB is a textual representation of the pivot table data. Current month only -- pure data, no analysis. The dashboard skill handles all comparison logic by reading previous months from the open dashboard.

```
# CPS Monthly Update Brief

**Period:** 2026 March (Month 03)
**Generated:** 2026-04-02
**Source:** activityreport_2026_03_base.xlsx
**Total CPS hours:** 1856
**Projects:** 12

---

### Jumio AWS -- Jumio

**Type:** T&M

| Person | E-level | Emp Status | Hours | Daily Rate | Billable | Discount | Fixed |
|--------|---------|------------|-------|------------|----------|----------|-------|
| Kovacs Attila | e6 | Employee | 160 | 310 | Billable | 0 | 0 |
| Peidl Gergely | e7 | Employee | 40 | 571 | Billable | 0 | 0 |
```

The MUB is the DATA. The skill (`sonrisa-cps-dashboard-update`) is the LOGIC that reads this data, compares with the dashboard's existing history, and updates project by project.

---

## Phase 2: Dashboard Update

**Tool:** Claude for Excel + `sonrisa-cps-dashboard-update` skill
**Input:** Monthly Update Brief (MUB) + Dashboard open in Excel Online
**Output:** Updated `CPS - Dashboard - v2.xlsx` (all rows ACK'd, synced to SharePoint)

### How It Works

The `sonrisa-cps-dashboard-update` skill is installed in Claude Settings. It encodes:
- Dashboard structure (which sheets, which columns)
- T&M Raw column mapping (A-AD)
- Formula templates for calculated columns
- State tracking conventions (PREFILLED/ACK/REVIEW/ADJUSTED/SKIP)
- The interaction pattern (announce -> ACK -> write -> verify -> ACK)
- Comparison logic: reads previous months from the dashboard to detect rate changes, new/dropped people, hour anomalies

The MUB provides the current month's raw data. Together: **skill = how to update (+ comparison), MUB = what to update (current month only)**.

### Steps

1. Open `CPS - Dashboard - v2.xlsx` in Excel Online (browser)
2. Open Claude for Excel sidebar
3. Attach the MUB file or paste its content into the chat
4. Claude for Excel reads the skill and understands the dashboard structure
5. For each project in the MUB:
   - Claude announces: "Next: [Project]. Adding [N] rows for [people]. Ready?"
   - ACK
   - Claude writes rows: values in A-Q, formulas in C/N/R-X (copied from row above), Status = PREFILLED in AC
   - Changes visible immediately in the spreadsheet
   - Verify visually, say "ACK"
   - Claude updates Status from PREFILLED to ACK
   - Next project
6. After all T&M Raw projects: update Service Income rows
7. If applicable: Actual PSIC, Planned EDC, CPS Team updates
8. Final verification: check BU Dash1, CPS Dash V2, BU Dash2 for correct totals

### Resumability

The Status column (AC) in T&M Raw tracks progress. If you stop mid-way:
- ACK'd projects = done, skip
- PREFILLED projects = need your review
- No status = not started yet
- REVIEW = needs discussion first

Next session: paste same MUB, Claude reads T&M Raw state and picks up where you left off.

---

## Phase 3: TIG Review

**Tool:** Cowork + `tig-review-v0.1` skill
**Input:** Contractor TIG document (SharePoint) + `_base.xlsx` Sontime data
**Output:** Gmail drafts (AM sign-off requests in Hungarian)

### Steps

1. Say **"review TIG"** in Cowork
2. Cowork navigates to Banfi Istvan's TIG folder on SharePoint
3. Cowork downloads and reads the TIG for the current month
4. Cross-references hours per project with the _base.xlsx Sontime data
5. Identifies the Account Manager for each project
6. Drafts Hungarian sign-off request emails (one per AM, grouped by projects)
7. Creates Gmail drafts with proper CC (Finance + PM)
8. Review drafts and send

---

## Phase 4: (TBD)

*Reserved for additional monthly steps -- invoice verification, review meeting prep, etc.*

---

## State Tracking (T&M Raw columns AC-AD)

| State | Meaning | Who sets it |
|-------|---------|-------------|
| PREFILLED | Claude added rows, not yet reviewed | Claude |
| ACK | Reviewed and confirmed | Szabolcs (via chat) |
| REVIEW | Something unclear, needs discussion | Either |
| ADJUSTED | Was ACK'd then manually corrected | Szabolcs |
| SKIP | Intentionally excluded this month | Szabolcs |

Column AD = Notes (free text context).

---

## Tools & Skills

| Skill | Version | Where it runs | Purpose |
|-------|---------|---------------|---------|
| cps-statistics | v0.1 | Cowork | Phase 1: raw timesheets to _base, _tam, MUB |
| sonrisa-cps-dashboard-update | v0.1 | Claude for Excel | Phase 2: uses MUB to update dashboard |
| tig-review | v0.1 | Cowork | Phase 3: contractor TIG verification |

**Plugin:** `sonrisa-management.plugin` v0.2.0 (bundles all skills for Cowork)
**Standalone skill:** `sonrisa-cps-dashboard-update-v0.1.skill` (for Claude for Excel)

---

## File Locations

| File | Location |
|------|----------|
| Raw activity report | SharePoint: Sales > CPS > raports |
| _base.xlsx | Same (after Phase 1) |
| _tam.xlsx | SharePoint: Cloud Guild > Technical > Raport > Raw timesheets |
| MUB | `CPS\Administration\MUB_YYYY_MM.md` (or attached in chat) |
| Dashboard | SharePoint: Sales > General > Planning > Services > CPS |
| Dashboard (local) | OneDrive synced via "Add shortcut to OneDrive" |
| Plugin source | `00_Prompts\Claude\Plugins\Sonrisa Management Plugin\` |
| Skill file | `00_Prompts\Claude\Skills\sonrisa-cps-dashboard-update-v0.1\` |
| Administration | `CPS\Administration\` |
| Process memory | `CPS\memory\dashboard-update-process.md` |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v0.1 | 2026-04-21 | Initial version. Phase 1-3 documented. MUB as Phase 1 output. |
| v0.1.1 | 2026-04-21 | Simplified MUB: current month data only, skill handles comparison. |
