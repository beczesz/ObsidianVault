# Monthly Update Brief (MUB) -- Generation Instructions

**Version:** 0.1
**Owner:** Szabolcs
**Last updated:** 2026-04-22

---

## What is the MUB?

The MUB is a structured markdown document that distills the `_base.xlsx` pivot tables into text form. It serves as the data input for the Phase 2 dashboard update skill (`sonrisa-cps-dashboard-update`).

The MUB contains:
- Project hours breakdown (who worked on which project, how many hours)
- Team member hours breakdown (which projects each person worked on)
- Billable vs internal hours summary per person
- Contractor breakdown (for TIG verification)

The MUB does NOT contain daily rates, E-levels, employment status, or billing types. Those are derived by the dashboard update skill from the dashboard's existing data.

---

## Source Data

**Input file:** `activityreport_YYYY_MM_base.xlsx` (Phase 1 output)

The `_base.xlsx` contains:
- **CPS sheet:** Raw timesheet entries (User, Team, Project name, Company, Task ID, Task name, Activity description, Date, Start, End, Length, Work type)
- **Team sheet:** Team roster (Name, Site, Status, Level, Position)
- **Pivot tables:** Pre-built aggregations of the CPS data

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

## MUB Structure

The MUB has 4 sections:

### Section 1: Project Hours Breakdown by Client

Groups hours by client company and task (project), with per-person detail. This is the primary view for the dashboard update.

Aggregation rules:
- Group by Company name, then by Task name, then by User
- For Spinwheel: aggregate all SIL-xxx tickets into one "Spinwheel" project
- For Synlab: aggregate all SD-xxx tickets into one "Synlab" project
- For IdomSoft: aggregate all tasks into one "IdomSoft" project
- For Observer: include sub-tasks (e.g., "5.1 ES index feltoltes...") under Observer
- For Onriva: merge "Incidents, New features" and "Availability, Monitoring, Meetings" into one "Onriva" project

### Section 2: Team Member Hours by Client

Groups hours by person, showing which projects each person worked on. Use this to verify individual workloads and cross-project allocation.

### Section 3: Hours Summary per Person

Two tables:
- **Billable hours per person:** Total client-facing hours per team member
- **Internal hours per person:** Non-billable/internal hours per team member (meetings, learning, etc.)

### Section 4: Contractor Breakdown

Hours per project for the E9+ contractor (Banfi Istvan). Used for TIG verification in Phase 3.

---

## Billable vs Internal Categorization

The `_base.xlsx` Sheet3 has an "Internal hours" pivot table that filters on Task name to define which tasks are internal. This is the **authoritative source** for the categorization. All tasks NOT in the internal filter are treated as billable.

### IMPORTANT: Maintaining the categorization

When a new project/task appears in the Sontime data, it MUST be classified as billable or internal. Update this section AND the `_base.xlsx` Sheet3 pivot table filter accordingly. If not updated, the MUB totals will be incorrect.

### How the categorization works

Sheet3 in `_base.xlsx` contains two pivot tables:

1. **"Total hours" pivot** (rows 3-19) -- shows a filtered subset of tasks (not all billable tasks)
2. **"Internal hours" pivot** (rows 24-36) -- the Task name page filter on this pivot defines the internal tasks

The internal categorization is read from the "Internal hours" pivot filter. Tasks visible in this filter = internal. Everything else = billable.

### Internal tasks (per Sheet3 "Internal hours" pivot filter)

These Task names are marked as internal in the pivot filter:

| Task name (Sontime) | Notes |
|----------------------|-------|
| Meeting | Team meetings, syncs, WSMs |
| Megbeszeles | IdomSoft-related meetings (company: IdomSoft Zrt.) |
| General Research | Internal research |
| Internal Systems | Internal infrastructure |
| Interviews | Recruitment interviews |

### Non-work activities (excluded from both billable and internal)

These are filtered by Work type column, not by pivot filter:

| Task name (Sontime) | Work type |
|----------------------|-----------|
| Paid leave | Non-work activity |
| Sick leave | Non-work activity |

### Billable tasks (everything else)

All tasks NOT listed above are billable. This includes:

| Task name (Sontime)                               | Company          | Dashboard project        |
| ------------------------------------------------- | ---------------- | ------------------------ |
| Development and operations                        | Jumio            | Jumio AWS                |
| General development                               | Lufthansa        | Lufthansa Netline - Crew |
| Observer                                          | Sonrisa/OBSERVER | Observer                 |
| Bayer                                             | Sonrisa          | Bayer                    |
| ColosseumDental                                   | Sonrisa          | Colosseum Dental         |
| Diligent - ARC BOS Sunset                         | Sonrisa          | Diligentes               |
| DirectTravel                                      | Sonrisa          | Direct Travel            |
| greeHill                                          | Sonrisa          | Green Hill               |
| MVMI                                              | Sonrisa          | MVMI ADO Managed Service |
| MVMI OMNI - general availability collector ticket | Sonrisa          | MVMI Omni Support        |
| OKFO                                              | Sonrisa          | OKFO                     |
| Onriva: *                                         | Sonrisa          | Onriva                   |
| ProSharp - OTEL                                   | Sonrisa          | ProSharp                 |
| ErdSoft                                           | Sonrisa          | ErdSoft                  |
| EuroLeasing                                       | Sonrisa          | EuroLeasing              |
| RSM                                               | Sonrisa          | RSM                      |
| IdomSoft - Faker Microsite Platform               | Sonrisa          | IdomSoft                 |
| SIL-xxx (all Spinwheel tickets)                   | Spinwheel        | Spinwheel (Silver 3.0)   |
| SD-xxx (all Synlab tickets)                       | Synlab           | Synlab Plasma            |
| PM task                                           | Spinwheel        | Spinwheel (Silver 3.0)   |
| [SUPPORT] NKP MTR...                              | NKP              | NKP                      |
| Power automate                                    | Sonrisa          | Power automate           |
| Aws Inference Farm                                | Sonrisa          | Aws Inference Farm       |
| Sonrisa Sys                                       | Sonrisa          | Sonrisa Sys              |
| Sontools                                          | Sonrisa          | Sontools                 |
| Learning                                          | Sonrisa          | Learning                 |
| Deutsche Telekom                                  | Sonrisa          | Deutsche Telekom         |
| Workshop - business                               | Sonrisa          | Workshop - business      |
| SocialBud: *                                      | Sonrisa          | SocialBud                |
| DevOps Guild activities                           | Sonrisa          | DevOps Guild activities  |
| Development                                       | Sonrisa          | Development              |

**Note:** Deutsche Telekom and Workshop - business have Work type "Non-billable work" in Sontime, but they are NOT in the Sheet3 internal pivot filter. They are treated as billable per the pivot categorization. Review if this is intentional.

### Edge cases

- **Megbeszeles** is internal (meetings) but has company "IdomSoft Zrt." -- do NOT aggregate into the IdomSoft billable project
- **SIL-xxx / SD-xxx tickets** change every month -- the aggregation rule (all SIL -> Spinwheel, all SD -> Synlab) handles this automatically
- **SocialBud** tasks follow the same pattern as Onriva (merge all SocialBud: * tasks)

---

## How to Generate the MUB

1. Phase 1 produces `_base.xlsx`
2. Open `_base.xlsx` or have it available in Cowork
3. Read the CPS sheet raw data
4. Apply the aggregation rules (Spinwheel, Synlab, Onriva merging)
5. Apply the billable/internal categorization
6. Generate the markdown following the template below
7. Save as `MUB_YYYY_MM.md`

---

## MUB Template

```markdown
# CPS Monthly Update Brief

**Period:** YYYY MonthName (Month MM)
**Generated:** YYYY-MM-DD
**Source:** activityreport_YYYY_MM_base.xlsx
**Total billable hours:** [number]
**Total internal hours:** [number]
**Total hours:** [number]
**Projects:** [number of billable projects]
**Team size:** [number of people]

---

## Project Hours Breakdown by Client

[One block per project, alphabetical by company then project name]

### [Project Name] -- [Company]

| Person | Hours |
|--------|-------|
| [Name] | [hours] |

[repeat for each project]

---

## Team Member Hours by Client

[One block per person, alphabetical]

### [Person Name] (total: [X]h billable, [Y]h internal)

| Project | Company | Hours |
|---------|---------|-------|
| [task] | [company] | [hours] |

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

---

## Contractor Breakdown (Banfi Istvan)

| Project | Company | Hours |
|---------|---------|-------|
| [project] | [company] | [hours] |
| **Total** | | **[total]** |

---

**Categorization version:** MUB_Instructions_v0.1
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v0.1 | 2026-04-22 | Initial version. Billable/internal categorization based on March 2026 data. Several tasks pending classification review. |
| v0.1.1 | 2026-04-22 | Corrected categorization from actual Sheet3 pivot filter values. Internal = Meeting, Megbeszeles, General Research, Internal Systems, Interviews. All other tasks billable (including Power automate, Learning, Sonrisa Sys, etc.). Removed "Tasks needing classification" section. |
