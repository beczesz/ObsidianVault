---
title: "Regio Consult + Napsugár Tejüzem: a workshop kontextusa"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "A Regio Consult haladó workshop teljes szimulációs kontextusa: a (fiktív, de a valós RC-t hűen tükröző) tanácsadó cég profilja, a strukturált projekt-felépítés logikája és indoka, valamint a végigfutó fiktív ügyfél-projekt (Napsugár Tejüzem tejfeldolgozó-beruházás) minden lényeges adata, szereplője és pénzügyi kontroll-száma. Oktatói referencia."
id: 8b1d3f27-6e40-4a95-9c2b-1e7f5a0c4d68
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, ceg-leiras, napsugar, kontextus]
---
# Regio Consult + Napsugár Tejüzem: a workshop kontextusa

> **Teljesen fiktív gyakorló-környezet.** A cég és a projekt kitalált, a számok kitaláltak. A **struktúra** a valós Regio Consult belső sztenderdjének logikáját követi, hogy a csapat a saját világában érezze magát. Sehol nincs valós ügyféladat.

---

## 1. rész: A cég: Regio Consult

### Alapadatok

| Adat | Érték |
|------|-------|
| **Profil** | EU / állami pályázati tanácsadó |
| **Irodák** | 3 (Székelyudvarhely, Kolozsvár, Szentegyháza) |
| **Csapat** | 21 fő, pályázati szakértők |
| **Régió** | Erdély |
| **Nyelv** | belső: magyar; dokumentumok: román (pályázati rendszer) |

### Mit csinál a Regio

A Regio az ügyfelei **teljes pályázati életciklusát** viszi:
`potential` (tárgyalás, adatgyűjtés) → `actual` (leszerződött, előkészítés) → `implementation` (megvalósítás) → `elszámolás` (monitorizare).

Minden projekt **azonos, nagyon strukturált rendszerben** él. Ez tudatos döntés: bárki a három iroda közül fél óra alatt átvesz egy ismeretlen projektet, mert mindig ugyanott van minden. Van egy belső „internet sztendard" (dokumentum-mentés, projektfelépítés, kommunikáció, aláírás, betűtípus) és egy templét-könyvtár (deviz general, üzleti terv, pénzügyi modell Excel-ek).

### A strukturált rendszer (minden projekt így néz ki)

| Mappa | Tartalom |
|---|---|
| `01_Cerere_de_finantare` | pályázati dosszié: Anexa B üzleti terv, deviz |
| `02_Editabil` | a végleges, szerkeszthető master-dokumentumok |
| `03_Documente_de_lucru` | munkaanyag, kapott dokumentumok, régi verziók |
| `04_Scan` | leadott PDF-ek |
| `05_Semnat` | elektronikusan aláírt, beadott dokumentumok |
| `06_Contract_de_finantare` | támogatási szerződés + acte adiționale |
| `07_Proiect_tehnic` | technikai terv (edit + scan) |
| `08_Dosare_de_achizitii` | beszerzési dossziék: DAC konzultáció, DAP tervezés, DAD dirigenție, DAL munkálatok, DAF szállítás |
| `09_Cereri_de_plata` | kifizetési / elszámolási kérések |
| `10_Monitorizare` | progres-riportok, notificări, Centralizator (SL-követés) |

**Elnevezési konvenció (kötelező):** `sorszám_dokumentumnév_Iniciálé_dátum` (pl. `01.b_THR_Deviz_general_ISZ_30.06.2026`).
**Formátum:** minden kimenő dokumentum Verdana 9.

### Miért ez a workshop kiindulópontja

A régi Haladó egy kaotikus céget rendezett. A Regionál nincs káosz, épp ellenkezőleg: **erős struktúra**. Ezért a mi kiindulópontunk nem a rendrakás, hanem az, hogy **ezt a meglévő, tudatos rendet írjuk le az AI-nak úgy, hogy értse és kövesse**. A struktúra itt előny: pontosan az teszi taníthatóvá az AI-t.

---

## 2. rész: A résztvevő szerepe

A workshopon **te egy Regio-tanácsadó vagy**, aki egy konkrét ügyfél-projektet visz: a Napsugár Tejüzem beruházását. A csapatod strukturált rendszerében dolgozol, sok ismétlődő, senior-igényes szakmunkával. A workshop során az AI-t (Cowork) állítod munkába a saját rendszereden.

Amit **nem** csinálunk: nem építünk agentet (az a Mester szint), nem tanuljuk a szakmádat (a devizt, anexát, elszámolást profin ismered), nem a pályázatírásból indulunk (abban már erős vagy).

Amit **igen**: megtanulod az eszközöket, hogy a napi ismétlődő munkádat magad tudd felgyorsítani.

---

## 3. rész: A projekt: Napsugár Tejüzem

### A projekt egy pillantásra

| Adat | Érték |
|------|-------|
| **Beneficiar** | SC NAPSUGÁR TEJÜZEM SRL (fiktív), CUI RO12345678 |
| **Helyszín** | Cristuru Secuiesc (Székelykeresztúr), jud. Harghita |
| **Projekt** | tejfeldolgozó-üzem bővítése (extindere fabrică de procesare lapte) |
| **Projekt-kód** | THR |
| **Proiectant** | SC PLANTERV STUDIO SRL (fiktív) |
| **Kivitelező** | SC CONSTRUCT TRANSILVANIA SRL (fiktív), CUI RO98765432 |
| **Finanszírozás** | PNRR-szerű építési beruházás, TVA 19%, curs 4,97 lei/EUR |
| **Fázis** | implementation (kivitelezés folyik, monitoring aktív) |

### A pénzügyi kontroll-számok (lei, fără TVA)

Ezeket használjuk végig; minden feladat ezekre a számokra fut ki (megoldókulcs):

| Tétel | Érték |
|---|---:|
| Deviz general TOTAL fără TVA | **6 455 000** |
| TVA (19%) | 1 226 450 |
| Deviz general cu TVA | 7 681 450 |
| Cap. 4 investiția de bază (összesen) | 5 435 000 |
| Ebből 4.1 Construcții și instalații | 3 190 000 |
| Kivitelezői ajánlat végösszege | **5 375 000** |
| F4 eltérés (4.6 Active necorporale hiányzik az ajánlatból) | **−60 000** |
| Anexa B An1 profit net | 1 369 200 |

Az `5_DO1` (Deviz obiectului) bontása: Hala 2 330 000 + Depozit 380 000 + Centrală 270 000 + Amenajări 210 000 = 3 190 000 (ez a 4.1).

### A szereplők (fiktív NPC-k)

| Név | Szerep | Jellem |
|-----|--------|--------|
| **Laci** | senior tanácsadó (Regio) | precíz, tapasztalt, ő látja a deviz-logikát; kiadja a feladatokat |
| **Kinga** | projektfelelős (Regio) | a Napsugár projekt napi gazdája, sok manuális munkával küzd |
| **Beneficiar** | Napsugár Tejüzem ügyvezetése | a 4.6 szoftver-tétel tisztázása vele történik |
| **Kivitelező** | Construct Transilvania | ő adta a szkennelt ajánlatot, amit egyeztetni kell |

### A három napi fájdalom, a Napsugáron keresztül

1. **Szkennelt ajánlat** (`08_.../04.04_DAL_Lucrari/Scan/`): a kivitelező 200 oldal körüli, kép-only PDF-et töltött fel. Kézzel kellene tételesen egyeztetni. → F3.
2. **Deviz-templét**: a levédett, képletvezérelt deviz generalt forrásból kell kitölteni. → F5 (killer-demo).
3. **Monitoring**: a Centralizatorba be kell vezetni az első situație de lucrări-t (SL1), és követni a `Rest de executat`-ot. → F6.

---

## 4. rész: A szimuláció indulása

**Csütörtök reggel.** Belépsz a workshopra. A Napsugár projekt már fut, implementation fázisban. A gépeden ott a `Napsugar_projekt/` mappa: a Regio strukturált rendszere, benne a Napsugár teljes dossziéja. A kivitelező pénteken feltöltött egy szkennelt ajánlatot, a Centralizator frissítésre vár, és a deviz general még nincs lezárva.

Az első kérdés nem az, hogy „mit csinál az AI", hanem hogy **mit csinál veled az AI a saját rendszereden**. Indulhat.
