---
title: "Build Process -- Technical Specification"
date: 2026-04-22
author: Becze Szabolcs
status: active
description: "Technical specification for building an Excel activity report from Sontime export files, detailing data extraction, sheet generation, pivot table patching, and final ZIP assembly for data and team management sheets."
description_source: auto
description_hash: a1741cbeea7e9fb8
id: 91061b58-0827-4dc9-bc37-0d983f9fcfbe
index_schema_version: 1
bdos_index: true
---
# Build Process -- Technical Specification

## Source Data Structure

Source file: `activityreport_YYYY_MM (N).xlsx` (Sontime export)

| Row | Content |
|-----|---------|
| 0-2 | Title / blank rows |
| 3   | Headers |
| 4+  | Data rows |

**11 Columns (A-K, no Team column):**

| Col | Letter | Content | Notes |
|-----|--------|---------|-------|
| 0 | A | User | FirstName LastName format (e.g., "Alexandru Ceclan") |
| 1 | B | Project name | Sontime container (e.g., "Cloud Platform Services") |
| 2 | C | Company name | Client company |
| 3 | D | Task issue ID | Ticket number |
| 4 | E | Task name | Actual project/task |
| 5 | F | Activity description | Free text |
| 6 | G | Activity date | Excel serial date number |
| 7 | H | Start time | Excel serial (may be empty) |
| 8 | I | End time | Excel serial (may be empty) |
| 9 | J | Length | ALREADY IN HOURS (do NOT multiply by 24!) |
| 10 | K | Work type | "Billable work" / "Non-billable work" / "Non-work activity" |

**CRITICAL:** Use `zipfile.ZipFile` + `ElementTree` to parse raw file. Do NOT use `openpyxl` read_only mode (it reports max_row=4 on large Sontime exports). Map cells by column letter (A-K), not by numeric index.

**CRITICAL:** Names in Sontime use FirstName LastName format, NOT Hungarian LastName FirstName.

---

## Example Template Extraction

The Example file (`activityreport_2026_02_Example.xlsx`) may appear corrupted (missing ZIP central directory due to SharePoint sync) but all local file entries are intact.

### Manual ZIP extraction algorithm

```python
def extract_all(data):
    entries = {}
    pos = 0
    while True:
        idx = data.find(b'PK\x03\x04', pos)
        if idx == -1:
            break
        comp_method = struct.unpack_from('<H', data, idx + 8)[0]
        comp_size = struct.unpack_from('<I', data, idx + 18)[0]
        fname_len = struct.unpack_from('<H', data, idx + 26)[0]
        extra_len = struct.unpack_from('<H', data, idx + 28)[0]
        fname = data[idx+30:idx+30+fname_len].decode('utf-8')
        start = idx + 30 + fname_len + extra_len
        comp_data = data[start:start + comp_size]
        if comp_method == 8:
            content = zlib.decompress(comp_data, -15)
        elif comp_method == 0:
            content = comp_data
        entries[fname] = content
        pos = idx + 4
    return entries
```

This yields ~31 entries including pivot tables, pivot cache, styles, shared strings, theme, and 6 worksheet XMLs.

---

## Sheet Generation

### Data sheet (sheet1.xml)

- Row 1: "Activity Report" title
- Row 4: Headers with style `s="10"` (bold)
  - `User | Team | Project name | Company name | Task issue ID | Task name | Activity description | Activity date | Start time | End time | Length | Work type`
- Row 5+: Data with column B as formula:
  ```xml
  <c r="B5"><f>IF(COUNTIF(Team!$A$2:$A$18,A5)&gt;0,"CPS","")</f></c>
  ```
  - Use `&gt;` for `>` in formulas (XML entity encoding)
- Date cells: `s="3"`, Time cells: `s="5"`
- Autofilter: `<autoFilter ref="A4:L{last_row}"/>`

### CPS sheet (sheet2.xml) + Excel Table

- Row 1: Headers with `s="10"`
- Row 2+: CPS rows only, column B = static "CPS"
- End of worksheet XML:
  ```xml
  <tableParts count="1"><tablePart r:id="rId1"/></tableParts>
  ```

**CPSTable definition** (`xl/tables/table1.xml`):
```xml
<table id="1" name="CPSTable" displayName="CPSTable"
       ref="A1:L{cps_last}" totalsRowShown="0">
  <autoFilter ref="A1:L{cps_last}"/>
  <tableColumns count="12">
    <!-- 12 columns matching headers -->
  </tableColumns>
  <tableStyleInfo name="TableStyleMedium2" showRowStripes="1"/>
</table>
```

**Relationship** (`xl/worksheets/_rels/sheet2.xml.rels`):
```xml
<Relationship Id="rId1"
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/table"
  Target="../tables/table1.xml"/>
```

**Content Types** -- add to `[Content_Types].xml`:
```xml
<Override PartName="/xl/tables/table1.xml"
  ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.table+xml"/>
```

### Team sheet (sheet3.xml)

- Copy from Example template (same team list)
- Columns A-E: Name, Site, Status, Level, Position
- ~18 rows (1 header + 17 members)
- Update if team composition changes

---

## Pivot Cache Patching

### pivotCacheDefinition1.xml

1. Change source to Table:
   ```xml
   <worksheetSource name="CPSTable" sheet="CPS"/>
   ```
   (replaces `<worksheetSource ref="A1:L730" sheet="CPS"/>`)

2. Add auto-refresh:
   ```xml
   <pivotCacheDefinition refreshOnLoad="1" ...>
   ```

3. Update record count to actual CPS row count

### workbook.xml

Update `_xlnm._FilterDatabase` defined names:
- CPS filter: `CPS!$A$1:$L${cps_last}`
- Data filter: `Data!$A$4:$L${last_data_row}`

---

## Final Assembly (_base)

Start with all Example entries (dict copy), then replace/add:

**Replace:**
- `xl/worksheets/sheet1.xml` (Data)
- `xl/worksheets/sheet2.xml` (CPS)
- `xl/worksheets/sheet3.xml` (Team)
- `xl/pivotCache/pivotCacheDefinition1.xml`
- `xl/workbook.xml`
- `[Content_Types].xml`

**Add new:**
- `xl/tables/table1.xml`
- `xl/worksheets/_rels/sheet2.xml.rels`

**Do NOT replace:** styles.xml, sharedStrings.xml, theme, pivot table definitions (pivotTable1-5.xml), pivot cache records

Write as valid ZIP with `zipfile.ZIP_DEFLATED`.

---

## TAM File (_tam)

Simple xlsxwriter workbook:
- Single sheet named "CPS"
- 11 columns (no Team): User, Project name, Company name, Task issue ID, Task name, Activity description, Activity date, Start time, End time, Length, Work type
- Row 0: Bold headers
- Row 1+: CPS data rows
- Date format: `yyyy-mm-dd`, Time format: `hh:mm`
- Column widths: User(20), Project(30), Company(20), Description(50), Date(14)
- Autofilter on `A1:K{last_row}`

---

## Excel Date Conversion

```python
def excel_date(dt):
    epoch = datetime(1899, 12, 30)
    delta = dt - epoch
    return delta.days + delta.seconds / 86400.0
```

---

## Helper: Cell XML Generation

```python
def make_cell_xml(ref, value, style=None):
    s_attr = f' s="{style}"' if style else ''
    if isinstance(value, str):
        return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape(value)}</t></is></c>'
    elif isinstance(value, datetime):
        return f'<c r="{ref}"{s_attr}><v>{excel_date(value)}</v></c>'
    elif isinstance(value, (int, float)):
        return f'<c r="{ref}"{s_attr}><v>{value}</v></c>'
    else:
        return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape(str(value))}</t></is></c>'
```

---

## File Structure (_base output)

```
activityreport_YYYY_MM_base.xlsx (ZIP)
├── [Content_Types].xml          (updated: +table content type)
├── _rels/.rels
├── customXml/...
├── xl/
│   ├── workbook.xml             (updated: filter ranges)
│   ├── styles.xml               (from Example, unchanged)
│   ├── sharedStrings.xml        (from Example, unchanged)
│   ├── theme/theme1.xml
│   ├── worksheets/
│   │   ├── sheet1.xml           (GENERATED: Data)
│   │   ├── sheet2.xml           (GENERATED: CPS + Table ref)
│   │   ├