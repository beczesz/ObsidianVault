---
title: Business Model Canvas -- Deák Húsmíves Online Platform (Pilot)
version: 2.0
date: 2026-03-28
author: Becze Szabolcs -- Exar Labs
collaborators: ChatGPT (GPT-4o) -- "Üzleti terv értékelés" session
description: >
  BMC v2.0 -- operatív és mérhető verzió. Az v1.0 stratégiai/vízió szintű BMC-ből
  "élesítve" az összes validált döntés, valós fejlesztési adat és a ChatGPT közös
  gondolkodási session alapján (2026-03-28). Fő változások: Growth Flywheel hozzáadva
  (az v1.0-ból hiányzó "engine"), customer segments priorizálva early adopter szegmensre,
  value prop rangsor korrigálva, guest-first UX, sávos revenue share modell, supplier
  playbook körvonalai, stop decision cap definiálva, platform vízió 4 fázisra bontva.
  A DHOP "nem a cél -- hanem a bizonyíték, hogy a LocalBasket működhet."
predecessor: business-model-canvas.md (v1.0, 2026-03-27)
---

# Business Model Canvas v2.0 -- Deák Húsmíves Online Platform (Pilot)

_Version: 2.0 | Last updated: 2026-03-28_
_Scope: DHOP pilot -- az online rendelési csatorna validálása. Ez **nem** a teljes húsüzlet modellje, és **nem** a LocalBasket platform BMC-je (az külön dokumentum lesz). A cél: gyors tanulás, első bizonyíték._

---

## PLATFORM MISSZIÓ

> _"Összekötjük a helyi termelőket a vásárlókkal, hogy a mindennapi élelmiszer egyszerűen, frissen és közvetlenül jusson el az emberekhez. Egy olyan rendszert építünk, ahol a helyi gazdaság erősödik, és mindenki nyer: a vásárló, a termelő és a közösség."_

Ez az iránytű érvényes a DHOP pilotra és a jövőbeli LocalBasket platformra egyaránt.

**A DHOP nem a cél -- hanem a bizonyíték, hogy a LocalBasket működhet.**

---

## 0. Growth Flywheel (az "engine" -- v1.0-ból hiányzott)

Ez a BMC legkritikusabb új szekciója. A DHOP **nem discovery business, hanem habit business.** A növekedési motor a rutin-alapú ismétlődő rendelés.

```
1. Megbízható, stabil supply (mindig van jó termék)
         ↓
2. Pozitív első rendelési élmény (gyors, egyszerű, pontos)
         ↓
3. Második rendelés (habit kezdete) -- T+3 nap trigger
         ↓
4. Heti rutin kialakul ("csütörtökön rendelek húst")
         ↓
5. Növekvő rendelési volumen (kosárérték és frekvencia nő)
         ↓
6. Supplier stabilabb és olcsóbban tud termelni
         ↓
7. Jobb ár + jobb elérhetőség → erősebb value proposition
         ↓
→ vissza az elejére (flywheel forog)
```

**A kritikus pillanat:** "ez kényelmes volt... legközelebb is innen rendelek."

**A flywheel 3 kulcskomponense:**
- **Supply Stability** -- mindig van készlet, nincs "elfogyott"
- **Fast First Order** -- 2-3 perc alatt rendelés (guest-first UX)
- **Second Order Trigger** -- T+3 napos manuális emlékeztető az első 30 usernél

---

## 1. Customer Segments

### Elsődleges early adopter szegmens (pilot: első 30 user)

**Nem a "Családok" lesznek az első 30 user.** A legkisebb ellenállással rendelők:

> **"Digitálisan nyitott, időszűkében lévő helyi vásárlók, 25-45 éves korosztály"**

| Jellemző | Leírás |
|----------|--------|
| Kor | 28-45 év |
| Foglalkozás | Irodai dolgozó, vállalkozó |
| Fájdalom | Nincs idő a bolti vásárlásra |
| Digitális szokás | Már rendel pizzát/ételt futárral; Google login nem probléma |
| Döntési sebesség | Gyors (alacsony ellenállás az online próbával) |
| Vásárlási mód | Tervezett (heti), nem impulzus |

**Miért ők az első 30?** Náluk egyszerre van meg:
- Probléma (időhiány) ✅
- Digitális komfort ✅
- Vásárlási szokás (online rendelés létezik az életükben) ✅
- Gyors döntés (nem kell 3 hét meggyőzés) ✅

### Szegmens térkép (pilot → scale)

| Szegmens | Pilot szerep | Scale szerep | Megjegyzés |
|----------|-------------|-------------|-----------|
| **Időszűkében lévők** (25-45) | ✅ Elsődleges | ✅ Core | Legjobb konverzió |
| **Korai digitális userök** | ✅ Enabler | ✅ Amplifier | Kipróbálják + megosztják |
| **Egészségtudatosak** | ⚠️ Másodlagos | ✅ Fontos | Nem trigger az első rendelésre |
| **Családok** (35-55) | ❌ Nem első 30 | ✅ Fő scale szegmens | Konzervatívak, bizalom kell |

**Validációs módszer:** UTM tracking csatornánként; melyik szegmens regisztrál és rendel legtöbbet (DHOP-42 analytics).

---

## 2. Value Proposition

### A vásárlónak (KORRIGÁLT PRIORITÁS -- v1.0-tól eltér)

A v1.0-ban Frissesség volt a #1. **A valódi első rendelési trigger a Kényelem.** A rangsor pilothoz optimalizálva:

| # | Pillér | Üzenet | Miért ez a sorrend |
|---|--------|--------|-------------------|
| **#1** | **Kényelem** | "Nem kell boltba menned -- house delivery" | Ez az azonnali fájdalomoldó; időszűkében lévő vásárló számára ez a trigger |
| **#2** | **Megbízhatóság** | "Mindig van, mindig jön -- megrendelés = teljesítés" | A flywheel forogásának feltétele |
| **#3** | **Frissesség** | "Hajnalban készül. Ma nálad." | Erős megkülönböztető, de csak az első rendelés UTÁN válik igazán értékessé |
| **#4** | **Ár** | "Ugyanannyiba kerül, mint a boltban -- plusz kiszállítás" | Implicit; nem kell külön kommunikálni |
| **#5** | **Helyi bizalom** | "A mi húsmívesünk -- ismert, megbízható" | Erősödik idővel; meglévő vásárlóknak azonnal releváns |

> **Adalékanyag-mentesség:** Nice-to-have. Fontos a szórólapon és az egészségtudatos szegmensnél, de **nem az első rendelés triggere.** Nem az első képernyőn.

### A co-venture partnernek (húsüzlet) -- változatlan

- Új bevételi csatorna nulla előzetes befektetéssel és nulla operatív teherrel
- Jobb készletgazdálkodás (előrendelések csökkentik a pazarlást)
- Első valódi értékesítési statisztikák -- pénzügyi átláthatóság
- Marketing teljesen az Exar Labs által kezelve

---

## 3. Channels

### Elsődleges akvizíciós csatorna (pilot: első 30 user)

**Egyetlen csatornára fókuszálunk a pilot első szakaszában:**

> **🏪 Fizikai bolt + személyes ajánlás QR kóddal**

**Miért ez és nem Facebook?**
- A boltban lévő vásárló: már vásárol, már bízik, már releváns → **high-intent traffic**
- Facebook: széles, zajos, alacsony vásárlási szándék

**Megvalósítás:**
- Scriptelt ajánlás a pultnál (egységes mondat mindenkitől):
  > _"Most már lehet rendelni is, és házhoz visszük -- itt egy QR kód, próbáld ki."_
- Napi cél: 10-20 megkeresett → 3-5 regisztráció → **1 hét alatt megvan a 30 user**
- QR kód: pulthoz rögzítve + ablakban + szórólapon

### Csatorna térkép (pilothoz rangsorolva)

| Csatorna | Szerep | Timing | Prioritás |
|----------|--------|--------|-----------|
| Bolti QR + személyes ajánlás | Fő akvizíció | Azonnal | 🔴 #1 |
| Szójról szájra | Természetes amplifikáció | Folyamatosan | 🔴 #2 |
| Szórólap (A5) | Bolti osztogatás, csomagolás mellé | Launch | 🟠 #3 |
| Facebook oldal | Kommunikáció, bizalom | Post-launch | 🟠 #4 |
| Helyi Facebook csoportok | Organikus posztok | 2-3. hét | 🟡 #5 |
| Boltablak poszter | Vizuális jelenlét | Launch | 🟡 Support |

---

## 4. Customer Relationships

### Onboarding -- Guest-first UX (v1.0-tól eltér)

**A v1.0 login screen az elején. Ez MEGVÁLTOZOTT.**

> **"Don't ask before you show value."**

**Helyes flow:**
```
Termékek megjelenítése azonnal (login nélkül)
    ↓
Böngészés, kosárba rakás (regisztráció nélkül)
    ↓
Checkout: ITT kér login-t az app (Google OAuth / email)
    ↓
Szállítási adatok kitöltése (előtöltve visszatérő usernél)
    ↓
Rendelés leadva → Köszönöm oldal
```

**Miért ez fontosabb a launch előtt:**
- ❌ Login az elején → "mi ez? minek adjam meg az adataim?"
- ✅ Termékek először → "hmm, ez érdekes... mennyibe kerül?"

### Kapcsolat fenntartása -- Második rendelés trigger

**Ez a flywheel legkritikusabb eleme.**

| Időpont | Akció | Eszköz | Cél |
|---------|-------|--------|-----|
| T+0 (kiszállítás után) | Személyes "hogy volt?" | WhatsApp / telefon | Bizalom |
| T+3 nap | Emlékeztető: "mikor rendelsz legközelebb?" | WhatsApp (manuális pilot fázisban) | 2. rendelés trigger |
| T+7 nap | Ha nem rendelt: egy egyszerű "friss termékek" üzenet | WhatsApp | Reaktiváció |

> **Pilot fázisban: nem automation kell, hanem személyes kapcsolat az első 30 usernél.**

### Folyamatos kapcsolat -- változatlan

- Közvetlen visszajelzés az első vásárlóktól (kvézi béta tesztelők)
- Rendszeres Facebook posztok (friss termékek, promók)
- Személyes, tegező hangnem (brand voice szerint)
- Szórólap melléklet minden kiszállításhoz

---

## 5. Revenue Streams

### Sávos Revenue Share modell (v1.0 X% helyett)

Az Exar Labs nem a vásárlóktól keres -- **a speak supplier oldalán van a monetizáció.**

**Online ár = bolti ár.** Nincs online felár a vásárló számára.

| Havi forgalom | Revenue Share % | Havi bevétel (Exar) | Megjegyzés |
|---------------|----------------|---------------------|-----------|
| 0-2 000 EUR | **5%** | 0-100 EUR | Pilot fázis -- alacsony belépési ellenállás |
| 2 000-5 000 EUR | **8%** | 160-400 EUR | Stabil fázis -- érték már bizonyított |
| 5 000+ EUR | **10-12%** | 500+ EUR | Scale fázis -- standard ajánlat |

**Miért sávos és nem fix?**
- Motivál (mindenki érdekelt a volumen növelésben)
- Skáláz (partner "nem fél" az elején alacsony %-tól)
- Fair marad minden fázisban

**Skálázási küszöb:** ≥ 40 000-50 000 RON / hó forgalom felett kezd pozitív hozzájárulást termelni.

### Pricing Strategy (vásárlói oldal)

| Tétel | Döntés | Indok |
|-------|--------|-------|
| Online ár | = Bolti ár | Bizalom; nincs "megverik az online rendelőt" érzés |
| Kiszállítás (pilot) | Beépítve vagy ingyenes | Friction csökkentés, gyors adoption |
| Kiszállítás (post-pilot) | 5-10 RON | Ha volumen megengedi |
| Súlyeltérés | ±10% tolerancia, figyelmeztetéssel | Természetes hús-sajátosság |

### Bevételi projekció (sávos modellel)

| Havi forgalom | Revenue (5%) | Revenue (8%) | Éves | Break-even |
|---------------|-------------|-------------|------|-----------|
| 500 EUR | 25 EUR | -- | 300 EUR | Soha (stop) |
| 2 000 EUR | 100 EUR | 160 EUR | 1 920 EUR | ~50+ hónap |
| 5 000 EUR | -- | 400 EUR | 4 800 EUR | ~21 hónap |
| 10 000 EUR | -- | -- (12%) | 14 400 EUR | ~7 hónap |

---

## 6. Key Resources

A BMC-logika szerint az erőforrásokat két tengely mentén kell értékelni: **kié** (Exar Labs vs. Húsüzlet) és **mennyire kritikus** a flywheel működéséhez.

### Erőforrás térkép

| Erőforrás | Tulajdonos | Kritikusság | Megjegyzés |
|-----------|-----------|-------------|-----------|
| **Supply megbízhatóság** | Húsüzlet | 🔴 #1 | A flywheel első és legkritikusabb lépése -- ha elfogyott a termék, leáll a loop |
| **Digitális platform (PWA)** | Exar Labs | 🔴 #2 | Vue 3 + Frappe; staging: deak.ignis.academy; 56% kész; beta: ápr 14-17 |
| **Guest-first UX + checkout flow** | Exar Labs | 🔴 #3 | A konverzió kulcsa; login nélkül böngészés → login csak a fizetésnél |
| AI-alapú fejlesztési módszertan | Exar Labs | 🟠 | 12x gyorsabb, 92% olcsóbb; lehetővé teszi a co-venture modellt |
| Termékkatalógus | Exar Labs | 🟠 | 37 termék, 4 kategória, HU+RO JSON, optimalizált WebP fotók |
| Bench kapacitás (fejlesztők) | Exar Labs | 🟠 | Aktív projekt nélküli fejlesztők; co-venture modell alapja |
| Brand identity + marketing anyagok | Exar Labs | 🟡 | Brand voice, szórólap v9-v10 nyomtatásra kész, Facebook cover |
| Helyi márka bizalom + termékminőség | Húsüzlet | 🟡 | Kézműves, generációs szakértelem -- meglévő vásárlói hálózat |
| Húsfeldolgozó infra (3 bolt, saját autó, hűtőlánc) | Húsüzlet | 🟡 | Fizikai logisztikai alap; pilot fázisban a húsüzlet futároz |

### Az erőforrás-aszimmetria mint modell

**Az Exar Labs erőforrásai:** digitálisak, skálázhatóak, egyszer létrehozva többször hasznosíthatóak (platform, brand, módszertan).

**A Húsüzlet erőforrásai:** fizikainak, helyieknek, nem másolhatóak (supply, bizalom, minőség).

Ez az aszimmetria **teszi lehetővé a co-venture modellt:** mindkét fél olyat ad, amije a másiknak nincs.

### Legkritikusabb erőforrás-kockázat

> ⚠️ **Supply kockázat:** Ha a Deák Húsmíves nem tudja stabilisan teljesíteni a rendeléseket (elfogyott, minőségi probléma, operatív zavar), a flywheel megáll. **Ez az egyetlen erőforrás, ami leállíthatja a pilotot anélkül, hogy az Exar Labsnak bármi köze lenne hozzá.**

**Mitigáció:**
- Dry run előtt készletellenőrzés és kapacitás-megbeszélés
- Minimum 3 termékkategóriában stabil supply (ne csak 1-2 premium termék)
- Hiány esetén: aktív visszahívás a vásárlónak (ne csendben töröld a rendelést)
- Hosszú távon: B terv supplier az egyes kategóriákhoz

---

## 7. Key Activities

### TOP 3 -- Most, beta launch előtt

> _Ha csak 3 dolgot csinálsz, ez legyen az:_

**#1 -- End-to-end rendelési dry run**
- 5-10 próbarendelés valódi körülményekkel (készlet, csomagolás, futár, pénz)
- Mérd: idő (rendeléstől kiszállításig), hibák, kommunikáció
- Cél: 0 kritikus hiba a core loopon (browse → cart → order → deliver)

**#2 -- Boltban scriptelt ajánlás + QR kihelyezés**
- Egységes mondat a pultnál, jól látható QR
- Napi cél: 10-20 megkeresett → 3-5 regisztráció
- Cél: első 30 user pipeline a beta első hetére

**#3 -- Második rendelés trigger felállítása (manuálisan)**
- Lista az első rendelőkről + T+3 nap WhatsApp emlékeztető
- Rövid, kontextusos üzenet
- Cél: első 5 visszatérő user

### Teljes tevékenységtérkép

| Tevékenység | Felelős | Timing | Prioritás |
|-------------|---------|--------|-----------|
| Dry run (5-10 próba) | Exar Labs + Húsüzlet | MOST | 🔴 #1 |
| QR + scriptelt ajánlás a boltban | Exar Labs setup + Húsüzlet kivitel | Launch előtt | 🔴 #2 |
| 2. rendelés trigger (manuális) | Exar Labs | Post-launch, T+3 | 🔴 #3 |
| Írásbeli partnerségi megállapodás | Exar Labs | AZONNAL (blocker) | 🔴 Blocker |
| Domain véglegesítése | Exar Labs | AZONNAL (blocker) | 🔴 Blocker |
| MVP fejlesztés befejezése (44% hátra) | Exar Labs | Ápr 14-17 | 🟠 |
| GDPR consent + adattörlés | Exar Labs | Launch előtt kötelező | 🟠 |
| Soft launch (10-15 béta tesztelő) | Exar Labs | 1 héttel launch előtt | 🟠 |
| Pilot mérés (KPI dashboard) | Exar Labs | Launch-tól | 🟡 |
| Marketing (Facebook, szórólap) | Exar Labs | Post-launch | 🟡 |

---

## 8. Key Partners

### Deák Húsmíves (jelenlegi partner)

**Minimális írásbeli megállapodás tartalom (1-2 oldal):**

| Pont | Tartalom |
|------|----------|
| Tárgy | Online rendelési és kiszállítási együttműködés |
| Revenue share | Sávos % (5-8% pilot) + elszámolás gyakorisága |
| Árpolitika | Online = bolti ár; súlyeltérés ±10% kezelése |
| Szerepek (RACI) | Deák: készlet/minőség/csomag; Exar: platform/marketing/rendelés |
| SLA light | Visszaigazolás max. X perc; kiszállítási idősávok |
| Termékelérhetőség | Mi van, ha elfogy (helyettesítés / visszahívás) |
| COD folyamat | Ki szedi be, mikor számol el |
| Időtartam | 30-60 nap pilot; bármely fél felmondhat 7 napos határidővel |
| Kapcsolattartó | **EGY kijelölt személy a Deák részéről** |

> ⚠️ **Két testvér / konfliktus kockázat:**
> - Risk: lassú döntések, egymásnak ellentmondó utasítások, operatív instabilitás
> - Megoldás: **EGY kapcsolattartó** -- az operáció leválasztva az érzelmekről
> - Szabolcs = "külső stabil pont" -- nem oldja meg a konfliktusukat, de stabil rendszert ad
> - **Exit thinking:** Mi van, ha Deák kiesik? Legyen B terv supplier -- ne legyen 100% függőség

### Supplier Pitch (jövőbeli: sajtosok, zöldségesek, stb.)

**A pitch lényege:**
> _"Semmi előzetes befektetés nem kell tőled. Mi fejlesztjük, mi marketingeljük, te csak a termékedet hozod. A mi platformunk megmutat téged az egész városnak. Fizetsz csak ha eladtál."_

**Miért vonzó a termelőnek:**
- Nulla entry barrier (nincs IT költség)
- Forgalom-alapú bevételmegosztás (csak ha elad)
- Láthatóság anélkül, hogy online marketing ismeretük lenne
- Olcsóbban adhat (nem kell piacra/vásárra menni → fix cost csökken)

### Többi partner -- változatlan

| Partner | Hozzájárulás |
|---------|-------------|
| Helyi közösség | Első vásárlók, szájról szájra |
| Facebook / Meta | Marketing csatorna |
| Google | OAuth, Maps (futár), Analytics |
| Frappe / ERPNext | Backend platform |

---

## 9. Cost Structure

Minden költséget az **Exar Labs** visel saját tőkéből.

### Befektetés

| Tétel | Összeg | Megjegyzés |
|-------|--------|-----------|
| MVP fejlesztés (AI-val, 1 fő) | ~4 620 EUR | 116h x 40 EUR/h; hagyományos: 55 440 EUR |
| Éves üzemeltetés | ~3 900 EUR | Hosting + support + ügyfélszolgálat |
| Marketing (pilot) | ~500-2 000 EUR | QR, szórólap, Facebook |
| **Összes kitettség plafon** | **~12-13 000 EUR** | **Ez a stop decision boundary** |

### Stop Decision Framework

| Döntés | Feltétel | Timing |
|--------|----------|--------|
| **Folytatás / scale** | 30+ reg + 15+ rendelés + 5+ visszatérő | 30 nap |
| **Pivot** | 1-2 metrika részben teljesül | 30 nap |
| **Stop** | < 10 reg ÉS < 5 rendelés teljes marketing erőfeszítéssel | 30 nap |
| **Hard stop** | 3 hónap után nincs kialakult heti rendelési habit | 90 nap |

> **Az Exar Labs maximális vállalható vesztesége: ~12-13 000 EUR.** Ennél több nincs a kockázatvállalási keretben.

### Break-even (reális)

- **Skálázási küszöb:** ≥ 40 000-50 000 RON / hó forgalom
- **Teljes megtérülés:** 7-30 hónap (forgalom növekedésétől függően)
- **Realisztikus cél (12 hónap):** 2 000-3 000 EUR / hó online forgalom → 8% = ~160-240 EUR / hó → ~2 000 EUR / év (a 3 900 EUR üzemeltetési cost felé)

---

## 10. Pilot Hypotheses (változatlan, de kiegészítve)

| ID | Hipotézis | Validáció | Siker |
|----|-----------|-----------|-------|
| H1 | Van kereslet online húsrendelésre | 30 napos pilot | ≥15 rendelés |
| H2 | Vásárlók hajlandóak friss húst online rendelni | Regisztrációk | ≥30 regisztráció |
| H3 | Online kosárérték > bolti | Összehasonlítás | ≥20%-kal magasabb |
| H4 | Kialakul ismétlő vásárlási habit | ≥2 rendelés/user | ≥5 visszatérő |
| H5 | Bolt + QR a legjobb csatorna | UTM tracking | QR ≥40% regisztrációk |
| H6 | Kényelem az erősebb marketing üzenet (nem Frissesség) | A/B teszt | Kényelem CTR > Frissesség |
| **H7** | **T+3 napos trigger hozza a 2. rendelést** | Manuális WhatsApp + mérés | ≥50% az emlékeztetőre rendel |

---

## 11. Pilot Success Metrics (30 nap)

| Metrika | Cél | Mérés |
|---------|-----|-------|
| Regisztrációk | 30 | DHOP-42 |
| Leadott rendelések | 15 | DHOP-39 |
| Visszatérő vásárlók (≥2 rendelés) | 5 | DHOP-39 |
| Átlagos kosárérték | Mérni (bázis nélkül) | DHOP-39 |
| Rendelés visszavonás | < 20% | DHOP-39 |
| **2. rendelés aránya (T+3 trigger)** | ≥50% | Manuális nyomon követés |
| **Kosárérték vs. bolti átlag** | +20% | Manuális összehasonlítás |

---

## 12. Fejlesztési státusz (2026-03-28)

| Fázis | Tartalom | Státusz |
|-------|----------|---------|
| 0 -- Alapok | Hosting, order schema | ✅ Kész |
| 1 -- Auth + Profil | Google OAuth, email auth, session | ~90% |
| 2 -- Termékkatalógus | Product listing, detail, kosár | ~80% |
| 3 -- Rendelési flow | Cart, checkout, order placement | ~85% |
| 4 -- Admin alap | Rendeléskezelés, státusz | Folyamatban |
| 5 -- Mészáros + Futár | Pregătire + Livrare tabok (DHOP-52) | Tervezett |
| 6 -- Statisztikák | KPI dashboard | Tervezett |
| 7 -- UX + GDPR | Guest-first, GDPR consent, Nézet váltó | Tervezett |
| 8 -- Launch prep | QR, Facebook CTA, domain | Blokkolva |

> **Összesített haladás: 56% | Beta céldátum: 2026. április 14-17.**

---

## 13. Blokkolók (launch előtt kötelező)

| # | Blokkoló | Státusz |
|---|----------|---------|
| 1 | **Domain véglegesítése** | ❌ Nyitott |
| 2 | **Írásbeli partnerségi megállapodás** | ❌ Nyitott |
| 3 | **Revenue share % rögzítése** (pénzügyi adatok kellenek) | ❌ Nyitott |
| 4 | **Marketing budget cap** | ❌ Nyitott |
| 5 | **Reklamációs folyamat** | ❌ Nyitott |
| 6 | **GDPR consent** (DHOP-68, DHOP-69) | 🟡 Fejlesztés |
| 7 | **Guest-first UX implementálása** (v1.0-hoz képest új) | 🟡 Fejlesztés |

---

## 14. Platform Vision -- Post-Pilot Scaling Path

> **Ez a szekció a jövőbe mutat. A DHOP pilot az első lépés, de a valódi lehetőség nagyobb.**

### 1 Platform, 2 Mód

Nem 2 külön app -- 1 platform, 2 különböző use-case réteggel:

| | Mode A: 🥩 Daily Supply | Mode B: 🧺 Local Market |
|--|--------------------------|--------------------------|
| Use-case | Gyors, rutin vásárlás | Felfedezés, prémium |
| Frekvencia | Napi / heti | Alkalmanként |
| UX | Category-first, gyors checkout | Vendor/story-first, vizuális |
| Termékek | Hús, tej, zöldség (alapok) | Sajt, kerámia, méz, ruha (különleges) |
| Jelleg | Utility product | Experience product |

**App csomagnév irány:** `ro.exar.localbasket`

### 4 Fázisú Stratégiai Roadmap

```
Phase 1 -- PILOT & VALIDATION (MOST)
  ├── Deák Húsmíves app beta (ápr 14-17)
  ├── 30 regisztráció validálása
  ├── 15 rendelés validálása
  ├── 5 visszatérő user (habit validálás)
  └── pricing és kosárérték megértése

Phase 2 -- CATEGORY EXPANSION (Curated Supply)
  ├── 1 sajtos partner bevonása
  ├── 1 zöldséges partner bevonása
  ├── 1 gyümölcsös partner bevonása
  ├── Category-first UX stabilizálása
  └── Supply reliability validálása

Phase 3 -- GEOGRAPHIC EXPANSION
  ├── 2. város pilot
  ├── Supplier onboarding playbook alkalmazása
  ├── Logistics tanulás
  └── Regionális működés validálása

Phase 4 -- LOCAL MARKET LAYER (Discovery)
  ├── Termelő adatbázis építése
  ├── Multi-vendor modell tesztelése
  ├── Marketplace UX kialakítása
  └── Premium / discovery kategória bevezetése
```

> ⚠️ **Fontos:** A Phase 2-4 csak akkor indul, ha a Phase 1 validál. Most kizárólag a Phase 1-re fókuszálunk.

---

## 15. Supplier Playbook (körvonal -- kidolgozandó)

_Ez a v1.0-ban nem szerepelt. A skálázás kulcsa._

**Új supplier megszólítása:**
1. Személyes egyeztetés (nem email)
2. Pitch: nulla befektetés + forgalom-alapú megtérülés
3. Próbaidőszak ajánlat (30 nap, kiszállás lehetőségével)
4. Minimális megállapodás (a Deák sablonból kiindulva)
5. Onboarding: terméklista + fotók + árak (Exar Labs segít)

**Pricing strategy az új suppliernek:**
- Ugyanaz a sávos modell (5-8% pilot → 8-12% stabil)
- Az online ár a termelő határozza meg (nem az Exar Labs)
- Szállítás: a termelő meglévő logisztikájával (ha van), vagy koordinált

---

## Változáskövetés

| Verzió | Dátum | Változás |
|--------|-------|---------|
| 0.1--0.5 | 2026-03-04--05 | Első draftek |
| 1.0 | 2026-03-27 | Átfogó frissítés: AI elemzés, brand voice, 37 termék, architektúra |
| **2.0** | **2026-03-28** | **Operatív élesítés ChatGPT kollaborációval:** Growth Flywheel (új); Customer Segment priorizálás (időszűkében lévők = #1 early adopter); Value Prop rangsor korrigálva (Kényelem #1, nem Frissesség); Guest-first UX (termék előbb, login csak checkoutnál); Sávos revenue share (5%/8%/10-12%); Supplier Playbook körvonal; Stop Decision cap (~12-13k EUR); Break-even reális becslés (7-30 hónap); Platform Vision 4 fázisra bontva; Missziós nyilatkozat; Beta dátum: ápr 14-17 |
