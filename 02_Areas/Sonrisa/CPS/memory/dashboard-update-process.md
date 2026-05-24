# Phase 2 -- Dashboard Update Process

**Owner:** Szabolcs
**Frequency:** Monthly (after Phase 1 statistics processing)
**Single source of truth:** `CPS\Administration\CPS Monthly Process v0.1.md`
**Target:** CPS - Dashboard - v2.xlsx (SharePoint)

---

## Architecture

MUB = DATA (current month only), Skill = LOGIC (+ comparison with dashboard history).

Phase 1 (Cowork) generates the Monthly Update Brief (MUB) as its 3rd output alongside _base and _tam. The MUB is a textual representation of the pivot table: which project, who worked, how many hours, at what rate. No previous month comparison -- the MUB only contains the current month.

Phase 2 runs in Claude for Excel. The user pastes the MUB into the chat, and the `sonrisa-cps-dashboard-update` skill drives the project-by-project update loop. The skill reads the dashboard (which has 1.5+ years of history) and handles all comparison logic itself.

```
Phase 1 output: MUB_YYYY_MM.md     +   Skill: sonrisa-cps-dashboard-update
(the DATA - current month)              (the LOGIC - structure + comparison)
        |                                       |
        v                                       v
        Claude for Excel (dashboard open in browser)
        -> Reads previous months from dashboard
        -> Per project: compare, announce, ACK, write, verify, ACK
```

**Why Claude for Excel?** openpyxl does full-file replacement, which conflicts with Excel Online's browser lock (see `memory/sharepoint-sync-issue.md`). Claude for Excel edits cells natively through the Office add-in -- no sync issues.

---

## Prerequisites

- Phase 1 complete: `activityreport_YYYY_MM_base.xlsx` and `_tam.xlsx` generated
- MUB generated: `MUB_YYYY_MM.md`
- Dashboard file on SharePoint: `CPS - Dashboard - v2.xlsx`
- Dashboard open in Excel Online (browser) with Claude for Excel add-in active
- `sonrisa-cps-dashboard-update` skill uploaded in Claude settings
- Desktop Excel NOT open on the same file

---

## End-to-End Workflow

### Brief Generation (part of Phase 1, in Cowork)

1. User says "process timesheets" in Cowork
2. Cowork processes _base.xlsx, builds pivot tables
3. Cowork reads the pivot table and converts to structured markdown (MUB)
4. MUB contains: header (period, total hours, project count) + one block per project (person table with hours/rates)
5. No comparison with previous months -- that's the skill's job

### Dashboard Writing (Phase 2, in Claude for Excel)

1. User opens dashboard in Excel Online, opens Claude for Excel sidebar
2. User pastes the MUB into the chat
3. Skill reads the MUB and parses project blocks
4. Skill reads previous month's T&M Raw from the dashboard for comparison
5. For each project in the MUB:
   a. Skill compares with previous month (detects rate changes, new/dropped people, hour anomalies)
   b. Claude announces: "Next: [Project]. Adding [N] rows. [any comparison notes]. Ready?"
   c. User ACKs
   d. Claude writes rows with Status = PREFILLED
   e. User sees changes immediately in the spreadsheet
   f. User verifies and ACKs -> Claude updates Status to ACK
   g. Move to next project
6. After all MUB projects: skill checks for projects that were active last month but missing from MUB
7. Service Income, PSIC, EDC, Team (if applicable)
8. Final verification: check dashboard summary sheets for correct totals

### Sync Back (automatic)

After Claude for Excel writes to the dashboard, OneDrive syncs the changes back to the local copy.

---

## State Tracking (T&M Raw columns AC-AD)

Column AC = `Status`, Column AD = `Notes`

| State | Meaning |
|-------|---------|
| `PREFILLED` | Claude added these rows, not yet reviewed by Szabolcs |
| `ACK` | Reviewed and confirmed by Szabolcs |
| `REVIEW` | Something unclear -- needs discussion |
| `ADJUSTED` | Was ACK'd but then manually corrected by Szabolcs |
| `SKIP` | Intentionally excluded this month |

**Notes column (AD):** Free-text context set by the skill based on comparison. Examples: "rate changed from 280 to 310", "new on this project", "hours up significantly from 80 to 160"

**Resumability:** The state in column AC allows any session to pick up where the last one left off.

---

## Step 1: Update T&M Raw

### What it is
One row per person-per-project-per-month.

### Column mapping (A-AD)

See skill reference: `sonrisa-cps-dashboard-update-v0.1/references/column-map.md`

**Manual input columns (A-Q):** Year, Month, Date ID, #Month, Client, Project, Type, Name, Emp Status, Seniority, Hours, Suggested Rate, Daily Rate, Rate (formula), Fixed, Is Billable, Discount

**Formula columns (R-X):** Value, Invoiced, TP, Cost Share, Normalized Profit, Margin, Project copy

**State columns (AC-AD):** Status, Notes

### Process flow (in Cowork, generating the MUB)

1. **Read new month's _base pivot** -- get all person-project-hours for month M
2. **Convert to structured text** -- one block per project, person table with hours/rates
3. **No comparison** -- MUB is pure current month data

### Process flow (in Claude for Excel, writing the rows)

1. Receive MUB via chat paste
2. Read previous month's T&M Raw from dashboard (for comparison)
3. Find last used row in T&M Raw
4. For each project:
   a. Compare with previous month (rate changes, new/dropped people, anomalies)
   b. Announce with comparison notes and wait for ACK
   c. Write rows: values in A-Q from MUB, formulas in C/N/R-X (copy from row above), PREFILLED in AC, comparison notes in AD
5. After user verifies, update AC to ACK
6. After all projects: report any projects missing vs last month
7. Continue to next step (Service Income, etc.)

### End-of-step sanity check
- Compare total hours: MUB total vs sum of T&M Raw new rows
- Compare project list: any project in MUB not covered?

---

## Step 2: Update Service Income

One row per client-project-per-month for invoiced revenue. For continuing projects: copy previous month's row, update Year/Month. MUB includes a Service Income section if there are new contracts or price changes.

---

## Step 3: Update Actual PSIC (if applicable)

Support overtime, phone service, availability payments. Only when included in MUB.

---

## Step 4: Update Planned EDC (if applicable)

Banfi Istvan's monthly contractor fee. Only when included in MUB.

---

## Step 5: Update CPS Team (if applicable)

Monthly team composition snapshot. Only when team changes are noted in MUB.

---

## Step 6: Final Verification

1. Check BU Dash1 for correct revenue/costs
2. Check CPS Dash V2 for contract counts
3. Check BU Dash2 for per-project breakdown
4. Scan for #REF, #N/A, or obviously wrong numbers
5. Mark any remaining PREFILLED rows as ACK or flag for follow-up

---

## File Locations

- **Dashboard (SharePoint):** Sales > General > Planning > Services > Cloud Platform Services
- **Dashboard (local sync):** `C:\Users\EvoComputers\Downloads\Work\Sonrisa\CPS\New folder\Sonrisa Kft\sales - Cloud Platform Services\CPS - Dashboard - v2.xlsx`
- **Phase 1 outputs:** `C:\Users\EvoComputers\Downloads\Work\Sonrisa\CPS\raports\activityreport_YYYY_MM_base.xlsx`
- **MUB:** `CPS\Administration\MUB_YYYY_MM.md`
- **Skill:** `00_Prompts\Claude\Skills\sonrisa-cps-dashboard-update-v0.1\`
- **Brief template:** `sonrisa-cps-dashboard-update-v0.1/references/brief-template.md`

---

## Formula Templates (for new T&M Raw rows)

See skill reference: `sonrisa-cps-dashboard-update-v0.1/references/formula-templates.md`

Key formulas at row R:

```
C{R}: =A{R} & " " & CHOOSE(B{R}, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
N{R}: =IF(K{R} = 0, 0, M{R} / 8)
R{R}: =K{R}*N{R}+O{R}
S{R}: =IF(Q{R} = "", "", IF(Q{R} > 0, (1 - Q{R}) * IF(P{R} = "Billable", IF(O{R} > 0, O{R}, K{R} * N{R}), 0), IF(P{R} = "Billable", IF(O{R} > 0, O{R}, K{R} * N{R}), 0)))
T{R}: =IF(OR(I{R} = "", J{R} = ""), "", -VLOOKUP("DevOps",'Transfer Prices'!$A$12:$J$18,RIGHT($J{R},1)+1,FALSE))
U{R}: =IF(K{R}<>"",T{R}/Utils!$B$14 * K{R},T{R})
V{R}: =N{R}*Utils!$B$14+T{R}
W{R}: =IF(N{R}<>0,V{R}/(N{R}*Utils!$B$14),"NA")
X{R}: =F{R}
```
