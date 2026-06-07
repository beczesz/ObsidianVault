---
description: Alfred LEARNING RETIRE — active Alfred-learning archiválása (active → retired). Confirmation kötelező.
id: a1f10017-0000-4c00-8000-000000000017
index_schema_version: 1
---

A felhasználó egy aktív Alfred learning nyugdíjazását kéri.

**$ARGUMENTS** — kötelező: slug (pl. `2026-05-15_old-pattern`)

**Tennivaló:**

1. Keresd: `agents/alfred/learnings/active/<slug>.md`
2. Ha nincs → error.
3. Mutasd a tartalmát + kérd reason-t: "Miért archivált? (pl. outdated, superseded, context changed)"
4. **Confirmation-gate**: "Archiválom: <slug> — mehet?"
5. Confirmation után:
   - Frontmatter: `status: retired`, `retired_at: <ISO>`, `retire_reason: <reason>`
   - Mozgasd: `active/` → `retired/`
   - Frissítsd `agents/alfred/learnings/00_INDEX.md`
   - Logolj learning log stream szerint (§8)

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `learn` mód.
