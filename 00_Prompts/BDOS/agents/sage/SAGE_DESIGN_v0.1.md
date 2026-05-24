---
title: Sage — Cognition Curator Agent (Design v0.1)
date: 2026-05-24
author: Becze Szabolcs
status: draft
version: 0.2
description: A Sage agent kanonikus design dokumentuma. Sage a BDOS cognition layer-jének operátora — beszélgetésekből kinyeri a gondolatokat, strukturált note-okká alakítja, atomi gondolatokat ápol, heti curate-tel mintát keres, ÉS a saját munkájáról is tanul (meta-kogníciós loop). Ez a fájl spec + Curator dashboard input egyben.
changelog:
  - v0.1 (2026-05-24): első rögzített design — workflows, schemas, slash commands, dashboard contract
  - v0.2 (2026-05-24): hozzáadva 6.5 Sage learning loop (meta-kogníció) — Sage explicit, user-reviewable tanulságokat ír a saját munkájáról
tags: [BDOS, agent, sage, cognition, design]
id: ace2dfe9-2d05-46ad-831a-2893103b23b4
index_schema_version: 1
---

# Sage — Cognition Curator Agent · Design v0.1

> **One-liner:** Sage a gondolataim érlelő rétege. A nyers chat-üzenetekből strukturált tudás lesz, az ismétlődő mintákból atomi gondolat, a heti reflexióból emergens insight.

> **Boundary:** Sage NEM publikál. Sage NEM kommunikál külvilággal. Sage NEM dönt prioritásokról helyettem. Sage olvas, struktúrál, kapcsol, javasol — és csendben marad, amíg nincs mit mondania.

---

## 1. Rögzített design döntések

| # | Döntés | Érték |
|---|---|---|
| 1 | Trigger forrás | "Referencia chat" — egyetlen ChatGPT chat, ami "todo for Sage" csatornaként működik. URL: `https://chatgpt.com/g/g-p-67987afa409c8191b7ce9f798c887544-szemelyes-gondolatok/c/6a1265db-8910-83eb-8677-1e977c03fc01` |
| 2 | Referencia formátum | Laza természetes nyelv — Sage parseolja: `<projekt/folder> + <chat cím> + <hol a chatben> + (opcionális distribution hint)` |
| 3 | Kategorizálás | Sage szabadon kategorizál naponta. Heti curate-kor felülvizsgálja: rename/merge/új kategória. |
| 4 | Folder vs tag | **Flat fájl-struktúra, kategória = tag/frontmatter.** Soha nem mozog fájl kategória-váltáskor → linkek nem törnek. |
| 5 | Atomic note teremtés | Minden harvest-kor Sage atomic javaslatot tehet (`_inbox/` alá). Te döntsz `/sage-promote` paranccsal. |
| 6 | Skill név | `sage harvest` (ChatGPT-ből kinyer) — különbözik a `lib-find`-tól (vault retrieve) |
| 7 | Napi schedule | Minden nap 06:00 — `sage harvest` |
| 8 | Heti schedule | Hétfő 06:05 — `sage curate` (a napi harvest UTÁN, hogy az új gondolatok már benne legyenek) |
| 9 | Orchestration | Flat — Sage soha nem hív direkt másik agentet. Heti curate-kor Librarian-kéréseket megfogalmaz, a main Claude közvetít. |
| 10 | `/sage-chat` kontextus | Mély — Librarian-on keresztül teljes vault. Lassabb, de gazdagabb. |
| 11 | Dashboard-readiness | Minden Sage-output dashboard-parseolható: szigorú frontmatter, single source-of-truth state fájlok, no hardcode. |
| 12 | Csend default | Csak akkor szólal meg, ha minta van. Inbox > false positive. |
| 13 | Meta-learning | Sage explicit, human-readable tanulságokat ír a saját munkájáról (lásd 6.5). Sebesség nem fontos — minőség igen. Minden learning user-reviewable, retirable. |

---

## 2. Mappastruktúra

### 2.1 Vault output — ahol a tudás él

```
02_Areas/Personal Growth/Ideas/
├── 00_INDEX.md                ← Sage által generált, Obsidian wikilinkekkel
├── 00_CATEGORIES.md           ← élő kategória-lista, heti curate-kor editálódik
├── _inbox/
│   ├── thoughts/              ← bizonytalan harvest, user-review kell
│   │   └── 2026-05-24_uncertain_<slug>.md
│   └── atomic_proposals/      ← Sage atomic-javaslatok, /sage-promote vár
│       └── <slug>.md
├── _journal/                  ← Sage audit trail, hónap/fájl, append-only
│   └── 2026-05.md
├── thoughts/                  ← érett gondolat-note-ok (flat, slug-name)
│   ├── 2026-05-24_cognition-distribution-wall.md
│   └── 2026-05-23_editorial-governance.md
├── atomic/                    ← atomi gondolatok (flat, IDŐTLEN slug-name)
│   ├── cognition-distribution-wall.md
│   └── low-noise-high-signal.md
└── curate/                    ← heti riportok
    └── 2026-W21.md
```

### 2.2 Sage agent home — a "brain"

```
00_Prompts/BDOS/agents/sage/
├── SAGE_DESIGN_v0.1.md        ← ez a fájl
├── SAGE.md                    ← rövid kanonikus agent leírás (későbbi)
├── REFERENCE_FORMAT.md        ← példák, hogy mit ért meg Sage biztosan
├── state/
│   ├── last_run.md            ← KRITIKUS: dashboard ezt olvassa
│   ├── last_seen.md           ← ChatGPT-side state (utolsó feldolgozott üzenet)
│   └── chatgpt_snapshot.md    ← legutóbb látott folder/chat sorrend
├── prompts/
│   ├── daily_harvest.md
│   ├── weekly_curate.md
│   └── chat_persona.md
└── learnings/                 ← meta-kognició (lásd 6.5)
    ├── 00_INDEX.md
    ├── active/
    ├── proposals/
    └── retired/
```

---

## 3. Schema-k

### 3.1 Thought note (`thoughts/`)

```yaml
---
schema: sage.thought.v1
title: <emberi cím>
date: 2026-05-24
note_revision: 1
source_chat_title: "AI alapú operációs rendszer"
source_chat_url: https://chatgpt.com/...
source_project: "ExarLabs"          # ChatGPT projekt / folder név
source_author: self                  # self | ChatGPT-5 | hibrid
category: philosophy                 # Sage által adott, heti curate felülbírálhatja
subcategory: ai-architecture         # opcionális
status: new                          # new | reviewed | archived
distribution_hints: [LinkedIn]       # üres lista is OK
atomic_links:
  - "[[atomic/cognition-distribution-wall]]"
related_thoughts:
  - "[[thoughts/2026-05-23_editorial-governance]]"
tags: [ai-ops, architecture, exarlabs]
---

## Egy mondatban
<1 mondatos summary — a dashboard ezt mutatja card-fejlécben>

## Kifejtés
<1-2 bekezdés a TE szóhasználatoddal>

## Az eredeti szöveg
> <pontos idézet a chatből — markdown blockquote>

## Instrukciók
- <distribution hint vagy egyéb user-utasítás>

## Kapcsolódó atomi gondolatok
- [[atomic/...]]
```

### 3.2 Atomic note (`atomic/`)

```yaml
---
schema: sage.atomic.v1
title: <absztrakt elv neve>
slug: cognition-distribution-wall
note_revision: 3
status: maturing                     # nascent | maturing | crystallized | retired
first_seen: 2026-05-23
last_updated: 2026-05-24
category: philosophy
tags: [ai-architecture, governance]
source_thoughts:
  - "[[thoughts/2026-05-23_editorial-governance]]"
  - "[[thoughts/2026-05-24_cognition-distribution-wall]]"
---

## A gondolat (absztrakt)
<a gondolat lényege, függetlenül kontextustól>

## Konkrét példák
1. <példa 1>
2. <példa 2>

## History
- 2026-05-23 — első megfogalmazás · [[thoughts/2026-05-23_editorial-governance]]
- 2026-05-24 — note_revision 3, megerősítve · [[thoughts/2026-05-24_cognition-distribution-wall]]
```

### 3.3 Journal entry (`_journal/YYYY-MM.md`)

Append-only, minden Sage-akció **egy** sor + opcionális részletek. Strikt YAML-blokk minden bejegyzéshez, hogy dashboard parseolhassa:

```markdown
---

```yaml
event: harvest
ts: 2026-05-24T06:00:12+02:00
run_id: 2026-05-24-daily
references_seen: 2
thoughts_created: 1
atomic_proposals: 1
inbox_uncertain: 0
notified_user: false
notes:
  - "[[thoughts/2026-05-24_cognition-distribution-wall]]"
  - "[[_inbox/atomic_proposals/marketing-as-translation-layer]]"
```
```

(Megj.: a markdown-on belüli YAML codeblock azért, hogy Obsidianban olvasható maradjon, és egy egyszerű regex `^---$ ... ^```yaml$ ... ^```$` parser is megtalálja.)

### 3.4 `last_run.md` — dashboard contract

**Ez a fájl a single source of truth Curator dashboardja számára.** Sage minden futás végén ezt kötelezően frissíti.

```yaml
---
schema: sage.lastrun.v1
last_daily_run_at: 2026-05-24T06:00:42+02:00
last_daily_run_id: 2026-05-24-daily
last_daily_status: ok               # ok | error | partial | no_references
last_weekly_run_at: 2026-05-18T06:05:33+02:00
last_weekly_run_id: 2026-W20-curate
last_weekly_status: ok
totals:
  thoughts: 23
  atomic: 7
  inbox_thoughts: 1
  inbox_atomic_proposals: 2
last_harvest:
  references_seen: 2
  thoughts_created: 1
  atomic_proposals: 1
  inbox_uncertain: 0
  notified_user: false
  notes:
    - path: thoughts/2026-05-24_cognition-distribution-wall.md
      title: A cognition és distribution layer között fal kell
      category: philosophy
last_curate:
  emergent_patterns: 0
  category_changes: 0
  atomic_promotions: 0
  librarian_queries: 0
  learning_proposals: 0           # új tanulság-javaslatok
learnings:
  active: 7
  proposed: 2
  retired: 3
  preamble_tokens: 1240           # aktuálisan a prompt-ba töltött tanulságok mérete
errors: []
---

# Sage — Last Run

Ez egy gép-és-ember-olvasható state fájl. A frontmatter a forrás.
Részletek: lásd `_journal/`.
```

---

## 4. Workflow-k

### 4.1 Daily harvest — minden nap 06:00

```
1. Read state/last_seen.md (utolsó feldolgozott üzenet ID + ts)
2. Read state/chatgpt_snapshot.md (utolsó látott folder/chat sorrend)
3. Open Referencia chat (Chrome MCP, work browser)
4. Snapshot: aktuális folder/chat sorrend → write state/chatgpt_snapshot.md
5. Iterate új üzeneteken (azok, amik > last_seen):
   a) Parse referencia (project + chat title + window + hints)
   b) Nem értelmezhető? → _inbox/thoughts/<date>_uncertain_<slug>.md
   c) Értelmezhető? →
      - Open hivatkozott chat (Chrome MCP navigate)
      - Olvasd a window-t (default: last 15 üzenet)
      - Kinyer gondolat (TE szóhasználatoddal, csak user-üzenetekből)
      - Generál thoughts/<date>_<slug>.md (schema sage.thought.v1)
      - Detektál atomic mintát → _inbox/atomic_proposals/<slug>.md
6. Update 00_INDEX.md (regenerate)
7. Append _journal/2026-05.md (event: harvest)
8. Write state/last_run.md (overwrite)
9. Update state/last_seen.md (utolsó feldolgozott üzenet)
10. NOTIFY user IF:
    - thoughts_created >= 3 (sok új gondolat egy futásban)
    - inbox_uncertain > 0 (figyelmet kér)
    - errors not empty
    ELSE: csend.
```

### 4.2 Weekly curate — hétfő 06:05

```
1. (Várja meg, hogy daily harvest végzett — fájl-lock check state/last_run.md-on)
2. Olvas: thoughts/* + atomic/* + _inbox/* + curate/2026-W{N-1}.md
3. Trend-analízis: melyik kategóriában nőtt a sűrűség
4. Kapcsolat-keresés: mely thought-ok között hiányzik a wikilink, de szemantikailag rokonok
5. Kategória-revízió:
   - rename ha jobb név van
   - merge ha 2 kategória átfed
   - új ha emergens minta
   - update 00_CATEGORIES.md
6. Librarian-kérések (main Claude orchestrátoron át):
   pl. "kérlek hozz minden AI-ops kontextust az elmúlt hétből"
   pl. "mi történt Navigátor-rel az elmúlt 7 napban"
7. Atomic promote-javaslatok: melyik _inbox/atomic_proposals/ érett crystallized-é
8. Eredmény: curate/2026-W21.md
   - max 3 emergens minta
   - max 2 atomic promote-javaslat
   - kategória-változás lista
   - figyelmet érdemlő thought-ok (nem zaj)
9. Append _journal/2026-05.md (event: curate)
10. Write state/last_run.md (overwrite weekly részt)
11. NOTIFY user IF:
    - emergent_patterns >= 1 (legalább 1 erős minta)
    - errors not empty
    ELSE: csend.
```

### 4.3 `/sage-chat` — interaktív mód

A Sage perszóna betöltődik (`prompts/chat_persona.md`), kontextusa:
- Teljes Ideas/ mappa elérhető
- Librarian retrieve-en keresztül mély vault-hozzáférés
- Beszélgetésközben módosíthat note-ot (csak `--confirm` után)
- Beszélgetés ideje alatt nem ír journal-t — csak ha mutáció történik

---

## 5. Slash commandok

| Command | Mód | Confirmation | Mit csinál |
|---|---|---|---|
| `/sage-status` | info | — | last_run.md kiolvasása, emberi formátum |
| `/sage-harvest` | manual run | — | Kézi napi harvest (cron-on kívül) |
| `/sage-curate` | manual run | igen | Kézi heti curate (drága, megerősítés kell) |
| `/sage-summary --days N` | info | — | Összefoglaló az elmúlt N napról |
| `/sage-find <query>` | retrieval | — | Keresés a thoughts/+atomic/ tárban |
| `/sage-chat` | interactive | — | Beszélgetés mély vault kontextussal |
| `/sage-edit <note>` | mutation | igen | Note edit / refine |
| `/sage-promote <thought-slug>` | mutation | igen | thought → atomic promote (vagy _inbox/atomic_proposals/ → atomic/) |
| `/sage-index` | maintenance | — | 00_INDEX.md regenerálás |

---

## 6. Architekturális invariánsok

Ezek a szabályok megsértése = bug, nem feature.

1. **Csend default.** Sage csak akkor notifikál, ha minta van. Lásd workflow-k notify feltételeit.
2. **Idempotencia.** Kétszeri futás ugyanazon az inputon → ugyanaz a vault-állapot. last_seen state biztosítja.
3. **Markdown-natív state.** Minden Sage-állapot `.md` fájl, frontmatter YAML-lel. Sosem JSON-only. (Frontmatter YAML self.)
4. **Flat orchestration.** Sage nem hív direkt másik agentet. Heti curate-kor Librarian-kéréseket megfogalmaz, main Claude továbbít.
5. **Append-only journal.** `_journal/` sorai sosem törölhetők. Csak append.
6. **Inbox > false positive.** Bizonytalan harvest → `_inbox/`, soha nem hallucinált note.
7. **Linkek nem törnek.** Slug-alapú nevezés, kategória-váltás csak frontmatter-edit, fájl nem mozog.
8. **Dashboard-contract.** `last_run.md` schemája visszafelé kompatibilis kell maradjon. Új mezők hozzáadhatók, régiek nem törölhetők → új major schema verzió kell hozzá.
9. **Learnings láthatók és visszavonhatók.** Minden Sage-learning markdown, user által editálható, törölhető. Sosem rejtett súly. Cap: max 15 active learning / max 2000 token preamble.
10. **Sebesség nem cél, mélység igen.** Sage inkább lassan, mint felszínesen. Egy futás 10 percig is mehet — a vault-állapot kell jó legyen, nem a wall-time.

---

## 6.5 Sage learning loop (meta-kogníció)

> **Sage nem csak ápolja a tudásbázist — Sage tanul attól, hogy ápolja.**

A daily harvest és weekly curate során Sage megfigyeli a saját munkáját: milyen referencia-formátumokat ért meg könnyen, milyen kategória-nevek bizonyulnak tartósnak, milyen atomic javaslatokat fogadsz el / utasítasz el, hol történik félreértés. Ezekből **explicit, human-readable tanulságokat** ír — és a következő futáshoz betöltődnek a promptjába.

Ez NEM finomhangolás, NEM rejtett "súly". Minden tanulság markdown fájl, amit te bármikor megnyithatsz, editálhatsz vagy törölhetsz.

### 6.5.1 Mit tanul Sage

| Tanulság-típus | Példa | Mit változtat |
|---|---|---|
| `harvest-pattern` | "User gyakran 'az utolsó 10-15 üzenet' alatt valójában 25-30-at ért — érdemes nagyobb ablakot olvasni" | bővíti az olvasási ablakot |
| `category-naming` | "User többször átnevezte 'mindset' → 'philosophy'. Az új gondolatokat 'philosophy'-ba sorolja default" | default kategória-választás |
| `atomic-detection` | "3+ thought-ban szereplő absztrakció jó atomic-jelölt. 2-ben szereplő még korai" | promote-küszöb |
| `user-taste` | "User elutasított 5 db 'meta-' kezdetű atomic javaslatot — kerülöm" | proposal-szűrő |
| `voice-style` | "User voice-átirataiban gyakori szófordulatok ('gyakorlatilag', 'tulajdonképpen') nem instrukciók" | parser tolerancia |
| `failure-mode` | "Ha a referencia chat URL fragmentet tartalmaz (#message-...), navigate meghiúsulhat. Csip le az URL-ről." | hibakerülés |
| `linking-pattern` | "User azokat a thought-okat kérdezi vissza, amik atomic-kal vannak crosslinkelve. Több crosslink = jobb." | aggresszívabb crosslink |
| `signal-noise` | "Heti curate-ben max 2 emergent pattern eddig minden héten elég volt. 3+ már zaj." | curate output cap |

### 6.5.2 Hol élnek a tanulságok

```
00_Prompts/BDOS/agents/sage/learnings/
├── 00_INDEX.md                ← Sage által generált, csak active learningek
├── active/                    ← jelenleg loadolódó tanulságok
│   ├── 2026-05-24_user-rejects-meta-atomic.md
│   ├── 2026-05-24_window-15-means-25.md
│   └── 2026-05-25_category-philosophy-canonical.md
├── proposals/                 ← Sage javasolta, még nem confirmed
│   └── 2026-05-26_voice-fillers.md
└── retired/                   ← már nem alkalmazott (archived, NEM törölt)
    └── 2026-05-12_obsolete-pattern.md
```

### 6.5.3 Életciklus

```
proposed  ──user-review──>  active  ──unused 4 weeks──>  retired
   │                          │
   │                          └──contradicts new──>  retired (auto)
   │
   └──user-reject──>  retired (with reason)
```

- **proposed**: Sage észrevett valamit, de még csak hipotézis. Heti curate-kor user-review.
- **active**: Confirmed. Bekerül a következő futás promptjába.
- **retired**: Vagy elavult (4 hét nem segített), vagy ellentmondásba került egy újabbal, vagy user-rejected. Soha nem törölve, csak archived (audit miatt).

### 6.5.4 Learning schema

```yaml
---
schema: sage.learning.v1
slug: user-rejects-meta-atomic
type: user-taste                # harvest-pattern | category-naming | atomic-detection | user-taste | voice-style | failure-mode | linking-pattern | signal-noise
status: active                  # proposed | active | retired
confidence: high                # low | medium | high
proposed_at: 2026-05-24
confirmed_at: 2026-05-25
last_applied_at: 2026-05-30
applications_count: 4
evidence:
  - "2026-05-12 _journal: user rejected [[atomic/_inbox/meta-cognition-pattern]]"
  - "2026-05-18 _journal: user rejected [[atomic/_inbox/meta-feedback-cycle]]"
  - "2026-05-22 _journal: user rejected [[atomic/_inbox/meta-observer-bias]]"
retired_at: null
retired_reason: null
---

## A tanulság
A user elutasítja a 'meta-' prefixű, túl-absztrakt atomic-javaslatokat. Az ő atomic preference-je konkrét, alkalmazható elvek.

## Hatás a Sage-re
Atomic-detection során a 'meta-', 'meta-cognition', 'meta-feedback' kezdetű candidates nem mennek _inbox/-ba automatikusan. Ehelyett kifejezetten konkrét megfogalmazást próbál.

## Hogyan vonom vissza
Ha 2 héten belül a user maga ír 'meta-' kezdetű atomic-ot kézzel, ez retired.
```

### 6.5.5 Mikor írnak tanulság-javaslatot

Sage **csak** akkor javasol új learninget, ha:
- weekly curate fut (nem napi — túl korai lenne aggregálni)
- ÉS 3+ független evidence összegyűlt egy mintára
- ÉS a megfigyelt minta nem konfliktál active learninggel (vagy ha konfliktál, az új a régit retired-be küldi)

Tehát egy reggeli harvest-ben Sage **nem** ír új learning fájlt. Csak megfigyel — a journal-be jegyez — és a heti curate aggregálja.

### 6.5.6 Hogyan alkalmazza Sage a tanulságokat

A daily harvest és weekly curate promptja minden futás elején betölt egy **learnings preamble**-t:

```
Sage active learnings (top-N by confidence × recency):
1. [user-taste] Ne javasolj 'meta-' kezdetű atomic-ot — user 5x rejected. Konkrét megfogalmazást próbálj.
2. [category-naming] 'philosophy' a canonical, ne 'mindset'.
3. [harvest-pattern] '10-15 üzenet' valójában 20-25-öt olvass — user gyakran alábecsüli.
4. [linking-pattern] Minden új thought-hoz legalább 1 atomic crosslink kötelező, ha van releváns atomic.
...
```

A preamble cap: **max 15 active learning**, vagy **max 2000 token**. Ami előbb. Ezzel megelőzzük a prompt-bloat-ot.

Ha több aktív learning van, mint amennyi befér, a sorrend: `confidence (high>medium>low) DESC, last_applied_at DESC`.

### 6.5.7 Védelmek

| Veszély | Védelem |
|---|---|
| Runaway prompt growth | 15 / 2000 token cap, retired ha unused 4 hét |
| Hidden drift | Minden learning markdown, user által editálható |
| Self-reinforcing bias | Heti curate-kor user reviewelheti az active learningeket |
| Conflict | Két ellentmondó learning közül az újabb wins, régi retired-be megy `retired_reason: superseded_by <slug>` |
| Hallucination | Minden learning kötelező evidence-szel (min. 2 journal-entry hivatkozással) |
| Over-confidence | `high` confidence csak akkor adható, ha 5+ evidence ÉS 2+ hét alkalmazás után még mindig helyes |

### 6.5.8 User-control commandok

Hozzáadva a slash-command listához (lásd 5. szekció):

| Command | Mit csinál |
|---|---|
| `/sage-learnings` | Active learnings listája emberi formában |
| `/sage-learnings --proposed` | Pending proposals review-hoz |
| `/sage-learning-accept <slug>` | proposed → active |
| `/sage-learning-reject <slug> --reason "..."` | proposed → retired (reason kötelező) |
| `/sage-learning-retire <slug>` | active → retired manuálisan |
| `/sage-learning-edit <slug>` | active learning szövegének editálása |

### 6.5.9 Filozófiai keret

Ez a tanulási loop az, ami megkülönbözteti Sage-t egy statikus harvest-scripttől. De **NEM** autonóm intelligencia — pontosan a cognition stack brainstorm szellemében:

> "Az AI segít az embernek nagyobb léptékben gondolkodni anélkül, hogy elveszítené a saját emberi középpontját."

A tanulság a vault-ban él, te bármikor láthatod és visszavonhatod. Sage nem "fejlődik a hátad mögött". Sage *megfigyel és javasol*, te *elfogadsz vagy elutasítasz*. Ez ugyanaz a hierarchia, mint a publish-gate-é a marketing oldalon: Sage javaslattevő, te döntéshozó.

### 6.5.10 Sebességkompromisszum

Mivel a user explicit kimondta: **a sebesség nem fontos, a minőség az** → Sage learning-loop minden döntésnél a mélyebb feldolgozást választja, ha kompromisszum van. Konkrétan:

- Heti curate akár 15-20 percig is mehet — full reread engedélyezve
- Librarian-kéréseket nem batch-eli, egyenként mehet a mélyebb retrieval kedvéért
- Atomic detekciónál inkább proposal mint kihagyás (false negative drágább, mint a user 1 review)
- Tanulság-evidence collection nem korlátos: ha 10 journal-entry kell egy mintához, mindet beolvassa

---

## 7. Dashboard-readiness contract (Curator számára)

Curator építeni fog egy HTML dashboardot, ami **élőben** olvassa a vault-ot. Sage erre így van felkészítve:

### 7.1 Single source of truth fájlok

| Fájl | Mit ad a dashboardnak |
|---|---|
| `agents/sage/state/last_run.md` | utolsó futás összes statisztikája, schema sage.lastrun.v1 |
| `Ideas/00_INDEX.md` | minden thought + atomic listája wikilinkekkel |
| `Ideas/00_CATEGORIES.md` | élő kategória-lista |
| `Ideas/_journal/<YYYY-MM>.md` | havi audit trail, parseolható YAML-blokkok |
| `Ideas/curate/<YYYY-Www>.md` | heti riport |
| `agents/sage/learnings/active/*.md` | aktív tanulságok (meta-kogníció) — dashboard megmutathatja "Sage hogyan tanul" panelt |
| `agents/sage/learnings/00_INDEX.md` | learnings áttekintés gyors render-hez |

### 7.2 Parseolhatóság garanciái

- Minden Sage-generált markdown frontmatter-rel kezdődik, kötelező mezővel: `schema: sage.<type>.v<N>`
- A frontmatter szigorú YAML — nincs benne markdown / inline link / multiline string trick
- A wikilinkek mindig `[[path/from/Ideas-root/slug]]` formában — sosem `[[slug]]` only
- A journal YAML-blokkok mindig ```` ```yaml ```` és ```` ``` ```` között
- Dátumok mindig ISO 8601 (`2026-05-24` vagy `2026-05-24T06:00:42+02:00`)

### 7.3 No-hardcode invariáns

A dashboard HTML soha nem tartalmaz konkrét gondolatot, kategóriát vagy fájlnevet. Minden adat futásidőben jön a fenti fájlokból.

---

## 8. Nyitott / halasztott döntések

| # | Kérdés | Halasztva | Decision deadline |
|---|---|---|---|
| 1 | Sage perszóna hangja a `/sage-chat`-ben (érlelő bölcs vs. kritikus szerkesztő) | v0.2 | első chat session után |
| 2 | Atomic note "retired" életcsklus — mikor archiváljunk | v0.2 | első 3 atomic után |
| 3 | Cross-vault retrieval — Librarian csak Ideas-en kívül, vagy mindenhol | most: mindenhol | — |
| 4 | Notification csatorna (chat overlay vs. daily notes vs. külön notify file) | v0.2 | implementáció során |
| 5 | Atomic note konfliktus-kezelés (ha 2 atomic ugyanazt mondja) | heti curate kezeli (merge) | — |
| 6 | ChatGPT auth lejárat — recovery flow | v0.2 | első auth-fail után |

---

## 9. Implementációs lépések (sorrend)

1. ✅ **Design v0.2** — ez a fájl
2. **REFERENCE_FORMAT.md** — 3-4 példa hogy mit ért meg Sage biztosan
3. **state/last_run.md skeleton** — üres, schema-helyes
4. **learnings/00_INDEX.md skeleton** — üres index + folder struktúra
5. **prompts/daily_harvest.md** — a fat prompt + learnings-preamble loader logika
6. **prompts/weekly_curate.md** — learning-proposal aggregálási logikával
7. **prompts/chat_persona.md**
8. **.claude/agents/sage.md** — Claude Code runtime regisztráció
9. **.claude/commands/sage-*.md** — 15 slash command (9 alap + 6 learnings-control)
10. **Scheduling** — daily 06:00, weekly Monday 06:05 (CronCreate)
11. **Smoke test** — egy manuálisan beírt referencia a Referencia chatben, `/sage-harvest` futtatás
12. **00_AGENTS_INDEX.md update** — Sage felvétele
13. **CLAUDE.md update** — agent rendszer szekcióba Sage hozzáadás
14. **Curator briefing** — dashboard-spec átadása (ez a fájl 7. szekciója + learnings panel)

---

## 10. Hivatkozások

- BDOS belépő: [`00_Prompts/BDOS/CLAUDE.md`](../../CLAUDE.md)
- Agentek index: [`00_Prompts/BDOS/00_AGENTS_INDEX.md`](../../00_AGENTS_INDEX.md)
- Cognition stack brainstorm: [`00_Prompts/BDOS/brainstorm/brainstorm_cognition_stack_2026-05-23.md`](../../brainstorm/brainstorm_cognition_stack_2026-05-23.md)
- Referencia chat: https://chatgpt.com/g/g-p-67987afa409c8191b7ce9f798c887544-szemelyes-gondolatok/c/6a1265db-8910-83eb-8677-1e977c03fc01
- Vault konvenciók: `[CLAUDE.md](../../../../CLAUDE.md)`

---

## Záró elv

> **Érlelj, ne reagálj. Inkább csend, mint zaj. A gondolat fontosabb a publikációnál. És minden héten légy egy kicsivel jobb — láthatóan, visszavonhatóan.**
