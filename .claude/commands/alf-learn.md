---
description: Alfred LEARN — learning-lifecycle router: accept / reject / retire / edit. Az agents/alfred/learnings/ proposals/active/retired könyvtárak kezelése. Confirmation-gate kötelező.
id: a1f10012-0000-4c00-8000-000000000012
index_schema_version: 1
---

A felhasználó Alfred learning-lifecycle műveletet kér.

**$ARGUMENTS** — kötelező: `<action> <slug>`

Actions: `accept`, `reject`, `retire`, `edit`

Példák:
- `accept 2026-05-28_deep-work-rhythm`
- `reject 2026-05-20_morning-capture-proposal`
- `retire 2026-05-15_old-pattern`
- `edit 2026-05-28_deep-work-rhythm`

**Tennivaló:**

1. Parsold action-t és slug-ot.
2. **accept**: keresd `agents/alfred/learnings/proposals/<slug>.md`, mutasd tartalmát, kérd confirmation, majd: frontmatter `status: active` + `confirmed_at`, mozgasd `proposals/` → `active/`, frissítsd `learnings/00_INDEX.md`. Cap ellenőrzés: max 15 active learning.
3. **reject**: keresd `proposals/<slug>.md`, mutasd, kérd confirmation, majd: töröld (vagy mozgasd `retired/`-ba `status: rejected`-del).
4. **retire**: keresd `active/<slug>.md`, mutasd, kérd reason ("Miért archivált?"), confirmation, majd: frontmatter `status: retired` + `retired_at` + reason, mozgasd `active/` → `retired/`, frissítsd `00_INDEX.md`.
5. **edit**: keresd a fájlt (proposals vagy active), mutasd jelenlegi tartalmat, kérd a módosítást, confirmation, majd: végrehajt.
6. Logolj (learning log stream §8 szerint).

**Confirmation-gate minden esetben kötelező.**

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `learn` mód (v0.3 kognitív, Sage-merged).
