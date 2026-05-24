---
description: Presto ADAPT mode — Sage atomic/thought transzformálása N platform-specifikus variánssá. Distribution transformation. Confirmation kötelező.
id: 09f472e7-f8df-4095-abb9-b25c8bf6c335
index_schema_version: 1
---

A felhasználó Presto adapt módot kér — Sage-tartalmat platform-natív variánssá.

**$ARGUMENTS** — kötelező:
- `--source <slug>` — atomic slug VAGY `thoughts/<date>_<slug>`
- `--platforms LinkedIn,X,IG,YouTube,Newsletter,...` (comma-separated)
- `--area <name>` — brand kontextushoz
- opcionális `--tone <override>`

**Tennivaló:**

1. Parse $ARGUMENTS, validáld a source-ot (létezik-e Sage Ideas-ban)
2. Hívd `subagent_type: presto`
3. Paraméterek: `mode: adapt`, `source`, `platforms`, `area`, `tone`
4. Presto:
   - Olvassa source-t (Sage atomic/thought)
   - Olvas Area brand-tone-t a MARKETING_ENGINE.md-ből
   - Olvassa az `audience-learnings/active/*.md`-t a vonatkozó tanulságokra
   - Generál adaptation-tervet (NEM végleges szöveg, struktúrális szándék)
5. **Confirmation gate KÖTELEZŐ** — bemutatja: source + platforms + brand-tone + várt karakter
6. `--apply` után: kampány létrehozás, draft taskok platformonként, `/marketing:draft-content` skill
7. **NEM publikál** — drafts only

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.8.
