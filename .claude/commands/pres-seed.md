---
description: Presto SEED mode — raw marketing input formalizálása presto.seed.v1 sémájú fájlként a presto/_inbox/seeds/ inbox-ba. A Marketing Engine v0.2 pipeline első lépése. Confirmation kötelező.
id: b3e1f7a2-9c4d-4e8f-a0b1-2c3d4e5f6a7b
index_schema_version: 1
bdos_index: true
---

A felhasználó új marketing seed-et rögzít — ötlet, Sage atomic, user-note, vagy külső tartalom-tipp.

**$ARGUMENTS** — kötelező:
- `--content "<szöveg>"` VAGY `--from-atomic <atomic-slug>` — a seed tartalma
- opcionális `--area <name>` — melyik projekthez tartozik (ha tudható)
- opcionális `--platforms LinkedIn,X,Blog,...` — javasolt csatornák (comma-separated)
- opcionális `--source user|sage-atomic|external|campaign` (default: user)

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből a fenti paramétereket.
2. Ha `--content` ÉS `--from-atomic` is hiányzik, kérdezz vissza: "Mi a seed tartalma?"
3. Hívd `subagent_type: presto` **seed módban**:
   - Ha `--from-atomic`: olvasd be a Sage atomic fájlt (`Ideas/atomic/<slug>.md`), validáld hogy `status != nascent`
   - Generálj `seed-id`-t: `seed-<YYYYMMDD>-<kebab-case-slug>` format
   - Töltsd ki a `presto.seed.v1` frontmattert:
     - `intent.audience` — kinek szól (az area audience-ből vagy az atomic targetjéből)
     - `intent.message` — egy mondatos fő üzenet
     - `intent.hook_angle` — javasolt megközelítési szög
     - `channels` — javasolt platformok
     - `area` — project area
     - `source_ref` — atomic link ha `--from-atomic`
4. **Confirmation gate KÖTELEZŐ** — mutasd: seed-id, intent összefoglaló (audience, message, hook), channels, area. Vár igen/yes válaszra.
5. Írj `00_Prompts/BDOS/agents/presto/_inbox/seeds/<seed-id>.md`-t.

**Seed schema minimuma:**
```yaml
---
schema: presto.seed.v1
seed_id: seed-YYYYMMDD-slug
status: new
created_date: YYYY-MM-DD
area: <name>
source: user|sage-atomic|external|campaign
source_ref: null|"[[atomic/...]]"
channels: [LinkedIn, ...]
intent:
  audience: "<kinek>"
  message: "<egy mondatos fő üzenet>"
  hook_angle: "<javasolt megközelítés>"
---

## Raw content
<eredeti szöveg vagy referencia>
```

**Következő lépés seed után:**
- `/pres-draft --seed <seed-id>` → draft Publication generálása ebből a seed-ből
- `/pres-plan --area <area> --from-seed <seed-id>` → teljes kampány a seed-ből

**Soha:** ne exhaustálj seed-et automatikusan. Seed perzisztens — csak `/pres-exhaust` szünteti meg.

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.4a.
