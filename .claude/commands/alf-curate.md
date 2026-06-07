---
description: Alfred CURATE — heti idea-reflexió: trend-analízis, kategória-revízió, emergens minták. Kimenet: Ideas/curate/YYYY-Www.md. Confirmation-gate kötelező (drága futás).
id: a1f10010-0000-4c00-8000-000000000010
index_schema_version: 1
---

A felhasználó Alfred heti curate-t kér — az összegyűlt idea-thought-note-ok reflexiója, minta-keresés.

**$ARGUMENTS** — opcionális: `--week YYYY-Www` (default: aktuális hét, pl. `2026-W22`).

**Tennivaló:**

1. **Confirmation-gate:** "Alfred heti curate-t indítok — ez ~15-20 perces, mélyebb elemzés. Folytassam?"
2. Confirmation után:
3. Glob + Read: az adott hét thought-note-jai (`Ideas/thoughts/YYYY-MM-DD_*.md`) + atomic-javaslatok.
4. Trend-analízis: milyen témák, gondolat-típusok, kapcsolatok jelennek meg.
5. Kategória-revízió: van-e érdemes új kategória `Ideas/00_CATEGORIES.md`-be?
6. Max 3 emergens minta azonosítása (explicit és implicit).
7. Max 2 atomic-promote javaslat (`Ideas/atomic/`-ba kerülhet).
8. Learning-proposal generálása ha erős minta látszik (→ `agents/alfred/learnings/proposals/`).
9. Kimenet írása: `Ideas/curate/<YYYY-Www>.md` (frontmatter + patterns + atomic-javaslatok + learning-javaslat ha van).
10. Frissítsd `agents/alfred/state/last_run.md`.
11. Notify: ha emergent_patterns >= 1 vagy hiba.

**Tools:** Read, Write, Edit, Glob, Grep + Librarian-kérések main Claude orchestrátoron át.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `curate` mód (v0.3 kognitív, Sage-merged).
