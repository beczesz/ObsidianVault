---
title: "Dry-Run pontozás — Ignis Academy Haladó AI Workshop"
date: 2026-05-12
author: Becze Szabolcs
status: active
description: "Dry-run értékelés a 6 fázis Cowork-oktatási workshop-járól 25 fős HBC-csoport szimulációjára, 8,1 átlagponttal; erős narratív illeszkedés (9,0) és Cowork-specifikus novitás (8,3), de gyenge hands-on érték (6,5) és F4-F5 érthetőségi kihívások."
description_source: auto
description_hash: e0fa2fc463ae0a21
id: bd5224dc-f2ad-41cd-8f82-92dde2e20594
index_schema_version: 1
bdos_index: true
---
# Dry-Run pontozás — Ignis Academy Haladó AI Workshop

> **Készítette:** Claude (dry-run meta-evaluator)
> **Dátum:** 2026-05-12
> **Skála:** 1-10 (1 = csapnivaló, 5 = elfogadható, 7 = jó, 8-9 = kiváló, 10 = referencia-szintű)
> **Forrás:** A 6 fázis tényleges végrehajtása + az oktatói segédlet v1.0 értékelése egy 25 fős HBC-csoport szimulált perspektívájából.

---

## Összesített pontozási tábla

| Fázis | Érthetőség | Új info (Cowork-spec) | Hasznosság | Narratív illeszkedés | WOW-faktor | Hands-on érték | Realizmus | **Átlag** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Bevezető (0:00-0:30)** | 8 | 6 | 7 | 9 | 7 | 4 | 8 | **7,0** |
| **F1 — Káoszból rend** | 9 | 9 | 9 | 9 | 9 | 6 | 9 | **8,6** |
| **F2 — TODO-k** | 8 | 10 | 9 | 9 | 8 | 7 | 8 | **8,4** |
| **F3 — Pályázat-elemzés** | 7 | 9 | 10 | 8 | 9 | 6 | 8 | **8,1** |
| **F4 — Multi-persona** | 6 | 10 | 9 | 10 | 10 | 5 | 7 | **8,1** |
| **F5 — Pályázat összeáll.** | 6 | 9 | 9 | 9 | 9 | 6 | 6 | **7,7** |
| **F6 — Web redesign** | 9 | 8 | 7 | 8 | 10 | 9 | 8 | **8,4** |
| **Zárás (3:50-4:00)** | 10 | 5 | 8 | 10 | 7 | 9 | 9 | **8,3** |
| **ÖSSZÁTLAG** | **7,9** | **8,3** | **8,5** | **9,0** | **8,6** | **6,5** | **7,9** | **8,1** |

---

## Részletes magyarázat — kritikus pontok

### Érthetőség (7,9 átlag)
A bevezető (8) és a zárás (10) **kiválóan érthető**. F4 és F5 a **legnehezebb** (6) — 3 párhuzamos sub-flow (Legal/Pénzügy/CEO) + 35 perc + komplex prompt-szerkezet → egy AI-szel kezdő résztvevőt **elveszít**. Az oktatói segédlet jó "Mondom"-mondatokkal próbálja kompenzálni, de **valós csoportban** 2-3 résztvevő kiesik az F4-F5 sávban.

### Új info (Cowork-spec) — átlag 8,3
A workshop **igazi súlypontja**. F1 (project memory CLAUDE.md), F2 (Productivity plugin session-ök közötti emlékezés), F3 (cross-document analízis 94 oldalra), F4 (Legal plugin + multi-doc cross-check) **mind Cowork-specifikus képességek**, amik a ChatGPT-vel nem reprodukálhatóak. F6 (web-generálás) viszont ChatGPT-vel is megoldható — itt **8 pont** csak a beépített kontextus-folytonosság (F1-F5 adatai automatikusan a 4 variánsba kerülnek) miatt.

### Hasznosság — átlag 8,5
Minden résztvevő hazaviheti: **a saját cégére átültethető**. A pályázat-narratíva univerzális (AFM helyett ESF, IH-IT, EFOP, GINOP, Horizon EU — mind ilyen szerkezetben). F5 a **legmagasabb** (9-10): az "AI tölti ki a formot" élmény minden résztvevőnek **másnap reggel reprodukálható**.

### Narratív illeszkedés — átlag 9,0
**A workshop legszebb erőssége.** A film-metafora **nem ürügy** — minden fázis **a story-bookba illeszkedik**. F4 a csúcs (10): a Béla bácsi-szál F1-ben elindul (szerződés bekerül a kaotikus mappába), F2-ben sejtetve (meeting transcript 41. mondat), F3-ban felszínesen ✅ (Data Board zöld), **F4-ben drámailag felfedezik** (Cowork cross-doc), **F5-ben végkifejlet** (declarație notarială bekerül a csomagba). Ez **forgatókönyv-szintű** színvonal.

### WOW-faktor — átlag 8,6
**F4 és F6 a TOP 10-es** — a Béla bácsi-felfedezés és a 3 weboldal-variáns 4 perces parádéja. F1-F3 **konzisztens 9** (gap-analízis a 94 oldalra, eligibility-pontszám 65/100). A bevezető **csak 7** (a film-metafora jó, de **első benyomásra** nem WOW — az csak F1 közepén jön).

### Hands-on érték — átlag 6,5 ← **A workshop GYENGE PONTJA**
Az oktatói segédlet 70/20/10 arányt **ígér**, de **a valós megvalósításban 80/15/5** lesz. Minden fázis HANDS-ON-ja **rövid, irányított, nem termel kézzelfogható output** (F1: "kérdezz egy dolgot", F3: "ellenőrizz 1 kritériumot", F4: "diktálj 1 slide-újrahangolást"). Az F6 a **kivétel** (9): mindenki **saját weboldal-variánst készít**. **Ez a HANDS-ON arány nagyon növelhető** — lásd a `jelentes.md` minden fázis "Javítási ötlet" szakasza.

### Realizmus — átlag 7,9
**Erős**, de **2 megjegyzés**:
1. **F5 (6)** — a MySMIS form-mockup **nem natív MySMIS portál**. A real MySMIS-szel a "Cowork tölti ki magától" **csak browser-automation-nel** működne (Chrome MCP, vagy Cowork is még nem ad MySMIS-integrációt). Egy résztvevő, aki **másnap reggel megpróbálja**, **kísértés-szerű csalódást** élhet meg.
2. **F4 (7)** — a "Béla bácsi visszaválaszol 2 nap múlva" előre megrendelve van. A workshop **manipulált narratíva**, **ami OK** mert oktatási kontextusban, **de** az élményt **akkor** csökkenti, ha egy résztvevő rákérdez: "ez most élő válasz vagy előre megírt?".

---

## Top 3 erősség

1. **Narratív íve katarktikus** (átlag 9,0). A 4 órás "film" **valóban film** — a Béla bácsi-szál, az EBITDA-szál, a Comic Sans-vs-modern-kontraszt **mind szorosan illeszkednek** a story-bookba. Egy Apple keynote és egy HBO-mini-sorozat **kombinált energiája** — és ez ritka workshop-anyagban.

2. **A Cowork-spec funkciók kiemelése konkrét és mérhető** (átlag 8,3). Nem **általános AI-marketing** ("milyen ügyes!"), hanem **konkrét képesség-érvek**: project memory (F1), session-ök közötti emlékezés (F2), cross-document analízis (F4), kontextus-folytonosság (F5). **Mindegyik mérhetően jobb mint a ChatGPT** — és **mindegyiket élőben látjuk**.

3. **Az értékpropozíció óriási** (átlag 8,5 hasznosság + 9,0 narratív). Egy **3 000 EUR-os tanácsadói anyag + 25 fős workshopra reprodukálva** = **az oktatás közvetlen ROI-ja egyértelmű**. A 30 000 RON / HBC-csoport ár **védhető**.

---

## Top 3 fejlesztendő pont

1. **Hands-on érték (6,5)** — **A 70/20/10 arány csak névleges, valódi 80/15/5.** A HANDS-ON pillanatok rövidek, irányítottak, ritkán produkálnak kézzelfogható outputot. Javaslatok:
   - **F1**: HANDS-ON-ban **a résztvevők írják meg közösen a CLAUDE.md-t** (5 perc, csoportmunka).
   - **F3**: a **12 kritériumot 3 csapatra osztani**, mindegyik 4-et értékel → versenyhelyzet + outputot termel.
   - **F4**: a 3 sub-flow szétbontása **3 csoportra** (Legal / Pénzügy / CEO) — mindegyik 12 percig dolgozik, aztán bemutat.
   - **F5**: a Form-mockup hibavadászat helyett **identitás-élmény** ("írd át a saját cégnevedre").
   - **F6**: már jó (9) — modellként szolgálhat a többinek.

2. **Realizmus a 4-5 sávban (átlag 6,5 F4+F5)** — a manipulált beérkezések (Béla bácsi-válasz, Mihaela-Excel) **dramaturgiailag erősek**, **de** ha a résztvevő rákérdez, az élmény-illúzió **gyorsan szétesik**. Javaslat:
   - **Becsületesen elmondani** a bevezetőben: "A workshop a TransOffice-t **5 nap** alatt mutatja be **4 órában** — egyes válaszok és emailek **a film miatt fiktívek**, de **a Cowork-képességek mind valódiak**." → az átláthatóság **növeli** a bizalmat.
   - **F5**: a MySMIS-mockup helyett **valós magyar/román online form** (NAV, ANAF, e-Romania) — egy egyszerűbb, **valódi-formra** → reprodukálható másnap reggel.

3. **F4 35 perc kevés, F5 35 perc még kevesebb** — az időtervezésben **csúszás-tűrés 0**. Javaslat:
   - **F4 → 40 perc**, **F5 → 40 perc**, **F6 → 20 perc** (a 25 percből 5 percet le lehet vágni a "régi oldalon vidám-bizarr-zoomolás" szakaszból). Összes 4 óra változatlan.
   - Vagy: **F6-ot 15 percre rövidíteni**, mert a vizuális csúcs **nem igényel 25 percet** — 15 perc bőven elég 2 variáns + 1 hands-on alkotásra.

---

## Egy mondatos overall vélemény

A workshop **filmszerűen erős, narratíván Apple-keynote-osan kidolgozott**, és **a Cowork-spec képességeket konkrétan és mérhetően mutatja be** — **de** a 70%-os DEMO-arány a gyakorlatban 80% felé csúszik, és **a tényleges tanuló-aktivitást** úgy lehetne **átemelni 6,5-ről 8,5-re**, ha **minden fázisban legalább egy 5-8 perces csoportmunka** kerülne be, ami **kézzelfogható outputot termel**.

---

## Számszerű összegzés

- **6 fázis + Bevezető + Zárás átlag: 8,1 / 10**
- **Legmagasabb fázis: F1 (8,6)** — a workshop nyerő nyitása
- **Legalacsonyabb fázis: Bevezető (7,0)** — túl sok információ rövid idő alatt
- **Top kritérium: Narratív illeszkedés (9,0)** — referencia-szintű
- **Gyenge kritérium: Hands-on érték (6,5)** — egy fókusz-átdolgozás indokolt

**Ajánlás:** **Indítható v1.0-ként élesben**, de a v1.1 (post-dry-run) **kötelezően** módosítsa a hands-on arányt.
