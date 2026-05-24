# Sonrisa Management Plugin

Management workflows for the Sonrisa CPS team.

## Skills

### cps-statistics-v0.1

Monthly timesheet statistics processor. Takes a raw Sontime activity report and produces two output files:
- `_base.xlsx` -- full workbook with pivot tables (internal)
- `_tam.xlsx` -- CPS-only extract for Technical Account Managers

**Trigger phrases:** "process timesheets", "build statistics", "activity report", "havi statisztika", "raport"

### cps-dashboard-update-v0.1

Interactive dashboard update workflow (Phase 2). Works across two environments:
- **Cowork:** reads Phase 1 outputs, compares with previous month, generates a Monthly Update Brief
- **Claude for Excel:** receives the brief, walks through projects one by one, writes cells directly

Features: project-by-project ACK workflow, state tracking (PREFILLED/ACK/REVIEW/ADJUSTED/SKIP), formula preservation, resumable sessions.

**Trigger phrases:** "update dashboard", "Phase 2", "dashboard update", "T&M Raw update", "havi dashboard", "projekt frissites"

### tig-review-v0.1

Contractor TIG (Teljesitmeny Igazolas) verification workflow. Cross-references contractor hours with Sontime data and drafts AM sign-off emails in Hungarian.

**Trigger phrases:** "review TIG", "check TIG", "istvan hours", "contractor review"

## Setup

No special configuration needed. The plugin uses:
- Python (pandas, xlsxwriter) for statistics processing
- Gmail MCP for draft creation
- Chrome MCP for SharePoint navigation (optional)
- Claude for Excel add-in for dashboard editing (Phase 2b)

## Version History

- **0.2.0** -- Added cps-dashboard-update-v0.1 (Phase 2 dashboard update with Cowork + Claude for Excel split architecture)
- **0.1.0** -- Initial release with cps-statistics-v0.1 and tig-review-v0.1
