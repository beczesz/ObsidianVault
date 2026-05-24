---
description: Librarian RETRIEVE mode — kontextus-védett keresés. Visszahozza a legrelevánsabb fájlokat anélkül hogy a hívó kontextusa felfújódna.
id: ab6703ac-9fd9-404d-9a79-a128621918ec
index_schema_version: 1
---

A felhasználó keresést kér a Librarian-tól.

**$ARGUMENTS** — a query + opcionális scope/limit. Példák:
- `DH üzletfejlesztés` → globálisan, default limit
- `DH üzletfejlesztés --scope=deak --limit=5` → scoped, limit megadva
- `Navigátor csatorna intelligencia --scope="02_Areas/Navigátor Podcast"`

**Tennivaló:**

1. Parsold a query-t és az opcionális paramétereket az $ARGUMENTS-ből (`--scope=`, `--limit=`, `--depth=`)
2. Default-ok: scope=global, limit=5, depth=shallow
3. Hívd meg a Librariant **`subagent_type: librarian`**-nal (vagy fallback general-purpose) **retrieve módban**:
   - `mode: retrieve`
   - `query: <query>`
   - `scope: <scope>`
   - `limit: <limit>`
   - `depth: <depth>`
4. A subagent **csak olvas** (Write/Edit tiltva ebben a módban). Te (a main session) nem nyitod meg a fájlokat — a Librarian olvas helyetted.
5. Az output egy strukturált lista: `{path, why_relevant, relevance_score, key_excerpt}` minden találathoz, + összesítő summary

**Kontextus-védelmi alapelv:** ne ismételd meg a `key_excerpt`-eket prózában — a lista az output. Csak rövid bevezetőt írj, és add át a listát ahogy van.

Ha a query üres vagy túl homályos, kérdezz vissza egy mondatban.
