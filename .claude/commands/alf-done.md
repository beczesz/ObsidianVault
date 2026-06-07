---
description: Alfred DONE — task kipipálása (- [x]) és ## Archive szekcióba mozgatása. Sosem töröl. Triviális esetben confirmation nélkül fut.
id: a1f10007-0000-4c00-8000-000000000007
index_schema_version: 1
---

A felhasználó egy task elvégzettnek jelöl.

**$ARGUMENTS** — kötelező: task szövege (részleges egyezés is elég) + opcionális `--scope <scope>`.

Példák:
- `"CCHBC proposal beküldés"`
- `"jegyet megvásárolni" --scope personal`

**Tennivaló:**

1. Keresd a `02_Areas/Personal Growth/Alfred/todos/` mappában az egyező nyitott checkbox-ot (`- [ ]` tartalmazza az argumentum szövegét).
2. Ha több egyezés → mutasd listán, kérd pontosítást.
3. Ha egyértelmű egyezés:
   - Cseréld `- [ ]` → `- [x]`
   - Add hozzá `✅ <YYYY-MM-DD>` a sor végén (completion date).
   - Mozgasd a sort a `## Archive` szekció végébe.
4. Triviális és egyértelmű esetben a confirmation elhagyható. Ha kétséges (több egyezés, nem egyértelmű scope) → confirmation-gate.
5. Visszajelzés: "Kész: [task szöveg]"

**Sosem töröl** — az archivált sor megmarad a fájlban.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `done` mód + §5a archív konvenció.
