---
description: Curator BUILD mode — új dashboard scaffold a capability recept + DESIGN_SYSTEM szerint, plusz launcher-regisztráció és index-frissítés.
id: 664e7414-c3e0-43b3-88ff-26d971ae236e
index_schema_version: 1
---

A felhasználó új dashboard építését kéri.

**$ARGUMENTS** — kötelező: a dashboard célja / adatforrása. Példák:
- `marketing — _dashboards/marketing.html, fetch 00_MARKETING_INDEX.md` → új marketing dashboard
- `cps-finance — _dashboards/cps-finance.html, fetch 02_Areas/Sonrisa/CPS/Finance/*.md`

**Tennivaló:**

1. Parsold a célt és az adatforrást az $ARGUMENTS-ből (név, fájl-útvonal, fetch-target).
2. Hívd meg a Curator-t **`subagent_type: curator`** **build módban**:
   - célfájl: `_dashboards/<név>.html`
   - adatforrás: a megadott markdown(ok)
   - recept: `00_Prompts/BDOS/capabilities/vault-dashboards/CLAUDE.md`
   - design system: `_dashboards/_design/DESIGN_SYSTEM.md` (kanonikus tokenek, hét törvény)
3. Curator scaffoldolja a HTML-t, fetch + 8s polling + sync indicator + home button + version pill + audit-trail + light/dark toggle + card-copy-ref komponensek a 7-törvény szerint.
4. Regisztrálja a launcherbe (`index.html`) és frissíti a `00_DASHBOARD_INDEX.md`-t.
5. Ne indítson szervert — `/dash-serve` parancs külön kezeli.

**Confirmation:** új fájl írása előtt a Curator visszaigazolást kér (név, hely, adatforrás megerősítése).
