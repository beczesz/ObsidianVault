---
description: Sage CURATE mode — heti reflexió (kézi futtatás). Trendet, kapcsolatot, kategória-revíziót, learning-proposalt aggregál. Confirmation kötelező.
id: c00ca51b-6e82-4a74-aaf3-bc81c21f4bcb
index_schema_version: 1
---

A felhasználó kézi heti Sage curate-et kér (drága, hosszú futás — akár 15-20 perc).

**$ARGUMENTS** — opcionális. Lehet:
- üres → standard heti curate
- `--week <YYYY-Www>` → konkrét hetet kurálni (audit célra)
- `--dry-run` → fut, de NEM ír semmit

**Tennivaló:**

1. **Megerősítés kötelező** — kérdezd meg: "Sage heti curate ~15-20 perc lehet, Librarian-kéréseket fog tenni. Folytassuk?"
2. Csak `yes`/`igen`/explicit megerősítés után indítsd
3. Hívd `subagent_type: sage` (fallback `general-purpose`)
4. Paramétrek:
   - `mode: curate`
   - `prompt_file: 00_Prompts/BDOS/agents/sage/prompts/weekly_curate.md`
   - opcionális: `week`, `dry_run`
5. Várd vissza a summary-t (max 500 szó)
6. Adj vissza:
   - heti összegzés (új thought-ok, atomic-promote-javaslatok, learning-proposalok)
   - top 1-2 emergent pattern (ha van)
   - kategória-változások listája
   - notify-flag és indok
