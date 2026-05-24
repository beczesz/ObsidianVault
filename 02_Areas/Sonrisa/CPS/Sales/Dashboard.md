---
title: CPS Sales Dashboard
date: 2026-05-11
description: KPI tracking dashboard using Dataview queries. Requires Dataview and Dataview Charts plugins.
dashboard_contract: Sales/DASHBOARD_CONTRACT.md
related: Sales/dashboard.html
id: 07caffeb-9cb3-420b-95d4-36ce4ca3f162
index_schema_version: 1
---

# CPS Sales Dashboard

> **There is also a live HTML dashboard.** `Sales/dashboard.html` is an interactive kanban + Today panel that polls Pipeline.md, leads.md, and TODAY.md every 8 seconds and rebuilds itself from those files. Open it via a local HTTP server (`npx serve .` from the vault root, then visit `http://localhost:<port>/02_Areas/Sonrisa/CPS/Sales/dashboard.html`). Format contract: `Sales/DASHBOARD_CONTRACT.md`. This markdown file is the older KPI tracker, retained for plugin-driven Dataview / Charts views.

> **Last updated:** 2026-05-19 | **Day:** 9 of 90 | **Days remaining:** 81 | **Start (reset):** 2026-05-11
>
> Sales Engine v1.0 was built 2026-04-27. Execution restarted 2026-05-11. Week 1: 2 sends (CIG Pannonia connect, KBOSS connect) vs 5 target. Week 2 day 1: 2 sends (SEON InMail to Adam Berkecz, CIG Attila Zankai escalation InMail). 4 total touches. Three leads in dialogue window (CIG, KBOSS, SEON). Pipeline state cleaned 2026-05-18 overnight: ABRIS new HOT (banking IT, ~142 emp, fresh DevOps Fejlesztő), Cardinal Software new WARM monitor. 3 WARMs demoted to COLD (Lensa, EOS Faktor, Barion), 2 COLDs cut to Lost (Pentech, ABZ Innovation). Tomorrow morning send: ABRIS.

## Pipeline Health

### Leads by Stage (manual update weekly)

| Stage | Count | Potential MRR |
|-------|-------|---------------|
| HOT - Outreach This Week | 1 | EUR 2,700 |
| WARM - Outreach This Sprint | 5 | EUR 6,690 - 11,200 |
| COLD - Research | 5 | EUR 1,980 - 4,950 |
| Contacted | 3 | EUR 8,700 - 9,200 |
| Lost / Parked | 4 | -- |
| Discovery Call | 0 | -- |
| Proposal Sent | 0 | -- |
| Won | 0 | EUR 0 |
| **Total Pipeline** | **14** | **EUR 16,650 - 28,360** |

### Weekly Outreach Velocity

| Week | Period | Touches Sent | Target | Replies | Calls Booked |
|------|--------|-------------|--------|---------|--------------|
| W1 | May 11-17 | 2 | 5 | 0 | 0 |
| W2 | May 18-24 | 2 | 10 | 0 | 0 |
| W3 | May 25-31 | | 15 | | |
| W4 | Jun 1-7 | | 20 | | |
| W5 | Jun 8-14 | | 25 | | |
| W6 | Jun 15-21 | | 25 | | |
| W7 | Jun 22-28 | | 25 | | |
| W8 | Jun 29-Jul 5 | | 25 | | |

> Ramp curve: W1 starts at 5 (the 5 HOT) and grows to the 25/week target by W5. Realistic for a single human sender (Szabolcs/Nandi).

### Funnel Conversion Tracking

| Metric | Actual | Benchmark | Status |
|--------|--------|-----------|--------|
| Total outreach sent | 4 | 150-200 per deal | 2.0% to 2.7% of way to first deal |
| Reply rate | -- | 5-15% | Awaiting responses (KBOSS Day 5, SEON Day 0, CIG Attila Day 0 InMail) |
| Reply to discovery | -- | 30-50% | No data |
| Discovery to qualified | -- | 40-60% | No data |
| Qualified to proposal | -- | 60-80% | No data |
| Proposal to close | -- | 25-35% | No data |
| Avg cycle time | -- | 30-90 days | No data |

## 90-Day Plan Progress

### Phase 1: Activate & Convert (Weeks 1-4, 2026-05-11 to 2026-06-07) -- CURRENT

Infrastructure already built (carried over from prior cycle):
- [x] Build sales infrastructure (scanner, case studies, enablement)
- [x] Validate historical leads (15 leads re-scored)
- [x] Career page scan all pipeline leads (7 confirmed hiring)
- [x] ENGINE B: Identify 10 Hungarian product companies
- [x] Strategy review with thinking team (4 AIs)
- [x] Migrate pipeline to Obsidian Kanban

This-cycle execution:
- [ ] Lead validation refresh (orchestrator scrape 2026-05-11, refresh HOT/WARM)
- [ ] Send outreach to top 5 HOT leads (target: 2026-05-12/13)
- [ ] Send outreach to all 15 leads (target: 2026-05-15)
- [ ] Process BSides Budapest contacts (event was 2026-04-29)
- [ ] Attend Craft Conference Budapest (2026-06-04)
- [ ] Book first discovery call (target: Day 35, 2026-06-15)

### Phase 2: Scale & Refine (Weeks 5-8, 2026-06-08 to 2026-07-05)

- [ ] Maintain 25 touches/week consistently
- [ ] Publish first article (Managed Service series, drafts in Marketing/Blogs/)
- [ ] Conduct Free Audit #1
- [ ] Submit Craft Conference talk for 2027
- [ ] First proposal sent (target: Day 56, 2026-07-06)

### Phase 3: Compound & Expand (Weeks 9-12, 2026-07-06 to 2026-08-02)

- [ ] Close deal #1
- [ ] Close deal #2
- [ ] First case study from own-pipeline client
- [ ] Western Europe expansion plan

## Key Dates

| Date | Event | Action |
|------|-------|--------|
| 2026-05-11 | Mon | Day 1 -- orchestrator lead validation refresh, sharpen HOT drafts |
| 2026-05-12 | Tue | Send top 5 HOT outreach (KBOSS, Chemaxon, Loxon, SEON, Colossyan) |
| 2026-05-13 | Wed | Send WARM batch (CIG Pannonia, EOS Faktor, Allonic) |
| 2026-05-15 | Fri | All 15 leads contacted target |
| 2026-06-04 | Thu | Craft Conference Budapest |
| 2026-06-15 | Mon | Day 35 -- first discovery call target |
| 2026-06-22 | Mon | Day 42 -- first Free Audit target |
| 2026-07-06 | Mon | Day 56 -- first proposal target |
| 2026-08-02 | Sun | Day 84 -- 90-day plan review |
| 2026-08-09 | Sun | Day 90 -- end of plan |

## Live Queries

### HOT Leads (from Pipeline.md)

```dataview
TASK FROM "Sales/Pipeline"
WHERE contains(tags, "#hot") AND !completed
SORT text ASC
```

### All Open Leads with Tags

```dataview
TASK FROM "Sales/Pipeline"
WHERE !completed
GROUP BY section
```

### Outreach Velocity (requires Charts plugin)

```chart
type: bar
labels: [W1, W2, W3, W4, W5, W6, W7, W8]
series:
  - title: Touches Sent
    data: [2, 2, 0, 0, 0, 0, 0, 0]
  - title: Target
    data: [5, 10, 15, 20, 25, 25, 25, 25]
tension: 0.2
width: 80%
labelColors: false
fill: false
beginAtZero: true
```

### Lead Source Breakdown (requires Charts plugin)

```chart
type: doughnut
labels: [ENGINE A (Job Posting), ENGINE B (Pain-Based), ENGINE C (Inbound)]
series:
  - title: Leads by Source
    data: [6, 8, 1]
tension: 0.2
width: 60%
labelColors: true
```

## Required Obsidian Plugins

For full dashboard functionality, install these community plugins:

1. **Kanban** -- for Pipeline.md board view
2. **Dataview** -- for dynamic queries across notes
3. **Charts** (obsidian-charts) -- for bar/line/pie charts
4. **Homepage** (optional) -- to make Dashboard.md your startup page
5. **Tracker** (optional) -- for streak/habit-style tracking

## Notes for Future Sessions

This dashboard is manually updated. When updating after outreach:
1. Move cards in Pipeline.md between columns
2. Update the Weekly Outreach Velocity table above
3. Update Funnel Conversion Tracking when data comes in
4. Check off 90-Day Plan items as completed
