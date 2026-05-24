---
description: Presto LEARNING ACCEPT — proposed audience-learning → active. Confirmation kötelező.
id: fe2db165-1caa-47cf-a638-df76b33f89c1
index_schema_version: 1
---

A felhasználó audience-learning-proposal elfogadását kéri.

**$ARGUMENTS** — kötelező: slug (pl. `2026-06-02_linkedin-philosophy-resonance`)

**Tennivaló:**

1. Keresd: `agents/presto/audience-learnings/proposals/<slug>.md`
2. Ha nincs → error
3. Mutasd a tartalmát + kérdezz: "Elfogadod?"
4. Confirmation után:
   - Frontmatter: `status: active`, `confirmed_at: <ISO>`
   - Mozgasd: `proposals/` → `active/`
   - Update `audience-learnings/00_INDEX.md`
   - Append `02_Areas/<area>/Marketing/Pipeline.md` Iteration history-ba (vagy presto/logs/learning/<YYYY-MM>.md ha Phase 2.B kész)
