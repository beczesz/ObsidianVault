# 2026-05-07 — Termelői meeting döntések (Mikado-i ülés)

> **Forrás:** `Products/meetings/DH - Mikado - Termek variációk-transcript-full.srt`
> **Hossz:** ~43 perc
> **Résztvevők:** Speaker 1 (Szabolcs — kérdező), Speaker 2 (Termelő — fő info forrás), Speaker 3 (Termelő — kiegészítő), Speaker 4 (Háziasszony — vásárlói perspektíva)
> **Cél:** Mind a 37 termék variációinak végigvétele + új termékek azonosítása + foto-/marketing-stratégia.

---


---

## ✅ Megerősítések (Szabolcs visszajelzése — 2026-05-07 este, fotók után)

1. **Csirke `mellcsont` ≠ önálló termék.** A „Csirke Mellcsont" amit a transcriptben hallottam, valójában a **„Csirke mell csont és bőr nélkül"** termék (kód `ACS04`, 34 RON/kg). Tehát NEM 4, hanem 3 csirke termék — plusz amit a belső lista ad (ld. lent).
2. **Sertés Bordacsont = KÉT különálló termék** (megerősítve, transcript-tel egyezik):
  - `0221 Sertés Bordacsont` (kisebb darabok) — 12 RON/kg
  - `0222 Egész Bordacsont` — 15 RON/kg
  - A Sheet logikája (1 termék 2 árponttal) **NEM** lesz alkalmazva — két különálló termék kell legyen.
3. **Sheet hiba (row 7, Sertés Csülök) — javítandó.** Az „Új Név" és „nume produs" mezők a row 6-ról másolódtak be (Sertés Csontos Karaj). A helyes RO név: `Ciolan porc`. Szabolcs javítja a Sheet-ben.

> **Ezen kívül ma kaptam egy belső termékkód-listát (Baczo Annamaria, Sziget — két oldal fénykép). Lásd:** `Products/meetings/2026-05-07_internal-product-codes.md`

---
## 📋 Per-termék döntések (a beszélgetés sorrendjében)

### 1. Sertés Nyakaskaraj `nyakas_karaj` — kg, **TÖBB OPCIÓ**
- **Forma** opció (single_select):
 - `sima` — vékony szelet, **MINIMUM újnyi** vastag (vékonyabbnál „cipőtalp érzet")
 - `dupla` — két szelet középen egyben, kinyitva, potyolva (nagyobb, férfias)
- **Pácolás** opció (single_select, 3 érték):
 - `nem_pacolt`
 - `hagyomanyos` — só, bors, fokhagyma
 - `barbecue` — paradicsomos, BBQ-szerű (új pác)
- **Foto kell** mindhárom variációhoz, zöld + piros zöldséggel (saláta, paradicsom)

### 2. Sertés Bélszín `sertes_belszin` — hybrid, ár kilóra
- **Méret variáció: NINCS** ("nagyon minimális eltérés, max 5 deka")
- **Felülbírálás:** a v1.0 sample MD-ben van `meret` opció — KIVENNI
- ~50-60 deka körüli darabok

### 3. Sertés Bordacsont `sertes_borda_csont` — kg, **12 RON**
- Kisebb darabok (a kicsontozott combhoz tartozó bordák)
- ⚠️ KÜLÖN termék az „Egész Bordacsont"-tól!

### 4. Sertés Egész Bordacsont `sertes_egesz_bordacsont` — kg, **15 RON**
- A hasból egészben kivéve, mielőtt feldarabolnák
- ⚠️ KÜLÖN termék az „bordacsont"-tól!

### 5. Sertés Comb `sertes_comb` — kg, **25 RON**, „kotlét csontnélkül"
- **Variációk: NINCSENEK** (felülbírálás!)
 - Régen szokták szeletelni → ma alig
 - Nem szokták kockázni (a háziasszony saját maga előkészíti, zsiradékot levesz, főleg gyermekek miatt)
- Csak simán kilóra
- Felhasználás: **pörkölt** (fő)
- Megjegyzés: **comb tovább fő mint a lapocka** (lapocka külön termék)

### 6. Sertés Csontos Karaj `sertes_csontos_karaj` — hybrid, ~1.5 kg/db, kg-ra ár
- **Szeletelés: szeletelve adják ALAPBÓL** (a csontot grillhez hagyják)
- **Pácolás** opció (3 érték): `nem_pacolt`, `hagyomanyos`, `barbecue` — bármelyik
- **Vastagság variáció: NINCS** („ahogy fogja adni a borda")
- Felhasználás: **bárbekű, grillezés**

### 7. Sertés Csülök `sertes_csulok` — hybrid, ~1.5 kg/db, kg-ra ár
- **Méret** opció (single_select, 3 érték): ✅ MEGERŐSÍTVE
 - `kisebb` — ~1.2-1.4 kg
 - `kozepes` — ~1.4-1.6 kg
 - `nagyobb` — ~1.6-1.8 kg
- Megjegyzés: „nagyon kicsi a különbség, kb. 10 deka", de **vásárlók kérik** („mama a kisebbiket szereti")

### 8. Sertés Fehér Karaj `sertes_feher_karaj` — kg, csontnélküli, szalonna nélküli
- **Szeletelve** (Bécsi szelet, „szeletnek való")
- **Pácolás** opció: lehet pácolva is
- Felhasználás: Bécsi szelet, **flekken** (sovány szereti), szelet
- Pörköltnek **NEM ideális**

### 9. Sertés Hasrész — 🔴 **HÁROM/NÉGY ELKÜLÖNÜLÖ TERMÉK** (eddig egynek tudtuk!)
- **a) `sertes_hasresz_csontos_borr`** — egész hasrész CSONTOS+BŐRÖS, **24,50 RON/kg** — *„rajta van a bőr, rajta a csont"*
 - Variáció: **NINCS** (csak kilóra, „nem szeletelve")
- **b) `sertes_hasresz_csont_nelkul`** — bőrös, csont nélkül, **26 RON/kg**
 - **Szeletelhető, pácolható**, lerben sütve, grillezve
- **c) `sertes_oldalas`** (sertés hasoldalas / kosztica) — csontos, **bőr nélkül**, **26 RON/kg**
 - **Szeletelhető, pácolható**
 - Román: „costiță"
- ⚠️ A pre-v1.0 archív JSON-ban csak `sertes_hasresz` (24.5 RON) van — **kettéválasztandó**

### 10. Apró Hús `sertes_apro_hus` — kg, **21 RON**
- **Variáció: NINCS**
- Régi név: „munkahús" → ma `apróhús` (érthetőbb)
- Kb. 2-3 cm-es darabok
- Felhasználás: pörkölt, gulyás, leves alap

### 11. Őrölt Hús / Darált Hús `sertes_orolt_hus` — kg, **21 RON** — **2 OPCIÓ ⚠️**
- **Alapanyag** opció (single_select, 3-4 érték):
 - `comb` — szárazabb, ragú/bolognai
 - `lapocka` — közepes (alapértelmezett)
 - `has` — zsírosabb, fasírtnak, töltelékes káposztának
 - `vegyes` (opcionális — fele-fele a comb és has között)
- **Zsírosság** opció (single_select, 3 érték):
 - `kevésbé_zsiros` — bolognai, ragú
 - `normal` — alapértelmezett (FONTOS: kell legyen normál opció, „fele-fele")
 - `zsirosabb` — fasírt, töltelékes káposzta
- **Ár fix 21 RON** — a vásárló választása NEM módosítja az árat
- **UX-megjegyzés:** opció alá kell írni magyarázatot („mit csinálsz belőle")

### 12. Sertés Szalonnás Comb `sertes_szalonnas_comb` — kg
- **Variáció: NINCS** („ezen lépjünk túl")

### 13. Sertés Toka Szalonna `sertes_toka_szalonna` — kg
- Egy termék készül belőle: **Abált Szalonna**
- (Maga a tokaszalonna nem önálló termék az appban!)

### 14. Növendék Velős Csont `velos_csont` — kg
- Felvágva tárolják → kilóra mérik
- **±10 deka** eltérés a fél kilónál (~55 deka jön ki egy fél kilós kérésre)
- **Hybrid** kezelés ajánlott (becsült 0.5 kg, ±0.1 kg)
- Felhasználás: leves, lerben kisüthető

---

## 🔥 Füstölt áruk

### 15. Füstölt Bélszín `fustolt_belszin` — darabra (~fél kg)
- **Felvágott**
- Lehet darabolni, de nem szokták

### 16. Füstölt Bordacsont `fustolt_bordacsont` — kg
- **Variáció: NINCS**

### 17. Füstölt Csülök `fustolt_csulok` — darabra (~1.5 kg, hybrid)
- **Méret** opció (kisebb, nagyobb) — kicsi a különbség, de vannak kérők

### 18. Füstölt Csülök Csont Nélkül = „Csemege Csülök" `fustolt_csulok_csont_nelkul` — darabra (~1.20-1.50 kg, hybrid)
- **Méret** opció (kisebb, nagyobb)
- Csont kivéve

### 19. Füstölt Egész Sonka `fustolt_egybe_sonka` — kg, **CSONTOS, ~5-6 kg/db**, **🌟 SZEZONÁLIS**
- **Szezonális** — csak húsvét + karácsony
- ⚠️ App-szinten beállítható: mikor látható / mikor nem
- Felszeletelhető 5 cm karikákra (elektromos fűrésszel)
- **Marketing megjegyzés**: „bükkfa fűrészporral füstölt"

### 20. Füstölt Fehér Karaj `fustolt_feher_karaj` — kg, **SZELETELVE**
- **Vastagság** opció (single_select, 3 érték):
 - `vekony` — 2 mm
 - `kozepes` — 4 mm
 - `vastag` — 6 mm

### 21. Füstölt Has `fustolt_has` — kg, szeletelhető, pácolható
- **Szeletelés** opció: **vékony / közepes / vastag** (mint a fehér karaj)
- **Pácolás** opció: lehet
- Felhasználás: leves, lerben sütés, **káposztához** (nem grill)
- **Marketing: bükkfa füst** kiemelése

### 22. Füstölt Kötözött Sonka `fustolt_kotozott_sonka` — kg, **🌟 SZEZONÁLIS**
- Hálóban tartva
- **Fél darab is adható**
- Szezonális (mint az egész sonka)

### 23. Füstölt Nyakaskaraj `fustolt_nyakas_karaj` — kg
- **Szeletelve** (csak ennyi opció — vastagság NEM)

### 24. Füstölt Oldalas `fustolt_oldalas` — kg
- **Variáció: NINCS** (nem szeletelhető)

### 25. Füstölt Szalonna `fustolt_szalonna` — kg
- **Variáció: NINCS**

### 26. Füstölt Szalonnás Sonka `fustolt_szalonnas_sonka` — kg
- **Variáció: NINCS**

---

## 🌭 Kolbász & Szalámi

### 27. Cérna Kolbász `cerna_kolbasz` — kg, 48 RON

### 28. Erdélyi Kolbász / Deák Házi Kolbász `erdelyi_kolbasz` — kg

### 29. Miccs `miccs` — kg, **40 RON**
- **Megjegyzés**: 8 db = ~fél kg, **16 db = ~1 kg** (referencia a vásárlónak)

### 30. Növendék Szalámi / Házi Szalámi `novendek_szalami` — kg, szeletelhető
- **Vastagság** opció (single_select, 3 érték): vékony / közepes / vastag
- **UX-megjegyzés:** Szabolcs azt szeretné, hogy szeleteléskor lehúzzák a bőrét — termelő szerint nem jellemző. Megjegyzés: nyitott végű — termelő képezhető hozzá.

### 31. Sertés Szalámi `sertes_szalami` — kg, szeletelhető
- Ugyanolyan opciók mint a növendék szalámi (vastagság)

### 32. Székely Kolbász `szekely_kolbasz` — kg
- **Variáció: NINCS** („szárán szokták szárítani")

### 33. Téli Szalámi `teli_szalami` — kg, szeletelhető
- **Vastagság** opció (single_select): vékony / közepes / vastag

---

## 🍖 Felvágott & Egyéb

### 34. Abált Szalonna `abalt_szalonna` — kg
- **Szeletelhető**: igen
- Felhasználás: kell egy receptcikk ami magyarázza a használatát

### 35. Disznó Fősajt `diszno_fosajt` — egyben (db)
- **Variáció: NINCS** („nem szokták szeletelve kérni")

### 36. Göngyölt Hús `gongyolt_hus` — kg
- **Szeletelés: NEM** („az őrült hús kipotyoghat a beléből")

### 37. Pástétom `pastetom` — darabra
- **Variáció: NINCS**

---

## 🆕 ÚJ TERMÉKEK (a pre-v1.0 archív JSON-ban NEM voltak — most jönnek!)

### Csirke szekció (új kategória? vagy `friss_serteshus`-ba?)
> **Kérdés Szabolcsnak:** új kategóriát kell `friss_csirkehus` néven, VAGY ezek a `friss_serteshus`-ba mennek?

| ID | Név | Ár | Megjegyzés |
|----|-----|-----|-----------|
| `csirke_egybe_comb` | Csirke Egybe Comb (alsó+felső) | 17 RON/kg | kg, weight |
| `csirke_mell_csont_borr_nelkul` | Csirke Mell csont és bőr nélkül | 34 RON/kg | kg, weight |
| `csirke_szarny` | Csirke Szárny | 16 RON/kg | kg, weight |
| `csirke_mellcsont` | Csirke Mellcsont | 26 RON/kg | kg, weight (a Speaker 2 mondta hogy „26", de nem 100%-os) |

### Sertés-szekció új termékek

| ID | Név | Ár | Megjegyzés |
|----|-----|-----|-----------|
| `sertes_lapocka` | Sertés Lapocka | 25 RON/kg | kg, weight. Pörköltnek/levesnek/töltelékesnek puhább mint a comb |
| `sajtos_cerna_kolbasz` | Sajtos Cérna Kolbász | 48 RON/kg | kg, weight. Főzni, sütni, grillezni |
| `tepertonek_valo_szalonna` | Tepertőnek való szalonna (régi „munkaszalonna") | 15 RON/kg | kg, weight, **NYÁRI termék** |
| `koppados_virsli` | Koppadós Virsli | 48 RON/kg | kg, weight. Disznócombból + szalonna, juhbélbe töltve, „ehető bél" |

### Bontandó termék (volt egynek, most több)
- `sertes_hasresz` (régi 24.5 RON) → bontandó:
 - `sertes_hasresz_csontos_borr` (csontos+bőrös) — 24,50 RON/kg
 - `sertes_hasresz_csont_nelkul` (bőrös, csontnélküli) — 26 RON/kg, szeletelhető+pácolható
 - `sertes_oldalas` (csontos, bőr nélkül) — 26 RON/kg, szeletelhető+pácolható

---

## 🎯 Cross-cutting business döntések

### Foto stratégia
- Minden variációhoz külön fotó (sima/dupla, pácolt/nem pácolt)
- **Háttér konzisztens** (azonos)
- **Zöld + piros zöldség** (paradicsom, saláta) hozzáadva — különben „hátborzongató" csak nyers hús
- **3 szelet** elrendezés látszódjon (jó pózú referencia)
- Avi (a fotós) intézi

### Marketing megjegyzések
- **„Bükkfa fűrészporral füstölt"** — minden füstölt termékhez (vs. „füstlével leöntött")
- **„Fával füstölt"** — még pontosabb fogalmazás
- **Receptcikkek** kell minden termékhez (gasztronómia stílusban)
- **YouTube videó linkelés** termékekhez
- **Adagok** számítása (4/6/8 személyre) — későbbi feature, zöldségekkel együtt
- **Belső Facebook csoport** terve

### Termékkód rendszer
- A termékeknek belső kódja van (pl. nyakaskaraj = `014`)
- Megjegyzés Szabolcs: „kódban tudjunk beszélni"
- TODO: kódokat be kell vinni a termék MD-kbe (`internal_code` mező?)

### Eladók képzése
- Anna Mari (Petriben) példa — türelmesen magyarázott
- Szöveges segítség minden termék mellett
- A vásárlóknak **NORMÁL gomb** kell (különben a két extrémum elveszti őket)

### Termék leírás stratégia
- Rövid táblázat-szöveg + hosszabb „segítség" / receptötlet
- Felvágott szöveg + felhasználás külön-külön

---

## ⚠️ Open questions / TODO

1. **Csirke termékek kategóriája?** — új `friss_csirkehus`, vagy `friss_serteshus`?
2. **Csirke mellcsont ára** — Speaker 2 mondta „26", de nem 100%-os
3. **Hasrész 3-4 termékre bontás** — pontosan hány sub-termékre? (3: csontos+bőrös / csontnélkül+bőrös / csontos-bőr nélkül)
4. **Internal code (014, stb.)** — bekerüljön a JSON-ba? Új schema mező?
5. **Szezonális termékek megjelenítése** — az app már támogat szezonális be-/kikapcsolást
6. **Növendék szalámi bőr eltávolítás** — termelő képzése (UX kérdés, nem schema)
7. **Receptcikk feature** — most még nincs, de a tartalmat gyűjteni érdemes
8. **„Normál" érték a darált hús zsírosság opcióhoz** — kötelező legyen-e default?
9. **Marketing szöveg** („bükkfa füst") — ez egy közös meta-mező, vagy terméknént tartjuk?

---

## 🚦 Ajánlott következő lépések (Szabolcsnak)

**Most:**
1. Olvasd át ezt a doksit, **flag-eld az open questions-eket**
2. Eldönteni az új csirke kategória + hasrész bontás kérdéseit
3. Ha rendben → indulhat a batch migráció

**Migráció sorrend** (én javaslom):
- **Phase 1** — meglévő 37 termék MD-be migrálása (a meeting-info bedolgozásával)
- **Phase 2** — új termékek (8 db) hozzáadása: csirke szekció + lapocka + sajtos cérna + tepertő szalonna + koppadós virsli
- **Phase 3** — termékkód mező eldöntése + bevezetése
- **Phase 4** — recept/marketing szöveg külön struktúra (talán külön schema bump v1.1?)

Minden Phase = külön build + deploy.

---

**Készítette:** Cowork session (Szabolccsal együttműködésben)
**Dátum:** 2026-05-07
**Forrás:** transcript-full SRT, sorvázolt analízissel
