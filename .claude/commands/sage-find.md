---
description: Sage FIND mode — keresés a thoughts/ + atomic/ tárban. Kontextus-védett, csak az Ideas mappára nézve. Megerősítés nélkül.
id: 3efff33f-4813-474f-b3e8-13b3506669b3
index_schema_version: 1
---

A felhasználó Sage-find keresést kér a saját tudásbázisában.

**$ARGUMENTS** — a keresett kifejezés vagy téma (kötelező).

**Tennivaló:**

1. Ha $ARGUMENTS üres → kérdezz vissza egy mondatban
2. Hívd `subagent_type: sage` (fallback `general-purpose` + kanonikus prompt)
3. Paraméterek:
   - `mode: find`
   - `query: <$ARGUMENTS>`
   - `scope: 02_Areas/Personal Growth/Ideas/`
4. Az agent kontextus-védetten dolgozik — ne olvasd be a fájlokat itt
5. Várj egy listát: top 5-10 találat, mindegyik wikilinkkel + 1 mondatos relevancia-indok
6. Add vissza a listát + 1 mondatos szintézis ha látsz mintát
