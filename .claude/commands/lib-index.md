---
description: Librarian INDEX mode — indexel egy scope-ot, 5 index fájlt generál (00_INDEX, KNOWLEDGE_MAP, DECISIONS, OPEN_QUESTIONS, GAPS).
id: fa3cdd79-f9da-447e-b68c-c133c43aa91b
index_schema_version: 1
---

A felhasználó indexelést kér a Librarian-tól.

**$ARGUMENTS** — a scope, amit indexelni kell. Lehet:
- `global` vagy üres → teljes vault (output: vault gyökerébe)
- konkrét mappa-útvonal (pl. `02_Areas/Navigátor Podcast`) → scoped index az adott mappa gyökerébe
- `deak` rövidítés → `02_Areas/Deák Húsüzlet`

**Tennivaló:**

1. Értelmezd az $ARGUMENTS-et, döntsd el a scope-ot és az output útvonalat
2. Hívd meg a Librariant **`subagent_type: librarian`**-nal (ha még nem regisztrált a futó sessionben, fallback `general-purpose`-ra a kanonikus prompttal)
3. Adj át paramétereket:
   - `mode: index`
   - `scope: <eldöntött path vagy "global">`
   - `output_path: <hova írja az 5 fájlt>`
4. A subagent izolált contextusban fut — várd a summary-t
5. Add vissza a felhasználónak: scope, fájl-szám, top találatok, GAP-ok, esetleges meglepetések

Ha az $ARGUMENTS üres és nem egyértelmű a szándék, kérdezz vissza egy mondatban: "Globális vagy konkrét scope?".
