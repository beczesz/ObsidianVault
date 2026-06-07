---
description: Alfred LEARNING ACCEPT — proposed Alfred-learning → active. Confirmation kötelező.
id: a1f10014-0000-4c00-8000-000000000014
index_schema_version: 1
---

A felhasználó Alfred learning-proposal elfogadását kéri.

**$ARGUMENTS** — kötelező: slug (pl. `2026-05-28_deep-work-rhythm`)

**Tennivaló:**

1. Keresd: `agents/alfred/learnings/proposals/<slug>.md`
2. Ha nincs → error: "Nem találom: proposals/<slug>.md"
3. Mutasd a tartalmát + kérdezz: "Elfogadod?"
4. Confirmation után:
   - Frontmatter: `status: active`, `confirmed_at: <ISO>`
   - Mozgasd: `proposals/` → `active/`
   - Frissítsd `agents/alfred/learnings/00_INDEX.md`
   - Cap check: ha active count >= 15 → figyelmeztess, de ne blokkolj
   - Logolj learning log stream szerint (§8)

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `learn` mód.
