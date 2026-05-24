---
# ===========================================================================
# CPS Team board, dashboard source. Read by _dashboards/team.html every 8s.
# Edit here in Obsidian; the dashboard reflects changes live (read-only).
# Compiled from: CLAUDE.md (Team Structure), Workshop Summary 2026-03-24,
# 01_PROJECT_STATE.md, Team/01. Team.md. Deep reference stays in those files.
# ===========================================================================
type: team-board
title: CPS Team
updated: 2026-05-22
# --- Delivery units (client -> TAM -> members) -------------------------------
units:
  - client: "Green Hill / SynLab"
    package: "Managed Service"
    tam: "Molnár Dániel"
    members: [Kovács Marcell, Tornai Zsolt]
    profit: null
    status: healthy
    accent: "#1f7a4d"
    note: "TAM is also the Sales Engineer. Active delivery."
    source_file: "Accounts/Active/Green_Hill_SynLab/NOTES.md"
  - client: "Onriva"
    package: "Managed Service"
    tam: "Kovács Attila / Vaida Márk"
    members: [Vaida Márk, Gáll Botond]
    profit: 72
    status: watch
    accent: "#0e7490"
    note: "TAM not yet formally decided (KV or Márk). Was a sick project, now healthy at 72% margin."
    source_file: "Accounts/Active/Onriva/NOTES.md"
  - client: "Colosseum Dental"
    package: "Managed Service"
    tam: "Kovács Marcell"
    members: [Gáll Botond, Szántó Zoltán]
    profit: null
    status: risk
    accent: "#c0392b"
    note: "URGENT. May 2026 deadline, behind schedule. Status meeting with unit still not held. Contract renewal review in progress."
    source_file: "Accounts/Active/Colosseum_Dental/NOTES.md"
  - client: "Diligentes"
    package: "Managed Service"
    tam: "Ceclan Alexandru"
    members: []
    profit: null
    status: new
    accent: "#b07a18"
    note: "New client. Unit members TBD."
    source_file: "Accounts/Active/Diligentes/NOTES.md"
  - client: "SocialBud"
    package: "Managed Service"
    tam: "Szabolcs (light touch)"
    members: [Kovács Marcell, Pap Dávid]
    profit: null
    status: healthy
    accent: "#1f7a4d"
    note: "Loss-making early, profitable for the last 6+ months. A learning project."
    source_file: "Accounts/Active/SocialBud/NOTES.md"
  - client: "OKFO"
    package: "Managed Service"
    tam: "Tornai Zsolt"
    members: []
    profit: null
    status: healthy
    accent: "#1f7a4d"
    note: "Self-organizing unit. Dull but reliable revenue. 'We need many like this.'"
    source_file: "Accounts/Active/OKFO/NOTES.md"
  - client: "Jumeon"
    package: "Managed Service"
    tam: "Kovács Attila"
    members: []
    profit: 48
    status: watch
    accent: "#b07a18"
    note: "Yellow margin (48%) but stable revenue. Client maximally satisfied with KV."
    source_file: "Accounts/Active/Jumeon/NOTES.md"
  - client: "Observer"
    package: "Fixed price"
    tam: "Bánfi István"
    members: []
    profit: null
    status: watch
    accent: "#0e7490"
    note: "Project lead model, fixed price. Cost optimization report pending, then post-mortem."
    source_file: "Accounts/Active/Observer/NOTES.md"
  - client: "MVMI, AzureDevOps"
    package: "Managed Service"
    tam: "TBD"
    members: []
    profit: null
    status: blocked
    accent: "#6d6d6a"
    note: "Contract has RED clauses needing negotiation before signing. Not at kickoff. Team unassigned."
    source_file: "Accounts/Active/MVMI/AzureDevOps Managed Service/NOTES.md"
# --- Team members ------------------------------------------------------------
members:
  - name: "Ceclan Alexandru"
    short: "Ceclan"
    group: Leadership
    title: "Team Lead & Guildhead"
    level: E8
    location: MVH
    tam: true
    star: true
    skills: [AWS]
    units: [Diligentes]
    note: "Backbone of the team, the only E8 AWS engineer, holds the team together. ~6h/day. Interviews heavily. Guildhead, formalized with a contract."
  - name: "Szántó Zoltán"
    short: "Zoli"
    group: Leadership
    title: "Team Lead, Sales Engineer"
    level: ""
    location: MVH
    tam: false
    star: true
    skills: [Cloud Native, AWS]
    units: [Colosseum Dental]
    note: "Proactive, cloud native, CORE. Also acts as Sales Engineer. Strong English."
  - name: "Póda Alexander"
    short: "Sanyi"
    group: Leadership
    title: "Senior Engineer"
    level: E7
    location: BUD
    tam: false
    star: false
    skills: [AWS, GCP, n8n]
    units: []
    note: "AWS expert, reliable. Interviews candidates and proactively handles clients. Strategic AWS work."
  - name: "Bánfi István"
    short: "István"
    group: Contractor
    title: "E9+ Solution Architect, Sales Engineer"
    level: E9+
    location: ""
    tam: true
    star: true
    skills: [AWS, GCP, Oracle]
    units: [Observer]
    note: "E9+ contractor architect. Multi-cloud (AWS, GCP, Oracle). Observer project lead. Monthly hours certified via TIG review."
  - name: "Molnár Dániel"
    short: "Dani"
    group: Sales Engineer
    title: "Sales Engineer"
    level: E7-E8
    location: ""
    tam: true
    star: false
    skills: [AWS]
    units: [Green Hill / SynLab]
    note: "Talented, highest salary on the team. Negotiates with clients in English, stress-tolerant. TAM for Green Hill."
  - name: "Kovács Attila"
    short: "KV"
    group: Experienced
    title: "Engineer"
    level: E6
    location: MVH
    tam: true
    star: false
    skills: [AWS]
    units: [Jumeon, Onriva]
    note: "Jumeon TAM, client maximally satisfied. Onriva TAM candidate (decision pending). Stepping up a level."
  - name: "Tornai Zsolt"
    short: "Zsolt"
    group: Experienced
    title: "Engineer"
    level: ""
    location: MVH
    tam: true
    star: false
    skills: [AWS]
    units: [OKFO, Green Hill / SynLab]
    note: "OKFO TAM (self-organizing). Green Hill unit member."
  - name: "Török Bálint"
    short: "Bálint"
    group: Experienced
    title: "Engineer"
    level: ""
    location: MVH
    tam: false
    star: false
    skills: [AWS]
    units: []
    note: "AWS Security Specialty certification planned (fills the partner Technical Certified gap)."
  - name: "Vaida Márk-Ádám"
    short: "Márk"
    group: Young Talent
    title: "Engineer"
    level: ""
    location: MVH
    tam: false
    star: true
    skills: [AWS]
    units: [Onriva]
    note: "Standout young talent. Onriva unit member and TAM candidate."
  - name: "Kovács Marcell"
    short: "Marci"
    group: Young Talent
    title: "Engineer"
    level: ""
    location: BUD
    tam: true
    star: false
    skills: [AWS]
    units: [Colosseum Dental, Green Hill / SynLab, SocialBud]
    note: "Colosseum TAM. Carries the monthly client reporting (to be AI-assisted). Works across three units."
  - name: "Pap Dávid"
    short: "Dávid"
    group: Young Talent
    title: "Engineer"
    level: ""
    location: BUD
    tam: false
    star: false
    skills: [AWS]
    units: [SocialBud]
    note: "SocialBud unit member."
  - name: "Gáll Botond"
    short: "Boti"
    group: Young Talent
    title: "Engineer"
    level: ""
    location: MVH
    tam: false
    star: false
    skills: [AWS]
    units: [Onriva, Colosseum Dental]
    note: "Onriva and Colosseum unit member."
# --- Alumni (departed) -------------------------------------------------------
alumni:
  - name: "Bakonyi Péter"
    location: SZEG
    reason: "Departed, narcissistic behavior, not a values fit."
  - name: "Jankó-Király Attila"
    location: PCS
    reason: "Departed, not a team fit."
# --- Recruitment pipeline ----------------------------------------------------
recruitment:
  - name: "2x E1 Junior"
    status: planned
    note: "From the junior program. Replaces the paused senior hires."
  - name: "Kulcsár Vencél"
    status: paused
    note: "Recruitment postponed, juniors prioritized instead."
  - name: "Csirak Raymond"
    status: paused
    note: "First call when the team needs to grow with the pipeline."
---

# CPS Team

Live data for the team board lives in the frontmatter above. Edit it in Obsidian and `_dashboards/team.html` reflects the change within 8 seconds. Read-only dashboard, single source of truth is this file.

**Headcount:** ~13 engineers + 1 E9+ contractor. Stable after two departures (Bakonyi, Jankó-Király). Two E1 juniors planned.

## Roles in the unit model

- **TAM (Technical Account Manager)** — single point of accountability per client. First contact, communication, escalation, reporting. Empowered decision-maker inside the project. 2h reaction-time expectation in the TAM hat.
- **Unit Member** — engineer behind the TAM. Entry point for juniors ("kovácsinas" who learns and carries).
- **Sales Engineer** — separate function (Zoli, Molnár Dani, István). Sits with the client, negotiates in English, stress-tolerant.

See `Team/Units/00_Units_Concept.md` for the full unit model and `Team/Workshop Summary 2026-03-24.md` for the workshop decisions that assigned these TAMs.

## Editing notes

- `units[]`: one card per client delivery unit. `status` is one of `healthy`, `watch`, `risk`, `new`, `blocked`. `profit` is an integer percent or `null` if unknown.
- `members[]`: `group` is one of `Leadership`, `Architect`, `Sales Engineer`, `Experienced`, `Young Talent`, `Contractor`. `tam: true` adds a TAM badge. `star: true` flags a standout. `short` is the nickname used in unit member lists.
- `alumni[]`: departed members, shown muted at the bottom.
- `recruitment[]`: hiring pipeline. `status` is `planned` or `paused`.
- Profitability figures (Onriva 72%, Jumeon 48%) come from the 2026-03-24 workshop. Update as new numbers land from the financial dashboard.

## Deep reference

- `CLAUDE.md` — Team Structure section (canonical roster + recruitment values)
- `Team/Workshop Summary 2026-03-24.md` — unit/TAM assignments, profitability, escalation model
- `Team/Units/00_Units_Concept.md` — unit model concept
- `01_PROJECT_STATE.md` — current risks (Colosseum, Onriva TAM, MVMI contract)
