# CPS Monthly Statistics Process

**Owner:** Szabolcs
**Frequency:** Monthly
**Source:** Activity report from Sontime (SharePoint raports folder)
**Goal:** Prepare statistics with pivot tables, verify contractor hours, get AM sign-off on TIGs
**Template:** `activityreport_2026_02_Example.xlsx` (contains real Excel pivot tables + pivot cache)
**Outputs:** Two files per month:
- `activityreport_YYYY_MM_base.xlsx` -- full workbook with 6 sheets + pivot tables (internal use)
- `activityreport_YYYY_MM_tam.xlsx` -- CPS data only, without Team column (for Technical Account Managers)

---

## Overview

The process takes a raw Sontime activity report (`activityreport_YYYY_MM (N).xlsx`) and produces a complete statistics workbook with 6 sheets: Data, CPS, Team, Sheet2, Sheet1, Sheet3. The pivot tables (Sheet1/2/3) are real interactive Excel pivots sourced from a CPSTable on the CPS sheet.

**Strategy:** Use the Example file as a template (it has the pivot table XML structure). Extract all its ZIP entries, replace the 3 data worksheets with fresh month data, create a CPSTable for dynamic pivot sourcing, patch the pivot cache, and rebuild as a valid xlsx.

---

## Step 1: Identify the source file

- Source file pattern: `activityreport_YYYY_MM (N).xlsx` (downloaded from SharePoint/Sontime)
- Location: `raports/` folder
- Two output files will be generated:
  - `activityreport_YYYY_MM_base.xlsx` -- full workbook (replaces old `_Claude` naming)
  - `activityreport_YYYY_MM_tam.xlsx` -- TAM extract

---

## Step 2: Extract the Example template

- The Example file (`activityreport_2026_02_Example.xlsx`) may appear "corrupted" (missing ZIP central directory due to SharePoint sync) but all local file entries are intact.
- Extract all ZIP entries manually using `PK\x03\x04` header scanning + zlib decompression.
- This gives us ~31 entries including:
  - `xl/pivotTables/pivotTable1-5.xml` (5 real pivot table definitions)
  - `xl/pivotCache/pivotCacheDefinition1.xml` and `pivotCacheRecords1.xml`
  - `xl/styles.xml`, `xl/sharedStrings.xml`, `xl/theme/theme1.xml`
  - `xl/workbook.xml`, `[Content_Types].xml`, relationship files
- **Keep all of these intact** -- only replace the 3 data worksheet XMLs.

---

## Step 3: Read source data and Team list

- Read the source file's Sheet1 with pandas: `pd.read_excel(..., header=None, usecols=range(11))`
  - Structure: rows 0-2 = title/blank, row 3 = headers, rows 4+ = data
  - 11 columns: User(0), Project(1), Company(2), TaskID(3), TaskName(4), Description(5), Date(6), Start(7), End(8), Length(9), WorkType(10)
- Read Team names from the Example's Team sheet (sheet3.xml) using the shared strings table
  - Parse shared strings from `xl/sharedStrings.xml`
  - Parse Team sheet XML, resolve string indices to actual names
  - Build `team_names` set (~17 members)
- Identify CPS rows: any data row where User is in `team_names`

---

## Step 4: Generate Data sheet XML (sheet1.xml)

- Use **inline strings** (`t="inlineStr"`) instead of shared string references to avoid dependency on the Example's shared strings table
- Structure:
  - Row 1: "Activity Report" title
  - Row 4: Headers with style `s="10"` (bold in Example's stylesheet)
    - `User | Team | Project name | Company name | Task issue ID | Task name | Activity description | Activity date | Start time | End time | Length | Work type`
  - Row 5+: Data with column B as formula: `IF(COUNTIF(Team!$A$2:$A$18,A{row})>0,"CPS","")`
    - Write formula directly in XML: `<c r="B5"><f>IF(COUNTIF(Team!$A$2:$A$18,A5)&gt;0,"CPS","")</f></c>`
    - This avoids the `\!` backslash bug that openpyxl/xlsxwriter introduce
  - Date cells use style `s="3"` (date format), time cells use style `s="5"` (time format)
- Autofilter: `<autoFilter ref="A4:L{last_row}"/>`
- `excel_date()` function: convert Python datetime to Excel serial number (days since 1899-12-30)

---

## Step 5: Generate CPS sheet XML (sheet2.xml) with Excel Table

- Row 1: Same headers as Data row 4 (with `s="10"` style)
- Row 2+: Only CPS team member rows
  - Column B = static "CPS" value (not formula)
  - Same date/time formatting as Data sheet
- **Add `<tableParts>` reference** at end of worksheet XML:
  ```xml
  <tableParts count="1"><tablePart r:id="rId1"/></tableParts>
  ```
- **Create Table definition** (`xl/tables/table1.xml`):
  - Table name: `CPSTable`
  - Range: `A1:L{cps_last}` (dynamic, based on actual row count)
  - 12 columns matching the headers
  - Style: `TableStyleMedium2` with row stripes
- **Create relationship** (`xl/worksheets/_rels/sheet2.xml.rels`):
  - `rId1` -> `../tables/table1.xml` (table relationship type)
- **Update `[Content_Types].xml`**: Add table content type override

---

## Step 6: Generate Team sheet XML (sheet3.xml)

- Copy the Team data from the Example (same team list)
- Simple inline string cells, columns A-E: Name, Site, Status, Level, Position
- ~18 rows (1 header + 17 members)
- Update if team composition changes

---

## Step 7: Patch pivot cache and workbook

### Pivot cache (`xl/pivotCache/pivotCacheDefinition1.xml`):
- **Change source to Table:** Replace `<worksheetSource ref="A1:L730" sheet="CPS"/>` with `<worksheetSource name="CPSTable" sheet="CPS"/>` -- this makes the range dynamic (always all rows)
- **Add auto-refresh:** Add `refreshOnLoad="1"` attribute to `<pivotCacheDefinition>` tag -- pivots refresh automatically when file is opened
- **Update record count:** Change `recordCount="729"` to actual CPS row count

### Workbook (`xl/workbook.xml`):
- Update `_xlnm._FilterDatabase` defined names:
  - CPS filter: `CPS!$A$1:$L${cps_last}`
  - Data filter: `Data!$A$4:$L${last_data_row}`

---

## Step 8: Build final xlsx

- Start with all Example entries (dict copy)
- Replace these entries:
  - `xl/worksheets/sheet1.xml` (Data) -- generated in Step 4
  - `xl/worksheets/sheet2.xml` (CPS) -- generated in Step 5
  - `xl/worksheets/sheet3.xml` (Team) -- generated in Step 6
  - `xl/pivotCache/pivotCacheDefinition1.xml` -- patched in Step 7
  - `xl/workbook.xml` -- patched in Step 7
  - `[Content_Types].xml` -- updated in Step 5
- Add new entries:
  - `xl/tables/table1.xml` -- created in Step 5
  - `xl/worksheets/_rels/sheet2.xml.rels` -- created in Step 5
- Write as valid ZIP with `zipfile.ZIP_DEFLATED`
- **Do NOT replace:** styles.xml, sharedStrings.xml, theme, pivot table definitions, pivot cache records (these all come from the Example and are refreshed by Excel on open)

---

## Technical Notes

- **Inline strings vs shared strings:** We use inline strings in generated sheet XMLs to avoid needing to rebuild the shared strings table. This is slightly less compact but fully compatible.
- **Style indices from Example:** `s="10"` = bold header, `s="3"` = date format, `s="5"` = time format. These reference the Example's `xl/styles.xml` which we keep intact.
- **Pivot tables auto-refresh:** With `refreshOnLoad="1"`, Excel rebuilds the pivot cache from the CPSTable when opening. The stale February cache records are replaced automatically.
- **Excel "repair" dialog:** May still appear due to stale pivot cache records not matching the new data. Clicking "Yes" is safe -- Excel just rebuilds the cache. This is expected behavior.
- **Formula in XML:** Write formulas directly in XML `<f>` tags to avoid the backslash escaping bug. Use `&gt;` for `>` in formulas (XML entity encoding).
- **Sheet order in workbook:** Data(sheet1), CPS(sheet2), Team(sheet3), Sheet2(sheet4), Sheet1(sheet5), Sheet3(sheet6)

---

## File Structure (final outputs)

### _base file (full workbook with pivots)
```
activityreport_YYYY_MM_base.xlsx (ZIP)
├── [Content_Types].xml          (updated: +table content type)
├── _rels/.rels
├── customXml/...
├── xl/
│   ├── workbook.xml             (updated: filter ranges)
│   ├── styles.xml               (from Example, unchanged)
│   ├── sharedStrings.xml        (from Example, unchanged)
│   ├── theme/theme1.xml         (from Example, unchanged)
│   ├── _rels/workbook.xml.rels
│   ├── worksheets/
│   │   ├── sheet1.xml           (GENERATED: Data sheet)
│   │   ├── sheet2.xml           (GENERATED: CPS sheet + Table ref)
│   │   ├── sheet3.xml           (GENERATED: Team sheet)
│   │   ├── sheet4.xml           (from Example: Sheet2 pivot output)
│   │   ├── sheet5.xml           (from Example: Sheet1 pivot output)
│   │   ├── sheet6.xml           (from Example: Sheet3 pivot output)
│   │   └── _rels/
│   │       ├── sheet2.xml.rels  (NEW: table relationship)
│   │       ├── sheet4.xml.rels  (from Example: pivot refs)
│   │       ├── sheet5.xml.rels  (from Example: pivot refs)
│   │       └── sheet6.xml.rels  (from Example: pivot refs)
│   ├── tables/
│   │   └── table1.xml           (NEW: CPSTable definition)
│   ├── pivotCache/
│   │   ├── pivotCacheDefinition1.xml  (PATCHED: CPSTable source + refreshOnLoad)
│   │   └── pivotCacheRecords1.xml     (from Example, stale -- refreshed on open)
│   └── pivotTables/
│       ├── pivotTable1-5.xml    (from Example, unchanged)
│       └── _rels/...            (from Example, unchanged)
```

---

## Step 9: Generate TAM file

The TAM (Technical Account Manager) file is a simple single-sheet extract for account managers to create their own reports.

- **Source:** The same CPS rows collected in Step 3
- **Content:** CPS sheet data WITHOUT column B (Team)
- **Columns (11):** User, Project name, Company name, Task issue ID, Task name, Activity description, Activity date, Start time, End time, Length, Work type
- **Row 1:** Headers with bold formatting
- **Row 2+:** CPS data rows with date/time formatting
- **Autofilter** on the header row
- **Output:** `activityreport_YYYY_MM_tam.xlsx`
- **Method:** Simple xlsxwriter workbook (no template needed, no pivot tables)
- **Column widths:** User(20), Project(30), Company(20), Description(50), Date(14)

### _tam file (TAM extract)
```
activityreport_YYYY_MM_tam.xlsx
└── Sheet1 "CPS"
    ├── Row 1: Headers (bold) -- 11 columns (no Team column)
    ├── Row 2+: CPS team data
    └── Autofilter on A1:K{last_row}
```

---

## Step 10: Upload to SharePoint

Two separate uploads via browser (Chrome):

### _base file
- **Destination:** SharePoint Sales site
- **URL:** `https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/Forms/AllItems.aspx?id=%2Fsites%2Fsales%2FMegosztott%20dokumentumok%2FGeneral%2FPlanning%2FServices%2FCloud%20Platform%20Services%2Fraports&viewid=dfd2979e%2D7b28%2D49ac%2D9be0%2Dc493d63eeabc`
- **Path:** Sales > General > Planning > Services > Cloud Platform Services > raports

### _tam file
- **Destination:** SharePoint Cloud Guild site
- **URL:** `https://sonrisakft.sharepoint.com/sites/cloudguild/Megosztott%20dokumentumok/Forms/AllItems.aspx?id=%2Fsites%2Fcloudguild%2FMegosztott%20dokumentumok%2FTechnical%2FRaport%2FRaw%20timesheets&viewid=27bbc06a%2D762c%2D4e13%2D8c63%2D1f0cf00cde83`
- **Path:** Cloud Guild > Technical > Raport > Raw timesheets

### Upload method
- Navigate to each SharePoint folder in Chrome
- Use the Upload button or drag-and-drop
- Verify the file appears in the folder after upload

---

## Source Data Reference

- **Source columns (Sheet1, before processing):** User, Project name, Company name, Task issue ID, Task name, Activity description, Activity date, Start time, End time, Length, Work type
- **Data sheet columns (after processing):** Same + inserted "Team" as column B
- **TAM sheet columns (no Team):** User, Project name, Company name, Task issue ID, Task name, Activity description, Activity date, Start time, End time, Length, Work type
- **Work types:** "Billable work", "Non-billable work", "Non-work activity"
- **Team sheet columns:** Name, Site, Status, Level, Position
