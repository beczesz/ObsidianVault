---
description: Sage INDEX mode — 00_INDEX.md regenerálása az Ideas/ mappában. Megerősítés nélkül.
id: fa936cac-b16e-431e-9293-74e7eac2d9c5
index_schema_version: 1
---

A felhasználó az Ideas index frissítését kéri.

**Tennivaló:**

1. Hívd `subagent_type: sage`
2. Paraméterek:
   - `mode: index`
   - `target: 02_Areas/Personal Growth/Ideas/00_INDEX.md`
3. Sage:
   - Glob: `Ideas/thoughts/*.md`, `Ideas/atomic/*.md`, `Ideas/_inbox/**/*.md`
   - Kategória szerint csoportosít (frontmatter `category` alapján)
   - Obsidian wikilinkekkel listáz: `[[thoughts/...]]`, `[[atomic/...]]`
   - Inbox-szekció külön (uncertain, atomic_proposals)
4. Visszaad: hány note kategóriánként, melyek a top kategóriák
