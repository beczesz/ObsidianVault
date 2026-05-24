---
name: tig-review-v0.1
description: >
  This skill should be used when the user asks to "review TIG",
  "check TIG", "tig review", "istvan hours", "teljesitmenyigazolas",
  "Banfi Istvan", "verify contractor hours", "contractor review",
  "hora visszaigazolas", or needs to verify a contractor's monthly
  performance certificate against Sontime data and draft AM sign-off emails.
version: 0.1.0
id: 7f8cc376-0596-44fe-bfd0-6746d0434495
index_schema_version: 1
---

# TIG Review -- Contractor Hour Verification

Verify contractor (Banfi Istvan) monthly hours, cross-reference with Sontime statistics, and draft AM sign-off emails.

## What This Does

TIG = Teljesitmeny Igazolas (Certificate of Completion). Each month, the contractor uploads a TIG document. This skill:

1. Checks the TIG upload on SharePoint
2. Cross-references hours with the Sontime activity report (_base or raw)
3. Identifies which projects the contractor worked on and who the AM is
4. Drafts Hungarian confirmation emails to each AM
5. Tracks confirmations until TIG can be officially accepted

## Process Steps

### 1. Check TIG upload

Navigate to Istvan's TIG folder on SharePoint (see `references/links.md`) and verify the current month's TIG is uploaded. Check the service period matches the correct month -- past uploads have contained wrong months.

### 2. Cross-reference with Sontime data

Open the _base activity report for the same month. Filter for exact match `User == 'Istvan Banfi'` (careful: other team members may also have "Istvan" in their name -- always use exact full name match).

Extract per-project breakdown:
- Project name
- Total hours per project
- Grand total hours

Compare with TIG document totals. All numbers must match exactly.

### 3. Identify AMs per project

From the timesheet data, note which projects the contractor worked on. AM assignments vary monthly. Check with the user if AM mapping is unclear.

Known project name mapping (TIG vs Sontime names):

| TIG Name | Sontime Name |
|----------|-------------|
| CPS - Architektura tervezes | Cloud Platform Services |
| Idomsoft - architektura tervezes | Idomsoft - Legacy kolteoztetes |
| Silver 3.0 | Silver 3.0 |
| Sonrisa Presales | Sonrisa Presales |

### 4. Draft confirmation emails

Draft one email per project to the responsible AM. Email is in Hungarian, short and to the point.

**Recipients per email:**
- **To:** AM for the project
- **CC:** PM (if applicable) + Finance

**Key contacts (update as needed):**
- Nagy Sandor (PM): nagy.sandor.pm@sonrisa.hu
- Sajo Peter (AM): peter.sajo@sonrisa.hu
- Szellar Tamara (Finance): szellar.tamara@sonrisa.hu

See `references/email-template.md` for the exact template.

### 5. Create Gmail draft

Use the Gmail MCP to create a draft for each project email. The user reviews and sends manually.

### 6. Track confirmations

After sending, wait for all AMs to confirm. Once all confirmations are received, officially accept the TIG.

## Important Notes

- AMs vary monthly depending on project assignments
- The Sontime timesheet is the **source of truth** for raw numbers
- Always verify TIG service period dates match the intended month
- If hours don't match, flag the discrepancy to the user before drafting emails
