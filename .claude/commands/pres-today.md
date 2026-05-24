---
description: Presto TODAY mode — mai napi marketing action queue, prioritás szerint. Cross-project: mit kell ma mozdítani melyik Area-ban.
id: 5473bffd-f2c6-4b7e-a095-6d265c8ddf10
index_schema_version: 1
---

A felhasználó a mai marketing teendőket kéri.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → ma (default)
- `--date=2026-05-25` → másik napra

**Tennivaló:**

1. Parsold a `--date=` paramétert (default: ma).
2. Hívd meg a Presto-t **`subagent_type: presto`** **today módban**:
   - Olvas: `_dashboards/00_MARKETING_INDEX.md` `## Today (YYYY-MM-DD)` szekcióját
   - Ha a megadott dátum nincs a `## Today` blokkban, fallback: szűri az aktív kampányokat ahol `due` ≤ adott dátum vagy `publish_date` = adott dátum
3. Output: számozott lista, Area-onként csoportosítva, prioritás szerint. Minden tételen rajta a következő konkrét akció + (ha van) idő.
4. Confirmation NEM kell (info-mód).

**Példa-output:**
```
Ma 3 helyen kell mozdítani:
1. ExarLabs — Microsite Factory Q3: blog draft v2 review (due ma)
2. DH        — Húsvét #2: publish 14:00 (draft kész)
3. CPS       — AWS co-marketing: feedback Erikára
```

**Kontextus-védelem:** a lista az output — ne ismételd prózában.
