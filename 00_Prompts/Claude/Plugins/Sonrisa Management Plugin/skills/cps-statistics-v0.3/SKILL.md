---
name: cps-statistics-v0.3
description: >
  This skill should be used when the user asks to "process timesheets",
  "build statistics", "create activity report", "generate CPS stats",
  "havi statisztika", "activity report", "activityreport", "raport",
  "sontime report", or needs to produce the monthly CPS statistics
  workbooks from a raw Sontime activity export.
version: 0.3.0
id: 27897489-d657-4d75-92bb-d180ad62d87e
index_schema_version: 1
---

# CPS Monthly Statistics Processor (Phase 1)

Process a raw Sontime activity report into three output files for the CPS team.

## What This Does

Take a source file (`activityreport_YYYY_MM (N).xlsx` from Sontime/SharePoint) and produce:

1. **`activityreport_YYYY_MM_base.xlsx`** -- full workbook with 6 sheets + real Excel pivot tables (internal use)
2. **`activityreport_YYYY_MM_tam.xlsx`** -- CPS data only, without Team column (for Technical Account Managers)
3. **`MUB_YYYY_MM.md`** -- Monthly Update Brief (structured text for Phase 2 dashboard update)

## Before You Start -- Ask the User

1. **Which month?** If not clear from the request, ask.
2. **Which raw file?** Look for `activityreport_YYYY_MM (N).xlsx` in the raports folder. The `(N)` suffix varies. If multiple exist, ask which one.
3. **Which Example/template file?** Default is `activityreport_2026_02_Example.xlsx` but the user may provide a different one. Ask: "Should I use `activityreport_2026_02_Example.xlsx` as the template, or do you have a different one?"

## Plugin Source Folder

The plugin source lives at a user-accessible folder (typically under `Obsidian/.../Plugins/Sonrisa Management Plugin/`). This skill's reference files -- especially `references/mub-instructions.md` -- are the single source of truth for classification rules.

**When new tasks are classified during a run, the plugin source MUST be updated:**
- Update `references/mub-instructions.md` in the plugin source folder
- This ensures the next month's run already knows the new rules

**If the plugin source folder is not among the connected workspace folders:**
- Use `request_cowork_directory` to ask the user to grant access to the Plugins folder
- Say: "I need access to the plugin source folder to save updated classification rules. Can you add the folder where the Sonrisa Management Plugin lives?"
- Do NOT skip this step -- if you can't update the source, the learning is lost

## Reference Files

Before generating, read these reference files for the authoritative rules:

- **`references/build-process.md`** -- XML template assembly spec for _base.xlsx
- **`references/mub-instructions.md`** -- MUB classification rules, template, and aggregation logic (SINGLE SOURCE OF TRUTH)
- **Previous month's MUB** (if available in `raports/generated/`) -- for context on known projects

## Prerequisites

- Source file in the `raports/` folder (SharePoint CPS raports sync)
- Example/template file (contains pivot table XML structure, styles, team list)
- Required Python packages: `xlsxwriter` (for _tam), standard lib only for _base (zipfile, xml, zlib)
- Do NOT use `openpyxl` for reading the raw file (it fails on large Sontime exports with read_only mode). Use `zipfile` + `ElementTree` to parse the XML directly.

## Source Data Format

The raw Sontime export has:
- Rows 1-3: Title / blank rows (skip)
- Row 4: Headers
- Row 5+: Data rows

**11 Columns (A-K, no Team column):**

| Col | Letter | Content | Type |
|-----|--------|---------|------|
| 0 | A | User | string (FirstName LastName format!) |
| 1 | B | Project name | string (Sontime container) |
| 2 | C | Company name | string |
| 3 | D | Task issue ID | string |
| 4 | E | Task name | string (actual project/task) |
| 5 | F | Activity description | string |
| 6 | G | Activity date | Excel serial number |
| 7 | H | Start time | Excel serial number (may be empty) |
| 8 | I | End time | Excel serial number (may be empty) |
| 9 | J | Length | numeric, already in HOURS (not day fractions!) |
| 10 | K | Work type | "Billable work" / "Non-billable work" / "Non-work activity" |

**CRITICAL:** Sontime uses **FirstName LastName** format (e.g., "Alexandru Ceclan", "Balint Lajos Torok"), NOT Hungarian LastName FirstName. The CPS team member set must match this format.

## CPS Team (current, as of 2026-04)

```
Alexandru Ceclan, Zoltan Szanto, Alexander Poda,
Attila Kovacs, Zsolt Tornai, Balint Lajos Torok,
Mark-Adam Vaida, Marcell Kovacs, David Pap, Botond Gall,
Daniel Molnar,
Istvan Banfi (contractor), Andor Szabo (contractor), Ferenc Beder (part-time)
```

If the team composition changes, update this list AND the Example's Team sheet.

---

## Execution Flow

This is a TWO-PHASE process. Phase A parses and classifies. If there are "Other" items, you STOP and ask the user. Only after classification is complete and confirmed do you proceed to Phase B (generation).

### PHASE A: Parse and Classify

#### Step 1: Read reference files

Read `references/build-process.md` and `references/mub-instructions.md` before doing anything else. These contain the authoritative rules.

#### Step 2: Extract Example template

The Example xlsx may have a corrupted ZIP central directory (SharePoint sync artifact). Use manual `PK\x03\x04` header scanning + zlib decompression with error handling to extract all entries (~48).

#### Step 3: Parse raw source file

Use `zipfile.ZipFile` (standard) to read the raw file. Parse shared strings table, then iterate sheet1.xml rows. Map cells by column letter (A-K), not by index. Length (col J) is already in hours.

Filter CPS rows: any row where User (col A, stripped) is in the CPS team set.

#### Step 4: Classify hours (5-category system)

Apply classification rules from `references/mub-instructions.md` in this priority order:

1. **Sick + Paid leave:** Work type = "Non-work activity" AND Task name in {Paid leave, Sick leave}
2. **MVMI Availability:** Task name in {"MVMI OMNI ticket", "MVMI OMNI - general availability collector ticket"}
3. **Internal:** Task name in {Meeting, Megbeszeles, General Research, Internal Systems, Interviews, Learning, PM task, DevOps Guild activities, Workshop - business}
4. **Billable:** Work type = "Billable work" or "Non-billable work" AND task/project is in the known billable list
5. **Other:** Anything not matched above

Use `.strip()` on all task names (trailing spaces exist in Sontime data).

#### Step 5: Present classification review to user

**ALWAYS present this before generating files.** Show:

1. **Category totals:** Billable X, Internal Y, MVMI Z, Sick W, Other O = Total T
2. **Full unique task mapping table** -- every unique (task_name, project_name) pair and which category it was assigned to. This lets the user eyeball whether any task is miscategorized:

```
Classification Review:
| Task Name | Project | Category | Hours |
|-----------|---------|----------|-------|
| Meeting   | ...     | Internal | 45.00 |
| Bayer     | CPS Support | Billable | 32.00 |
| ...       | ...     | ...      | ...   |
```

3. **If "Other" items exist:** List each one explicitly and ASK the user where to put it. Use AskUserQuestion or direct chat. Do NOT proceed to Phase B until every item is classified. The "Other" category should be ZERO before generating.

4. **After user classifies "Other" items:** Update `references/mub-instructions.md` in the **plugin source folder** with the new rules (add to the appropriate category table, known billable list, or aggregation rules). This is how the system learns -- next month these tasks will be auto-classified.

   If the plugin source folder is not accessible, use `request_cowork_directory` to ask for access. Say: "I need to update the classification rules so these new tasks are remembered next month. Can you add the Plugins folder?"

5. **User confirms classification is correct** -> proceed to Phase B.

### PHASE B: Generate

#### Step 6: Apply aggregation rules

Map Sontime task names to MUB project names (see mub-instructions.md for full table):
- SIL-xxx -> Spinwheel
- SD-xxx -> Synlab
- Onriva:* -> Onriva
- SocialBud:* -> SocialBud
- Observer + sub-tasks -> Observer

#### Step 7: Generate _base.xlsx

See `references/build-process.md` for the complete XML template assembly specification.

Key points:
- Data sheet (sheet1): ALL rows from raw, with Team formula in col B
- CPS sheet (sheet2): CPS rows only, static "CPS" in col B, with CPSTable reference
- Team sheet (sheet3): Copy from Example
- Patch pivotCacheDefinition: source -> CPSTable, refreshOnLoad="1"
- Patch workbook.xml: update filter ranges
- Add table1.xml + sheet2 rels + update Content_Types
- Remove calcChain.xml
- Write as valid ZIP with deflate compression

#### Step 8: Generate _tam.xlsx

Simple xlsxwriter workbook:
- Single "CPS" sheet, 11 columns (no Team): User, Project name, Company name, Task issue ID, Task name, Activity description, Activity date, Start time, End time, Length, Work type
- Bold headers, date/time formats, autofilter, column widths

#### Step 9: Generate MUB

Follow the MUB template from `references/mub-instructions.md` EXACTLY. The MUB has these 7 sections:

1. **Header** -- period, generated date, source file
2. **Summary table** -- 5 categories + total, project count, team size, contractor count
3. **Project Hours Breakdown by Client** -- per project with company name, per-person detail, project total. Each project block MUST include a `**Dashboard:**` line showing the exact Client / Project name used in the T&M Raw sheet (see TASK_TO_DASH mapping in mub-instructions.md). Projects are ordered to match Dashboard T&M Raw order, NOT alphabetically.
4. **Team Member Hours by Client** -- per person showing all their projects with categories
5. **Hours Summary** -- 4 separate tables (Billable, Internal, MVMI Availability, Sick+Leave) each with per-person hours and category total
6. **Contractor Breakdowns** -- one section per contractor/part-time with level, position, all hours by project and category
7. **Category Verification** -- final cross-check table with Match: Yes/No

#### Step 10: Verify and save

- Verify: Billable + Internal + MVMI + Sick/Leave + Other = CPS Total (must match exactly)
- Save MUB to vault: `02_Areas/Sonrisa/CPS/Administration/Reports/MUB/MUB_YYYY_MM.md`
- Save _base.xlsx and _tam.xlsx locally (temp), then upload to SharePoint (see Step 11)
- Print summary with file sizes

#### Step 11: Upload to SharePoint (manual, document for user)

See `references/sharepoint-urls.md` for exact URLs.

---

## Critical Technical Details

- Use **inline strings** (`t="inlineStr"`) in generated XML to avoid shared string table dependency
- Write formulas directly in XML `<f>` tags (avoid openpyxl/xlsxwriter backslash escaping bug)
- Style indices from Example: `s="10"` = bold header, `s="3"` = date format, `s="5"` = time format
- Keep Example's styles.xml, sharedStrings.xml, theme, pivot table definitions, and pivot cache records intact
- Excel "repair" dialog may appear on first open due to stale pivot cache records -- this is expected, clicking "Yes" is safe
- Do NOT multiply Length values by 24 -- they are already in hours

## Output Naming Convention

- `activityreport_YYYY_MM_base.xlsx` -- full workbook (SharePoint upload)
- `activityreport_YYYY_MM_tam.xlsx` -- TAM extract (SharePoint upload)
- `MUB_YYYY_MM.md` -- Monthly Update Brief (vault: `02_Areas/Sonrisa/CPS/Administration/Reports/MUB/`)

Raw input location (vault): `02_Areas/Sonrisa/CPS/Administration/Reports/raw/activityreport_YYYY_MM.xlsx`
