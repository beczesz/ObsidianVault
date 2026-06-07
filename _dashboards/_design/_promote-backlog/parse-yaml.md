---
title: Promote — parseYamlFrontmatter unification
description: "Six dashboard YAML frontmatter parsers (sales, aiops, broker, librarian, presto, sage) need unification into a single canonical parser in `_design/markdown-parser.js`, with support for nested objects, block scalars, hex-color preservation, and array formats; includes phased rollout plan with per-dashboard testing."
description_source: auto
description_hash: ec3ced48e646f7bc
date: 2026-05-25
status: pending
priority: medium
estimated_loc_savings: 500
risk: high
discovered_in: Sprint 3 (2026-05-25)
id: 85d06381-7806-4f37-8be4-d59f31e34162
index_schema_version: 1
---
# Promote — parseYamlFrontmatter unification

> **Cél:** a 6 dashboard inline parser-variánsait (sales/aiops/broker/librarian/presto/sage) átállítani a kanonikus `_design/markdown-parser.js`-re — vagy bővíteni azt szuperset-té, amely mind a 6 használati esetet lefedi.

## Miért nem ment mechanikusan a Sprint 3-ban

A 9 dashboard közül **csak 3** (partnerships, team, navigator) volt verbatim azonos (hash `41edbbd902e5`). A többi 6 funkcionálisan **különböző feature-set**-tel rendelkezik. Hash-audit-gated migration ezeket SZÁNDÉKOSAN kihagyta.

## Variáns-mátrix

| Hash | Fájl(ok) | Sor | Kulcs-feature |
|---|---|---|---|
| `41edbbd902e5` ✅ extracted | partnerships, team, navigator | 83-87 | Nested obj, indent stack, quote-aware comment-strip, scalar coercion, inline + block arrays |
| `41c36beb495e` | broker, librarian | 29-33 | Compact. Basic key:value. Inline `[a,b,c]` + block `- item` arrays. **Hex-preserving** comment-strip (`#abc123` color values nem törlődnek) |
| `1f1861cebd1d` | sales | 124 | Extended. Hosszabb logika valószínűleg nested lead-struktúrákhoz |
| `d6249b7a1875` | aiops | 88 | ~canonical-szerű variáns, de hash eltér — apró logika-különbség |
| `bfc697f4c043` | presto | 35 | Block scalar support (`\|`, `>`). JSON-style arrays via try/catch. Quote-aware comment-strip regex |
| `aeabaf0877d6` | sage | 14 | Modular stub — delegate to külön `parseYamlBlock` függvényre |

## Funkció-mátrix (mit kell az új parsernek tudnia)

| Funkció | partn./team/nav (canonical) | broker/lib | sales | aiops | presto | sage |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Basic `key: value` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Nested objects (indent) | ✓ | ✗ | ✓ | ? | ✗ | (via parseYamlBlock) |
| Block array `- item` | ✓ | ✓ | ✓ | ✓ | ✓ | ? |
| Inline array `[a,b,c]` | ✓ | ✓ | ? | ? | ✓ (JSON) | ? |
| Comment-strip `# ...` | ✓ (quote-aware) | ✓ (hex-preserving) | ? | ? | ✓ (quote-aware) | ? |
| Block scalar `\|` / `>` | ✗ | ✗ | ? | ? | ✓ | ? |
| Scalar coercion (int/float/bool/null) | ✓ | partial | ? | ? | ? | ? |
| Hex-color preservation in `#`-strip | ✗ | ✓ | ? | ? | ? | ? |

## Javasolt kanonikus szuperset

A **canonical 87-line parser BŐVÍTETT** változata, amely tartalmazza:

1. **A canonical összes feature-jét** (nested, indent stack, scalar coercion, quote-aware strip)
2. **+ Hex-color preservation** (broker/librarian-ből): `#` előtt csak akkor strip ha NEM hex-color-szerű — `#[0-9a-fA-F]{3,8}\b` whitelist
3. **+ Block scalar `|` és `>` support** (presto-ból): üres value után indent-aware block-collection, `|` literal join `\n`-nel, `>` folded join space-szel

Becsült méret: ~120 sor (vs jelenlegi 87).

## Rollout terv

### Fázis 1: a szuperset megírása + test
- Bővítsd `_design/markdown-parser.js`-t (DS 0.7.4 → 0.7.5)
- Tesztelni: minden 6 dashboard input-mintát parse-elni offline
- Output-egyenlőség check (deep-equal) az eredeti inline parser output-jaival

### Fázis 2: per-dashboard migráció (egyesével, hash-audit-gated)
Minden dashboardnak:
1. Compute current inline parser output minden élő markdownjára (snapshot)
2. Cserélni inline parser-t shared lib-re (`/* parseYamlFrontmatter: moved to ... */`)
3. Re-compute output az új sharing parser-rel
4. Diff → ha üres, success. Ha eltér, vissza, vizsgálat, javítás a szuperset-en.

Sorrend (legkisebb kockázat először):
1. **sage** (14 sor stub — biztos szuperset lefedi)
2. **broker** (29 sor compact) — figyelni: hex-strip működik-e
3. **librarian** (33 sor compact) — broker-rel együtt rolloutol
4. **presto** (35 sor block-scalar) — figyelni: `|` és `>` használat
5. **aiops** (88 sor variant) — close to canonical
6. **sales** (124 sor extended) — legnagyobb risk, legutoljára

### Fázis 3: cleanup + DS-bump
- Inline parser-ek törlése mind a 6 fájlból
- DS audit-trail entry "parseYamlFrontmatter unification complete"
- Curator backlog `parse-yaml.md` status = `rolled-out`
- `ARCHITECTURE.md` §3 (komponens-rétegek) frissítése: parser most teljesen shared

## Kockázatok

- 🔴 **Sales 124-sor extended** — ha komplex nested lead-struktúrákat parse-ol (multi-level objects), a canonical szuperset-nek tudnia kell. Risk: silent data loss vagy crash a render fázisban.
- 🟡 **Broker hex-preserve** — ha a markdown YAML-okban hex-color értékek élnek `#`-vel és a strip elveszi őket, render hiba lesz. Mitigation: erős unit test a szuperset-re.
- 🟡 **Presto block-scalar** — ha CAMPAIGN.md-k tartalmaznak `description: \|\n  multi-line text\n  with indent`-et, azt meg kell tartani.
- 🟢 **Aiops variant** — kis eltérés, valószínűleg könnyen lefedhető.

## Alternatív minimum-rizikó megközelítés

Ha a szuperset túl ambiciózus:

**Opció: 3 named exports a shared lib-ben**
- `window.parseYamlFrontmatter` — canonical (jelenlegi)
- `window.parseYamlFrontmatterCompact` — broker/librarian variánsának kanonizált verziója (hex-preserving)
- `window.parseYamlFrontmatterBlock` — presto variánsának kanonizált verziója (block-scalar support)

Minden dashboard explicitly válassza ki melyiket akarja használni. **Hátrány**: 3 párhuzamos parser. **Előny**: 0 kockázat behavioral mismatch-re.

## Becsült LOC nyereség

| Fájl | Inline LOC | Mentés |
|---|---|---|
| sales | 124 | -124 |
| aiops | 88 | -88 |
| broker | 29 | -29 |
| librarian | 33 | -33 |
| presto | 35 | -35 |
| sage | 14 (stub) + delegate | -14 |
| **Shared lib bővítés** | +35 | |
| **Net** | | **~285 LOC** |

(Eredeti becslés Sprint 5-ben ~500 LOC volt, de a sales extended verziójának súlya miatt valószínűleg 285 körül van a reálisabb szám.)

## Rollback terv

Per-dashboard rollback git checkout-tal. Mivel egyesével migrálunk, blast radius minimal.

## Kapcsolódó

- [`../markdown-parser.js`](../markdown-parser.js) — a jelenlegi canonical (Sprint 3-ban extrahált)
- [`../DESIGN_SYSTEM.md`](../DESIGN_SYSTEM.md) DS 0.7.2 audit-trail
- [`../../00_DASHBOARD_INDEX.md`](../../00_DASHBOARD_INDEX.md) Sprint 3 entry
