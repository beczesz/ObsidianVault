---
title: Presto Marketing Engine — Flow v0.2
version: 0.2.0
date: 2026-05-25
author: Becze Szabolcs
status: draft
description: Normatív v0.2 modell a Presto Marketing Engine-hez. Leírja a 2-entitásos szubsztrátumot (Seed + Publication), az opcionális Campaign esernyőt, a 6-stage kanban flow-t és a per-Area Publications könyvtár-konvenciót. Supersedes a v0.1 SEED/INTENT/MATCH/PUBLICATION négyes-modelljét.
id: 9693547e-7969-4e6f-91d4-31951fde8bfd
index_schema_version: 1
bdos_index: true
tags: [presto, marketing-engine, flow, architecture, substrate]
---

# Presto Marketing Engine — Flow v0.2

> **Alapelv:** az ember a forrás, a rendszer a memória. Minden publikációs szándék emberből indul, de Presto javasolhat. A szubsztrátum egyszerű: két entitás (Seed, Publication) + egy opcionális esernyő (Campaign). Minden más ebből következik.

---

## 1. Reconciliation — v0.1 vs. v0.2

A `MARKETING_OS_ARCHITECTURE.md` (v0.1) 6 új markdown entitást vezetett be:

```
v0.1: PUBLICATION · CHANNEL_DNA · COMMENT · TODO · INSIGHT · TEMPLATE
```

Ezek az entitások **mind érvényesek maradnak** a Marketing OS működési rétegén (lásd `MARKETING_OS_ARCHITECTURE.md` §3). Ami v0.2-ben egyszerűsödik: a **szubsztrátum modell** — az az alap, amelyből a tartalom megszületik.

**v0.1 szubsztrátum (négyes-modell, superseded):**
```
SEED → INTENT (külön entitás) → MATCH (külön entitás) → PUBLICATION
```

**v0.2 szubsztrátum (duó-modell, normatív):**
```
SEED → PUBLICATION
       (intent beágyazott frontmatterben)
       (channel+area = match, beágyazott frontmatterben)
```

**Mi marad változatlanul érvényes a v0.1-ből:**
- `CHANNEL_DNA.md` — cross-project kanonikus csatorna-definíciók
- `COMMENT.md` — komment lifecycle
- `TODO.md` — operacionális inbox
- `INSIGHT.md` — megfigyelés-lifecycle
- `TEMPLATE.md` — struktúra-minták
- Publication-as-atom modell (a Publication az elsődleges atom)
- Engine-pull modell (Presto soha nem cselekszik magától)

**Mi változik v0.2-ben:**
- Az `INTENT` NEM önálló entitás/fájl — beolvad a Publication `intent:` blokkjába
- A `MATCH` NEM önálló entitás/fájl — a `channel:` + `area:` frontmatter mezők fedik le
- A SEED perzisztens (nem konzumálódik draft-átmenetnél)
- A Campaign mint esernyő opcionális — null = standalone Publication

---

## 2. A három entitás szerepe és kapcsolata

### 2.1 SEED — az inbox-elem

**Mi:** a raw input, az ötlet csírája. Bármilyen forrásból jöhet (URL, inline szöveg, atomikus gondolat-ref, BMC negyedből, képből, más médiaból).

**Perzisztencia:** a Seed **addig aktív, amíg a user nem mondja: "kinyertük belőle mindent"**. Nem töröljük, nem mozgatjuk draft-átmenetnél. Egy Seed → N Publication kapcsolat lehetséges (különböző Area-kban, különböző intent-ekkel).

**Hely:** `00_Prompts/BDOS/agents/presto/_inbox/seeds/<seed-id>.md`

**Lifecycle:** `active → exhausted → archived`

**Invariáns:** a Seed soha nem tartalmaz kész tartalmat — csak a forrást és a metadatát. A tartalom a Publication-ökben él.

### 2.2 PUBLICATION — a központi atom

**Mi:** egyetlen publikálható egység. Tartalmaz mindent, ami az életciklusa során szükséges: szándék, csatorna, terület, draft szöveg, variációk, schedule, approval trail, analytics.

**Az egyetlen igazság forrása** egy adott tartalom-darab életciklusáról.

**Hely:** `02_Areas/<ProjectName>/Marketing/Publications/<pub-id>.md`

**Naming:** `<pub-id>` = `<channel>-<YYYY-MM-DD>-<seq>` (pl. `linkedin-2026-05-28-001`)

**Lifecycle (6 stage):** Seed → Draft → Prepared → Approval → Scheduled → Published

**Kapcsolat Seed-del:** `seed_ref:` frontmatter mező (opcionális, ha nem seed-ből származik)

**Kapcsolat Campaign-nel:** `campaign_id:` frontmatter mező (opcionális, null = standalone)

### 2.3 CAMPAIGN — az opcionális esernyő

**Mi:** aggregálja azokat a Publication-öket, amelyek egyazon szándék-csoporthoz tartoznak. Tipikus eset: ugyanaz a Seed több Area-ban, több intent-tel jelenik meg → kell egy aggregátum.

**Opcionális:** ha egy Publication standalone, `campaign_id: null` és nincs Campaign-fájl.

**Hely:** `_dashboards/00_MARKETING_INDEX.md` alatti kampány-blokkok, VAGY per-Area `Marketing/Campaigns/<campaign-slug>/CAMPAIGN.md` (a v0.1 schema marad érvényes esernyő-szinten)

**Invariáns:** a Campaign egy koordinációs objektum, nem tartalom-forrás. A tartalom kizárólag Publication-ökben él.

---

## 3. A 6-stage kanban flow

```
┌────────┐   ┌───────┐   ┌──────────┐   ┌──────────┐   ┌───────────┐   ┌───────────┐
│  SEED  │──▶│ DRAFT │──▶│ PREPARED │──▶│ APPROVAL │──▶│ SCHEDULED │──▶│ PUBLISHED │
│(inbox) │   │       │   │  (volt:  │   │          │   │           │   │(=Measuring│
│        │   │       │   │  Polish) │   │          │   │           │   │  30 napig)│
└────────┘   └───────┘   └──────────┘   └──────────┘   └───────────┘   └───────────┘
```

### Lane: SEED

**Mit jelent:** raw input, amely még nem vált Publication-né.

**Belép:** amikor a user (vagy Presto, user jóváhagyásával) behoz egy új ötletet/forrást.

**Kilép:** amikor legalább egy Publication születik belőle (de maga a Seed aktív marad).

**State változás:** `status: active` marad mindaddig, amíg a user `exhausted`-re nem állítja.

**Fájl:** `_inbox/seeds/<seed-id>.md` (schema: `presto.seed.v1`)

### Lane: DRAFT

**Mit jelent:** a Publication létrejött a Seed-ből (vagy direkten), szövegváz van, de még nincs készen az emberi review-ra.

**Belép:** Presto `adapt` mód futtatásakor, vagy user manuálisan hoz létre egy Publication-t.

**Kilép:** amikor a copy- és format-munka befejeződött, készen van review-ra.

**State változás:** `publication_status: draft` → `needs_review`

**Felelős akció:** `/marketing:draft-content` skill, majd user + Presto iteráció.

### Lane: PREPARED (volt: Polish)

**Mit jelent:** a tartalom review-n átment, vizuális eszközök (képek, carousel slide-ok) elkészültek, a szöveg végleges. Emberi jóváhagyásra vár.

**Belép:** amikor a szöveg elérte a végleges állapotot és az összes asset megvan.

**Kilép:** az Approval lane-be lép, amikor a user `approved`-ra állítja.

**State változás:** `publication_status: needs_review` → `approved` (Approval lane belépése)

### Lane: APPROVAL

**Mit jelent:** a Publication jóváhagyásra vár. A user explicit döntést hoz (approve / reject / request-change).

**Belép:** Prepared lane-ből, emberi döntéssel.

**Kilép:** approve után Scheduled lane-be lép; reject esetén visszamegy Draft-ba.

**State változás:** `approval_status: pending` → `approved` VAGY `rejected`

**Invariáns:** publication soha nem lép Scheduled-be emberi approve nélkül.

### Lane: SCHEDULED

**Mit jelent:** jóváhagyott, ütemezett tartalom. Meghatározott időpontban várja a publikálást.

**Belép:** Approval lane-ből, `scheduled_time` kitöltésével.

**Kilép:** a Publication megjelenik a csatornán (Presto `publish` módja végzi, emberi triggerrel vagy scheduled-del).

**State változás:** `publication_status: scheduled` → `published`

### Lane: PUBLISHED (= Measuring, 30 napig)

**Mit jelent:** a tartalom élő. Az első 30 napban a `analytics_status: not-collected → collected` átmenet figyelhető. 30 nap után archivált.

**Belép:** sikeres publikáció után.

**Kilép:** 30 nappal a publikálás után → `publication_status: archived` (Archive nem lane, külön screen lesz P6-ban).

**State változás:** `publication_status: published` → (30 nap után) `archived`

**Anti-pattern:** az Archive NEM lane a kanbanan — nem jelenítjük meg a napi flow-ban.

---

## 4. Intent — beágyazott, nem külön entitás

Az Intent **nincs** külön fájlban. Minden Publication frontmatterében él egy `intent:` blokk:

```yaml
intent:
  goal: thought-leadership        # thought-leadership | seo-lead-gen | community | announcement | nurture
  audience_segment: tech-leaders  # ki olvassa ezt
  desired_action: follow          # mi legyen az olvasó következő lépése
  source: human                   # human | suggested-by-presto-then-approved
  notes: "Q2 BDOS positioning narrative"
```

**Forrás-tag:** az Intent mindig emberből indul. De Presto javasolhat intent-et → user jóváhagyja → `source: suggested-by-presto-then-approved`. Ez az audit trail.

---

## 5. Match (Channel + Area) — beágyazott, nem külön entitás

A channel + Area párosítás a Publication frontmatterének `channel:` és `area:` mezőiben él:

```yaml
channel: linkedin                 # references presto/channel-dna/linkedin.md
area: ExarLabs                    # melyik Area brand-voice-át használjuk
```

Az operatív csatorna-szabályok a Channel DNA-ban élnek (lásd `channel-dna/<channel>.md`). A Publication csak hivatkozik rájuk — nem duplikálja.

---

## 6. Per-Area Publications könyvtár-konvenció

A v0.1 campaign-nested struktúra (`Campaigns/<slug>/publications/<pub-id>.md`) megmarad kampányos esetekre. A v0.2-ben bevezetett **standalone Publication** egy egyszerűbb útvonalat is támogat:

```
02_Areas/<ProjectName>/Marketing/
├── MARKETING_ENGINE.md          ← engine overview, KPI-k, voice, cadence (meglévő)
├── Pipeline.md                  ← kanban: kampányok stage-ei (meglévő)
├── Dashboard.md                 ← per-Area KPI tracker (meglévő)
├── Publications/                ← ÚJ — standalone és kampányhoz nem kötött publication-ök
│   └── <pub-id>.md              ← pl. linkedin-2026-05-28-001.md
└── Campaigns/
    └── <campaign-slug>/
        ├── CAMPAIGN.md          ← kampány esernyő (meglévő schema, v0.1)
        └── publications/        ← kampányhoz kötött publication-ök (v0.1 path megmarad)
            └── <pub-id>.md
```

**Routing döntés:**
- `campaign_id: null` → `Marketing/Publications/<pub-id>.md`
- `campaign_id: <slug>` → `Marketing/Campaigns/<slug>/publications/<pub-id>.md`

Ez a döntés a Publication létrehozásakor születik. Utólag áthelyezhető, de a `pub-id` stabil marad.

---

## 7. Engine-pull modell (manuális indulás, lépésről-lépésre automatizálva)

A Marketing Engine **soha nem cselekszik önállóan** publikáció-generálásban. Minden lépés:

1. User (vagy Presto javaslata + user approve) → Seed bekerül az inbox-ba
2. User kéri a draft-ot → Presto bemutatja a tervet (confirmation gate) → user approve → draft elkészül
3. User Prepared-re állítja → Approval lane-be kerül
4. User approve-ol → Scheduled
5. User triggereli (vagy scheduled job) → `publish` mód → Presto végrehajtja → Published

Az automatizálás a later phase-ekben épül rá (P3+), de az emberi döntési pontok megmaradnak az Approval és a Publish-trigger lépéseknél.

---

## 8. Schema referenciák

A három entitás teljes schema-specifikációja a kísérő fájlban él:

`00_Prompts/BDOS/agents/presto/MARKETING_OS_SCHEMAS_v2.md`

Gyors áttekintés:

| Entitás | Schema ID | Hely |
|---|---|---|
| Seed | `presto.seed.v1` | `_inbox/seeds/<seed-id>.md` |
| Publication | `presto.publication.v2` | `Marketing/Publications/<pub-id>.md` VAGY `Campaigns/<slug>/publications/<pub-id>.md` |
| Campaign | `presto.campaign.v2` | `Marketing/Campaigns/<slug>/CAMPAIGN.md` |

---

## 9. Worked example referencia

Szintetikus seed + 3 publication + 1 campaign esernyő demonstrációja:

`00_Prompts/BDOS/agents/presto/_examples/marketing-engine-v2/`

| Fájl | Mit demonstrál |
|---|---|
| `seed-bdos-markdown-substrate.md` | SEED lifecyclé, source_type, publications_spawned |
| `campaign-bdos-positioning-q2-2026.md` | Campaign esernyő, multi-intent, multi-area |
| `pub-linkedin-001-exarlabs.md` | LinkedIn publication, ExarLabs area, thought-leadership intent |
| `pub-x-thread-001-personal.md` | X thread, Personal area, developer community intent |
| `pub-blog-001-exarlabs.md` | Blog post, ExarLabs area, SEO+lead-gen intent |

---

## Changelog

- **0.2.0 (2026-05-25)** — initial v0.2 flow spec. Supersedes SEED/INTENT/MATCH/PUBLICATION v0.1 quadruple with SEED+PUBLICATION duó modell. Campaign marad opcionális esernyőként. Intent + Match beágyazva. 6-stage kanban (Seed/Draft/Prepared/Approval/Scheduled/Published). Per-Area Publications könyvtár-konvenció. Engine-pull modell dokumentálva.
