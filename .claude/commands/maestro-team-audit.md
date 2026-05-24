---
description: Maestro TEAM-AUDIT mode — mély minőségi check az agent-családon. Verzió-sync, AGENTS_INDEX-konzisztencia, description-frissesség, broken cross-referencia.
id: 50d4e994-411d-406f-a14d-eceb61dff827
index_schema_version: 1
---

A felhasználó mély agent-audit-ot kér.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → teljes család audit
- `--agent=herald` → csak egy agent
- `--strict` → szigorú mód (stale > 60 nap, üres `<TODO>` placeholdert hibaként jelzi)

**Tennivaló:**

1. Parsold az `--agent=` és `--strict` paramétereket.
2. Hívd meg a Maestro-t **`subagent_type: maestro`** **team-audit módban**:
   - Per-agent checklist (lásd canonical §4.B.2):
     - Canonical létezik, frontmatter teljes
     - Registration létezik, verzió sync
     - AGENTS_INDEX bejegyzés tükrözi a tényleges canonical-t
     - BDOS/CLAUDE.md táblában szerepel
     - Description ésszerű hosszú, nincs `<TODO>` placeholder
     - Last_updated < 90 nap (strict: < 60)
     - Slash command-ok száma egyezik a mode számmal
     - Cross-referenciák valid path-ra mutatnak
3. Output: per-agent compliance mátrix ✅/⚠️/🔴 + konkrét hibalista + javasolt follow-up (pl. `team-promote --change="..."`).
4. Confirmation NEM kell (info-mód, nem módosít semmit).

**Kontextus-védelem:** a mátrix + hibalista az output. Ne hígítsd próza-ismétléssel.
