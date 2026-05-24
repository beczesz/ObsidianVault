---
title: Marketing Dashboard Contract
version: 0.1
date: 2026-05-23
status: design
description: Adat-formátum kontraktus a leendő `_dashboards/marketing.html` és a markdown source-ok (CAMPAIGN.md, Pipeline.md, 00_MARKETING_INDEX.md) között. A Sales DASHBOARD_CONTRACT.md mintáját követi.
id: a8aea4fd-f557-4c7f-bdd7-97148826446e
index_schema_version: 1
---

# Marketing Dashboard Contract — v0.1

> **Status: design.** A `_dashboards/marketing.html` dashboard még nem épült meg (Fázis 3). Ez a kontraktus előre rögzíti, milyen mezőket kell a CAMPAIGN.md frontmatterben + body szekciókban tartani, hogy a dashboard parse-olni tudja. Ha a Presto és a templatek ezt követik, a build-fázisban nincs adatformátum-mismatch.

---

## 1. Adatforrások — priorizálva

A dashboard 3 markdown source-ot fetchel élőben (8s polling, mint a sales.html):

| Prioritás | Forrás | Mit ad |
|---|---|---|
| **A — primary** | minden `02_Areas/*/Marketing/Campaigns/*/CAMPAIGN.md` | per-kampány state (frontmatter + tasks + schedule + results) |
| **B — stage** | minden `02_Areas/*/Marketing/Pipeline.md` | stage-meghatározás (a kanban `## <Stage>` szekciók) |
| **C — today** | `_dashboards/00_MARKETING_INDEX.md` `## Today (YYYY-MM-DD)` szekció | napi action queue (Presto `index` mód generálja) |

A fetch-path mindig a vault root-relatív (a dash-server.mjs onnan szolgál ki).

---

## 2. CAMPAIGN.md frontmatter — kötelező mezők

A dashboard ezeket parse-olja. Hiányzó kötelező mező → a kampány **nem renderelődik** (silent skip), és a Presto `audit` (későbbi mód) jelzi.

```yaml
type: campaign            # REQUIRED — a parser ezt keresi szűrőnek
area: "<ProjectName>"     # REQUIRED — group-by kulcs
title: "<...>"            # REQUIRED — card-cím
stage: <enum>             # REQUIRED — szín + szekció
owner: "<név>"            # opcionális
channels: [...]           # opcionális — chip-render
publish_date: YYYY-MM-DD  # opcionális — schedule-render
status: <enum>            # opcionális — in_progress | blocked | done
kpi_targets: {...}        # opcionális — KPI progress bar
next_action: "<...>"      # opcionális — Today panel
due: YYYY-MM-DD           # opcionális — szín-kódolás (lejárt → piros)
tags: [...]               # opcionális — filter-chip
```

**Stage enum (case-sensitive):**
`idea | brief | draft | review | scheduled | published | promoted | measured | archived`

**Status enum (case-sensitive):**
`in_progress | blocked | done`

---

## 3. CAMPAIGN.md body — parse-olt szekciók

A parser case-sensitive H2 nevekre szűr. A többit ignorálja.

| Szekció | Mit parse-ol |
|---|---|
| `## Brief` | Markdown render közvetlenül a card drawer-ben |
| `## Tasks` | `- [ ]` / `- [x]` checkbox lista + `type:` és `due:` sub-bullet-ek |
| `## Assets` | Markdown link-lista |
| `## Schedule` | Markdown table (Dátum / Csatorna / Mi / Status) |
| `## Results / Metrics` | Markdown table + win/miss bullet-ek |
| `## Iteration history` | Append-only log (legutolsó 10 jelenik meg drawer-ben) |

---

## 4. Pipeline.md formátum

```markdown
## <Stage>
- [ ] **Title** #tag1 @{YYYY-MM-DD} teaser
```

A parser:
- `## <Stage>` headert keres (case-sensitive enum)
- Alatta minden `- [ ] **...**` sort egy kampány-belépőként értelmez
- `@{YYYY-MM-DD}` = due-date
- `#tag` = tag-chip

Ha a `Pipeline.md` stage-je ÉS a `CAMPAIGN.md` `stage:` frontmatter-je **különbözik**, a `CAMPAIGN.md` az igazság. A `Pipeline.md` szinkronon-kívülisége flag-elendő.

---

## 5. `00_MARKETING_INDEX.md` formátum (Presto `index` mód által generálva)

```markdown
## Active campaigns (cross-project)

| Area | Campaign | Stage | Due | Next action |
|---|---|---|---|---|
| ExarLabs | Microsite Factory Q3 launch | draft | 2026-06-15 | Finalize blog draft v2 |

## Today (YYYY-MM-DD)

- **<Area>** → <next action> [<time?>]
- ...
```

A `## Today` szekcióban a dátum case-sensitive ISO formátum. A `today` Presto-mód ezt olvassa.

---

## 6. Dashboard UI elemei (a build-fázishoz)

A `_dashboards/marketing.html` build-kor a `vault-dashboards/CLAUDE.md` recipe-jét + `_design/DESIGN_SYSTEM.md`-t követi (canonical tokenek, hét törvény, light/dark, card-copy-ref). A specifikus szekciók:

| Szekció | Mit mutat |
|---|---|
| **Today panel** (felül) | `00_MARKETING_INDEX.md` `## Today` szekciója Area-onként csoportosítva |
| **Cross-project kanban** | Stage-oszlopok, kampány-kártyák Area-filter chip-ekkel |
| **KPI dashboard** | Aggregált metrikák Area-onként (havi/qtr toggle) |
| **Drawer** | Egy kampányra kattintás megnyitja a `CAMPAIGN.md` teljes nézetét (`Brief`, `Tasks`, `Assets`, `Schedule`, `Results`, `Iteration history`) |

---

## 7. Verziózás

Ez a kontraktus saját verzióval bír. A `CAMPAIGN.md` frontmatter / body shape változása előtt **mindig** ezt is bumpolni kell, hogy a dashboard parser tudjon hozzáigazodni.

- v0.1 (2026-05-23) — initial spec, Sales DASHBOARD_CONTRACT.md mintájára

---

## 8. Hivatkozott dokumentumok

- Capability recept: [`CLAUDE.md`](CLAUDE.md)
- Sales DASHBOARD_CONTRACT (mintaforrás): `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md`
- Vault Dashboards recipe (build-szabályok): [`../vault-dashboards/CLAUDE.md`](../vault-dashboards/CLAUDE.md)
- Design system (kanonikus tokenek): `_dashboards/_design/DESIGN_SYSTEM.md`
