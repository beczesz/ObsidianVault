---
description: Librarian DEEP-CLEAN mode — nagytakarítás: byte-azonos duplikátum / üres / temp törlése + stale archiválás. Dry-run default!
id: ff8840e7-87e6-4ce8-96fb-8b3520092823
index_schema_version: 1
---

A felhasználó **nagytakarítást** kér a Librarian-tól — tidy-nál mélyebb cleanup elavult, duplikált, üres tartalmakra.

**$ARGUMENTS** — scope + safety flag + opcionális stale_days. Példák:
- üres → globális dry-run, default 180 nap stale
- `--scope=deak` → DH scope, dry-run
- `--scope=deak --apply` → ténylegesen végrehajt
- `--stale-days=365` → egy év alatt nem érintett fájlok stale-nek számítanak
- `--apply --stale-days=90` → globális végrehajtás 90 napos stale küszöbbel

**Tennivaló:**

1. Parsold a scope-ot, `--apply` flag-et, `--stale-days` értéket (default 180)
2. **Default `dry_run: true`** — csak ha `--apply` van, akkor `dry_run: false`
3. Ha `--apply` van **ÉS** a scope aktív projektet érint (DH Sprint 3 alatt), **kérdezz vissza** mielőtt indítasz: "Ez tényleges fájl-mozgatás/törlés lesz. Az aktív sprint folyamatban van. Folytassam?"
4. Hívd meg a Librariant **`subagent_type: librarian`**-nal deep-clean módban:
   - `mode: deep-clean`
   - `scope: <scope>`
   - `dry_run: <bool>`
   - `stale_days: <int>`
5. A subagent megengedett akciói (priority order):
   - Byte-azonos duplikátum törlés (md5 confirm)
   - Üres fájl törlés
   - Temp/.bak fájlok (> 30 nap, nem hivatkozott) törlés
   - `status: archived|stale|outdated` frontmatter → mozgatás `04_Archive/`-ba
   - Stale fájlok (> stale_days, nem hivatkozott) → flag (mozgatás csak `--apply`-vel)
   - `**`-prefixű elavult fájlok → archive
   - Üres mappa törlés
6. **Cross-reference check** minden akció előtt: ha bárki hivatkozik a fájlra (wikilink vagy md link), NEM törli/archiválja, csak flag-eli
7. Output: `00_DEEPCLEAN_LOG.md` a scope gyökerében — minden tervezett vagy végrehajtott akció timestamppel, indoklással, visszacsinálási paranccsal
8. Summary-ben mondd el: hány akció tervezett/végrehajtott típusonként, hol a log

**Safety alapelv:** semantically-similar (nem byte-azonos) fájlok merge-elését SOSEM csinálja. Aktív sprint alatt extra óvatos. A visszacsinálási parancs minden akcióhoz a logban van — ne félj a dry-run-tól.
