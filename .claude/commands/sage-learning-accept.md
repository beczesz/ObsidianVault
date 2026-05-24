---
description: Sage LEARNING ACCEPT — proposed learning → active promote. Confirmation kötelező.
id: 337bef43-f6e0-49ea-867b-40b20b047c6d
index_schema_version: 1
---

A felhasználó egy learning-proposal elfogadását kéri.

**$ARGUMENTS** — kötelező: a learning slug-ja (pl. `2026-05-26_voice-fillers`)

**Tennivaló:**

1. Keresd: `00_Prompts/BDOS/agents/sage/learnings/proposals/<slug>.md`
2. Ha nincs → error: "Nincs ilyen pending proposal."
3. Mutasd a tartalmát + kérdezz: "Elfogadod a learning-et? Bekerül a következő Sage-futás promptjába."
4. Confirmation után:
   - Frontmatter update: `status: active`, `confirmed_at: <ISO ts>`
   - Mozgasd: `proposals/<slug>.md` → `active/<slug>.md`
   - Update: `learnings/00_INDEX.md`
   - Append `02_Areas/Personal Growth/Ideas/_journal/<YYYY-MM>.md`: `event: learning-accept`
