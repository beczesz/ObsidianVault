---
description: Alfred LEARNING REJECT — proposed Alfred-learning elvetése. Confirmation kötelező.
id: a1f10016-0000-4c00-8000-000000000016
index_schema_version: 1
---

A felhasználó Alfred learning-proposal elvetését kéri.

**$ARGUMENTS** — kötelező: slug (pl. `2026-05-20_morning-capture-proposal`)

**Tennivaló:**

1. Keresd: `agents/alfred/learnings/proposals/<slug>.md`
2. Ha nincs → error.
3. Mutasd a tartalmát + kérd reason-t: "Miért veted el?"
4. **Confirmation-gate**: "Elvetem: <slug> — mehet?"
5. Confirmation után:
   - Frontmatter: `status: rejected`, `rejected_at: <ISO>`, `reject_reason: <reason>`
   - Mozgasd: `proposals/` → `retired/` (NEM töröl — audit-trail marad)
   - Frissítsd `agents/alfred/learnings/00_INDEX.md`
   - Logolj learning log stream szerint (§8)

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `learn` mód.
