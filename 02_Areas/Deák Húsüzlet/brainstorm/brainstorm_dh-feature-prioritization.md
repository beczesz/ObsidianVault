---
description: "A DH platform Sprint 4 prioritási rangsora, amit ChatGPT és Perplexity AI-val közösen felállított egy csapat. Tartalmazza a tiered feature listát, a pilot KPI-kra fókuszált fő elveket és az egyesített javaslat a második rendelés valószínűségének növelésére."
description_source: auto
description_hash: d399d1394a71e342
topic: DH Feature Prioritization — Sprint 4/5/Backlog
created: 2026-05-01
last_updated: 2026-05-01
status: active
id: e2da6b87-cf00-41db-b263-4e7eaede6c2f
index_schema_version: 1
---
# Brainstorm: DH Feature Prioritization

## Team
| AI | Role | URL |
|----|------|-----|
| ChatGPT (Deák GPT) | Strategist | https://chatgpt.com/g/g-p-69cbee4a04c481918a2a738959b92361-deak/c/69da0a38-ce68-8391-bfb4-a2bbf24a66e7 |
| Perplexity | Researcher | https://www.perplexity.ai/search/072cbfa0-d36a-4109-8fd2-27eece7362cc |

## Sessions
| Date | Team | Key Outcome |
|------|------|-------------|
| 2026-05-01 | ChatGPT (Strategist) + Perplexity (Researcher) | Unified priority ranking for 18 features; Sprint 4 scope defined |

## AI Session Links
- ChatGPT: https://chatgpt.com/g/g-p-69cbee4a04c481918a2a738959b92361-deak/c/69da0a38-ce68-8391-bfb4-a2bbf24a66e7 (2026-05-01)
- Perplexity: https://www.perplexity.ai/search/072cbfa0-d36a-4109-8fd2-27eece7362cc (2026-05-01)

---

## Szintézis: Egyesített Prioritási Rangsor

### Alapelv (mindkét AI egyetért)

> **Most nem a platform gazdagságát kell növelni, hanem a második rendelés valószínűségét.**

A pilot célja: 30 regisztráció, 15 rendelés, 5 visszatérő vásárló 30 napon belül. Minden feature, ami nem ezt szolgálja, másodlagos.

**Framework:** MoSCoW a legjobb <50 user pilotnál (Perplexity kutatás). RICE adathiány miatt nem működik pre-revenue fázisban. Kano max second-pass lensként.

---

### Egyesített Prioritási Lista (1-18)

#### TIER 1 — Sprint 4 MUST (közvetlen pilot KPI hatás)

| # | Ticket | Feature | Miért most | Forrás |
|---|--------|---------|-----------|--------|
| 1 | DH-174 | Admin ár-korrekció (befejezés) | Már In Progress, blocker | ChatGPT |
| 2 | DH-148 | Reorder Quick Panel ("Utolsó rendelésed") | North Star = 2nd Order Rate → ez a #1 retention lever. Perplexity: "30% repeat order increase" redesign után | Mindkettő |
| 3 | DH-173 | Termék testreszabás (szűk MVP: top 5 SKU) | Bizalom + "ismer engem" érzés. Perplexity: customization reduces offline clarification, high-value for butcher | Mindkettő |
| 4 | NEW | Falusi route pilot (minimál MVP) | Nem teljes delivery platform, hanem: 1 település, settlement-based zone, fix nap, cutoff, checkout info. Access > convenience hipotézis tesztelése | ChatGPT |
| 5 | DH-161 | Timeslot kapacitás-limit | Operációs védőkorlát — ha szétesik a kiszolgálás, nem lesz 2nd order. Különösen fontos falusi route esetén | ChatGPT |
| 6 | DH-134 | Privacy Policy (v0.4 BLOCKER) | Csak ha mobil app Sprint 4 cél — egyébként SHOULD | ChatGPT |
| 7 | DH-135 | App Store developer account (v0.4 BLOCKER) | Csak ha mobil app Sprint 4 cél — egyébként SHOULD | ChatGPT |

#### TIER 2 — Sprint 5 SHOULD (retention + expansion)

| # | Ticket | Feature | Miért itt | Forrás |
|---|--------|---------|----------|--------|
| 8 | DH-127 | Familiar Favourites ("Szokásos rendelésem") | Reorder következő szintje — de a Quick Panel előbb jön | ChatGPT |
| 9 | DH-51 | Szállítási zóna korlátozás (teljesebb) | Falusi pilot után kell a teljesebb delivery zone rendszer | ChatGPT |
| 10 | DH-139 | Rendelésszám egyszerűsítés (DH-0001) | Support és bizalmi feature, alacsony effort | ChatGPT |
| 11 | DH-165 | Admin platformdíj kalkulátor | Üzletileg hasznos, de nem customer-facing, nem húzza KPI-t | ChatGPT |
| 12 | DH-146 | Kedvenc Termékek (csillag toggle) | Hasznos de alacsonyabb prioritás mint order-level reorder | Mindkettő |

#### TIER 3 — Backlog / Later (nice-to-have)

| # | Ticket | Feature | Miért később | Forrás |
|---|--------|---------|-------------|--------|
| 13 | DH-149 | Shared Basket (Group Order) | Stratégiailag erős (AOV, social), de operációsan komplex. Nem Sprint 4 | ChatGPT |
| 14 | DH-128 | Swap suggestion MVP | Korai — user még nem bízik eléggé az online húsvásárlásban | ChatGPT |
| 15 | DH-163 | Szezonális cikk oldal (Grillszezon) | Marketing content, alacsony pilot ROI | ChatGPT |
| 16 | DH-162 | Changelog nézet (long tap) | Belső/technikai feature, minimális KPI hatás | ChatGPT |
| 17 | DH-48/49/50 | Térkép + SMS + Route kalkulátor | Teljes csomag korai — falusi MVP-hez nem kell | Mindkettő |

#### TIER 4 — Explicit NEM KELL pilot fázisban

| Feature | Miért nem | Forrás |
|---------|-----------|--------|
| Natív mobil app (most) | PWA/mobile web first — native csak ha repeat usage erős | Perplexity |
| NPS rendszer | Nincs infra, nincs elég user | Korábbi döntés |
| Email drip sorozatok | "Nem spammelünk" — bolt + személyes ajánlás az elsődleges | Szabolcs döntése |

---

## Key Insights

### ChatGPT (Strategist)

1. **"Nem feature backlogot optimalizálunk, hanem pilot döntési rendszert"** — minden feature-t a pilot KPI-n mérd: hoz-e 1st ordert, 2nd ordert, vagy csökkent-e bizalmi akadályt?

2. **Falusi modell = új validációs hipotézis, nem sima backlog feature.** Erősebb lehet mint a városi convenience modell, mert hiányt tölt be (access vs convenience). De fegyelmezetten kell bevezetni: 1 település, 1 nap, 1 cutoff.

3. **Top 5 feature a 2nd Order Rate-re:** (1) DH-148 Reorder Quick Panel, (2) DH-173 Termék testreszabás, (3) DH-127 Familiar Favourites, (4) Falusi route pilot, (5) DH-161 kapacitáslimit.

4. **Sprint 4 javasolt scope:** DH-174 befejezése + DH-173 szűk MVP + DH-148 Reorder + falusi route MVP + DH-161 kapacitáslimit. Jogi/app store blockerek csak ha mobil app is Sprint 4 cél.

5. **Végső stratégiai mondat:** "Most ne a platform gazdagságát növeljétek, hanem a második rendelés valószínűségét. Ehhez három pontos mechanika kell: «ismerem, hogyan szereted», «egy kattintással újrarendelheted», és «oda is elvisszük, ahol nincs alternatíva»."

### Perplexity (Researcher)

1. **Framework:** MoSCoW a legjobb pre-revenue <50 user pilotnál. RICE gyenge mert nincs adat. Kano second-pass lensnek jó.

2. **MVP scope:** Kutatás szerint 5-8 core capability az ideális, nem 18 párhuzamos feature. Csak az end-to-end order loop-hoz szükséges funkciók kellenek.

3. **Repeat ordering evidence:** Egy food-app redesign 30%-kal növelte a repeat ordereket pusztán azzal, hogy egyszerűsítette a reorder UX-et. → DH-148 validáció.

4. **Savings/loyalty:** Akkor működik, ha valós reward loop-hoz kötött (free delivery threshold, loyalty points), nem standalone vanity stat.

5. **Native vs PWA:** PWA/mobile web first, native csak amikor a repeat usage erős és push re-engagement fontos. → Natív app NEM Sprint 4.

6. **Rural expansion:** Kutatás szerint csak operational maturity után érdemes terjeszkedni. Romániában a lokális élelmiszer-vállalkozások jellemzően egyszerű közvetlen rendelésekkel kezdenek (social media, ajtóhoz szállítás).

7. **Prioritási sorrend (Perplexity):** Admin tools + legal compliance → Favorites/reorder → Product customization (top SKUs) → Mobile/PWA → Rural expansion → Native app → Savings display → Seasonal pages.

---

## Decisions Made

| ID | Döntés | Dátum | Döntötte |
|----|--------|-------|----------|
| D-1 | Sprint 4 fő fókusz: Reorder Quick Panel + Termék testreszabás MVP + Falusi route pilot MVP | 2026-05-01 | Think Engine szintézis (Szabolcs jóváhagyásra vár) |
| D-2 | Framework: MoSCoW prioritizálás, nem RICE (nincs adat) | 2026-05-01 | Perplexity kutatás |
| D-3 | Natív app NEM Sprint 4 — PWA/mobile web first | 2026-05-01 | Mindkét AI + Perplexity kutatás |
| D-4 | Falusi modell = külön validációs hipotézis, minimál MVP-vel tesztelni Sprint 4-ben | 2026-05-01 | ChatGPT stratégia |
| D-5 | Seasonal content, changelog, swap suggestion → Backlog (nem Sprint 4) | 2026-05-01 | Mindkét AI |

---

## Open Questions

- [ ] Szabolcs jóváhagyása a Sprint 4 scope-ra (D-1)
- [ ] Mobil app Sprint 4 cél-e? (Ha igen → DH-134, DH-135 MUST. Ha nem → SHOULD later.)
- [ ] Melyik legyen az első falusi pilot település? (ChatGPT javaslata: 1 település, csütörtök délután, szerda 20:00 cutoff)
- [ ] DH-173 termék testreszabás scope: melyik top 5 SKU kapja először? Milyen opciók (vastagság, méret, pácolás)?
- [ ] Shared Basket (DH-149): manuális MVP-vel tesztelhető-e hamarabb? (ChatGPT szerint stratégiailag erős, de operációsan komplex)

---

## Context References

- `01_PROJECT_STATE.md` — aktuális sprint státusz
- `Business Development/pilot-husuzlet/BMC-v2.2.md` — business model
- `brainstorm/brainstorm_falusi-hazhozszallitas.md` — falusi delivery modell részletes elemzés
- `brainstorm/brainstorm_deak-pricing-revenue-share.md` — platformdíj modell
- `Business Development/pilot-husuzlet/founding50-spec-v1.0.md` — early adopter program

---

## Raw Notes

### 2026-05-01 — Think Engine Session

**Cél:** 17 meglévő Jira feature + 1 új (falusi házhozszállítás) optimális prioritási sorrendjének meghatározása.

**ChatGPT összefoglaló:** 18 feature-t egyenként elemzett a pilot KPI-k szemszögéből (30 reg / 15 order / 5 visszatérő). Javasolt Sprint 4 scope: DH-174 + DH-173 + DH-148 + falusi route MVP + DH-161. Sprint 5: Familiar Favourites, delivery zone, route kalkulátor, kedvenc termékek, shared basket.

**Perplexity összefoglaló:** Kutatás-alapú prioritás: admin/legal first, aztán repeat ordering (favorites/reorder), aztán customization top SKU-kra, aztán mobile/PWA, aztán rural expansion. 45 forrást használt. Fő insight: MoSCoW framework, 5-8 core capability MVP, PWA before native, reorder UX 30% repeat increase.

**Konszenzus pontok:**
- Reorder/repeat ordering a #1 prioritás
- Termék testreszabás fontos de szűk scope-pal
- Natív app NEM most
- Seasonal/changelog/swap → later
- Rural expansion: érdemes tesztelni de kontrolláltan

**Eltérés:**
- ChatGPT agresszívebb a falusi pilot MVP Sprint 4-be helyezésével
- Perplexity óvatosabb: "rural expansion after ops stabilize"
- Szintézis: minimál falusi MVP (1 település, fix nap) Sprint 4-ben, teljesebb rendszer Sprint 5-ben
