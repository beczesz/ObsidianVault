---
description: Presto TODAY mode — mai napi marketing action queue, prioritás szerint. Kötelező "Most ajánlott következő lépés" + "Egyéb opciók" szekció. Engine-pull szemantika: azonnal futtatható javaslatot ad.
id: 5473bffd-f2c6-4b7e-a095-6d265c8ddf10
index_schema_version: 1
bdos_index: true
---

A felhasználó a mai marketing teendőket kéri.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → ma (default)
- `--date=2026-05-25` → másik napra

**Tennivaló:**

1. Parsold a `--date=` paramétert (default: ma).
2. Hívd meg a Presto-t **`subagent_type: presto`** **today módban**:
   - Olvas: `_dashboards/00_MARKETING_INDEX.md` `## Today (YYYY-MM-DD)` szekcióját
   - Fallback ha nincs match: szűri az aktív Publications ahol `publish_date` = adott dátum VAGY aktív Campaigns ahol `due` ≤ adott dátum
   - Olvassa az `presto/_inbox/seeds/` tartalmát a régi érintetlen seed-ekre

**Prioritás-logika (sorrendben):**
1. `publication_status: approval` — emberi jóváhagyás-blocker, legsürgősebb
2. `publication_status: scheduled`, `publish_date` = ma — közzé kell tenni
3. `publication_status: prepared` — review-ready, approve-ra vár
4. `publication_status: draft`, due = ma
5. Seed: `status: new` ÉS `created_date` > 3 napja (exhaust-jelölt vagy draft-jelölt)

3. Output (kötelező szekciók):
   - **Számozott lista** (max 5 tétel, prioritás sorrendben) — minden tételen: Area + entitás + konkrét akció + következő parancs
   - **"Most ajánlott következő lépés"** — EGYETLEN konkrét slash-command amit most kell futtatni (pl. `/pres-approve --pub dh/pub-linkedin-001 --action approve`)
   - **"Egyéb opciók"** — 2-3 alternatív akció bullet-ben

4. Confirmation NEM kell (info-mód).

**Példa-output:**
```
Ma 3 helyen kell mozdítani:
1. DH — pub-linkedin-001 (Approval stage): jóváhagyás szükséges
2. ExarLabs — pub-blog-001 (Prepared, review kész): ütemezés
3. DH — seed-20260522-nyari-akció (5 napja érintetlen): draft vagy exhaust

Most ajánlott következő lépés:
/pres-approve --pub dh/pub-linkedin-001 --action approve

Egyéb opciók:
- /pres-draft --seed seed-20260522-nyari-akció → draft generálás a régi seed-ből
- /pres-exhaust --seed seed-20260522-nyari-akció --reason "időszerűtlen" → lezárás
```

**Kontextus-védelem:** a lista az output — ne ismételd prózában.
