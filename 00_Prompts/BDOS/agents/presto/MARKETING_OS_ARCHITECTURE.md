---
title: Presto Marketing OS — Architecture
version: 0.1.0
date: 2026-05-25
author: Becze Szabolcs
status: draft
owner: presto
description: Normatív architektúra-spec a Presto Marketing Operating System teljes újratervezésére. Nem dashboard-tend, hanem capability-level evolúció: új markdown entitások (Publication, Channel DNA, Comment, TODO, Insight, Template), új Presto módok (publish/comment-ops/insight/template/channel), és egy operacionális dashboard cockpit. Reconcilálja a 18 felhasználói követelményt a meglévő invariánsokkal (markdown source of truth, zero build, event-driven, Curator-owned design system). Phased build (4 fázis), explicit per-fázis deliverable-lista.
tags: [presto, marketing-os, architecture, capability]
index_schema_version: 1
id: a7f3e2d1-8c4b-4f9a-9e3d-1b2c5e7a8d9f
bdos_index: true
---

# Presto Marketing OS — Architecture

> **Ez nem dashboard-tend.** Ez egy capability-szintű evolúció: a Presto v0.5 (Distribution Cognition Layer) → v0.6 (Marketing Operating System). A dashboard a látható réteg, de az igazi munka a markdown szubsztrátum bővítése: új entitások, új agent módok, új lifecycle-ek.
>
> A dashboard a **renderer marad** (DS 1.1 invariáns). A "cockpit" érzés a markdown-natív állapot **gondos megjelenítéséből** és a **copyable command-okból** jön — nem write-back-ből.

---

## 1. Mit kérdezett a felhasználó (a 18 szekció esszenciája)

A felhasználó **marketing operating system**-et kér, nem dashboard-update-et. A követelmények öt rétegre szervezhetők:

| Réteg | Mit ad | Új entitás |
|---|---|---|
| **A. Operational backbone** | Publikáció-szintű lifecycle: tervezés → draft → approval → publish → analytics | `PUBLICATION.md` (új) |
| **B. Distribution intelligence** | Channel DNA, multi-channel identity, fallback execution hierarchy | `CHANNEL_DNA.md` (új) |
| **C. Audience feedback loop** | Comment scanning, classification, response drafting | `COMMENT.md` (új) |
| **D. Cognitive surfacing** | Insights (high-signal observations), Templates (validated patterns), TODOs (operational inbox) | `INSIGHT.md`, `TEMPLATE.md`, `TODO.md` (új) |
| **E. Operational cockpit** | Time board, daily rhythm, calm UI, observable Presto | Dashboard rebuild (v0.6.0) |

**Kulcs felismerés:** a kért funkcionalitás 70%-a **új markdown infrastruktúra**, 20% új agent-módok, 10% dashboard UI. A dashboard önmagában nem oldja meg — ez egy kiegészítő réteg a markdown-szubsztrátum köré.

---

## 2. Reconciliation a meglévő invariánsokkal

A felhasználó 18 szekciója helyenként sérti a dashboard alkotmányt. Ezek a feloldások:

### 2.1 "Approve from phone, Presto executes" vs. "Dashboard NEVER writes markdown" (Architecture 1.1)

**Konfliktus:** UI-ban approval gomb → ki publikál?

**Feloldás (phased):**

- **Phase 1 — copyable command:** approval gomb a dashboardon `/pres-approve pub:exarlabs/microsite-q3/linkedin-001` parancsot tesz a vágólapra. User átkattint terminálba, Presto agent futtatja a publish-flow-t. Tiszta read-only marad. Mobil-flow: a vágólap-tartalmat elküldi magának üzenetben → terminálba.
- **Phase 2 — approval signal pattern (Curator promote):** új konvenció — dashboard `_inbox/approval-actions/<ts>_<pub-id>.md` fájlt írhat egyetlen, schema-szabályozott payload-dal (`approval_signal.v1`). Scheduler.py vagy Presto cron percenként scanneli, feldolgozza. Ez **kivétel** az invariáns alól, formálisan promote-olt szabállyal: a dashboard *signal-eket* írhat, *content-et* sosem.

A 18. szekció `signature-request` flow-jához hasonló modellt használ a `legal` plugin — ott is signal-pattern van. Bevett megoldás.

### 2.2 "Realtime publication" vs. "Daily rhythm" (felhasználó saját 16. szekciója)

**Nincs konfliktus** — a felhasználó **maga írja** hogy daily cadence-t akar, nem realtime-ot. Ezt invariánssá tesszük: a Marketing OS **nem realtime**. Cron-alapú: morning scan (07:00), analytics sweep (08:00), comment review (09:00 + 15:00), insight check (heti). Az SSE-rendszer kizárólag a markdown-mtime változását tükrözi a dashboard-on, nem új publikációkat triggerel.

### 2.3 "18-féle entitás" vs. "Stabilitás > intelligencia" (BDOS alapelv)

**Veszély:** 6 új markdown-típus (`PUBLICATION`, `CHANNEL_DNA`, `COMMENT`, `TODO`, `INSIGHT`, `TEMPLATE`) → szétaprózott vault.

**Feloldás:** szigorú schema-disciplin minden új típusra. Mindegyik:
- Kötelező `schema:` frontmatter-mező (`presto.publication.v1` stb.)
- Schema dokumentáció ebben a fájlban (§4)
- Lifecycle-átmenetek explicit listán
- Új típus bevezetése = Curator/Maestro promote-cycle, nem ad-hoc

### 2.4 "Comment operations" vs. "soha ne publish autonomously"

**Konfliktus:** a comment-response is publikáció. Ki "approve"-ol egy kommentre adott választ?

**Feloldás:** **minden** comment-response is ugyanaz a publikáció-lifecycle, csak `format: comment-reply`, `parent_publication_id: <orig-pub-id>`. Az approval-flow ugyanaz. Egyetlen flow, nem duplikálva.

### 2.5 "Channel DNA" — hol éljen?

**Két opció:**
- Per-Area (`02_Areas/<Project>/Marketing/channels/`)
- Cross-project canonical (`agents/presto/channel-dna/`)

**Döntés:** **cross-project canonical**, per-project tone-override mechanizmussal. Egy LinkedIn = egy LinkedIn (technikai/formátum-szabályok univerzálisak). A *brand-voice* override-ol per-Area egy `tone_overrides:` blokk-kal. Indok: ha minden Area külön LinkedIn-DNA-t tartana, a karakter-limit-változás 5 helyen ismétlődne. Kanonikus + override = DRY + flexibilis.

---

## 3. Markdown szubsztrátum — a 6 új entitás

### 3.1 `PUBLICATION.md` — a központi atomi egység

**Hely:** `02_Areas/<Project>/Marketing/Campaigns/<campaign-slug>/publications/<pub-id>.md`

**Naming:** `<pub-id>` = `<channel>-<seq>` (pl. `linkedin-001`, `x-thread-002`, `ig-carousel-001`). Egy publikáció = egy fájl. Egyetlen forrás minden lifecycle-state-hez.

**Schema (`presto.publication.v1`):**

```yaml
---
schema: presto.publication.v1
publication_id: linkedin-001            # auto-generated, stable
campaign_id: microsite-q3
campaign_path: 02_Areas/ExarLabs/Marketing/Campaigns/microsite-q3
project: ExarLabs
channel: linkedin                       # references channel-dna/<channel>.md
format: long-post                       # see channel-dna for allowed formats
language: hu                            # ISO 639-1
publication_status: draft               # see §3.1.1 lifecycle
approval_status: pending                # pending | approved | rejected | revoked
scheduled_time: 2026-05-28T14:00+02:00  # ISO 8601 with TZ; null if unscheduled
planned_publish_date: 2026-05-28        # for time-board placement when unscheduled
visual_assets:
  - assets/linkedin-001-hero.png
linked_atomic_thoughts:
  - "[[atomic/ai-native-companies-thesis]]"
linked_insights:
  - "[[insight/2026-05-15_long-form-resonance]]"
generated_by: presto-adapt              # presto-adapt | human | presto-comment-reply
created_at: 2026-05-24T10:32+02:00
updated_at: 2026-05-25T09:15+02:00
publication_method: null                # api | mcp | manual ; null until published
retry_count: 0
analytics_status: not-collected         # not-collected | collected | aggregated | archived
comment_status: not-scanned             # not-scanned | clean | needs-attention
parent_publication_id: null             # set only for comment-replies (format: comment-reply)
token_usage:
  input: 1840
  output: 612
tags: [thought-leadership, microsite-launch]
metadata:
  thumbnail_text: null
  hook_variant: A
  utm:
    source: linkedin
    campaign: microsite-q3
    content: linkedin-001
---

## Content

<the actual draft text — what gets published>

## Short preview

<140-char preview for time-board card display>

## Approval history
- 2026-05-25 09:15 — generated by presto-adapt run #c4f2
- (awaiting approval)

## Publication history
- (empty until published)

## Analytics
- (populated after analytics scan)

## Comments
- (populated after comment scan)

## Operational log
- 2026-05-24 10:32 — created from adapt mode (source: atomic/ai-native-companies-thesis)
- 2026-05-25 09:15 — content revised by user
```

#### 3.1.1 `publication_status` lifecycle

Egyetlen lineáris lifecycle (a felhasználó által javasolt 14 állapot konszolidálva 11-re — a duplikációkat egyesítve):

```
draft → generated → needs_review → approved → scheduled →
publish_pending → published → monitoring → archived

Branch states (oldalt léphetnek be):
  failed         (a publish_pending-ből, retry után escalate)
  manual_required (a failed-ből, ha API+MCP is fail)
  revoked        (post-approval rejection: bármelyikből vissza approved-ig)
```

**Visual semantics dashboardon:**
- `draft` / `generated` → szürke (idle)
- `needs_review` → sárga (warn)
- `approved` / `scheduled` → halvány zöld
- `publish_pending` → animált narancs
- `published` / `monitoring` → zöld (ok)
- `failed` / `manual_required` → piros (gap)
- `archived` → szürke (idle)

#### 3.1.2 Comment-reply mint publikáció

Egy comment-reply ugyanolyan `PUBLICATION.md`, csak:
- `format: comment-reply`
- `parent_publication_id: <orig>` (és visszafele a parent egy `replies:` listát kap)
- ugyanaz az approval-flow, lifecycle, retry, analytics

Ez kritikus DRY-megoldás — egyetlen flow, kétféle dolog egyszerre.

### 3.2 `CHANNEL_DNA.md`

**Hely:** `00_Prompts/BDOS/agents/presto/channel-dna/<channel-slug>.md`

**Cross-project canonical.** Egy fájl per platform. Per-Area tone-override = inline blokk.

**Schema (`presto.channel-dna.v1`):**

```yaml
---
schema: presto.channel-dna.v1
channel: linkedin
display_name: LinkedIn
status: active                        # active | dormant | sunset
primary_language: en                  # default; per-Area override-olható
allowed_formats: [long-post, short-post, article, carousel, video, poll]
constraints:
  max_chars:
    long-post: 3000
    short-post: 700
    article: 110000
  max_images: 9
  max_hashtags: 5
  link_in_text: false                 # platform behavior: links auto-OG
posting_rhythm:
  recommended_per_week: 3-5
  optimal_hours_local: [08, 12, 17]
publication_capabilities:
  api_available: true
  mcp_available: true                 # claude-in-chrome
  manual_required: false
  analytics_api: true
  comment_response_api: true
fallback_chain: [api, mcp, manual]    # execution preference order
authentication_state:
  api_token_present: false            # checked dynamically; this is just hint
identity:
  default_tone: thought-leadership
  emoji_policy: minimal
  cta_style: open-ended-question
  audience_profile: B2B decision makers, tech-adjacent leaders
  preferred_structures:
    - hook → narrative → insight → CTA
    - listicle → punchline
  forbidden_patterns:
    - "growth hack" language
    - listicles starting with "X tips"
    - emoji-laden hooks
visual_identity:
  ratio: 1.91:1
  template: linkedin-thought-leader-v2
engagement_expectations:
  baseline_engagement_rate: 0.024
  signal_threshold_for_resonance: 0.08

tone_overrides:                       # per-Area
  ExarLabs:
    default_tone: technical-philosophical
    primary_language: en
    preferred_structures:
      - thesis statement → contrarian framing → evidence → invitation
  DeákHúsüzlet:
    default_tone: warm-local
    primary_language: hu
    forbidden_patterns:
      - corporate jargon
---

# LinkedIn — Channel DNA

## Audience profile
<narrative description of who's on LinkedIn for our brand>

## Historical examples
- [[publications/linkedin-001]] — 8.3% ER, atomic: ai-native-companies-thesis
- [[publications/linkedin-014]] — 12.1% ER, atomic: feedback-loop-economics

## Forbidden patterns — rationale
<why these don't work for us>

## Iteration history
- 2026-05-01 — initial DNA
- 2026-05-20 — added "long-form > short-form" finding from audience-learning
```

### 3.3 `COMMENT.md`

**Hely:** `02_Areas/<Project>/Marketing/Campaigns/<slug>/publications/<pub-id>/comments/<comment-id>.md`

**Hierarchia:** publikáció alá fészkelve — egy publikáció minden kommentje vele él. Ez segít az archiválásnál (30 nap után az egész publikáció + comments archív).

**Schema (`presto.comment.v1`):**

```yaml
---
schema: presto.comment.v1
comment_id: cmt-linkedin-001-003
publication_id: linkedin-001
platform: linkedin
external_comment_id: urn:li:comment:xyz
author_name: "Jane Doe"
author_handle: janedoe
author_external_url: https://linkedin.com/in/janedoe
collected_at: 2026-05-26T09:14+02:00
classification: question              # praise | question | criticism | lead | partnership | technical | spam
classification_confidence: 0.87
suggested_response:
  status: drafted                     # drafted | approved | sent | skipped
  draft_pub_id: comment-reply-cmt-linkedin-001-003   # ref a PUBLICATION.md-be
  confidence: 0.71
human_todo_generated: false           # true if confidence below threshold
sentiment: positive                   # positive | neutral | negative
sentiment_score: 0.6
---

## Comment text
<the actual comment content>

## Context
- Replied to: <if a reply chain>
- Thread depth: 1

## Analysis notes
<Presto's classification reasoning>
```

**Comment scanning model:** napi 2x cron (`comment-ops` mode). Új komment → `COMMENT.md` create + classify. Ha confidence ≥ 0.75 → draft response generálás → emberi approval pending. Ha < 0.75 → `TODO.md` create human review-hez.

### 3.4 `TODO.md`

**Hely:** `00_Prompts/BDOS/agents/presto/todos/<YYYY-MM-DD>_<slug>.md`

**Egyetlen operacionális inbox** — NEM a campaign-state-be elegyítve. A felhasználó 11. szekciója expliciten ezt kéri.

**Schema (`presto.todo.v1`):**

```yaml
---
schema: presto.todo.v1
todo_id: 2026-05-25_low-conf-comment-reply
created_at: 2026-05-25T15:32+02:00
source: comment-low-confidence        # see §3.4.1
urgency: medium                       # low | medium | high
status: open                          # open | in-progress | done | dismissed
linked_publication: linkedin-001
linked_campaign: ExarLabs/microsite-q3
suggested_action: |
  Manually classify and respond to comment. AI confidence 0.62 — uncertain
  whether this is sarcasm or genuine question.
confidence_level: 0.62                # the underlying signal's confidence
due: null
completed_at: null
completed_by: null
resolution_note: null
---

## Context
<the comment text, the publication context, why it surfaced>

## Recommended response (low confidence)
<the AI's tentative draft, if any>
```

**Source kategóriák (8):**
- `comment-low-confidence` — uncertain classification
- `publication-failed` — API+MCP+retry all failed
- `campaign-blocked` — missing asset, channel-auth lapsed
- `missing-asset` — visual asset needed, not in `assets/`
- `platform-failure` — channel-wide outage
- `insight-review` — new candidate insight needs human eyes
- `strategic-review` — `reflect` mode flagged a stable pattern needing decision
- `manual-required` — escalated publication needing manual paste

### 3.5 `INSIGHT.md`

**Hely:** `00_Prompts/BDOS/agents/presto/insights/<YYYY-MM-DD>_<slug>.md`

**Lifecycle:** `candidate → approved → operational → retired`

**Schema (`presto.insight.v1`):**

```yaml
---
schema: presto.insight.v1
insight_id: 2026-05-15_long-form-resonance
created_at: 2026-05-15T08:00+02:00
source_mode: reflect                  # reflect | audience | discover | manual
status: candidate                     # candidate | approved | operational | retired
observation: |
  LinkedIn long-form posts (>1500 chars) outperform short posts 3.4x on our
  account when topic = AI-native operating models.
evidence:
  - publication_id: linkedin-005
    metric: engagement_rate
    value: 0.082
  - publication_id: linkedin-014
    metric: engagement_rate
    value: 0.094
  - publication_id: linkedin-021
    metric: engagement_rate
    value: 0.077
evidence_strength: high               # low | medium | high
sample_size: 3                        # min 3 for promotion to approved
reversibility: reversible             # what happens if we act on it and it's wrong
proposed_action: |
  Default LinkedIn channel format to long-post for ExarLabs Area.
linked_channel: linkedin
linked_areas: [ExarLabs]
human_approved_at: null
operationalized_at: null
operationalized_as:
  - "channel-dna/linkedin.md tone_override for ExarLabs"
retired_at: null
retired_reason: null
---

## Observation
<full prose narrative>

## Audit trail
- 2026-05-15 — candidate generated by reflect mode
- (awaiting human review)
```

**Anti-spam:** csak akkor `candidate`, ha `sample_size ≥ 3` és `evidence_strength ≥ medium`. Sage `learnings` mintára szigorú threshold.

### 3.6 `TEMPLATE.md`

**Hely:** `00_Prompts/BDOS/agents/presto/templates/<channel>/<slug>.md`

**Lifecycle:** `draft → reusable → validated → canonical → deprecated`

**Schema (`presto.template.v1`):**

```yaml
---
schema: presto.template.v1
template_id: linkedin-thought-leader-v2
channel: linkedin
format: long-post
language: en
status: validated                     # draft | reusable | validated | canonical | deprecated
created_from_publication: linkedin-014
created_at: 2026-04-10
validated_at: 2026-05-01
validated_by: human-approval
usage_count: 7
avg_engagement_rate: 0.073
baseline_engagement_rate: 0.024
multiplier: 3.04
linked_atomic_categories: [systems-thinking, ai-native]
applicable_areas: [ExarLabs]
---

## Structure

1. **Hook** (1-2 lines): contrarian framing of a common assumption
2. **Thesis** (3-4 lines): the actual claim, plainly stated
3. **Evidence block** (5-8 lines, can be a list): why this is true
4. **Invitation** (2 lines): open question, not a CTA

## Example
[[publications/linkedin-014]]

## Forbidden in this template
- starting with "Hot take:"
- ending with "What do you think? 👇"
```

**Promotion logic:** Presto `template` mode (új) figyel: ha ≥ 3 publikáció ugyanazt a struktúrát követi és `avg_engagement > 2x baseline` → javaslat `reusable`-re. Ha ≥ 7 használat + stabil multiplier → `validated`. Csak human approval → `canonical`.

---

## 4. Új Presto módok (v0.5 → v0.6)

A meglévő 12 mód marad. Új módok:

| Új mód | Operacionális | Cél | Confirmation |
|---|---|---|---|
| `publish` | executor | Egy approved publikáció execution-je (API → MCP → manual fallback chain) | KÖTELEZŐ |
| `comment-scan` | scheduled | Napi 2x: új kommentek begyűjtése, classify, draft response | NEM (additive) |
| `comment-reply` | executor | Egy classified komment-re draft + approval flow | KÖTELEZŐ |
| `insight` | cognition | Insight lifecycle ops: list, approve, operationalize, retire | KÖTELEZŐ akcióhoz |
| `template` | cognition | Template lifecycle ops: detect candidates, promote, retire | KÖTELEZŐ akcióhoz |
| `channel` | maintenance | Channel DNA tend (list, view, update tone-override) | KÖTELEZŐ edit-hez |
| `todo` | info | TODO inbox view + close | KÖTELEZŐ close-hoz |

**Slash commands (új):** `/pres-publish`, `/pres-approve`, `/pres-comment-scan`, `/pres-comment-reply`, `/pres-insight`, `/pres-template`, `/pres-channel`, `/pres-todo`.

**Schedule cadence:**
- `comment-scan`: napi 2x (09:00 + 15:00)
- `template detect-candidates`: heti egyszer (hétfő reggel)
- `analytics-sweep`: napi egyszer (08:00) — meglévő `measure` mód cron-osítva

---

## 5. Dashboard rebuild — v0.5.5 → v0.6.0 (major bump indokolt)

A jelenlegi 10-panel observatory **nem törlődik** — átalakul operacionális cockpit-tá. Major bump indokolt: a publikáció-szintű modell **breaking change** a campaign-only modellhez képest.

### 5.1 Új layout (felülről lefelé)

```
┌────────────────────────────────────────────────────────────────┐
│ ADMIN BAR (DS §5c, változatlan)                                │
├────────────────────────────────────────────────────────────────┤
│ MASTHEAD                                                       │
│ Presto — Marketing OS  ·  v0.6.0  ·  Daily rhythm: 07/08/09/15│
├────────────────────────────────────────────────────────────────┤
│ DAILY BRIEFING STRIP (új) — 4 stat card                        │
│ [Today's actions: 3] [Awaiting approval: 2] [Comments: 5] [...]│
├────────────────────────────────────────────────────────────────┤
│ PANEL 1: TIME BOARD  ◀── elsődleges felület                    │
│ Horizontal scroll, columns = days, cards = publications        │
│ [-2d][-1d][TODAY][+1d][+2d][+3d][+4d][+5d][+6d][+7d]...        │
│   ↑ Backlog lane (unscheduled drafts) — separate row below     │
├────────────────────────────────────────────────────────────────┤
│ PANEL 2: APPROVAL QUEUE (mobile-friendly, big tap targets)     │
├────────────────────────────────────────────────────────────────┤
│ PANEL 3: CHANNELS & TOOLS (Channel DNA browser)                │
├────────────────────────────────────────────────────────────────┤
│ PANEL 4: ANALYTICS — Audience Intelligence (not vanity)        │
├────────────────────────────────────────────────────────────────┤
│ PANEL 5: COMMENTS INBOX  │  PANEL 6: TODO INBOX                │
├────────────────────────────────────────────────────────────────┤
│ PANEL 7: INSIGHTS (lifecycle) │ PANEL 8: TEMPLATES (lifecycle) │
├────────────────────────────────────────────────────────────────┤
│ PANEL 9: AUDIENCE LEARNINGS (meglévő, refined)                 │
├────────────────────────────────────────────────────────────────┤
│ PANEL 10: PRESTO OPERATIONAL LOG (recent activity, calm)       │
└────────────────────────────────────────────────────────────────┘
```

### 5.2 Time Board részletes terv (Panel 1 — a legfontosabb)

**Adat-folyam:**
1. Glob: `02_Areas/*/Marketing/Campaigns/*/publications/*.md`
2. Parse: each PUBLICATION.md frontmatter
3. Sort by `scheduled_time || planned_publish_date`
4. Group by date (ISO YYYY-MM-DD)
5. Render: horizontal scrolling row of day-columns

**Day-column ARC:**
```
┌──────────────────┐
│ HÉT  · 26        │  ← weekday + day number, today highlighted
│ 2026-05-26       │
├──────────────────┤
│ [card]           │
│ [card]           │
│ [card]           │
└──────────────────┘
```

**Card kompakt nézet:**
- Top stripe (3px): approval szín (green/yellow/red)
- Channel ikon + format chip
- Project badge (color-coded)
- Title (1-2 sor, truncated)
- Status chip (publication_status)
- Time (HH:mm if scheduled, "any" if just date)
- Hover: copy-ref button (DS §4a)

**Click → detailed drawer overlay** (NEM új oldal — slide-in panel a jobb oldalról):
- Full content
- Visual asset preview
- Linked atomic thoughts (clickable)
- Approval controls (copy-command pattern Phase 1; signal-write Phase 2)
- Publication history
- Analytics (ha published)
- Comments (linked COMMENT.md-k)
- Operational log
- "Open in Obsidian" link (`obsidian://open?file=...`)

**Time-board interakciók:**
- Horizontal scroll (mouse wheel + drag)
- "Today" gomb visszaugrik
- "+ Backlog" lane: drafts without dates, alul külön
- Filter chips: per channel, per project, per status
- Search box (publication title / campaign / atomic-link)

**Anti-pattern:** NE legyen drag-drop reschedule. Az újraütemezés markdown-edit, nem UI-akció. Az approval flow-val konzisztens: signal-pattern lehet, de Phase 2-re.

### 5.3 Approval Queue (Panel 2)

Külön panel, mert a felhasználó expliciten **mobil-flow**-t kér (5. szekció). Mobil-prioritás: nagy tap-targets, vertikális lista, minimum scroll.

**Per row:**
- Channel ikon + project badge
- Preview text (140 char)
- Visual asset thumbnail (ha van)
- Két gomb: `[Copy /pres-approve cmd]` + `[Copy /pres-reject cmd]`
- "Open in Obsidian" link

**Phase 2 evolúció:** a két gomb közvetlenül signal-fájlt ír `_inbox/approval-actions/`-be, scheduler.py másodpercenként scanneli, Presto agent végrehajt.

### 5.4 Channels & Tools (Panel 3)

A felhasználó 8. szekciója: "what Presto can currently operate".

**Adat-forrás:** `agents/presto/channel-dna/*.md`

**Per channel card:**
- Channel név + ikon
- Status pill (active / dormant / sunset)
- 4 capability pill: `API`, `MCP`, `Analytics`, `Comments` (zöld ha elérhető, szürke ha nem)
- Auth state (ha auth-check capability létezik): `✓ authenticated` / `× re-auth needed`
- Per-Area tone overrides: 1 sor per Area

### 5.5 Analytics rebuild (Panel 4)

A felhasználó 9. szekciója: "audience understanding and resonance analysis", NEM vanity.

**Felülírjuk a meglévő analytics-panelt:**
- Cross-reference: minden publikáció → forrás atomic
- Resonance ranking: top-3 atomic by aggregate engagement
- Channel × format mátrix: melyik kombóra van hozzá adat
- Drift indicators: ha valami statisztikailag változott az elmúlt 30 napban
- **NEM mutatunk:** abszolút engagement-számokat hero-position-ben (vanity)

### 5.6 Comments (Panel 5) + TODOs (Panel 6) + Insights (Panel 7) + Templates (Panel 8)

Minden panel ugyanaz a pattern:
- Lifecycle column header-ek
- Per-item kompakt card
- Click → drawer (azonos drawer-rendszer mint a publikációknál)
- Empty-state graceful (DS standard)

### 5.7 Presto Operational Log (Panel 10)

A felhasználó 15. szekciója: minden meaningful operation logolt.

**Adat-forrás:** `_dashboards/_design/agent_logs.json` filtered to `agent_name === 'presto'`.

Schema v2-aware (DS §7). Calm timeline view, NEM real-time stream. 24h window default, ágenscsoport-szerű group-olással (start → tool calls → end).

---

## 6. Phased rollout terv

Ez a teljes scope ~4 fázis, mindegyik egy-egy session.

### Phase 1 — Operational backbone (THIS SESSION + next)

**Deliverable:**
1. `MARKETING_OS_ARCHITECTURE.md` (this file) — ✅
2. `PUBLICATION.md` schema példa-fájlja (`agents/presto/_examples/publication-sample.md`)
3. `CHANNEL_DNA.md` 4 alap-platformra (LinkedIn, X, Instagram, YouTube)
4. Presto v0.6.0 dashboard rebuild:
   - Daily Briefing Strip
   - Time Board (Panel 1) — működő empty-state-tel + 1-2 demo PUBLICATION.md-val
   - Approval Queue (Panel 2) — copy-command pattern
   - Panel 10 (Operational Log) — meglévő logsection refinement
5. Presto canonical (`agents/presto.md`) bumpolva v0.6.0-ra: új `publish` mód + schema-link

**NEM lesz Phase 1-ben:** comment-scanning, insights, templates, MCP-publish végrehajtás, signal-pattern approval

### Phase 2 — Distribution intelligence

**Deliverable:**
1. Panel 3 (Channels & Tools) — élő DNA-browser
2. Channel-DNA edit flow (`pres-channel` mód)
3. `publish` mód implementáció (API-first, MCP fallback) — agent oldal
4. Phase 2-approval signal pattern Curator promote
5. `template-detection` (heti cron)

### Phase 3 — Feedback loop

**Deliverable:**
1. `comment-scan` cron implementation
2. `COMMENT.md` schema instances
3. Panel 5 (Comments Inbox)
4. Panel 6 (TODO Inbox) — sources beépítése
5. `comment-reply` mód

### Phase 4 — Cognitive surfacing + polish

**Deliverable:**
1. `INSIGHT.md` lifecycle + Panel 7
2. `TEMPLATE.md` promotion + Panel 8
3. Analytics rebuild (Panel 4) — full resonance ranking
4. Retention policy (30-day archival job)
5. Audience-learning loop refined integration

---

## 7. Curator promote-cycle szükséges elemek

Ez a capability bevezetése **több Curator promote-ot** igényel:

1. **DS-promote: time-board pattern** — horizontal scrolling day-column. Új komponens-család. Curator dönti el, hány dashboard használhatja majd (jelenleg csak Presto, de a Broker sales pipeline is hasonló lehet).
2. **DS-promote: drawer overlay pattern** — slide-in jobboldali drawer kártyák detail-view-jához. Generikus, Curator promote-olja.
3. **Architecture promote: signal-write pattern** (Phase 2) — kivétel a "dashboard never writes" invariáns alól, schema-szabályozva. Maestro `team-promote` confirmation-nel.
4. **DS-promote: mobile-friendly approval row** — Phase 1-ben copy-command, de a layout-pattern már most promote-olható.

Ezeket a Phase-ek során külön Curator-call-okkal hajtjuk végre.

---

## 8. Mit NEM csinálunk (explicit scope-zárás)

A felhasználó 18 szekciója impliciten elvárhatna ennél többet — itt kifejtve mit NEM:

- ❌ **Realtime publishing.** Daily rhythm marad. (16. szekció maga írja.)
- ❌ **Engagement-optimization automation.** Csak surfacing — döntés ember.
- ❌ **Audience-segmentation engine.** Channel DNA tone-override igen, segmentation NEM (külön capability lenne).
- ❌ **A/B testing infrastructure.** Templates ad alapot, de fennmarad manual decision.
- ❌ **Trend-chasing / viral content suggestion.** Presto `discover` mód már létezik szigorú 4-filterrel — ez NEM bővül.
- ❌ **Direct API integration írása** (LinkedIn, X stb.). Cowork plugin-ok használandók, ha vannak; egyébként MCP. Phase 2-re halasztva.
- ❌ **Multi-language Channel DNA generálás.** Tone-override per-Area van, de a fő DNA per-platform egy verziójú.

---

## 9. Hivatkozott dokumentumok

- [`presto.md`](../presto.md) — Presto canonical (v0.5)
- [`../CONSTITUTION_PHASE_2.md`](../../CONSTITUTION_PHASE_2.md) — 3 log-stream
- [`../LOG_SCHEMAS.md`](../../LOG_SCHEMAS.md) — log schemas
- [`_dashboards/_design/ARCHITECTURE.md`](../../../../_dashboards/_design/ARCHITECTURE.md) — dashboard normatív spec
- [`_dashboards/_design/DESIGN_SYSTEM.md`](../../../../_dashboards/_design/DESIGN_SYSTEM.md) — DS v0.7.3
- [`_dashboards/presto/index.html`](../../../../_dashboards/presto/index.html) — current dashboard (v0.5.5)

---

## 10. Verziózás (ennek a fájlnak)

- **0.1.0 (2026-05-25)** — initial architecture. 18-section user spec reconciliation. Phase 1-4 plan. Awaiting human sign-off on Phase 1 scope before implementation begins.

Audit-trail növelés szabálya: minden Phase-átmenetkor bump + dated entry. Új entitás-schema bevezetésekor minor bump.
