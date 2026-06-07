---
title: "Monthly Update Brief (MUB) Template"
date: 2026-05-05
author: Becze Szabolcs
status: active
description: "A structured template for monthly activity reports that captures current-month hours by project and person, designed for Claude to process into dashboard updates using the sonrisa-cps-dashboard-update skill."
description_source: auto
description_hash: 35de11a6b0e85ed0
id: 7aeac6bd-a2dc-45a3-94f6-e3a08c370007
index_schema_version: 1
bdos_index: true
---
# Monthly Update Brief (MUB) Template

**Version:** 0.3
**Last updated:** 2026-04-22

The MUB is a textual representation of the Phase 1 data. It contains **only the current month's data** -- who worked on which project, how many hours, organized at task-level granularity matching Dashboard T&M Raw rows.

The MUB does NOT contain daily rates, E-levels, employment status, or billing types. Those are derived by this skill from the dashboard's existing data (previous month carry-forward).

---

## How to Use

1. Cowork processes Phase 1 (activity report -> _base.xlsx + _tam.xlsx + MUB)
2. User pastes the MUB into Claude for Excel chat (or attaches the file)
3. Claude for Excel processes projects one by one using the `sonrisa-cps-dashboard-update` skill
4. The skill reads existing dashboard data for comparison and carry-forward

---

## MUB Format (v0.3)

### Header

```markdown
# CPS Monthly Update Brief

**Period:** YYYY MonthName (Month MM)
**Generated:** YYYY-MM-DD
**Source:** activityreport_YYYY_MM_base.xlsx

| Category | Hours |
|----------|-------|
| Billable | [X] |
| Internal | [X] |
| MVMI Availability | [X] |
| Sick + Paid leave | [X] |
| **Total** | **[X]** |

**Billable projects:** [count]
**Team size:** [count]
**Contractors:** [count]
```

### Per-Project Block (Section 1)

One block per billable project, ordered to match Dashboard T&M Raw sheet order (NOT alphabetical).

```markdown
### [Sontime Task Name] -- [Company]

**Dashboard:** [Client] / [Project]

| Person | Hours |
|--------|-------|
| [FirstName LastName] | [hours] |
| **Total** | **[hours]** |
```

The `**Dashboard:**` line is critical -- it maps directly to the Client (col E) and Project (col F) in T&M Raw. This skill uses it to find/create the correct rows.

**Name format:** MUB uses FirstName LastName (Sontime convention). The skill reverses to LastName FirstName (Dashboard convention) when matching rows.

### Team Member Hours (Section 2)

```markdown
### [Person Name] (billable: [X]h, internal: [Y]h, MVMI avail: [Z]h)

| Project | Category | Hours |
|---------|----------|-------|
| [task] | Billable | [hours] |
| [task] | Internal | [hours] |
```

### Hours Summary (Section 3)

Four separate tables: Billable, Internal, MVMI Availability, Sick + Paid Leave. Each has per-person hours and a total row. Used by Pass 2 (FTE internal) and Pass 3 (contractor internal).

### Contractor Breakdowns (Section 4)

```markdown
### [Name] ([Level], [Position])

| Project | Category | Hours |
|---------|----------|-------|
| [project] | [category] | [hours] |
| **Total** | | **[total]** |
```

Used by Pass 3 to determine contractor internal hours.

### Category Verification (Section 5)

```markdown
| Category | Hours |
|----------|-------|
| Billable | [X] |
| Internal | [X] |
| MVMI Availability | [X] |
| Sick + Paid leave | [X] |
| **CPS Total** | **[X]** |
| **Match:** | **Yes/No** |
```

---

## What is NOT in the MUB

Daily Rate, E-level, Emp Status, Billable type, Discount, Fixed price amount. These are all derived by the skill from the dashboard's previous month data. If the skill cannot find a person (new person, first appearance), it asks the user.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v0.1 | 2026-04-22 | Initial version. Alphabetical project ordering, no Dashboard mapping line. |
| v0.2 | 2026-04-22 | Simplified to current-month-only data. Removed comparison logic (moved to skill). |
| v0.3 | 2026-04-22 | Task-level granularity. Added `**Dashboard:**` line per project. Dashboard T&M Raw ordering (not alphabetical). Added name format note (FirstName LastName -> LastName FirstName). Aligned with mub-instructions.md v0.3. |
