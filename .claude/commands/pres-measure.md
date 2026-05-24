---
description: Presto MEASURE mode — KPI ramp, cadence, conversion számítás. /marketing:performance-report skill futtatása. Per-kampány / per-Area / cross-project.
id: 30b399f8-4180-4900-9211-f0dcbfc41e18
index_schema_version: 1
---

A felhasználó sikerességet mér.

**$ARGUMENTS** — opcionális (default: aktív kampány). Példák:
- `--scope=campaign:ExarLabs/microsite-q3` → egy kampány
- `--scope=area:DH --period=last30d` → egy Area, utolsó 30 nap
- `--scope=cross-project --period=2026-05` → minden Area, adott hónap
- (üres) → aktív kampány, kampány indulása óta

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--scope=` (default: aktív kampány), `--period=` (default: kampány indulása óta).
2. Hívd meg a Presto-t **`subagent_type: presto`** **measure módban**:
   - Scope alapján beolvassa a megfelelő `CAMPAIGN.md` / `Pipeline.md` / cross-project adatokat
   - Futtatja a `/marketing:performance-report` skillt a beolvasott metrikákkal
3. Output: KPI-tábla, trend, win/miss, prioritás-javaslat a következő periódusra.
4. Per-kampány mérés esetén: a riport mentődik `Campaigns/<slug>/Results-YYYY-MM-DD.md`-be (audit-trail).
5. Confirmation NEM kell (info-mód, de a Results-fájl írás megerősíthető lehet).

**Kontextus-védelem:** a KPI-tábla az output — ne ismételd prózában.
