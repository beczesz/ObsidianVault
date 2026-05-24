---
title: Technikai Árajánlat -- AI-alapú WhatsApp Árajánlatkérő Rendszer
project: MELS-SON-M2025-02
version: 1.0
date: 2026-04-30
status: DRAFT
author: Sonrisa Informatikai Kft.
related: MELS-SON-M2025-01 (n8n Part 1)
id: 29aeabf4-3f78-43b7-b67d-b3bb5da2575e
index_schema_version: 1
---

# Technikai Árajánlat -- AI-alapú WhatsApp Árajánlatkérő Rendszer

## 1. Összefoglaló

A Melinda Steel ügyfelei jelenleg telefonon vagy emailben kérnek árajánlatot acélipari termékekre. Ez az értékesítők idejének jelentős részét köti le, és a válaszidő óráktól napokig terjedhet.

A javasolt rendszer ezt a folyamatot automatizálja: az ügyfél WhatsApp-on, természetes nyelven ír (pl. "500m 50x30x2 zárt szelvény ára?"), a rendszer azonosítja a terméket, lekérdezi az aktuális árat a Priority ERP-ből, majd PDF árajánlatot küld vissza -- mindezt perceken belül.

A fejlesztés a MELS-SON-M2025-01 (n8n Part 1) projekt eredményeire épít, ahol a WhatsApp integráció, a Gemini AI motor, és a termékazonosító rendszer már elkészült és működik. Ez jelentősen csökkenti a fejlesztési időt és kockázatot.

## 2. Mi épül az előző projektre?

Az n8n Part 1 során a következő komponensek készültek el, amelyeket a Part 2 közvetlenül újrahasznál:

| Kész komponens                        | Újrahasználás módja                                       |
| ------------------------------------- | --------------------------------------------------------- |
| WhatsApp Cloud API integráció         | Ugyanaz a csatorna, trigger, üzenetküldés -- hangolás szükséges az ügyfél-oldali flow-hoz |
| Google Gemini AI bekötés              | Prompt átírás szükséges (PDF helyett szabad szöveg input) |
| Fuzzy matching API (termékazonosítás) | Új endpoint szükséges -- a jelenlegi az első projektre specifikus adatokat ad vissza |
| LLM matching fallback (Gemini)        | Hangolás szükséges -- a prompt és az output struktúra adaptálása az ügyfél-oldali use case-re |
| Termékkatalógus (n8n adattábla)       | Szinkronizálás szükséges a Priority ERP-ben található adatokkal |
| Terméknév normalizálási szabályok     | Alapként használható, hangolás szükséges az ügyfél-oldali szóhasználathoz |

Az előző projekt komponensei képezik az alapot, de mindegyiknél számítani kell kisebb-nagyobb adaptációra az ügyfél-oldali use case sajátosságai miatt.

**Ami genuinely új:** Priority ERP árlekérdezés, PDF árajánlat generálás, ügyfél-azonosítás, conversational flow.

## 3. Hogyan működik?

```
Ügyfél WhatsApp üzenetet ír
  -> n8n workflow fogadja (meglévő WhatsApp integráció)
    -> Gemini AI értelmezi a kérést (termék, mennyiség, mérték)
    -> Fuzzy matching azonosítja a terméket a Melinda katalógusban
    -> Priority ERP OData API: aktuális ár lekérdezése
    -> PDF árajánlat generálás (Melinda sablonnal)
  -> Értékesítő jóváhagyja (WhatsApp/Teams értesítés)
  -> PDF árajánlat visszaküldése az ügyfélnek WhatsApp-on
```

**Megerősítési lépés:** A rendszer nem küld automatikusan árajánlatot. Az értékesítő kap egy értesítést a felismert termékkel és árral, és csak az ő jóváhagyása után megy ki a PDF az ügyfélnek. Ha a rendszer nem tud árazni (ismeretlen termék, hiányzó ár), az értékesítő kézzel áraz.

## 4. Fejlesztési fázisok

### Phase 0: Discovery és előkészítés (2-3 nap)

A fejlesztés előtt validáljuk, hogy a Priority ERP API hozzáférhető és a szükséges adatok lekérdezhetők.

- Priority ERP OData API endpoint-ok feltérképezése (árlista, ügyfél-entitások)
- API authentikáció tesztelése (Basic Auth / PAT)
- Teszt lekérdezések: 3 termék ára + 1 ügyfél adatai
- Meglévő fuzzy matching API állapot ellenőrzése
- Termékkatalógus (n8n adattábla) és Priority ERP termékadatok összehasonlítása
- Fejlesztési környezet felállítása

**Eredmény:** Validált API hozzáférés, azonosított endpoint-ok, teszt környezet kész.

### Phase 1: Fejlesztés (15-20 nap)

A teljes rendszer felépítése, a meglévő Part 1 komponensekre alapozva.

**Conversational flow + Gemini prompt (~5 nap)**
- Gemini prompt átírása szabad szövegű ügyfél-üzenetekre
- n8n beszélgetési logika: üzenet fogadás, értelmezés, visszakérdezés ha hiányos
- Nyelvi detektálás (román és magyar üzenetek kezelése)
- Ha a match confidence alacsony: visszakérdezés az ügyféltől
- Fuzzy matching API: új endpoint fejlesztése az ügyfél-oldali use case-re (a jelenlegi a Part 1-re specifikus)
- Termékkatalógus szinkronizálása a Priority ERP adataival

**Priority ERP integráció (~5-7 nap)**
- Priority OData REST API connector az n8n-ben
- Termék árlekérdezés: ITEMKEY alapján aktuális ár, valuta
- Ügyfél-azonosítás: telefonszám alapján Priority ügyfél lookup
- ÁFA számítás és valutakezelés (RON/EUR)
- Hibakezelés: timeout, nem található termék, nem árazható SKU

**PDF árajánlat generálás (~3-5 nap)**
- PDF sablon tervezése (Melinda arculat, cégnév, elérhetőség)
- Árajánlat tartalom: termék, mennyiség, egységár, összár, ÁFA, végösszeg
- Érvényességi idő feltüntetése
- PDF generálás és visszaküldés WhatsApp-on

**Értékesítői megerősítés (~2-3 nap)**
- Értékesítő értesítés a készülő árajánlatról
- Jóváhagyás flow: "OK" -> PDF kimegy, "Módosítás" -> kézi árazás
- Eszkaláció: ha a bot nem tud árazni, értékesítő kap értesítést

**Eredmény:** Működő rendszer, amely végigmegy a teljes flow-n: ügyfél kérés -> termékazonosítás -> ár -> PDF -> jóváhagyás -> küldés.

### Phase 2: Tesztelés, pilot és éles indítás (5-10 nap)

**Belső tesztelés (~3-5 nap)**
- Edge case-ek kezelése (ismeretlen termék, hiányzó ár, félbeszakított beszélgetés)
- 20+ belső teszt beszélgetés mindkét nyelven
- Válaszidő optimalizálás (a teljes feldolgozási idő az AI és ERP hívások miatt tipikusan 30-90 másodperc; a cél ennek minimalizálása)
- Nyelvi finomhangolás

**Pilot valós ügyfelekkel (~2-5 nap)**
- 5-10 megbízható ügyfél kiválasztása
- Valós körülmények között tesztelés
- Iteráció a tapasztalatok alapján
- Dokumentáció és átadás

**Eredmény:** Stabil, tesztelt rendszer, amely készen áll az éles használatra.

## 5. Időterv

| Fázis | Időtartam | Kumulatív |
|-------|-----------|-----------|
| Phase 0: Discovery | 2-3 nap | 1. hét |
| Phase 1: Fejlesztés | 15-20 nap | 2-5. hét |
| Phase 2: Teszt + pilot | 5-10 nap | 5-7. hét |
| **Összesen** | **20-30 munkanap** | **5-7 hét** |

**Fontos:** Az időterv munkanapokban értendő, nem naptári napokban. Az aláírástól számított tényleges átfutási idő a szabad napok, ünnepnapok és egyéb projektek ütemezése miatt 2-3 héttel meghaladhatja a fenti munkanap-becslést. A fejlesztés végének pontos dátuma nem naptári alapon kerül meghatározásra, hanem a ténylegesen ledolgozott munkanapok alapján.

## 6. Költségbecslés

### Fejlesztési költség

| | Minimum | Maximum |
|---|---------|---------|
| Munkanapok | 20 nap | 30 nap |
| Órák (napi 8 óra) | 160 óra | 240 óra |
| Óradíj | 39 EUR | 39 EUR |
| **Összesen** | **6 240 EUR** | **9 360 EUR** |

Elszámolás: Time & Material (T&M), a ténylegesen ráfordított órák alapján, havi részszámlázással. A fizetési határidő a számla kézhezvételétől számított 30 nap.

### Üzemeltetési költség (havi, a Megrendelőt terheli)

| Tétel | Becsült havi költség |
|-------|---------------------|
| Google Gemini API | ~$10-30 |
| Fuzzy Matching API (Render) | Meglévő, nincs plusz költség |
| Priority ERP API | Meglévő licenc által fedezve |
| n8n hosting | Meglévő Part 1 infrastruktúra |
| **Összesen** | **~$10-30/hó** |

## 7. Kockázatok

| Kockázat | Kezelése |
|----------|---------|
| Priority ERP API lassúsága | Phase 0-ban teszteljük; cache ha szükséges |
| Szabad szövegű inputok félreértelmezése | Értékesítői megerősítés + visszakérdezés az ügyféltől |
| PDF sablon egyeztetés húzódása | Phase 1 elején tisztázzuk a sablont |
| Többnyelvűség (román/magyar vegyes üzenetek) | Nyelvi detektálás + visszakérdezés |
| AI feldolgozási idő (LLM + fuzzy matching + ERP) | A teljes válasz 30-90 másodpercet vehet igénybe; az ügyfél várakoztatása "feldolgozás alatt" üzenettel |

## 8. Előfeltételek (a Megrendelő oldaláról)

1. Priority ERP API hozzáférés biztosítása (felhasználó + jogosultságok)
2. Döntés a PDF árajánlat sablonról (meglévő Melinda minta, ha van)
3. Kijelölt kapcsolattartó, aki a Priority rendszert ismeri (technikai kérdésekhez)
4. Döntés: melyik WhatsApp szám legyen a chatbot száma (meglévő vagy új)

## 9. Nyitott kérdések (Phase 0-ban tisztázandó)

1. Van-e ügyfél-specifikus árkezelés a Priority-ban, vagy mindenki listárat kap?
2. Egy beszélgetésben hány termékre kérhet árajánlatot az ügyfél?

### Már eldöntött kérdések

- **ÁFA:** Belföldi értékesítés, 19% TVA
- **Valuta:** RON (elsődleges), EUR (másodlagos)
- **Nyelvek:** Román és magyar
- **Rendelkezésre állás:** A bot automatikusan válaszol, értékesítői megerősítés munkaidőben

---

*Sonrisa Informatikai Kft.*
*Kapcsolat: Becze Szabolcs, Head of Cloud Platform Services*
*Dátum: 2026. április 30.*
