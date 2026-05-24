---
title: Standard tier recept — 7 réteg + Pulse
version: 0.1
date: 2026-05-14
tier: standard
target: tipikus marketing site · scale-up · közepes vállalkozás · service business
description: Brand Spine Standard tier recept — 7 réteg + Pulse loop tipikus marketing site-okhoz és scale-up cégekhez. A Maestro `continue` és `next` módjai ezt olvassák a lépéssorrendhez és tool/skill ajánlásokhoz.
id: 0dd78bf3-74b4-4a94-8040-116a18994298
index_schema_version: 1
---

# Standard Tier Recept (7 réteg + Pulse)

> **Mikor használd:** tipikus marketing site, scale-up cég, service business — ahol a brand már megérdemli a külön Narrative UX réteget ÉS a külön Creative Direction munkát. Komplexebb mint Lean (több oldal, több persona, több sales cycle stage), de nem high-ticket B2B (akkor → Premium).

## A Standard 7 rétege — a Brand Spine v0.2 standard tier

| # | Réteg | Default tool | Tipikus időigény |
|---|---|---|---|
| 1 | **Brand Core** | brand-toolkit · brand-voice | 1-2 óra |
| 2 | **Market & Audience Reality** | brand-toolkit · brand-radar + Cowork:PM · user-research-synthesis | 2-3 óra |
| 3 | **Positioning & Offer** | brand-toolkit · brand-positioning (Dunford 5) | 1-2 óra |
| 4 | **Messaging & Proof Architecture** | brand-toolkit · brand-messaging (StoryBrand) + marketingskills · copywriting | 2-3 óra |
| 5 | **Narrative UX + IA** | impeccable · shape | 3-5 óra |
| 6 | **Creative Direction → Design System** | brand-toolkit · brand-visual-identity → ui-ux-pro-max + designer-skills | 4-6 óra |
| 7 | **Build + Polish + Quality Gate** | impeccable · craft + audit + polish | 8-15 óra |
| ↻ | **Pulse** | marketingskills · ab-test-setup + analytics-tracking | folyamatos |

## Rétegenkénti recept

### L1. Brand Core

**Cél:** 1-2 oldal: miért létezünk, miben hiszünk, karakter, mit nem csinálunk. NEM 20 oldalas manifesto.

| Default | brand-toolkit · brand-voice (NN/g + Aaker + Jung) |
|---|---|
| **Alternatíva** | Cowork:marketing · brand-voice (egyszerűbb) |
| **Artifact** | `./brand-core.md` |

### L2. Market & Audience Reality

**Cél:** ICP / persona, JTBD-állítások, awareness-szintek (Schwartz létra), competitive alternatives.

| Default | brand-toolkit · brand-radar (versenytárs-intel) + Cowork:PM · user-research-synthesis (interjúk) |
|---|---|
| **Alternatíva** | marketingskills · customer-research (Reddit/G2 mining), Dembrandt (versenytárs visual) |
| **Artifact** | `./audience.md` — 3-5 JTBD + awareness map + competitive landscape |

### L3. Positioning & Offer

**Cél:** Dunford 5-komponens pozicionálás + Offer architecture (mit ajánlunk, milyen áron, milyen konverziós céllal).

| Default | brand-toolkit · brand-positioning |
|---|---|
| **Alternatíva** | Cowork:PM · competitive-analysis + feature-spec (egy mondatos positioning kihasználása) |
| **Artifact** | `./positioning.md` — 1 mondat positioning + offer-térkép + primary CTA |

### L4. Messaging & Proof Architecture

**Cél:** Üzeneti hierarchia (StoryBrand 7-elem) + Objection mapping + Proof inventory.

| Default | brand-toolkit · brand-messaging |
|---|---|
| **Alternatíva** | marketingskills · copywriting (CRO-tudatos) |
| **Artifact** | `./messaging.md` — message hierarchy + objections list + proof inventory |

### L5. Narrative UX + IA

**Cél:** Sitemap (milyen oldalak), narratív ív (probléma → miért mi → bizonyíték → akció), wireframe-ek **tényleges szöveggel** (lorem ipsum tilos), CTA-térkép.

**Kritikus szabály:** a copy a wireframe-mel **együtt születik**, nem utólag.

| Default | impeccable · shape |
|---|---|
| **Alternatíva** | Cowork:design · user-research + designer-skills · wireframe-spec |
| **Artifact** | `./wireframes/<page>.md` minden tervezett oldalra (3-7 oldal) |

### L6. Creative Direction → Design System

**Cél:** **ELŐBB** vizuális irány (stylescape — 3 ellentétes javaslat), **AZUTÁN** formalizált rendszer (paletta, tipográfia, tokenek, komponensek, restraint rules).

**Anti-reference check KÖTELEZŐ** — olvasd be a `_anti_references.md` vagy state `anti_references` mezőjét.

| Default | brand-toolkit · brand-visual-identity (Chris Do stylescape) → ui-ux-pro-max (industry default) → designer-skills (audit) |
|---|---|
| **Alternatíva** | ux-pilot (dialógus-első) + Tokven (token gen) + Dembrandt (versenytárs visual) |
| **Artifact** | `./stylescape.md` (3 irány) + `./design-system.md` (a kiválasztott) |

### L7. Build + Polish + Quality Gate

**Cél:** kész, production-grade site + minőségi kapu (a11y, perf, responsive, image quality, consistency, interaction restraint).

| Default | impeccable · craft → audit → polish |
|---|---|
| **Alternatíva** | impeccable · harden (production hardening) + Cowork:design · /accessibility |
| **Artifact** | a kész HTML/CSS site + `./quality-audit.md` |

**Handoff:** kész site → Microsite Factory (deploy / DNS / SSL / analytics).

### ↻ Pulse

**Cél:** Analytics + A/B + iteráció. **Visszacsatol a L2-L4 rétegekre** elsősorban (nem a vizuálra).

| Default | marketingskills · analytics-tracking + ab-test-setup |
|---|---|
| **Alternatíva** | Cowork:marketing · performance-analytics |
| **Artifact** | `./pulse-log.md` — folyamatos kísérleti napló |

## Tipikus iteráció Standard tier-ben

```
Week 1: L1-L4 (stratégia) — kb. 8-10 óra
Week 2: L5 (narrative + wireframes) — kb. 5 óra
Week 3: L6 (visual identity + design system) — kb. 6 óra
Week 4-5: L7 (build + polish + QA) — kb. 15 óra
Week 6: Microsite Factory deploy
Week 7+: Pulse loop indul
```

## Mit ad többet Standard (vs Lean)

- ✅ Külön Narrative UX réteg (több oldal, több narratív ív)
- ✅ Külön Creative Direction réteg a design system előtt (mood-first, nem token-first)
- ✅ Explicit Proof architecture (Objection mapping + proof inventory)
- ✅ Explicit Offer architecture (több offerrel is dolgozhat)
- ✅ Komplex Pulse (A/B + multivariáns kísérletek)

## Mikor lépj át Premium-ra

Ha bármelyik igen:
- ❑ Több, mint 1 célközönség (B2B + B2C, vagy enterprise + SMB)
- ❑ High-ticket sales cycle (>3 hét, >€10k deal size)
- ❑ Új kategória teremtése (Category Design)
- ❑ Befektetői oldal vagy boardroom-grade
- ❑ Multi-language / multi-region
- ❑ >10 oldalas site
