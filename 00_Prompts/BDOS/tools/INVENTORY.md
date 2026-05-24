---
title: BDOS Tool Inventory — három plugin-univerzum
version: 0.1
date: 2026-05-13
author: Becze Szabolcs
status: active
description: Áttekintés minden Claude-toolról amit a BDOS-ben használunk vagy fontolóra veszünk. Három univerzum: (A) Anthropic Cowork knowledge-work plugins, (B) Claude Code Official Marketplace, (C) közösségi / harmadik fél. Brand Spine réteg-mappinggel és átfedés-elemzéssel.
id: bf26d7d1-38a0-434c-a3d5-7c1ea0e904aa
index_schema_version: 1
---

# BDOS Tool Inventory

> **Cél:** ne keverjük össze, ne duplikáljunk, ne maradjon ki értékes eszköz. Minden tool egy helyen.

## A három plugin-univerzum

| Univerzum | Forrás | Cél | Mit ad | Hány |
|-----------|--------|-----|--------|------|
| **A. Cowork** | `anthropics/knowledge-work-plugins` | Role-alapú bundle-ek nem-mérnök tudásmunkához | Skill-csomagok + slash command-ok + bundled MCP connectorok role-onként | **17 plugin** |
| **B. Claude Code Official** | `anthropics/claude-plugins-official` | Általános Claude Code marketplace | Egyedi pluginek, MCP integrációk, dev toolingok | **172 plugin** |
| **C. Közösségi / 3rd-party** | GitHub repo-k | Specializált skill-csomagok | Skillek, parancsok, MCP-k | sok |

A három **különböző telepítési útvonalon** él (Cowork: `~/Library/Application Support/Claude/local-agent-mode-sessions/.../cowork_plugins/cache/`; Official: `~/.claude/plugins/`; 3rd-party: vegyes).

---

## Mit használunk most (telepítve)

| Univerzum | Plugin | Verzió | Mire |
|-----------|--------|--------|------|
| A. Cowork | **marketing** | 1.0.0 | tartalom, kampány, brand voice |
| A. Cowork | **productivity** | 1.0.0 | task, naptár, email, chat sync |
| A. Cowork | **cowork-plugin-management** | 0.2.1 | további pluginok hangolása |
| C. 3rd-party | **ui-ux-pro-max** | 2.5.0 | design katalógus (Brand Spine 6) |
| Local (Desktop uploads) | navigator-podcast, speed-reader | — | személyes skill-ek |

A többi még nincs telepítve, de a Cowork marketplace-ben elérhető (egy paranccsal): **design**, **product-management**, **legal**, **sales**, **finance**, **data**, **customer-support**, **enterprise-search**, **engineering**, **operations**, **human-resources**, **bio-research**, **partner-built**.

---

## A. Cowork — Anthropic knowledge-work plugins

Role-alapú csomagok. Mindegyik 5–7 skill + 3–7 slash command + (jellemzően) MCP server connectorokat hoz az adott szakma tipikus tooljaihoz.

### Brand→site szempontból releváns Cowork pluginek

#### `design` — UI/UX munkafolyamat
> *„Accelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs."*

- **Skills:** `accessibility-review` · `design-critique` · `design-handoff` · `design-system-management` · `user-research` · `ux-writing`
- **Commands:** `/accessibility` · `/critique` · `/design-system` · `/handoff` · `/research-synthesis` · `/ux-copy`
- **Bundled MCPs:** Asana · Atlassian · Figma · Intercom · Linear · Notion · Slack
- **Brand Spine réteg:** **5. Narrative UX** (research-synthesis, ux-writing) · **6. Design System** (design-system-management) · **7. Build/Quality** (accessibility-review, design-critique, design-handoff)
- **Vs harmadik fél:** kiegészíti az `impeccable`-t (kritika) és `designer-skills`-et (audit). NEM industry catalogue — azt az `ui-ux-pro-max` adja.

#### `marketing` — tartalom + kampány + brand voice ✅ telepítve
> *„Create content, plan campaigns, and analyze performance across marketing channels. Maintain brand voice consistency, track competitors, and report on what's working."*

- **Brand Spine réteg:** **4. Messaging** (brand voice consistency) · **7. Copy** (content) · **Pulse** (performance analysis, competitor tracking)
- **Vs harmadik fél:** átfedés a `marketingskills` (coreyhaines31) és `brand-toolkit · messaging` (jgerton) skillekkel, de **általánosabb** — kampány, közösségi média, riport, nem csak landing copy. A három együtt egészséges.

#### `product-management` — pozicionálás, spec, roadmap
> *„Write feature specs, plan roadmaps, and synthesize user research faster. Keep stakeholders updated and stay ahead of the competitive landscape."*

- **Skills:** `competitive-analysis` · `feature-spec` · `metrics-tracking` · `roadmap-management` · `stakeholder-comms` · `user-research-synthesis`
- **Commands:** `/competitive-brief` · `/metrics-review` · `/roadmap-update` · `/sprint-planning` · `/stakeholder-update` · `/synthesize-research` · `/write-spec`
- **Bundled MCPs:** Amplitude · Amplitude-EU · ClickUp · Fireflies · Monday · Pendo · Similarweb
- **Brand Spine réteg:** **2. Market & Audience Reality** (competitive-analysis, user-research-synthesis) · **Pulse** (metrics-tracking)
- **Vs harmadik fél:** részben fedi a `brand-toolkit · positioning` skill-jét, de **általánosabb PM keret**, nem Dunford-specifikus. A `competitive-analysis` skill viszont nagyon hasznos a 2. rétegben.

#### `enterprise-search`
> *„Search across all of your company's tools in one place. Find anything across email, chat, documents, and wikis without switching between apps."*

- **Skills:** `knowledge-synthesis` · `search-strategy` · `source-management`
- **Brand Spine szempontból:** nem közvetlen, de a brand asset audit input rétegben hasznos (régi marketing anyagok feltárása).

### A többi Cowork plugin (most nem priorítás, de tudni érdemes)

| Plugin | Mit ad | Mikor lenne hasznos |
|--------|--------|---------------------|
| `legal` | NDA triage, contract review, compliance, legal brief, signature workflow. MCP: Box, Egnyte, MS365. | Sonrisa CPS / ExarLabs partnerszerződések, Ignis Academy pályázati compliance |
| `sales` | Account research, call prep, outreach, pipeline. | ExarLabs / Sonrisa CPS sales |
| `finance` | Journal entry, reconciliation, financial statements, variance analysis. | Sonrisa CPS / ExarLabs könyvelés |
| `data` | SQL, exploration, viz, dashboards, statistical analysis. | DH dashboard, Navigátor analytics |
| `customer-support` | Ticket triage, response drafting, escalation, KB. | DH ügyfélszolgálat éles indulás után |
| `bio-research` | Genomics, single-cell RNA, scientific problem selection. | Nem releváns |
| `human-resources`, `operations`, `engineering`, `partner-built` | Egyéb role-csomagok | Esetfüggő |

> A teljes Cowork lista: `~/Library/Application Support/Claude/local-agent-mode-sessions/.../cowork_plugins/marketplaces/knowledge-work-plugins/`

---

## B. Claude Code Official Marketplace (172 plugin)

Kategória-megoszlás: **78 development**, 33 productivity, 16 database, 10 security, 8 monitoring, 5 deployment, **3 design**, 2 learning, 1 testing, 1 math, 1 location.

### Anthropic-szerzői pluginek (a leginkább megbízhatóak)

#### Brand→site szempontból kulcs

| Plugin | Kategória | Mit ad |
|--------|-----------|--------|
| **`frontend-design`** | development | *„Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthetics."* ← **Az impeccable ennek a kiterjesztése!** Forrás-skill. |
| `playground` | development | Interaktív HTML playground-ok: self-contained single-file explorerek visual controlokkal. **Pont olyan, mint a `diagram.html`-ünk** — sablon design playgroundhoz. |
| `claude-md-management` | productivity | CLAUDE.md auditálás és karbantartás. A BDOS-hez közvetlen érték. |
| `claude-code-setup` | productivity | Codebase analízis → testreszabott Claude Code automatizációs ajánlások (hooks, skills, MCP, subagents). |
| `code-review` | productivity | PR review több specializált agent-tel, confidence-based score-ral. |
| `pr-review-toolkit` | productivity | Comprehensive PR review agentek. |
| `hookify` | productivity | Custom hookok markdown szabályfájlokból. |
| `plugin-dev` | development | Plugin fejlesztési toolkit — 7 expert skill (hooks, MCP, commands, agents). Ha BDOS-agentet írunk, ide kell nézni. |
| `mcp-server-dev` | development | MCP szerver építéshez skillek. |
| `skill-creator` | development | Skill létrehozás, javítás, eval, benchmark. Ha BDOS-agentet skillé alakítunk, ez kell. |
| `session-report` | productivity | Session usage HTML report — tokenek, cache, subagent-ek, skillek. |
| `commit-commands`, `discord`, `imessage`, `telegram` | productivity | Messaging bridge-ek és git workflow. |

#### Connector-pluginek (MCP servereket hoznak)

| Plugin | Connector |
|--------|-----------|
| `figma` | Figma design files, tokenek, component info |
| `notion` | Notion workspace |
| `slack` | Slack workspace |
| `atlassian` | Jira, Confluence |
| `linear` | Linear issue tracking |
| `asana` | Asana project management |
| `github`, `gitlab` | Git repo platformok |
| `airtable` | DB + UI layer |
| `intercom` | Customer support |
| `box`, `firebase`, `terraform`, `playwright` | Egyéb infra |

> **Megjegyzés:** sok ilyen connector már bundled a Cowork pluginekben (pl. design → Figma, Atlassian, Notion, Linear). A standalone változatokat akkor érdemes telepíteni, ha a Cowork bundle-en kívüli use case kell.

### Design kategória (csak 3 plugin)

1. **`frontend-design`** (Anthropic) — fent
2. **`figma`** — design fájl olvasás, token kinyerés
3. **`adobe-for-creativity`** (Adobe) — image edit, design workflow automation
4. **`miro`** (Miro) — vizuális kollaboráció (a productivity listájában van)

---

## C. Közösségi / harmadik fél

A multi-AI brainstorm során feltárt repo-k. Részletek a [Brand Spine capability CLAUDE.md](../capabilities/brand-to-site/CLAUDE.md)-ben.

| Tool | GitHub | Brand Spine réteg | Egyedi érték |
|------|--------|-------------------|---------------|
| **brand-toolkit** | jgerton/brand-toolkit | 1–4 | Dunford + StoryBrand + NN/g voice + Chris Do stylescape skillek, megosztott `brand-brief.md`, confidence score, anti-slop |
| **impeccable** | pbakaus/impeccable | 5, 7 | UI/UX design judgment, Tessl benchmark 0.82/1.00 (a `frontend-design` kiterjesztése!) |
| **ui-ux-pro-max** ✅ | nextlevelbuilder/ui-ux-pro-max-skill | 6 | 161 paletta, 99 UX guideline, 1923 font, 161 reasoning rule |
| **ux-pilot** | Sakaax/ux-pilot | 6 | Dialógus-első discovery flow + élő preview (ui-ux-pro-max kiegészítője) |
| **designer-skills** | Owl-Listener/designer-skills | 6 | 87 skill / 27 parancs, design system audit (token coverage, naming, a11y) |
| **marketingskills** | coreyhaines31/marketingskills | 4, 7, Pulse | CRO, copy, SEO, analytics, email, pricing (5700+ ⭐) |
| **Dembrandt** | (CLI + MCP) | Brand audit input | Bármely site → W3C DTCG tokenek (versenytárs-analízis) |
| **Tokven** | tokven.dev | 6 | AI design token generátor brand briefből, WCAG AA |

---

## Brand Spine réteg → tool mapping (mátrix)

| Réteg | Cowork (A) | Official (B) | 3rd-party (C) |
|-------|------------|--------------|---------------|
| **1. Brand Core** | — | — | brand-toolkit · voice |
| **2. Market & Audience Reality** | product-management · `competitive-analysis`, `user-research-synthesis` | — | brand-toolkit; Dembrandt (versenytárs) |
| **3. Positioning & Offer** | product-management · `feature-spec` (rokon) | — | brand-toolkit · positioning (Dunford) |
| **4. Messaging & Proof** | marketing · brand voice | — | brand-toolkit · messaging (StoryBrand); marketingskills |
| **5. Narrative UX + IA** | design · `user-research`, `ux-writing` | frontend-design | **impeccable** (gondolkodó mód) |
| **6. Creative Direction → Design System** | design · `design-system-management`, `design-critique` | figma, frontend-design | **ui-ux-pro-max** ✅; ux-pilot; designer-skills; Tokven |
| **7. Build + Polish + Quality Gate** | design · `accessibility-review`, `design-handoff` | frontend-design, playwright | **impeccable** (build mód) |
| **Pulse (analytics + iter)** | product-management · `metrics-tracking`; marketing | (Amplitude MCP) | marketingskills · CRO |
| **Inputs (asset audit)** | enterprise-search | — | Dembrandt |

### A mátrix olvasata

- **Stratégia (1–4):** a `brand-toolkit` (3rd) a legmélyebb és legkonkrétabb. A Cowork `marketing` + `product-management` általánosabb keret, jó komplementer.
- **Design (5–7):** három réteg egészséges metszetben dolgozik együtt — Cowork `design` (kritika + a11y + UX writing), `frontend-design` (Anthropic kódminőség), `impeccable` (judgment + craft), katalógusok (`ui-ux-pro-max` + `ux-pilot`). Nincs súlyos átfedés.
- **Pulse:** Cowork `marketing` + `product-management` adja a stratégiai mérési keretet; `marketingskills` adja a konkrét CRO-skilleket.

---

## Átfedés-térkép — hol kell tudatosnak lenni

| Átfedés-zóna | Toolok | Hogyan használjuk |
|--------------|--------|-------------------|
| **UI design judgment** | `frontend-design` (Anthropic) ←→ `impeccable` (3rd) | `impeccable` a `frontend-design` *kiterjesztése* (Tessl benchmark +0.35). → `impeccable`-t használjuk, a `frontend-design` automatikusan benne van. |
| **Design system / katalógus** | Cowork `design · design-system-management` ←→ `ui-ux-pro-max` ←→ `ux-pilot` ←→ `designer-skills` | A Cowork: az **adott projekt design system karbantartása**. A `ui-ux-pro-max` / `ux-pilot`: **industry catalogue, korrekt defaultok**. A `designer-skills`: **audit + checking**. Mindhárom más, együtt használhatók. |
| **Marketing copy** | Cowork `marketing` ←→ `marketingskills` (Corey Haines) ←→ `brand-toolkit · messaging` | Cowork: általános kampány + voice consistency. `marketingskills`: CRO + landing copy + A/B. `brand-toolkit · messaging`: StoryBrand BrandScript framework. → mind a hármat más céllal hívjuk. |
| **Pozicionálás** | Cowork `product-management · competitive-analysis` ←→ `brand-toolkit · positioning` | Cowork: általános PM versenykutatás. `brand-toolkit`: Dunford 5-komponens, specifikusabb framework. → a Dunford a strukturáltabb. |
| **Connectorok** | Cowork bundled (Figma, Notion, Slack, Atlassian, Linear, Asana) ←→ standalone (Official) | Ha már installálva a Cowork `design` plugin, a Figma connector benne van — ne installáld duplán. |

---

## Ajánlott telepítések — fontossági sorrendben

### Most azonnal hasznos (Brand Spine v0.2 validációhoz, DH pilot)

1. **Cowork `design`** — kritikus a Brand Spine 5–7. réteghez. 1 parancs.
   *Hogyan:* `/plugin` Cowork marketplace-ből (vagy a desktop appon át).
2. **Cowork `product-management`** — `competitive-analysis` és `user-research-synthesis` a 2. rétegben azonnal hasznos.
3. **`brand-toolkit` (jgerton)** — a legértékesebb harmadik fél találat. Az 1–4. réteghez nincs jobb.
   *Hogyan:* `git clone https://github.com/jgerton/brand-toolkit.git`, majd plugin-dirként hozzáadni.
4. **`marketingskills` (coreyhaines31)** — CRO + landing copy a 7. réteghez és Pulse loophoz.
   *Hogyan:* `npx add-skill coreyhaines31/marketingskills`.

### Második körben (ha a fenti négy bevált)

5. **`ux-pilot` (Sakaax)** — az `ui-ux-pro-max` dialógus-első alternatívája egy adott projektnél.
6. **`designer-skills` (Owl-Listener)** — design system audit (Premium tier-hez).
7. **`Dembrandt`** — versenytárs site → tokenek (brand audit input).

### BDOS-fejlesztéshez (nem brand-to-site, hanem BDOS belső)

8. **`plugin-dev`** (Anthropic) — ha BDOS-agentet pluginná csomagolnánk.
9. **`mcp-server-dev`** (Anthropic) — ha custom MCP-t építenénk.
10. **`claude-md-management`** (Anthropic) — vault CLAUDE.md fájlok karbantartására.
11. **`session-report`** (Anthropic) — session-szintű telemetria.
12. **`playground`** (Anthropic) — interaktív HTML playground sablonok (a `diagram.html`-hez hasonló).

### Cowork pluginek a többi BDOS pilotjához

| Pilot / Area | Ajánlott Cowork plugin |
|--------------|------------------------|
| DH éles indulás után | `customer-support` |
| Sonrisa CPS / ExarLabs | `sales`, `legal`, `finance`, `data` |
| Navigátor Podcast | `data` (csatorna analytics) — már van saját skill-csomag |
| Ignis Academy pályázat | `legal` (compliance) |

---

## Mire NEM telepítünk

- **Az Official marketplace 78 dev-plugin** java része (LSP-k, AWS-skill-ek, egyéb dev-eszközök) → ezeket projektenként hívjuk be, nem default user-scope.
- **Bio-research, partner-built** Cowork pluginek — irreleváns.
- **Spotify-ads-api, legalzoom, similarweb (standalone)** — csak ha konkrét use case van.

---

## Vizuális döntéstámogatás

- **Decision Matrix** — [`decision-matrix.html`](decision-matrix.html) — interaktív 11×12 hőtérkép tool × képesség, 8 átfedési zóna (ki nyer hol?), 5 komplementer pár, ~40 feladat-lookup. Kattintható cellák részletes magyarázattal.

## Hivatkozott

- BDOS belépő: [`../CLAUDE.md`](../CLAUDE.md)
- Brand Spine capability: [`../capabilities/brand-to-site/CLAUDE.md`](../capabilities/brand-to-site/CLAUDE.md)
- Multi-AI brainstorm: [`../brainstorm/brainstorm_brand-spine.md`](../brainstorm/brainstorm_brand-spine.md)
- Cowork marketplace fizikai elérése: `~/Library/Application Support/Claude/local-agent-mode-sessions/<session-id>/<...>/cowork_plugins/marketplaces/knowledge-work-plugins/`
- Official marketplace: `~/.claude/plugins/marketplaces/claude-plugins-official/`
- Cowork repo (publikus): `github.com/anthropics/knowledge-work-plugins`
- Official repo: `github.com/anthropics/claude-plugins-official`
