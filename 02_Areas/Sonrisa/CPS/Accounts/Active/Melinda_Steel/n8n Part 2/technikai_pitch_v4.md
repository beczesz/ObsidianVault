---
title: "Technikai ajanlat -- AI-alapu WhatsApp ajanlatkero rendszer (Part 2)"
date: 2026-04-30
author: Becze Szabolcs
status: active
description: "AI-alapú WhatsApp-rendszer technikai ajánlata a Melinda Steel számára, amely természetes nyelvű termékkéréseket dolgoz fel, azonosít és automatikusan ároffertákat küld PDF-ben. A Part 2 a Part 1 meglévő WhatsApp, AI és matching komponenseire építve integrálja a Priority ERP-t és PDF-generálást."
description_source: auto
description_hash: 163cdd5e705f296b
id: 768a7573-997c-478b-beb2-bbe6a609a16a
index_schema_version: 1
bdos_index: true
---
# Technikai ajanlat -- AI-alapu WhatsApp ajanlatkero rendszer (Part 2)

**Projekt:** MELS-SON-M2025-02
**Kapcsolodo projekt:** MELS-SON-M2025-01 (n8n Part 1 -- versenytars-arajelzes automatizalas)
**Datum:** 2026-04-30
**Statusz:** AJANLAT

---

## 1. Projekt cel

A rendszer celja, hogy a Melinda Steel ugyfelei WhatsApp-on, termeszetes nyelven kerhessenek arajanlat-ot acelipari termekekre (pl. "500m 50x30x2 zaart szelveny ara?"), es a rendszer automatikusan feldolgozza a kerest, azonositsa a termeket a Melinda katalogusban, lekerdezze az aktualis arat a Priority ERP rendszerbol, majd PDF ajanlatot kuldjjon vissza WhatsApp-on.

## 2. Elozmenyek -- Part 1 eredmenyei

A MELS-SON-M2025-01 projekt (n8n Part 1) soran a kovetkezo komponensek keszultek el:

| Komponens | Leiras | Statusz |
|-----------|--------|---------|
| WhatsApp Cloud API integracio | Trigger, media download, valasz kuldes, interaktiv formok | KESZ, ujrahasznalhato |
| Google Gemini AI integracio | Dokumentum ertelmezese, strukturalt JSON kimenet | KESZ, prompt ujratervezes szukseges |
| Fuzzy matching API | Python szolgaltatas (Render), termekazonositas | KESZ, ujrahasznalhato |
| LLM matching fallback | Gemini-alapu masodik szintu egyeztetes, ha a fuzzy score < 60 | KESZ, ujrahasznalhato |
| Termekkatalogus | n8n data table, teljes Melinda termekpaletta | KESZ, ujrahasznalhato |
| SharePoint integracio | Adattarolas, archivalas | KESZ, ujrahasznalhato |
| Denumire_enriched szabalyok | Termeknev normalizalas (meret-sorrend, anyagminoseg, szabvany) | KESZ, ujrahasznalhato |

**A Part 1 elony:** A fejlesztes jelentos resze -- WhatsApp, AI, matching -- mar mukodik es tesztelt. A Part 2 ezekre epit, nem nullarol indul.

## 3. Megkozelites -- AI + kontrollalt validacio

A rendszer a meglevo Google Gemini multimodalis modellre epit, amely szoveget es kepet is ertelmezel. A Part 1 promtjainak ujratervezesevel a rendszer termeszetes nyelvu ugyfel-uzeneteket is kepes feldolgozni (a Part 1-ben strukturalt PDF/kep inputot kezelt).

A folyamat human-in-the-loop validacioval egeszul ki: az ertekesito latja a rendszer altal felismert termekeket es arakat, mielott a PDF ajanlat kimegy az ugyffelnek.

## 4. Architektura

```
Ugyffel (WhatsApp)
  -> WhatsApp Cloud API (MEGLEVO Part 1-bol)
    -> n8n workflow (uj, de a meglevo infrastrukturaara epit)
      -> Gemini AI (termek ertelmezese -- MEGLEVO, prompt uj)
      -> Fuzzy Matching API (termekazonositas -- MEGLEVO)
      -> Priority ERP (OData REST API -- UJ)
        -> Arlekerdezes (PRICELIST/PARTPRICE)
        -> Ugyffeladat (CUSTOMERS)
      -> PDF generalas (UJ)
    -> Ertekesito megerosites (WhatsApp vagy Teams ertesites)
  -> PDF ajanlat visszakuldes WhatsApp-on
```

### Uj vs meglevo elemek

| Elem | Statusz | Munkaigeny |
|------|---------|------------|
| WhatsApp Cloud API | MEGLEVO | 0 ora (kesz) |
| n8n alapinfrastruktura | MEGLEVO | 0 ora (kesz) |
| Fuzzy matching API | MEGLEVO | 0 ora (kesz) |
| Gemini prompt atiras (szabad szoveg input) | MODOSITAS | ~8 ora |
| Conversational flow (n8n) | UJ | ~20 ora |
| Priority ERP OData integracio | UJ | ~32 ora |
| PDF ajanlat generalas + sablon | UJ | ~16 ora |
| Ugyffel-azonositas (telefon -> CUI) | UJ | ~8 ora |
| Nyelvi detektalas (roman/magyar) | UJ | ~8 ora |
| Teszteles + edge case-ek | UJ | ~16 ora |
| Pilot tamogatas + finomhangolas | UJ | ~12 ora |

## 5. Reszletes fazisok

### Phase 0: Discovery es elokeszites (1 het, ~16 ora)

**Cel:** A Priority ERP hozzaferes validalasa es az API endpoint-ok felterkepezese.

**Feladatok:**
1. Priority ERP API hozzaferes tesztelese (OData endpoint, authentikacio)
2. Arlistahoz tartozo entitasok azonositasa (PRICELIST, PARTPRICE, LOGPART)
3. Ugyffel-entitasok azonositasa (CUSTOMERS, CUI mapping)
4. API rate limit validalasa (max 100 hivas/perc/user -- elegseges-e?)
5. Meglevo fuzzy matching API allapot ellenorzese
6. Test kornyezet felepitese

**Sikerkriterium:** Priority API-bol sikeresen lekerdezzuk 3 termek arat es 1 ugyffel adatat.

### Phase 1: Conversational flow + Gemini prompt (2 het, ~28 ora)

**Cel:** Az ugyffel WhatsApp-on irt kerest a rendszer ertelmezi es strukturalt adatta alakitja.

**Feladatok:**
1. Gemini prompt ujratervezese: szabad szovegu ugyfel-uzenetekre (nem PDF-re)
   - Input: "500m 50x30x2 zaart szelveny ara?"
   - Output: JSON {termek: "zaart szelveny", meret: "50x30x2", mennyiseg: 500, UM: "M"}
2. n8n workflow: ugyffel-uzenet fogadasa -> Gemini -> fuzzy matching
3. Ha a match confidence < 60: visszakerdezes az ugyfeltol ("Erre a termekre gondolt: [opcio1] vagy [opcio2]?")
4. Ha a Gemini nem tud ertelmezni: udvarias uzenet + ertekesitohoz iranytias
5. Nyelvi detektalas: roman es magyar uzenetek kezelese

**Sikerkriterium:** 10 kulonbozo tipusu ugyfel-uzenetre helyes termek-azonositas mindket nyelven.

### Phase 2: Priority ERP integracio (2 het, ~32 ora)

**Cel:** A rendszer valoidoben lekerdezi a termek arat a Priority ERP-bol.

**Feladatok:**
1. Priority OData API connector az n8n-ben (authentikacio, HTTPS)
2. Termek arlekerdezes: ITEMKEY -> aktualis ar, valuta, keszlet
3. Ugyffel-azonositas: telefon szam -> Priority CUI/CUSTNAME mapping
   - Ha uj ugyffel: listaar alkalmazasa
   - Ha meglevo ugyffel: ugyffel-specifikus ar (ha van)
4. AFA szamitas: belfoldi (19% TVA) vs EU (fordtiott ado)
5. Hibakezelese: timeout, nem talalt termek, nem arazhaato SKU
6. Valuta kezeles: RON es/vagy EUR (a Priority-ban rogzitett valuta szerint)

**Sikerkriterium:** 5 kulonbozo termek arat sikeresen lekerdezzuk a Priority-bol n8n-en keresztul.

### Phase 3: PDF ajanlat generalas (1 het, ~16 ora)

**Cel:** A rendszer formatalt PDF ajanlatot general es kuld vissza WhatsApp-on.

**Feladatok:**
1. PDF sablon tervezese (Melinda logo, cegnev, cim, kapcsolat)
2. Ajanlat tartalom: termek, mennyiseg, egysegar, osszar, AFA, vegosszeg
3. Ajanlat szamozas (egyeztetes a meglevo rendszerrel, ha van)
4. Ervenyessegi ido feltuntetese (pl. 72 ora)
5. PDF generalas n8n-ben (HTML -> PDF konverzio vagy dedikalt library)
6. PDF visszakuldes WhatsApp-on (WhatsApp Cloud API document melleklet)

**Sikerkriterium:** Teljes, formatalt PDF ajanlat eloallitasa es sikeres kuldese WhatsApp-on.

### Phase 4: Megerosites + teszteles (1-2 het, ~16 ora)

**Cel:** Az ertekesito latja es jovahagyja az ajanlatot mielott kimegy.

**Feladatok:**
1. Ertekesitoi ertesites: a rendszer WhatsApp/Teams uzenetet kuld az ertekesitonek a keszulo ajanlatrol
2. Jovahagyas flow: ertekesito "OK" -> PDF kimegy; "Modositas" -> ertekesito kezzel araz
3. Edge case-ek kezelese:
   - Ismeretlen termek (nincs match)
   - Priority-ban nincs ar (termek letezik, de nincs aktualis arszint)
   - Ugyffel felbesakitja a beszelgetest
4. Belso teszteles: Sonrisa + Melinda ertekesitok 20+ teszt beszelgetest futtatnak
5. Valaszido optimalizalas: fuzzy match + ERP lekerdezes < 10 masodperc

**Sikerkriterium:** 20+ belso teszt beszelgetes sikeres mindket nyelven. Ertekesitoi jovahagyas flow mukodik.

### Phase 5: Pilot + eles inditas (1-2 het, ~12 ora)

**Cel:** Valos ugyfelekkel tesztelni es stabilizalni.

**Feladatok:**
1. 5-10 megbizhato ugyffel kivelasztasa pilot-ra
2. Pilot inditas: valos ugyfelek hasznaljak, ertekesitok monitorozzak
3. Finomhangolas a pilot tapasztalatok alapjan (heti iteracio)
4. Dokumentacio lezarasa es atadas

**Sikerkriterium:** 20+ valos ugyffel beszelgetes, 10+ sikeres PDF ajanlat, nincs kritikus hiba.

## 6. Idovonal

| Fazis | Idotartam | Kumulativ |
|-------|-----------|-----------|
| Phase 0: Discovery | 1 het | 1. het |
| Phase 1: Conversational flow + Gemini | 2 het | 3. het |
| Phase 2: Priority ERP integracio | 2 het | 5. het |
| Phase 3: PDF generalas | 1 het | 6. het |
| Phase 4: Megerosites + teszteles | 1-2 het | 7-8. het |
| Phase 5: Pilot + eles | 1-2 het | 8-10. het |

**Osszesen: 8-10 het**

## 7. Orabecsles es koltseg

| Tetel | Ora | EUR (39 EUR/ora) |
|-------|-----|------------------|
| Phase 0: Discovery | 16 | 624 |
| Phase 1: Conversational flow | 28 | 1 092 |
| Phase 2: Priority ERP | 32 | 1 248 |
| Phase 3: PDF generalas | 16 | 624 |
| Phase 4: Teszteles | 16 | 624 |
| Phase 5: Pilot | 12 | 468 |
| **Osszesen** | **120** | **4 680** |

**Elszamolas:** Time & Material (T&M), a tenyleges raforditas alapjan, havi reszszamlazassal.
**A Part 1-hez kepest 21%-kal kevesebb ora**, a meglevo komponensek ujrafelhasznalasanak koszonhetoen.

## 8. Uzemeltetesi koltseg (havi, a Megrendelot terheli)

| Tetel | Becsult havi koltseg |
|-------|---------------------|
| Google Gemini API | ~$10-30 (fugg a beszelgetesek szamatol) |
| Fuzzy Matching API (Render) | Mar meglevo, nincs plusz koltseg |
| Priority ERP API licensz | A Megrendelo meglevo licence altal fedezve |
| n8n hosting | Mar meglevo Part 1 infrastruktura |
| **Osszesen** | **~$10-30/ho** |

## 9. Kockazatok

| Kockazat | Valoszinuseg | Hatas | Kezelese |
|----------|-------------|-------|---------|
| Priority ERP API valaszido lassusag | Kozepes | Lassu ajanlat-generalas | Phase 0-ban teszteles, cache ha szukseges |
| Szabad szovegu inputok ertelmezesi hibak | Kozepes | Rossz termekazonositas | Ertekesitoi megerosites + visszakerdezes |
| Gemini rate limit (magas volumen eseten) | Alacsony | Varakozas, lassu valasz | Cache, batch optimalizalas |
| PDF sablon egyeztetes | Alacsony | Kesleletes | Phase 3 elejen egyeztetes |
| Tobbnyelvuseg (roman/magyar kevert uzenetek) | Kozepes | Felreertelmezett keres | Nyelvi detektalas + visszakerdezes |

## 10. Nyitott kerdesek

### Phase 0-ban megvalaszolandao (blokkolo)
1. A Priority ERP-ben melyik entitas tartalmazza az arlistat? (PRICELIST / PARTPRICE / egyedi?)
2. Van-e ugyffel-specifikus arkezeles a Priority-ban? (Vagy mindenki listaarat kap?)
3. Ki a projekt kontakt a Melinda Steel oldalron, aki a Priority rendszert ismeri?

### Phase 1-3-ban megvalaszolandao (fontos)
4. A PDF ajanlat milyen sablont kovet? (Van-e meglevo Melinda ajanlat-minta?)
5. Ajanlat ervenyessegi ido: 24 ora, 72 ora, vagy egyedi?
6. Egy beszelgetesben hany termekre kerhet ajanlatot az ugyffel? (MVP: 1-3 termek)
7. A chatbot melyik WhatsApp szamra epul? (A meglevo Part 1 szam, vagy uj?)

### Strategiai
8. Mennyi a vart napi beszelgetes szam? (koltseg- es kapacitastervezeshez)
9. Az eles rendszernek 24/7 kell-e mukodnie, vagy csak munkaido alatt?
10. AFA: belfoldi (19%) es/vagy EU ertekesites?
11. Valuta: RON, EUR, vagy mindketto?

## 11. Forrasok

- [Priority ERP REST API dokumentacio](https://prioritysoftware.github.io/restapi/)
- [Priority Developer Portal](https://prioritysoftware.github.io/)
- [Part 1 projekt dokumentacio](../Melinda%20steel%20n8n%20project%20documentaion.md)
- [Copilot Studio vs n8n kutatas](./brainstorm/brainstorm_copilot-studio-vs-n8n.md)
- [Copilot Studio akcioterv (referenciaul)](./action_plan_client_quoting.md)
