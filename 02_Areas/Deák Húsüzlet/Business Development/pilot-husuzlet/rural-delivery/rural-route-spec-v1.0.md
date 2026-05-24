# Falusi Route Pilot — Feature Specifikáció v1.1

**Dátum:** 2026-05-03
**Státusz:** DRAFT v1.4 — Hibrid zóna-detekció modell (GPS-javaslat + 2 gomb + checkout validáció)
**Jira Epic:** DH-184
**Brainstorm forrás:** `brainstorm/brainstorm_zona-detektacio.md` (v3 szintézis)
**Útvonal dokumentáció:** `Business Development/pilot-husuzlet/rural-delivery/route-plan-v1.0.md`

---

## 1. Probléma és hipotézis

**Probléma:** A Székelyudvarhely környéki falvakban nincs friss, minőségi húshoz való hozzáférés. Ez nem kényelmi, hanem **elérhetőségi** probléma — a falusi vásárlónak be kell mennie a városba, ami idő + költség.

**Hipotézis:** Ha fix napon, előrendeléses modellel szállítunk a falvakba, a kereslet stabilabb lesz, mint a városi convenience modell, mert nincs alternatíva.

**Validáció forrása:** Telefonos beszélgetés egy vidéki érdeklődővel (2026-04-30) + 3 AI szintézis (ChatGPT + Perplexity + Gemini).

---

## 2. Az útvonal

### 2.1 Tervezett route (Google Maps alapján)

**Kiindulópont:** Székelyudvarhely (Deák Húsmíves üzem) — kisváros, ~31.000 lakos
**Fordulópont:** Cristuru Secuiesc (Székelykeresztúr) — kisváros, ~8.800 lakos
**Becsült távolság:** ~55 km (körkörös hurok — délen lemegy, Keresztúrnál fordul, északon visszajön)
**Becsült menetidő:** ~1 óra 5 perc (megállók nélkül)

**Települések az útvonal mentén (sorrend szerint):**

| # | Település | Magyar név | Típus | Becsült háztartás | Megjegyzés |
|---|-----------|------------|-------|-------------------|------------|
| 1 | Feliceni | Felsőboldogfalva | Falu | ~400 | Route indulás déli irányba |
| 2 | Tăureni | Bikafalva | Falu | ~300 | |
| 3 | Mugeni | Bögöz | Falu | ~600 | Nagyobb község |
| 4 | Dejuțiu | Dezsőfalva | Falu | ~200 | |
| 5 | Porumbenii Mari | Nagygalambfalva | Falu | ~500 | |
| 6 | Porumbenii Mici | Kisgalambfalva | Falu | ~200 | |
| 7 | Beteşti | Betfalva | Falu | ~150 | |
| 8 | **Cristuru Secuiesc** | **Székelykeresztúr** | **Város** | **~4.000** | **Második legnagyobb város a körzetben** |
| 9 | Rugăneşti | Rugonfalva | Falu | ~200 | |
| 10 | Şimoneşti | Siménfalva | Falu | ~400 | |
| 11 | Cobăteşti | Kobátfalva | Falu | ~150 | |
| 12 | Mihăileni | Csíkszentmihály | Falu | ~300 | |
| 13 | Morăreni | Malomfalva | Falu | ~200 | |
| 14 | Bulgăreni / Bisericani | — | Falu | ~200 | Visszaút Udvarhelyre |

**Összesen:** ~7.800 háztartás a route mentén (ebből Cristuru Secuiesc ~4.000).

### 2.2 Route economics

| Tétel | Összeg |
|-------|--------|
| Üzemanyag (~55 km) | ~55 RON |
| Sofőr (3-4 óra x 30 RON) | ~100-120 RON |
| Amortizáció + egyéb | ~25 RON |
| **Összes OPEX / route** | **~190 RON** |

| Rendelés/route | Költség/rendelés | Fedezet (200 RON AOV, 20% margin) | Eredmény |
|---------------|-----------------|-----------------------------------|----------|
| 5 | 38 RON | 24 RON | **-14 RON/rendelés** |
| 10 | 19 RON | 24 RON | **+5 RON/rendelés** |
| 15 | 12,7 RON | 24 RON | **+11,3 RON/rendelés** |
| 20 | 9,5 RON | 24 RON | **+14,5 RON/rendelés** |

**Breakeven:** ~8 rendelés/route. Cél: 15+ rendelés a fenntarthatósághoz.

**⚠️ Pilot döntés:** Phase 1-ben NINCS minimum küszöb. Ha 1-2 rendelés van, akkor is indul a route — ez tudatos befektetés a flywheel beindításához. Az első hetek OPEX vesztesége (~150-170 RON/route alacsony rendelésszámnál) a szórólapozás + ambassador toborzás + bizalom-építés költsége. A cél: az emberek lássák, hogy TÉNYLEG jön a szállítás, és következő héten már többen rendelnek.

### 2.3 Szállítási díj logika (Keresztúri régió)

| Kosárérték | Szállítási díj |
| ---------- | -------------- |
| >= 150 RON | **INGYENES**   |
| < 150 RON  | **15 RON**     |

---

## 3. Üzleti modell — a "tejkihordós" rendszer

### 3.1 Hogyan működik

```
1. RENDELÉS         Vásárló rendel az appon/weben (település-választó)
                    Határidő: szállítás előtti nap 20:00

2. ÖSSZESÍTÉS       Rendszer összesíti a route rendeléseit
                    Ha < minimum küszöb -> értesítés küldése

3. CSOMAGOLÁS       Deák Húsmíves becsomagolja settlement szerint csoportosítva
                    Hűtőtáskás rendszer

4. SZÁLLÍTÁS        Fix napon (pl. csütörtök 14:00-18:00) körbejárja a route-ot
                    Átadási pontok: ambassador háza / megbeszélt pont

5. FIZETÉS          Készpénz átvételkor (pilot fázis)

6. VISSZACSATOLÁS   "Hogy ízlett?" push notification másnap
                    Reorder suggestion 5-7 nap múlva
```

### 3.2 Fix nap logika

| Paraméter | Érték | Megjegyzés |
|-----------|-------|------------|
| Szállítási nap | **Csütörtök** | Hét második fele — hétvégi főzéshez időzítve |
| Cutoff idő | **Szerda 20:00** | 18-20 óra a szállítás előtt (csomagolási idő) |
| Szállítási ablak | **14:00-18:00** | Délutáni kiszállítás |
| Minimum indítási küszöb | **Nincs (Phase 1)** | Pilot alatt MINDEN rendelés kiszállításra kerül — befektetés. Phase 2-től: 5-8 rendelés. |

### 3.3 Falusi ambassador modell

A falvakban egy helyi bizalmi személy (boltosné, postás, ismerős) segíti a rendeléseket:

- Összegyűjti a telefonos rendeléseket az idősebb vásárlóktól
- Átadási pont (nála lehet átvenni a csomagot)
- Kis jutalék vagy ingyenes szállítás fejében
- QR kódos plakátot kihelyezi a boltban/postán

---

## 4. UI specifikáció — Screenek

> **Cél:** A specifikáció alapján UI wireframe-ek tervezhetők.

### 4.1 Screen lista

| # | Screen | Leírás | Prioritás |
|---|--------|--------|-----------|
| S1 | **Kiszállítási kör választó (hibrid)** | Kosárban — GPS-javaslat + 2 gomb (Udvarhely / Keresztúri kör) + checkout település-validáció | P0 |
| S2 | **Route info banner** | Főoldalon/kosárban: "A te településedre csütörtökön szállítunk" | P0 |
| S3 | **Checkout — szállítási info** | Checkout flow-ban a settlement-specifikus info (nap, idő, cutoff, díj) | P0 |
| S4 | **Cutoff visszaszámlálás** | "Rendelési határidő: szerda 20:00 — még X óra Y perc" | P1 |
| S5 | **Route nem indul értesítés** | Phase 2: Ha < min. rendelés -> "Sajnos ezen a héten..." card | P2 (Phase 2) |
| S6 | **Admin: Zone kezelés** | Settlement -> zone hozzárendelés, route nap, cutoff beállítás | P0 |
| S7 | **Admin: Route összesítő** | Csütörtök reggel: hány rendelés, melyik település, összesítés | P1 |

### 4.2 S1 — Település-választó (részletes)

**Mikor jelenik meg:**
- Első regisztráció után (onboarding)
- Profil szerkesztésben (bármikor módosítható)
- Ha GPS-alapú detekció nem egyezik mentett településsel

**Wireframe:**

```
+-----------------------------------------------+
|                                                |
|  [pin] Hol szeretnéd átvenni a rendelésed?     |
|                                                |
|  +---------------------------------------+     |
|  | Válassz települést...              [v] |     |
|  +---------------------------------------+     |
|                                                |
|  Elérhető települések:                         |
|                                                |
|  [city] Székelyudvarhely (másnapi szállítás)   |
|  [village] Cristuru Secuiesc (csütörtök)       |
|  [village] Mugeni / Bögöz (csütörtök)          |
|  [village] Porumbenii Mari (csütörtök)         |
|  [village] Siménfalva (csütörtök)              |
|  [village] ... (további települések)           |
|                                                |
|  +---------------------------------------+     |
|  | Nem találom a településem ->           |     |
|  | Írj nekünk, bővítjük a körzetet       |     |
|  +---------------------------------------+     |
|                                                |
|            [ Mentés ]                          |
|                                                |
+-----------------------------------------------+
```

**Logika:**
- Város (Udvarhely) = másnapi / aznapi szállítás (meglévő modell)
- Falu = fix nap + szállítási ablak megjelenítés
- "Nem találom" -> feedback form (várólistára kerül -> bővítési input)
- GPS fallback: Ha elérhető, automatikusan javasol egy települést, de a user bármikor átírhatja

### 4.3 S2 — Route info banner

**Megjelenik:** Főoldal teteje + Kosár oldal teteje (ha a user falusi settlement-en van)

```
+--------------------------------------------------+
| [truck] Csütörtökön szállítunk a településedre!   |
|    Rendelési határidő: szerda 20:00               |
|    [clock] Még 2 nap 4 óra a határidőig           |
+--------------------------------------------------+
```

**Variációk:**
- **Cutoff előtt:** zöld banner, visszaszámláló
- **Cutoff után:** szürke banner: "A következő szállítás jövő csütörtökön. Rendelj szerda 20:00-ig!"
- **Route nem indul:** narancs banner: "Ezen a héten sajnos nem indult járat. A rendelésed a következő hétre kerül."

### 4.4 S3 — Checkout szállítási info (falu)

A meglévő checkout flow-ba beépülő settlement-specifikus blokk:

```
+--------------------------------------------------+
|  [truck] Szállítási részletek                     |
|                                                   |
|  [pin] Település: Mugeni / Bögöz                  |
|     [Módosítás]                                   |
|                                                   |
|  [calendar] Szállítási nap: Csütörtök, máj. 8    |
|  [clock] Szállítási ablak: 14:00 - 18:00          |
|  [box] Átadási pont: ___________________          |
|     (cím vagy ambassador neve)                    |
|                                                   |
|  -------------------------------------------------|
|                                                   |
|  Kosár összesen:           95 RON                 |
|  Szállítási díj:           15 RON                 |
|  ----------------------------                     |
|  [bulb] Még 25 RON és INGYENES a csütörtöki szállítás!       |
|                                                   |
|  Fizetés: [cash] Készpénz átvételkor              |
|                                                   |
|            [ Rendelés leadása ]                   |
|                                                   |
+--------------------------------------------------+
```

**Fontos UI elemek:**
- **Threshold nudge:** Ha kosár < 200 RON -> "Még X RON és ingyenes a csütörtöki szállítás!" + ajánlott termékek
- **Cutoff figyelmeztetés:** Ha közel a cutoff -> piros badge: "Még 2 óra a határidőig!"
- **Átadási pont:** Szabad szöveges mező VAGY ambassador-lista dropdown (ha van beállítva)

### 4.5 S5 — Route nem indul értesítés

```
+--------------------------------------------------+
|  [warning] Sajnos ezen a héten nem indult járat   |
|  a te településedre.                              |
|                                                   |
|  A rendelésed automatikusan átkerült a            |
|  következő hétre (csütörtök, máj. 15).            |
|                                                   |
|  [button: Rendelés megtartása]                    |
|  [link: Rendelés törlése]                         |
|                                                   |
|  Tipp: Oszd meg a linket a szomszédaiddal,        |
|  hogy minél többen rendeljünk!                    |
|  [button: Link megosztása]                        |
+--------------------------------------------------+
```

### 4.6 S6 — Admin: Zone kezelés

```
+--------------------------------------------------+
|  [gear] Szállítási zónák kezelése                 |
|                                                   |
|  [ + Új zóna hozzáadása ]                         |
|                                                   |
|  +-- Route 1: Udvarhely-Cristuru kör -----------+|
|  |                                               ||
|  |  Szállítási nap: Csütörtök                    ||
|  |  Ablak: 14:00-18:00                           ||
|  |  Cutoff: Szerda 20:00                         ||
|  |  Min. rendelés induláshoz: 8                  ||
|  |  Ingyenes szállítás: >= 200 RON               ||
|  |  Szállítási díj alatta: 15 RON               ||
|  |                                               ||
|  |  Települések:                                 ||
|  |  [x] Feliceni    [x] Taureni    [x] Mugeni   ||
|  |  [x] Dejutiu     [x] Porumbenii Mari          ||
|  |  [x] Porumbenii Mici  [x] Betesti            ||
|  |  [x] Cristuru Secuiesc                        ||
|  |  [x] Ruganesti   [x] Simonesti               ||
|  |  [x] Cobatesti   [x] Mihaileni               ||
|  |  [x] Morareni    [x] Bulgareni               ||
|  |                                               ||
|  |  [Szerkesztés]  [Route szüneteltetése]        ||
|  +-----------------------------------------------+|
|                                                   |
|  +-- Városi zóna: Székelyudvarhely -------------+|
|  |  Típus: Másnapi szállítás                     ||
|  |  [Szerkesztés]                                ||
|  +-----------------------------------------------+|
+--------------------------------------------------+
```

### 4.7 S7 — Admin: Route összesítő (szállítás napján)

```
+--------------------------------------------------+
|  [truck] Route összesítő — Csütörtök, máj. 8     |
|                                                   |
|  Státusz: [check] INDUL (12 rendelés)             |
|  Össz. forgalom: 1.440 RON                        |
|  Becsült OPEX: 220 RON                            |
|  Margin: +1.220 RON                               |
|                                                   |
|  --- Települések szerinti bontás ---------------  |
|                                                   |
|  [pin] Mugeni (3 rendelés) — 420 RON              |
|     Kovács Anna — 150 RON — [check] Becsomagolva  |
|     Nagy Béla — 120 RON — [wait] Csomagolásra vár |
|     Szabó Mária — 150 RON — [wait] Csomagolásra vár|
|                                                   |
|  [pin] Cristuru Secuiesc (5 rendelés) — 680 RON   |
|     ...                                           |
|                                                   |
|  [pin] Siménfalva (2 rendelés) — 190 RON          |
|     ...                                           |
|                                                   |
|  [pin] Mihăileni (2 rendelés) — 150 RON           |
|     ...                                           |
|                                                   |
|  -------------------------------------------------|
|  [ [print] Nyomtatás ]  [ [phone] Sofőrnek küldés ]|
+--------------------------------------------------+
```

---

## 4A. Részletes funkcionális leírás — User Flow-k

> **Ez a szekció a képernyőtervezés (impeccable) alapdokumentuma.**
> Minden flow lépésről-lépésre leírja, hogy mit lát a felhasználó, milyen állapotváltozások történnek, és milyen edge case-ek kezelendők.

---

### F1. Kiszállítási kör választás — Hibrid modell (v1.4)

> **v1.4 változás:** A település dropdown/bottom sheet helyett **hibrid GPS-javaslat + 2 gombos kiszállítási kör választó + checkout település-validáció**. Forrás: `brainstorm/brainstorm_zona-detektacio.md` v3 szintézis (ChatGPT + Perplexity + Szabolcs konszenzus, 2026-05-03).

#### Alapelv

> **A GPS segítsen, de ne döntsön.** A GPS előjavasolja a zónát, a user megerősíti vagy felülírja, a checkout település-alapon validálja.

#### F1.1 Kosár — zónaválasztás (első alkalom)

**Trigger:** User a kosárba lép, de nincs még `selected_delivery_zone` mentve.

**A) GPS engedélyezve (80-90% usernek eltalálja):**

```
+-----------------------------------------------+
|                                                |
|  [pin] Helyzet alapján ezt javasoljuk:         |
|                                                |
|  Udvarhely — napi kiszállítás                  |
|  150 RON felett ingyenes                       |
|                                                |
|  [ Ezt választom ]                             |
|  [ Másik kiszállítási kört választok ]         |
|                                                |
+-----------------------------------------------+
```

- A GPS NEM automatikusan beállítja a zónát — hanem **javaslatot tesz**, amit a user megerősít
- Ha a user "Ezt választom"-ot nyom → zóna mentve, Savings Engine frissül
- Ha "Másik kört választok" → a B) nézet jelenik meg

**B) GPS nem engedélyezve / megtagadva / nem elérhető:**

```
+-----------------------------------------------+
|                                                |
|  [truck] Kiszállítási kör kiválasztása         |
|                                                |
|  A szállítási díj és az ingyenes kiszállítás   |
|  határa attól függ, hova kéred a rendelést.    |
|                                                |
|  [ Udvarhely — napi kiszállítás ]              |
|    150 RON felett ingyenes, egyébként 10 RON   |
|                                                |
|  [ Keresztúri kör — csütörtöki kiszállítás ]   |
|    200 RON felett ingyenes, egyébként 15 RON   |
|                                                |
|  vagy                                          |
|                                                |
|  [ Helyzet alapján javaslat kérése ]           |
|    (GPS engedélyezés szükséges)                |
|                                                |
+-----------------------------------------------+
```

- A "Helyzet alapján javaslat kérése" gomb = GPS engedélykérés trigger (opcionális)
- Itt a GPS csak **harmadik opció**, nem automatikus felugró

**Fontos UX szabály:** Ha nincs zóna kiválasztva, a Savings Engine NE mutasson hamis thresholdöt. Ehelyett: "Válassz kiszállítási kört, és megmutatjuk, mennyi hiányzik az ingyenes szállításhoz."

#### F1.2 Kosár — zóna kiválasztva (persistent state)

```
+-----------------------------------------------+
|  Kiszállítás: Udvarhely — napi                 |
|  150 RON felett ingyenes                       |
|  [Módosítás]                                   |
+-----------------------------------------------+
```

vagy:

```
+-----------------------------------------------+
|  Kiszállítás: Keresztúri kör — csütörtök       |
|  200 RON felett ingyenes                       |
|  [Módosítás]                                   |
+-----------------------------------------------+
```

- A "Módosítás" link → B) nézet (2 gombos választó) megjelenik újra
- A kiválasztás mentésre kerül: `localStorage` + user profil (ha be van jelentkezve)
- Visszatérő vásárlónál automatikusan előtöltődik — nem kell újra választani

#### F1.3 Checkout — település-validáció (biztonsági háló)

**Trigger:** Checkout-nál a user megadja a szállítási címet és települést.

**Ha a település EGYEZIK a kosárban választott körrel:** Semmi extra — normál checkout flow.

**Ha a település NEM EGYEZIK:**

```
+-----------------------------------------------+
|  [warning] Szállítási kör eltérés              |
|                                                |
|  A kosárban Udvarhelyi kiszállítást             |
|  választottál, de a megadott település          |
|  (Betfalva) a Keresztúri körhöz tartozik.      |
|                                                |
|  A szállítási feltételek módosulnak:            |
|  - szállítás: csütörtök                        |
|  - ingyenes határ: 200 RON                     |
|  - díj: 15 RON                                 |
|                                                |
|  [ Frissítés Keresztúri körre ]                |
|  [ Cím javítása ]                              |
|                                                |
+-----------------------------------------------+
```

**Logika:**
- Település → zóna mapping egy egyszerű lookup tábla (nem geocode!)
- Ha a checkout település a Keresztúri régió 14 településeinek egyike → Keresztúri kör
- Ha Székelyudvarhely → Városi kör
- Ha egyik sem → "Sajnos erre a településre még nem szállítunk" hibaüzenet

#### F1.4 GPS implementációs részletek

**Mikor kérjük a GPS engedélyt:**
- NEM első belépéskor (túl korai, privacy-súrlódás)
- NEM automatikusan (félreérthető)
- A kosárban, amikor a user kontextusban van (szállítási kör választás)
- CSAK ha a user rákattint a "Helyzet alapján javaslat kérése" gombra (Phase 1)
- Phase 2-ben: automatikus javaslat, ha korábban engedélyezte

**GPS → zóna mapping:**
- Udvarhely város koordináta-körzete (pl. 5 km sugár) → Városi kör
- Minden más a route mentén → Keresztúri kör
- Ismeretlen terület → fallback a 2 gombos választóra

**GPS hibakezelés:**
- Engedély megtagadva → 2 gombos választó (B nézet)
- Pontatlan pozíció (accuracy > 5km) → 2 gombos választó + "Nem voltunk biztosak a helyzeted alapján"
- Timeout (>5s) → 2 gombos választó

#### F1.5 Fázisolás

| Feature | Phase 1 (Sprint 4 MVP) | Phase 2 (Sprint 5 / v0.4) |
|---------|----------------------|--------------------------|
| 2 gombos kiszállítási kör választó | ✅ | ✅ |
| GPS-javaslat gomb (user-initiated) | ✅ | ✅ |
| Automatikus GPS-javaslat (returning user) | ❌ | ✅ |
| Checkout település-validáció | ✅ (egyszerű lookup) | ✅ (bővített) |
| Zóna mismatch figyelmeztetés | ✅ | ✅ |
| localStorage mentés | ✅ | ✅ |
| User profil mentés | ❌ (nincs auth a kosárnál) | ✅ |

#### F1.6 Adatmodell

```
DeliveryZone:
  id: "urban" | "keresztur_region"
  label: "Udvarhely" | "Keresztúri kör"
  delivery_fee: 10 | 15
  free_shipping_threshold: 150 | 200
  delivery_schedule: "napi" | "csütörtök"
  settlements: ["Székelyudvarhely"] | ["Feliceni", "Tăureni", "Mugeni", ...]

UserDeliveryPreference:
  selected_zone: "urban" | "keresztur_region"
  source: "gps_suggestion" | "manual_selection" | "checkout_correction"
  last_updated: ISO date
```

#### F1.7 Edge case-ek

| Eset | Viselkedés |
|------|-----------|
| GPS Udvarhelyen, de user Keresztúri kört választ | OK — user döntés felülírja a GPS-t |
| GPS falusi, user elfogadja, checkout cím = Udvarhely | Mismatch figyelmeztetés (F1.3) |
| User nem választ kört és checkout-ra megy | Checkout blokkolva: "Először válaszd ki a kiszállítási kört" |
| Visszatérő vásárló (localStorage-ban van zóna) | Auto-fill, nem kérdezünk újra |
| Település nem szerepel egyik körben sem | "Sajnos erre a településre még nem szállítunk. Írd meg nekünk, és bővítjük a körzetet!" |

---

### F2. Route info banner — kontextuális tájékoztatás

#### F2.1 Banner megjelenése és elhelyezése

**Megjelenik:** Kizárólag Keresztúri régió felhasználóknak. Városi felhasználóknak NEM jelenik meg.

**Pozíció:** Főoldal — a kategória tab-ok FELETT, sticky. Kosár oldal — a tételek FELETT.

#### F2.2 Banner állapotok (4 állapot)

| Állapot | Mikor | Szín | Szöveg | Ikon |
|---------|-------|------|--------|------|
| **Aktív — nyitott** | Cutoff előtt, van még idő (>24h) | Zöld háttér | "Csütörtökön szállítunk [település]-re! Rendelj szerda 20:00-ig." | 🚚 |
| **Aktív — sürgős** | Cutoff előtt, kevesebb mint 24 óra | Narancs háttér | "⏰ Még [X óra Y perc] a rendelési határidőig!" | ⏰ |
| **Zárt — cutoff lejárt** | Cutoff után, szállítás napja előtt | Szürke háttér | "A következő szállítás jövő csütörtökön. Rendelj szerda 20:00-ig!" | 📅 |
| **Zárt — route nem indul** | Admin törölte/postponed a route-ot | Piros háttér | "Ezen a héten sajnos nem indul járat. A következő lehetőség: [dátum]." | ⚠️ |

#### F2.3 Visszaszámláló logika

- A visszaszámláló a **cutoff időponthoz** képest számol (szerda 20:00)
- Formátum:
  - Ha > 24 óra: "2 nap 4 óra" (óra pontossággal)
  - Ha 1-24 óra: "14 óra 32 perc" (perc pontossággal, narancs szín)
  - Ha < 1 óra: "42 perc" (perc, piros, pulzáló animáció)
- A számláló **kliens-oldalon frissül** (setInterval, 60 másodpercenként)
- Ha eléri a 0-t → automatikusan "Zárt" állapotra vált (oldal újratöltés nélkül)

---

### F3. Termékböngészés — falusi felhasználó perspektíva

#### F3.1 Termékoldal különbségek (falu vs. város)

A termékoldal (főoldal) **NEM változik** a falusi felhasználónál. Ugyanaz a 37 termék, ugyanazok a kategóriák, ugyanaz az ár. A különbség:

1. **Route info banner** a tetején (F2)
2. **Savings engine threshold:** 200 RON (Keresztúri régió) vs. 150 RON (Városi régió) az ingyenes szállításhoz
3. A progress bar szövege adaptálódik: "Még X RON és INGYENES a csütörtöki szállítás!"
4. Ha cutoff lejárt → a "Kosárba" gomb továbbra is aktív (a rendelés a következő hétre szól)

#### F3.2 Savings engine adaptáció

| Paraméter | Városi régió | Keresztúri régió |
|-----------|-------------|-----------------|
| Ingyenes szállítás küszöb | 150 RON | 200 RON |
| 2% kedvezmény küszöb | 300 RON | 300 RON (változatlan) |
| Progress bar szöveg | "Ingyenes szállítás 150 RON-tól" | "Ingyenes csütörtöki szállítás 200 RON-tól" |
| Szállítási díj (ha küszöb alatt) | 10 RON | 15 RON |
| Szállítás | Minden nap | Csütörtök 14:00–18:00 |
| Rendelési határidő | Nincs (aznap/másnap) | Szerda 20:00 |

---

### F4. Kosár — falusi adaptáció

#### F4.1 Kosár oldal kiegészítések

A meglévő kosár layout megmarad. Kiegészítések falusi felhasználóknál:

1. **Route info banner** a tetején (kompakt verzió — 1 soros)
2. **Szállítási összesítő blokk** a tételek alatt:
   ```
   Település: Mugeni / Bögöz  [Módosítás]
   Szállítási nap: Csütörtök, máj. 8.
   Szállítási ablak: 14:00 – 18:00
   ```
3. **Threshold nudge** ha kosár < 200 RON (Keresztúri régió):
   > "Még 25 RON és INGYENES a szállítás! 👇"
   > Alatta: 2-3 ajánlott termék kártya (legolcsóbb, ami átlöki a küszöböt)

#### F4.2 Cutoff kezelés a kosárban

- **Cutoff előtt:** Normál "Tovább a fizetéshez" gomb
- **Cutoff után, de van nyitott kosár:**
  - A gomb szövege változik: "Rendelés a következő csütörtökre →"
  - Info szöveg: "A rendelési határidő lejárt. A rendelésed a következő csütörtöki szállításra szól (máj. 15.)"
- **Cutoff után, üres kosár:** Normál állapot, a banner jelzi a következő lehetőséget

---

### F5. Checkout flow — falusi szállítás

#### F5.1 Checkout lépések (falu)

A checkout flow **egy képernyő** (nem multi-step wizard). Felépítés felülről lefelé:

**1. blokk — Szállítási adatok**
```
📍 Település: Mugeni / Bögöz          [Módosítás]
📅 Szállítás: Csütörtök, 2026. május 8.
🕑 Időablak: 14:00 – 18:00
```

**2. blokk — Átadási pont** (ÚJ mező — csak falusi rendelésnél!)
```
📦 Átadási pont
[___________________________________]
Pl. "Fő utca 42." vagy "Kis Boltja előtt"

💡 Ha nem adod meg, a sofőr telefonon egyeztet.
```
- Szabad szöveges mező (nem kötelező, de ajánlott)
- Ha a településen van ambassador → automatikus javaslat: "Javasolt átadási pont: [Ambassador neve] — [cím]"
- A felhasználó felülírhatja

**3. blokk — Rendelés összesítő**
```
Termékek (4 tétel):                 385 RON
Szállítási díj:                    INGYENES ✅
─────────────────────────────────
Összesen:                           385 RON
```

**4. blokk — Fizetési mód**
```
💵 Készpénz átvételkor
   (Online fizetés hamarosan elérhető)
```

**5. blokk — Megjegyzés** (opcionális)
```
📝 Megjegyzés a rendeléshez
[___________________________________]
```

**6. blokk — CTA**
```
[ Rendelés leadása – 385 RON ]
```

#### F5.2 Rendelés leadása — mi történik

1. User megnyomja a "Rendelés leadása" gombot
2. A rendszer:
   - Rögzíti a rendelést ("Új" státusszal)
   - Hozzárendeli a megfelelő szállítási zónához
   - Kiszámolja a szállítási díjat (200 RON felett ingyenes)
   - Beállítja a szállítási dátumot (a zóna alapján: következő csütörtök)
3. Siker → "Rendelés visszaigazolás" képernyő (F6)
4. Hiba → inline hibaüzenet (nem modal, retry lehetőséggel)

#### F5.3 Checkout edge case-ek

| Eset | Viselkedés |
|------|-----------|
| Cutoff lejárt rendelés közben | A rendelés a **következő hétre** szól — a checkout dátum automatikusan frissül, info banner jelzi |
| Settlement megváltozott checkout közben | Szállítási blokk újraszámol (díj, dátum, ablak) |
| Kosár < minimum? | Nincs kosár minimum a falusi route-nál — de 200 RON alatt szállítási díj van (15 RON) |
| Ambassador átadási pont kitörlése | Üres mező OK — sofőr telefonon egyeztet |
| Hálózati hiba küldéskor | Retry gomb + "A rendelés nem ment át. Próbáld újra." |

---

### F6. Rendelés visszaigazolás (falu)

**Megjelenik:** Sikeres rendelés leadása után.

**Tartalom:**
```
✅ Rendelésed megkaptuk!

Rendelésszám: #DH-2026-0142
Szállítás: Csütörtök, 2026. május 8.
Időablak: 14:00 – 18:00
Település: Mugeni / Bögöz
Átadási pont: Fő utca 42.

Összeg: 385 RON (készpénz átvételkor)

📞 Szállítás napján a sofőr hív, mielőtt odaér.

[Rendeléseim megtekintése]
[Vissza a termékekhez]
```

**Speciális elem (Phase 2-től):** Ha a route indulása még nem garantált (< min. rendelés):
> "ℹ️ A szállítás akkor indul, ha elegendő rendelés összegyűlik. Szerda este értesítünk!"

> **Phase 1 (pilot):** Ez az elem NEM jelenik meg — minden rendelés kiszállításra kerül.

---

### F7. Rendelés státusz — falusi rendelés életciklusa

#### F7.1 Státusz-flow (falusi rendelés)

```
Új  →  Megerősítve  →  Előkészítés alatt  →  Úton  →  Kézbesítve
 │                                                          │
 │         ┌──── Route nem indul ────┐                      │
 └─────→  Elhalasztva (→ következő hét)                     │
           │                                                │
           └─── User törli ──→ Törölve                      │
                                                            │
                                              Kézbesítve ───→ (másnap) "Hogy ízlett?" push
```

| Státusz | Mikor | User lát | Admin lát |
|---------|-------|----------|-----------|
| **Új** | Rendelés leadva, cutoff előtt | "Rendelésed rögzítve" | Új rendelés a listán |
| **Megerősítve** | Cutoff lejárt + route INDUL (≥8 rendelés) | "Csütörtökön szállítjuk!" | Route összesítőben "Megerősítve" |
| **Elhalasztva** | Phase 2: Cutoff lejárt + route NEM INDUL (< min.) | F8 értesítés: "Sajnos nem indul..." | "Elhalasztva" badge |
| **Előkészítés alatt** | Admin megkezdi a csomagolást | "Csomagodat készítjük" | Mészáros: csomagolási lista |
| **Úton** | Sofőr elindult | "A sofőr úton van!" | Futár: kiszállítási lista |
| **Kézbesítve** | Sofőr megjelölte | "Rendelésed kézbesítve ✅" | Done |
| **Törölve** | User vagy admin törölte | "Rendelésed törölve" | Törölve |

#### F7.2 Rendeléseim lista — falusi kiegészítések

A "Rendeléseim" oldalon minden rendelés kártyáján:
- **Szállítási nap** kiemelve (nem "holnap", hanem "Csütörtök, máj. 8.")
- **Település** megjelenítve
- Ha státusz = "Elhalasztva": narancs badge + "Áttéve: máj. 15."
- **Újrarendelés gomb** — ugyanaz mint a városi (basket loader)

---

### F8. Route nem indul — értesítés és kezelés

> **⚠️ Phase 1 (pilot) alatt ez a flow NEM aktív.** Pilot alatt minden rendelés kiszállításra kerül, függetlenül a rendelésszámtól. Ez a szekció Phase 2-től releváns, amikor bevezetjük a minimum küszöböt.

#### F8.1 Trigger

**Mikor:** Phase 2-től — Szerda 20:00 (cutoff) után a rendszer lefuttatja a `check_route_dispatch()` függvényt.
Ha az adott zone-ban kevesebb mint a beállított minimum rendelés van → route NEM INDUL.

#### F8.2 User értesítés

**Push notification** (ha engedélyezve):
> "Sajnos ezen a héten nem indult járat [település]-re. A rendelésed a következő hétre került."

**In-app értesítés** (Rendeléseim oldalon):
```
⚠️ Ezen a héten nem indult járat

A rendelésed automatikusan átkerült a következő
csütörtökre (május 15.).

[Rendelés megtartása]     [Rendelés törlése]

💡 Tipp: Oszd meg az appot a szomszédaiddal,
   hogy minél többen rendeljünk!
   [Link megosztása 📤]
```

#### F8.3 Háttérfolyamat

1. Cutoff lejárta után a rendszer automatikusan ellenőrzi a rendelésszámot
2. Ha Phase 2-ben vagyunk és kevesebb mint a minimum:
   - Érintett rendelések státusza → "Elhalasztva"
   - Szállítási dátum → következő hét csütörtök
   - Push értesítés minden érintett felhasználónak
   - Admin értesítés: "Route nem indul — X rendelés elhalasztva"
3. A felhasználó bármikor törölheti az elhalasztott rendelést (nincs kötbér)


---

### F9. Mészáros/Futár interfész — falusi route kiegészítések

#### F9.1 Mészáros: Előkészítés tab

A meglévő "Előkészítés" tab-on a rendelések **settlement szerint csoportosítva** jelennek meg (nem egyenként):

```
── Csütörtöki Route: 2026. május 8. ──────────

📍 Mugeni / Bögöz (3 rendelés)
   □ Kovács Anna — 2.5 kg csirkemell, 1 kg kolbász...  [Részletek]
   □ Nagy Béla — 1 kg sertéskaraj...                   [Részletek]
   □ Szabó Mária — Családi csomag (L)...               [Részletek]

📍 Cristuru Secuiesc (5 rendelés)
   □ ...

📍 Siménfalva (2 rendelés)
   □ ...

── Összesítő ──────────────────────────────────
12 rendelés | 1.440 RON | 14 tétel összesen

[Minden becsomagolva ✅]
```

**Működés:**
- Checkbox-szal jelöli az egyes rendelések csomagolását
- "Minden becsomagolva" → összes rendelés státusza: `Előkészítés alatt` → `Úton` (ha a sofőr is ő)
- Nyomtatható csomagolási lista (print-optimized CSS)

#### F9.2 Futár: Kiszállítás tab — route mód

A "Kiszállítás" tab-on **route-sorrend** szerint rendezve jelennek meg a települések:

```
── Route: Udvarhely → Cristuru kör ──────────

1. 📍 Feliceni (1 csomag)
   Kovács Péter — Fő u. 12. — 120 RON (készpénz)
   [📞 Hívás]  [✅ Kézbesítve]

2. 📍 Mugeni (3 csomag)
   Kovács Anna — Fő utca 42. — 150 RON
   [📞 Hívás]  [✅ Kézbesítve]
   Nagy Béla — Ambassador: Kis Boltja — 120 RON
   [📞 Hívás]  [✅ Kézbesítve]
   Szabó Mária — Iskola melletti ház — 115 RON + 15 RON szállítás
   [📞 Hívás]  [✅ Kézbesítve]

3. 📍 Cristuru Secuiesc (5 csomag)
   ...

── Haladás: 1/12 kézbesítve ─── [████░░░░░] 8%
```

**Működés:**
- A települések az útvonal sorrendjében (nem ABC)
- Minden csomagnál: telefonszám + átadási pont + összeg
- "Kézbesítve" gomb → státusz váltás + GPS timestamp rögzítés
- Haladás-sáv alul (motiváció — "mennyi van hátra")
- Ha nincs válasz a telefonra → "Nem elérhető" opció → admin értesítés

#### F9.3 Admin: Route összesítő dashboard

**Mikor látható:** Szállítási napon (csütörtök) reggeltől.
**Hol:** Admin > Szállítás > Route összesítő (új menüpont)

**Tartalom:**
```
Route: Udvarhely–Cristuru kör | Csütörtök, máj. 8.

Státusz: ✅ INDUL (12 rendelés — min. 8 teljesült)
Forgalom: 1.440 RON | OPEX: ~190 RON | Nettó: ~1.250 RON

Települések:
  Mugeni          3 rendelés   420 RON   ✅ Mind csomagolva
  Cristuru Sec.   5 rendelés   680 RON   ⏳ 3/5 csomagolva
  Siménfalva      2 rendelés   190 RON   ⏳ 0/2 csomagolva
  Mihăileni       2 rendelés   150 RON   ⏳ 0/2 csomagolva

[📄 Csomagolási lista nyomtatása]
[📱 Route indítása (sofőr értesítés)]
```

---

### F10. Mérendő események (Analytics)

A falusi route-hoz kapcsolódó kulcs-események, amiket mérni kell:

| Esemény | Mikor |
|---------|-------|
| Település kiválasztás | User kiválaszt egy települést |
| Route banner látható | Falusi banner megjelenik |
| Falusi rendelés leadva | Rendelés a route-on |
| Rendelés elhalasztva | Route nem indult (Phase 2) |
| Rendelés törölve | User törli az elhalasztott rendelést |
| Route elindult | Sofőr elindul |
| Összes kézbesítés kész | Route befejezve |
| Sürgős banner látható | Cutoff < 24 óra |
| Megosztás link koppintás | User megosztja az appot |


---

### F11. Integrációs pontok a meglévő app-pal

#### F11.1 Módosítandó meglévő képernyők

| Képernyő | Módosítás | Hatás |
|----------|-----------|-------|
| **Regisztráció / Onboarding** | + Település-választó lépés (F1) | Új bottom sheet |
| **Főoldal** | + Route info banner (F2), + threshold adaptáció | Banner + progress bar szöveg |
| **Termék részletek** | + "Csütörtökön szállítjuk!" badge (ha falu) | Kis kiegészítés |
| **Kosár** | + Szállítási info blokk (F4), + threshold 120→150 fork | Új blokk + logika |
| **Checkout** | + Átadási pont mező (F5), + dátum/ablak megjelenítés | Módosított layout |
| **Rendelés visszaigazolás** | + Route-specifikus info (F6) | Szöveg adaptáció |
| **Rendeléseim** | + Település, szállítási nap, "Elhalasztva" badge (F7) | Kártya kiegészítés |
| **Profil** | + "Település" menüpont | Új sor + bottom sheet |
| **Mészáros: Előkészítés** | + Settlement-csoportosítás (F9.1) | Lista átstrukturálás |
| **Futár: Kiszállítás** | + Route-sorrend mód (F9.2) | Lista átstrukturálás |

#### F11.2 Új képernyők / komponensek

| Komponens | Típus | Prioritás |
|-----------|-------|-----------|
| Settlement picker bottom sheet | Shared component | P0 |
| Route info banner | Shared component | P0 |
| Checkout — átadási pont mező | Inline component | P0 |
| Route nem indul értesítés | Card component | P1 |
| Admin: Route összesítő | Új oldal | P1 |
| Admin: Zone kezelés | Új oldal | P0 |

#### F11.3 Nem módosuló képernyők

Ezek változatlanok maradnak:
- Bejelentkezés / Jelszó reset
- Termék részletek (csak egy badge kiegészítés)
- Family Bundles (ugyanúgy működik falu/város)
- Kedvencek (v0.5)
- Savings recap (Sprint 3 feature — zone-agnosztikus)

---

### F12. Konfigurálhatóság és admin-kontroll

#### F12.1 Admin által módosítható paraméterek

| Paraméter | Hol | Default |
|-----------|-----|---------|
| Szállítási nap | Zone settings | Csütörtök |
| Cutoff idő | Zone settings | Szerda 20:00 |
| Szállítási ablak | Zone settings | 14:00–18:00 |
| Minimum rendelés (route indulás) | Zone settings | 0 (pilot) / 8 (scaling) |
| Ingyenes szállítás küszöb | Zone settings | 200 RON (Keresztúri) / 150 RON (Városi) |
| Szállítási díj | Zone settings | 15 RON |
| Település lista | Zone > Settlements | 14 település |
| Ambassador adatok | Settlement > Ambassador | Név + telefon + cím |
| Route aktív/szünetel | Zone settings | Aktív |

#### F12.2 Zone szüneteltetés

Az admin **egy gombbal** szüneteltetheti a route-ot (szabadság, ünnepnap, kapacitáshiány):
- "Route szüneteltetése" → összes érintett settlement banner: "Szünetel — nem szállítunk"
- Meglévő rendelések: admin értesítést kap, manuálisan kezeli (elhalasztás vagy visszamondás)
- Egy gombbal újraindítható

---

### F13. Biztonsági háló és fallback-ek

| Szituáció | Kezelés |
|-----------|---------|
| Felhasználó nem választott települést | Checkout blokkolva + bottom sheet megnyílik |
| Cutoff lejárt + user rendel | Rendelés a KÖVETKEZŐ hétre szól (auto-dátum) |
| Route nem indul (Phase 2, < min.) | Rendelés elhalasztva + push értesítés + törlési lehetőség. **Phase 1: nem releváns — mindig indul.** |
| Ambassador nincs a településen | Átadási pont = szabad szöveg (sofőr telefonon egyeztet) |
| Sofőr nem éri el a vásárlót | "Nem elérhető" → admin értesítés → manuális kezelés |
| Hálózati hiba rendeléskor | Retry + offline queue (PWA) |
| Settlement lista változik | Admin Zone kezelésben módosítja → instant érvényes |


---


## 5. Marketing — falusi bevezetés

### 6.1 Plakát / QR kód (faluként testreszabott)

```
+------------------------------------+
|                                    |
|   DEÁK HÚSMÍVES                    |
|   Friss hús az ajtódig!           |
|                                    |
|   Minden CSÜTÖRTÖKÖN szállítunk   |
|   [település neve]-re             |
|                                    |
|   +----------+                     |
|   |  QR kód  |  Rendelj online:   |
|   |          |  deakhus.ro         |
|   +----------+                     |
|                                    |
|   Rendelési határidő:             |
|   Szerda este 20:00               |
|                                    |
|   200 RON felett INGYENES szállítás|
|                                    |
+------------------------------------+
```

### 6.2 Ambassador toborzás

Faluként 1-2 bizalmi személy azonosítása:
- Helyi boltos, postás, falusi tanácsos
- Jutalék: ingyenes szállítás a saját rendeléseire
- Feladat: plakát kihelyezés, telefonos rendelés segítés, átadási pont biztosítás

### 6.3 Csatornák (prioritás sorrendben)

| Csatorna | Prioritás | Megjegyzés |
|----------|-----------|------------|
| **Falusi ambassador** | P0 | Helyi bizalmi személy |
| **Plakát + QR** | P0 | Bolt, posta, templom |
| **Facebook csoportok** | P1 | Helyi csoportok (pl. "Székelykeresztúri boldog szülők") |
| **Szórólap a szállítással** | P1 | Minden csomagba 2-3 szórólap a szomszédoknak |
| **Személyes bemutató** | P2 | Első route-on kóstoltatás |

---

## 6. Pilot terv — fázisok

### Phase 0: Előkészítés (1 hét)

- [ ] Deák kapacitás-check (bírják-e a heti +1 route csomagolást?)
- [ ] Sofőr azonosítás (meglévő vagy új?)
- [ ] 3 pilot település kiválasztása a route-ból
- [ ] Ambassador toborzás (1 fő/település)

### Phase 1: Soft launch (4-8 hét, heti 1 route, NINCS minimum küszöb)

- [ ] Settlement-választó + checkout flow fejlesztés
- [ ] Admin zone kezelés
- [ ] Plakátok + QR kódok nyomtatása
- [ ] Első route indítása (heti 1x csütörtök)
- [ ] Mérés: rendelésszám, AOV, visszatérés

### Phase 2: Bővítés (ha Phase 1 breakeven elérve)

- [ ] Route kiterjesztés teljes 14 településre
- [ ] Heti 2x szállítás (kedd + csütörtök)
- [ ] GPS-alapú település detekció
- [ ] Admin route összesítő dashboard

### Siker kritériumok

| KPI | Cél | Mérés |
|-----|-----|-------|
| Rendelés/route | >= 10 (breakeven) | Route összesítő |
| Visszatérő vásárló (30 nap) | >= 3 fő | Firebase analytics |
| AOV (Keresztúri régió) | >= 200 RON | Rendelés átlag |
| Route indulási arány | 100% (pilot: mindig indul ha van rendelés) | Dispatch log |
| Ambassador aktivitás | >= 1 fő aktívan segít | Manuális tracking |

---

## 7. Ami NINCS benne (tudatosan)

- Automatikus route optimizer / útvonaltervező
- Térkép nézet az adminban (DH-48 backlogban)
- SMS/push értesítés a sofőrnek (DH-49)
- GPS tracking a szállítás közben
- Online fizetés (csak készpénz a pilot alatt)
- Több route párhuzamosan (Phase 2)
- Szezonális árazás a szállítási díjra

---

## 8. Kapcsolódó Jira ticketek

| Ticket | Kapcsolat |
|--------|-----------|
| **DH-184** | Ez a feature (Falusi Route Pilot MVP) |
| DH-161 | Timeslot kapacitás-limit — szükséges a route-hoz |
| DH-51 | Szállítási zóna korlátozás (Sprint 5 — teljesebb rendszer) |
| DH-48 | Térkép nézet (backlog — későbbi fázis) |
| DH-49 | SMS értesítés (backlog — későbbi fázis) |
| DH-173 | Termék testreszabás — független, de szinergia a falusi kosárral |

---

## 9. Döntésre vár (Szabolcs)

1. **Melyik 3 település legyen a Phase 1 pilot?** Javaslat: Cristuru Secuiesc + Mugeni + Siménfalva (legnagyobb + route mentén jól elosztva)
2. **A szállítási nap csütörtök jó?** Vagy másik nap lenne jobb operációs szempontból?
3. **Ki vezeti a szállítást?** Meglévő sofőr vagy új ember?
4. ~~120 RON threshold reális?~~ **ELDÖNTVE: 200 RON** (Szabolcs döntése, 2026-05-02)
5. **Cristuru Secuiesc (Székelykeresztúr) benne van-e?** Ez város, nem falu — más a pozicionálás, de a route mentén van
