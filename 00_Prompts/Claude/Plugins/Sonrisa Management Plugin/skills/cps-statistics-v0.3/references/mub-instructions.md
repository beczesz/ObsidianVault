# Monthly Update Brief (MUB) - Generation Instructions

**Version:** 0.4
**Owner:** Szabolcs
**Last updated:** 2026-05-05

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

**Important:** The "Project name" in Sontime can be either:
- A **generic container** (e.g., "Cloud Platform Services") where the "Task name" identifies the actual client project (e.g., "Observer", "Bayer", "ColosseumDental")
- A **dedicated client project** (e.g., "Silver 3.0", "Idomsoft - Legacy költöztetés", "Consultancy - Observer Service Remap") where ALL hours belong to that client regardless of task name

The MUB uses Task name for project grouping when the Sontime Project is "Cloud Platform Services". For dedicated client projects, ALL hours (including generic tasks like "Megbeszeles", "PM task", "Development") are billable to that client.

---

## 5-Category Hour Classification

Every logged hour in the CPS sheet must be assigned to exactly one of these 5 categories. The categories are mutually exclusive and must sum to the CPS total.

### Category 1: Billable

Client-facing project work. This is the primary revenue-generating category.

All tasks NOT classified as Internal, Sick+Leave, MVMI Availability, or Other are Billable.

### Category 2: Internal

Team overhead required for CPS to function. Defined by the Sheet3 "Internal hours" pivot filter.

**CRITICAL RULE:** Internal classification ONLY applies when the Sontime **Project name** is "Cloud Platform Services" (or other generic CPS containers like "Other", "Sonrisa Onboarding"). When hours are logged under a **dedicated client project** (e.g., "Silver 3.0", "Idomsoft - Legacy költöztetés", "Consultancy - Observer Service Remap", "Synlab Plasma (BigCommerce)"), ALL hours stay billable to that client -- even if the task name matches the Internal list below.

| Task name (Sontime) | Notes |
|----------------------|-------|
| Meeting | Team meetings, syncs, WSMs |
| Megbeszeles | General meetings (only Internal under CPS project) |
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
2. **Dedicated client project override:** If Project name is a dedicated client project (NOT "Cloud Platform Services", "Other", "Sonrisa Onboarding", "NKP-MTR"), then ALL hours are **Billable** to that client -- skip Internal check entirely. Map via the Dedicated Client Projects table below.
3. **Internal:** Task name in the Internal tasks list (see Category 2 table) OR (Work type = "Non-work activity" AND Task name = "DevOps Guild activities"). **Only applies when Project name = "Cloud Platform Services" or similar generic containers.**
4. **MVMI Availability:** Task name = "MVMI OMNI - general availability collector ticket"
5. **Other:** Task not matched by any rule above AND not in the known Billable list
6. **Billable:** Everything else

### Dedicated Client Projects (Sontime Project Name -> MUB Project)

These Sontime "Project name" values are dedicated client projects. ALL hours logged under them are billable to that client, regardless of task name:

| Sontime Project Name | MUB Project | Dashboard Client |
|---------------------|-------------|-----------------|
| Silver 3.0 | Spinwheel | Spinwheel |
| Idomsoft - Legacy költöztetés | IdomSoft | Idomsoft |
| Consultancy - Observer Service Remap | Observer | Observer |
| Synlab Plasma (BigCommerce) | Synlab | Synlab |
| Jumio AWS | Jumio AWS | Jumio |

**Note:** New dedicated client projects may appear in Sontime. If the Project name is clearly a client name (not a generic container), treat it as dedicated and add it to this table.

---

## Task-to-Project Aggregation Rules

These rules map Sontime Task names to MUB project names:

**For dedicated client projects** (Project name != "Cloud Platform Services"), ALL tasks are mapped to the project's MUB name (see Dedicated Client Projects table above). No task-level aggregation needed.

**For "Cloud Platform Services" project**, use task name to determine the MUB project:

| Pattern | MUB Project Name | Company |
|---------|-----------------|---------|
| SIL-xxx (all Spinwheel tickets) | Spinwheel (Silver 3.0) | Spinwheel |
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

### Task-to-Dashboard Mapping (TASK_TO_DASH)

Each MUB project block MUST include a `**Dashboard:**` line mapping the Sontime task to the exact Client / Project name used in the Dashboard's T&M Raw sheet. This enables Phase 2 to directly match MUB blocks to T&M Raw rows.

| Sontime Task Name | Dashboard Client | Dashboard Project |
|-------------------|-----------------|-------------------|
| Development and operations | Jumio | Jumio AWS |
| NKP-MTR (or [SUPPORT] NKP MTR...) | Agrárminisztérium | MTR support |
| Aws Inference Farm | CPS | AWS Inference Farm |
| Bayer | BayerStrada | Cloud Platform Services |
| ColosseumDental | ColosseumDental | Azure Logic App Phase 4 |
| Diligent - ARC BOS Sunset | Diligent | ARC BOS Sunset Phase 2 |
| DirectTravel | Direct Travel | Cloud Platform Services |
| greeHill | greehill | Managed Service |
| IdomSoft - Faker Microsite Platform | Idomsoft | Faker Microsite Platform |
| MVMI | MVMI | Monitoring Jan 1 - Feb 2 |
| Observer (+ sub-tasks) | Observer | Migration Part 2 |
| OKFŐ | Nádor Rendszerház (OKFŐ) | OKFŐ - CPS services |
| Onriva (Onriva:*) | Onriva | Onriva Project Container |
| Power automate | CPS | Power Automate |
| ProSharp - OTEL | ProSharp | OTEL |
| Sonrisa Sys | Sonrisa | Sonrisa Sys |
| Synlab (SD-xxx) | Synlab | Synlab - Plasma |
| Deutsche Telekom / Sonrisa Presales | Sonrisa | Sonrisa Presales |
| ErdSoft | ErdSoft | Performace Fix |
| EuroLeasing | EuroLeasing | Presales |
| General development | Lufthansa | Lufthansa Netline - Crew |
| RSM | RSM | Presales |
| Sontools | Sonrisa | Sontools |
| Spinwheel (SIL-xxx) | Spinwheel | Silver 3.0 |

**IMPORTANT:** Dashboard Project names may change between months (e.g., MVMI phases). When a new month starts and the project name in T&M Raw has changed, update this table. If a task has no mapping here, ask the user for the Dashboard Client / Project.

### Project Ordering in MUB

The MUB Section 1 (Project Hours Breakdown) must be ordered to match the Dashboard's T&M Raw sheet row order -- NOT alphabetically. This makes Phase 2 processing sequential and predictable.

The current T&M Raw order (as of March 2026):
1. Jumio / Jumio AWS
2. Agrárminisztérium / MTR support
3. CPS / AWS Inference Farm
4. BayerStrada / Cloud Platform Services
5. ColosseumDental / Azure Logic App Phase 4
6. Diligent / ARC BOS Sunset Phase 2
7. Direct Travel / Cloud Platform Services
8. greehill / Managed Service
9. Idomsoft / Faker Microsite Platform
10. MVMI / Monitoring Jan 1 - Feb 2
11. Observer / Migration Part 2
12. Nádor Rendszerház (OKFŐ) / OKFŐ - CPS services
13. Onriva / Onriva Project Container
14. CPS / Power Automate
15. ProSharp / OTEL
16. Sonrisa / Sonrisa Sys
17. Synlab / Synlab - Plasma
18. Sonrisa / Sonrisa Presales
19. ErdSoft / Performace Fix
20. EuroLeasing / Presales
21. Lufthansa / Lufthansa Netline - Crew
22. RSM / Presales
23. Sonrisa / Sontools
24. Spinwheel / Silver 3.0

New projects not in this list go at the end. Update the ordering when the Dashboard changes.

### Edge cases

- **Dedicated client projects take priority:** When "Megbeszeles", "PM task", "Development", or other generic task names appear under a dedicated client Sontime project (e.g., "Silver 3.0", "Idomsoft - Legacy költöztetés"), they are BILLABLE to that client, NOT Internal. Internal classification only applies under "Cloud Platform Services".
- **SIL-xxx / SD-xxx tickets** change every month - the aggregation rule (all SIL -> Spinwheel, all SD -> Synlab) handles this automatically
- **SocialBud** tasks follow the same merge pattern as Onriva
- **Sonrisa Onboarding** is treated as Internal (generic container), not a client project

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

Groups billable hours by Sontime task name and company, with per-person detail. Ordered to match Dashboard T&M Raw sheet order (see "Project Ordering in MUB" above). Each project block includes a `**Dashboard:**` line with the exact Client / Project name for T&M Raw matching.

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

[One block per billable project, in Dashboard T&M Raw order]

### [Sontime Task Name] -- [Company]

**Dashboard:** [Client] / [Project]

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
| v0.3 | 2026-04-22 | Major update: Task-level granularity (group by Sontime Task Name, not Project Name). Added TASK_TO_DASH mapping table. Added Dashboard ordering (T&M Raw order, not alphabetical). Added `**Dashboard:**` line to each project block. Updated template format. |
| v0.4 | 2026-05-05 | Critical fix: Dedicated client Sontime projects (Silver 3.0, Idomsoft, Observer, Synlab, etc.) keep ALL hours as billable regardless of task name. Internal classification now only applies under "Cloud Platform Services" generic container. Added Dedicated Client Projects table. Fixed Banfi Istvan misclassification (58h Silver was showing as 54h, 31h IdomSoft was showing as 10h). |
