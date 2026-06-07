---
type: practice
id: 6d2a8f51-c739-4b86-9e14-2a7f3c0b5e89
practice: "Microsites"
unit: "ExarLabs"
unit_display: "ExarLabs"
unit_short: "Exar"
slug: exarlabs-microsites
owner: "TBD (ExarLabs lead)"
status: active
maturity_stage: patterns-emerging
description: ExarLabs practice area for AI-assisted microsite delivery. Both a research focus (how to generate beautiful, brand-aligned microsites efficiently with AI tooling) and a productized service (deliverable to clients). Connects upstream to BDOS `brand-to-site` capability (design pipeline) and `web-publishing` capability (deploy + DNS + SSL infrastructure). Bootstrap created 2026-05-27 as a cross-unit example of the practice-area pattern.

# At-a-glance (Forge dashboard card — kept in sync by Forge)
strategic_directions:
  - "AI-assisted microsite delivery as productized service-line"
  - "Bridge BDOS brand-to-site (upstream design) + web-publishing (deploy) capabilities"
  - "Tier productization: Lean / Standard / Premium scoping"
next_step: "Patterns inventory a bound repo factory-outputjaiból (14 élő site, v0.6.0 soul-first) → patterns/microsite-archetypes.md"
deadline: null
blocker: "ExarLabs lead időbeosztás az inventory-passhoz"

# Bound repository (source of truth a factory implementációra — Forge mindig pull-lel kezd, push-sal végez)
bound_repository:
  path: "/Users/becze-mac/Downloads/Work/ExarLabs/microsite-factory"
  remote: "git@github.com:ExarLabs/microsite-factory.git"
  branch: "master"
  factory_version: "0.6.0"
  git_protocol: "pull-first, push-last (mindig git pull munka előtt, git push commit után; soha force-push)"
  skill_entry: ".claude/skills/microsite-build/SKILL.md"
top_todos:
  - "Inventory existing microsite assets (Glob ExarLabs/**/*.html + Ignis/**/*.html)"
  - "Pin archetype-pattern vocabulary (landing / one-pager / event / brand intro)"
  - "Define Lean / Standard / Premium tier scope + árazás-anchor"

tags: [practice, exarlabs, microsites, ai-assisted, design, web-publishing, service-offering]
created: 2026-05-27
last_signal: 2026-06-05
related_engagements: []
related_practices:
  - "BDOS capability: brand-to-site"
  - "BDOS capability: web-publishing"
counts:
  open_questions: 21
  related_engagements: 0
  learnings_active: 0
  learnings_proposed: 0
bdos_index: false
index_schema_version: 1
---

# Microsites — ExarLabs Practice Area

> **Status 2026-05-27:** `active` / `patterns-emerging` stage. Bootstrap példa-szinten létrehozva Forge v0.1-mel együtt. Mid- to long-term ExarLabs strategic offering.

## Mission

**AI-asszisztált microsite szállítás mint service-line.** Egy practice, ami egyszerre:
- **Kutatási terület:** hogyan generálunk gyönyörű, brand-aligned, technikailag kifogástalan microsite-okat AI-eszközökkel a leghatékonyabban?
- **Szolgáltatás:** klienseknek odaadható deliverable — landing page, kampány-site, one-pager, brand microsite, event-site, etc.

A practice "duális természete" az egyik tipikus jellemzője — pont ezért **practice area** és nem csak "BDOS capability" vagy "client project".

## Scope

**In scope:**
- AI-assisted design generation (with `impeccable`, `ui-ux-pro-max`, `designer-skills` plugin stack)
- Brand spine pipeline application — design tokens, component library, content-first structure
- HTML/CSS/JS hand-crafted output (no heavy framework dependency)
- Deploy automation (Cloudflare Pages / Netlify / Vercel)
- DNS + SSL setup
- Performance optimization (Core Web Vitals)
- Accessibility (WCAG AA min)
- Light CMS overlay (when needed — typically content baked-in)

**Out of scope:**
- Full-stack web applications (más service-line)
- E-commerce platforms (más service-line)
- Multi-page marketing sites > ~10 pages (más service-line vagy custom engagement)
- Brand identity development from scratch (`brand-toolkit` upstream, nem itt)

## Current state

**Maturity:** `patterns-emerging`. ExarLabs portfolio több microsite-ot szállított már (a vault `_dashboards/_design/`-ban + Ignis/marketing/design folder-ekben több HTML asset látható). Néhány pattern már kikristályosodott, de **NEM** dokumentált structured way-ben — pont ezért kell a practice area.

**Bootstrap state (2026-05-27):** mappa-szerkezet létrehozva. Tartalom (research, patterns, decisions, experiments, proposals) progresszívan kerül feltöltésre ahogy ExarLabs lead és a team time-ot tesz rá.

**First fill-up priority:** a meglevő ExarLabs microsite-eredmények inventory-zása. Egy `patterns/microsite-archetypes.md` ami katalogizálja: campaign landing, one-pager, brand intro, event-site, etc. — az ExarLabs portfolio alapján.

## Bound repository (source of truth)

> **Forge tudja: ehhez a practice area-hoz tartozik egy élő git repo. Mindig `git pull`-lal kezd, `git push`-sal végez.**

A Microsite Factory **éles implementációja** egy különálló git repóban él, NEM a vaultban. A vault tartja a cognition/pattern réteget (ez a practice area); a repo tartja az élő kódot, a skilleket és a deploy-tooling-ot.

| Mező | Érték |
|---|---|
| **Path** | `/Users/becze-mac/Downloads/Work/ExarLabs/microsite-factory` |
| **Remote** | `git@github.com:ExarLabs/microsite-factory.git` |
| **Branch** | `master` |
| **Factory verzió** | `0.6.0` (soul-first + experience release) |
| **Skill belépő** | `.claude/skills/microsite-build/SKILL.md` (+ `impeccable`, `ui-ux-pro-max` bundled) |
| **Site-ok** | 14 regisztrált site a `registry.yaml`-ban (production) |

### Git-protokoll (kötelező, minden session)

1. **Munka előtt:** `git -C <path> pull` — mindig friss állapotból indulunk
2. **Munka után:** commit + `git -C <path> push` — soha ne maradjon helyi-only változás
3. **Soha** force-push, soha közvetlen production-edit (a factory saját Phase 4-5 deploy-disciplinje érvényes)
4. A factory verziózás a repo `CHANGELOG.md` + `CLAUDE.md` szerint megy; Forge ezt **nem** írja felül, csak olvassa és pattern-szinten visszacsatolja

### Mit olvas Forge a repóból (top-down + bottom-up flow)

- `CHANGELOG.md` — metodológia-evolúció (v0.1 → v0.6.0), minden release tanulsága
- `.claude/skills/microsite-build/SKILL.md` — az 5-fázisú workflow kanonikus definíciója
- `sites/<slug>/docs/` — per-site stratégia-artefaktumok, amikből archetype-pattern desztillálható
- `registry.yaml` — a teljes site-portfólió inventory

A refined pattern-ek (archetype-vocabulary, tier-scoping, soul-first módszer) a repo factory-outputjaiból kristályosodnak ki → ide, a `patterns/` mappába (3+ evidence küszöbbel).

## Reference architecture

**Design pipeline (upstream):**
- BDOS [`brand-to-site`](../../../../00_Prompts/BDOS/capabilities/brand-to-site/CLAUDE.md) capability — 7-réteg Decision Spine + Pulse loop + Lean/Standard/Premium tier-ek

**Build pipeline (this practice):**
- AI-assisted design (impeccable, designer-skills, ui-ux-pro-max)
- Content-first prompting (StoryBrand, JTBD, Kapferer integration)
- Token + Atomic Design component generation
- Static HTML/CSS/JS output

**Deploy pipeline (downstream):**
- BDOS [`web-publishing`](../../../../00_Prompts/BDOS/capabilities/web-publishing/CLAUDE.md) capability — Cloudflare / Netlify API + DNS + SSL

A practice **összeköti a Brand Spine (design) felső réteget a Microsite Factory (deploy) alsó réteggel** ExarLabs-szempontú konkrét service-szállítássá.

## Why this practice area

1. **Recurring deliverable type** — több ExarLabs-projektnek volt microsite-output, anélkül hogy systematized lenne
2. **AI-assisted gain** — ezen a területen az AI-tooling **különösen** jó leverage-et ad (impeccable + designer-skills + ui-ux-pro-max kombóval 5-10x gyorsulás)
3. **Brand Spine + Microsite Factory bridge** — ExarLabs az unit ami a két BDOS capability-t éles deliverable-é forrasztja
4. **Cross-unit potencial** — CPS, Sonrisa más unit-ok is szállíthatnak microsite-deliverable-t client-engagementhez (pl. case study microsite, conference microsite); ExarLabs lehet a központi practice-owner

## Strategic positioning

A Microsites practice **több sub-practice-re bonthatja** időközben:
- **Campaign Landing** — short-lived, time-bound, conversion-fókusz
- **Brand One-Pager** — evergreen, pozícionálás-fókusz
- **Event Microsite** — dátum-kötött, rich content
- **Personal Brand Site** — egyéni szakember-site
- **Product Launch Microsite** — termék-bevezetés specific

Most: egy area, később felbontható.

## Folder structure

```
Microsites/
├── NOTES.md             ← ITT
├── _inbox/              ← raw dump-ok
├── research/            ← külső research (Awwwards inspirations, vendor blogs, design system papers)
├── patterns/            ← refined design patterns (microsite-archetypes, common layouts)
├── decisions/           ← ADR-ek (which CMS, which deploy target, which AI plugin combo)
├── experiments/         ← amit kipróbáltunk (Cloudflare Workers vs Pages, etc.)
├── proposals/           ← ügyfél-facing template-ek (Lean/Standard/Premium tier-ek)
├── learnings/           ← Forge structured learnings
├── related-projects.md  ← wikilinks engagementekhez
└── open-questions.md    ← nyitott kérdések
```

## Related engagements

Lásd: [[related-projects]]

## Open questions

Lásd: [[open-questions]]

## Forge log (append-only)

| Date | Event |
|---|---|
| 2026-05-27 | Practice area létrehozva — Forge v0.1 bootstrap cross-unit példaként. Maturity: `patterns-emerging` (több létező ExarLabs deliverable van, de nem dokumentált). First fill-up priority: inventory a meglevő microsite-eredmények alapján. |
| 2026-06-05 | **Repo binding** — Maestro a Microsite Factory git repóhoz kötötte ezt a practice area-t (`bound_repository` frontmatter + Bound repository szekció). Forge mostantól tudja: a factory implementáció a `Downloads/Work/ExarLabs/microsite-factory` repóban él (v0.6.0, 14 site), és a git-protokoll pull-first / push-last. Forge v0.1.0 → v0.1.1. User explicit felhatalmazás. |
| 2026-06-05 | **Q-021 felvéve** (open-questions) — shared header-partial + shared logó-asset gap az exar témában. A header/logó stílusa közös (téma `components.css`), de a markup + logó-fájl duplikálva van mind a 4 exar site-ban. Első repo-derived decision-candidate. Forge filing, user-kérés. |
