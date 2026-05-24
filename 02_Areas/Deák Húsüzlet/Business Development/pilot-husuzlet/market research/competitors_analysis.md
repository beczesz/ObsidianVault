---
title: "DH Versenytárs- és Piackutatás — Teljes Mélyelemzés"
version: 3.1
date: 2026-04-01
author: Claude (Anthropic) + ChatGPT (Deák GPT) + Perplexity
description: >
  Három AI párhuzamos kutatása alapján készült átfogó elemzés:
  20 versenytárs/platform, konkrét UX funkciók, pricing stratégiák,
  és DH-specifikus tanulságok.
sources: "Claude web search (15+) | ChatGPT deep research (2 round) | Perplexity (20+ forrás, 2 round)"
id: 566b6901-830c-452a-b00b-52fb8345b5a6
index_schema_version: 1
---

# DH Versenytárs- és Piackutatás — Teljes Mélyelemzés v3.1

> **A DH nem webshop, nem marketplace, nem grocery app — hanem *local demand orchestration system for meat*: egy rendszer ami irányítja, hogy mit, mikor és hogyan vásárolnak.** — ChatGPT

> **A legjobb külső minta: specialist local butcher + curated weekly basket + thresholded delivery + visible savings hibrid.** — ChatGPT Deep Research

---

## I. ONLINE HENTESBOLTOK — Részletes feature elemzés

### 1. ButcherBox (USA) — A kategória királya

**Alapadatok:** $600M/év bevétel, 400k+ előfizető, 156 alkalmazott, 0 VC (bootstrapped, Kickstarterről indult)

**Konkrét app/web funkciók (ChatGPT + Perplexity):**
- **Subscription-first logika:** User dobozt választ → delivery frequency-t állít → "complete flexibility" + free shipping
- **Box típusok:** Essentials (6 protein, Medium ~$159, Extra-Large 12 protein ~$319) + Custom Box (20+ cut-ból választhatsz)
- **Dashboard:** "Your Boxes" tab → upcoming box, next billing date, delivery status → egy pillantásra látható minden
- **Customization:** Box tartalom módosítható a számlázás előtti éjszakáig; rendszer előkészíti a boxot preferenciák + inventory alapján, user jóváhagyja email/SMS review után
- **Rewards:** Subscribers double points (1X non-sub, 2X sub); Moolah! rewards rendszer — pontok = free item vagy discount
- **Shipping:** $149+ ingyenes standard, alatta $19.99, priority $29.99 extra
- **UX redesign (2025):** Mobile-first onboarding 4 lépésben; at-a-glance subscription management csökkentette a CX hívásokat

**Pricing stratégia:**
- Fixebb árszintű nagy boxok, shipping-gate-tel kötött ingyenes szállítás
- A "savings" messaging nem explicit — inkább "premium at home, restaurant quality" pozicionálás
- Cancel-anytime rugalmasság csökkenti a belépési félelmet

**Amit DH-nak át kell vennie (ChatGPT):**
1. **Curated household box logic** — ne termékkatalógusból induljon a user, hanem 2-4 kész heti csomagból
2. **Simple decision architecture** — ne 37 SKU-ból válasszon, hanem csomagokból + add-on
3. **Repeat behavior architecture** — heti rutin logika, nem egyszeri rendelés

**Amit NE csináljon a DH:**
- A teljes subscription-first modellt most még NE — pilot fázisban változó operáció mellett retention-csapda
- A doboz és a rutin kell, nem a teljes előfizetéses kötöttség

---

### 2. Crowd Cow (USA) — Átláthatóság és farm-to-table

**Alapadatok:** Premium online marketplace, direct-to-farmer modell, "share" koncepció

**Konkrét funkciók (ChatGPT + Perplexity):**
- **Customizable premium marketplace:** User saját boxot craftolhat VAGY curated boxot választhat
- **Shipping:** $149 minimum ingyenes szállítás + ajándékokhoz is
- **Flexible schedule:** Rugalmas szállítási ütemezés
- **Rewards:** Erős rewards-réteg — subscribers double points, Moolah! pontrendszer
- **Recurring box:** Nem teljesen merev — rendszer előkészíti preferenciák + inventory alapján, user review-zhatja
- **Traceability:** "Farm-story" oldalak, origin transparency, breed/feed info minden terméknél
- **"Share" koncepció:** Bulk/family-packs, "quarter cow" opciók

**Amit kombinál:** traceability, flexibility, rewards, shipping threshold, pre-filled recurring box review

**Amit DH-nak át kell vennie (ChatGPT):**
1. **Threshold-led economics** — free shipping nem default, hanem elért kosárértékhez kötött viselkedésformáló eszköz
2. **Reward layer** — Moolah! logika: pontok minden költésből → free item vagy discount
3. **Review-before-recurring-order** — heti ajánlott kosár vasárnap este "kész", de user módosíthatja

**Amit NE csináljon:**
- Túl széles választék és premium-explorer identitás — DH nem discovery platform, hanem **heti háztartási döntésmotor**
- Túl sok opció rontja a rutinélményt

---

### 3. Porter Road (USA) — Specialist butcher + curated subscription

**Alapadatok:** Nashville-i hentes bolt + online D2C, whole-animal butchery filozófia

**Konkrét funkciók (ChatGPT + Perplexity):**
- **Subscription típusok:** Butcher's Choice Box $199, Best of Porter Road $170, Beef and Pork Basics $120, Grilling Heroes $110
- **Ritmus:** 2, 4 vagy 8 hetes ciklus, 15% kedvezmény subscription-nel
- **Customization:** Add-on termékekkel testre szabható a doboz
- **Fresh quality:** FAQ hangsúlyozza — legtöbb termék NEM fagyasztva megy, friss minőség
- **Checkout:** Gift note elérhető, eco-friendly csomagolás gel packekkel
- **Üzenet:** "Cuts for the Crowd", "Subscribe and Simplify", whole-animal butchery filozófia
- **Hybrid modell:** Fizikai bolt + online → bizalom-építés

**Amit DH-nak át kell vennie (ChatGPT):**
1. **Household-fit box naming** — nevezzétek el a csomagokat háztartás-mérethez (2 fős, 4 fős, stb.)
2. **Fresh-quality messaging** — a Deák friss, nem fagyasztott hús = erős differenciátor
3. **Fizikai jelenlét mint trust-builder** — a 3 bolt Újvárhelyen ingyen adja ezt

**Amit NE csináljon:**
- Országos D2C ambíció — helyi validáció az első

---

### 4. Farmison & Co (UK) — Prémium online hentes, threshold messaging

**Alapadatok:** 28.000+ pozitív értékelés, "UK's Best Online Butcher", friss hús (nem fagyasztott)

**Konkrét funkciók (ChatGPT + Perplexity):**
- **Product page:** Cuts grouped by animal + use case (steaks, roasts, burgers), részletes leírás, cooking suggestions, origin info
- **Cart flow:** Lightweight cart, total weight + price real-time update
- **Delivery scheduling:** Postcode bevitel → nominated delivery day (Tue-Sat) → £60+ free, alatta fix fee
- **Checkout:** "You're X away from free delivery" persistent messaging
- **Live cart threshold messaging:** Nagyon konkrét — "Még £X és ingyenes szállítás"
- **Promo grammar:** "Any 3 for X", "családi csomag", "build your own box"
- **Lightweight loyalty:** Egyszerű belépési bónusz

**Amit DH-nak át kell vennie (ChatGPT):**
1. **Live cart threshold messaging** → "Még 32 lej és ingyenes szállítás" / "Még 18 lej és extra savings szint"
2. **Simple promo grammar** → családi csomag, "3 az 1-ben" ajánlatok
3. **Nominated delivery day** → fix szállítási nap a postcode/körzet alapján

**Amit NE csináljon:**
- Ne menjen el túl mélyen a promo-engine irányba — a savings-nek rendszerből kell jönnie, nem "kuponos húsbolt" érzésből

---

### 5. Pipers Farm / Edenmoor (UK) — Etikus brand + loyalty rendszer

**Alapadatok:** Devon-i farm, 25 kis farmmal dolgozik, 2026-ban Edenmoor névre váltott

**Konkrét funkciók (ChatGPT):**
- **Moor Rewards rendszer (az új brand alatt):**
  - 200 pont csatlakozásért
  - Születésnapi pont bónusz
  - Review-írásért pont
  - Pontok beválthatók következő rendelésnél
- **Brand messaging:** "We're all in this together" tone, co-creation érzés
- **USP:** Animal welfare, slow-growth breeds, traditional farming
- **Curated boxes + standalone cuts** az online store-ban

**Amit DH-nak át kell vennie (ChatGPT):**
1. **Egyszerű rewards belépés** — nem bonyolult klub, hanem egyszerű kezdő egyenleg (pl. 10 pont = első regisztráció)
2. **Values + story messaging** — Székelyudvarhelyen az értékek és a történet erősebb mint az ár (Perplexity)
3. **Customer testimonials + family recipes** mint social proof

**Amit NE csináljon:**
- A teljes loyalty komplexitást ne másolja — pilot fázisban a savings tracker elegendő

---

## II. HETI DOBOZ ÉS HELYI MODELLEK

### 6. Riverford Organic (UK) — A heti doboz veteránja

**Alapadatok:** 50.000 doboz/hét, 4.8/5 értékelés 20.000+ review, van 14 éve visszatérő ügyfél

**Konkrét funkciók (Perplexity + Claude):**
- **Két megközelítés:**
  - **Set Box:** Fix tartalom, éves tervezéssel (waste minimalizálás) — de "Veg Alerts": 3 terméket kizárhatsz
  - **Build Your Own:** £15 minimum felett teljesen szabad összeállítás
- **Edit box flow:** "Edit your box" → add/remove items → real-time weight + price recalculation
- **Skip/pause:** Egy gombnyomás, automatikus folytatás
- **Frequency:** Heti, kétheti, 3 heti, 4 heti, vagy egyszeri
- **Delivery:** Helyi "vegman/lady" (nem futár!) fix napi körökön → maximális hatékonyság
- **Ingyenes szállítás** minden rendelésre
- **Familiar Favourites:** A rendszer megjegyzi a kedvenceket → stickiness

**Kiegészítő részletek (Claude web research round 2):**
- **"Vegman/lady" modell:** Nem alkalmazott futárok, hanem helyi sofőrök, akik személyes viszonyt építenek az ügyféllel — pontosan a DH "helyi szállítás" vízió
- **Familiar Favourites:** App megjegyzi a rendszeres termékeket → egy kattintással újrarendelhető
- **Essentials add-on:** Kenyér, tej, liszt, hummus stb. hozzáadhatók a zöldségdobozhoz → cross-sell minta
- **Referral program:** Új ügyfél beajánlás = £15 kedvezmény mindkét félnek
- **Frequency rugalmasság:** 1/2/3/4 heti ritmus VAGY egyszeri — nem kényszerít előfizetésre
- **Annual planning:** A farm a fix dobozok alapján tervez (waste <3%) — a kiszámíthatóság = a farmer érdeke is

**Amit DH-nak át kell vennie:**
1. **"Húsos nap" koncepció** — fix szállítási nap körzetenként, helyi ember szállít (nem random futár)
2. **Set box + Veg Alerts logika** → alapcsomag + "mit NE tegyen bele" opció (egyszerűbb mint teljes customization)
3. **Skip/pause egyszerűség** → ne legyen nehéz szüneteltetni
4. **Essentials add-on** — kiegészítő termékek (pl. szalonna mellé kenyér, fűszer) → AOV növelés
5. **Familiar Favourites** → "Szokásos rendelésem" gomb a DH appban

---

### 7. Ooooby (NZ/AUS) — Kisvárosi food hub

**Alapadatok:** Új-zélandi digitális "farmers' market", kis farmoknak ad tech infrastruktúrát

**Konkrét funkciók (Perplexity):**
- **Heti parcel-építés:** Customer online összeállítja a heti parcellát
- **Neighbourhood delivery:** Batch-style, fix útvonalak, heti ritmus
- **Pricing:** Parcels $39-98, free delivery $200+, reduced $100+
- **Multi-producer:** Több helyi termelő egy platformon

**DH relevancia:** A modell bizonyítja, hogy "kisvárosi + helyi specialist + box delivery" séma működik. De a multi-producer komplexitás túl korai DH-nak.

### 8. CSA (Community Supported Agriculture) modell

**Koncepció (Perplexity):** Tagok a szezon előtt fizetnek → farm kiszámítható cash flow → heti/kétheti szállítás fix ütemezéssel

**Meat Share CSA modellek (Claude web research round 2):**
- **Európai jelenlét:** Főleg USA-ban népszerű (Carolina Pastures, Anchor Ranch Farm, Mint Creek Farm), Európában ritkább de létezik
- **Működés:** Havi/negyedéves fix összeg → heti/kétheti húscsomag (farmonként eltérő tartalom)
- **Pricing minta (USA):** $100-250/hó a legtöbb CSA meat share
- **Crowdbutching a európai változat:** Hollandia/Németország a legfejlettebb piac (ld. #17 fent)
- **"Quarter carcass" modell:** Családok negyedállatot vesznek szezonálisan → nagy kiszerelés, de alacsony egységár

**DH relevancia:** "Meat share / quarter-carcass" add-on — helyi vásárlók előre fizetnek X szállításért → cash flow simítás + ügyfél lock-in. Székelyudvarhelyen a bizalom és közösség ezt lehetővé teszi (Phase 2-3 ötlet). **A Crowdbutching modell (#17) a legközelebbi európai analógia.**

---

## III. SAVINGS-POZICIONÁLÁSÚ PLATFORMOK

### 9. Picnic (Hollandia) — A DH legjobb analógiája

**Alapadatok:** $496M Series E (2025), 5415 alkalmazott, 120+ holland város, 1000+ elektromos autó

**Konkrét app funkciók (Perplexity deep-dive):**
- **Home screen:** Hero banner "no delivery fee" + "low prices" + nagy search bar
- **Savings labels:** Minden termékkártyán "you save X €" felirat + szín-kódolt sáv
- **Smart trolley:** Futó "total" + "estimated savings vs. supermarket" a kosár képernyőn
- **Basket-level savings counter:** Persistent banner: "You've saved X € so far" + nudge: "add 1 more item to save extra 1.50 €"
- **Delivery slot:** Másnapi szállítás, fix időablakok körzetenként (nem on-demand!)
- **Post-order recap:** Confirmation screen explicit savings vs. "supermarket pricing" + link a "Your savings history"-hoz
- **Push notifications:** "Your order will arrive in 10 minutes" + "you saved X" recaps
- **Server-driven UI:** Gyors update-ek központilag, nem kell app update

**Ordering flow (Perplexity):**
1. Download & register → postcode check
2. Browse/search → auto discounts
3. Set delivery time (next day, neighbourhood slots)
4. Review basket + savings → persistent savings counter
5. Confirm & pay → savings recap
6. Push: "Van arrives in 10 min" + post-delivery savings recap

**Retention mechanika:**
- "Always free delivery" mint core UX promise
- Threshold-nudge: "Add 1 more item to save X" → basket size növelő
- Running savings counter → pszichológiai reward folyamatosan

**Kiegészítő részletek (Claude web research round 2):**
- **Eredet:** 2015, 30 mérnök fejlesztette 3 évig a route-based modellt mielőtt indultak volna — alaposság > sebesség
- **Skála:** 2M ügyfél, 200+ város, 7 distribution center (NL), terjeszkedés Németország (Hamburg, NRW)
- **€430M Series E (2025):** A piac hisz a milkman modellben — de ez nem quick commerce, hanem PLANNABLE commerce
- **100% elektromos flotta:** 1000+ kis elektromos furgon, brand-identity része
- **Napi 150k rendelés** feldolgozó kapacitás
- **"Modern milkman" branding:** A nosztalgia + megbízhatóság kombó — NEM tech-bro narrative
- **Zero delivery fee MINDIG:** Nincs minimum rendelés a szállításhoz (de van minimum order €35)

**Amit DH-nak KONKRÉTAN át kell vennie:**
1. **Running savings counter** a kosár képernyőn — "Eddig X lejt spóroltál"
2. **Threshold nudge** — "Még Y lej és ingyenes szállítás"
3. **Post-order savings recap** — "Ezzel a rendeléssel Z lejt spóroltál a bolti árhoz képest"
4. **Neighbourhood-based fix delivery slots** — Székelyudvarhely méretéhez tökéletes
5. **"Milkman" narratíva DH verzió:** "A te hentesed házhoz jön" — bizalom + személyes viszony, nem app-logika

---

### 10. Misfits Market (USA) — Shopping window + pre-filled cart

**Alapadatok:** ~$1B felé, 90% US ZIP code lefedés, "ugly food" + savings

**Konkrét app funkciók (Perplexity + Claude web search):**
- **Shopping window:** 6 nappal a szállítás előtt nyílik, 4 nap áll rendelkezésre módosításra
- **Pre-filled cart:** Hetente automatikusan feltöltve személyre szabott termékekkel (regisztrációkor megadott preferenciák alapján)
- **Dollar-based cart:** Nem darabszám, hanem összeg-alapú kosár
- **Learning algorithm:** A prefilled cart tanul a korábbi rendelésekből → egyre pontosabb
- **Auto-order:** Window zárásakor automatikusan leadja a rendelést (ha minimum teljesül)
- **Skip/pause:** Heti skip egy kattintással, bónuszok megmaradnak
- **Savings messaging:** "Up to 40% savings vs. grocery store" + $25/hét átlag savings

**Ordering flow (Perplexity):**
1. Sign up → preferences (plant-based, meat, bread, pets, stb.)
2. Pre-filled cart megjelenik a shopping window nyitásakor
3. Módosítás: remove/add items, teljes kínálatból
4. Window closes → auto-order ha minimum teljesül
5. Charge only for what's in cart at close

**Kiegészítő részletek (Claude web research round 2):**
- **Misfits Perks loyalty program:** Pontgyűjtés minden vásárlásra + app letöltés/ajánlás bónusz → pontok = rendelési kedvezmény
- **Környezeti hatás dashboard:** "X gallon vizet spóroltál" + "Y kg CO2 csökkentés" — morális reward a savings mellé
- **AI grocer:** Idővel tanul a preferenciákból → a pre-filled cart egyre pontosabb, egyre kevesebb módosítás kell
- **"Up to 40% savings"** fő messaging — nem "olcsó", hanem "OKOS vásárlás"
- **Auto-order window:** Ha nem nyúlsz hozzá, automatikusan rendelés → retention hack

**Amit DH-nak KONKRÉTAN át kell vennie:**
1. **"Heti ajánlott kosár" pre-fill** — default heti húscsomag a user korábbi rendelései alapján, de módosítható 24h ablakban
2. **"Savings vs. supermarket" messaging** — "Ennyit spóroltál a bolti árhoz képest" a kosár képernyőn
3. **Auto-order logika** (Phase 2) — ha a user nem módosít, az ajánlott kosár automatikusan lead
4. **Loyalty program egyszerű verzió** (Phase 2) — "10. rendelés = 10% kedvezmény" vagy hasonló egyszerű jutalmazás
5. **"Okos vásárlás" framing** — NEM "olcsó hús", hanem "okosan vásárolsz, mert termelőtől rendelsz"

---

## IV. ROMÁNIAI / CEE PLATFORMOK

### 11. Freshful (Románia) — A nagy romániai benchmark

**Alapadatok:** eMAG csoport, 100k+ letöltés, 45k+ vásárló 1. évben, 94% service promoter rate, 20.000+ termék

**Konkrét funkciók (Perplexity + ChatGPT + Claude):**
- **AI-driven routing:** ORTEC e-Grocery Delivery + saját ML algoritmok — order picking, route efficiency, delivery windows real-time optimalizálás
- **Delivery:** 7/7 nap, 08:00-23:00, 299 lej+ ingyenes, alatta 12.99 lej
- **"Add to order":** Megrendelés után is módosítható
- **ETA funkció:** Pontos szállítási idő becslés
- **Recept-alapú kosár:** "Egy kattintással kosárba" funkció receptekből
- **Barcode scanning:** Termék beazonosítás vonalkód olvasóval
- **Meal voucher:** Fizetés étkezési jeggyel
- **SGR begyűjtés:** Visszaváltható csomagolás kezelés
- **Freshful Now:** 30 perces delivery Wolt-on keresztül
- **95%+ on-time delivery** teljesítmény

**Kiegészítő részletek (Claude web research round 2):**
- **ORTEC route optimization:** Enterprise-grade ML a szállítási útvonalakhoz — DH-nak nem kell ilyen, de a FIX KÖRÖK = hasonló hatékonyság manuálisan
- **Mixed reviews:** Túl sok popup + notification spam → felhasználók panaszolják a UX-et — **DH tanulság: minimális push, ne spammeld az ügyfelet!**
- **Freshful Now (Wolt integráció):** 30 perces express → DH-nak NEM releváns, de mutatja hogy a piac a gyorsaságot is kéri
- **Barcode scanning:** Fizikai termék → app kosárba — kreatív bridge offline↔online — **DH Phase 2 ötlet: bolt QR → online újrarendelés**
- **Meal voucher elfogadás:** Romániai specifikus, DH-nál nem releváns

**Amit DH-nak tanulnia kell:**
- Még a nagy, jól finanszírozott modell is threshold-alapú szállítást használ
- A receptalapú kosár-feltöltés a DH "heti menü → automatikus kosár" funkciójának előképe
- **De a 94% SPR nem releváns DH benchmark** — pilotban 70-80% elégedett = nagyon jó
- **UX leckék:** Kerüld a popup-okat és notification-spammet — a kisvárosi ügyfél nem tolerálja

### 12. Bringo (Románia) — Carrefour-backed convenience

**Alapadatok:** 1.6M rendelés/2024, 37 város, 200+ partner bolt, ~€100M forgalom, 300 RON AOV

**Konkrét funkciók (Perplexity + Claude):**
- **Personal shopper:** Online rendelés → shopper vásárol a boltban → kiszállítás
- **"Same price as in store"** messaging — boltár-egyezés ígéret
- **Bringo YOU:** Loyalty program — vásárlási rutin jutalmazása
- **30-90 perc delivery:** Rapid-delivery modell
- **4/5 rendelés akciós terméket tartalmaz** — ár a fő motivátor

**Kiegészítő részletek (Claude web research round 2):**
- **Carrefour stratégiai partner** → 2016-tól, 2017-ben majority stake → Bringo = Carrefour delivery arm
- **37 város, 200+ partner bolt** → nem csak Carrefour, hanem más boltok is csatlakoztak
- **Revenue (2023):** 60M RON (~€12M), de még mindig veszteséges (-332k RON)
- **Tazz (konkurens):** 177M RON revenue, -110M RON veszteség (2022) → a delivery marketplace Romániában deficites üzlet
- **Piaci kontextus:** Glovo, Tazz, Bolt, Bringo = Big 4 Románia → de MIND veszteségesek → DH NEM akar ebbe a versenybe beszállni

**DH tanulság:** 300 RON AOV a romániai benchmark; DH 150+ RON cél reális. A "same price" messaging nem DH-ra való — DH-nál a savings rendszerből jön, nem ár-egyezésből. **Kritikus:** A nagy platformok MIND veszteségesek → a DH mikro-modell (alacsony overhead, nincs futárhálózat) pont ezért jobb pozícióban van.

### 13. Rohlik/Kifli (CZ/HU) — CEE e-grocery unicorn

**Alapadatok:** 5 ország, 800k+ customer, profitábilis München/Csehország/Magyarország

**DH tanulság:** CEE piac érett az online grocery-ra. De Rohlik szupermarket — DH specialist, ami jobb margint ad. A "heti tervezés" és "családi narratíva" átültethető.

---

## V. BUKÁSOK — Kritikus tanulságok

### 14. Farmdrop (UK) — A LEGFONTOSABB FIGYELMEZTETÉS

**Bukás:** £36M VC → megszűnt 2021. december
- 200 alkalmazott £12M bevételre
- 7.000 SKU — túl nagy kínálat
- Szupermarket-szintű szolgáltatást próbáltak kis cég erőforrásaival
- Post-Covid kereslet visszaesett, költségek maradtak

**DH tanulság:** NE próbálj szupermarket lenni. 37 termék = HELYES. Tartsd alacsonyan a fix költségeket.

### 15. Getir/Gorillas — Quick commerce összeomlás

**Bukás:** $12B értékelés → kivonulás EU/USA-ból (2024)
- Fenntarthatatlan unit economics, "blitzscaling"
- Post-pandemic: árérzékenység visszatért

**DH tanulság:** DH NEM quick commerce — tervezett, heti szállítási modell fenntarthatóbb.

### 16. HelloFresh — A retention probléma

**Churn adatok:** 50% 1. hónapban, 85% 6. hónapra, 90% 12 hónap
- Ingyenes próba → ingyenes elvárás → fizetésnél kilép

**DH tanulság:** NE adj ingyenes próbát! A hús alapanyag ami hetente kell — de az első 3 rendelésben kell szokást építeni.

---

## VI. INNOVATÍV MODELLEK

### 17. Crowdbutching / Grutto (NL) — Közösségi állatvásárlás

**Alapadatok:** Hollandia-alapú, Kaufnekuh.de (Németország), Kaufeinschwein.de, kaufnehun.de, kaufnegans.de (szezonális)

**Konkrét funkciók (Perplexity + Claude web research round 2):**
- **Crowdfunding logika:** Ügyfél "részvényt" vesz egy állatból → CSAK amikor az összes rész elkelt, történik vágás → zero waste
- **Teljes transzparencia:** Minden állat saját fülszámmal azonosítható → pontos farm eredet
- **Etikai garancia:** Hormone-free, antibiotikum-mentes, kis farmokról
- **Delivery idő:** ~2 hét rendeléstől (mert meg kell várni amíg az egész állat elkél)
- **Alacsony belépési küszöb:** Nem kell egy egész állatot venni, csak "részt" (2-5 kg csomag)
- **Multi-species:** Tehén, sertés, csirke, liba (szezonális) — mindegyik külön platform-oldalon
- **Német piac:** Kaufnekuh.de a fő német brand — bizonyítja hogy a modell skálázható más országokra

**DH relevancia:**
- **Phase 2-3 ötlet:** "Közösségi sertésvágás" — 10-15 család előrendel egy egész sertést, Deák vágja és szállítja → zero waste + community
- **De NEM MVP:** A crowdbutching logika túl komplex a pilot fázishoz
- **Meglepő tanulság:** A "várakozás" (2 hét) NEM probléma — sőt, növeli a perceived value-t. A DH fix heti szállítás hasonló pszichológiát épít.

### 18. Applestone Meat (USA) — Hús automatából

**Koncepció:** Prémium helyi hús 24/7 vending machine-ekből, 3.000 font/hét
**DH tanulság:** A kényelem önmagában is eladható ha a minőség ott van.

---

## VII. CROSS-PLATFORM MINTÁZATOK — Amit mind a 3 AI egyformán lát

### A három kutatás közös felismerései (legmagasabb konfidencia):

1. **Curated box > teljes katalógus** — Minden sikeres hentes-platform doboz/csomag logikát használ, nem "válogass a polcról"
2. **Threshold-based free delivery = egyetemes** — Farmison £60, Village Butchers £85, Freshful 299 lej, DH 150 RON → jól illeszkedik
3. **Savings must be VISIBLE** — Picnic, Ibotta, Misfits mind explicit savings counter-t használ
4. **Fix útvonal > on-demand** — Picnic, Riverford, Ooooby mind batch/route delivery → DH modellje helyes
5. **Specialist > Generalist** — Farmdrop (generalist) bukott, ButcherBox (specialist) $600M → DH specialist pozíció helyes
6. **Heti/kétheti rutin természetes** — Riverford 14 év, Misfits shopping window, Freshful kétheti ritmus
7. **Story + values > ár** — Pipers Farm, Crowd Cow, Porter Road mind értékekre épít → Deák Húsmíves helyi reputációja erős alap

### ChatGPT meta-felismerés:
> **A nyerők közül EGYIK sem "sima webshop"** — mindegyik vagy box/subscription, vagy curation + trust, vagy traceability + rewards logikát épít.

### A DH egyedülálló kombinációja:
Egyetlen versenytárs sem kombinálja mind a négy elemet: (1) helyi specialist hentes + (2) fix útvonal delivery + (3) savings engine UX + (4) kisvárosi közösségi modell. Külön-külön mindegyik létezik — de a kombináció DH-specifikus.

---

## VIII. SUPPLY-SIDE VAKFOLT — ChatGPT kritikus kiegészítés

> Mindkét eredeti kutatás demand-oldali fókuszú volt. Ami HIÁNYZOTT: **a hús ellátási lánc működése kis volumenen.**

Három kockázat:
1. **Inventory volatility:** Vágás ciklusos, részek eltérő kereslete → UX-re, savings-re hatás
2. **Margin nem egységes:** Comb ≠ tarja ≠ kolbász → basket optimization kell
3. **Waste risk:** Romlandó → rossz forecast = veszteség

**Meta-felismerés:** A Smart Basket Engine NEM UX feature — hanem **supply-side optimalizációs eszköz** (demand shaping system a hentes számára).

---

## IX. BETA KPI FRAMEWORK

### TOP 3 KPI (nincs kompromisszum — ChatGPT)

| # | KPI | Target |
|---|-----|--------|
| 1 | **TTFO** (Time to First Order) | ≤72 óra |
| 2 | **Second Order Rate (14 nap)** | ≥30% beta, ≥40% good, ≥50% excellent |
| 3 | **Contribution Margin/Order** | Pozitív |

### Kiegészítő KPI-k (ChatGPT 10 pontos javaslat)
4. AOV (benchmark: Bringo 300 RON)
5. Delivery cost/order
6. Share of orders above threshold
7. Reorder usage rate
8. Family pack share
9. Group-order share
10. Refund/complaint rate

**Jobb mérőszám mint SPR:** "Would order again within 7 days?" (ChatGPT)

---

## X. DH-RA KONKRÉTAN ÁTVEENDŐ FUNKCIÓK — TOP 10

| # | Funkció | Forrás | Prioritás |
|---|---------|--------|-----------|
| 1 | Running savings counter a kosárban | Picnic | Beta |
| 2 | Threshold nudge messaging | Farmison, Picnic | Beta |
| 3 | 2-4 curated family pack mint default | ButcherBox, Porter Road | Beta |
| 4 | Heti ajánlott kosár (pre-fill) | Misfits Market | Phase 2 |
| 5 | Post-order savings recap | Picnic | Beta |
| 6 | Fix delivery day körzetenként | Riverford, Picnic | Beta |
| 7 | Skip/pause egyszerűség | Riverford, Misfits | Phase 2 |
| 8 | Review-before-order flow | Crowd Cow, Misfits | Phase 2 |
| 9 | Simple rewards (kezdő egyenleg) | Edenmoor, Crowd Cow | Phase 2 |
| 10 | "Meat share" pre-order | CSA, Crowdbutching | Phase 3 |

---

## XI. AMIT NE CSINÁLJON A DH — TOP 7

1. **Ne legyen webshop** — legyen demand orchestration system
2. **Ne másolja a teljes subscription modellt** — előbb heti rutin + pre-filled cart
3. **Ne próbáljon szupermarket lenni** — 37 SKU = HELYES (Farmdrop tanulság)
4. **Ne versenyezzen árral** — savings = RENDSZER, nem kedvezmény
5. **Ne adjon ingyenes próbát** — HelloFresh trap
6. **Ne skálázzon profitabilitás előtt** — Getir/Gorillas tanulság
7. **Ne menjen el kuponos húsbolt irányba** — savings rendszerből jön, nem promo-zajból (ChatGPT)

---

## XII. ZÁRÓ VERDIKT

> **"A DH sikere nem azon múlik, hogy mit találtok ki, hanem azon, hogy melyik 3 dolgot csináljátok meg könyörtelenül jól."** — ChatGPT

A három AI kutatás legfontosabb közös következtetése: a DH pozíciója egyedülálló és védhető. A kulcs: **execution + fókusz + mérés.**

**Következő lépés:** Beta Playbook — napi KPI tracking, mikor avatkoztok be, mikor pivotoltok.

---

_Generálva: 2026-04-01 | 3 AI párhuzamos kutatása: Claude (15+ web search) + ChatGPT (2 round deep research) + Perplexity (20+ forrás, 2 deep-dive round)_

**Források:** ButcherBox (butcherbox.com, goodhousekeeping, shopify.com, bungleo.com), Crowd Cow (crowdcow.com, vizologi), Porter Road (porterroad.com, artofgrill), Farmison (farmison.com, d3r), Pipers Farm/Edenmoor (edenmoor.com, trustpilot), Riverford (riverford.co.uk, organic.riverford.co.uk), Ooooby (letsfoodideas, deliverybizpro), Picnic (apple, blog.picnic.nl, salesforce.com, diginomica.com), Misfits Market (misfitsmarket.com, dontwastethecrumbs.com, businessinsider), Freshful (zitec.com, ortec.com, thediplomat.ro, romania-insider.com), Bringo (esmmagazine, romania-insider.com), Rohlik (cityforthefuture), Farmdrop (thegrocer.co.uk, ooooby.medium.com), Getir (grocerygazette.co, businessinsider), HelloFresh (cotera.co), Ibotta (home.ibotta.com), Crowdbutching (mpulse.de), Applestone (modernfarmer.com), CSA (suscof)
