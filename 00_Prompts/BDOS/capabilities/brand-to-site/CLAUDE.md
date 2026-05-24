---
title: Brand Spine — Constitution-to-Site Capability
version: 0.3
date: 2026-05-14
author: Becze Szabolcs
status: design
description: BDOS capability — mentális modell + munkamódszer: mi rejlik egy komplex, gyönyörű, de letisztult marketing weboldal mögött. v0.2 — 7 rétegű "Decision Spine" + Pulse loop + Lean/Standard/Premium tier-ek, multi-AI brainstorm alapján (ChatGPT Strategist + Perplexity Researcher + Gemini Validator). Nevesített frameworkök (Dunford, StoryBrand, JTBD, Kapferer, Atomic Design, Content-First) + bővített tool-stack. A Microsite Factory upstream rétege.
id: bfe7779a-6b00-44bb-928b-3abdf7c3f752
index_schema_version: 1
---

# Brand Spine

> **Mappanév (canonical):** `brand-to-site` · **Brand-név (working):** Brand Spine · **v0.2** (2026-05-13)

> **Státusz:** design. A v0.2 a multi-AI brainstorm (ChatGPT + Perplexity + Gemini, [`../../brainstorm/brainstorm_brand-spine.md`](../../brainstorm/brainstorm_brand-spine.md)) eredménye. Validálás: DH pilot, Lean tier-rel.

## Cél

Egy **döntési gerinc** (nem "szép weboldal gyártási folyamat"), ami megválaszolja: *mi rejlik egy komplex és gyönyörű, de mégis letisztult marketing weboldal mögött?* — és megakadályozza, hogy szétessen a stratégia, a copy, a design és a build között.

A válasz nem a vizuális rétegben születik. A v0.1 8 rétege jó intuíció volt, de keverte a stratégiai / input / gyártási / minőségi-gate rétegeket, lineáris vízesésnek tűnt, és hiányzott belőle a proof, az offer és a mérés. A v0.2 ezeket javítja.

## A modell — v0.2 "Decision Spine" (Standard: 7 réteg + Pulse)

> Vizuális verzió: [`diagram.html`](diagram.html). **NEM vízesés** — a copy és a wireframe együtt születik (5–6), feedback loopok vannak, a Pulse visszacsatol a 2–5. rétegre.

| # | Réteg | Mit termel | Framework(ök) | Eszköz |
|---|-------|------------|---------------|--------|
| 1 | **Brand Core** *(volt: Alkotmány)* | Miért létezünk, miben hiszünk, mi a karakterünk, mit nem csinálunk. NEM 20 oldalas manifesto — 1 oldal elég. A gyökér, ettől nem generikus. | Golden Circle (Sinek), Brand Pyramid | `brand-toolkit` (voice skill) |
| 2 | **Market & Audience Reality** | Kinek szól, milyen érettségi szinten (awareness), milyen alternatívákat mérlegel, milyen döntési helyzetben érkezik, kik a versenytársak. JTBD: milyen *haladást* akar elérni. | Jobs-to-be-Done (Christensen), Ladder of Awareness | `brand-toolkit`; `Dembrandt` (versenytárs-audit) |
| 3 | **Positioning & Offer** | Kategória, fő ígéret, differenciátor, a konkrét ajánlat, a konverziós cél. | **April Dunford — Obviously Awesome** (5 komp.: competitive alternatives → differentiated capabilities → value → best-fit customers → market category) | `brand-toolkit` (positioning skill) |
| 4 | **Messaging & Proof Architecture** | Üzeneti hierarchia, objections (mitől nem hisz nekünk?), proof points, trust elemek. A "letisztult üzenet" itt áll össze — a szavak még nem. | StoryBrand BrandScript / PEACE (Miller), Message-Market Fit, Objection Mapping | `brand-toolkit` (messaging skill); `marketingskills` |
| 5 | **Narrative UX + IA** | Milyen oldalak/szekciók, milyen sorrendben, a meggyőzési ív (probléma → miért mi → bizonyíték → akció), a CTA-logika, a látogatói út. **Együtt születik a 6-tal.** | Content-First (UX Collective 8 lépés), StoryBrand wireframe | `impeccable` (gondolkodó mód) |
| 6 | **Creative Direction → Design System** | ELŐBB a vizuális irány (prémium / artisan / editorial / tech / minimal…), AZUTÁN a formalizált rendszer: paletta, tipográfia, tokenek, komponensek, restraint rules. A design system nem tokenekből indul — egy erős vizuális irányból. | Kapferer Prism (Physique → visual identity), Chris Do stylescape, Atomic Design (tokens→atoms→…), W3C Design Tokens (DTCG) | `ui-ux-pro-max` + `ux-pilot` (dialógus-első) + `designer-skills` (audit) + `Dembrandt` (asset extract) + `Tokven` (token gen) |
| 7 | **Build + Polish + Quality Gate** | A design systemből + copyból + IA-ból a kész, mobiloptimalizált site + minőségi kapu: performance, responsive, a11y, image quality, consistency, interaction restraint. **Itt lakik a "gyönyörű"** — a craft a kivitelezésben. | Atomic Design (komponens-szint), Mobile-First | `impeccable` (build+polish mód) → handoff a [Microsite Factory](../web-publishing/CLAUDE.md)-nak |
| ↻ | **Pulse** *(loop, nem réteg)* | Analytics, A/B teszt, iteráció. Visszacsatol a 2–5. rétegre. A v0.1-ből teljesen hiányzott. | Message-Market Fit mérés, CRO | `marketingskills` (analytics/CRO skillek); a Microsite Factory analytics-rétege |

### Inputok (nem rétegek)

- **Brand asset audit** — logó, meglévő színskála, tipográfia, fotóstílus, brand debt, tabuk. Korlátozza a 6. réteget. Eszköz: `Dembrandt` (meglévő site / versenytárs → W3C DTCG tokenek).
- **Content / media inventory** — van-e jó fotó, videó, termékkép, ügyféllogó? Ha nincs, a creative direction máshogy néz ki.
- **Business model logika** — teljes BMC csak ha kell (prémium/B2B); landinghez elég a monetizációs logika: kinek, milyen offerrel, milyen konverzióval.

## Tier-ek — méret szerint (a "Húsüzlet-szindróma" ellen)

A 7 rétegű Standard nem mindenkinek való. Egy hentesnek bizalom + konverzió kell (nyitvatartás, cím, árlista, rendelés gomb), nem 20 oldalas manifesto és teljes BMC — különben analízis-paralízis.

| Tier | Rétegek | Mikor |
|------|---------|-------|
| **Lean (5)** | Brand Core + Positioning *(összevonva)* → Offer / üzleti logika → Copy-first wireframe *(IA + Copy együtt)* → Visual identity *(asset audit + design direction + system)* → Build + Polish · **+ Pulse** | Kisvállalkozás (DH!), kampányoldal, MVP, sales landing |
| **Standard (7)** | a fenti 7 réteg + Pulse | Tipikus marketing site, scale-up |
| **Premium (9)** | + Business Logic *(teljes BMC)* külön réteg; Audience+JTBD külön a Positioning-tól; Offer/Conversion architecture külön réteg | Prémium szolgáltatás, B2B high-ticket, befektetői oldal, új kategória, többoldalas site |

## Hol lakik a szépség — a capability tézise (változatlan, élesítve)

- **Letisztult** = önmegtartóztatás. Egy gondolat / szekció, egy típus/szín/mozgásrendszer, whitespace. → a design system (6) + a jó IA (5) adja.
- **Komplex & gyönyörű** = craft a **kivitelezésben** (7), nem a katalógusban. `ui-ux-pro-max` / `ux-pilot` korrekt defaultot ad — a gyönyörű az, amikor az `impeccable` a korrekt rendszert mesterien építi meg.
- **Jelentéssel teli** (nem generikus) = a Brand Core (1) + Positioning (3) + Messaging (4). A legtöbb csúnya marketing oldal azért az, mert ezeket átugrották.
- **És működik is** *(új a v0.2-ben)* = mert pontosan tudjuk: kinek (2), milyen döntési pillanatban (3), milyen új hitet kell elfogadnia ahhoz, hogy cselekedjen (4) — és mert mérjük (Pulse).

## Mire NEM jó / a v0.2 csendes feltételezései, amik nem mindig igazak

- A vízió ritkán stabil — a piac diktál; a Brand Core gyakran csak a végére tisztul le. → ezért van Pulse.
- Az AI-eszközök NEM hibátlanok — kockázati forrás, nem magic bullet. A 7. réteg quality gate-je nem opcionális.
- A szépség nem feltétlen = konverzió — a "gyönyörű" oldal lehet lassú/zavaró. A craft a konverziót *szolgálja*, nem helyettesíti.
- Nem helyettesíti a stratégiai munkát (1–4) — ezt embernek/brainstormnak kell elvégeznie.
- `ui-ux-pro-max` / `ux-pilot` = katalógus, nem code generator marketing-weboldalhoz.

## Tool-stack (v0.2 — bővített)

| Cél | Tool | Megjegyzés |
|-----|------|------------|
| Brand strategy → messaging (1–4) | **brand-toolkit** (jgerton/GitHub, MIT) | 10 skill: Dunford positioning, StoryBrand messaging, NN/g+Aaker voice, Chris Do visual identity; megosztott `brand-brief.md`, confidence score, anti-slop. `git clone https://github.com/jgerton/brand-toolkit.git` |
| Copy + CRO + analytics (4, 7, Pulse) | **marketingskills** (coreyhaines31/GitHub, MIT, 5700+⭐) | 23–30 skill: CRO, copywriting, SEO, analytics, email, pricing. `npx add-skill coreyhaines31/marketingskills` |
| Design system audit (6) | **designer-skills** (Owl-Listener/GitHub, 977⭐) | 87 skill / 27 parancs; design-systems plugin: token coverage, naming, a11y, theming; `/strategize`. `/plugin marketplace add Owl-Listener/designer-skills` |
| Design katalógus — dialógus-első (6) | **ux-pilot** (Sakaax/GitHub, free) | 376 UX szabály, 161 paletta, 57 fontpár, 67 stílus; **kiegészíti** az ui-ux-pro-max-ot, discovery flow generálás előtt + élő preview. `/plugin marketplace add Sakaax/ux-pilot` |
| Design katalógus (6) | **ui-ux-pro-max** (nextlevelbuilder, már telepítve) | 161 reasoning rule, 161 paletta, 99 UX guideline, 1923 font, 25 chart, 10 stack |
| Brand asset audit / versenytárs (input, 2) | **Dembrandt** (CLI + MCP) | bármely site → W3C DTCG tokenek. `npm i -g dembrandt; dembrandt competitor.com --dtcg` |
| Token generálás (6) | **Tokven** (tokven.dev) | brand briefből token rendszer, WCAG AA validáció, DO/NEVER irányelvek |
| Token build pipeline (6–7) | **Style Dictionary** (Amazon), **Tokens Studio** | W3C DTCG kompatibilis, Figma→kód |
| UI/UX ítélet + polish (5, 7) | **impeccable** (pbakaus/GitHub, már telepítve) | Anthropic frontend-design-ra épül (277k telepítés), 7 ref fájl, 17 parancs; Tessl benchmark 0.82/1.00 (+0.35). **MARAD** — jól teljesít |

## Viszony a Microsite Factory-hoz

```
Brand Spine (1→7 + Pulse)  ──kész site──▶  Microsite Factory  ──▶  Cloudflare/Netlify · DNS · SSL · analytics
   "mit, kinek, miért — és működik-e"          "hogyan élesítjük"          ↑ a Pulse loop ide is köthet
```

## Open questions

- [ ] Brand-név (user-facing): **Brand Spine** working — végleges? (alt: Decision Spine, Constitution-to-Site, Gerinc)
- [ ] Telepítsük a feltárt toolokat? (`brand-toolkit`, `ux-pilot`, `designer-skills`, `marketingskills`) — vagy egyelőre csak dokumentáljuk?
- [ ] A "Pulse" loop — kötődjön-e formálisan a Microsite Factory analytics-rétegéhez?
- [ ] DH pilot: a Lean (5) tier-rel fussunk neki, és mi a tanulság?
- [ ] Kapnak-e a frameworkök külön sablon-fájlokat (`positioning-template.md`, `storybrand-script.md`, `content-first-ia.md`), vagy inline workflow marad?
- [x] ~~Kell-e BDOS-agent ehhez (pl. "Brand Steward"), vagy skill-orchestráció elég?~~ **Eldöntve 2026-05-14:** igen, kell. → **Maestro** agent létrehozva (v0.1). Lásd: [`../../agents/maestro.md`](../../agents/maestro.md).

## Agent: Maestro *(v0.1 LIVE)*

A capability **végrehajtó-agentje** a [`Maestro`](../../agents/maestro.md) — Brand-to-Site Conductor. Felelőssége:

- **Felmérés:** hol tart a projekt a 7+1 réteg / 3-tier struktúrában
- **Javaslat:** a következő konkrét lépés (réteg + tool + skill + parancs)
- **Folytatás:** félbehagyott munka resume-olása
- **Indítás:** új projekt setup (tier + state-fájl)
- **Audit:** minőségi check a kész rétegeken

Minden projekt egy **`brand-spine-state.md`** fájllal rendelkezik az Area gyökerében — ez a Maestro single source of truth. Séma: [`state-schema.md`](state-schema.md).

**5 mód** (lásd canonical spec §4):
| Mód | Mit csinál | Confirmation kell? |
|---|---|---|
| `status` | Riportál: hol vagyunk, hány %-on, mi a következő | nem |
| `next` | Részletesen javasolja a következő lépést | nem |
| `continue` | Folytatja a félbehagyott munkát, lefuttat skillt | ✅ igen |
| `start` | Új projekt: létrehozza a state-fájlt | ✅ igen |
| `audit` | Minőségi check a kész rétegeken | nem |

**Autonómia:** confirmation gate kötelező minden Write / Edit / skill-invocation előtt.

## Tier-receptek

Mindhárom tier-hez külön recept-fájl van — ezek mondják meg a Maestro-nak, milyen sorrendben mit hívjon:

| Tier | Rétegek | Recept | Mikor |
|---|---|---|---|
| **Lean** | 5 + Pulse | [`recipes/lean.md`](recipes/lean.md) | Kisvállalkozás, MVP, kampányoldal, sales landing |
| **Standard** | 7 + Pulse | [`recipes/standard.md`](recipes/standard.md) | Tipikus marketing site, scale-up |
| **Premium** | 9 + Pulse | [`recipes/premium.md`](recipes/premium.md) | Prémium szolgáltatás, B2B high-ticket, befektetői oldal |

## Templates

Minden réteghez egy kitölthető sablon — a Maestro a `continue` mód végén ezekből generál artifact-okat:

- [`templates/brand-spine-state.md.template`](templates/brand-spine-state.md.template) — a state-fájl initial sablon
- [`templates/layer-1-brand-core.md.template`](templates/layer-1-brand-core.md.template)
- [`templates/layer-2-audience.md.template`](templates/layer-2-audience.md.template)
- [`templates/layer-3-positioning.md.template`](templates/layer-3-positioning.md.template)
- [`templates/layer-4-messaging.md.template`](templates/layer-4-messaging.md.template)
- [`templates/layer-5-ia-narrative.md.template`](templates/layer-5-ia-narrative.md.template)
- [`templates/layer-6-design-system.md.template`](templates/layer-6-design-system.md.template)
- [`templates/layer-7-build.md.template`](templates/layer-7-build.md.template)
- [`templates/pulse.md.template`](templates/pulse.md.template)

## Struktúra

```
capabilities/brand-to-site/
├── CLAUDE.md            ← ITT — meta, belépő, a v0.2 modell + tier-ek + tool-stack
├── diagram.html         ✅ vizuális folyamatdiagram (v0.2)
├── decision-matrix.html ✅ tool × képesség hőtérkép
├── state-schema.md      ✅ a brand-spine-state.md kanonikus formátuma
├── recipes/             ✅ tier-onkénti receptek
│   ├── lean.md
│   ├── standard.md
│   └── premium.md
├── templates/           ✅ 9 layer + state template
│   ├── brand-spine-state.md.template
│   ├── layer-1-brand-core.md.template
│   ├── layer-2-audience.md.template
│   ├── layer-3-positioning.md.template
│   ├── layer-4-messaging.md.template
│   ├── layer-5-ia-narrative.md.template
│   ├── layer-6-design-system.md.template
│   ├── layer-7-build.md.template
│   └── pulse.md.template
└── pilots/              (TODO — DH végigfuttatás naplója, Lean tier)
```

## Hivatkozott

- BDOS belépő: [`../../CLAUDE.md`](../../CLAUDE.md)
- Multi-AI brainstorm napló: [`../../brainstorm/brainstorm_brand-spine.md`](../../brainstorm/brainstorm_brand-spine.md)
- Downstream capability: [Microsite Factory](../web-publishing/CLAUDE.md)
- DH pilot-napló: [`../../../../02_Areas/Deák Húsüzlet/brainstorm/brainstorm_bdos.md`](../../../../02_Areas/Deák%20Húsüzlet/brainstorm/brainstorm_bdos.md)
- Toolok: brand-toolkit (github.com/jgerton/brand-toolkit) · marketingskills (github.com/coreyhaines31/marketingskills) · designer-skills (github.com/Owl-Listener/designer-skills) · ux-pilot (github.com/Sakaax/ux-pilot) · impeccable (github.com/pbakaus/impeccable) · ui-ux-pro-max (github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- **Maestro agent (v0.1):** [`../../agents/maestro.md`](../../agents/maestro.md) · [`.claude/agents/maestro.md`](../../../../.claude/agents/maestro.md)
- **Tool inventory:** [`../../tools/INVENTORY.md`](../../tools/INVENTORY.md)
- **Decision matrix:** [`decision-matrix.html`](decision-matrix.html)
