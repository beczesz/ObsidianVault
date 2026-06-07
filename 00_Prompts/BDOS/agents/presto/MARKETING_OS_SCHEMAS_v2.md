---
title: Presto Marketing Engine — Schemas v0.2
version: 0.2.0
date: 2026-05-25
author: Becze Szabolcs
status: draft
description: Teljes schema-specifikáció a Presto Marketing Engine v0.2 három entitásához: presto.seed.v1 (inbox-fájl), presto.publication.v2 (fő atom, 6-stage lifecycle), presto.campaign.v2 (esernyő). Minden mező 1-soros magyarázattal, kötelező/opcionális jelöléssel és példa YAML-lel.
id: d1335407-be0d-4905-aaf1-7435c643a42f
index_schema_version: 1
bdos_index: true
tags: [presto, marketing-engine, schema, substrate]
---

# Presto Marketing Engine — Schemas v0.2

> Minden schema kötelező `schema:` frontmatter-mezővel indul — ez az egyetlen egyértelmű gép-olvasható típus-azonosító. Minden mező mellett jelölt: **K** = kötelező, **O** = opcionális.

---

## 1. `presto.seed.v1` — az inbox-elem *(superseded by v2 — lásd §1b)*

**Hely:** `00_Prompts/BDOS/agents/presto/_inbox/seeds/<seed-id>.md`

**Naming:** `seed-<YYYY-MM-DD>-<NNN>` ahol NNN = napi sorrend (001, 002, ...)

**Mikor hozzuk létre:** amikor új raw input (URL, gondolat, kép, forrás) érkezik, amelyből később Publication születhet.

**Invariáns:** a Seed soha nem tartalmaz kész tartalmat. Addig aktív, amíg a user nem mondja „kinyertük belőle mindent".

### Schema

```yaml
---
schema: presto.seed.v1              # K — típus-azonosító, gép olvassa
seed_id: seed-2026-05-25-001        # K — stabil, egyedi azonosító
title: "BDOS atomic note thought — markdown-as-substrate"  # K — rövid, leíró cím

source_type: inline-text            # K — az input forrásának típusa
                                    #   url: weblap, cikk, tweet URL
                                    #   inline-text: beírt szöveg, idézet
                                    #   atomic-ref: Sage atomic fájl hivatkozása
                                    #   bmc-quadrant: Business Model Canvas negyed
                                    #   image-ref: kép fájl-path
                                    #   other: minden más

source_ref: |                       # K — a konkrét forrás (URL, fájl-path, szöveg, atomic-id)
  "A markdown fájl egyenlő a szubsztrátummal. Nem dokumentálás, hanem gondolkodási felszín.
   A rendszer olvasható ember és AI által, nem kell kompilálni, nem kell deploy."

captured_at: 2026-05-25T10:00+02:00 # K — mikor vettük fel (ISO 8601 + TZ)
captured_by: Becze Szabolcs         # K — ki vette fel (nem AI, mert az ember kezdeményez)

status: active                      # K — lifecycle állapot
                                    #   active: még aktív, lehet belőle Publication
                                    #   exhausted: a user lezárta ("mindent kinyertünk")
                                    #   archived: hosszabb inaktivitás után archiválva

exhausted_at: null                  # O — mikor mondtuk hogy "kinyertünk belőle mindent"
                                    #   null ha még aktív; ISO timestamp ha lezárt

publications_spawned:               # O — ebből a seedből született Publication-ök ID-listája
  - pub-id: linkedin-2026-05-28-001
    area: ExarLabs
    created_at: 2026-05-28T09:00+02:00
  # append-only: minden új pub hozzáadódik, sosem törlünk

tags: [bdos, markdown, substrate, thought-leadership]  # O — keresési és szűrési tagek

notes: |                            # O — szabad szöveges megjegyzések
  Ez a gondolat a BDOS egyik alapítói tézise: a markdown NEM tárolás, hanem gondolkodás.
  Potenciálisan több Area-ban is releváns (ExarLabs, Personal, Navigátor Podcast).
---

## Seed body

A forrásból kivont gondolat, vagy az eredeti forrás copy-paste-je (strukturálatlan, nyers).
A szöveg itt NEM a végleges publikáció — az a Publication-ökben él.

<raw notes, összefoglalás, copy-paste a forrásból>
```

### Mező-összefoglaló

| Mező | K/O | Magyarázat |
|---|---|---|
| `schema` | K | Gép-olvasható típus-azonosító — mindig `presto.seed.v1` |
| `seed_id` | K | Stabil, egyedi ID — nem változik a lifecycle során |
| `title` | K | Rövid, leíró cím — embernek, nem gépnek |
| `source_type` | K | Az input kategóriája — meghatározza hogyan dolgozzuk fel |
| `source_ref` | K | A konkrét forrás — URL / path / inline szöveg |
| `captured_at` | K | Felvétel időpontja — audit trail |
| `captured_by` | K | Ki vette fel — mindig ember (Presto csak javasol) |
| `status` | K | Lifecycle: active / exhausted / archived |
| `exhausted_at` | O | Mikor lett "kinyerve" — null amíg aktív |
| `publications_spawned` | O | Belőle született Publication-ök listája (append-only) |
| `tags` | O | Keresési tagek |
| `notes` | O | Szabad megjegyzés, kontextus |

---

## 1b. `presto.seed.v2` — az inbox-elem (v2)

> **v2 supersedes v1 (2026-05-26).** A v1 schemát megtartjuk backward-compat-hoz — v1 seedek változatlanul működnek. Új seedeket v2-vel kell létrehozni.

**Változások v1 → v2:**
- `schema: presto.seed.v2` (kötelező v2-jelölés)
- `short_description` mező (kötelező) — dashboard kanban-kártya 1-soros leírás
- `runbook_ref` mező (opcionális) — melyik runbook triggere ez a seed
- `campaign_ref` mező (opcionális, jelenleg NULL) — campaign-esernyő pointer (later)
- `prerequisites` tömb (opcionális) — TODO-lista prereq-ekkel
- `distribution_timeline` tömb (opcionális) — strukturált multi-platform terv
- `status` enum bővítve (6 értékre)

### Schema

```yaml
---
schema: presto.seed.v2              # K — típus-azonosító, gép olvassa

# --- Azonosítók (v1-vel azonos) ---
seed_id: seed-2026-05-26-001        # K — stabil, egyedi azonosító
title: "EP43 Gyász — multi-platform launch"  # K — rövid, leíró cím

# --- v2 ÚJ: Dashboard leírás ---
short_description: "Egy sor leírás a kanban-kártyához. NE keverendő a frontmatter description:-vel (az index-search-hez van)."
                                    # K (v2-ben) — 1-2 mondat max
                                    # Cél: dashboard kártya, gyors scan emberi szemmel

# --- Runbook / Campaign pointer ---
runbook_ref: episode-launch         # O — melyik runbookra hivatkozik; null ha nincs runbook-trigger
campaign_ref: null                  # O — melyik campaign-esernyőhöz tartozik; most null (later aktiválódik)

# --- Forrás (v1-vel azonos) ---
source_type: other                  # K — url | inline-text | atomic-ref | bmc-quadrant | image-ref | other
source_ref: "[[path/to/source]]"    # K — a konkrét forrás
captured_at: 2026-05-26T09:00+02:00 # K — ISO 8601 + TZ
captured_by: Becze Szabolcs         # K — ki vette fel

# --- v2 BŐVÍTETT status enum ---
status: in_prep                     # K — lifecycle állapot
                                    #   in_prep:           van pending prerequisite
                                    #   ready:             minden prereq done, de még nincs spawned publication
                                    #   active:            legalább 1 publication spawned, még nincs minden done
                                    #   partially_spawned: N publication spawned, de a runbook-tervezett count nem teljes
                                    #   exhausted:         user explicit lezárta (emberi döntés)
                                    #   archived:          retired

exhausted_at: null                  # O — null ha aktív; ISO timestamp ha lezárt

# --- v2 ÚJ: Prerequisites (TODO-lista) ---
prerequisites:                      # O — runbook-ból vagy user által definiált prereq lista
  - id: prereq-001                  # K (prereq-en belül) — stabil ID
    description: "Felvétel elkészült"  # K — mit kell elvégezni
    status: pending                 # K — pending | in_progress | done | skipped
    owner: user                     # K — ki felel
    due_date: 2026-05-29            # O — YYYY-MM-DD
    notes: ""                       # O — szabad megjegyzés

# --- v2 ÚJ: Distribution timeline (strukturált multi-platform terv) ---
distribution_timeline:              # O — platform-lépések listája
  - step: T+0                       # K (elem-en belül) — T+N jelölés
    date: 2026-05-29                # K — ISO date, mikor fut
    channels: [youtube, spotify]    # K — érintett csatornák
    pub_type: launch                # K — launch | reel | followup | teaser | stats
    notes: "Elsődleges launch"      # O — szabad megjegyzés

publications_spawned: []            # O — ebből a seedből született Publication-ök (append-only)

tags: []                            # O
description: ""                     # K (frontmatter) — index-search-hez (NEM short_description!)
---

## Seed body

<raw notes, összefoglalás, a forrás szövege>
```

### Mező-összefoglaló

| Mező | K/O | Magyarázat |
|---|---|---|
| `schema` | K | Típus-azonosító — `presto.seed.v2` |
| `seed_id` | K | Stabil egyedi ID |
| `title` | K | Rövid, leíró cím (ember-olvasható) |
| `short_description` | K (v2) | Dashboard kanban-kártya leírás — 1-2 mondat. NEM az index `description:` |
| `runbook_ref` | O | Melyik runbookra hivatkozik (pl. `episode-launch`). null = nincs runbook-trigger |
| `campaign_ref` | O | Melyik campaign-esernyőhöz tartozik. Jelenleg null — later aktiválódik |
| `source_type` | K | Forrás kategóriája |
| `source_ref` | K | Konkrét forrás |
| `captured_at` | K | Felvétel időpontja (ISO 8601 + TZ) |
| `captured_by` | K | Ki vette fel |
| `status` | K | Lifecycle (6 érték): `in_prep \| ready \| active \| partially_spawned \| exhausted \| archived` |
| `exhausted_at` | O | null ha aktív; ISO ha lezárt |
| `prerequisites[].id` | K (elem) | Stabil prereq ID (`prereq-<NNN>`) |
| `prerequisites[].description` | K (elem) | Mit kell elvégezni |
| `prerequisites[].status` | K (elem) | `pending \| in_progress \| done \| skipped` |
| `prerequisites[].owner` | K (elem) | Ki felel |
| `prerequisites[].due_date` | O | YYYY-MM-DD |
| `prerequisites[].notes` | O | Szabad megjegyzés |
| `distribution_timeline[].step` | K (elem) | T+N jelölés |
| `distribution_timeline[].date` | K (elem) | ISO date |
| `distribution_timeline[].channels` | K (elem) | Csatornák tömbje |
| `distribution_timeline[].pub_type` | K (elem) | `launch \| reel \| followup \| teaser \| stats` |
| `distribution_timeline[].notes` | O | Szabad megjegyzés |
| `publications_spawned` | O | Belőle született Publication-ök (append-only) |
| `tags` | O | Keresési tagek |

### Computed mező (sidecar által — NEM a markdown-ban)

| Mező | Típus | Compute logika |
|---|---|---|
| `todos_count` | `{pending, in_progress, done, skipped, total}` | A `prerequisites` array `status` értékeit aggregálja csoportonként; `total` = mind |

> **Backward compat:** v1 seedek (`schema: presto.seed.v1`) változatlanul működnek. A sidecar generator mindkét schema-t parse-olja. v2-mezők v1-en alapértelmezett értékkel jelennek meg a sidecar JSON-ban (`short_description: ""`, `runbook_ref: null`, `campaign_ref: null`, `prerequisites: []`, `distribution_timeline: []`, `todos_count: {pending:0,…,total:0}`).

---

## 2. `presto.publication.v2` — a fő atom

**Hely:**
- Standalone: `02_Areas/<ProjectName>/Marketing/Publications/<pub-id>.md`
- Kampányhoz kötve: `02_Areas/<ProjectName>/Marketing/Campaigns/<slug>/publications/<pub-id>.md`

**Naming:** `<channel>-<YYYY-MM-DD>-<seq>` (pl. `linkedin-2026-05-28-001`)

**Invariáns:** egy Publication = egy fájl, az életciklusa teljes egyedül. Intent, channel, area, body, variációk, schedule, approval trail, analytics — mind ebben.

### Schema

```yaml
---
schema: presto.publication.v2                       # K — típus-azonosító

# --- Azonosítók ---
publication_id: linkedin-2026-05-28-001             # K — stabil, egyedi ID
seed_ref: seed-2026-05-25-001                       # O — forrás Seed ID, null ha direkt
campaign_id: bdos-positioning-q2-2026               # O — Campaign esernyő slug, null ha standalone

# --- Helymeghatározás ---
area: ExarLabs                                      # K — melyik Area brand-voice-át használjuk
                                                    #   ez határozza meg a tone-t, audience-t
channel: linkedin                                   # K — melyik csatornára megy
                                                    #   references presto/channel-dna/<channel>.md

# --- Tartalom paraméterek ---
format: long-post                                   # K — channel DNA-ban definiált formátum
language: en                                        # K — ISO 639-1; channel DNA default override-olható

# --- Intent blokk (beágyazott, nem külön entitás) ---
intent:
  goal: thought-leadership                          # K — publikáció célja
                                                    #   thought-leadership: pozícionálás, brand-építés
                                                    #   seo-lead-gen: organikus elérés, lead-szerzés
                                                    #   community: kapcsolat-építés, network
                                                    #   announcement: hír, frissítés
                                                    #   nurture: meglévő közönség ápolása
  audience_segment: tech-leaders-and-founders       # K — kinek szól ez a konkrét tartalom
  desired_action: follow-and-engage                 # K — mi legyen az olvasó következő lépése
  source: human                                     # K — ki határozta meg az intent-et
                                                    #   human: ember írta/döntötte
                                                    #   suggested-by-presto-then-approved: Presto javasolta, ember jóváhagyta
  notes: "Q2 BDOS positioning — markdown-as-substrate tézis"  # O — szabad magyarázat

# --- Lifecycle ---
publication_status: draft                           # K — kanban lane
                                                    #   draft: szövegváz, még nincs review-ra kész
                                                    #   needs_review: kész, emberi review kell
                                                    #   approved: ember jóváhagyta
                                                    #   scheduled: ütemezett, vár a publikálásra
                                                    #   publish_pending: publikálás folyamatban
                                                    #   published: élő
                                                    #   failed: publikálás sikertelen
                                                    #   manual_required: API+MCP is failed, kézi kell
                                                    #   archived: 30 nap published után
approval_status: pending                            # K — emberi jóváhagyás állapota
                                                    #   pending: vár
                                                    #   approved: jóváhagyva
                                                    #   rejected: visszautasítva (visszamegy draft-ba)
                                                    #   revoked: post-approval visszavonás

# --- Schedule ---
scheduled_time: null                                # O — ISO 8601 + TZ; null ha nincs konkrét időpont
planned_publish_date: 2026-05-28                    # O — YYYY-MM-DD; time board placement ha unscheduled

# --- Kapcsolatok ---
linked_atomic_thoughts:                             # O — Sage atomic hivatkozások
  - "[[atomic/markdown-as-substrate-thesis]]"
linked_insights:                                    # O — releváns Presto Insight hivatkozások
  - "[[presto/insights/2026-05-15_long-form-resonance]]"
visual_assets:                                      # O — kép, carousel slide, videó path-ok
  - assets/linkedin-2026-05-28-001-hero.png

# --- Generálás meta ---
generated_by: presto-adapt                          # K — ki/mi hozta létre
                                                    #   presto-adapt: adapt mód
                                                    #   human: ember írta
                                                    #   presto-comment-reply: comment-reply mód
created_at: 2026-05-25T10:30+02:00                  # K — létrehozás időpontja
updated_at: 2026-05-25T10:30+02:00                  # K — utolsó módosítás

# --- Publikálás ---
publication_method: null                            # O — null amíg nem published; api | mcp | manual
retry_count: 0                                      # K — hány publikálási kísérlet volt

# --- Analytics ---
analytics_status: not-collected                     # K — analytics lifecycle állapota
                                                    #   not-collected: még nincs adat
                                                    #   collected: nyers adatok megvannak
                                                    #   aggregated: feldolgozva, Insight-ok születtek
                                                    #   archived: lezárva
comment_status: not-scanned                         # K — komment-scan állapota
                                                    #   not-scanned: még nem scannelve
                                                    #   clean: nincs új komment
                                                    #   needs-attention: van válaszra váró komment

# --- Comment-reply meta (csak comment-reply formátum esetén) ---
parent_publication_id: null                         # O — ha format: comment-reply, ide kerül a szülő pub ID

# --- Token ---
token_usage:
  input: null                                       # O — null amíg Phase 2.C; generáláskor kitöltve
  output: null

# --- Tagek és UTM ---
tags: [bdos, markdown-substrate, thought-leadership]  # O
metadata:
  utm:                                              # O — UTM paraméterek analytics-hez
    source: linkedin
    campaign: bdos-positioning-q2-2026
    content: linkedin-2026-05-28-001
---

## Content

<a végleges draft szöveg — ez kerül publikálásra>

## Short preview

<140 karakteres preview a time-board kártya megjelenítéséhez>

## Variációk

### Variáció A — rövidebb hook
<alternatív nyitómondat>

### Variáció B — kérdés-alapú hook
<alternatív nyitómondat>

## Approval history

- <ISO-ts> — generated by <generated_by>
- (emberi jóváhagyásra vár)

## Publication history

- (üres amíg nem published)

## Analytics

- (published után kerül ide a nyers adat és az aggregált insight-link)

## Comments

- (comment-scan után kerül ide a linked COMMENT.md listája)

## Operational log

- <ISO-ts> — created from <mode> (source: <seed_ref vagy atomic>)
```

### Mező-összefoglaló

| Mező | K/O | Magyarázat |
|---|---|---|
| `schema` | K | Típus-azonosító — mindig `presto.publication.v2` |
| `publication_id` | K | Stabil ID — channel-date-seq mintával |
| `seed_ref` | O | Forrás Seed, null ha direkt |
| `campaign_id` | O | Campaign esernyő, null ha standalone |
| `area` | K | Melyik Area brand-voice-át használjuk |
| `channel` | K | Célcsatorna — Channel DNA-ra mutat |
| `format` | K | Channel-specifikus formátum |
| `language` | K | ISO 639-1 |
| `intent.goal` | K | Publikáció stratégiai célja |
| `intent.audience_segment` | K | Konkrét célközönség-szegmens |
| `intent.desired_action` | K | Elvárt olvasói következő lépés |
| `intent.source` | K | Human vs. presto-suggested audit trail |
| `intent.notes` | O | Szabad kontextus |
| `publication_status` | K | Kanban lane (8 érték) |
| `approval_status` | K | Emberi jóváhagyás (4 érték) |
| `scheduled_time` | O | Pontos időpont, null ha nincs |
| `planned_publish_date` | O | Dátum-szintű time-board helyezés |
| `linked_atomic_thoughts` | O | Sage atomic hivatkozások |
| `linked_insights` | O | Presto Insight hivatkozások |
| `visual_assets` | O | Képek, slide-ok path-listája |
| `generated_by` | K | Ki hozta létre |
| `created_at` | K | Létrehozás timestamp |
| `updated_at` | K | Utolsó módosítás timestamp |
| `publication_method` | O | api / mcp / manual — publisholáskor |
| `retry_count` | K | Publikálási kísérletek száma |
| `analytics_status` | K | Analytics lifecycle (4 érték) |
| `comment_status` | K | Komment-scan állapota (3 érték) |
| `parent_publication_id` | O | Csak comment-reply formátumhoz |
| `token_usage` | O | Input/output token count a generáláshoz |
| `tags` | O | Keresési tagek |
| `metadata.utm` | O | UTM paraméterek analytics-hez |

---

## 3. `presto.campaign.v2` — az opcionális esernyő

**Hely:** `02_Areas/<ProjectName>/Marketing/Campaigns/<campaign-slug>/CAMPAIGN.md`

**Mikor kell:** ha ugyanaz a Seed (vagy szándék) több Area-ban / több csatornán jelenik meg, és ezeket együtt akarjuk koordinálni.

**Mikor nem kell:** ha a Publication standalone — ekkor `campaign_id: null` a Publication-ben, Campaign-fájl nem jön létre.

**Invariáns:** a Campaign koordinációs objektum, nem tartalom-forrás. A tartalom kizárólag Publication-ökben él.

### Schema

```yaml
---
schema: presto.campaign.v2                          # K — típus-azonosító

# --- Azonosítók ---
campaign_id: bdos-positioning-q2-2026               # K — stabil slug (kebab-case)
title: "BDOS Positioning Q2 2026"                   # K — ember-olvasható kampánycím

# --- Forrás ---
seed_id: seed-2026-05-25-001                        # O — fő Seed amiből az esernyő indult
                                                    #   null ha nincs egy specifikus kiindulási Seed

# --- Intent-lista (esernyő alatt több intent lehetséges) ---
intents:                                            # K — legalább 1 kell
  - goal: thought-leadership                        # melyik cél
    area: ExarLabs                                  # melyik Area-hoz tartozik
    notes: "Technical philosophical positioning"
  - goal: community                                 # másik cél
    area: Personal                                  # másik Area
    notes: "Developer community connection"
  - goal: seo-lead-gen
    area: ExarLabs
    notes: "Organic discovery for BDOS methodology"

# --- Érintett dimenziók ---
areas:                                              # K — melyik Area-kat érinti
  - ExarLabs
  - Personal
channels:                                           # K — melyik csatornákon fut
  - linkedin
  - x-twitter
  - blog

# --- Publication-lista ---
publications:                                       # O — Campaign alatt lévő Publication-ök
  - publication_id: linkedin-2026-05-28-001         #   append-only
    area: ExarLabs
    channel: linkedin
    publication_status: draft
  - publication_id: x-2026-05-29-001
    area: Personal
    channel: x-twitter
    publication_status: draft
  - publication_id: blog-2026-06-01-001
    area: ExarLabs
    channel: blog
    publication_status: draft

# --- Lifecycle ---
stage: draft                                        # K — kampány egészének állapota
                                                    #   draft: tervezési fázis, publication-ök készülnek
                                                    #   active: legalább 1 publication published
                                                    #   done: minden publication archived
status: in_progress                                 # K — operacionális állapot
                                                    #   in_progress: aktív munka folyik
                                                    #   blocked: valami megakadályozza az előrehaladást
                                                    #   done: kampány lezárva

# --- Dátumok ---
start_date: 2026-05-25                              # K — kampány indulása
target_end_date: 2026-06-30                         # O — célzott befejezés

# --- KPI-k ---
kpi_targets:                                        # O — kampány-szintű célok
  total_reach: 5000
  total_leads: 20
  avg_engagement_rate: 0.05

# --- Meta ---
owner: Becze Szabolcs                               # K — felelős személy
tags: [bdos, positioning, q2-2026]                  # O
---

## Brief

<kampány rövid összefoglalója — mi a stratégiai szándék, miért indítjuk>

## Coordination notes

<cross-Area koordinációs megjegyzések — mi az egységes narratíva, mi a per-Area adaptáció>

## Results summary

<kampány lezárásakor aggregált eredmények — per-publication linkekkel>

## Iteration history

- <ISO-ts> — created by <agent/user>
```

### Mező-összefoglaló

| Mező | K/O | Magyarázat |
|---|---|---|
| `schema` | K | Típus-azonosító — mindig `presto.campaign.v2` |
| `campaign_id` | K | Stabil slug, kebab-case |
| `title` | K | Ember-olvasható kampánycím |
| `seed_id` | O | Forrás Seed, null ha nincs egy kiindulási seed |
| `intents` | K | Legalább 1 intent-objektum a kampányhoz |
| `intents[].goal` | K | Stratégiai cél per intent |
| `intents[].area` | K | Melyik Area-hoz tartozik az intent |
| `intents[].notes` | O | Szabad kontextus |
| `areas` | K | Érintett Area-k listája |
| `channels` | K | Érintett csatornák listája |
| `publications` | O | Alá tartozó Publication-ök (append-only) |
| `stage` | K | Kampány kanban állapota (draft/active/done) |
| `status` | K | Operacionális állapot (in_progress/blocked/done) |
| `start_date` | K | Kampány indulása |
| `target_end_date` | O | Célzott befejezés |
| `kpi_targets` | O | Kampány-szintű KPI célok |
| `owner` | K | Felelős személy |
| `tags` | O | Keresési tagek |

---

## Changelog

- **0.3.0 (2026-05-26)** — `presto.seed.v2` szekció (§1b) hozzáadva. Új mezők: `short_description` (K), `runbook_ref` (O), `campaign_ref` (O, null), `prerequisites[]` (O, TODO-lista), `distribution_timeline[]` (O, strukturált multi-platform terv). Bővített `status` enum (6 érték: `in_prep | ready | active | partially_spawned | exhausted | archived`). Computed `todos_count` sidecar-mező specifikálva (NEM a markdown-ban). v1 `status` enum: v1 doc-ban jelölve "superseded by v2". Backward compat megőrzve.
- **0.2.0 (2026-05-25)** — initial v0.2 schema spec. `presto.seed.v1` new. `presto.publication.v2` new (supersedes `presto.publication.v1` from v0.1 ARCHITECTURE.md — key change: `intent:` blokk beágyazva, `seed_ref:` + `campaign_id:` mezők). `presto.campaign.v2` new (supersedes v0.1 `CAMPAIGN.md` schema — key change: `intents[]` tömb, `seed_id:`, schema mező).
