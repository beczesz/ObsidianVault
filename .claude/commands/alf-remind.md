---
description: Alfred REMIND — emlékeztető-task felvétele due dátummal. A today/sync kiemeli lejáratkor. Confirmation-gate kötelező.
id: a1f10006-0000-4c00-8000-000000000006
index_schema_version: 1
---

A felhasználó emlékeztetőt kér — valami miatt emlékeztetni kell a megfelelő időpontban.

**$ARGUMENTS** — opcionális: `"<mire emlékeztessen>" [dátum/holnap/jövő héten/...]`

Példák:
- `"Marcsi szülinapja" jövő héten`
- `"CCHBC proposal beküldés" 2026-06-03`
- `"orvosi időpont egyeztetés" holnap`

**Tennivaló:**

1. Parsold a szöveget és dátumot.
2. Dátum-felismerés: "holnap" = ma+1, "jövő héten" = ma+7, ISO dátum → közvetlen.
3. Ha dátum hiányzik → kérdezz rá.
4. Scope-felismerés a szövegből (pl. "Marcsi" → family, "CCHBC" → sonrisa, stb.). Ha bizonytalan → kérdezz.
5. **Mutasd a tervezett reminder-sor-t + célhelyet** (confirmation-gate).
6. Confirmation után: fűzd a megfelelő `todos/<scope>.md` ## Active szekcióba:
   ```
   - [ ] Emlékeztető: <szöveg> 📅 <YYYY-MM-DD> #<scope>
   ```
7. A `today` és `sync` módok kiemelni fogják, ha a due date elér.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `remind` mód + §11 intent-felismerés.
