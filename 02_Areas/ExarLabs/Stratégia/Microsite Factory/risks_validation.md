---
title: Risks & Validation — Microsite Factory
source: Gemini (Validator role) + Claude saját pre-validation
url: https://gemini.google.com/app/a14b7323cb6a7de5
imported: 2026-05-16
status: v2 — Gemini válasz integrálva
id: a2fe75e1-3b6b-4b1d-a98c-cdadde86b6b7
index_schema_version: 1
---

# Risks & Validation — Microsite Factory

> Gemini Validator brutális, részletes kritikát adott a 10 kérdésre. Ez a legértékesebb dokumentum a BMC-ben — itt tárul fel az ötlet legtöbb sebezhetősége. **Nem szabad átsiklani rajta.**

---

## 🚨 Gemini Validator átfogó verdiktje

> *"Az ötlet papíron (technológiailag és elméleti marzsként) gyönyörű, de a kkv-szektor – különösen a magyar egészségügyi mikropiac – egy egészen más állatfaj."*

A 10 pont elemzéséből 7 erős kritika érkezett. Sorrendben:

---

### (1) €25-45/hó hosting + maintenance — a margin-illúzió

**Gemini matek:** Ha egy fogászat havonta 2× kér változtatást (akciós implant ár, új asszisztens) és ez adminisztrációval együtt 1.5 óra/hó, akkor:
- €25 / 1.5 óra = **€16/óra effektív hourly rate**
- *"Ez nem egy skálázódó szoftvercég, ez egy alulfizetett support ügynökség."*

**Churn-veszély:** A microsite-nak nincs "sticky" funkciója. Nem ott vezetik a naptárt, nincs ott páciensadat. Ha 6 hónap múlva nem látja számszerűen, hogy hány új beteg jött → **első költségcsökkentésnél lemondja**.

**Számszerű figyelmeztetés:** Ha havi churn eléri **6%-ot**, a 24. hónapban nem 120 ügyfélnél vagy → folyamatosan a lyukas vödröt foltozod.

---

### (2) Unsolicited demo taktika — Jogi aknamező

**A GDPR-csapda:**
- **Grt. (reklámtörvény):** Magyarországon B2B-ben sem küldhetsz kéretlen elektronikus hirdetést egyéni vállalkozónak előzetes hozzájárulás nélkül
- **Sok kis fogászat = egyéni vállalkozó**
- **Személyes email cím (dr.kovacs@gmail.com)** → biztos GDPR-megsértés
- *"A fogorvosok rendkívül érzékenyek a jogi megfelelésre."*

**Reputációs veszély:** Ha a fogorvosok spambe jelentik a domainjeidet, a **fő ExarLabs brand email-kézbesíthetősége** szenved.

**[Implication]:** Az "unsolicited demo" taktika a jelenlegi formában **NEM mehet élesre**. Vagy:
- Soft consent first (LinkedIn outreach → engedélykérés → demo)
- Vagy event-alapú (előadás → névjegykártya gyűjtés → demo)
- Vagy partner-csatorna (kamara, ajánlások)

---

### (3) "Vanilla HTML, nincs lock-in" — Az érv VISSZAFELÉ sül el

**Gemini insight:**
> *"Egy fogorvost egyáltalán nem érdekli a vendor lock-in vagy a vanilla HTML. Fogalma sincs, mi az. Számára a 'nincs lock-in' nem előny, hanem fenyegetés: 'Ha elmegyek tőletek, kapok egy zip fájlt kóddal, amihez nem értek, és kereshetek egy másik fejlesztőt, aki horror áron nyúl hozzá?'"*

**Kulcs reframe:** Az SMB szektorban a lock-in hiánya a **biztonságérzet hiánya**. Ők pont azt akarják, hogy *"fogja a kezüket örökre"*.

**[Implication]:** A "nincs lock-in" pillért **NE használjuk** sales-érvként SMB-felé. Tech-savvy felé igen (későbbi vertikumok: ügynökségek, fejlesztők). SMB-nek a value prop legyen "mi gondoskodunk rólatok mindig", NEM "elvihetitek bármikor".

---

### (4) Done-for-you skálázhatóság — Időcsapda matek

**Gemini számítás:**
- Havi 5 új ügyfél cél
- @ 5% konverzió (zseniális hideg outreach) → **havi 100 demó kell**
- 100 demó × min. 2 óra/demó (még AI-jal is) = **200 óra/hó tiszta gyártás**
- + sales + számlázás + support meglévő 40 ügyfélnek = **lehetetlen egyedül**

**Burnout-prognózis:** *"Szabolcs a 4. hónapban ki fog égni, és a növekedés megáll."*

**[Implication]:** Vagy:
- (a) Csökkenteni a növekedési célt (havi 2-3 új ügyfél kezdetben)
- (b) Korábbi team-scaling (3-4. hónaptól virtuális asszisztens / junior)
- (c) Automatizálni a demo-gyártást (de ez a "moat" rovására megy — már nem handcrafted)

---

### (5) AI builder verseny — A piac közepe szorul

**Gemini comparison:**

| Megoldás | Egyszeri | Havi | Pozicionálás |
|---|---|---|---|
| **Microsite Factory** | €300-500 | €25-45 | "Prémium köntösbe bújtatott sablon" |
| Hostinger AI / Wix | €0 | €3-10 | DIY |
| Helyi kis ügynökség | €800-1500 | €10-20 | Személyes, egyedi, SEO |

**Gemini kritika:** A piac közepe nagyon vékony — a fukar fogászat DIY-jal megoldja, a prémium személyes ügynökségtől vesz.

**Moat-realitás:**
> *"Az egyetlen valódi moat az értékesítési csatorna és a személyes bizalom lehetne – de a te modelled pont egy skálázható, személytelen gyárat céloz meg."*

**[Implication]:** Vagy lemegyünk a DIY/sablon szintre (de akkor commodity vagyunk), vagy felmegyünk a "személyes ügynökség" szintre — **a középső sávot újra kell pozícionálni**.

---

### (6) Magyar fogászatok — "Unokaöccs-szindróma"

**Gemini kettéosztása:**

**A fukar / kezdő típus:**
- Megoldja az unokaöccs, a recepciós lány barátja, vagy elég neki a Google Maps profil
- **NEM fog €400 + havi díjat fizetni**

**A prémium típus:**
- Nagy klinikák saját marketinges + integrált rendszer (FlexiDental stb.)
- Egyedi design, SEO ("fogászat Budapest" first place)
- **A €300-500-os ajánlat túl "olcsó" és komolytalan**

**A piac közepe nagyon vékony.**

**[Implication]:** Az ICP-t újra kell definiálni: **NEM "magyar fogászatok" általában**, hanem egy specifikus alszegmens:
- ❓ Talán: 2-5 fős privát rendelő, már van weboldal de 5+ éves, dental tourism-ra is nyitott, alapító 30-50 éves
- Validálandó: 8-10 interjúval (ahogy Perplexity is javasolta)

---

### (7) Industry Cognition Layer — Túlbecsült buzzword

**Gemini lehúzza:**
> *"Ez egy jól hangzó buzzword, de a gyakorlatban mit jelent? Hogy az AI promptba be van írva: 'Írj szöveget egy fogászatnak, legyen benne implantológia és fogfehérítés'. Ezt a 'tudást' bármelyik konkurens egy délután alatt lemásolja egy rendszerprompttal."*

**Miért nem moat:** Nem zárt, védett orvosi adatbázisból dolgozunk, hanem publikus Google Maps adatokból.

**[Implication]:** A "Dental Pack" mint moat-érv **gyenge**. Strategist (ChatGPT) ezt felülbecsülte. Igazi moat-jelöltek: portfolio (élő referenciák), lokális kapcsolat, ügyfél-bizalom — DE EZEK NEM SKÁLÁZHATÓK gyorsan.

---

### (8) Self-service halasztása — Copycat-veszély

**Gemini hangsúlya:**
> *"A legnagyobb kockázatod nem az, hogy lefejlesztik a szoftveredet, hanem hogy egy copycat gyorsabban és agresszívebben fog értékesíteni. Ha egy ex-értékesítő meglátja a modelledet, felbérel 3 indiai egyetemistát, és napi 200 demót küld ki a te havi 5-öddel szemben, elveszted a piacot."*

**[Implication]:** A self-service late-pivot stratégia kockázatos. A "manual concierge MVP" csak akkor működik, ha közben **brutálisan agresszív outreach** zajlik (ami GDPR-jogilag pont nem lehetséges — lásd 2. pont). **Catch-22.**

---

### (9) Magyar/EU számlázás — ÁFA-trap

**Gemini matek:**
- Havi €5,000 × 12 = **€60,000/év ≈ 24 millió HUF/év**
- Magyar **AAM (alanyi adómentesség) határa 12 millió HUF/év**
- **~50 ügyfélnél már átléped** → ÁFA-kötelezett

**Két opció amikor átlépsz:**
- (a) Felemeled az árat 27%-kal → €25 → €31.75/hó (versenyképtelenebb a $3 Hostinger ellen)
- (b) Lenyeled a 27%-ot → margin szétmegy

**Plusz devizás komplexitás:** EUR számlázás magyar cégből → napi MNB árfolyamon NAV felé HUF-ban kell jelenteni → könyvelési overhead.

**[Implication]:** Az AAM-határ átlépésekor (~50 ügyfél) **stratégiai döntési pont**. Az árazási modellt **AAM-átlépés ELŐTT** kell úgy beállítani, hogy 27% ÁFA elférjen — pl. €30/hó kezdő ár, ne €25.

---

### (10) TOP 3 Silent Killer

#### 🔥 Silent Killer #1 — A Konverziós Illúzió (The Broken Funnel)

> *"Azt feltételezed, hogy a kész demo látványa azonnali vásárlási ingert vált ki. A valóságban a kkv-tulajdonosok ignoránsak: nem nyitják meg a linket, félnek a vírusoktól a kéretlen levelekben, vagy egyszerűen nincs idejük."*

**Realisztikus konverzió: 0.5% (NEM 5%).**

Ha 0.5%, akkor havi 5 ügyfélhez nem 100 hanem **1000 demo kell**. 1000 × 2 óra = **2000 óra/hó** → matematikailag lehetetlen.

#### 🔥 Silent Killer #2 — Az Integrációs Szakadék

> *"Egy modern fogászatnak ma már nem elég egy statikus névjegykártya-oldal. Ha a microsite nem szinkronizálódik a meglévő pácienskezelő szoftverükkel, akkor a recepciósnak manuálisan kell másolnia az adatokat. Amint rájönnek, hogy a microsite plusz munkát generál, lemondják."*

**Implication:** A booking complexity boundary nem csak árban van — **operatív integrációban is**. A pácienskezelő szoftvert (FlexiDental, Dentasoft, stb.) ismerni, mappingelni kell. Ez új research-igény.

#### 🔥 Silent Killer #3 — Sub-Brand Reputációs Kannibalizmus

> *"Ha az ExarLabs egy komoly, magas hozzáadott értékű tech/AI stúdió, és a piac összeköti a nevét a 'kéretlen e-mailekben spammelő, olcsó fogászati sablonoldalakat gyártó' projekttel, az súlyos bizalomvesztést okozhat a fő üzletág magasabb árazású ügyfeleinél."*

**Implication:** **Külön brand** kell, NEM ExarLabs sub-brand. Pl. "Sitesmith.hu", "Fogászati-jelenlét.hu", "Praxisweb.hu" — domain és arc legyen szétválasztva.

---

## 🎯 Gemini-után-szintézis — Mit változtat a BMC-n?

### 🔴 KRITIKUS megszorítások (azonnal beépítendő)

| Eddig | Most |
|---|---|
| "Unsolicited demo" sales taktika | **JOGILAG NEM mehet** — soft consent / event / partner-csatorna kell |
| "Nincs lock-in" mint value prop | **NE használjuk** SMB-felé — biztonságérzet kérdés |
| "99% margin" | **~60% reális**, korrigálva |
| "5 új ügyfél/hó egyedül" | **2-3 fenntarthatóan**, team scaling 3. hónaptól |
| "Industry Cognition Layer = moat" | **Gyenge moat** — portfolio + lokális kapcsolat erősebb |
| "ExarLabs sub-brand" | **Külön brand** — reputációs kannibalizmus elkerülése |
| "€25/hó belépőszint" | **€30/hó kezdőár** — ÁFA-átlépés bekészítve |
| "120 ügyfél 24 hónap alatt" | **Realisztikus: 60-80 ügyfél**, ha churn 5% és outreach jogszerű |

### 🟡 ÚJ stratégiai követelmények

1. **GDPR-megfelelő outreach modell kidolgozása** (LinkedIn / event / partner)
2. **ICP szűkítés** — alszegmens 8-10 interjúval validálva
3. **Pácienskezelő szoftver integráció research** (FlexiDental, Dentasoft stb.)
4. **Külön brand és domain** — sub-brand szétválasztása ExarLabs-tól
5. **AAM/ÁFA átlépési pont kezelése** az árazásban
6. **Sticky funkció keresése** — analytics dashboard / mini-CRM, ami megtartja az ügyfelet
7. **Realisztikus konverziós várakozás:** 0.5% nem 5% → outreach volumét újra kell tervezni

### 🟢 Ami áll a kritikák után

- ✅ Magyar AI-gap mint piaci rés (Perplexity validálta)
- ✅ Fogászat mint első vertikum (Perplexity is)
- ✅ Done-for-you mint híd-szerep (Perplexity)
- ✅ Dental tourism extra szegmens
- ✅ Transformation ladder long-term opportunity (Strategist)
- ✅ Composable architecture (Strategist + Researcher)

---

## 📋 Validációs feladatok prioritás-sorrendben

### P0 (hét 1)
- [ ] 20 magyar fogászat manuális auditja (Perplexity javasolta)
- [ ] **8-10 fogász/praxisvezető interjú** — KÖZPONTI VALIDÁCIÓ az ICP-re és az "unokaöccs vs prémium" kérdésre
- [ ] Pácienskezelő szoftverek listája + integráció lehetőség research
- [ ] GDPR/Grt jogi konzultáció (egyórás ügyvéd) — milyen outreach jogszerű

### P1 (hét 2-4)
- [ ] 2 különböző landing oldal teszt: "microsite 10 nap alatt" vs "új páciensekre optimalizált fogászati weboldal"
- [ ] AAM-átlépés árazási modell finomítás
- [ ] Külön brand + domain regisztráció

### P2 (hét 4-8)
- [ ] Sticky funkció prototípus (analytics dashboard MVP)
- [ ] Team scaling terv (3. hónaptól)
- [ ] Copycat-védelem (ne legyen mit lemásolni — workflow + lokális kapcsolat fontosabb mint tech)

---

## Iteráció

- **v1 (2026-05-16):** Claude pre-validation
- **v2 (2026-05-16):** Gemini Validator brutális kritika integrálva → fundamentális reframek azonosítva
- **v3 [tervezett]:** ChatGPT második kör — reakció a Gemini findings-ra (különösen unsolicited demo átalakítás)
- **v4 [tervezett]:** Élő piaci validáció (interjúk) után
