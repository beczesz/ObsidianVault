---
description: Curator RETIRE mode — dashboard archiválása/törlése + launcher-deregisztráció + index-frissítés. Confirmation + dry-run default.
id: 22730951-e269-4df7-a37b-4cb5ff75deab
index_schema_version: 1
---

A felhasználó egy dashboard leszerelését kéri.

**$ARGUMENTS** — kötelező: melyik dashboard + opcionális mód. Példák:
- `old-experiment` → dry-run (default): mit fog tenni
- `old-experiment --apply` → tényleg végrehajtja az archiválást
- `old-experiment --delete` → archiválás helyett törlés (csak nagyon óvatosan)

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: dashboard név + apply/delete flag (default: dry-run).
2. Hívd meg a Curator-t **`subagent_type: curator`** **retire módban**:
   - megnézi a `_dashboards/<név>.html`-t, idézi a tartalmát
   - dry-run-ban: kilistázza mit tenne (archive path, launcher-deregisztráció, index-frissítés)
   - `--apply`-jal: mozgatás `_dashboards/_archive/<dátum>-<név>.html`-be, eltávolítás a launcherből, index-frissítés, dated audit-trail komment
   - `--delete`-tel: végleges törlés (rendkívül óvatos, fokozott confirmation)
3. A Curator destruktív akció előtt **mindig** explicit megerősítést kér a chat-ben, az `--apply`/`--delete` flag csak engedély-jelző.

**Alapelv:** ha bizonytalan vagy, először futtasd dry-run-ban.
