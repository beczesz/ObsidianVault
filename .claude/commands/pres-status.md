---
description: Presto STATUS mode — cross-project marketing áttekintés. Megmondja, hol tart minden aktív kampány minden Area-ban.
id: 9d23d4d4-0572-467e-a4c4-03157ad0c896
index_schema_version: 1
---

A felhasználó marketing-státuszt kér a Presto-tól.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → cross-project áttekintés minden Area-ról
- `--area=ExarLabs` → csak egy Area kampányai
- `--stage=draft` → csak egy stage-ben lévő kampányok

**Tennivaló:**

1. Parsold az opcionális paramétereket az $ARGUMENTS-ből (`--area=`, `--stage=`).
2. Hívd meg a Presto-t **`subagent_type: presto`** **status módban**:
   - Olvas: `_dashboards/00_MARKETING_INDEX.md` (ha nincs, jelzi és javasolja a `/pres-index`-et)
   - Aggregálja minden Area `Marketing/Pipeline.md`-jét + aktív `CAMPAIGN.md`-ket
3. Output: Area × Campaign × Stage × Due × Next action tábla.
4. Confirmation NEM kell (info-mód).

**Kontextus-védelem:** a tábla az output — ne ismételd prózában. Csak rövid bevezető és a tábla.
