---
description: Librarian TIDY mode — rendrakás (árvák mozgatása, broken link javítás, byte-azonos duplikátum törlés). Dry-run default!
id: b8ac149e-0a45-45ed-9983-c6369f796c3b
index_schema_version: 1
---

A felhasználó rendrakást kér a Librarian-tól.

**$ARGUMENTS** — scope + safety flag. Példák:
- üres → globális dry-run (csak megmutatja mit csinálna)
- `--scope=deak` → Deák scope, dry-run
- `--scope=deak --apply` → ténylegesen végrehajt
- `--apply` → globálisan végrehajt (RITKÁN)

**Tennivaló:**

1. Parsold a scope-ot és az `--apply` flag-et
2. **Default `dry_run: true`** — csak ha `--apply` van, akkor `dry_run: false`
3. Ha `--apply` van **ÉS** a scope tartalmaz aktív projektet (pl. Deák Sprint 3 alatt), **kérdezz vissza** mielőtt indítasz: "Ez tényleges fájl-mozgatás/törlés lesz. Folytassam?"
4. Hívd meg a Librariant **`subagent_type: librarian`**-nal tidy módban:
   - `mode: tidy`
   - `scope: <scope>`
   - `dry_run: <bool>`
5. A subagent megengedett akciói: a) árva fájl mozgatása, b) broken link fix (fuzzy>0.9), c) byte-azonos duplikátum törlés
6. Output: `00_TIDY_LOG.md` a scope gyökerében — minden akció timestamppel, visszacsinálási paranccsal
7. Summary-ben mondd el: hány akció történt (vagy dry-run-ban: mit csinálna), és hogy hol a log

**Safety alapelv:** semmilyen destruktív akció nélkül a felhasználó tudta nélkül. Sprint 3 alatt extra óvatos.
