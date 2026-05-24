---
description: Sage LEARNING RETIRE — aktív learning → retired manuálisan. Confirmation kötelező.
id: 4853955a-ca03-43a0-a65e-6af169412538
index_schema_version: 1
---

A felhasználó egy aktív tanulság visszavonását kéri.

**$ARGUMENTS** — kötelező: a learning slug-ja + opcionális `--reason "..."`

**Tennivaló:**

1. Parse slug + reason (opcionális)
2. Keresd: `learnings/active/<slug>.md`
3. Mutasd a tartalmat — kérdezz: "Visszavonod ezt az aktív tanulságot? A következő Sage-futások már nem alkalmazzák."
4. Confirmation után:
   - Frontmatter: `status: retired`, `retired_at`, `retired_reason` (default: "manual_retire")
   - Mozgasd: `active/` → `retired/`
   - Update index
   - Append `_journal`: `event: learning-retire`
