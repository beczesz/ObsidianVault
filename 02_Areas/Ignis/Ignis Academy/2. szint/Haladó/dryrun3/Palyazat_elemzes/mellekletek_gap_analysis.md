---
title: "Mellékletek — Gap Analízis (TransOffice ↔ AFM Mobilitate Verde IMM 2026)"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Gap-analízis a TransOffice AFM Mobilitate Verde IMM 2026 pályázatához, amely dokumentálja a 27 szükséges melléklet állapotát a beadás (12 dokumentum) és szerződéskötés (15 dokumentum) szakaszaiban. Szabolcs komplex felsorolása részletes státussal, felelősségi körökkel és ügyintézési időbecslésekkel olyan vezetők számára, akik a"
description_source: auto
description_hash: 3520238ad70bcdff
id: c4222f81-8104-4779-a399-bf7c07287ae6
index_schema_version: 1
bdos_index: true
---
# Mellékletek — Gap Analízis (TransOffice ↔ AFM Mobilitate Verde IMM 2026)

**Forrás:** Ghidul Solicitantului v1.0 (2026-03-16), kapitolul 7.4 (anexe la depunere) + 7.6 (anexe la contractare)
**Dátum:** 2026-05-14
**Készítette:** Szabolcs (OM)

---

## Áttekintés

Az AFM **két szakaszban** kéri a mellékleteket:

1. **Cap. 7.4 — A BEADÁSKOR (2026-08-31-ig):** 12 számozott dokumentum-csomag, minden PDF-ben, a jogi képviselő digitális aláírásával, MySMIS2021-ben feltöltve. Egyenkénti max. 20 MB / file, össz. max. 400 MB.
2. **Cap. 7.6 — A SZERZŐDÉSKÖTÉSKOR (csak ha nyertünk, a contractare-meghívástól 15 munkanapon belül):** 15 további dokumentum.

Összesen **27 melléklet-csomag**, plusz a Studiul de oportunitate (Anexa 6) önmaga 8 fejezetes ~30 oldalas szöveg. Az alábbiakban mind a 27-et átveszem, plusz a 4 modell-anexát (3, 6, 7, 11, 12, 13, 14) amelyek a beadás strukturális vázát adják.

---

## A) MELLÉKLETEK A BEADÁSKOR (cap. 7.4) — 12 dokumentum-csomag

### M-01. Declarația unică (Anexa standard, MySMIS-generált)

| Mező | Érték |
|------|-------|
| **Mit fed le** | Minden eligibility-feltétel önbevallása + de minimis történet + IMM-besorolás + TVA-deductibilitás + összeférhetetlenség + dokumentum-másolat hitelessége |
| **Forma** | A MySMIS automatikusan generálja, a jogi képviselő digitális aláírásával hitelesíti |
| **TransOffice állapot** | ⚠️ RÉSZBEN — magát a deklarációt automatikusan generáljuk, **de a tartalma blokkolódik** addig amíg nem tisztáztuk: ki a hivatalos jogi képviselő (István vs. Márton) + Mártonnak/Istvánnak van-e érvényes certificat digital calificat |
| **Honnan** | MySMIS2021/SMIS2021+ portál (mysmis2021.gov.ro) |
| **Ki intézi** | **Márton** (személyesen kell, mint reprezentant legal) |
| **Ügyintézés** | 2-5 nap a certifikátum beszerzésére (certSign / DigiSign / Trans Sped / Alfasign), maga a deklaráció kitöltés ~2 óra |

### M-02. Pénzügyi adatok — utolsó 2 zárt fiscal év (Bilanț, Cont P&L, Date informative — Formular 10/20/30)

| Mező | Érték |
|------|-------|
| **Mit fed le** | Pénzügyi stabilitás (CR-09) + IMM-küszöb (CR-04) bizonyítása |
| **Forma** | PDF, ANAF-letétbe-helyezés bizonyítékával (electronic ANAF mention vagy hivatalos recipisă) |
| **TransOffice állapot** | ⚠️ RÉSZBEN — **A `05_Penzugy/eves_jelentes_2020-2022.xlsx` fájlunk csak Ilona kézzel összeállított összegzése, NEM az ANAF-os Formular 10/20/30 hivatalos állomány.** A 2024 és 2025 zárt évek hivatalos formulárjai Mihaela külsős könyvelőnél vannak. |
| **Honnan** | Mihaela (külsős könyvelő) — emailben |
| **Ki intézi** | **Enikő** (vele dolgozik együtt — már megfogalmazott email az ő felé, lásd `00_AFM_Palyazat_2026/meeting_20260825/04_followup_email_eniko.md`) |
| **Ügyintézés** | 3-7 nap (Mihaela tudja közvetlenül kiküldeni, ha lezárt, le-PDF-elt változatban van; ha 2025 még nem volt deponálva, balanță analitică + külön declarație) |

### M-03. Cartea tehnică + forgalmi engedélyek + RCA + ITP — minden meglévő ICE jármű

| Mező | Érték |
|------|-------|
| **Mit fed le** | CR-07 bizonyítása: a cég rendelkezik már parc auto-val, melyik ICE-eket vonjuk ki (1:1 înnoire) |
| **Forma** | Forgalmi engedély másolata (talon ARR/RAR) + RCA polisz másolat + ITP igazolás másolat — minden járműre, PDF-ben |
| **TransOffice állapot** | ❌ NINCS — egyetlen járműdokumentum sincs a digitális mappában. Márton "3 vagy 4" autót becsült. |
| **Honnan** | Fizikai dokumentumok az autóban / székhelyen / Eniknél; ha biztosítás lejárt, a biztosítótársaságok ügyfélportáljáról; ha ITP lejárt, RAR/ITP állomáson megújítani |
| **Ki intézi** | **Szabolcs + Attila** (raktáros, ismeri a fizikai autókat) |
| **Ügyintézés** | 1-2 nap a feltérképezésre + scanrelésre; ha valamelyik biztosítás vagy ITP lejárt, +1-3 nap megújítás |

### M-04. Plan de înnoire a parcului auto — Anexa 13 (model standard)

| Mező | Érték |
|------|-------|
| **Mit fed le** | A 1:1 înnoire korelácja: melyik ICE-t váltjuk melyik új BEV-re; tervezett kalendárium IE-01-től IE-08-ig |
| **Forma** | Az AFM által biztosított Word/Excel sablon kitöltve, PDF-ként aláírva |
| **TransOffice állapot** | ❌ NINCS — még nem létezik. Akkor írható meg, ha M-03 megvan ÉS Márton döntött a 2 új BEV típusáról |
| **Honnan** | Saját kitöltés a sablon alapján (Anexa 13 a Ghid 84-85. oldalán) |
| **Ki intézi** | **Szabolcs** (összesít) — input Mártontól (BEV-választás) és Szabolcstól (M-03) |
| **Ügyintézés** | 4-6 óra önállóan, miután minden input megvan |

### M-05. Studiul de oportunitate / Plan de afaceri — Anexa 6 (model recomandat)

| Mező | Érték |
|------|-------|
| **Mit fed le** | A pályázat **érdemi része**: a cég bemutatása, indoklás, technikai megoldás, TCO-elemzés 5 évre, cash-flow, kockázatelemzés, foglalkoztatási hatás, fenntarthatóság |
| **Forma** | 8 fejezet, max. 30 oldal összesen, PDF (a Ghid pontosan szabályozza max. oldalszámot fejezetenként) |
| **TransOffice állapot** | ❌ NINCS — még semmi sincs ebből megírva. **Ennek hiánya = automatikus elutasítás** (a Ghid 7.4.5 explicit kimondja: "Lipsa acestui document NU poate face obiectul unei solicitări de clarificări") |
| **Honnan** | Saját megírás. Esetleg külsős consultant bevonható (a costuri sunt eligibilis în categoria C, max. 4% din proiect) |
| **Ki intézi** | **Szabolcs** (lead) + Márton (tartalom-input) + Mihaela (pénzügyi previziune) |
| **Ügyintézés** | **15-25 munkanap tényleges munka**, ez a beadás munka-csúcsa |

### M-06. Macheta de analiză și previziune financiară — Anexa 7 (model standard)

| Mező | Érték |
|------|-------|
| **Mit fed le** | 5 év pénzügyi modellje: bilanț previzionat, P&L previzionat, cash-flow havi az implementációra + éves a durabilitásra, indikátorok (EBITDA-marja, ROA, ROE, lichiditate, D/E), beruházási hatékonyság (NPV, IRR, megtérülési idő) |
| **Forma** | Excel sablon kitöltve, PDF-be exportálva, aláírva |
| **TransOffice állapot** | ❌ NINCS — még nincs előrejelzési modell |
| **Honnan** | Saját megírás. Mihaela vagy egy pénzügyi consultant kell hozzá (egyik sem triviálisan készíthető Excelben adat nélkül) |
| **Ki intézi** | **Mihaela** (külsős könyvelő) — vagy ha nem éri rá, externál consultant. Szabolcs koordinál. |
| **Ügyintézés** | 5-10 nap, miután M-02 és Márton üzleti tervezete kész |

### M-07. Specificații tehnice ale vehiculelor electrice + min. 3 árajánlat dealer-ektől

| Mező | Érték |
|------|-------|
| **Mit fed le** | Mindkét tervezett BEV-re: gyártói data sheet (autonómia WLTP, akku kapacitás, motor teljesítmény, AC/DC töltési idő, garancia) + CE-konformitási tanúsítvány + RAR omologare + **min. 3 db árajánlat különböző hivatalos forgalmazótól** |
| **Forma** | PDF-ek: dealer árajánlatok eredetiben + összesítő centralizator (Anexa 7-be vagy Anexa 14-szerű táblázatba) |
| **TransOffice állapot** | ❌ NINCS — semmi |
| **Honnan** | Helyi és országos hivatalos BEV-forgalmazók (Tesla, BYD, Volkswagen Renault, Hyundai, Dacia stb. dealerei) |
| **Ki intézi** | **Szabolcs** — emailben/telefonon kérni 3-3 ajánlatot, miután Márton kiválasztotta a két modellt (M1: pl. autoturism city; N1: pl. utilitar dostavă) |
| **Ügyintézés** | 2-3 hét — a dealerek lassan reagálnak, nyári időszak figyelembe vétele |

### M-08. Specificații tehnice ale stațiilor de reîncărcare + min. 3 árajánlat ANRE-engedélyes telepítőktől

| Mező | Érték |
|------|-------|
| **Mit fed le** | A tervezett töltőre: gyártói data sheet, EN 61851 + EN 62196 megfelelési tanúsítvány, min. 24 hónap garancia, **min. 3 árajánlat** különböző ANRE-engedélyes telepítőktől |
| **Forma** | Mint M-07, PDF-ek |
| **TransOffice állapot** | ❌ NINCS |
| **Honnan** | Romániai ANRE IIB+ engedélyes EV-töltő telepítők (pl. Renovatio, E-Charge, ABB, Schneider Electric ezekhez fűződő hálózat) |
| **Ki intézi** | **Szabolcs** — kell egy IT/elektromos beszállító-kapcsolat. **InfoProg Solutions** (Kovács Attila, az ügyfelünk!) tud-e ajánlani? |
| **Ügyintézés** | 2-3 hét |

### M-09. Aviz tehnic de racordare la rețeaua electrică (vagy declarație că nu este necesar)

| Mező | Érték |
|------|-------|
| **Mit fed le** | A telephely villamos hálózati csatlakozása alkalmas-e a tervezett töltő telepítésére. Két alternatíva: (a) **Aviz tehnic** Distribuție Energie Electrică Romania-tól; vagy (b) **Declarație pe propria răspundere** ANRE-engedélyes telepítő aláírásával hogy a meglévő bekötés is elég |
| **Forma** | PDF, hivatalos elosztói pecséttel |
| **TransOffice állapot** | ❌ NINCS — semmi információ a telephely villamos kapacitásáról |
| **Honnan** | Distribuție Energie Electrică Romania, Sucursala Odorheiu Secuiesc (online kérelem) — VAGY egyszerűbben Variant (b) |
| **Ki intézi** | **Szabolcs** — Variant (b) gyorsabb (csak az M-08-ban kiválasztott telepítő aláírja) |
| **Ügyintézés** | (a) 30-60 nap; (b) 1-3 nap (ha kis kapacitású AC töltő, valószínűleg elég) |

### M-10. Documentele care dovedesc dreptul asupra imobilului (kivonat / szerződés)

| Mező | Érték |
|------|-------|
| **Mit fed le** | CR-08: a pályázó jogosult-e az ingatlanon töltőt telepíteni. Beadáskor "extras curent" elég (extras de carte funciară, contract de închiriere, contract de comodat stb.) |
| **Forma** | PDF — beadáskor pl. a 2018-as bérleti szerződés másolata. Contractare-nál friss (max 30 napos) extras de CF kell + a tulajdonos írásos hozzájárulása a töltő telepítéséhez |
| **TransOffice állapot** | ⚠️ RÉSZBEN — a 2018-as szerződés megvan (`01_Szerzodesek/ingatlan/szerzodes_chirie_TransOffice_2018.docx`), de **csak 2028-04-30-ig szól**. **Ez a CR-08 problémája — lásd Eligibility Check Top 3 Risk #1.** Béla bácsi 2025-02-26-i emailje hozzátartozó (`07_Email_archivum/`), de az nem helyettesíti a hivatalos act adițional-t. |
| **Honnan** | (a) Beadáskor: a meglévő szerződés + Béla bácsi-email. (b) **Contractare előtt**: act adițional 2035-ig + új extras CF — Andrei Munteanu közjegyzőnél (Béla közjegyzője). |
| **Ki intézi** | **Márton** (Béla bácsi-kontakt) → Andrei Munteanu közjegyző |
| **Ügyintézés** | 2-3 hét közjegyzői ütemezéstől függően |

### M-11. Centralizator privind rezonabilitatea costurilor

| Mező | Érték |
|------|-------|
| **Mit fed le** | Egyetlen Excel/PDF táblázat ami összesíti az M-07 és M-08 árajánlatokat: melyik a választott, miért (ha nem a legolcsóbbat választjuk, indoklás) |
| **Forma** | Excel sablon → PDF (Anexa 7-tel rokon, de külön dokumentum) |
| **TransOffice állapot** | ❌ NINCS — automatikusan készíthető lesz, miután M-07 és M-08 megvan |
| **Honnan** | Saját kitöltés |
| **Ki intézi** | **Szabolcs** |
| **Ügyintézés** | 2-3 óra |

### M-12. Certificat constatator emis de ONRC (max 30 napos)

| Mező | Érték |
|------|-------|
| **Mit fed le** | Cégadatok: CUI, jogi forma, capital social, asociats/acționari, CAEN-kódok, jogi képviselő, aktuális státusz |
| **Forma** | ONRC online (InfoCert) PDF, max. 30 napos |
| **TransOffice állapot** | ❌ NINCS friss — a meglévő dokumentumok között nincs ilyen |
| **Honnan** | ONRC.ro online portál (InfoCert szolgáltatás), 30 RON körüli díj, azonnal letölthető |
| **Ki intézi** | **Szabolcs** — gyors online ügylet |
| **Ügyintézés** | 1 óra (online, kártyás fizetés, azonnali letöltés). **DE: max 30 napos érvényesség → csak ~2026 augusztus elején érdemes lekérni.** |

---

## B) MELLÉKLETEK A SZERZŐDÉSKÖTÉSKOR (cap. 7.6) — +15 dokumentum

> A contractare-fázis csak akkor releváns, ha pontszámunk a 60-as küszöböt elérte ÉS bekerültünk az alocare-ba. Csak emlékeztető-listaként szerepel itt — minden tételt majd a contractare-meghívástól számított 15 munkanapon belül kell küldeni.

| Kód | Tétel | Hol szerezhető be | Időigény |
|-----|-------|-------------------|----------|
| C-01 | Documente statutare actualizate (act constitutiv, statut, CIF) | Cég saját irattára / közjegyző | 1 hét |
| C-02 | Act de identitate a reprezentantului legal | Márton (vagy István) magán-CI/passport | azonnal |
| C-03 | Documente actuale dovadă drept asupra imobilului (extras CF max 30 napos + act adițional 2035-ig) | OCPI Odorheiu + Andrei Munteanu közjegyző | 2-3 hét |
| C-04 | Hotărârea/Decizia adunării generale a asociaților privind aprobarea proiectului | Cég belső dokumentum (Márton egyedüli asociat? → akkor saját döntés) | 1-3 nap |
| C-05 | Certificate de atestare fiscală ANAF (max 30 napos) | ANAF Harghita | 3-5 nap online |
| C-06 | Certificat fiscal Direcția de Impozite și Taxe Locale (max 30 napos) | Primăria Odorheiu Secuiesc | 3-5 nap |
| C-07 | Cazier fiscal (max 30 napos) | ANAF | 3-5 nap |
| C-08 | Cazier judiciar al reprezentantului legal (max 30 napos) | Inspectoratul de Poliție / online | 3-7 nap |
| C-09 | Plan de amplasare a stațiilor (proiect tehnic detailat) | Tervezőmérnök (proiectant autorizat) | 2-4 hét |
| C-10 | Dovada capacității financiare (extras de cont actual / scrisoare bancară) | Bank | 1-3 nap |
| C-11 | Declarație pe propria răspundere ajutoare de minimis primite (Anexa 11) | Saját kitöltés Mihaela adatai alapján | 1 nap |
| C-12 | Plan de monitorizare al proiectului (Anexa 14) | Saját kitöltés | 1-2 nap |
| C-13 | Cele mai recente situații financiare (ha közben lettek frissítettek) | Mihaela | 2-3 nap |
| C-14 | Declarația privind încadrarea în categoria IMM (frissített, ha változott) | Saját kitöltés | 1 nap |
| C-15 | Polițe de asigurare (RCA + CASCO) az új BEV-ekre, ha már átvettük | Biztosítótársaság | 1-2 nap |

---

## C) Külön kiemelt: Anexa 12 — Lista de verificare DNSH simplificată

A Ghid 20. fejezete szerint a < 100K EUR projektekre ezt a sablont kell kitölteni (6 környezeti céllal, mindegyikre DA/NU + ≤100 szavas indoklás). **TransOffice projektje becslés szerint ~84K EUR — ALATTA marad a 100K EUR-nak**, így a simplificată elég, **nem kell a detailat változat** (ami az AFM külön doksiban van, sokkal hosszabb).

**TransOffice DNSH-státusz előzetes kiértékelés:**

| Cél | Várható válasz | Megjegyzés |
|-----|----------------|------------|
| 1. Atenuarea schimbărilor climatice | ✅ DA × 3 | BEV (zero emisii utilizare); semmi fosszilis támogatás; net-pozitív CO2-mérleg (Anexa 8 számítás alapján) |
| 2. Adaptarea la schimbările climatice | ✅ DA × 2 | Telephely Odorheiu Secuiesc — nem inundabil, nem alunecări-zónában; AC töltő -20°C+50°C tipológiájú lesz |
| 3. Utilizarea durabilă a apelor | ✅ DA × 2 | Töltő nem fogyaszt vizet; nincs uzate ape generálva |
| 4. Tranziția către o economie circulară | ✅ DA × 2 | ICE-ek Legea 212/2015 szerinti casare-ba (REMAT operator); akku end-of-life UE 2023/1542 alapján kezelendő |
| 5. Prevenirea și controlul poluării | ✅ DA × 2 | NOx/PM csökkentés helyi szinten (BEV-csere); zaj < HG 321/2005 szint |
| 6. Protejarea biodiversității | ✅ DA × 2 | Telephely meglévő ipari/kereskedelmi terület, nem Natura 2000-ben; semmi új földmunkálat |

**Mind a 13 kérdésre DA várható → DNSH OK.**

---

## D) Beszerzési ütemterv (collapsed view)

| Hét (2026) | Mit kell beszerezni | Felelős |
|-----------|--------------------|---------| 
| **W20-21 (máj 18-31)** | M-03 járműleltár + scan; certificat digital Mártonnak | Szabolcs / Márton |
| **W22-23 (jún 1-14)** | Mihaelától M-02 (2024+2025 hivatalos zárások); Márton döntés a 2 BEV típusáról; act adițional Béla bácsival | Enikő / Márton |
| **W24-26 (jún 15 — júl 5)** | M-07 + M-08 (3-3 árajánlat); aviz tehnic / declarație ANRE installer-tól (M-09) | Szabolcs |
| **W27-30 (júl 6 — aug 2)** | M-05 (Studiul de oportunitate / Plan de afaceri) megírás | Szabolcs + Márton |
| **W31-32 (aug 3-16)** | M-06 (Macheta financiară) Mihaelával; M-04 (Plan înnoire); M-11 (Centralizator) | Mihaela / Szabolcs |
| **W33 (aug 17-23)** | M-12 (Certificat constatator friss); M-01 (Declarația unică); összes anexa csomagolása PDF-be | Szabolcs |
| **W34 (aug 24-28)** | Belső review + javítások + MySMIS-feltöltés | Mindenki |
| **W35 (aug 31)** | **BEADÁS** | Szabolcs |

---

**Megjegyzés:** A teljes 27-tételes lista alapján a TransOffice **jelenleg 0 db** beadás-kész melléklettel rendelkezik (a 2018-as szerződés és a Béla-email csak részben fedi a M-10-et). Reális timeline 12-14 hét — **van rá időnk** (ma még 15+ hét van), de **azonnali start kell**.
