# F4 — Kommunikáció + feldolgozás (multi-persona)
**Időkeret:** 30-35 perc
**Fázis a workshopban:** 4/6

## Narratív összefoglaló
**F1 = rend a fájlok között. F2 = rend a TODO-k között. F3 = rend a döntésben. F4 = rend a kommunikációban.**

Az F3 végén megvan a Data Completion Board: tudjuk mit kell beszerezni, kitől, mikorra. De most jön a neheze: ténylegesen el kell küldeni az emaileket, feldolgozni a válaszokat, ellenőrizni a dokumentumokat, és összefoglalni az egészet a főnöknek. Egy ember, három különböző célközönség, három különböző stílus.

Ez az F4 lényege: az AI mint **multi-persona kommunikátor és operátor**.

## A 3 sub-flow (LIVE)

| # | Sub-flow | Célközönség | Plugin | Idő |
|---|----------|-------------|--------|-----|
| 4.1 | Bérleti szerződés deep-check | Béla bácsi (tulajdonos) | Legal plugin | ~12 perc |
| 4.2 | Pénzügyi adatok beszerzése | Mihaela (külsős könyvelő) | Excel feldolgozás | ~10-12 perc |
| 4.3 | CEO update prezentáció | Márton (ügyvezető) | PPTX generálás | ~8-10 perc |

## Bónusz feladatok (OTTHON)

| # | Feladat | Idő |
|---|---------|-----|
| 4.4 | (Bónusz) Saját szerződés deep-check | ~20 perc |
| 4.5 | (Bónusz) Ugyanaz az email, 3 hangnemben | ~10 perc |
| 4.6 | (Bónusz) Excelből vezetői dashboard | ~15 perc |
| 4.7 | (Bónusz) Ugyanaz a prezentáció, 3 célközönségnek | ~20 perc |

## Kulcs üzenet

Az AI nemcsak elemez — **dolgozik**:
- Emailt ír románul a könyvelőnek
- Kockázatot fedez fel a bérleti szerződésben (cross-document)
- Prezentációt generál a CEO-nak

Ugyanaz az adat → három célközönségnek három formátum. Az ember dönt, az AI végrehajtja.

## Asset-ek (már léteznek)
- `TransOffice/szerzodes_chirie_TransOffice_2018.docx` — bérleti szerződés
- `TransOffice/email_exportok/raspuns_bela_iosif_2025-02-26.txt` — Béla úr válasza
- `TransOffice/meetings/meeting_transcript_20250224.md` — a "Béla bácsi" mondat benne van

## Delivery design

| Fázis | Ki | Mit |
|-------|----|-----|
| **F4.1 WOW** | Te (demo) | Bérleti szerződés deep-check → cross-doc riasztás ("Béla bácsi") |
| **F4.1 MICRO** | Ők | Béla bácsi válaszának feldolgozása, DCB frissítés |
| **F4.2 WOW** | Te (demo) | Könyvelő email generálás románul |
| **F4.2 MICRO** | Ők | Határidő módosítás vagy plusz kérés hozzáadása |
| **F4.3 WOW** | Te (demo) | 5 slide CEO prezentáció az eddigi munkából |
| **F4.3 MICRO** | Ők | +1 slide: "Mi ha NEM pályázunk?" |

## Átmenet F5-be
"Márton látta a prezentációt, rábólintott: pályázunk. Most össze kell rakni az egész csomagot és be kell adni. Az F5 az, ahol minden összeáll."
