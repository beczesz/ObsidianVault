---
topic: DH Feature Prioritization v2 — Weighted Scoring
created: 2026-05-02
last_updated: 2026-05-02
status: active
parent: brainstorm_dh-feature-prioritization.md
id: 8daf3992-688e-4750-a0a3-e9c8e2a4d75d
index_schema_version: 1
---

# DH Feature Prioritization v2 — Súlyozott Rangsor

## Alapelv

> **"Most nem a platform gazdagságát kell növelni, hanem a második rendelés valószínűségét."**

Pilot cél: 30 regisztráció, 15 rendelés, 5 visszatérő vásárló 30 napon belül.
North Star KPI: Second Order Rate 14 napon belül (cél: ≥40%).

## Pontozási módszertan

Minden feature 1-10 skálán, egyetlen dimenzió: **mennyire növeli közvetlenül a 2nd order valószínűségét a pilot 3 hónapjában?**

Súlyozási szempontok (beépítve az 1-10 értékbe):
- Közvetlen hatás a visszatérő vásárlásra (50%)
- Bizalmi akadály csökkentés (20%)
- Operációs stabilitás (15%)
- Effort vs. impact arány (15%)

---

## Súlyozott Rangsor (1-22)

### #1 — DH-148: Reorder Quick Panel ("Utolsó rendelésed") — **10/10**

**Jira:** DH-148 (technikai alap: DH-120 Reorder Basket Loader)

A legközvetlenebb retention mechanizmus. Egy gomb, ami betölti az előző rendelés kosarát. Kutatás szerint egy food-app redesign 30%-kal növelte a repeat ordereket pusztán a reorder UX egyszerűsítésével. Ez a feature a North Star KPI (2nd Order Rate >=40%) egyetlen legfontosabb drivere. Ha a vásárló 2 kattintással újra tudja rendelni, amit múltkor rendelt, drasztikusan csökken a döntési frikció.

### #2 — DH-174: Admin ár-korrekció befejezése — **9/10**

**Jira:** DH-174 (In Progress)

Már elkezdett munka, blocker jellegű. A mészáros napi szinten módosítja az árakat a beszerzés függvényében — ha ezt nem tudja gyorsan csinálni, az operáció szétesik. Ha az admin oldal nem működik gördülékenyen, a fulfillment sem fog, és nem lesz 2nd order. Alacsony maradék effort, magas impact.

### #3 — DH-183: Terméktípusok modellezése (weight/piece/hybrid) — **9/10**

**Jira:** DH-183 (In Progress)

Jelenleg a termékek nem kezelik jól a súly-alapú vs. darab-alapú vs. vegyes árazást. Ez közvetlen bizalmi akadály: ha a vásárló nem érti, mennyit fog fizetni 1 kg csirkemellért vs. 1 db kolbászért, nem rendel újra. A pontos árazási modell a "kiszámíthatóság" érzését adja — ami a visszatérés feltétele.

### #4 — DH-173: Termék testreszabás és preferencia mentés — **9/10**

**Jira:** DH-173 (To Do)

Szűk MVP: top 5 SKU-ra (pl. vastagság, méret, pácolás). A "ismer engem" érzés a legerősebb retention driver az élelmiszer-e-commerceben. Ha a rendszer megjegyzi, hogy mindig 1 cm-es szeletelt szalonnát kérek, nem a boltba megyek legközelebb — hanem ide rendelek. Customization reduces offline clarification, különösen értékes húsüzletnél.

### #5 — DH-161: Timeslot kapacitás-limit — **8/10**

**Jira:** DH-161 (To Do)

Operációs védőkorlát. Ha egy időablakra 20 rendelés jön és a mészáros csak 8-at tud kiszolgálni, a fulfillment szétzuhan. A szétesett kiszolgálás = nem lesz 2nd order. Különösen kritikus a falusi route esetén (fix nap, korlátozott kapacitás). Alacsony effort, magas védelmi érték.

### #6 — DH-181: Analytics cleanup v2.2 — **8/10**

**Jira:** DH-181 (To Do)

4 FIX + 4 ellenőrzés + 8 új event. Nem customer-facing, de nélküle vakon repülünk: nem tudjuk mérni, hol veszítjük el a vásárlókat a 2nd order útján. A pilot 3 hónapjában az adatvezérelt döntéshozás a különbség a sikeres iteráció és a találgatás között.

### #7 — NEW: Falusi Route Pilot MVP — **8/10**

**Jira:** DH-184 (To Do)

1 település, fix nap (pl. csütörtök), szerda 20:00 cutoff, settlement picker a checkout-ban, route banner a főoldalon. Ez NEM a platform gazdagítása — ez egy új validációs hipotézis. Falvakban nincs friss hús: ez elérhetőségi probléma, nem kényelmi. A falusi vásárló motivációja sokkal erősebb, mint a városié. Numerikus modell szerint 15 rendelés/route = 12-14 RON/kiszállítás, breakeven 10 rendelés. Az első mockup már létezik.

### #8 — DH-127: Familiar Favourites ("Szokásos rendelésem") — **7/10**

**Jira:** DH-127 (To Do)

A Reorder Quick Panel (#1) következő szintje: nem az utolsó rendelést tölti be, hanem a rendszeres vásárlási mintázatot. Ez a L3 Habit Engine része — de csak akkor van értelme, ha már van elég vásárlási adat (min. 3-4 rendelés/user). Sprint 5-ben reális.

### #9 — DH-176: Ikonok és szövegek vertikális igazítása — **7/10**

**Jira:** DH-176 (To Do)

Apró UX polish, de a vizuális minőség közvetlenül hat a bizalomra. Minimális effort, észrevehető impact a "profi" érzetre. Gyors win.

### #10 — DH-145: Firebase + GDPR cookie consent banner — **7/10**

**Jira:** DH-145 (To Do)

Kettős funkció: (1) GDPR compliance — jogi minimum a beta-hoz; (2) Firebase Analytics helyes consent-alapú működése. Beta előtt MUST.

### #11 — NEW: Natív mobil app fejlesztés — **5/10**

**Jira:** Nincs (új feature kandidátum)

iOS + Android natív app (vagy Capacitor wrapper). PWA/mobile web first, native csak ha a repeat usage erős és push re-engagement fontos. Jelenleg nincs elég user adat. Sprint 4 végén / Sprint 5 elején reális, ha a pilot adatok pozitívak. DH-134 + DH-135 blokkolók.

### #12 — DH-51: Szállítási zóna korlátozás (10 km) — **5/10**

**Jira:** DH-51 (To Do)

Fontos operációs korlát — de a jelenlegi pilot méretben (30 user, Újvárhely) nem kritikus. A falusi route pilot szükségessé teszi Sprint 5-ben.

### #13 — DH-139: Rendelésszám egyszerűsítés (DH-0001) — **5/10**

**Jira:** DH-139 (To Do)

Support és bizalmi feature. Alacsony effort, de nem retention driver. "Polish" kategória.

### #14 — DH-146: Kedvenc Termékek (csillag toggle) — **5/10**

**Jira:** DH-146 (To Do)

Hasznos, de alacsonyabb prioritás mint az order-level reorder. A csillag toggle egyéni termékekre vonatkozik — a teljes kosár szintű reorder erősebb retention mechanizmus.

### #15 — DH-165: Admin platformdíj kalkulátor — **4/10**

**Jira:** DH-165 (To Do)

Üzletileg hasznos, de nem customer-facing, nem húzza a pilot KPI-t.

### #16 — DH-167: QR kód kassza szalagra — **4/10**

**Jira:** DH-167 (To Do)

Founding 50 toborzási eszköz. Fontos a regisztrációs célhoz, de nem retention feature.

### #17 — DH-134 + DH-135: Privacy Policy + App Store account — **4/10**

**Jira:** DH-134, DH-135 (To Do)

v0.4 mobil app blokkolók. PWA first konszenzus: Sprint 5-re tolhatók.

### #18 — DH-149: Shared Basket (Group Order) — **3/10**

**Jira:** DH-149 (To Do)

Stratégiailag erős, de operációsan komplex. Nem 30 usernél van értelme, hanem 200+-nál.

### #19 — DH-128: Swap suggestion MVP — **3/10**

**Jira:** DH-128 (To Do)

Korai — a user még nem bízik eléggé az online húsvásárlásban ahhoz, hogy elfogadjon helyettesítést.

### #20 — DH-163: Szezonális cikk oldal (Grillszezon) — **2/10**

**Jira:** DH-163 (To Do)

Marketing content. 30 usernél a személyes ajánlás erősebb.

### #21 — DH-162: Changelog nézet (long tap) — **2/10**

**Jira:** DH-162 (To Do)

Belső/technikai feature. Minimális KPI hatás.

### #22 — DH-48/49/50: Térkép + SMS + Route kalkulátor — **2/10**

**Jira:** DH-48, DH-49, DH-50 (To Do)

Teljes delivery tech stack. A falusi route MVP-hez nem kell. Sprint 6+ features.

---

## Sprint Allocation — Javasolt

### Sprint 4 MUST (közvetlen 2nd order hatás)
| # | Feature | Score |
|---|---------|-------|
| 1 | DH-148/120: Reorder Quick Panel | 10 |
| 2 | DH-174: Admin ár-korrekció (befejezés) | 9 |
| 3 | DH-183: Terméktípusok modellezése | 9 |
| 4 | DH-173: Termék testreszabás (szűk MVP) | 9 |
| 5 | DH-161: Timeslot kapacitás-limit | 8 |
| 6 | DH-181: Analytics cleanup v2.2 | 8 |
| 7 | DH-184: Falusi Route Pilot MVP | 8 |
| 8 | DH-176: Ikonok vertikális igazítás | 7 |
| 9 | DH-145: Firebase + GDPR consent | 7 |

### Sprint 5 SHOULD (retention + expansion)
| # | Feature | Score |
|---|---------|-------|
| 10 | DH-127: Familiar Favourites | 7 |
| 11 | Natív mobil app | 5 |
| 12 | DH-51: Szállítási zóna | 5 |
| 13 | DH-139: Rendelésszám egyszerűsítés | 5 |
| 14 | DH-146: Kedvenc Termékek | 5 |

### Backlog / Later
| # | Feature | Score |
|---|---------|-------|
| 15 | DH-165: Admin platformdíj kalkulátor | 4 |
| 16 | DH-167: QR kassza szalag | 4 |
| 17 | DH-134/135: Privacy + App Store | 4 |
| 18 | DH-149: Shared Basket | 3 |
| 19 | DH-128: Swap suggestion | 3 |
| 20 | DH-163: Szezonális oldal | 2 |
| 21 | DH-162: Changelog | 2 |
| 22 | DH-48/49/50: Térkép+SMS+Route | 2 |

---

## Validációs státusz

- [x] Think Engine validáció (ChatGPT + Perplexity) — 2026-05-02 ✅
- [ ] Szabolcs jóváhagyás
---

## Think Engine Validáció (2026-05-02)

### Team
| AI | Role | URL |
|----|------|-----|
| ChatGPT (Deák GPT) | Strategist | https://chatgpt.com/g/g-p-69cbee4a04c481918a2a738959b92361-deak/c/69da0a38-ce68-8391-bfb4-a2bbf24a66e7 |
| Perplexity | Researcher | https://www.perplexity.ai/search/5072f1ac-b046-4906-9dd9-1f6af86b967b |

### ChatGPT (Strategist) — Validációs eredmény

**Top 7 sorrend:** Alapvetően jó, de egy módosítás: **Analytics cleanup (#6) legyen #4** — a mérés nem "support feature", hanem döntési infrastruktúra. Ha rosszul mértek, rossz döntést hoztok.

**ChatGPT javasolt sorrend:**
1. Reorder Quick Panel (10)
2. Admin ár-korrekció (9)
3. Terméktípusok weight/piece/hybrid (9)
4. **Analytics cleanup (8 → felfelé)** — döntési infra
5. Top 5 SKU testreszabás (9 → lefelé)
6. Timeslot limit (8)
7. Falusi route MVP (8)

**9 feature Sprint 4-ben:** TÚL SOK. Valódi core scope = 5-6 feature. Minimum viable Sprint 4: Reorder Quick Panel + Admin ár-korrekció + terméktípusok + Analytics cleanup + top 5 SKU testreszabás. Ha belefér: Timeslot limit. Falusi route MVP akkor ha külön mini-pilotként, nagyon szűk scope-pal. Ikon fix és GDPR consent csak ha blocker vagy nagyon alacsony effort.

**Natív app 5/10:** Helyes, sőt akár 4/10. Pilotfázisban a fő akadály nem az app ikon hiánya, hanem a trust gap. Natív app akkor lesz fontos, amikor van visszatérő vásárlási minta.

**Falusi route MVP 8/10:** Helyes, de csak ha MVP marad. 1 route, 1 nap, 1 cutoff, 1 településlista, 1 egyszerű checkout kommunikáció. Ennyi.

**Shared basket + Swap:** Backlogba tétele helyes. Túl korai.

**Familiar Favourites:** Sprint 5 OK, de szorosan összekötné a Reorder Quick Panel adataival. Ne építsetek külön "kedvencek" világot.

**Végső javaslat:** Sprint 4 = "Pilot Validation Infrastructure Sprint". Újrarendelés, termékmodell, ár kezelés, mérés, top SKU kontrollopciók, majd ha belefér kapacitáslimit és falusi route MVP.

### Perplexity (Researcher) — Kutatási validáció

**1. Reorder UX = #1 driver?** IGEN. Baymard 2025-2026: cart abandonment 70.22%. Repeat-friendly checkout flow (one-tap reorder, saved basket) közvetlenül támogatja a 2nd order-t 14 napon belül. Sourced: ijirt, econsultancy, chainstoreage.

**2. Natív app BEFORE vagy AFTER web retention?** AFTER. PWA/mobile web first, native csak ha repeat usage erős. A fő akadály nem az app ikon — hanem trust, termékvariabilitás, kontrollvesztés érzése. Sourced: multiple e-commerce studies.

**3. Rural expansion timing:** Óvatosan, de érdemes tesztelni. Falvakban az access > convenience — erősebb motiváció. De csak minimál MVP-vel: settlement picker + fix nap + cutoff. Sourced: European food delivery case studies.

**4. Product customization:** IGEN, növeli a repeat-et. Specialty food e-commerce-ben a preference saving csökkenti a döntési frikcióba. Sourced: norbr, ceo-review.

**5. 9 feature túl sok?** IGEN. Kutatás szerint 5-8 core capability az ideális MVP-hez. Sprint 4-ben 5-6 feature a reális scope.

**Perplexity javasolt MVP prioritás:**
1. Transparent total cost + delivery timing (már van)
2. Guest/low-friction checkout (már van)
3. COD + simple card payment (COD van, card v0.5)
4. One-tap reorder / favorites
5. Immediate order confirmation + next steps
6. Payment clarity + delivery zone display

### Szintézis — Konszenzus pontok

| Kérdés | ChatGPT | Perplexity | Konszenzus |
|--------|---------|------------|-----------|
| Top 7 sorrend | Analytics cleanup feljebb (#4) | Reorder + trust features first | **Analytics = #4, Testreszabás = #5** |
| 9 feature Sprint 4 | Túl sok, 5-6 legyen | 5-8 core capability | **Core scope: 5-6 feature + 1-2 ha belefér** |
| Natív app | 5/10 helyes, akár 4/10 | AFTER web retention | **4-5/10, Sprint 5 leghamarabb** |
| Falusi route | 8/10 OK, de szűk MVP | Óvatosan, minimál MVP | **8/10, de NE nyerje el a Sprint 4 fókuszát** |
| Shared basket | Túl korai | N/A (not researched) | **Backlog (3/10)** |

### Adjustált végső sorrend (Think Engine validáció után)

| # | Feature | Score | Változás |
|---|---------|-------|----------|
| 1 | Reorder Quick Panel | 10 | — |
| 2 | Admin ár-korrekció DH-174 | 9 | — |
| 3 | Terméktípusok DH-183 | 9 | — |
| 4 | Analytics cleanup DH-181 | 8→9 | **FEL** (ChatGPT: döntési infra) |
| 5 | Termék testreszabás DH-173 | 9→8 | **LE** (analytics előbbre) |
| 6 | Timeslot limit DH-161 | 8 | — |
| 7 | Falusi Route MVP DH-184 | 8 | — (de szűk scope!) |
| 8 | Firebase GDPR DH-145 | 7 | FEL (Ikon fix fölé) |
| 9 | Ikon igazítás DH-176 | 7 | LE |
| 10 | Familiar Favourites DH-127 | 7 | — |
| 11 | Natív mobil app | 4-5 | **LE** (konszenzus: 4/10) |
| 12-22 | Változatlan | 2-5 | — |

### Sprint 4 — Adjustált core scope (5-6 + 1-2)

**Core (MUST):**
1. Reorder Quick Panel (10)
2. Admin ár-korrekció DH-174 (9)
3. Terméktípusok DH-183 (9)
4. Analytics cleanup DH-181 (9)
5. Termék testreszabás DH-173 (8)

**Ha belefér (SHOULD):**
6. Timeslot limit DH-161 (8)
7. Falusi Route MVP DH-184 (8) — de csak ha mini-pilot scope

**Quick wins (alacsony effort, bármikor):**
- Ikon igazítás DH-176 (7)
- Firebase GDPR DH-145 (7) — beta blocker, MUST ha beta elindul

