---
title: "MVMI Omni Support -- Chaos Engineering Workshop"
date: 2026-04-13
author: Becze Szabolcs
status: active
description: "Chaos engineering workshop az MVMI Omni Support csapatának 3 hetes intenzív képzése, amely gyakorlati szimulációkkal felkészíti az operátorokat önálló incidenskezelésre az OpenShift-alapú omnichannel platformon. Két fázisból áll: elméleti oktatás majd szimulált outage-szcenáriók, ahol az MVMI csapat gyakorol CPS támogatással."
description_source: auto
description_hash: 00e760bf1d16d50c
id: fbb08f3a-aefe-4107-bf76-52655c131b1c
index_schema_version: 1
bdos_index: true
---
# MVMI Omni Support -- Chaos Engineering Workshop

## Quick Info

| Field | Value |
|-------|-------|
| **Status** | Planning |
| **Tipus** | Projekt (3 het) + upsell lehetoseg |
| **Idotartam** | 3 het intenziv + folyamatos (ev vegeig, ha upsell sikeres) |
| **MVMI oldal** | Daboczi Mihaly, Szacsuri Laszlo |
| **CPS oldal** | Becze Szabolcs + csapat (TBD) |
| **Platform** | Omnichannel rendszer -- OpenShift (OCP), Angular portal, iOS/Android mobil, PostgreSQL, RabbitMQ, Redis, SAP IS-U integraciok |
| **Meglevo szerzodes** | 3000031047 (2027.02.07-ig), uj szerzodes kell 2026.01.01-tol 2 evre |
| **Muszaki melleklet** | Omnichannel support musz.mell_7x24_uj musz.pdf |
| **Indulas** | TBD |

## Mi ez a projekt

Chaos engineering workshop az MVMI Omni Support uzemeltetoi csapatanak. A cel: felkesziteni az MVMI operacios csapatot arra, hogy onalloan kezeljenek incidenseket, outage-eket es biztonsagi esemenyeket, szimulalt kornyezetben.

Ket fazisbol all: eloszor oktatasi fazis (elmeleti roadmap + napi konzultacio), utana gyakorlati fazis (szimulalt outage-ek, amiket az MVMI csapatnak kell megoldania CPS tamogatassal).

## Forrasok

- Meeting transcript: 2026 aprilis, resztvevok: Becze Szabolcs, Daboczi Mihaly, Szacsuri Laszlo (+ Szanto Zoltan, Vaida Mark-Adam roviden)
- Muszaki melleklet: `../Omnichannel support műsz.mell_7x24_új műsz.pdf` (10 oldal, Toth Istvan, 2026-04-13)

## A rendszer amit "tamadunk" -- technikai attekintes

**Forras: Omnichannel support musz.mell, 1. fejezet**

Az Omni rendszer az MVM aram- es gazszolgaltatasi online ugyfelfiszolgalati keretrendszere, 3M+ haztartast szolgal ki. Komponensek:

| Komponens | Technologia | Leiras | Chaos szcenaroo relevancia |
|-----------|-------------|--------|---------------------------|
| **MVM Next Portal** | Angular, web | Lakossagi ugyintezes (szamlabefizeteas, meroallas, szerzodes) | Frontend hiba szimulacio, UX hatasviizsgalat |
| **Publikus feluletek** | Web | Navigator, meroora-diktalas, szamlafizetees (regisztracio nelkul) | Elerheteosegi teszt, DDoS szimulacio |
| **iOS / Android app** | Mobil | Push ertesites, biometrikus azonositas | Mobil-specifikus outage |
| **MVM Next Admin** | Web | Uzemeltetesi konfig, tartalomkezeles | Admin feluleti hiba, config corrupttion |
| **MVM Next API** | REST, OAuth2, OCP gateway | Kozponti API reteg, SAP IS-U kapcsolat, hitelesites, terheleslelosztas | **Fo tamadasi felulet**: throttling, auth hiba, gateway outage |
| **Data Bridge-ek** | Mikroszolgaltatasok | Omni <-> SAP IS-U kommunikacio | Integraacios hiba szimulacio, cso bedugulas |
| **Meroora kezeles** | Backend | Fogyasztasi adatok, allas diktalas, szamlazasi mod | Adatinkonzisztencia szimulacio |
| **Ertesites kezeles** | RabbitMQ, aszinkron | Email, push, rendszeruzenet | Queue overflow, message loss |
| **Config Server** | Kozponti config | Kornyezetfuggo beallitasok | Config corruption, rossz ertek injektalas |
| **Translation Service** | Kozponti | Feliratok, hibauzennetek | Nyelvi szolgaltatas kieses |
| **PostgreSQL klaszter** | OCP-ben futoo | Kozponti adatbazis, HA | DB failover, replication lag, connection pool kimerules |

**Monitoring stack:** OpenTelemetry Collector -> Elasticsearch/Kibana (logok), Prometheus/VictoriaMetrics/Grafana (metrikak), Jaeger (trace-ek). Redis cache. OAuth2 hitelesites. NFS log archivalas.

**Integracios partnerek:** MVM Fiok, Linistry/Hotline, MVM AD, Facekom, Firebase, Google Geocode, Rocketmail, CIB Bank.

**Meglevo SLA (7x24):**

| Prioritas | SLA | Meresi idoszak |
|-----------|-----|----------------|
| Kritikus | 8 munkaora | 7x24 (0:00-24:00) |
| Magas | 16 munkaora | 7x24 |
| Normal | 4 munkanap | 7x24 |
| Alacsony | 60 munkanap | 7x24 |

**Fontos:** Ez 7x24, nem 5x11 mint az AzureDevOps szerzodees! Keszenlet idoszakban (munkaidon kivul) e-mail + telefon elerheteoseg kell.

**Havidijas szolgaltatasok (PDF 2.1. pont):**
1. Szoftvertamogatasi szolgaltatas es szoftverkovetes
2. SM rendszerben beerkezett ticketek kezelese, hibaelharitas, eszkalas
3. Altalanos szakertoi konzultacios tamogatas
4. 7x24 rendelkezesre allas, keszenlet munkaidon kivul

**Szakertoi orakeret (PDF 2.3. pont) -- ez a chaos engineering workshop helye:**
- Konzulensi tamogatas: testreszabas, tervezoi tanacsadas, projektjellegu feladatok, idoszakos konzultaciok, **tematikus oktatasok**
- Testreszabasi feladatok tamogatasa: valtozaskezeles, interfeszek, rendszerszervezes
- Dokumentaciok: funkcionalis spec, rendszerterv, elesitesi terv, DRP, uzemeltetesi kezikonyv

## Engagement struktura (transcript alapjan)

### 1. fazis: Oktatasi fazis (~2-3 het)

- **Formatum:** Napi ~4 oras session-ok, ~2-3 heten at
- **Tartalom:** CPS keszit egy roadmap-et, hogy miket kell atnezni
- **Interakcio:** MVMI csapat tanul es kerdez, CPS rendelkezesre all valaszolni
- **Cel:** Elmeleti alap megteremtese a gyakorlati fazis elott

### 2. fazis: Gyakorlati fazis (szimulacio)

- **Formatum:** Intenziv par oras session-ok, tobbszor egymas utan
- **Logika:** CPS "tamadja" / rontja a rendszert, MVMI csapat javitja es helyreallitja
- **CPS szerepe:** Szcenariok kitalaalasa + vegrehajtasa + konzultacio ha elakadnak
- **MVMI szerepe:** Rendszer epen tartasa, helyreallitas, root cause analysis

**4 alapszenariotipus (Szacsuri Laszlo javaslata) -- rendszerre szabva:**

| # | Szenariotipus | Konkret Omni peldak | Becsult ido |
|---|---------------|---------------------|-------------|
| 1 | **Alkalmazas szintu hiba** | Kezeletlen kivetel a Portal-ban vagy API retegben; Data Bridge hibas valasz az SAP IS-U fele; Translation Service kiesese (feliratok eltunnek); Config Server rossz ertek injektalas | 4 ora + felkeszules |
| 2 | **Terhelesi szimulacio (battle test)** | API gateway throttling / kvota lock; RabbitMQ queue overflow az Ertesites kezelesben; PostgreSQL connection pool kimerules; Redis cache flush; fajl I/O tulterhelees az NFS log szerveren | 4 ora + felkeszules |
| 3 | **Security audit szenaroo** | Fraudulens felhasznaloi aktivitas szimulacio (pl. tobb fiok, gyanils tranzakciok); OAuth2 token manipulacio; log elemzes Kibana-ban: ki mit csinalt, mikor; Facekom / CIB Bank integracio visszaeles nyomkovetes | 4 ora + felkeszules |
| 4 | **Komponens knockout** | Teljes API reteg kiutese (gateway down); PostgreSQL primary node kiesese (failover teszt); Egy Data Bridge leallitasa (SAP IS-U kommunikacio megaakad); OpenShift pod/node kiutese; mobil push (Firebase) kiesese | 4 ora + felkeszules |

**Osszesen: min. 4x4 ora = 16 ora aktiv gyakorlati session + 8-16 ora felkeszulesi ido CPS oldalon (szcenaroo tervezes, kornyezet elokkeszites)**

### 3. fazis: Folyamatos program (upsell)

- **Formatum:** Havonta ~40 lehivhato ora, havi 1 szimulacio
- **Idotartam:** Ev vegeig (2026 december)
- **Cel:** Folyamatosan "tamadni" amig az MVMI csapat onalloan, ugyesen meg tudja oldani
- **Erveleset:** Nekik ez "nem penz" -- ha meg tudjuk ervelni miert kell, megfinanszirozzak
- **Tipusa:** Managed service jellegu, de oktatas + gyakorlat kombinacio

## Open Items

- [ ] Platform / technologia meghatarozasa (mit tamadunk)
- [ ] Pontos idotartam es kezdes egyeztetese
- [ ] CPS csapat kivalasztasa (ki csinalja a szcenariokat)
- [ ] Roadmap keszitese az oktatasi fazishoz
- [ ] 4 szenariotipus reszletes kidolgozasa
- [ ] Arajanlatot keszitese (3 hetes intenziv + upsell havi dij)
- [ ] Feedback kor: Szabolcs + Misi + Laszlo
- [ ] Upsell pitch megfogalmazasa az ev vegeig tartao programra

## CPS szerep: Red Team

A chaos engineering-ben a CPS a **Red Team** (tamado), az MVMI uzemeltetoi csapata a **Blue Team** (vedo).

| | **Red Team (CPS)** | **Blue Team (MVMI)** |
|---|---|---|
| **Szerep** | Hibakat tervez es injektal | Detektal, diagnosztizal, helyrealit |
| **Cel** | Felderiteni a gyenge pontokat | Bizonyitani, hogy kepesek kezelni |
| **Tudas** | Mely architekturalis ismeret (mi epitettuk) | Operativ uzemeltetesi tudas |
| **Output** | Szcenariotervek, post-mortem review | Incidenskezeles, runbookok, MTTR javulas |

**CPS konkret feladatai fazisokra bontva:**

**1. fazis (Oktatas):** Architect / Coach szerep -- roadmap, elmeleti alapok, monitoring (Kibana/Grafana/Jaeger), incidenskezelesi best practice, runbook irasi gyakorlat

**2. fazis (GameDay-ek):** Red Team Lead -- szcenariok tervezese + vegrehajtasa. GameDay formatum: Owner + Coordinator (CPS), Reporter + Observer (MVMI). Minden GameDay utan post-mortem review.

**3. fazis (Upsell):** Folyamatos Red Team -- havi uj szcenariok, egyre komplexebbek. MVMI MTTR meres es fejlodes kovetes.

**Miert mi:** CPS az egyetlen csapat aki eleg melyen ismeri az Omni rendszert (mi epitettuk). Kulso chaos engineering ceg nem ismeri az SAP IS-U integraciokat, Data Bridge logikat, OpenShift konfigot.

## Arazes

**Napidij:** 200.000 HUF/nap

### 3 hetes intenziv (kulon projekt)

| Tetel | Oraszam | Napok | Osszeg (Ft) | Osszeg (EUR ~400) |
|-------|---------|-------|-------------|-------------------|
| Heti 20 ora (0,5 FTE) x 3 het | 60 ora | 15 nap | 3.000.000 | ~7.500 |

### Upsell -- havi fix (ev vegeig)

| Tetel | Oraszam/ho | Napok/ho | Havi dij (Ft) | Havi dij (EUR) | Eves (8 ho) |
|-------|------------|----------|---------------|----------------|-------------|
| Havi 40 ora fix | 40 ora | 10 nap | 2.000.000 | ~5.000 | 16.000.000 (~40.000 EUR) |

**Tartalom (NEM passziv oktatas):** Havonta GameDay szcenariok a rendszer kulonbozo teruleltein -- alkalmazas hibak, terhelesi tesztek, security audit szcenariok, komponens knockout. Chaos Engineering as a Service.

**Osszesites ha mindketto megvalosul:**

| Tetel | Osszeg (Ft) | Osszeg (EUR) |
|-------|-------------|-------------|
| 3 hetes intenziv workshop | 3.000.000 | ~7.500 |
| Upsell 8 honap (majus-december) | 16.000.000 | ~40.000 |
| **TOTAL** | **19.000.000** | **~47.500** |

## Kovetkezo lepesek

1. Szabolcs: megerosites a platformrol es technikai reszletekrol
2. CPS: professzionalis ajanlat megfogalmazasa + beaarazas
3. Feedback kor: Szabolcs + Misi + Laszlo egyeztetes
4. Dontesek: csapat, roadmap, idopont

## Related Files

- MVMI Omni Support NOTES: `../NOTES.md`
- (Arajanlat: TBD)
- (Roadmap: TBD)
