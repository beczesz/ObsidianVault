---
description: Sage LEARNING REJECT — proposed learning → retired (rejection). Reason kötelező.
id: 26df490a-b7ab-48ec-b714-5a9963db3547
index_schema_version: 1
---

A felhasználó egy learning-proposal elutasítását kéri.

**$ARGUMENTS** — kötelező: a learning slug-ja + `--reason "..."` (egyrövid mondat indok)

**Tennivaló:**

1. Parse $ARGUMENTS — slug + reason
2. Ha reason hiányzik → error: "`--reason \"...\"` kötelező"
3. Keresd: `learnings/proposals/<slug>.md`
4. Frontmatter update:
   - `status: retired`
   - `retired_at: <ISO ts>`
   - `retired_reason: "<reason from $ARGUMENTS>"`
5. Mozgasd: `proposals/` → `retired/`
6. Update `learnings/00_INDEX.md`
7. Append `_journal/<YYYY-MM>.md`: `event: learning-reject`, `reason: "..."`

Nincs külön confirmation — a reason-megadás már szándékot jelez.
