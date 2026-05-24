# Chaos Engineering Workshop

**Omnichannel platform felkészítési program**

---

**Prepared for:** MVMI Informatika Zrt.

**Contact:** Dabóczi Mihály, Szacsúri László

**Offer Date:** 2026-04-14

**Version:** 1.0

**Security Classification:** Confidential

**Prepared by:** Becze Szabolcs, Cloud Platform Services, Sonrisa Technologies

---

## 1. Vezetői összefoglaló

A Sonrisa CPS egy 3 hetes intenzív Chaos Engineering Workshop programot javasol az MVMI Omnichannel platformjának üzemeltetői csapata számára. A program célja, hogy a csapat szimulált, kontrollált környezetben gyakorolhassa az incidenskezelést, és ezáltal magabiztosabban reagáljon éles helyzetekben.

A megközelítésünk a chaos engineering filozófiáját követi: strukturált, hipotézis-vezérelt kísérletezés a rendszer különböző rétegein, ahol a CPS "támadó" (Red Team) és az MVMI csapat "védő" (Blue Team) szerepben dolgozik együtt.

---

## 3. A szolgáltatás terjedelme

A program három fázisból áll. Az első két fázis képezi a 3 hetes intenzív workshop-ot, a harmadik fázis egy folyamatos, éves program.

### 3.1 Oktatási fázis (1-2. hét)

A CPS csapat egy strukturált roadmap-et készít az Omnichannel rendszer különböző területeihez, és kiadja a tananyagot az MVMI csapatnak. A csapat önállóan dolgozza fel az anyagot, a CPS pedig rendelkezésre áll kérdések megválaszolására és konzultációra.

**Tartalom:**

- Chaos engineering alapelvek: hipotézis-vezérelt kísérletezés, steady state definiálás, blast radius minimalizálás
- Az Omnichannel rendszer architektúrális áttekintése támadási felületenként
- Monitoring mélymerülés: Kibana (logok), Grafana (metrikák), Jaeger (trace-ek) hatékonyabb használata
- Incidenskezelés best practice: eszkalációs utak, kommunikáció, post-mortem sablon
- Runbook írási gyakorlat: hogyan dokumentáljuk az incidensválaszokat

**Deliverable:** Chaos Engineering Roadmap dokumentum, incidenskezelés sablon, runbook template-ek.

### 3.2 Gyakorlati fázis / GameDay-ek (3. hét)

A gyakorlati fázis az oktatási fázis eredményétől függően alakul - minél jobban halad a csapat, annál komplexebb szcenáriókkal dolgozunk. A cél az, hogy itt töltsük a legtöbb időt, élőben gyakorolva az incidenskezelést.

A CPS Red Team-ként tervezett, kontrollált hibaforrásokat injektál az Omnichannel rendszerbe, míg az MVMI Blue Team-ként detektál, diagnosztizál és helyreállít. Minden GameDay egy 4 órás strukturált session, amelyet felkészülési idő és post-mortem review egészít ki.

**4 szcenárió-típus, az Omni rendszerre szabva:**

| # | Típus | Konkrét Omni példák | Idő |
|---|-------|---------------------|-----|
| 1 | **Alkalmazás szintű hiba** | Kezeletlen kivétel a Portal/API rétegben; Data Bridge hibás válasz az SAP IS-U felé; Translation Service kiesés; Config Server rossz érték injektálás | 4 óra + felkészülés |
| 2 | **Terhelési szimuláció** | API gateway throttling / kvóta lock; RabbitMQ queue overflow; PostgreSQL connection pool kimerülés; Redis cache flush; NFS I/O túlterhelés | 4 óra + felkészülés |
| 3 | **Security audit** | Fraudulens felhasználói aktivitás szimuláció; OAuth2 token manipuláció; Log elemzés Kibana-ban; Integráció visszaélés nyomkövetés (Facekom, CIB) | 4 óra + felkészülés |
| 4 | **Komponens knockout** | Teljes API réteg kiütése (gateway down); PostgreSQL primary node kiesés (failover); Data Bridge leállítás (SAP IS-U megakad); OpenShift pod/node kiütés; Firebase kiesés | 4 óra + felkészülés |

**Deliverable:** Szcenáriótervek, GameDay jegyzőkönyvek, post-mortem review dokumentumok, MTTR mérési eredmények.

### 3.3 Folyamatos Chaos Engineering program (éves, ajánlott!)

A 3 hetes intenzív workshop önmagában megalapozza a szemléletet, de a valódi eredmény a folyamatos gyakorlásból jön. Az incidenskezelés olyan készség, amit rendszeresen kell edzeni.

A folyamatos program keretében havi 40 lehívható órát biztosítunk, amelyből a CPS minden hónapban legalább egy szimulációt tervez és végrehajt a rendszer különböző területein. A keret rugalmasan beosztható: a szimulációk mellett konzultáció, runbook fejlesztés, monitoring finomhangolás és post-mortem review is benne van. A csapat minden hónapban más típusú kihívással találkozik, így fokozatosan lefedi az Omni rendszer teljes támadási felületét.

A havi MTTR mérések objektíven mutatják a fejlődést, és az év végére az MVMI csapat önállóan, magabiztosan fogja kezelni a legtöbb incidenst.

- Havi 40 lehívható óra keretszerződés
- Havonta legalább 1 szimulált GameDay session (CPS tervezi és végrehajtja)
- Új szcenáriók a rendszer különböző területeire (nem ismétlés)
- MTTR mérés és fejlődés követés havi riporttal
- Időtartam: 2026. májustól 2027. áprilisig (12 hónap)

**Formátum:** Chaos Engineering as a Service. Nem passzív oktatás, hanem aktív, szimulált incidenskezelési gyakorlat a rendszer különböző rétegein.

---

## 4. Időkeretterv

| Hét | Fázis | Deliverable-ök | CPS ráfordítás |
|-----|-------|----------------|----------------|
| 1-2. hét | Oktatási fázis | Roadmap, monitoring workshop, runbook sablonok, incidenskezelési folyamat | ~40 óra |
| 3. hét | GameDay-ek (4 session) | Szcenáriótervek, élőben végrehajtott szimuláció, post-mortem review-k | ~20 óra aktív + felkészülés |
| Hét 3 vége | Zárás | Összesítő riport, fejlesztési ajánlások, MTTR baseline | Benne van a 3. hétben |
| Május 2026 - Április 2027 | Folyamatos program | Havi GameDay, új szcenáriók, MTTR mérések | 40 óra/hó |

A pontos indulási időpont egyeztetés tárgyát képezi. A 3 hetes intenzív workshop hét elején indul és péntek délután zárással végződik.

---

## 5. Csapat és megközelítés

### 5.1 CPS csapat (Red Team)

A chaos engineering-ben a CPS a Red Team (támadó), az MVMI üzemeltetői csapata a Blue Team (védő). A CPS csapat feladata a hibák tervezése, injektálása és a post-mortem review levezetése.

| | Red Team (CPS) | Blue Team (MVMI) |
|---|---|---|
| **Szerep** | Hibákat tervez és injektál | Detektál, diagnosztizál, helyreállít |
| **Cél** | Felderíteni a gyenge pontokat | Bizonyítani, hogy képesek kezelni |
| **Tudás** | Mély architektúrális ismeret | Operatív üzemeltetési tudás |
| **Output** | Szcenáriótervek, post-mortem | Incidenskezelés, runbookok, MTTR |

### 5.2 CPS csapat feladatai fázisonként

**1. fázis (Oktatás):** Architect / Coach szerep. Roadmap készítés, elméleti alapok, monitoring workshop, incidenskezelési best practice, runbook írási gyakorlat.

**2. fázis (GameDay-ek):** Red Team Lead. Szcenáriók tervezése és végrehajtása. Minden GameDay után post-mortem review.

**3. fázis (Folyamatos):** Havi új szcenáriók, egyre komplexebbek. MVMI MTTR mérés és fejlődés követés.

---

## 6. Árazás

### 6.1 3 hetes intenzív workshop

| Tétel | Mennyiség | Egységár | Összeg |
|-------|-----------|----------|--------|
| Oktatási fázis + GameDay-ek (0.5 FTE, 3 hét) | 15 nap (60 óra) | 200.000 Ft/nap | 3.000.000 Ft |
| **Workshop összesen** | | | **3.000.000 Ft** |

### 6.2 Folyamatos program (éves)

| Tétel | Mennyiség | Egységár | Összeg |
|-------|-----------|----------|--------|
| Havi fix keretszerződés (12 hónap) | 40 óra/hó | 200.000 Ft/nap | 2.000.000 Ft/hó |
| 12 hónap összesen | 480 óra | | 24.000.000 Ft |
| **Folyamatos program összesen** | | | **24.000.000 Ft** |

### 6.3 Teljes összesítés

| Tétel | Összeg |
|-------|--------|
| 3 hetes intenzív workshop | 3.000.000 Ft |
| Folyamatos program, 12 hónap | 24.000.000 Ft |
| **TOTAL** | **27.000.000 Ft** |

Az árak nettó árak, az ÁFA külön számítandó.

---

## 7. Feltételek

### 7.1 Érvényesség

Jelen ajánlat 2026. május 14-ig érvényes. Az érvényességi idő lejártát követően az ajánlat felülvizsgálat után újra kiértékelendő.

### 7.2 Előfeltételek

- Az MVMI biztosítja a szükséges hozzáféréseket a teszt/staging környezetekhez (OpenShift, monitoring stack, adatbázisok)
- A GameDay session-ök nem éles környezetben történnek, hacsak erről külön megállapodás nem születik
- Az MVMI operációs csapat (Blue Team) résztvevőinek rendelkezésre állása a session-ök idején
- A CPS csapat előzetesen egyeztetett időpontokban végzi a szimulált hibainjektálást

### 7.3 Ami nem képezi az ajánlat részét

- Éles környezetben történő chaos engineering (külön megállapodás tárgyát képezi)
- Fejlesztési munka (hibajavítás, új feature-ök) - a workshop célja az üzemeltetési képesség fejlesztése
- Harmadik felek rendszereinek tesztelése (SAP IS-U éles rendszer, CIB Bank, Facekom)
- Hardver vagy infrastruktúra beszerzés
                                                                            