---
description: Curator TEND mode — meglévő dashboard gondozása (verzió-bump, audit-trail bővítés, kisebb fix, index-frissítés).
id: 00e9fc3b-03f4-4097-b1d2-fa9867674ba2
index_schema_version: 1
---

A felhasználó egy meglévő dashboard módosítását/karbantartását kéri.

**$ARGUMENTS** — kötelező: melyik dashboard + mit. Példák:
- `sales — fix kanban scroll on mobile` → célzott fix
- `agents — add példa-hívás block to cards` → kis fejlesztés
- `partnerships — bump version pill alignment` → patch

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: dashboard név + a kért változás.
2. Hívd meg a Curator-t **`subagent_type: curator`** **tend módban**:
   - megnyitja a megfelelő `_dashboards/<név>.html`-t
   - végrehajtja a célzott módosítást (csak amit kértél, semmi spread)
   - patch verzió-bump (x.y.z → x.y.z+1)
   - dated audit-trail comment hozzáadás a fejléchez
   - `_dashboards/00_DASHBOARD_INDEX.md` frissítés
3. Megőrzi a kanonikus DS-tokeneket (nem talál fel újat). Ha közben DS-gap-et lát, jelzi a `promote` jelöltek közé.

**Confirmation:** módosítás előtt megmutatja a tervezett változást és visszaigazolást kér.
