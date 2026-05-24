---
description: Maestro TEAM-PROMOTE mode — közös meta-szabály vagy capability ráhúzása az egész agent-családra. Confirmation + dry-run default. Analóg Curator promote-tal, agentekre.
id: 7f3c2600-1bd5-4c8c-82fb-4de462abbe7c
index_schema_version: 1
---

A felhasználó egy közös meta-változást húz rá a teljes agent-családra.

**$ARGUMENTS** — kötelező a `--change=` paraméter. Példák:
- `--change="minden canonical kapjon explicit '## Anti-patterns' szekciót, ha még nincs"` → dry-run (default)
- `--change="adj hozzá '## Output language' szabályt minden registration-höz" --apply` → tényleges
- `--change="bumpold mindegyik canonical-be a kontextus-védelmi alapelvet" --apply --agents=librarian,curator,herald` → csak megnevezettekre

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--change=` (kötelező), `--apply` flag (default: dry-run), opcionális `--agents=` (vesszős lista, default: all).
2. Ha `--change=` hiányzik, kérdezz vissza.
3. Hívd meg a Maestro-t **`subagent_type: maestro`** **team-promote módban**:
   - Dry-run: bontja a change-t per-agent konkrét edit-té, mutatja a változás-tervet (mely fájlokat módosítja, milyen verzió-bump, milyen audit-trail sor). Nem ír semmit.
   - **Confirmation gate KÖTELEZŐ** — Maestro a tervezett akciót strukturált formában mutatja, vár igen/yes válaszra.
   - `--apply`: a user OK-jára végrehajtja: minden érintett canonical edit + registration verzió-sync + dated audit-trail comment + AGENTS_INDEX frissítés.
4. **Önreflexivitás:** Maestro saját canonical-ja IS része a futtatásnak, ha a change rá is alkalmazható.
5. Végén: rövid summary + javaslat → `team-audit` futtatás verifikációként.

**Alapelv:** mindig először dry-run, csak utána `--apply`. Ha a Maestro során újabb gap-et észlel, listázza follow-up jelöltként.
