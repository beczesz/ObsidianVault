---
description: Alfred TODO — új task felvétele a megfelelő scope todos/<scope>.md ## Active szekcióba. Confirmation-gate kötelező.
id: a1f10005-0000-4c00-8000-000000000005
index_schema_version: 1
---

A felhasználó új task-ot akar felvenni.

**$ARGUMENTS** — opcionális: `<scope> "<feladat>" [--due YYYY-MM-DD] [--priority high|mid|low]`

Példák:
- `personal "Megvásárolni a Duna-parki jegyet" --due 2026-06-01`
- `navigator "EP41 vágás végig nézni" --priority high`
- (üres) → Alfred rákérdez scope-ra és feladatra

**Tennivaló:**

1. Parsold scope-ot, feladatot, due-t, prioritást.
2. Ha scope hiányzik vagy bizonytalan → kérdezz rá (ne tippelj).
3. Ha feladat hiányzik → kérdezz rá.
4. Generálj checkbox sort task-formátumban:
   ```
   - [ ] <feladat> <prioritás emoji> 📅 <YYYY-MM-DD> #<scope>
   ```
   Prioritás emoji: `⏫` high, `🔼` mid, `🔽` low (opcionális ha nincs megadva).
5. **Mutasd a tervezett sort + célhelyet**: "Ezt veszem fel: [sor] → `todos/<scope>.md` ## Active — mehet?"
6. Confirmation után: fűzd a `## Active` szekció végéhez.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §5a + §4 `todo` mód.
