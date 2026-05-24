---
title: "DH Savings Engine — Ötletgyűjtemény és Tervezés"
version: 1.3
date: 2026-04-02
author: Becze Szabolcs + Claude (Anthropic) + ChatGPT + Perplexity
description: >
  A DH spórolás motor teljes ötletgyűjteménye. A cél: az okos vásárlás
  élményét logikai játékká tenni — minél ügyesebb a vásárló, annál többet spórol.
  Referencia-ár: a Deák Húsmíves saját bolti ára (NEM más boltok).
status: validálva — 65 ötlet pontozva, 4 hetes implementációs terv kész
sources: >
  Szabolcs eredeti ötletei (10 db) + Claude web research (Picnic, ButcherBox, Ibotta,
  Pinduoduo, Misfits Market, Farmison, Riverford, behavioral economics kutatás,
  ecommerce gamification 2025-2026 trendek) + DH competitors_analysis v3.1 +
  dhop-siker-otlettar v4.0
id: ae74972d-e100-4aed-b7b4-7bd0b6381ad2
index_schema_version: 1
---

# DH Savings Engine — "Okosan vásárolsz, többet spórolsz"

> **Alapelv:** Az okos vásárlás egy logikai játék. Aki ügyesen játszik, nyer.
> Minél több szabályt ismer és alkalmaz a vásárló, annál többet spórol.
> A referencia-ár a Deák Húsmíves saját bolti ára — nem más boltokkal versenyezünk, hanem saját magunkkal.

---

## ÁRAZÁSI ALAPTÁBLA

| Paraméter | Érték | Megjegyzés |
|-----------|-------|------------|
| Minimum kosárérték | 80 RON | Alatta nem lehet rendelni |
| Ingyenes szállítás küszöb | 150 RON | Alatta ~10 RON szállítási díj |
| Volumen kedvezmény 1 | 300 RON felett → 2% | TODO: pontos árrés kalkuláció |
| Volumen kedvezmény 2 | 600 RON felett → 5% | TODO: pontos árrés kalkuláció |
| Szállítási díj | ~10 RON | TODO: véglegesítés |

---

## AZ 60 ÖTLET — 9 KATEGÓRIÁBAN

### A. THRESHOLD & NUDGE MECHANIKÁK (8 ötlet)

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| A1 | **Running savings counter** | Kosárban real-time: "Eddig X lejt spóroltál a bolti árhoz képest" — minden hozzáadott terméknél frissül | Picnic, Szabolcs | AOV ↑, Conversion ↑ | v0.3 |
| A2 | **Ingyenes szállítás threshold nudge** | "Még X lej és ingyenes szállítás (spórolsz 10 lejt)" — persistent banner a kosárban | Farmison, Picnic | AOV ↑ | v0.3 |
| A3 | **Volumen kedvezmény nudge** | "Még X lej a 300-as küszöbig → 2% kedvezmény az egész kosárra" — progress bar | Szabolcs, Pinduoduo | AOV ↑ | v0.3 |
| A4 | **Multi-threshold progress bar** | Vizuális sáv 3 mérföldkővel: 80 (min) → 150 (free delivery) → 300 (2%) → 600 (5%) | Gamification research | AOV ↑, Engagement ↑ | v0.3 |
| A5 | **"Okos ajánlás" a küszöbhöz** | Ha 130 RON-nál jár → a rendszer ajánl 1-2 terméket ami átlendíti 150 fölé, savings-sel megmutatva | Picnic "add 1 more" | AOV ↑ | v0.3 |
| A6 | **Szállítási díj savings counter** | Ha 150+ RON → "10 lejt spóroltál a szállításon" bekerül a savings történetbe | Szabolcs | Retention ↑ | v0.3 |
| A7 | **"Majdnem ott vagy" exit-intent nudge** | Ha a user el akarja hagyni a kosarat küszöb közelében → "Még csak X lej és spórolsz Y-t!" | Ecommerce gamification | Conversion ↑ | v0.4 |
| A8 | **Post-order savings recap** | Rendelés visszaigazolás + email: "Ezzel a rendeléssel X lejt spóroltál. Idén összesen: Y lej." | Picnic, Misfits | Retention ↑ | v0.3 |

### B. BUNDLE & CSOMAG SAVINGS (7 ötlet)

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| B1 | **Családi heti csomag (2/4/6 fős)** | Előre összeállított heti húscsomag háztartás-mérethez, %-os kedvezménnyel a darabos árhoz képest | ButcherBox, Porter Road, Szabolcs | AOV ↑, Conversion ↑ | v0.3 |
| B2 | **"Próbacsomag" első rendeléshez** | 5 termékes kóstolócsomag kedvezményes áron — az első rendelés default ajánlata | Ötlettár #3 | TTFO ↓, Acquisition ↑ | v0.3 |
| B3 | **Szezonális csomag** | Grillszezon, karácsony, húsvét — tematikus csomagok időszakos kedvezménnyel | Porter Road, Ötlettár | AOV ↑ | v0.4 |
| B4 | **"Heti menü" csomag** | Recepthez kötött csomag: "Vasárnapi ebéd csomag" (2 adag sült + mellékek) → hentes összeállítja | Freshful recept-kosár | AOV ↑, Differenciáció ↑ | v0.4 |
| B5 | **Bundle builder** | "Állítsd össze a saját csomagodat 5 termékből → X% kedvezmény" — a vásárló maga rakja össze | Crowd Cow custom box | Engagement ↑, AOV ↑ | v0.4 |
| B6 | **Akciós termékek** | Időszakos %-os kedvezmény kiválasztott termékekre — admin felületen állítható, készlet/szezon alapú | Szabolcs | Conversion ↑ | v0.3 |
| B7 | **"Teljes állat" előrendelés** | 10-15 család közösen előrendel egy egész sertést → max kedvezmény, zero waste | Crowdbutching/Grutto | Community ↑, AOV ↑↑ | v0.5+ |

### C. SOCIAL & KÖZÖSSÉGI SAVINGS (8 ötlet)

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| C1 | **Megosztott kosár (Group Order)** | Több család összefog → közös kosár → 600 RON-os küszöb közösen elérhető → 5% mindenkinek. Külön csomagolás. | Szabolcs, Pinduoduo | AOV ↑↑, Virális ↑ | v0.3-v0.4 |
| C2 | **Referral program** | Meghívó kap X RON kedvezményt, meghívott is kap Y RON-t az első rendelésére | Szabolcs, ButcherBox ($30/$30) | Acquisition ↑ | v0.3 |
| C3 | **Szomszéd-meghívó / Tömbház unlock** | "Ha 3 szomszédod is regisztrál → mindannyian kaptok Z RON-t" — lakótelep-szintű virális terjedés | Ötlettár #1.2, #1.5 | Acquisition ↑↑ | v0.4 |
| C4 | **Pinduoduo-stílusú "csapatos vásárlás"** | "Még 2 ember kell a 600 RON-os küszöbhöz → oszd meg a linket!" — 24 órás ablak | Pinduoduo FOMO algebra | AOV ↑, Virális ↑ | v0.4 |
| C5 | **Munkahelyi csomagajánlat** | Iroda/cég közösen rendel → nagyobb volumen → jobb kedvezmény. Heti rutin a munkahelyen. | Ötlettár #1.4 | AOV ↑, B2B ↑ | v0.4 |
| C6 | **"Ajánlom" social proof** | "Kata 4 családja már 3x rendelt" — anonim social proof a termékoldalakon | Behavioral economics | Trust ↑ | v0.4 |
| C7 | **Közösségi savings dashboard** | "A székelyudvarhelyi vásárlók összesen X lejt spóroltak" — város-szintű counter | Misfits environmental dashboard | Community ↑, PR ↑ | v0.5 |
| C8 | **Családi "savings verseny"** | Két család összehasonlíthatja a spórolási statisztikáját — gamifikált közösségi elem | Gamification research | Engagement ↑, Retention ↑ | v0.5 |

### D. LOYALTY & JUTALOM RENDSZER (8 ötlet)

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| D1 | **Forgalmi bónusz utalvány** | 5.000 RON → 100 RON / 10.000 → 150 RON / 20.000 → 300 RON bónusz utalvány | Szabolcs | Retention ↑↑ | v0.4 |
| D2 | **Köztes mérföldkövek** | 500 RON → 10 RON / 1.000 RON → 25 RON / 2.500 RON → 50 RON — hogy az első hónapokban is érezze | Claude javaslat | Retention ↑ | v0.3-v0.4 |
| D3 | **"Sizzle" pontrendszer** | Minden 1 RON = 1 pont. 500 pont = 10 RON kedvezmény. Egyszerű, átlátható. | ButcherBox Sizzle Society | Retention ↑ | v0.4 |
| D4 | **Heti rendelési streak** | 3 egymást követő heti rendelés → bónusz (pl. ingyenes szállítás a 4. rendelésre) | Ibotta streak, Gamification | Frequency ↑ | v0.4 |
| D5 | **"10. rendelés = 10% kedvezmény"** | Egyszerű, megjegyezhető szabály. Minden 10. rendelés extra kedvezményes. | Ötlettár | Retention ↑ | v0.4 |
| D6 | **Születésnapi bónusz** | Születésnapon X RON kedvezmény vagy ajándék termék a rendeléshez | Edenmoor/Pipers Farm | Emotional loyalty ↑ | v0.5 |
| D7 | **Review-írásért jutalom** | Termék értékelés = 5 pont / rendelés értékelés = 10 pont → social proof + engagement | Edenmoor, Ibotta | Trust ↑, Content ↑ | v0.5 |
| D8 | **"VIP vásárló" státusz** | 20+ rendelés vagy 10.000+ RON → VIP: elsőbbségi szállítás, exkluzív csomagok, extra kedvezmények | Tiered loyalty psychology | Retention ↑↑, Status ↑ | v0.5 |

### E. SMART BASKET & REORDER (7 ötlet)

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| E1 | **1-click reorder** | Előző rendelés betölt → módosítható → savings azonnal látszik | Misfits Market, Ötlettár #4 | 2nd Order ↑, TTFO ↓ | v0.3 |
| E2 | **"Szokásos rendelésem" gomb** | Familiar Favourites — a rendszer megjegyzi a kedvenc kosarat, egy gombbal betölthető | Riverford | 2nd Order ↑ | v0.3 |
| E3 | **Kosár-optimalizáló javaslat** | "Ha kicseréled az X-et Y-ra, 8 lejjel többet spórolsz ugyanannyi húsért" — swap ajánlás | Misfits AI grocer | AOV ↑, Savings ↑ | v0.4 |
| E4 | **Heti ajánlott kosár (pre-fill)** | Rendszer előre összeállítja a heti kosarat korábbi rendelések + szezon + akciók alapján | Misfits pre-filled cart | Retention ↑, Convenience ↑ | v0.4 |
| E5 | **"Hány fős a háztartásod?" onboarding** | Regisztrációkor → háztartás méret → default ajánlott csomag → azonnal relevancia | Porter Road household-fit | TTFO ↓, Conversion ↑ | v0.3 |
| E6 | **Auto-order (opt-in)** | Ha a user nem módosít → az ajánlott kosár automatikusan leadódik a szokásos napon | Misfits auto-order window | Retention ↑↑ | v0.5 |
| E7 | **Termékalapú reorder trigger email** | Hús (3-4 nap), kolbász (5-7 nap), szalámi (10-14 nap) → időzített email: "Ideje újrarendelni?" | Ötlettár #6 | 2nd Order ↑ | v0.3 |

### F. SAVINGS TRACKING & VIZUALIZÁCIÓ (6 ötlet)

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| F1 | **Savings history dashboard** | Profil oldal: minden rendelés savings-e, forrás szerinti bontás, kumulált összeg, havi/éves trend | Picnic, Misfits, Szabolcs | Retention ↑↑ | v0.3-v0.4 |
| F2 | **"Ennyit spóroltál idén" éves összesítő** | December végén / évfordulón: teljes éves savings riport email-ben | Misfits environmental dashboard | Emotional retention ↑ | v0.5 |
| F3 | **Savings forrás bontás** | Szállítás spórolás / Volumen kedvezmény / Bundle savings / Akciós / Bónusz — külön-külön látható | Szabolcs | Transparency ↑ | v0.4 |
| F4 | **Progress bar a következő mérföldkőig** | "Még X RON a következő bónusz utalványig" — vizuális haladás | Zeigarnik effect, Goal gradient | Motivation ↑ | v0.4 |
| F5 | **Havi savings email összesítő** | Havonta 1 email: "Ebben a hónapban X lejt spóroltál, Y rendelésből" | Picnic post-order | Retention ↑ | v0.4 |
| F6 | **Savings leaderboard (opt-in)** | Anonim rangsor: "Te a TOP 15%-ban vagy a spórolásban" — státusz-pszichológia | Gamification tiered status | Engagement ↑ | v0.5 |

### G. ÁRAZÁS & DINAMIKUS KEDVEZMÉNYEK (6 ötlet)

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| G1 | **Bolti ár vs. online ár termékszintű** | Minden termékkártyán: bolti ár áthúzva + online ár + különbség ("Spórolsz: X lej") | Picnic "you save" label | Conversion ↑, Trust ↑ | v0.3 |
| G2 | **Volumen kedvezmény (tiered)** | 300+ RON → 2% / 600+ RON → 5% az egész kosárra | Szabolcs | AOV ↑ | v0.3 |
| G3 | **Pick-up from store kedvezmény** | Bolti átvétel → szállítási díj megtakarítás → savings-be számlálódik | Szabolcs | Ops. hatékonyság ↑ | v0.5 |
| G4 | **"Happy hour" időszakos kedvezmény** | Hétfő reggel 8-10: +2% extra kedvezmény → kereslet simítás, off-peak ösztönzés | Behavioral economics | Demand shaping ↑ | v0.5 |
| G5 | **Készlet-alapú dinamikus ár** | Ha egy termékből sok van → automatikus árcsökkentés → waste csökkentés + savings a vásárlónak | Supply-side optimization | Waste ↓, Savings ↑ | v0.5 |
| G6 | **"Egész tarja" kedvezmény** | Ha egész darabot vesz (nem felszeletelve) → kedvezményesebb, mert kevesebb munka a hentesnek | Supply-side logic | AOV ↑, Ops ↑ | v0.4 |

### H. ONBOARDING & ELSŐ RENDELÉS (5 ötlet)

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| H1 | **TTFO email drip** | Reg. után 24h/48h/72h emlékeztető email — fokozatosan erősödő incentive | Ötlettár #5 (push→email) | TTFO ↓ | v0.3 |
| H2 | **"Savings tutorial" első rendelésnél** | Mini onboarding: "Így spórolhatsz a legtöbbet" — 3 tipp megjelenítése az első checkout-nál | Nudge design research | Education ↑, AOV ↑ | v0.3 |
| H3 | **Referral kedvezmény az első rendelésre** | Meghívott kap X RON kedvezményt az első rendelésére — csökkenti a belépési küszöböt | Szabolcs, ButcherBox | Acquisition ↑ | v0.3 |
| H4 | **"Bolti asszisztált regisztráció" support** | QR + script a pultosnál: segít regisztrálni ÉS az első rendelést helyben leadni | Ötlettár #1, #2 | TTFO → 0 | v0.3 (ops) |
| H5 | **"Spórolási kihívás" első 3 rendelésre** | "Rendeld 3x 14 napon belül → X RON bónusz" — a szokás megalapozása | HelloFresh anti-pattern (de ok ha kicsi) | Retention ↑ | v0.4 |


### I. CHATGPT DEEP INSIGHTS — Kiegészítő ötletek (5 ötlet)

> **Forrás:** ChatGPT "Deák GPT" Savings Engine Koncepció beszélgetés (2026-04-02)
> **Meta-insight:** "Nem az a cél, hogy tényleg spóroljon a user — hanem hogy úgy érezze, hogy okos döntést hozott."

| # | Ötlet | Leírás | Forrás | KPI hatás | Fázis |
|---|-------|--------|--------|-----------|-------|
| I1 | **"Whole animal" savings** | Ha a kevésbé keresett részeket választja (pl. csülök, dagadó), olcsóbb — framing: "A hentes kedvence, mert okosan választottál" | ChatGPT whole animal logic | AOV mix ↑, Waste ↓ | v0.4 |
| I2 | **Waste reduction savings framing** | "Azzal hogy online rendeltél, nem pazaroltál — a Deák pontosan annyit készít elő amennyit rendeltél" — morális + pénzügyi savings | ChatGPT + Misfits environmental | Emotional loyalty ↑ | v0.4 |
| I3 | **Előrendelési kedvezmény (early bird)** | Ha vasárnap 20:00-ig leadja a hétfői rendelést → +1% kedvezmény — a hentes jobban tud tervezni | ChatGPT előrendelés | Demand smoothing ↑, Ops ↑ | v0.3 |
| I4 | **Margin guardrail rendszer** | Max discount cap: egy rendelés SOHA ne legyen nettó veszteséges. Backend szabály: ha a kombó-kedvezmény meghaladná az X%-ot, automatikusan csökkenti | ChatGPT | Profitability protection | v0.3 (backend) |
| I5 | **"Okos döntés" badge rendszer** | Minden "okos" cselekvésért (küszöb átlépés, csomag választás, early bird, group order) → badge a profilban — gamification réteg a savings fölött | ChatGPT behavior layer + Gamification research | Engagement ↑↑ | v0.4 |

### ChatGPT 3-komponensű keretrendszer (referencia)

A savings engine nem 1 feature, hanem 3 réteg:

1. **Calculation Layer** — Mi a baseline? Hogyan számolja a rendszer a savings-et? (Deák bolti ár = referencia)
2. **Communication Layer** — Hol és mikor jelenik meg? (termékkártya, kosár, checkout, post-order, email, profil)
3. **Behavior Layer** — Hogyan formálja a viselkedést? (threshold nudge, progress bar, badge, streak)

Ez a keret segít priorizálni: **először a Calculation Layer kell (v0.3), aztán Communication (v0.3), végül Behavior (v0.4+).**

---

## VALIDÁLT RANGSOR — 65 ÖTLET PONTOZVA (v1.2)

> **Validáció dátuma:** 2026-04-02
> **Módszertan:** 5 dimenzió súlyozva — KPI Impact (30%) + Megvalósíthatóság (25%) + Pilot Fit (25%) + Revenue Protection (10%) + Egyediség (10%)
> **Pontszám tartomány:** 4.65 (G5) → 8.75 (I4)

### TOP 10 — Ezeket építjük

| Rang | ID | Ötlet | Composite | Layer | Státusz |
|------|----|-------|-----------|-------|---------|
| 🥇 1 | I4 | Margin guardrail (max discount cap) | **8.75** | Calculation | 🔴 CRITICAL CONTROL |
| 🥇 2 | E1 | 1-click reorder | **8.55** | Behavior | ✅ READY |
| 🥇 3 | A1 | Running savings counter | **8.45** | Communication | ✅ READY |
| 🥇 4 | A3 | Volume discount nudge (→300/600) | **8.45** | Communication | ✅ READY |
| 🥇 5 | A2 | Free delivery threshold nudge | **8.40** | Communication | ✅ READY |
| 🥈 6 | G2 | Tiered volume discount (létezik) | **8.35** | Calculation | 🔄 REINFORCE |
| 🥈 7 | G1 | Bolti ár vs online ár termékkártyán | **8.35** | Communication | ✅ READY |
| 🥈 8 | E2 | "Szokásos rendelésem" gomb | **8.15** | Behavior | ✅ READY |
| 🥈 9 | A4 | Multi-threshold progress bar | **8.15** | Communication | ✅ READY |
| 🥈 10 | H1 | TTFO email drip (24/48/72h) | **8.05** | Communication | ✅ READY |

**Insight:** A TOP 10 erősen Communication-központú (savings megmutatása) + Behavior (újrarendelés). Nulla margin kockázat. 2-3 hét alatt megvalósítható.

### BOTTOM 10 — Ezeket NEM építjük a pilotban

| Rang | ID | Ötlet | Composite | Miért nem? |
|------|----|-------|-----------|-----------|
| 60 | G5 | Inventory-based dynamic pricing | **4.65** | Túl komplex (30 perc sync, real-time inventory) |
| 59 | G3 | Pick-up from store kedvezmény | **4.95** | Modell-ütközés (delivery-first DH) |
| 58 | D7 | Review reward (5-10 pont) | **5.00** | Alacsony engagement 30 usernél |
| 57 | G4 | Happy hour kedvezmény | **5.30** | Margin kockázat + ops complexity |
| 56 | E6 | Auto-order opt-in | **5.65** | OPS kockázat (visszatérítés automatizálás) |
| 55 | B7 | "Teljes állat" előrendelés | **5.70** | Ops complexity + koordináció |
| 54 | G6 | "Egész tarja" kedvezmény | **5.80** | Alacsony kereslet |
| 53 | I5 | Smart decision badge rendszer | **5.95** | Korai 30 usernél |
| 52 | D6 | Születésnapi bónusz | **5.95** | Privacy + alacsony ROI |
| 51 | C8 | Családi savings verseny | **6.00** | Mérethez kötött, erőltetett |

---

### 5 ÚJ ÖTLET — A validáció során azonosított hiányok

| # | Ötlet | Leírás | Composite | Layer | Fázis |
|---|-------|--------|-----------|-------|-------|
| J1 | **Streakable Cart State** | 5-7 naponta: "A szokásos kosarak készen áll" — nem auto-debit, csak gentle reminder + savings vs előző rendelés. E6 (auto-order) és E1 (reorder) közötti híd. | **8.25** | Behavior+Calc | v0.3 |
| J2 | **First-Order Margin Protection** | Hard cap az első rendelés kedvezményeire: standalone max 10 RON, referral max 8 RON, trial max 15 RON. Biztosítja hogy H3/H5/B2 nem okoz negatív LTV-t. | **8.15** | Calculation | v0.3 |
| J3 | **Repeat-Ability Score** | Dashboard: "2.3x gyakrabban rendelsz mint az átlagos vásárló" + előrejelzett következő rendelés dátum. A North Star személyes szokássá alakítása. | **7.65** | Comm+Behav | v0.4 |
| J4 | **Zero Delivery Fee Conditionals** | 150 RON fix küszöb helyett: INGYENES ha H-Sze 20-21h (off-peak) / 250+ RON / 14 napon belüli 2. rendelés. Margin-védett + viselkedés-formáló. | **7.90** | Calc+Behav | v0.4 |
| J5 | **Savings Companion Email** | Heti péntek 18:00 email: (1) savings recap, (2) szezonális ajánlat, (3) soft social proof, (4) csomag javaslat. Passzív dashboard (F1-F6) és agresszív drip közötti arany középút. | **7.85** | Communication | v0.3 |

---

### TELJES PONTOZÁS — Mind a 65 ötlet

| ID | Ötlet | KPI | Feas. | Pilot | RevP | Unique | **Comp.** | Layer | Kockázat | Javaslat |
|----|-------|-----|-------|-------|------|--------|-----------|-------|----------|----------|
| I4 | Margin guardrail | 9 | 7 | 10 | 10 | 8 | **8.75** | Calc | CRITICAL | v0.3 Week 1 |
| E1 | 1-click reorder | 8 | 9 | 10 | 8 | 6 | **8.55** | Behav | — | v0.3 Week 2 |
| A1 | Running savings counter | 8 | 9 | 10 | 7 | 6 | **8.45** | Comm | — | v0.3 Week 1 |
| A3 | Volume discount nudge | 8 | 9 | 10 | 8 | 5 | **8.45** | Comm | — | v0.3 Week 3 |
| A2 | Free delivery threshold nudge | 7 | 10 | 10 | 8 | 5 | **8.40** | Comm | — | v0.3 Week 2 |
| G2 | Tiered volume discount | 8 | 9 | 10 | 8 | 4 | **8.35** | Calc | EXISTING | Messaging erősítés |
| J1 | Streakable cart state | 8 | 8 | 10 | 8 | 7 | **8.25** | Hybrid | — | v0.3 Week 2 |
| G1 | Bolti ár vs online ár | 7 | 9 | 10 | 9 | 6 | **8.35** | Comm | — | v0.3 Week 1 |
| J2 | First-order margin protection | 7 | 9 | 10 | 9 | 6 | **8.15** | Hybrid | CRITICAL | v0.3 Week 1 |
| E2 | Szokásos rendelésem gomb | 7 | 9 | 10 | 8 | 5 | **8.15** | Behav | — | v0.3 Week 2 |
| A4 | Multi-threshold progress bar | 7 | 9 | 10 | 8 | 5 | **8.15** | Comm | — | v0.3 Week 2 |
| H1 | TTFO email drip | 7 | 9 | 10 | 8 | 4 | **8.05** | Comm | — | v0.3 Week 1 |
| B2 | Próbacsomag | 8 | 8 | 9 | 5 | 8 | **7.95** | Calc | MARGIN | v0.3 Week 3 (capped) |
| J4 | Zero delivery fee conditionals | 8 | 7 | 8 | 9 | 6 | **7.90** | Hybrid | OPS | v0.4 |
| J5 | Savings companion email | 7 | 8 | 10 | 8 | 7 | **7.85** | Comm | — | v0.3 Week 3 |
| E7 | Termékalapú reorder trigger email | 7 | 8 | 9 | 8 | 6 | **7.75** | Behav | — | v0.3 Week 4 |
| A6 | Szállítási díj savings counter | 6 | 10 | 9 | 8 | 4 | **7.75** | Comm | — | v0.3 Week 2 |
| J3 | Repeat-ability score | 7 | 7 | 9 | 8 | 8 | **7.65** | Hybrid | — | v0.4 |
| C2 | Referral program | 7 | 8 | 9 | 5 | 7 | **7.55** | Behav | MARGIN | v0.4 (post-MVP) |
| F4 | Progress bar milestone | 6 | 9 | 9 | 8 | 4 | **7.50** | Comm | — | v0.3 Week 4 |
| B1 | Családi heti csomag | 8 | 7 | 8 | 6 | 7 | **7.45** | Calc | MARGIN | v0.4 (post-MVP) |
| A8 | Post-order savings recap | 6 | 9 | 9 | 7 | 4 | **7.40** | Comm | EMAIL | → F5-el összevonva |
| E4 | Weekly suggested cart | 7 | 7 | 9 | 7 | 6 | **7.40** | Behav | — | v0.3 Week 3 |
| H2 | Savings tutorial | 6 | 8 | 9 | 8 | 5 | **7.35** | Comm | — | v0.3 Week 4 |
| F1 | Savings history dashboard | 6 | 8 | 9 | 8 | 5 | **7.35** | Comm | — | v0.3 Week 4 |
| E5 | Háztartás méret onboarding | 6 | 8 | 9 | 8 | 5 | **7.35** | Behav | — | v0.3 Week 1 |
| H5 | Savings challenge 3 rendelés | 7 | 7 | 9 | 6 | 6 | **7.30** | Behav | MARGIN | v0.4 |
| C1 | Group Order / megosztott kosár | 9 | 5 | 7 | 8 | 8 | **7.30** | Behav | OPS | v0.4 (manuális teszt) |
| A7 | Exit-intent nudge | 7 | 8 | 8 | 7 | 5 | **7.30** | Behav | — | v0.3 Week 3 |
| B3 | Szezonális csomag | 6 | 7 | 9 | 7 | 7 | **7.20** | Calc | — | v0.4 |
| F5 | Havi savings email | 5 | 9 | 9 | 8 | 4 | **7.20** | Comm | EMAIL | → A8-cal összevonva |
| D8 | VIP státusz | 7 | 8 | 7 | 7 | 6 | **7.15** | Behav | — | v0.5 |
| A5 | Okos ajánlás küszöbhöz | 7 | 6 | 9 | 7 | 6 | **7.15** | Hybrid | — | v0.4 |
| H3 | Referral kedvezmény első rendelés | 6 | 8 | 9 | 5 | 5 | **7.05** | Behav | MARGIN | v0.4 |
| B6 | Akciós termékek | 6 | 8 | 9 | 6 | 4 | **7.05** | Calc | MARGIN | v0.4 |
| I1 | Whole animal savings framing | 5 | 8 | 8 | 8 | 7 | **7.00** | Comm | — | v0.4 |
| D4 | Heti streak bónusz | 7 | 7 | 8 | 6 | 5 | **6.95** | Behav | — | v0.4 |
| B5 | Bundle builder | 7 | 6 | 8 | 6 | 7 | **6.90** | Calc | MARGIN | v0.4 |
| D2 | Köztes mérföldkövek | 6 | 8 | 8 | 6 | 5 | **6.90** | Calc | MARGIN | v0.4 |
| B4 | Heti menü csomag | 7 | 5 | 8 | 7 | 8 | **6.85** | Hybrid | CONTENT | v0.4 |
| H4 | Bolti asszisztált regisztráció | 6 | 5 | 9 | 8 | 7 | **6.80** | Behav | — | v0.3 (ops) |
| I2 | Waste reduction framing | 4 | 8 | 8 | 8 | 8 | **6.80** | Comm | — | v0.4 |
| F2 | Éves savings összesítő email | 5 | 8 | 8 | 8 | 5 | **6.80** | Comm | — | v0.5 |
| D1 | Forgalmi bónusz utalvány | 6 | 8 | 7 | 6 | 6 | **6.75** | Calc | MARGIN | v0.4 |
| C6 | Social proof | 5 | 7 | 9 | 8 | 4 | **6.70** | Comm | — | v0.4 |
| D5 | 10. rendelés = 10% | 6 | 8 | 7 | 6 | 4 | **6.55** | Calc | MARGIN | v0.5 |
| F3 | Savings forrás bontás | 5 | 7 | 8 | 8 | 5 | **6.55** | Comm | — | v0.4 |
| C4 | Pinduoduo team buying | 8 | 4 | 6 | 7 | 9 | **6.50** | Behav | OPS | v0.5 |
| C3 | Szomszéd-meghívó | 6 | 5 | 8 | 6 | 8 | **6.45** | Behav | OPS | v0.5 |
| E3 | Kosár-optimalizáló | 6 | 5 | 8 | 7 | 7 | **6.45** | Calc | — | v0.5 |
| C7 | Közösségi savings dashboard | 4 | 6 | 9 | 8 | 7 | **6.45** | Comm | PRIVACY | v0.5 |
| C5 | Munkahelyi rendelés | 6 | 6 | 7 | 7 | 6 | **6.35** | Behav | OPS | v0.5 |
| I3 | Early bird kedvezmény | 5 | 7 | 7 | 7 | 5 | **6.20** | Calc | MARGIN | v0.4 |
| F6 | Savings leaderboard | 4 | 7 | 7 | 8 | 6 | **6.10** | Comm | PRIVACY | v0.5 |
| D3 | Sizzle pontrendszer | 5 | 7 | 7 | 6 | 5 | **6.10** | Calc | — | v0.5 |
| C8 | Családi savings verseny | 5 | 5 | 7 | 8 | 7 | **6.00** | Behav | — | v0.5 |
| D6 | Születésnapi bónusz | 4 | 7 | 8 | 6 | 4 | **5.95** | Calc | PRIVACY | v0.5 |
| I5 | Smart decision badge | 4 | 6 | 7 | 8 | 7 | **5.95** | Behav | — | v0.5 |
| G6 | Egész tarja kedvezmény | 3 | 7 | 7 | 8 | 6 | **5.80** | Calc | — | v0.5 |
| B7 | Teljes állat előrendelés | 5 | 4 | 6 | 8 | 9 | **5.70** | Hybrid | OPS | v0.5+ |
| E6 | Auto-order opt-in | 5 | 5 | 6 | 8 | 6 | **5.65** | Behav | OPS | v0.5 |
| G4 | Happy hour kedvezmény | 4 | 6 | 6 | 6 | 5 | **5.30** | Calc | MARGIN | ❌ REJECT |
| D7 | Review reward | 3 | 6 | 6 | 8 | 3 | **5.00** | Behav | — | ❌ REJECT |
| G3 | Pick-up from store | 3 | 6 | 5 | 9 | 4 | **4.95** | Calc | MODEL | ❌ REJECT |
| G5 | Inventory dynamic pricing | 4 | 4 | 5 | 5 | 7 | **4.65** | Calc | OPS | ❌ REJECT |

---

## 3-LAYER ARCHITEKTÚRA BONTÁS

### 🧮 CALCULATION LAYER — Árlogika (18 ötlet)
> Mi a baseline? Hogyan számolja a rendszer a savings-et?

B1, B5, B6, D1-D6, G1-G6, I3, I4, J2

**Kockázati profil:** Legmagasabb margin erózió veszély → mindig guardrail-lel párosítva.

### 📢 COMMUNICATION LAYER — Üzenet & Láthatóság (20 ötlet)
> Hol és mikor jelenik meg? Hogyan kommunikáljuk a megtakarítást?

A1-A4, A6-A8, C6-C7, F1-F6, G1*, H1-H2, I1-I2, J3, J5

**Kockázati profil:** Biztonságos ha a calculation helyes. Bizalomépítő.

### 🎯 BEHAVIOR LAYER — Szokások, Triggerek, Közösség (20 ötlet)
> Hogyan formálja a viselkedést? Mi készteti visszatérésre?

C2, C5, C8, D4, D7-D8, E1-E2, E4-E7, H3-H5, I5, J1

**Kockázati profil:** Friction, trust (auto-order), privacy kockázatok.

### 🔀 HYBRID — Többrétegű (7 ötlet)
> Összetett, több layert érint.

A5, B4, B7, C1, C3-C4, J1-J4

**Dev költség:** 2-4 hét per ötlet, orchestrálás szükséges.

---

## KOCKÁZATI ZÁSZLÓK

### 🔴 Margin Erózió (14 ötlet — guardrail kötelező)
Minden bundling/kedvezmény ötletnek max cap kell:
- **B1, B2, B5:** Kedvezmény cap (7-15 RON vagy max 8%)
- **D1-D2, D5:** Loyalty jutalmak (50+ user kell a ROI-hoz)
- **C2, H3, H5:** Referral + kihívás ösztönzők (LTV tracking)
- **B6, G4, I3:** Promo / early bird / időalapú (ops + kannibalizáció)

> **Szabály:** I4 (margin guardrail) MINDIG előbb kell, mint bármilyen kedvezmény.

### 🟡 Ops/Komplexitás (7 ötlet — blokkolók)
- **C1:** Group order (fizetés megosztás API)
- **C3-C4:** Geo/csapat vásárlás (state machine, privacy)
- **E6:** Auto-order (visszatérítés automatizálás)
- **G5:** Inventory pricing (30 perces sync)
- **J4:** Feltételes ingyenes szállítás (logisztika ütemezés)
- **B7:** Teljes állat (koordináció)

### 🟠 Email Fáradtság (4 átfedő ötlet)
- A8 + F5 → **ÖSSZEVONÁS:** Heti összefoglaló email (vasárnap 21:00)
- J5 → **ÚJ:** Péntek 18:00 "Savings Companion" digest
- H1 → **MEGTARTÁS:** 3 email 72h alatt (acquisition-fókuszú)
- F2 → **MEGTARTÁS:** Éves, alacsony frekvencia

---

## v0.3 IMPLEMENTÁCIÓS TERV — FRISSÍTETT (4 hét)

### Week 1 (ápr 2-8) — ALAPOZÁS
| # | Feature | Effort | Dependency |
|---|---------|--------|------------|
| I4 | Margin guardrail (hard cap) | 1 nap | — |
| J2 | First-order margin protection | 0.5 nap | I4 |
| G1 | Bolti ár vs online ár termékkártyákon | 1 nap | Product JSON: "bolti_ar" mező |
| A1 | Running savings counter | 1-2 nap | G1 |
| H1 | TTFO email drip (scaffold) | 1 nap | Frappe email |
| E5 | Háztartás méret onboarding | 1 nap | — |

**Eredmény:** Margin biztonság + messaging hitelesés + savings alapja

### Week 2 (ápr 9-15) — REORDER MOTOR
| # | Feature | Effort | Dependency |
|---|---------|--------|------------|
| E1 | 1-click reorder | 2-3 nap | Rendelés történet API |
| E2 | "Szokásos rendelésem" gomb | 1 nap | E1 |
| J1 | Streakable cart reminder | 1 nap | E1 |
| A2 | Free delivery threshold nudge | 1 nap | — |
| A4 | Multi-threshold progress bar | 2 nap | A2+A3 |
| A6 | Szállítási díj savings counter | 0.5 nap | — |

**Eredmény:** 2nd order rate trigger tesztelés → 40% cél

### Week 3 (ápr 16-22) — AOV + CSOMAG TESZT
| # | Feature | Effort | Dependency |
|---|---------|--------|------------|
| B2 | Próbacsomag (capped I4-el) | 1 nap | I4 guardrail |
| A3 | Volume discount nudge | 1 nap | G2 (létezik) |
| J5 | Savings companion email template | 1 nap | — |
| E4 | Weekly suggested cart pre-fill | 2 nap | Rendelési adat |
| A7 | Exit-intent nudge | 1 nap | A4 |

**Eredmény:** Bundle stickiness validálás + AOV lift mérés

### Week 4 (ápr 23-30) — ANALITIKA + DÖNTÉS
| # | Feature | Effort | Dependency |
|---|---------|--------|------------|
| F1 | Savings dashboard (személyes) | 2 nap | A1 savings adat |
| F4 | Progress bar milestone-hoz | 1 nap | F1 |
| H2 | Savings tutorial | 1 nap | A1 |
| E7 | Reorder trigger email | 1 nap | Frappe email |
| A8+F5 | Összevont heti összefoglaló email | 1 nap | — |
| **MÉRÉS** | 2nd Order Rate (≥40%?) | — | Dashboard |
| **DÖNTÉS** | Pivot: C1 (group order) scale VAGY kill | — | Adat |

**v0.3 teljes becsült effort: ~22-25 nap → AI-gyorsítással ~3-4 hét**

---

## VALIDÁLÁSI HIPOTÉZISEK

| Ötlet | Hipotézis | Siker kritérium |
|-------|-----------|----------------|
| A1 | Real-time savings → AOV +5% vagy abandon -10% | A/B teszt 2 héten |
| E1 | 1-click reorder → ≥40% 2nd order rate | 5 user teszt, 14 nap |
| B2 | Próbacsomag → ≥40% repeat rate | 5 új user, 30 nap |
| I4 | Margin cap betartva → nulla cap sértés | Hard-code 15 RON cap, audit |
| J1 | Gentle reminder → 2nd order trigger | 10 user, 14 nap |

---

## STRATÉGIAI ÖSSZEFOGLALÁS

**Megközelítés: "Lean Communication"**

1. **Margin guardrails** (I4+J2) először — nem tárgyalható
2. **Savings megmutatása** (A1, G1) — hitelesség + AOV nudge
3. **Súrlódásmentes reorder** (E1, E2, J1) — 2nd order rate → 40%
4. **Gentle reminders** (H1, A2) — viselkedési trigger
5. **Mérés, tanulás, pivot**

**Amit NEM építünk a pilotban:**
- Komplex social/group mechanikák (C1, C3-C4) — manuális teszt max
- Inventory-sync (G5), előrendelés (B7)
- Agresszív loyalty (D1-D8) — nincs elég adat a ROI-hoz

---

## v0.4+ FEATURES

| # | Feature | Miért v0.4? |
|---|---------|-------------|
| C1 | Group Order | Multi-user session, fizetés megosztás, manuális teszt eredmény kell |
| C2 | Referral program | LTV adat kell a ROI számoláshoz |
| B1 | Családi heti csomag | Mészáros input + margin validálás |
| D1-D2 | Forgalmi bónusz | Revenue data kell |
| J3 | Repeat-ability score | 30+ nap rendelési adat |
| J4 | Conditional delivery fee | Logisztika redesign |
| A5 | Okos ajánlás | Threshold logika + termék adat |

## v0.5+ FEATURES

| # | Feature | Miért v0.5? |
|---|---------|-------------|
| D3-D8 | Teljes loyalty rendszer | Kritikus tömeg kell |
| E6 | Auto-order | Erős szokás + trust |
| F2, F6 | Éves összesítő, Leaderboard | Min. 6 hónap adat |
| G3 | Pick-up from store | Más operációs modell |
| C4, C7-C8 | Pinduoduo, közösségi | Közösségi méret kell |
| B7 | Teljes állat | Crowdbutching — komplex |

---

## CHATGPT STRATÉGIAI VÁLASZ — v0.3 ERŐSÍTÉS (2026-04-02)

> **Forrás:** ChatGPT Deák GPT "Savings Engine Koncepció" chat, 2. stratégiai válasz
> **Kulcs-insight:** "Ez NEM savings engine, hanem **decision engine** disguised as savings"

### 1) Supply-side MINIMAL beépítés v0.3-ba

A teljes Cut Optimization Engine túl nagy → **thin layer** elég.

**MVP: "Smart Swap Suggestion" (E3 minimal verzió)**
- Logika: rule-based, NEM ML
- Ha user kosárban drágább cut → ajánlj olcsóbb, hasonló use-case cut-ot
- Példák: tarja → lapocka (pörkölt), comb → darált hús, szelet hús → családi csomag
- UI: Kosárban: *"Ugyanez az étel −18 RON → válts lapockára"* [Csere gomb]

**+1 supply hook: "Ajánlott ma" (inventory pressure lite)**
- Admin flag: "push product"
- UI: *"Ma ezt éri meg választani"*
- Nem kell dinamikus pricing még — csak egy egyszerű admin toggle

### 2) CORE LOOP — Konkrét DH v0.3 User Journey

> **Kosár → Progress → Ajánlás → Reward → Reorder**

| Lépés | Képernyő | Savings elem | Cél |
|-------|----------|-------------|-----|
| 1. Terméklista | Termék badge | *"+12 RON megtakarítás ha elérsz 150-et"* | Játék indítása |
| 2. Kosár (**CRITICAL**) | Progress bar + ajánlás + swap | *"120/150 RON → még 30 RON az ingyen szállításig"* + *"Add hozzá → elérted"* + *"Olcsóbb opció: −14 RON"* | **EZ A MOTOR** |
| 3. Checkout | Minimális, megerősítés | *"+42 RON-t spóroltál"* | Nem játék, csak validation |
| 4. Post-order | Savings recap email | *"Okos döntés: 10 szállítás + 18 optimalizálás + 14 bundle = 42 RON nyereség"* | Retention driver |
| 5. Reorder | 3-5 nap email trigger | *"Újra rendelhető kosár → még jobb áron"* | Loop zárás |

### 3) Scope kompromisszum — ChatGPT javaslat

ChatGPT véleménye: **FOCUS > FEATURE COUNT**

> "Az enyém (6 feature) a jobb — HA execution számít. A tietek (22-25 nap) a jobb — HA discovery fázisban vagytok.
> DH: kis csapat + új termék + kevés adat → FOCUS."

**Javasolt kompromisszum: max 7 feature v0.3-ban**

| # | Feature | Típus |
|---|---------|-------|
| A2 | Free delivery threshold nudge | **CORE MUST** |
| A4 | Multi-threshold progress bar | **CORE MUST** |
| A5 | Smart threshold recommendation | **CORE MUST** |
| E1 | 1-click reorder | **CORE MUST** |
| A8 | Post-order savings recap | **CORE MUST** |
| E3 | Smart swap suggestion (MVP) | **EXPERIMENTAL** |
| B1/B2 | 1 bundle (családi VAGY próba) | **EXPERIMENTAL** |

> **Megjegyzés Claude:** A mi tervünk (22-25 nap) tartalmazza I4 (margin guardrail) és G1 (bolti vs online ár) is, amelyeket ChatGPT nem emelt ki külön, de implicit módon szükségesek. A kompromisszum: **ChatGPT 7 feature + I4 + G1 = 9 core feature**, a többi nice-to-have.

### 4) Naming / UI Copy / Branding — ChatGPT javaslatok

**Pozícionálás:** NEM "akció/kedvezmény/olcsóbb" → HANEM **"Okos választás"**

| Hely | ❌ NE | ✅ IGEN |
|------|-------|--------|
| Naming | "Akciók", "Kedvezmények" | **"Okos kosár"**, "Jobb választás", "Gazda mód" |
| Progress | "Még X lej a kedvezményig" | *"Még 30 RON → jobb döntés"* |
| Swap | "Olcsóbb termék" | *"Ugyanaz az étel, okosabban"* |
| Recap | "Ennyit spóroltál" | *"Így vásárolnak a törzsvásárlók"* |
| Badge | "Akciós" | *"Ajánlott választás"* |

> **Kulcs:** Nem pénzről beszélünk → **döntés minőségéről**

### 5) Mérési pontok — ChatGPT v0.3 KPI framework

| Metrika | Mit mér | Cél |
|---------|---------|-----|
| **North Star: Second Order Rate (14 nap)** | Visszatérés | ≥40% |
| **Threshold Achievement Rate** | % user aki elér 150/300 RON-t | A savings engine valós hatása |
| **Suggestion Acceptance Rate** | Swap elfogadás % + ajánlott termék kattintás % | Ha alacsony → nem segítünk dönteni |
| **AOV Uplift** | Baseline vs savings engine után | +10-15% cél |
| **Reorder within 7 days** | Heti szokás kialakulás | Loop metric |
| **Manual vs Assisted Basket** | Volt-e ajánlás interakció | Quality metric |
| 🚨 **Anti-metric: Time to Checkout** | Ha nő → túl komplex | Nem szabad növekednie |

### 6) Stratégiai veszélyek (ChatGPT figyelmeztetés)

1. **Feature halmaz csapda** — könnyű átbillenni "sok feature"-be ahelyett, hogy a core loop-ot mélyítenéd
2. **"Casino UI" veszély** — túl sok vizuális elem a savings körül → zavaró
3. **Discount trap** — ha a user "kedvezmény"-t lát "okos döntés" helyett → brand halott
4. **Supply nincs bekötve** — jelenleg frontend okos, backend vak → hosszú távon bukás

> **ChatGPT záró gondolat:** *"A v0.3 sikere nem attól függ, hogy hány feature van benne, hanem hogy: a user érzi-e, hogy 'okosabban vásárolt', mint legutóbb."*

---

## OPEN QUESTIONS / TODO

1. **TODO:** Bolti ár adatok begyűjtése → a savings engine referencia-ára (G1 dependency)
2. **TODO:** Pontos árrés kalkuláció a 300/600 RON küszöbökhöz (mit bír el az üzlet?)
3. **TODO:** Szállítási díj véglegesítés (10 RON pontos?)
4. **TODO:** Referral jutalom összeg (meghívó + meghívott — mennyi RON?)
5. **TODO:** Családi csomag összeállítás — ki dönt? (mészáros / Szabolcs / algoritmikus?)
6. **TODO:** Group Order részletes specifikáció (C1) — max résztvevők, fizetés, csomagolás
7. **TODO:** Pick-up from store modell (G3) — más árazás, más logika, későbbi fázis
8. **TODO:** I4 margin guardrail pontos küszöbértékek meghatározása (max % per rendelés)
9. **TODO:** Email küldési rendszer: Frappe email engine kapacitás és template design

---

_Generálva: 2026-04-02 | Validálva: Claude strategic analysis (5-dim scoring, 65 ötlet)_
_Eredeti források: Szabolcs (10 ötlet) + Claude web research (8 search round) + ChatGPT 3-layer framework + DH competitors_analysis v3.1 + dhop-siker-otlettar v4.0_
_Scoring: KPI Impact (30%) × Feasibility (25%) × Pilot Fit (25%) × Revenue Protection (10%) × Uniqueness (10%)_
