---
title: Microsites — Open Questions
date: 2026-05-27
description: Nyitott kérdések az ExarLabs Microsites practice area körül. Forge `reflect` mód periodikusan átfut és vagy `research/`-ba forward-eli (külső kutatást igénylő) vagy `_inbox/`-ba (várjuk hogy egy engagement evidence-t hozzon). Lezárt kérdések áthelyeződnek `decisions/` ADR formájában. Bootstrap-állapot — induló kérdés-szettet ExarLabs lead-jel finomítandó.
bdos_index: false
id: 6e889386-e56f-46c6-b197-1ad22b9760e4
index_schema_version: 1
---

# Microsites — Open Questions

> Élő nyitott-kérdés-lista. Forge `reflect` mód karbantartja.

## Archetypes & patterns

- [ ] **Q-001:** Mely microsite-archetypes-ok (landing / one-pager / brand intro / event / product launch / personal brand) van pinned scope-pal a Microsites practice-ben?
- [ ] **Q-002:** Egyes archetypes-okra van-e dedicated layout-template-ünk (LP-1, LP-2, OP-1, OP-2, etc.) ami AI-assisted gyorsan kitölthető?
- [ ] **Q-003:** Melyik archetype-ra hány óra reálisan az AI-assisted produkció? (Anchor árazáshoz)

## AI plugin combo

- [ ] **Q-004:** Mi a default plugin-combo egy "Standard tier" microsite-hoz? (impeccable + designer-skills + ?)
- [ ] **Q-005:** ui-ux-pro-max + ux-pilot kombináció mikor érdemes (komplex UX) vs. csak impeccable (egyszerű landing)?
- [ ] **Q-006:** Mely AI-tool-okat soha NE használjuk Microsites-context-ben (failure modes-ban)?

## Design tokens & systems

- [ ] **Q-007:** Default token-pack van-e ExarLabs Microsites-szempontból, vagy minden site-specific?
- [ ] **Q-008:** Atomic Design hierarchia: érdemes-e standardizálni component-nevezést cross-microsite?
- [ ] **Q-009:** Dark-mode mint default vs opt-in: ExarLabs Microsites alapértelmezett policy?

## Performance & accessibility

- [ ] **Q-010:** Core Web Vitals target: minden microsite-nak ugyanaz a target (LCP < 2.5s, etc.) vagy tier-szerint?
- [ ] **Q-011:** WCAG AA minimum vs AAA aspirational: ExarLabs Microsites default?

## Deploy stack

- [ ] **Q-012:** Default deploy target: Cloudflare Pages, Netlify, Vercel — mikor melyik?
- [ ] **Q-013:** Custom domain + SSL workflow time-to-deploy benchmark?
- [ ] **Q-014:** Light CMS (Sanity, Contentful, baked-in markdown) — mikor érdemes egyiket vagy másikat?

## Packaging & pricing

- [ ] **Q-015:** Lean / Standard / Premium tier konkrét deliverable-scope-ja és árazás-anchorja?
- [ ] **Q-016:** Egyedi engagement-eknél (kliens-specific extras) milyen overpricing-multipláló reális?
- [ ] **Q-017:** Maintenance / iteration tier (renewal) van-e külön, vagy egyszeri delivery default?

## Strategic / cross-area

- [ ] **Q-018:** ExarLabs Brand-to-Site Pipeline lesz-e külön practice area, vagy a Microsites magába olvasztja?
- [ ] **Q-019:** CPS-kliensnek microsite-deliverable szállítása (pl. case study microsite) — ExarLabs viszi vagy CPS? Cross-unit kollaboráció mintája?
- [ ] **Q-020:** Marketing case study Microsites-practice-area-ról (Presto-relevant): érdemes-e külön case study?

## Shared theme architecture (factory gap)

- [ ] **Q-021:** **Shared header-partial + shared logó-asset a témában.** Megfigyelt gap (2026-06-05, repo `microsite-factory` v0.6.0): az exar téma a header/logó **stílusát** közös elemként tartja (`themes/exar/components.css`: `.site-header`, `.header-inner`, `.logo-link`, `.logo-wordmark`), DE a **header HTML-markup** és **maga a logó-fájl** (`logo-shield.png` / `-sm.png`) duplikálva van mind a 4 exar site-ban (`exarlabs-main`, `exarlabs-sites`, `exarlabs-catalog`, `digitalizare`). A `.logo-mark` méretező CSS is site-onkénti `style.css`-ben él, nem a témában. → **Drift-kockázat:** ha a logó vagy a header-struktúra változik, 4 helyen kell kézzel editálni. **Megoldási irány:** téma-szintű `partials/header.html` + `assets/` (shared bináris), amit a `new-site.sh` / build-step injektál (mint a jelenlegi `__THEME_FONTS__` marker a `fonts.html`-re). Eldöntendő: (a) HTML-partial mechanizmus kell-e a téma-rendszerbe általában, (b) shared-asset (logó) hogyan deployoljon Workers alatt, (c) ez factory MINOR vagy MAJOR bump. Forge-releváns: ez az első konkrét repo-derived pattern/decision-candidate a practice area-ban.

## Closed (moved to decisions/ as ADRs)

*Üres — még nincs lezárt kérdés.*

---

## Change log

| Date | Event |
|---|---|
| 2026-05-27 | Fájl létrehozva. 20 induló nyitott kérdés rögzítve archetypes / AI-tooling / design / performance / deploy / packaging / strategic kategóriákban. Bootstrap-szintű — ExarLabs lead-jel finomítandó. |
| 2026-06-05 | **Q-021** felvéve (Forge, user-kérés) — shared header-partial + shared logó-asset gap az exar témában. Első repo-derived (bound `microsite-factory` v0.6.0) decision-candidate. |
