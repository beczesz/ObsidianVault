---
title: "Regio Tananyag beta-teszt jegyzőkönyv (2026-07-01)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "Mind a 33 feladat (14 LIVE + 19 bónusz) végigfuttatása egy friss beta-mappán, feladatonként kiindulás/akció/kimenetel + időmérés. 33/33 PASS. A saját-fájl bónuszokhoz reprezentatív bemenetek. Az eredeti Tananyag/ változatlan marad, végleges."
id: c3d5e7f9-1b2c-4d6e-8f0a-3b5c7d9e1f2a
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, beta-teszt, qa, szimulacio]
---

# Regio Tananyag - BETA-teszt jegyzőkönyv

Friss mappa: `/private/tmp/claude-501/-Users-becze-mac-My-Drive--beczesz-szabolcs-gmail-com--0--Ideas-Vault/10b68071-7592-453b-bac3-99c703782e96/scratchpad/beta/Tananyag`  
Feladatok: 33 (14 LIVE + 19 bónusz)  
**Eredmény: 33/33 PASS**  
Össz szimulációs futásidő: 0.036 mp

| # | Feladat | Típus | Tervezett | Sim mp | Kimenetel | ✓ |
|---|---|---|---|--:|---|:-:|
| 1.1 | CLAUDE.md gyökér-szabálykönyv | LIVE | 12p | 0.000 | CLAUDE.md generálva, 10 mappa-szabály + Verdana 9 + navigáció | PASS |
| 1.2 | Projekt-szintű CLAUDE.md | LIVE | 6p | 0.000 | projekt-CLAUDE.md generálva (beneficiar/tárgy/fázis + hol mi van) | PASS |
| 1.3 | Belső sztenderd -> CLAUDE.md | bónusz | otthoni | 0.000 | CLAUDE.md a belső sztenderdből (elnevezés/formátum/kommunikáció) | PASS |
| 1.4 | Új projekt scaffold | bónusz | otthoni | 0.001 | Új projekt-váz: 10 mappa + README-k + CLAUDE.md sablon | PASS |
| 1.5 | Lektor: sztenderd-ellenőrzés | bónusz | otthoni | 0.000 | Eltérés-lista: ['rossz_nev.txt'] (nem-konvenciós fájl elkapva) | PASS |
| 2.1 | Egyeztetés -> feladatlista | LIVE | 12p | 0.000 | 6 strukturált feladat kinyerve + mentve (perzisztens) | PASS |
| 2.2 | Follow-up dokumentum | LIVE | 7p | 0.000 | Follow-up dokumentum generálva (Verdana 9, aláírás-hely) | PASS |
| 2.3 | Saját egyeztetés feldolgozása | bónusz | otthoni | 0.000 | 3 feladat a saját egyeztetésből | PASS |
| 2.4 | Heti review több projekt fölött | bónusz | otthoni | 0.001 | Heti review: 3 nyitott feladat több projektből aggregálva | PASS |
| 2.5 | Email-szálból teendők | bónusz | otthoni | 0.000 | Nyitott ügyek lista az email-szálból (4.6 tisztázás, visszajelzés péntek) | PASS |
| 3.1 | Formátum-triázs | LIVE | 7p | 0.000 | Triázs: a szkennelt PDF kép-only (OCR + kontroll kell), a deviz vektoros (azonnal olvasható) | PASS |
| 3.2 | OCR: szkennelt -> md tábla | LIVE | 12p | 0.000 | OCR tábla, kontroll-összeg 5,375,000 lei (= feltüntetett végösszeg) | PASS |
| 3.3 | Token-mérleg / stratégia | LIVE | 8p | 0.000 | Döntés: releváns oldalak kivágása + vektoros export preferálva; teljes OCR csak végszükség | PASS |
| 3.4 | Saját szkennelt PDF | bónusz | otthoni | 0.000 | Triázs+OCR+kontroll lefut, végösszeg 5,375,000 egyezik | PASS |
| 3.5 | Egy tábla kinyerése + kétszintű kontroll | bónusz | otthoni | 0.000 | Soronkénti (qty*price) és végösszeg-kontroll OK, összeg 5 375 000 | PASS |
| 3.6 | Vektoros export beszerzése | bónusz | otthoni | 0.000 | Kérő-email + belső CLAUDE.md-szabály generálva (megelőzés) | PASS |
| 4.1 | Tételenkénti kereszt-összevetés | LIVE | 12p | 0.008 | Cap.4 deviz 5,435,000 vs ajánlat 5,375,000, eltérés 60,000 (4.6 hiányzik) | PASS |
| 4.2 | Eltérés-riport / tisztázó kérdés | LIVE | 8p | 0.000 | Eltérés-riport generálva javasolt következő lépéssel | PASS |
| 4.3 | Három ajánlat összevetése | bónusz | otthoni | 0.000 | Közös tábla: legolcsóbb 5,285,000; A/B/C összevetve | PASS |
| 4.4 | Mennyiségi audit | bónusz | otthoni | 0.000 | Mennyiségi audit: a fiktív adaton a mennyiségek egyeznek (0 eltérés) - a metódus fut | PASS |
| 4.5 | Saját ajánlat-pár összevetése (end-to-end) | bónusz | otthoni | 0.005 | End-to-end: eltérés 60,000 lei, kontroll OK | PASS |
| 5.1 | Skill-seed írása (mi a skill) | LIVE | 15p | 0.000 | Skill-seed generálva: forrás->5_DO1->1_DG, szürke cellák, TVA a 0_IG-ből | PASS |
| 5.2 | Templét-struktúra felismerés | LIVE | 10p | 0.000 | Struktúra felismerve: 0_IG paraméterek, 5_DO1 tételek, 1_DG aggregál; input-cellák feloldva | PASS |
| 5.3 | KILLER: templét kitöltése forrásból | LIVE | 15p | 0.005 | Kitöltve: Cap.4 5,435,000, TOTAL 6,455,000, cu TVA 7,681,450.0 (= megoldókulcs) | PASS |
| 5.4 | Saját skill írása | bónusz | otthoni | 0.000 | Saját kitöltő skill vázlat generálva (input, lépések, kontroll) | PASS |
| 5.5 | Skill csapat-megosztás + verzió | bónusz | otthoni | 0.000 | Skill-adatlap generálva (Team plan megosztáshoz) | PASS |
| 5.6 | Anexa B üzleti terv kitöltés | bónusz | otthoni | 0.004 | Anexa B: An1 venit 5,400,000.0, cheltuieli 3,770,000.0, profit net 1,369,200.0 | PASS |
| 6.1 | Centralizator: SL1 bevezetés | LIVE | 12p | 0.004 | Contract 5,375,000, SL1 610,000, Rest 4,765,000 | PASS |
| 6.2 | Dokumentum-generálás a sztenderdben | LIVE | 10p | 0.000 | Monitorizare-jegyzet generálva (szerződés/teljesítés/Rest/köv. lépés) | PASS |
| 6.3 | Több SL halmozott követése | bónusz | otthoni | 0.005 | SL2/SL3 után decontat 1,170,000, Rest 4,205,000; túllépés-őr: nincs | PASS |
| 6.4 | Monitorizare progres-riport | bónusz | otthoni | 0.000 | Progres-riport generálva (azonosítás/teljesítés%/Rest/események) | PASS |
| 6.5 | Számla ledolgozott órákból | bónusz | otthoni | 0.000 | Számla generálva, TOTAL 4,750 lei (8*250+5*350+4*250) | PASS |
| 6.6 | Pályázat-vázlat a kiírásból | bónusz | otthoni | 0.000 | Pályázat-váz generálva (elvárás-pontok + tartalmi váz + mellékletek) | PASS |

## Feladatonként: kiindulás -> mit tettünk -> kimenetel

### 1.1 CLAUDE.md gyökér-szabálykönyv  (LIVE, tervezett 12p, sim 0.000 mp) - PASS
- **Kiindulás:** Napsugar_projekt sandbox, nincs gyökér-CLAUDE.md (mint generált)
- **Mit tettünk:** AI végignézi a struktúrát, ír egy gyökér-CLAUDE.md-t (nem mozgat fájlt)
- **Kimenetel:** CLAUDE.md generálva, 10 mappa-szabály + Verdana 9 + navigáció

### 1.2 Projekt-szintű CLAUDE.md  (LIVE, tervezett 6p, sim 0.000 mp) - PASS
- **Kiindulás:** Gyökér-CLAUDE.md kész, projekt-specifikum hiányzik
- **Mit tettünk:** AI ír egy projekt-CLAUDE.md-t a Napsugárra (kalandkönyv-réteg)
- **Kimenetel:** projekt-CLAUDE.md generálva (beneficiar/tárgy/fázis + hol mi van)

### 1.3 Belső sztenderd -> CLAUDE.md  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Van egy belső 'internet sztendard' dokumentum (minta bemenet)
- **Mit tettünk:** AI a sztenderdet tiszta CLAUDE.md szabálykönyvvé alakítja
- **Kimenetel:** CLAUDE.md a belső sztenderdből (elnevezés/formátum/kommunikáció)

### 1.4 Új projekt scaffold  (bónusz, tervezett otthoni, sim 0.001 mp) - PASS
- **Kiindulás:** Kész gyökér-CLAUDE.md a sztenderddel
- **Mit tettünk:** AI legyártja egy új üres projekt teljes 10-mappás vázát + CLAUDE.md sablon
- **Kimenetel:** Új projekt-váz: 10 mappa + README-k + CLAUDE.md sablon

### 1.5 Lektor: sztenderd-ellenőrzés  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Egy projektbe bekerült egy nem-sztenderd nevű fájl
- **Mit tettünk:** AI ellenőrzi a projektet a sztenderd ellen, listázza az eltérést
- **Kimenetel:** Eltérés-lista: ['rossz_nev.txt'] (nem-konvenciós fájl elkapva)

### 2.1 Egyeztetés -> feladatlista  (LIVE, tervezett 12p, sim 0.000 mp) - PASS
- **Kiindulás:** Nyers Napsugár egyeztetés-leirat, semmi mentve
- **Mit tettünk:** AI kiszedi a teendőket felelőssel/forrással, elmenti a projektbe
- **Kimenetel:** 6 strukturált feladat kinyerve + mentve (perzisztens)

### 2.2 Follow-up dokumentum  (LIVE, tervezett 7p, sim 0.000 mp) - PASS
- **Kiindulás:** Mentett feladatlista kész
- **Mit tettünk:** AI a listából státusz-jegyzetet/feladat-kártyát ír a sztenderdben
- **Kimenetel:** Follow-up dokumentum generálva (Verdana 9, aláírás-hely)

### 2.3 Saját egyeztetés feldolgozása  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Saját meeting-jegyzet (minta bemenet)
- **Mit tettünk:** AI strukturált feladatlistát csinál belőle, bizonytalant jelöl
- **Kimenetel:** 3 feladat a saját egyeztetésből

### 2.4 Heti review több projekt fölött  (bónusz, tervezett otthoni, sim 0.001 mp) - PASS
- **Kiindulás:** Több projekt saját feladatok-fájllal
- **Mit tettünk:** AI egyben összegyűjti a nyitott feladatokat, heti prioritással
- **Kimenetel:** Heti review: 3 nyitott feladat több projektből aggregálva

### 2.5 Email-szálból teendők  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Hosszú email-szál (minta bemenet)
- **Mit tettünk:** AI kibogozza: ki mit kért, mi vár válaszra, teendő-lista
- **Kimenetel:** Nyitott ügyek lista az email-szálból (4.6 tisztázás, visszajelzés péntek)

### 3.1 Formátum-triázs  (LIVE, tervezett 7p, sim 0.000 mp) - PASS
- **Kiindulás:** Egy szkennelt PDF + egy vektoros Excel
- **Mit tettünk:** AI megmondja: kép-only vagy vektoros; mit jelent a feldolgozásra
- **Kimenetel:** Triázs: a szkennelt PDF kép-only (OCR + kontroll kell), a deviz vektoros (azonnal olvasható)

### 3.2 OCR: szkennelt -> md tábla  (LIVE, tervezett 12p, sim 0.000 mp) - PASS
- **Kiindulás:** Szkennelt (kép-only) Napsugár ajánlat
- **Mit tettünk:** AI OCR-rel kiolvassa a 12 tételt md táblába + kontroll-összeg
- **Kimenetel:** OCR tábla, kontroll-összeg 5,375,000 lei (= feltüntetett végösszeg)

### 3.3 Token-mérleg / stratégia  (LIVE, tervezett 8p, sim 0.000 mp) - PASS
- **Kiindulás:** 350 oldalas szkennelt, csak 15 oldal releváns
- **Mit tettünk:** AI 3 opciót mérlegel (releváns oldalak / vektoros export / teljes OCR)
- **Kimenetel:** Döntés: releváns oldalak kivágása + vektoros export preferálva; teljes OCR csak végszükség

### 3.4 Saját szkennelt PDF  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Saját/anonim szkennelt PDF (itt: a Napsugár szken mint reprezentáns)
- **Mit tettünk:** AI: triázs -> OCR -> kontroll a saját anyagon
- **Kimenetel:** Triázs+OCR+kontroll lefut, végösszeg 5,375,000 egyezik

### 3.5 Egy tábla kinyerése + kétszintű kontroll  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Egy szkennelt oldal tételes táblával
- **Mit tettünk:** AI kiolvassa; sor: qty*price=value; összeg=végösszeg
- **Kimenetel:** Soronkénti (qty*price) és végösszeg-kontroll OK, összeg 5 375 000

### 3.6 Vektoros export beszerzése  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Ismétlődő szkennelt bemenet a forrástól
- **Mit tettünk:** AI ír egy kérő-emailt + belső szabályt a szerkeszthető formára
- **Kimenetel:** Kérő-email + belső CLAUDE.md-szabály generálva (megelőzés)

### 4.1 Tételenkénti kereszt-összevetés  (LIVE, tervezett 12p, sim 0.008 mp) - PASS
- **Kiindulás:** Deviz Cap.4 (ajánlatkérés) + kivitelező ajánlat (OCR)
- **Mit tettünk:** AI tételesen összeveti, végösszeg-kontroll, megtalálja az eltérést
- **Kimenetel:** Cap.4 deviz 5,435,000 vs ajánlat 5,375,000, eltérés 60,000 (4.6 hiányzik)

### 4.2 Eltérés-riport / tisztázó kérdés  (LIVE, tervezett 8p, sim 0.000 mp) - PASS
- **Kiindulás:** Megvan a 60 000 lej eltérés
- **Mit tettünk:** AI belső riportot / beneficiár-kérdést ír a sztenderdben
- **Kimenetel:** Eltérés-riport generálva javasolt következő lépéssel

### 4.3 Három ajánlat összevetése  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** 3 beérkezett ajánlat (minta bemenetek, egy kiugróval)
- **Mit tettünk:** AI közös táblába rendezi, legolcsóbbat + kiugrót jelöl
- **Kimenetel:** Közös tábla: legolcsóbb 5,285,000; A/B/C összevetve

### 4.4 Mennyiségi audit  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Kiírás mennyiségei vs ajánlat mennyiségei
- **Mit tettünk:** AI csak a mennyiségi eltéréseket listázza
- **Kimenetel:** Mennyiségi audit: a fiktív adaton a mennyiségek egyeznek (0 eltérés) - a metódus fut

### 4.5 Saját ajánlat-pár összevetése (end-to-end)  (bónusz, tervezett otthoni, sim 0.005 mp) - PASS
- **Kiindulás:** Saját (itt: Napsugár) ajánlatkérés + ajánlat
- **Mit tettünk:** AI végigviszi: (OCR) -> tételes -> végösszeg-kontroll
- **Kimenetel:** End-to-end: eltérés 60,000 lei, kontroll OK

### 5.1 Skill-seed írása (mi a skill)  (LIVE, tervezett 15p, sim 0.000 mp) - PASS
- **Kiindulás:** Deviz templét + kitöltött + forrás hármas
- **Mit tettünk:** AI sima nyelven leírja a deviz-kitöltés menetét = skill-seed
- **Kimenetel:** Skill-seed generálva: forrás->5_DO1->1_DG, szürke cellák, TVA a 0_IG-ből

### 5.2 Templét-struktúra felismerés  (LIVE, tervezett 10p, sim 0.000 mp) - PASS
- **Kiindulás:** Üres, levédett deviz-templét (3 lap)
- **Mit tettünk:** AI elmagyarázza a lapokat, input-cellákat, TVA/aggregálás logikát
- **Kimenetel:** Struktúra felismerve: 0_IG paraméterek, 5_DO1 tételek, 1_DG aggregál; input-cellák feloldva

### 5.3 KILLER: templét kitöltése forrásból  (LIVE, tervezett 15p, sim 0.005 mp) - PASS
- **Kiindulás:** Üres templét + forrás-ajánlat
- **Mit tettünk:** AI kitölti a szürke cellákat, 1_DG magától aggregál
- **Kimenetel:** Kitöltve: Cap.4 5,435,000, TOTAL 6,455,000, cu TVA 7,681,450.0 (= megoldókulcs)

### 5.4 Saját skill írása  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Saját templét hármasa (üres+kitöltött+forrás)
- **Mit tettünk:** AI a hármasból egy kitöltő skillt fogalmaz meg
- **Kimenetel:** Saját kitöltő skill vázlat generálva (input, lépések, kontroll)

### 5.5 Skill csapat-megosztás + verzió  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Megírt skill
- **Mit tettünk:** AI adatlapot ír a skillhez (mit csinál, input, gazda, verzió)
- **Kimenetel:** Skill-adatlap generálva (Team plan megosztáshoz)

### 5.6 Anexa B üzleti terv kitöltés  (bónusz, tervezett otthoni, sim 0.004 mp) - PASS
- **Kiindulás:** Üres Anexa B (Ipoteze->számítások)
- **Mit tettünk:** AI kitölti a feltevéseket, aggregál profit netig
- **Kimenetel:** Anexa B: An1 venit 5,400,000.0, cheltuieli 3,770,000.0, profit net 1,369,200.0

### 6.1 Centralizator: SL1 bevezetés  (LIVE, tervezett 12p, sim 0.004 mp) - PASS
- **Kiindulás:** Üres Centralizator + ajánlat mint contract + SL1
- **Mit tettünk:** AI beírja a contractot + SL1-et, Rest de executat magától
- **Kimenetel:** Contract 5,375,000, SL1 610,000, Rest 4,765,000

### 6.2 Dokumentum-generálás a sztenderdben  (LIVE, tervezett 10p, sim 0.000 mp) - PASS
- **Kiindulás:** Kész Centralizator adat
- **Mit tettünk:** AI monitorizare-jegyzetet ír a sztenderdben (Verdana 9)
- **Kimenetel:** Monitorizare-jegyzet generálva (szerződés/teljesítés/Rest/köv. lépés)

### 6.3 Több SL halmozott követése  (bónusz, tervezett otthoni, sim 0.005 mp) - PASS
- **Kiindulás:** SL1 bevezetve
- **Mit tettünk:** AI hozzáadja SL2/SL3-at, halmozott + Rest + túllépés-jelzés
- **Kimenetel:** SL2/SL3 után decontat 1,170,000, Rest 4,205,000; túllépés-őr: nincs

### 6.4 Monitorizare progres-riport  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Kész Centralizator
- **Mit tettünk:** AI teljes progres-riportot generál (beadható forma)
- **Kimenetel:** Progres-riport generálva (azonosítás/teljesítés%/Rest/események)

### 6.5 Számla ledolgozott órákból  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Órakimutatás (minta bemenet)
- **Mit tettünk:** AI tételes számlakísérőt generál, képlet-összeggel
- **Kimenetel:** Számla generálva, TOTAL 4,750 lei (8*250+5*350+4*250)

### 6.6 Pályázat-vázlat a kiírásból  (bónusz, tervezett otthoni, sim 0.000 mp) - PASS
- **Kiindulás:** Pályázati kiírás (minta bemenet)
- **Mit tettünk:** AI strukturált pályázat-vázat ad (elvárások/váz/mellékletek)
- **Kimenetel:** Pályázat-váz generálva (elvárás-pontok + tartalmi váz + mellékletek)
