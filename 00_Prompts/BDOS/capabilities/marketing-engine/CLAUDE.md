---
title: Marketing Engine Capability
version: 0.1
date: 2026-05-23
author: Becze Szabolcs
status: active
description: Repeatable, markdown-natív módszer marketing kampányok tervezésére, futtatására, folytatására és sikerességmérésére több projekten keresztül. A Sales Engine mintáját (`02_Areas/Sonrisa/CPS/Sales/`) követi, és a Cowork `marketing` plugin (v1.2.0) 8 skilljére épül. A Presto agent (v0.1) hajtja végre.
id: ecf60642-f9d7-4821-8005-3dbfaf057c7b
index_schema_version: 1
---

# Marketing Engine — Capability v0.1

> **Mentális modell:** A Sales Engine markdown-natív mintáját adaptáljuk marketingre, **plusz egy új réteget tetejére**: cross-project áttekintés. Több projekten (Area-n) keresztül futnak kampányok, és egy aggregátor-indexen át egyszerre látható az egész.

> **Két single source of truth:**
> 1. **Per Area** — minden Area saját `Marketing/` mappája tartja a saját kampányait
> 2. **Cross-project** — `_dashboards/00_MARKETING_INDEX.md` aggregál mindent egyetlen táblába

> **Aki használja:** a **Presto** agent (executor). Az ember dönt, küld, publikál; a Presto tervez, draft-ot készít, mér, folytat.

---

## 1. Mit ad ez a capability

- **Recept** új Area marketing-rendszerének bootstrap-elésére
- **4 markdown template** (engine, kampány, pipeline, dashboard-kontraktus)
- **Skill-router szerződés** a Cowork `marketing` plugin 8 skillje és a kampány-task-típusok között
- **Cross-project index séma** és frissítési algoritmus
- **Anti-patternek** és tanulságok a Sales Engine-ből

A capability **nem** ad: kreatív stratégiát (az ember + Maestro+brand-toolkit), publish-automatizációt (ember dönti és küldi), site-buildet (Maestro).

---

## 2. Felépítés — per Area

Minden marketing-aktív Area-ban:

```
02_Areas/<ProjectName>/Marketing/
├── MARKETING_ENGINE.md      ← engine overview, KPI-k, voice, cadence (lásd template)
├── Pipeline.md              ← kanban: kampányok stage-ei (lásd template)
├── Dashboard.md             ← per-Area KPI tracker, weekly velocity (opcionális, később)
└── Campaigns/
    └── <campaign-slug>/
        ├── CAMPAIGN.md      ← egy kampány = egy fájl, PRIMARY STATE (lásd template)
        ├── brief.md         ← /marketing:campaign-plan output (opcionális)
        └── assets/          ← draftok, képek, csv-k
```

**Kötelező az alapindításnál:** `MARKETING_ENGINE.md` + `Pipeline.md`. A `Dashboard.md` később jöhet, ha kell.

---

## 3. Cross-project index — `_dashboards/00_MARKETING_INDEX.md`

A Presto `index` mód aggregálja minden Area `Pipeline.md`-jét + aktív `CAMPAIGN.md`-ket. Két szekció:

```markdown
## Active campaigns (cross-project)
| Area | Campaign | Stage | Due | Next action |

## Today (YYYY-MM-DD)
- **<Area>** → <next action> <time?>
```

A `_dashboards/marketing.html` dashboard (Fázis 3, később) ezt fetcheli élőben. A `today` és `status` Presto-mód ezt olvassa.

---

## 4. Pipeline-stage-ek

Marketing-specifikus, NEM a sales pipeline-t hozzuk át:

```
idea → brief → draft → review → scheduled → published → promoted → measured → archived
```

| Stage | Definíció |
|---|---|
| **idea** | Ötlet, még nincs validálva |
| **brief** | `/marketing:campaign-plan` kész, célok+audience+message megvan |
| **draft** | Tartalom-darab(ok) készülnek (`/marketing:draft-content`, `/marketing:email-sequence`) |
| **review** | Draft kész, `/marketing:brand-review` fut vagy emberi review |
| **scheduled** | Approved, kitűzve, vár a publish-időre |
| **published** | Élesben, csatornán kint van |
| **promoted** | Másodlagos csatornákon megosztva, boost / community share |
| **measured** | `/marketing:performance-report` lefutott, KPI tudható |
| **archived** | Lezárt, lessons learned dokumentálva, file áthelyezve |

A `Pipeline.md`-ben minden stage egy `## <Stage>` szekció, alatta `- [ ] **Campaign Title** #tag @{due} teaser` formátumú sorok.

---

## 5. Skill-router — a Cowork `marketing` plugin 8 skillje

A Presto `run` mód a `CAMPAIGN.md` aktuális open task-jának `type:` mezője alapján route-ol:

| Task `type:` | Hívott skill | Mit ad |
|---|---|---|
| `content-draft` | `/marketing:draft-content` | Blog / social / email / landing copy |
| `content-review` | `/marketing:brand-review` | Voice + style + claim audit egy drafton |
| `email-flow` | `/marketing:email-sequence` | Multi-email szekvencia copy + timing + branching |
| `seo-task` | `/marketing:seo-audit` | SEO-egészség, keyword + content gap |
| `competitor-research` | `/marketing:competitive-brief` | Versenytárs-elemzés |
| (plan módban) | `/marketing:campaign-plan` | Teljes kampány-brief |
| (measure módban) | `/marketing:performance-report` | KPI riport |
| (internal, helper) | `/marketing:content-creation` | Tartalom-keretek (a többi skill belsőleg) |

**Ha a task `type:` mező hiányzik vagy ismeretlen** → Presto nem találgat, hanem kérdez vissza melyik skillt használja.

---

## 6. Bootstrap új Area-ra — checklist

Új Area-ra a Presto-ot először a `plan` mód indítja, de manuálisan is bootstrap-elhető:

1. **Mappa**: `02_Areas/<Area>/Marketing/` létrehozás + `Campaigns/` almappa
2. **Engine fájl**: másold a `MARKETING_ENGINE.md.template`-et, töltsd ki (audience, voice, KPI-ramp, cadence)
3. **Pipeline fájl**: másold a `PIPELINE.md.template`-et, üres szekciókkal
4. **(Opcionális) Dashboard fájl**: ha már van mérendő, másold a Dashboard-templatet
5. **Első kampány**: futtasd `/pres-plan --area=<Area> --objective="..."`-t, a Presto a `Campaigns/<slug>/` alá teszi a `CAMPAIGN.md`-t + `brief.md`-t
6. **Index frissítés**: futtasd `/pres-index`-et, az Area megjelenik a cross-project táblában

---

## 7. Anti-patternek (NE ezt csináld)

- ❌ **Publish helyetted az AI**: soha. A publish/send emberi akció. A draft `ready`-re kerül, az ember küldi.
- ❌ **Cross-Area copy-paste**: minden Area-nak saját voice + KPI van. NE használj egy másik Area MARKETING_ENGINE.md-jét default-ként.
- ❌ **HTML szerkesztés**: a `_dashboards/marketing.html` (ha lesz) auto-fetcheli a markdown source-okat. Soha nem szerkeszted az HTML-t kézzel.
- ❌ **Stage-skip nyomon-követés nélkül**: ha egy kampány `brief` → `published`-ra ugrik, az Iteration history-ban dokumentáld miért (pl. urgent, sablon-alapú).
- ❌ **Index hígítása**: a `00_MARKETING_INDEX.md`-t csak a Presto `index` mód írja. `today`/`status` csak olvas.
- ❌ **Aktivációs gate hiánya**: a Sales Engine tanulsága szerint a v1.0 infrastruktúra megépülése ≠ engine running. Az új Area "marketing-aktiváltnak" akkor minősül, amikor **az első kampány `published` stage-be ér**, NEM amikor az engine-fájlok megvannak.

---

## 8. Tanulságok a Sales Engine-ből (rip-and-replace, hol érvényes)

| Sales Engine minta | Marketing Engine megfelelője |
|---|---|
| `Accounts/Leads/<Name>/NOTES.md` per lead | `Campaigns/<slug>/CAMPAIGN.md` per kampány |
| `Pipeline.md` kanban stage-ek | Ugyanaz, marketing stage-ekkel (lásd §4) |
| `Dashboard.md` KPI tracker | Per-Area Dashboard.md (opcionális) |
| 90-day clock + KPI ramp | Per-Area cadence target (heti/havi publish), nem fix reset |
| Verify-before-send gate | Verify-before-publish: a kampány még releváns-e (>7 nap olds esetén relevancia-check) |
| `seen-companies.md` dedup | (opcionális) `seen-topics.md` per Area, hogy ne ismételjünk content-ötletet |
| Scraper protocol (job board → lead) | Kampány-trigger (content calendar slot, competitor publish, seasonal hook) |
| Multi-AI brainstorm (think-engine) | Ugyanaz — kreatív kampány-ötlethez |

---

## 9. Hivatkozott dokumentumok

- Presto agent canonical: [`../../agents/presto.md`](../../agents/presto.md)
- Cowork `marketing` plugin: `~/.claude/plugins/marketplaces/knowledge-work-plugins/marketing/`
- Sales Engine (testvér-rendszer): `02_Areas/Sonrisa/CPS/Sales/SALES_ENGINE.md`
- Vault Dashboards capability: [`../vault-dashboards/CLAUDE.md`](../vault-dashboards/CLAUDE.md)
- BDOS belépő: [`../../CLAUDE.md`](../../CLAUDE.md)
- Templatek ebben a mappában: `MARKETING_ENGINE.md.template`, `CAMPAIGN.md.template`, `PIPELINE.md.template`, `DASHBOARD_CONTRACT.md`
