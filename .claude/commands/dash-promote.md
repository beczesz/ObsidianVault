---
description: Curator PROMOTE mode — tanult minta beemelése a DESIGN_SYSTEM.md-be + ráhúzás az egész családra. Confirmation + dry-run default.
id: d046ad3f-6025-4459-85d6-2b2e9b230828
index_schema_version: 1
---

A felhasználó egy közös design-system változást húz rá a családra.

**$ARGUMENTS** — kötelező: a promote tárgya + opcionális flag. Példák:
- `.copyable-row component` → dry-run: mit tenne
- `.copyable-row component --apply` → tényleges promote (DS-bump + family rollout)
- `--theme=dark token revision --apply` → dark tokenek finomhangolása mindenhol

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: a tanult minta/komponens/token + apply flag (default: dry-run).
2. Hívd meg a Curator-t **`subagent_type: curator`** **promote módban**:
   - **Dry-run**: kilistázza milyen DS-változás történne (új komponens/token spec, érintett dashboardok, verzió-bumpok)
   - **`--apply`**: kodifikálja a mintát a `_dashboards/_design/DESIGN_SYSTEM.md`-be (minor bump), majd végigmegy a családon és minden tagra ráhúzza a változást — patch verzió-bumpokkal + dated audit-trail sorral
3. Curator destruktív/család-szintű akcióhoz **mindig** explicit chat-confirmationt kér, az `--apply` flag csak engedély-jelző.
4. Az `_dashboards/00_DASHBOARD_INDEX.md` frissül a végén.

**Alapelv:** mindig először dry-run, csak utána `--apply`. Ha a Curator gap-et lát a változás során, listázza follow-up jelöltként.
