---
title: AM TODAY - CPS Account Management Action Queue
description: "Live action queue for account managers tracking post-sale project deliverables, renewals, kickoffs, and escalations tied to CPS client engagements, with kanban integration and cross-vault task queries."
description_source: auto
description_hash: f3cd798c5a775c3b
last-updated: 2026-05-27
purpose: Single source for what needs action TODAY on the Account Management side. Analog to TODAY.md (which is sales-flavored) but scoped to active project management. Read at every session start when in AM mode, update when work is done.
convention: Tasks use 📅 YYYY-MM-DD as due date. Mark done with [x] + ✅ YYYY-MM-DD done date. Each task links to (a) the project's NOTES.md, (b) any prepared deliverable.
dashboard_contract: Sales/DASHBOARD_CONTRACT.md (same contract, AM dashboard reads this file for its Today panel)
dashboard_note: "Live source for the Today panel in _dashboards/account-management.html. Day headers must include a date: `## Today: YYYY-MM-DD (Weekday)`. Subsection containing 'decisions needed' routes tasks to the Decisions column. Bold **ProjectName** in a task links it to the kanban card in PROJECTS.md. Date marker here is the 📅 emoji, NOT @{} (that is PROJECTS.md syntax)."
id: d6eb3e7b-f20f-4c29-a717-bcd0e64c6226
index_schema_version: 1
---
<!--
  ===========================================================================
  LIVE DATA SOURCE for the AM dashboard's Today panel.
  ===========================================================================
  Same conventions as TODAY.md (which serves the Sales dashboard).
  Difference: scope is post-Won project management, not sales outreach.

  DAY SECTION HEADER FORMAT (the date is REQUIRED, parser uses it to match):
      ## Today: 2026-05-27 (Wednesday)
      ## Tomorrow: 2026-05-28 (Thursday)
      ## Friday: 2026-05-30     <-- weekday + date also works

  Dashboard picks the section whose date matches the current system date,
  falls back to the next future date.

  TASK FORMAT:
      - [ ] **ProjectName** Free text 📅 2026-05-27 #tag [[wiki-link]]
  - Bold **ProjectName** links the task to a kanban card in PROJECTS.md.
  - Date marker in THIS file is 📅. PROJECTS.md uses @{}, do NOT swap.
  - Tag chip priority: #renewal, #kickoff, #escalation, #review, #upsell,
    #discovery-call, #milestone, #post-call. First recognized wins.

  Relationship to Sales TODAY.md:
  - Sales TODAY.md = outbound lead actions, follow-up nudges, scrape tasks
  - AM TODAY.md (THIS FILE) = project management actions, renewal preps,
    kickoffs, escalations, client reviews, upsell prep, post-call follow-ups
  ===========================================================================
-->

# AM TODAY - CPS Account Management Action Queue

> **AM Engine started:** 2026-05-27. First Backlog entry: Merkantil (multi-workstream engagement, CPS Discovery call held same day).

## Today: 2026-05-27 (Wednesday)

### Post-call follow-up

- [ ] **Merkantil Bank Zrt.** Discovery call held 12:00. User to send post-call info; once received, decide AM stage (Backlog → Initial meeting → Define need progression), formalize CPS infra scope in writing, share number with Miklós Nándor for offer dispatch. -> [[Accounts/Leads/Merkantil/NOTES]] 📅 2026-05-27 #post-call #urgent

### Active project review (Delivery cohort)

- [ ] **MVMI — Azure DevOps Managed Service** Verify kickoff status. The MVMI top-level NOTES flags "needs to start ASAP" — confirm whether engagement is truly in Delivery or still pre-kickoff (Contracted). If pre-kickoff, move card to Contracted in PROJECTS.md and schedule kickoff with Kardos Sanyi. -> [[Accounts/Active/MVMI/AzureDevOps Managed Service/NOTES]] 📅 2026-05-28 #kickoff #review
- [ ] **MVMI — Chaos Engineering Workshop** Verify stage. Sub-engagement under Omni Support — could be Delivery (ongoing) or Closed (one-off complete). Adjust PROJECTS.md card accordingly. -> [[Accounts/Active/MVMI/Omni Support/Chaos Engineering Workshop/NOTES]] 📅 2026-05-29 #review

### AM engine bootstrap (this week)

- [ ] **Account-level teasers** Per-project teasers in PROJECTS.md are minimal placeholders ("Active engagement — see NOTES"). Enrich each with package/MRR/TAM/contract-end signal as available. Direct Obsidian-Kanban edit. 📅 2026-06-03 #drafting
- [ ] **AM dashboard launcher registration** After dashboard HTML build, register `account-management.html` in `_dashboards/index.html` launcher (CPS category, next to Sales) + add row in `_dashboards/00_DASHBOARD_INDEX.md`. 📅 2026-05-27 #infra

## Tomorrow: 2026-05-28 (Thursday)

### Merkantil scoping (assumes user sent post-call info by then)

- [ ] **Merkantil Bank Zrt.** Incorporate post-call info from user. Update Merkantil NOTES (Action Items, scoping decisions, agreed CPS deliverables, number sent). Move kanban card from Backlog to appropriate stage (Initial meeting if just intro happened, Define project need if scoping in flight, Contracted if number accepted, etc.). -> [[Accounts/Leads/Merkantil/NOTES]] 📅 2026-05-28 #post-call

## Future / no specific date

- [ ] **All Active accounts** Per-account quarterly review cycle — establish cadence. Currently no formal review schedule. Likely candidates for first review: MVMI (largest), Onriva + Observer (reference clients), OKFO (recent install). 📅 2026-06-15 #review #cadence
- [ ] **Upsell scan** Run upsell discovery on accounts with one engagement (everyone except MVMI). The MVMI 2-engagement model is the pattern — which other accounts could carry a second engagement? 📅 2026-06-30 #upsell #strategy

## Live cross-vault query: open AM tasks with due dates

```dataview
TASK
FROM "02_Areas/Sonrisa/CPS/Accounts/Active"
WHERE !completed AND contains(text, "📅")
SORT text ASC
```

## Conventions

- **Adding a task anywhere in Accounts/Active**: include `📅 YYYY-MM-DD` somewhere in the task line, and it appears in the query above.
- **Completing a task**: change `[ ]` to `[x]` and append `✅ YYYY-MM-DD` at the end of the line.
- **Linking the project**: use `[[Accounts/Active/<Name>/NOTES|<Display>]]` or with sub-engagement `[[Accounts/Active/<Name>/<Engagement>/NOTES|<Display>]]`.

## Done log (latest first)

- 2026-05-27: **AM engine bootstrap.** PROJECTS.md created with 14 cards (1 Backlog: Merkantil, 13 Delivery: existing Active engagements incl. 3 MVMI sub-engagements). AM_TODAY.md created (this file). Dashboard HTML build pending. ✅
