---
description: Maestro OPTIMIZE mode — egy konkrét reflect-javaslatot végrehajt. Dry-run default + confirmation + Version Log audit-trail. Confirmation KÖTELEZŐ.
id: 1ae706ea-b558-4f38-9e70-3c1b187a4197
index_schema_version: 1
---

A felhasználó Maestro optimize módot kér — konkrét javaslat végrehajtása.

**$ARGUMENTS** — kötelező egyik:
- `--recommendation_id <slug>` — egy korábbi reflect-output-ban szereplő javaslat
- `--change "<plain English description>"` — manuális change-leírás
Plus opcionálisan:
- `--apply` — confirmation flag (default: dry-run)

**Tennivaló:**

1. Parse $ARGUMENTS — vagy recommendation_id vagy change kötelező
2. Hívd `subagent_type: maestro`
3. Paraméterek:
   - `mode: optimize`
   - `recommendation_id` vagy `change`
   - `apply: true/false` (default false — dry-run)
4. Maestro:
   - Resolve recommendation
   - Generálja a tervezett változtatás-listát (multi-fájl diff)
   - **Dry-run output** mutatja: melyik fájl, milyen változás, mit várunk
5. Ha `--apply NEM volt megadva` → dry-run summary visszaadása, NE írj
6. Ha `--apply` igen ÉS user confirmálta → Apply:
   - Edit files
   - Bump érintett agent versions (minor)
   - **KÖTELEZŐ:** Version Log bejegyzés minden érintett agent `logs/version/<YYYY-MM>.md`-jébe (schema `bdos.version.log.v1`)
   - `approved_by: user` + `reversible: true` + `rollback_path: ...` kitöltve
7. Output: summary, mit változtattál + audit-trail link

**Confirmation gate KÖTELEZŐ.** Soha nem futtass apply-t dry-run preview nélkül.

Lásd: `00_Prompts/BDOS/CONSTITUTION_PHASE_2.md` + `00_Prompts/BDOS/LOG_SCHEMAS.md` + `00_Prompts/BDOS/agents/maestro.md` §4.C.3.
