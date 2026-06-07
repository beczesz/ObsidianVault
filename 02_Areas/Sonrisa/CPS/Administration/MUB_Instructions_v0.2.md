---
title: "Monthly Update Brief (MUB) - Generation Instructions"
date: 2026-04-22
author: Becze Szabolcs
status: active
description: "Structured instructions for generating monthly update briefs from timesheet data: a markdown document that maps raw CPS entries to five hour categories (Billable, Internal, Sick+Leave, MVMI Availability, Other) and aggregates them by project and person. Used by Szabolcs to prepare dashboard update inputs."
description_source: auto
description_hash: 6171a4f00908e7cb
id: 102766d2-a4d8-4f86-9ec1-71775a9eb6df
index_schema_version: 1
bdos_index: true
---
# Monthly Update Brief (MUB) - Generation Instructions

**Version:** 0.2
**Owner:** Szabolcs
**Last updated:** 2026-04-22

---

## What is the MUB?

The MUB is a structured markdown document that distills the `_base.xlsx` data into text form. It serves as the data input for the Phase 2 dashboard update skill (`sonrisa-cps-dashboard-update`).

The MUB contains:
- Project hours breakdown (who worked on which project, how many hours)
- Team member hours breakdown (which projects each person worked on)
- Hours summary per person across 5 categories
- Per-contractor breakdowns (for TIG verification)

The MUB does NOT contain daily rates, E-levels, employment status, or billing types. Those are derived by the dashboard update skill from the dashboard's existing data.

---

## Source Data

**Input file:** `activityreport_YYYY_MM_base.xlsx` (Phase 1 output)

The `_base.xlsx` contains:
- **CPS sheet:** Raw timesheet entries (User, Team, Project name, Company, Task ID, Task name, Activity description, Date, Start, End, Length, Work type)
- **Team sheet:** Team roster (Name, Site, Status, Level, Position)
- **Sheet3:** Pivot tables for category validation

### Key columns from the CPS sheet

| Column | What it contains | Example |
|--------|-----------------|---------|
| User | Person name (Hungarian format) | Attila Kovacs |
| Project name | Sontime project container | Cloud Platform Services |
| Company name | Client company | Jumio |
| Task name | Actual project/task worked on | Development and operations |
| Length | Hours spent | 8 |
| Work type | Billable work / Non-billable work / Non-work activity | Billable work |

**Important:** The "Project name" in Sontime is a generic container (e.g., "Cloud Platform Services"). The "Task name" is the actual project (e.g., "Observer", "Bayer", "ColosseumDental"). The MUB uses Task name for project grouping.

---

## 5-Category Hour Classification

Every logged hour in the CPS sheet must be assigned to exactly one of these 5 categories. The categories are mutually exclusive and must sum to the CPS total.

### Category 1: Billable

Client-facing project work. This is the primary revenue-generating category.

All tasks NOT classified as Internal, Sick+Leave, MVMI Availability, or Other are Billable.

### Category 2: Internal

Team overhead required for CPS to function. Defined by the Sheet3 "Internal hours" pivot filter.

| Task name (Sontime) | Notes |
|----------------------|-------|
| Meeting | Team meetings, syncs, WSMs |
| Megbeszeles | IdomSoft-related meetings (company: IdomSoft Zrt.) |
| General Research | Internal research |
| Internal Systems | Internal infrastructure |
| Interviews | Recruitment interviews |
| Learning | Team learning and development |
| PM task | Project management overhead |
| DevOps Guild activities | Guild sessions (Work type: Non-work activity) |
| Workshop - business | Business workshops (Work type: Non-billable work) |

### Category 3: Sick + Paid leave

Non-work activities. Identified by Work type = "Non-work activity" AND task is a leave type.

| Task name (Sontime) | Work type |
|----------------------|-----------|
| Paid leave | Non-work activity |
| Sick leave | Non-work activity |

### Category 4: MVMI Availability

MVMI OMNI availability hours. These are reported as worked hours but represent availability (on-call) time, not active project work. Tracked separately because they inflate billable totals if mixed in.

| Task name (Sontime) | Notes |
|----------------------|-------|
| MVMI OMNI ticket | Short form (older exports) |
| MVMI OMNI - general availability collector ticket | Full form (current exports) |

### Category 5: Other

Any task that does not match categories 1-4. This category should ideally be empty after classification.

**Workflow:** When generating the MUB, if any hours fall into "Other," present them to the user for classification before finalizing. The user will assign each "Other" item to one of the 4 defined categories (or create a new rule).

---

## Classification Priority

Apply categories in this order (first match wins):

1. **Sick + Paid leave:** Work type = "Non-work activity" AND Task name in {Paid leave, Sick leave}
2. **Internal:** Task name in the Internal tasks list (see Category 2 table) OR (Work type = "Non-work activity" AND Task name = "DevOps Guild activities")
3. **MVMI Availability:** Task name = "MVMI OMNI - general availability collector ticket"
4. **Other:** Task not matched by any rule above AND not in the known Billable list
5. **Billable:** Everything else

---

## Task-to-Project Aggregation Rules

These rules map Sontime Task names to MUB project names:

| Pattern | MUB Project Name | Company |
|---------|-----------------|---------|
| SIL-xxx (all Spinwheel tickets) | Spinwheel (Silver 3.0) | Spinwheel |
| PM task (company: Spinwheel) | Spinwheel (Silver 3.0) | Spinwheel |
| SD-xxx (all Synlab tickets) | Synlab Plasma | Synlab |
| Onriva: * (all Onriva tasks) | Onriva | Sonrisa |
| SocialBud: * (all SocialBud tasks) | SocialBud | Sonrisa |
| Observer + sub-tasks (5.1 ES...) | Observer | Sonrisa/Observer |
| IdomSoft - Faker Microsite Platform | IdomSoft | Sonrisa |
| Development (company: IdomSoft) | IdomSoft | IdomSoft Zrt. |
| Development and operations | Jumio AWS | Jumio |
| General development | Lufthansa Netline - Crew | Lufthansa |
| Diligent - ARC BOS Sunset | Diligentes | Sonrisa |
| ColosseumDental | Colosseum Dental | Sonrisa |
| DirectTravel | Direct Travel | Sonrisa |
| greeHill | Green Hill | Sonrisa |
| ProSharp - OTEL | ProSharp | Sonrisa |
| MVMI | MVMI ADO Managed Service | Sonrisa |
| [SUPPORT] NKP MTR... | NKP | NKP |

All other billable tasks keep their Sontime task name as the MUB project name.

### Edge cases

- **Megbeszeles** is Internal (meetings) even though company = "IdomSoft Zrt." - do NOT aggregate into IdomSoft billable project
- **SIL-xxx / SD-xxx tickets** change every month - the aggregation rule (all SIL -> Spinwheel, all SD -> Synlab) handles this automatically
- **PM task** with company Spinwheel is aggregated into Spinwheel but categorized as Internal
- **SocialBud** tasks follow the same merge pattern as Onriva

---

## Name Format

**Important:** Sontime exports use **FirstName LastName** format (e.g., "Alexandru Ceclan", "Bálint Lajos Török"), not the Hungarian LastName FirstName convention. The CPS team list must use the Sontime format for matching.

---

## Contractor Identification

Contractors are identified from the **Team sheet**, column "Position":
- Position = "Contractor" -> full contractor (e.g., Banfi Istvan E9, Szabo Andor E3)
- Position = "PartTime" -> part-time contractor (e.g., Beder Ferenc E7)

Each contractor gets a separate breakdown section in the MUB showing all their hours by project and category.

---

## MUB Structure

The MUB has 5 sections:

### Section 1: Project Hours Breakdown by Client

Groups billable hours by client company and project, with per-person detail. Alphabetical by project name.

### Section 2: Team Member Hours by Client

Groups hours by person, showing which projects each person worked on and their category totals (billable, internal, MVMI availability).

### Section 3: Hours Summary

Four tables:
- **Billable hours per person** with total
- **Internal hours per person** with total
- **MVMI Availability hours per person** with total
- **Sick + Paid leave per person** with total

### Section 4: Contractor Breakdowns

One sub-section per contractor/part-time person, showing all their hours by project and category.

### Section 5: Category Totals (verification)

Summary table showing all 5 categories and verifying they sum to the CPS total.

---

## How to Generate the MUB

1. Phase 1 produces `_base.xlsx`
2. Read the CPS sheet raw data
3. Read the Team sheet for contractor identification
4. Apply the 5-category classification (in priority order)
5. If any "Other" hours exist, present to user for classification
6. Apply the aggregation rules (Spinwheel, Synlab, Onriva, SocialBud merging)
7. Generate the markdown following the template below
8. Verify: Billable + Internal + Sick/Leave + MVMI Availability + Other = CPS Total
9. Save as `MUB_YYYY_MM.md`

---

## MUB Template

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
| Other | [X] |
| **Total** | **[X]** |

**Billable projects:** [count]
**Team size:** [count]
**Contractors:** [count]

---

## Project Hours Breakdown by Client

[One block per billable project, alphabetical by project name]

### [Project Name] -- [Company]

| Person | Hours |
|--------|-------|
| [Name] | [hours] |
| **Total** | **[hours]** |

[repeat for each project]

---

## Team Member Hours by Client

[One block per person, alphabetical]

### [Person Name] (billable: [X]h, internal: [Y]h, MVMI avail: [Z]h)

| Project | Category | Hours |
|---------|----------|-------|
| [project] | Billable | [hours] |
| [task] | Internal | [hours] |

[repeat for each person]

---

## Hours Summary

### Billable Hours per Person

| Person | Hours |
|--------|-------|
| [Name] | [hours] |
| **Total** | **[total]** |

### Internal Hours per Person

| Person | Hours |
|--------|-------|
| [Name] | [hours] |
| **Total** | **[total]** |

### MVMI Availability Hours per Person

| Person | Hours |
|--------|-------|
| [Name] | [hours] |
| **Total** | **[total]** |

### Sick + Paid Leave per Person

| Person | Hours |
|--------|-------|
| [Name] | [hours] |
| **Total** | **[total]** |

---

## Contractor Breakdowns

### [Contractor Name] ([Level], [Position])

| Project | Category | Hours |
|---------|----------|-------|
| [project] | [category] | [hours] |
| **Total** | | **[total]** |

[repeat for each contractor]

---

## Category Verification

| Category | Hours |
|----------|-------|
| Billable | [X] |
| Internal | [X] |
| MVMI Availability | [X] |
| Sick + Paid leave | [X] |
| Other | [X] |
| **CPS Total** | **[X]** |
| **Match:** | [Yes/No] |

---

**Categorization version:** MUB_Instructions_v0.2
```

---

## Maintaining the Classification

When a new task appears in Sontime data that doesn't match any existing rule:
1. It will fall into "Other" during MUB generation
2. The generation process will pause and ask the user to classify it
3. Update this document's category tables with the new task
4. Update the `_base.xlsx` Sheet3 pivot filters accordingly

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v0.1 | 2026-04-22 | Initial version. 2-category structure (Billable vs Internal). |
| v0.1.1 | 2026-04-22 | Corrected categorization from actual Sheet3 pivot filter values. |
| v0.2 | 2026-04-22 | Major rewrite: 5-category structure (Billable, Internal, Sick+Leave, MVMI Availability, Other). Added contractor breakdowns, classification priority order, Other-review workflow. Internal now includes Learning, PM task, DevOps Guild activities. |
| v0.2.1 | 2026-04-22 | Added: Workshop - business to Internal tasks. Added both short/full MVMI OMNI ticket name forms. Documented Sontime FirstName LastName format. Verified with March 2026 live data. |
