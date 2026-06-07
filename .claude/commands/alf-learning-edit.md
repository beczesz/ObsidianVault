---
description: Alfred LEARNING EDIT — meglevo Alfred-learning (proposal vagy active) szerkesztése. Confirmation kötelező.
id: a1f10015-0000-4c00-8000-000000000015
index_schema_version: 1
---

A felhasználó Alfred learning szerkesztését kéri.

**$ARGUMENTS** — kötelező: slug (pl. `2026-05-28_deep-work-rhythm`)

**Tennivaló:**

1. Keresd a fájlt: elso `proposals/<slug>.md`, ha nincs ott, akkor `active/<slug>.md`.
2. Ha nem találod → error.
3. Mutasd a jelenlegi teljes tartalmat.
4. Kérd a módosítást: "Mit szeretnél módosítani?"
5. Mutasd a tervezett új tartalmat (diff-szerűen: mi változik).
6. **Confirmation-gate**: "Ezzel a változtatással frissítem — mehet?"
7. Confirmation után: hajtsd végre az editálást, add hozzá `updated_at: <ISO>` frontmatter mezőt.
8. Logolj learning log stream szerint (§8).

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `learn` mód.
