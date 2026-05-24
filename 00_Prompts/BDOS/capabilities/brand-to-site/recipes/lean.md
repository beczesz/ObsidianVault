---
title: Lean tier recept — 5 réteg + Pulse
version: 0.1
date: 2026-05-14
tier: lean
target: kisvállalkozás · kampányoldal · MVP · sales landing · pilot
description: Brand Spine Lean tier recept — 5 réteg + Pulse loop kisvállalkozásokhoz, MVP-khez, kampányoldalakhoz. A Maestro `continue` és `next` módjai ezt olvassák a lépéssorrendhez és a tier-specifikus tool/skill ajánlásokhoz.
id: d511b4ac-bb20-4050-af74-15ed278d9c69
index_schema_version: 1
---

# Lean Tier Recept (5 réteg + Pulse)

> **Mikor használd:** kisvállalkozás (pl. DH húsüzlet), kampányoldal, MVP, sales landing. Olyan projekt, ahol a "Húsüzlet-szindróma" elleni védelem kell — egy hentesnek **bizalom + konverzió** kell (nyitvatartás, cím, árlista, rendelés-gomb), nem 20 oldalas manifesto. **Kerüljük az analízis-paralízist.**

## A Lean 5 rétege — összevonások

A Standard 7-ből összevonással:

| Lean réteg | Mit fed le a Standardból | Default tool |
|---|---|---|
| **L1. Foundation** | Brand Core + Positioning *(összevonva)* | brand-toolkit · brand-positioning (+ brand-voice quick) |
| **L2. Audience + Offer** | Market & Audience Reality + Offer architecture | brand-toolkit · brand-audit (lite) |
| **L3. Copy-first Wireframe** | Messaging + Narrative UX + IA + Copy *(együtt)* | impeccable · shape + brand-toolkit · brand-landing-page |
| **L4. Visual Identity** | Brand asset audit + Creative Direction + Design System | ui-ux-pro-max + impeccable · craft |
| **L5. Build + Polish** | Build + Quality Gate | impeccable · craft + audit + polish |
| **↻ Pulse** | Analytics + iteration | marketingskills · analytics-tracking |

## Rétegenkénti recept

### L1. Foundation — *Brand Core + Positioning egyben*

**Cél:** egy oldalas brand-brief, amiben: miért létezünk, miben hiszünk, karakter, mit nem csinálunk, kategória, fő ígéret, differenciátor, célpiac.

| Default tool | brand-toolkit · brand-positioning (+ brand-voice gyors) |
|---|---|
| **Alternatíva** | Cowork:marketing · brand-voice (egyszerűbb, nincs Dunford keret) |
| **Várt artifact** | `./brand-brief.md` |
| **Tipikus időigény** | 30-60 perc |
| **Kész-jel** | A brand-brief 1 oldalon elfér, és a "mit nem csinálunk" mező is tele van |

**Maestro-prompt sablon (telepített tool esetén):**
```
/brand-toolkit:brand-positioning "<projekt rövid leírása + iparág + helyzet>"
```

### L2. Audience + Offer

**Cél:** kinek szól, milyen JTBD-vel, milyen alternatívák ellen, **milyen konkrét offerrel** (mit kínálunk, milyen áron/feltétellel, milyen konverziós céllal).

| Default tool | brand-toolkit · brand-audit + brand-radar (versenytárs) |
|---|---|
| **Alternatíva** | Cowork:product-management · user-research-synthesis + competitive-analysis |
| **Várt artifact** | `./audience-offer.md` — 1-3 JTBD állítás + offer-leírás + CTA-cél |
| **Tipikus időigény** | 30-45 perc |
| **Kész-jel** | Konkrét offer (nem általános), megfogalmazva: "**ki**nek **mit** kínálunk, **hogyan** konvertál" |

### L3. Copy-first Wireframe — *Messaging + Narrative + IA + Copy együtt*

**Cél:** Konkrét site-szerkezet **tényleges szöveggel** (lorem ipsum tilos). Section sorrend = meggyőzési ív (probléma → miért mi → bizonyíték → akció).

| Default tool | brand-toolkit · brand-landing-page (StoryBrand structure) → impeccable · shape (wireframe) |
|---|---|
| **Alternatíva** | marketingskills · copywriting + site-architecture |
| **Várt artifact** | `./wireframes/<page>.md` minden tervezett oldalra (Lean: 1-3 oldal max) |
| **Tipikus időigény** | 60-120 perc / oldal |
| **Kész-jel** | Minden section-höz tartozik egy gondolat + egy proof point + valós szöveg |

**Maestro-prompt sablon:**
```
/brand-toolkit:brand-landing-page "audience-offer.md alapján — fő landing page"
↓
/impeccable shape "<oldal-név>" --reference=./wireframes/landing.md
```

### L4. Visual Identity — *Brand audit + Creative Direction + Design System*

**Cél:** asset audit (mi van már: logó, színek, fotók) + creative direction (a hangulat, **stylescape**) + formalizált design system (paletta, tipográfia, tokenek, komponensek).

| Default tool | Dembrandt (asset audit) + ui-ux-pro-max (design system gen) + impeccable · craft (formalizálás) |
|---|---|
| **Alternatíva** | ux-pilot (dialógus-első) + Tokven (token gen) |
| **Várt artifact** | `./design-system.md` + `./stylescape.md` |
| **Tipikus időigény** | 90-150 perc |
| **Kész-jel** | A design system kitölti a teljes anti-reference listát (nem hasonlít a többi vault-projektre) |

**Anti-reference check KÖTELEZŐ** itt — olvasd be a `_anti_references.md`-t vagy a state.yaml `anti_references` mezőjét.

### L5. Build + Polish + Quality Gate

**Cél:** kész, mobiloptimalizált HTML site + minőségi kapu (a11y, perf, responsive, image quality, consistency).

| Default tool | impeccable · craft → audit → polish |
|---|---|
| **Alternatíva** | impeccable · harden (production-ready) |
| **Várt artifact** | a kész HTML/CSS site, plus `./quality-audit.md` |
| **Tipikus időigény** | 3-5 óra |
| **Kész-jel** | Quality gate átment: WCAG AA, LCP < 2.5s, 375px-en is működik, reduced-motion respektált |

**Handoff:** a kész site → Microsite Factory (deploy → DNS → SSL → analytics).

### ↻ Pulse (loop, post-ship)

**Cél:** analytics + iteráció. **Visszacsatol a L2-L3 rétegekre** (nem a vizuálra elsősorban).

| Default tool | marketingskills · analytics-tracking + ab-test-setup |
|---|---|
| **Alternatíva** | Cowork:marketing · performance-analytics |
| **Várt artifact** | `./pulse-log.md` — hipotézisek, tesztek, eredmények, iterációk |
| **Kész-jel** | NEM kész — folyamatos. Havi review-val. |

## Tipikus iteráció a Lean tier-ben

Egy DH-szerű projekt jellemző naplója:

```
Day 1 (3 óra): L1 (Foundation) + L2 (Audience + Offer)
Day 2 (3 óra): L3 (Copy-first wireframe, 1 oldal)
Day 3 (3 óra): L4 (Visual identity)
Day 4-5 (6-8 óra): L5 (Build + Polish + QA)
Day 6: Microsite Factory deploy
Week 2+: Pulse loop indul
```

## Mit hagy ki a Lean (vs Standard)

- ❌ Teljes BMC (csak monetizációs logika kell)
- ❌ Külön Messaging & Proof Architecture réteg (a Copy-first wireframe-ben implicit)
- ❌ Külön Creative Direction réteg a design system előtt (összevonva)
- ❌ Külön Offer/Conversion Architecture (az Audience+Offer-be vonva)

**Ha bármelyik kérdés merül föl, hogy "kell-e nekem külön kezelni ezt a réteget?"** — valószínűleg már **Standard** tier-be lépünk át.

## Hivatkozott

- Brand Spine modell: [`../diagram.html`](../diagram.html)
- Tool inventory: [`../../../tools/INVENTORY.md`](../../../tools/INVENTORY.md)
- Decision matrix: [`../decision-matrix.html`](../decision-matrix.html)
- Pilot példa: DH (`02_Areas/Deák Húsüzlet/brand-spine-state.md`)
