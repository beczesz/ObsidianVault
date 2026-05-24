---
description: Sage LEARNING EDIT — aktív learning szövegének editálása. Confirmation kötelező.
id: 0496c150-3590-4850-b22b-c98dcc1c3376
index_schema_version: 1
---

A felhasználó egy aktív learning szövegét akarja módosítani.

**$ARGUMENTS** — kötelező: a learning slug-ja

**Tennivaló:**

1. Keresd: `learnings/active/<slug>.md`
2. Olvasd be teljes tartalom
3. Hívd `subagent_type: sage`
4. Paraméterek:
   - `mode: learning-ops`
   - `op: edit`
   - `target: learnings/active/<slug>.md`
5. Sage javasol diffet, NEM ír
6. **Confirmation kötelező** ("igen" / "--confirm")
7. Csak akkor írj
8. Frontmatter update: `note_revision++` (ha van ilyen mező) vagy add `last_edited_at`
9. Append `_journal`: `event: learning-edit`
