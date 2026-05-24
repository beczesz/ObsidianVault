---
description: Presto RESUME mode — félbehagyott marketing kampány folytatása. Iteration history + next_action alapján javasol folytatást. Confirmation kötelező.
id: a817b836-52c9-4060-9ca5-111ea8265849
index_schema_version: 1
---

A felhasználó folytatni szeretne egy elindított kampányt.

**$ARGUMENTS** — kötelező: melyik kampány. Példák:
- `--campaign=ExarLabs/microsite-q3` → folytatás ettől
- `--campaign=current` → a legutóbb érintett kampány (Iteration history alapján)

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--campaign=<area>/<slug>` vagy `current`.
2. Hívd meg a Presto-t **`subagent_type: presto`** **resume módban**:
   - Olvas: `CAMPAIGN.md` `Iteration history` (utolsó 5 bejegyzés) + `next_action` + open task-ok
   - Megmutatja: hol tartottunk legutóbb, mi van blokkolva (ha van), mi a logikus következő lépés
3. **Confirmation gate KÖTELEZŐ** — Presto egy folytatási javaslatot ad strukturált formában. Vár igen/yes válaszra.
4. A user OK-jára átadja a `run` módnak az adott task-tal — onnan a run-flow folytatódik.

**Hint:** ha a kampány > 14 napja nem mozdult és time-sensitive (`due` lejárt, vagy seasonal hook elavult), Presto jelzi és kérdez: re-prioritizáljuk, archiváljuk, vagy módosítjuk?
