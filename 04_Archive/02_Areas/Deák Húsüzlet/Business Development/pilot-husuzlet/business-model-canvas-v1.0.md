---
title: Business Model Canvas -- Deák Húsmíves Online Platform (Pilot)
version: 1.0
date: 2026-03-27
author: Becze Szabolcs -- Exar Labs
description: >
  BMC v1.0 -- comprehensive update incorporating all validated decisions, actual development
  data, brand strategy, product catalog, architecture, and cost projections. Co-venture model
  where Exar Labs owns platform, marketing, and business development (funded from own capital);
  butcher shop owns production, quality, and delivery; return via revenue share.
  Changes from v0.5: actual dev cost data (AI analysis), brand voice finalized, 37 products
  in 5 categories cataloged, architecture solidified (single PWA, Customer/Admin nézet),
  GDPR requirements added, marketing materials ready, adalékanyag USP validated by research.
---

# Business Model Canvas v1.0 -- Deák Húsmíves Online Platform (Pilot)

_Version: 1.0 | Last updated: 2026-03-27_
_Scope: This BMC models the online ordering pilot channel only -- not the full butcher shop operation. The goal is market validation and learning, not immediate profit maximization._

---

## 1. Customer Segments

Jelenleg nincs adat a meglévő vásárlókról. A pilot egyik fő célja feltérképezni, melyik online vásárlói profil reagál a legerősebben.

**Hipotetikus szegmensek:**

| Szegmens | Profil | Motiváció | Becsült méret |
|----------|--------|-----------|---------------|
| Családok | 30-55 év, rendszeresen főznek, 2-5 kg/vásárlás | Kényelmes heti/kétheti bevásárlás, házhozszállítás | Nagy |
| Egészségtudatosak | Adalékanyag-mentes, helyi termékeket keresők | Frissesség, nincs tartósítószer, bizalom a helyi termelőben | Közepes |
| Időszűkében lévő dolgozó családok | Nincs idő bolti vásárlásra | Időmegtakarítás, kiszámítható rendelés | Közepes |
| Korai digitális felhasználók | Nyitottak új vásárlási csatornákra | Új digitális szolgáltatás kipróbálása | Kicsi |

A termék **nem prémium** -- széles potenciál Székelyudvarhely ~30.000 lakosán belül.

Vásárlási típus: **tervezett** (heti/kétheti), nem impulzusvásárlás.

**Szegmens validáció a pilotban:** A DHOP-39 (KPI dashboard) és DHOP-42 (analytics) ticketek mérik, melyik szegmens regisztrál és rendel a legtöbbet. UTM tracking csatornánként (QR, Facebook, szájról szájra).

---

## 2. Value Proposition

### Végfelhasználónak (vásárló):

**#1 -- Frissesség** (fő megkülönböztető)
- Hajnalban dolgozzák fel, aznap kiszállítják
- Nem fagyasztott, nem tárolt -- friss, pont
- Más online hentes ezt nem mondhatja el

**#2 -- Adalékanyag-mentesség** (kutatással validált)
- Minden termék teljesen adalékanyag-mentesen készül
- Az ipari húskészítmények 10-20 féle adalékanyagot tartalmaznak (nitritek, foszfátok, ízfokozók, színezékek, töltőanyagok) -- a Deák Húsmíves termékeiben ezek egyike sincs
- Az adalékmentesség nem marketing fogás, hanem a logisztikából fakadó tény: a friss kiszállítási modell miatt nincs szükség tartósítószerre
- Részletes kutatás: `Marketing/kutatas_ipari_hus_adalekanyagok.md`

**#3 -- Kényelem**
- Online rendelés otthonról, nincs parkolás, nincs sorban állás
- Házhozszállítás Székelyudvarhely területén, időablakos kiszállítással

**#4 -- Garantált elérhetőség**
- Előrendeléssel biztosított mennyiség
- 37 termék, 5 kategória -- széles választék

**#5 -- Helyi bizalom**
- Ismert helyi üzlet, családi vállalkozás
- Nem multinacionális -- "a mi húsmívesünk"

### Co-venture partnernek (húsüzlet):

- Új bevételi csatorna **nulla előzetes befektetéssel és nulla operatív teherrel** -- csak termelniük és szállítaniuk kell
- Jobb készletgazdálkodás (előrendelések csökkentik a pazarlást)
- Hozzáférés vásárlói adatokhoz és vásárlási szokásokhoz (jelenleg semmi nem létezik)
- Pénzügyi átláthatóság -- először lesznek valódi értékesítési statisztikáik
- Professzionális marketing teljes egészében az Exar Labs által kezelve -- nincs szükség képességre vagy költségvetésre a részükről
- Operatív felület (Admin nézet) a mészáros és futár számára -- a telefonjukról kezelik a rendeléseket

### Márka pozicionálás (véglegesített):

**Fő headline:** „Hajnalban készül. Ma nálad."
**Al-headline:** „Rendelj online. Házhoz szállítjuk. Adalékanyag nélkül."
**Tagline:** „Friss. Tiszta. Házhoz."

A teljes brand voice dokumentáció: `Marketing/brand_voice.md`

---

## 3. Channels

| Csatorna | Szerep | Státusz |
|----------|--------|---------|
| Mobile-first PWA | Elsődleges rendelési felület (Vue 3 + Frappe) | Fejlesztés alatt (45% kész) |
| Bolti QR kód | Fő akvizíciós csatorna -- meglévő forgalmat konvertál online-ba | Várunk domain véglegesítésre |
| Szórólap (A5, nyomtatott) | Bolti osztogatás, házhozszállításkor melléklet | Nyomtatásra kész (v8-v9) |
| Facebook oldal | Kommunikáció, promóciók, rendelési infó | Várakozik launch-ra |
| Helyi Facebook csoportok | Természetes, ajánlás jellegű posztok | Tervezett |
| Szájról szájra | Magas bizalmú helyi közösség -- gyors organikus terjedés | Természetes |
| Boltablak poszter | Vizuális: egy sor + QR kód | Tervezett |

**Csatorna-specifikus hangnem:** Részletek a `Marketing/brand_voice.md` 6. szekciójában.

---

## 4. Customer Relationships

### Onboarding

**Súrlódásmentes regisztráció** -- 30-60 másodperc alatt teljesíthető.

| Auth módszer | Státusz | Megjegyzés |
|-------------|---------|------------|
| Google OAuth | Elsődleges (DHOP-8) | ~90% kész |
| Email + jelszó | Fallback (DHOP-10) | ~90% kész |
| Facebook OAuth | Opcionális / post-MVP (DHOP-9) | Nem blokkolja a launch-ot |

Gyűjtött adatok: név, telefonszám, szállítási cím (DHOP-11).

GDPR consent képernyő regisztráció után + adattörlési lehetőség a Contul meu oldalon (DHOP-68, DHOP-69 -- launch előtt kötelező).

### Folyamatos kapcsolat

- Közvetlen visszajelzés az első vásárlóktól (kvézi béta tesztelők)
- Rendszeres Facebook posztok: friss termékek, akciók, rendelési infó
- Személyes, közvetlen hangnem -- tegezés, őszinte, helyi
- Szórólap mellékelése a kiszállított rendelésekhez
- Admin email értesítés minden új rendelésről (DHOP-22); post-MVP: WhatsApp értesítés, SMS a vásárlónak (DHOP-48)

---

## 5. Revenue Streams

### Co-venture revenue share

**X% az online forgalomból az Exar Labs-nak.** _(Pontos % blokkolva -- pénzügyi adatok szükségesek a húsüzlettől.)_

Ez nem szolgáltatási díj -- ez az Exar Labs platformba, marketingbe és üzletfejlesztésbe fektetett tőkéjének megtérülése. A húsüzlet semmit nem fizet; az Exar Labs csak akkor keres, amikor a csatorna bevételt termel.

**Miért működik ez a modell (validált adatokkal):**

| Paraméter | Hagyományos ügynökség | Exar Labs (AI-vel) |
|-----------|----------------------|-------------------|
| Fejlesztési költség | ~55.440 EUR (173 person-nap) | ~4.620 EUR (116 óra) |
| Fejlesztési idő (1 fő) | ~35 hét | ~3 hét |
| Gyorsulási faktor | 1x | **12x** |
| Költségcsökkentés | -- | **92%** |
| Break-even (2.000 EUR/hó forgalomnál, 15%-os share) | ~185 hónap (soha) | **~15 hónap** |

Forrás: `Business Development/strategy/ai-development-analysis.md`

**Pilot fizetési mód:** Készpénz szállításkor (nincs payment gateway a v1-ben -- csökkenti a komplexitást).

**Jövő:** Online fizetési gateway integráció (pilot utáni validáció esetén).

### Revenue projekció (illusztratív)

| Forgalom (havi) | Revenue share (15%) | Éves bevétel | Break-even |
|-----------------|--------------------:|-------------:|-----------:|
| 1.000 EUR | 150 EUR | 1.800 EUR | ~29 hónap |
| 2.000 EUR | 300 EUR | 3.600 EUR | ~15 hónap |
| 3.000 EUR | 450 EUR | 5.400 EUR | ~10 hónap |
| 5.000 EUR | 750 EUR | 9.000 EUR | ~6 hónap |

_A 15% illusztratív -- a végleges % a pénzügyi adatok alapján kerül meghatározásra._

---

## 6. Key Resources

| Erőforrás | Tulajdonos | Részletek |
|-----------|-----------|-----------|
| Digitális platform (PWA) | Exar Labs | Vue 3 + Frappe backend, staging: deak.ignis.academy |
| Termékkatalógus (digitális) | Exar Labs | 37 termék, 5 kategória, multilingual JSON (HU+RO), optimalizált WebP fotók |
| Design system | Exar Labs | Burgundi (#9B2335) színpaletta, InterVar font, mobile-first komponensek |
| Brand identity | Exar Labs | Brand voice, headline-ek, szórólap, logo |
| Marketing anyagok | Exar Labs | Szórólap (nyomtatásra kész), adalékanyag-kutatás, termékfotók |
| Marketing budget és kivitelezés | Exar Labs | Facebook ads, szórólapok, bolti QR |
| Fejlesztői csapat (bench kapacitás) | Exar Labs | 12 fős csapat, AI-alapú workflow |
| Üzletfejlesztés és analitika | Exar Labs | KPI dashboard, pilot mérés |
| Húsfeldolgozó infrastruktúra | Húsüzlet | 3 bolt Székelyudvarhelyen |
| Szállítójármű + hűtőlánc | Húsüzlet | Meglévő kapacitás, időablakos kiszállítás |
| Helyi márka bizalom és termékminőség | Húsüzlet | Kézműves, adalékanyag-mentes, generációs szakértelem |

---

## 7. Key Activities

| Tevékenység | Felelős | Státusz (2026-03-27) |
|-------------|---------|---------------------|
| MVP fejlesztés és karbantartás | Exar Labs | 45% kész (17/38 task, ~80h) |
| Operatív felület (mészáros + futár) fejlesztése | Exar Labs | Spec kész, fejlesztés indulóban |
| Marketing stratégia, tartalom, fizetett kampányok | Exar Labs | Brand voice kész, szórólap kész |
| Pilot mérés, analitika, riportolás | Exar Labs | Tervezett (6. fázis) |
| Ügyfélszolgálat | Exar Labs | Tervezett |
| Termékkatalógus kezelés (feltöltés, árazás) | Exar Labs (húsüzlet input) | 37 termék feldolgozva |
| GDPR compliance | Exar Labs | DHOP-68, DHOP-69 (launch előtt) |
| Húsfeldolgozás és csomagolás | Húsüzlet | Folyamatos |
| Rendelések kiszállítása | Húsüzlet | Meglévő kapacitás |
| Termékminőség biztosítás | Húsüzlet | Folyamatos |

---

## 8. Key Partners

| Partner | Hozzájárulás | Státusz |
|---------|-------------|---------|
| Deák Húsmíves (húsüzlet) | Termék, termelés, szállítás | Szóbeli megállapodás -- írásbeli szükséges |
| Helyi közösség | Első vásárlók, szájról szájra validáció | -- |
| Facebook / Meta | Marketing csatorna, FB page | Meglévő oldal |
| Google | OAuth, Maps (futár navigáció), Analytics | Integrálva |
| Frappe / ERPNext | Backend platform | Tech stack része |

---

## 9. Cost Structure

Minden költséget az **Exar Labs** visel saját tőkéből. A húsüzletnek nulla pénzügyi kötelezettsége van.

### Fejlesztési költségek (egyszeri, validált adatok)

| Tétel | Összeg | Megjegyzés |
|-------|--------|-----------|
| MVP fejlesztés (AI-val, 1 fő) | ~4.620 EUR | 116h x 40 EUR/h; hagyományos ár: 55.440 EUR |
| Ebből újrafelhasználható komponensek | ~1.760 EUR | 44h (55%); 2. projekttől amortizálódik |
| Ebből DHOP-specifikus munka | ~2.860 EUR | 71.5h (45%) |

### Éves üzemeltetési költségek

| Tétel | Összeg | Gyakoriság |
|-------|--------|-----------|
| Hosting (Frappe Cloud / VPS) | ~200 EUR | Éves |
| Support és karbantartás | ~3.000 EUR | Éves |
| Ügyfélszolgálat | ~500 EUR | Éves |
| Payment gateway | ~200 EUR | Éves (post-pilot) |
| **Összes üzemeltetés** | **~3.900 EUR** | **Éves** |

### Marketing költségek (pilot)

| Tétel | Összeg | Megjegyzés |
|-------|--------|-----------|
| Szórólap nyomtatás | ~50-100 EUR | 500-1000 db A5 |
| Facebook hirdetések | TBD | Pilot budget cap meghatározandó |
| **Marketing összesen** | **TBD** | **Budget cap blokkoló** |

### Összes első éves befektetés

| Tétel | Összeg |
|-------|--------|
| Fejlesztés | ~4.620 EUR |
| Üzemeltetés | ~3.900 EUR |
| Marketing (becsült) | ~500-1.500 EUR |
| **Összesen** | **~9.000-10.000 EUR** |

---

## 10. Product Catalog

### Kategóriák és termékszám

| Kategória | Termékszám | Emoji |
|-----------|-----------|-------|
| Friss Sertéshús | 13 | 🥩 |
| Füstölt Áruk | 12 | 🔥 |
| Kolbász & Szalámi | 7 | 🌭 |
| Felvágott & Egyéb | 4 | 🍖 |
| Friss Növendékhús | 1 | 🐄 |
| **Összesen** | **37** | |

Teljes terméklista: `Marketing/products/product_listing.md`
Multilingual JSON: `Marketing/products/products.json`
Optimalizált fotók: `Marketing/products/photos/` (1000x1000px WebP)

### Árazás

Árak RON/kg-ban, a húsüzlet által meghatározva. Az online ár megegyezik a bolti árral (pilot fázisban nincs online felár).

Megjegyzés: a végleges súly eltérhet a rendelttől -- a kosár összesítőben figyelmeztetés jelzi: "A végleges ár a lemérés után változhat."

---

## 11. MVP Product Design (aktuális architektúra)

### Technológia

| Komponens | Technológia |
|-----------|------------|
| Frontend | Vue 3 + Composition API, Tailwind CSS |
| Backend | Frappe REST API (Python) |
| Platform | Progressive Web App (PWA) |
| Auth | Google OAuth + Email/Password; JWT, 30 napos session |
| Nyelv | Román (app UI) + Magyar (marketing anyagok) |
| Design | Mobile-first, InterVar font, burgundi (#9B2335) primary color |

### Két nézet, egy alkalmazás

Az app egyetlen PWA, két nézettel, role-based tab bar váltással:

| | Tab 1 | Tab 2 | Tab 3 | Tab 4 |
|---|---|---|---|---|
| **Customer nézet** | Produse | Coș | Comenzi | Cont |
| **Admin nézet** | Pregătire | Livrare | Statistici | Cont |

A Cont tab mindkét nézetben állandó -- innen érhető el a Nézet váltó (DHOP-67).

### Role-ök

| Role | Hozzáférés |
|------|-----------|
| Customer | Customer nézet -- böngészés, rendelés, rendelési előzmények |
| Butcher (Mészáros) | Admin nézet -- Pregătire tab: rendelések előkészítése, termék toggle |
| Courier (Futár) | Admin nézet -- Livrare tab: kiszállítás, Google Maps, kézbesítés |
| Admin (Szabolcs) | Admin nézet -- teljes hozzáférés + Statistici + KPI dashboard |

### Order Flow (Customer nézet)

1. **Böngészés** -- termékek, mennyiség kiválasztása (kg, 0.5 kg lépésekkel), kosárba
2. **Kosár áttekintés** -- tételek, mennyiségek, becsült végösszeg (súly figyelmeztetéssel)
3. **Szállítási adatok** -- név, telefon, cím (előtöltve mentett profilból)
4. **Megerősítés** -- rendelés összesítő, "Trimite comanda" gomb
5. **Köszönöm oldal** -- rendelésszám, következő lépések

### Order Status Lifecycle

```
Comandă nouă → În procesare → Pregătit pentru livrare → În curs de livrare → Livrat → Închis
(Új rendelés)   (Előkészítés)  (Kiszállításra kész)     (Úton van)         (Kézbesítve) (Lezárva)
```

### Admin nézet -- Operatív felület

**Pregătire tab (Mészáros):**
- Napi rendelési lista összesítővel (kg kategóriánként)
- Rendelés előkészítési nézet (termékek, mennyiségek)
- "Kiszállításra kész" státuszgomb
- Termék elérhetőség toggle

**Livrare tab (Futár):**
- Napi kiszállítási lista (időablak szerint rendezve)
- Kiszállítás részletei (cím, telefon, tételek)
- Google Maps deep link (egy koppintás navigáció)
- Kézbesítés megerősítése (opcionális megjegyzéssel)

**Statistici tab:**
- Napi/heti/havi összesítők (rendelések, bevétel, kg)
- Oszlopdiagram (heti/havi bontás)
- Rendelési lista adott időszakra

Teljes specifikáció: `design/butcher-courier-interface.md`

### Admin értesítések

| Esemény | MVP (email) | Post-MVP |
|---------|------------|----------|
| Új rendelés | Admin email (SMTP) | WhatsApp admin, push notification |
| Rendelés státusz változás | -- | Email/SMS a vásárlónak |
| Kiszállítás indítása | -- | SMS a vásárlónak (DHOP-48) |

---

## 12. Pilot Hypotheses

| ID | Hipotézis | Validációs módszer | Siker jelzés |
|----|-----------|-------------------|-------------|
| H1 | Van kereslet online húsrendelésre Székelyudvarhelyen | 30 napos pilot: leadott rendelések száma | ≥15 rendelés 30 nap alatt |
| H2 | A vásárlók hajlandóak friss húst online rendelni | 30 napos pilot: regisztrációk száma | ≥30 regisztráció 30 nap alatt |
| H3 | Az online kosárérték magasabb lesz a boltinál | Online átlag összehasonlítása a bolti átlaggal | Online kosár ≥ 20%-kal magasabb |
| H4 | A vásárlók egy része visszatérő lesz | ≥2 rendeléssel rendelkező vásárlók követése | ≥5 visszatérő vásárló 30 nap alatt |
| H5 | A bolti QR kód a leghatékonyabb akvizíciós csatorna | UTM tracking csatornánként (QR, Facebook, szájról szájra) | QR adja a regisztrációk ≥40%-át |
| H6 | A frissesség a leghatékonyabb marketing üzenet | Facebook A/B teszt különböző messaging pillérekkel | Frissesség-üzenet CTR > többi |

---

## 13. Pilot Success Metrics (30 nap)

| Metrika | Cél | Mérés |
|---------|-----|-------|
| Regisztrációk | 30 | DHOP-39, DHOP-42 |
| Leadott rendelések | 15 | DHOP-39 |
| Visszatérő vásárlók (≥2 rendelés) | 5 | DHOP-39 |
| Átlagos kosárérték | Mérni (bázis nélkül) | DHOP-39 |
| Rendelés-visszavonási arány | < 20% | DHOP-39 |

---

## 14. Pilot Constraints (Szándékos)

| Korlát | Ok |
|--------|-----|
| 1 bolt (a 3-ból) | Komplexitás minimalizálása |
| Csak készpénz szállításkor | Nincs payment gateway szükséges |
| Csak webapp (nincs natív app) | Gyorsabb fejlesztés és telepítés |
| Rögzített marketing budget cap | Exar Labs összes befektetési kitettségének kontrollja |
| Csak Székelyudvarhely + 10 km | Szállítási zóna korlátozás (DHOP-50, post-MVP) |
| Román nyelvű app UI | Az app felület románul, marketing anyagok magyarul |

Cél: **gyors tanulás kontrollált, kiszámítható befektetéssel**.

---

## 15. Pilot Exit Criteria

**Scale döntés (folytatás, több befektetés):** Mind a 3 teljesül 30 nap után:
- ✅ 30+ regisztráció
- ✅ 15+ leadott rendelés
- ✅ 5+ visszatérő vásárló

**Pivot döntés (modell újragondolása):** 1-2 metrika részben teljesül -- blokkolók elemzése, egy változó módosítása, második 30 napos ciklus.

**Stop döntés (pilot leállítása):** 10-nél kevesebb regisztráció ÉS 5-nél kevesebb rendelés 30 nap után teljes marketing erőfeszítéssel -- elégtelen keresleti jelzés.

A stop döntés nem kudarc. Gyors, olcsó válasz egy stratégiai kérdésre, ami megvédi az Exar Labs-t a további befektetéstől egy nem validált csatornába.

---

## 16. Pilot Learning Goals

A rendszer célja nem csak rendeléskezelés -- **fogyasztói viselkedés adatgyűjtése**.

Kulcskérdések:
- Rendelnek-e az emberek friss húst online?
- Milyen kosárértékkel?
- Milyen gyakorsággal?
- Melyik akvizíciós csatorna működik a legjobban?
- Melyik marketing üzenet rezonál (frissesség, kényelem, helyi bizalom)?
- A mészáros + futár operatív felület használható-e a gyakorlatban?

A pilot sikere a **piaci visszajelzés sebessége és minősége** alapján definiált.

---

## 17. Post-Pilot Scaling Path

Ha a pilot validál (H1 + H2 + H4 teljesül):

1. **Optimalizálás** -- UX javítás valódi felhasználói visszajelzés alapján, online payment gateway hozzáadása
2. **Skálázás** -- kiterjesztés mind a 3 húsüzlet helyszínre; marketing költés növelése
3. **Replikáció** -- ugyanaz a sablon alkalmazása 2-3 másik helyi kézműves vállalkozásra (pékség, tejtermék stb.)
4. **Platform** -- fejlődés a **Local Artisan Commerce Platform** irányába, több kereskedő kiszolgálása

Ha a pilot részben validál: elemezni melyik hipotézis bukott, egy változó módosítása (pl. másik marketing csatorna, más termékkategória), második 30 napos ciklus futtatása.

### Újrafelhasználható komponensek értéke

Az eddigi 80 óra 55%-a (~44h) platformszintű, újrafelhasználható munkára ment:

| Komponens | Következő projektnél |
|-----------|---------------------|
| Multilingual product catalog JSON struktúra | ✅ Kész |
| Frappe Jira workflow template (7 Epic séma) | ✅ Kész |
| Business Model Canvas + pilot-concept sablonok | ✅ Kész |
| Dev-roadmap fázis-struktúra | ✅ Kész |
| Revenue share co-venture modell | ✅ Kész |
| Brand voice framework | ✅ Kész |

Becsült fejlesztési idő következő hasonló projektre: ~87h (16x gyorsulás hagyományoshoz képest).

---

## 18. Fejlesztési Haladás (2026-03-27)

| Fázis | Hét | Fő feladatok | Státusz |
|-------|-----|-------------|---------|
| 0 -- Alapok | 1. | Hosting, order schema | ✅ Kész |
| 1 -- Auth + Környezet | 1-2. | Google OAuth, email auth, session, profile | ~90% kész |
| 2 -- Termékkatalógus | 2. | Product listing, detail, quantity, categories | ~80% kész |
| 3 -- Rendelési folyamat | 2-3. | Cart, checkout, order placement | ~85% kész |
| 4 -- Rendeléskezelés + Admin alap | 3. | Order history, status mgmt, customer list, product mgmt | Tervezett |
| 5 -- Mészáros & Futár | 3-4. | DHOP-52 Epic: Pregătire + Livrare tabok | Tervezett |
| 6 -- Statisztikák + Analytics | 4. | KPI dashboard, Statistici tab | Tervezett |
| 7 -- UX Polish + GDPR | 4. | Branding, GDPR consent, Nézet váltó | Tervezett |
| 8 -- Launch prep | 4-5. | QR kódok, Facebook CTA | Blokkolva (domain) |

Részletes roadmap: `Business Development/pilot-husuzlet/dev-roadmap-v1.3.md`

---

## 19. Open Questions

> ⚠️ Az 1-5. tételek **blokkolók** -- launch előtt meg kell oldani.

1. **Revenue share pontos százalék** -- mi a méltányos, ha az Exar Labs viseli az összes költséget és marketinget? **[BLOCKER]** _Szükséges: pénzügyi adatok a húsüzlettől_
2. **Pilot marketing budget cap** -- mennyi a maximális összbefektetés? **[BLOCKER]**
3. **Go/no-go küszöb** -- mikor döntünk skálázás vagy leállás kérdésében? **[BLOCKER]** _Részben definiált (15. szekció), de számszerűsíteni kell a maximális veszteséget_
4. **Reklamációs és visszaküldési folyamat** -- mi történik panasz esetén? **[BLOCKER]**
5. **Írásbeli partnerségi megállapodás** -- minimális feltételek írásban **[BLOCKER]** _Két konfliktusban lévő testvér tulajdonos = különösen fontos_
6. **Domain véglegesítés** -- a QR kódok és Facebook CTA ettől függ **[BLOCKER]**
7. ~~Melyik marketing üzenet rezonál legjobban?~~ -- **Részben megválaszolva:** a frissesség a #1 megkülönböztető, „Hajnalban készül. Ma nálad." a fő headline; A/B tesztelés a pilotban véglegesíti

---

## Változáskövetés

| Verzió | Dátum | Változás |
|--------|-------|---------|
| 0.1 | 2026-03-04 | Első draft |
| 0.2 | 2026-03-04 | Struktúra javítás |
| 0.3 | 2026-03-05 | Google OAuth primary; hypothesis validation |
| 0.4 | 2026-03-05 | Post-pilot scaling path |
| 0.5 | 2026-03-05 | Heading/version consistency |
| **1.0** | **2026-03-27** | **Átfogó frissítés:** validált fejlesztési adatok (AI elemzés: 12x, 92%); brand voice véglegesítve; 37 termék 5 kategóriában; architektúra frissítés (Customer/Admin nézet, egyetlen PWA); GDPR szekció; revenue projekció; termékkatalógus szekció; fejlesztési haladás; marketing anyagok státusza; Open Questions frissítve (#6 domain hozzáadva, #7 részben megválaszolva) |
