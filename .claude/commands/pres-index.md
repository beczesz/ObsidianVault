---
description: Presto INDEX mode — cross-project marketing index regenerálása (_dashboards/00_MARKETING_INDEX.md). Az összes Area Marketing/Pipeline.md-jét aggregálja.
id: fc37090a-e9e5-454f-a856-7359cd449efb
index_schema_version: 1
---

A felhasználó cross-project marketing indexet regenerál.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → teljes regen
- `--quiet` → regen csak a change-deltával, részletes diff nélkül

**Tennivaló:**

1. Hívd meg a Presto-t **`subagent_type: presto`** **index módban**:
   - Bejár: minden `02_Areas/*/Marketing/Pipeline.md` + aktív `Campaigns/*/CAMPAIGN.md`
   - Aggregálja egy táblába a `_dashboards/00_MARKETING_INDEX.md`-be:
     - `## Active campaigns (cross-project)` — Area × Campaign × Stage × Due × Next action
     - `## Today (YYYY-MM-DD)` — mai dátumra esedékes akciók Area-onként
2. Az index-fájl frissül + chat-summary: hány Area indexelve, hány aktív kampány, mi változott a legutóbbi run óta.
3. Confirmation NEM kell (info-mód, csak az index-fájlt írja).

**Megjegyzés:** ez az egyetlen index-író Presto-mód. `today` és `status` csak olvas. Ha létezik a `_dashboards/marketing.html` dashboard (Fázis 3), az ezt fetcheli élőben.
