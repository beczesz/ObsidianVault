---
title: "🎬 Oktatói segédlet — Ignis Academy Haladó AI Workshop (HBC)"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Oktatói segédlet a TransOffice esettanulmányon alapuló 4 órás AI workshophoz, amely a Claude Cowork eszköz és a fájl, todo és pályázati munkafolyamatok szervezésén keresztül tanít. Tanároknak és facilitátoroknak ajánlott."
description_source: auto
description_hash: 8ddb6d9b68621dad
id: 2aeb750a-885d-4d2e-8fc1-4f5e341e8b22
index_schema_version: 1
bdos_index: true
---
# 🎬 Oktatói segédlet — Ignis Academy Haladó AI Workshop (HBC)

> **Verzió:** 1.0 (első kiadás)
> **Készült:** 2026-05-12
> **Hossz:** 4 óra (240 perc) — délelőttöd elejétől 4 órán át
> **Csoport:** 10-15 fő, HBC közösség
> **Helyszín:** [oktatói teremmel kell, projektor + WiFi]
> **Eszközök:** Claude Cowork (Pro), Obsidian, oktatói laptop projektorral
> **Tananyag verzió:** Tananyag v1.3

---

## 📋 Tartalomjegyzék

1. [Hogyan használd ezt a segédletet](#hogyan-használd-ezt-a-segédletet)
2. [Pre-workshop checklist (T-30p)](#pre-workshop-checklist-t-30p)
3. [Idővonalas áttekintés](#idővonalas-áttekintés)
4. [Nyitány (0:00 → 0:30)](#nyitány)
5. [F1 — Rend a fájlok között (0:30 → 0:55)](#f1)
6. [F2 — Rend a TODO-k között (0:55 → 1:20)](#f2)
7. [SZÜNET 1 (1:20 → 1:35)](#szünet-1)
8. [F3 — Pályázati elemzés (1:35 → 2:05)](#f3)
9. [F4 — Multi-persona kommunikáció (2:05 → 2:40)](#f4)
10. [SZÜNET 2 (2:40 → 2:50)](#szünet-2)
11. [F5 — Pályázat összeállítás (2:50 → 3:25)](#f5)
12. [F6 — Web redesign (3:25 → 3:50)](#f6)
13. [Zárás (3:50 → 4:00)](#zárás)
14. [Appendix A — Prompt library (copy-paste)](#appendix-a)
15. [Appendix B — Q&A best practices](#appendix-b)
16. [Appendix C — Vészforgatókönyv](#appendix-c)
17. [Verzió-előzmények](#verzió-előzmények)

---

## Hogyan használd ezt a segédletet

Ez a segédlet **élő segítség** — workshop közben pillantasz rá, nem előadod fejből.

**Jelölések:**
- 🎤 **[DEMO]** — élő képernyő-megosztás, te csinálod
- ✋ **[HANDS-ON]** — résztvevők csinálják, te segítesz
- 💬 **[BESZÉLGETÉS]** — kérdezz, várd a válaszokat
- ☕ **[SZÜNET]** — kávé, mosdó, levegő
- 📍 **Mondom:** — pontos mondat amit te mondasz (idézőjelben javasolt)
- 🖥 **Csinálom:** — konkrét tool akció (mit kattintok, mit nyitok)
- ⏱ **Idő:** — várt szegmens-hossz
- ⚠️ **Vigyázz:** — kritikus pont vagy gyakori hiba
- 🔄 **Csúszás-terv:** — ha futsz az időben, mit hagyj ki

**Tippek a segédlet használatára:**
- Nyomtasd ki és tedd magad mellé a laptophoz
- Vidd magaddal egy filctollat — jelöld meg ahol csúsztál (utólagos javítás)
- A *prompt library (Appendix A)* külön nyomtatva a kezed ügyében legyen — onnan másolod a Cowork-be
- Az `[asset:...]` hivatkozásokat a Tananyag mappához kell érteni

---

## Pre-workshop checklist (T-30p)

### 30 perccel a kezdés előtt érkezz a helyszínre

**Technikai ellenőrzés (10 perc):**

| ☐ | Tétel | Hogyan |
|---|-------|--------|
| ☐ | Projektor működik | Csatlakoztasd a laptopot, ellenőrizd a felbontást |
| ☐ | WiFi stabil | Próbáld ki: nyiss meg egy webvideót, fusson 1 percig |
| ☐ | Claude Cowork bejelentkezve | Pro account, billentyűzd be a jelszót előre |
| ☐ | Obsidian megnyitva | A `Tananyag/` vault legyen aktív |
| ☐ | Hangerő OK | Ha lesz video, állítsd be középre |
| ☐ | Laptopok feltöltve | Charger csatlakoztatva, 100% töltöttség |
| ☐ | Másik internet (mobile hotspot) | Vészhelyzet esetén |

**Asseteket előkészíteni (10 perc):**

| ☐ | Tétel | Hol |
|---|-------|-----|
| ☐ | `Tananyag/TransOffice/` mappa MEGNYITVA Obsidian-ban | Bal oldali fa |
| ☐ | `meeting_transcript_20250224.md` ELŐRE NYITVA | Egyik tab |
| ☐ | `Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md` ELŐRE NYITVA | Másik tab |
| ☐ | `szerzodes_chirie_TransOffice_2018.docx` letöltve | Asztalon |
| ☐ | `bilant_TransOffice_2023_2024.xlsx` letöltve | Asztalon |
| ☐ | `transoffice_old_website.html` MEGNYITVA browser tabban | Ott legyen |
| ☐ | Claude Cowork — Productivity plugin AKTIVÁLVA | Settings → Plugins |
| ☐ | Claude Cowork — Legal plugin AKTIVÁLVA | Settings → Plugins |
| ☐ | Prompt library kinyomtatva | Asztalon kezed ügyében |

**Mentális checklist (10 perc):**

| ☐ | Tétel |
|---|-------|
| ☐ | Olvasd át a Story Book-ot egyszer (`Műhely/00_Tervezes/00_STORY_BOOK.md`) |
| ☐ | Ellenőrizd a 3 szünet időpontját — írd fel táblára |
| ☐ | Készíts elő egy poharat vízzel |
| ☐ | 1 perc csendes lélegzés |

---

## Idővonalas áttekintés

| Idő (kumulatív) | Szegmens | Hossz | Típus |
|------------------|----------|-------|-------|
| 0:00 → 0:30 | **NYITÁNY** | 30p | Bevezetés + szabályok |
| 0:30 → 0:55 | **F1** Rend a fájlok között | 25p | 🎤 demo + ✋ micro |
| 0:55 → 1:20 | **F2** Rend a TODO-k között | 25p | 🎤 demo + ✋ micro |
| 1:20 → 1:35 | ☕ **SZÜNET 1** | 15p | kávé |
| 1:35 → 2:05 | **F3** Pályázati elemzés | 30p | 🎤 demo + ✋ micro |
| 2:05 → 2:40 | **F4** Multi-persona kommunikáció | 35p | 🎤 demo + ✋ micro |
| 2:40 → 2:50 | ☕ **SZÜNET 2** | 10p | kávé |
| 2:50 → 3:25 | **F5** Pályázat összeállítás | 35p | 🎤 demo (WOW) |
| 3:25 → 3:50 | **F6** Web redesign | 25p | 🎤 demo + ✋ micro |
| 3:50 → 4:00 | **ZÁRÁS** | 10p | összefoglaló + Q&A |

**Példa órakönyvvel:**
- 9:00 kezdés → 13:00 zárás
- 10:20-10:35: SZÜNET 1
- 11:40-11:50: SZÜNET 2

---

## 🎬 NYITÁNY
**Idő:** 0:00 → 0:30 (30 perc) · **Cél:** Mindenki helyén legyen, megismerkedjenek a kerettel, megérezzék a stake-eket

### Felkészülés (T-2p)
- Projektoron a TransOffice mappa látható (Obsidian, jobb oldalt prevu)
- A `Ceg_leiras_TransOffice.md` előre nyitva
- A „Welcome" slide (ha van) projektoron — vagy csak az Obsidian

### Lépésről lépésre

| ⏱ | Mód | Lépés |
|---|----|------|
| 0:00 → 0:03 | 💬 | **Üdvözlés + bemutatkozás** |
| 0:03 → 0:08 | 💬 | **Csoportos bemutatkozás** — mindenki 1 mondat: ki vagy, hány %-ban használod most az AI-t |
| 0:08 → 0:15 | 🎤 | **A workshop ívének bemutatása** — film-metafora |
| 0:15 → 0:22 | 🎤 | **TransOffice bemutatása** — a cég, Márton, a káosz |
| 0:22 → 0:27 | 🎤 | **A pályázati pisztolymisszió** — 7 nap, 200k EUR, AFM Mobilitate Verde |
| 0:27 → 0:30 | 💬 | **Szabályok + kérdezz bátran** |

### Részletek

**0:00 — Üdvözlés (3p)**
- 📍 **Mondom:** „Sziasztok! Köszönöm hogy itt vagytok. Ma 4 óra alatt egy fiktív céget fogunk káoszból kihúzni — beadunk vele egy 200.000 eurós EU-pályázatot. És megérzitek mit jelent ha az AI mellettetek dolgozik."
- ⚠️ **Vigyázz:** Ne mondd hogy „megtanítom" — mondd hogy „megtapasztaljátok". Ez nem tool-tanulás, hanem élmény.

**0:03 — Csoportos bemutatkozás (5p)**
- 📍 **Mondom:** „Mielőtt belekezdünk, körbemegyünk. Egy mondatban mondd: ki vagy, mivel foglalkozol, és **mennyi %-ban használod most az AI-t a napi munkádban**. Csak egy mondat — nem előadás."
- 🖥 **Csinálom:** Nézem az időt, ne menjen túl 5 percen
- ⚠️ **Vigyázz:** Egy „nullás" résztvevő itt **kínosnak érezheti magát** — légy melegszívű, „remek, ma kezdesz"

**0:08 — A workshop íve (7p)**
- 📍 **Mondom:** „A workshop egy film. Ti vagytok az új Operations Manager a TransOffice-nél. 4 óra alatt végigviszitek a céget a káoszból egy beadott pályázatig. 6 felvonás lesz — F1-től F6-ig. Mindegyik 20-35 perces. A film közben **megmutatok valamit**, aztán **ti kipróbáljátok**. Tényleg dolgozunk, nem csak nézzünk."
- 🖥 **Csinálom:** Mutatom a 6 fázis listáját az Obsidian-ban (a Tananyag/ mappa szerkezete)

**0:15 — TransOffice + Márton + káosz (7p)**
- 🖥 **Csinálom:** Megnyitom a `00_Bevezetes/Ceg_leiras_TransOffice.md`-t
- 📍 **Mondom:** „Ez itt TransOffice Trade SRL. Székelyudvarhely, Hargita megye. 22 éves cég, irodai eszközöket árul. Az anyu kezelte az adminisztrációt 20 évig. Most a fia, Márton átvette — és kiderült, hogy **az anyu fejében volt minden**. Excel-dzsungel, email-káosz, papír-hagyaték. Ti vagytok az új ember, aki rendet rak."
- 🖥 **Csinálom:** Scrollozom le a fájlt — látszik a struktúra
- ⚠️ **Vigyázz:** NE olvasd fel — mutogass és narrálj saját szavakkal

**0:22 — A pályázat (5p)**
- 📍 **Mondom:** „És van egy kemény határidő: az AFM Mobilitate Verde pályázat. 200.000 euró elektromos járműflottára. **Ezen a héten** be kell adni, vagy lemaradtok. Egy hét, egy ember, egy káosz, egy AI."
- 🖥 **Csinálom:** Megmutatom a `Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.pdf` borítóját
- 📍 **Mondom:** „És látjátok, ez itt egy 94 oldalas román nyelvű pályázati kiírás. Ezt valakinek el kellene olvasnia. Erre is fogunk visszatérni."

**0:27 — Szabályok (3p)**
- 📍 **Mondom:** „Két szabály. Egy: **kérdezz bátran**, bármikor. Két: ha **lassú vagyok**, vagy túl gyors, szóljatok. Nem a tempóban verseny ez, hanem az élményben."
- 📍 **Mondom:** „Két szünet lesz: kb. [10:20] és kb. [11:40]. Most kezdjük!"

### Csúszás-terv
- Ha 5 perccel előbb végzel → kérdezz: „Ki lenne kíváncsi mire ebből?" (várakozás-építés)
- Ha 5 perccel csúszol → vágd rövidebbre a bemutatkozást vagy a workshop-ív szekciót
- Ha 10+ perc csúszás → kihagyod a részletes TransOffice bemutatást, csak megmutatod a mappa-szerkezetet

### Átkötés F1-be
- 📍 **Mondom:** „Oké. Első napunk Márton mellett. Második kávé reggelinél elkapja az új embert — itt kezdődik az első felvonás."

---

## 🎬 F1 — Rend a fájlok között
**Idő:** 0:30 → 0:55 (25 perc) · **Cél:** A résztvevők megtapasztalják ahogy 30+ kaotikus fájlt az AI 5 percben átlát

### Asset
- `Tananyag/TransOffice/` mappa (30+ rendezetlen fájl)
- `Tananyag/01_Ceg_megertes/Feladat_1.1.md`

### Felkészülés (T-2p)
- Claude Cowork előre megnyitva, új projektben
- TransOffice mappa hozzáadva projekt-kontextusként
- Egy üres chat-tab előkészítve

### Lépésről lépésre

| ⏱ | Mód | Lépés | Hossz |
|---|----|------|--------|
| 0:30 → 0:32 | 🎤 | Márton kávés monológja — felolvasod a Feladat_1.1-ból | 2p |
| 0:32 → 0:34 | 🎤 | A klasszikus út: 30 fájl, 2 nap, kézzel | 2p |
| 0:34 → 0:42 | 🎤 | **DEMO:** Cowork áttekinti a TransOffice mappát | 8p |
| 0:42 → 0:47 | ✋ | **HANDS-ON:** mindenki kérdez 1 dolgot a Cowork-től | 5p |
| 0:47 → 0:51 | 🎤 | **DEMO:** CLAUDE.md generálás (project memory) | 4p |
| 0:51 → 0:54 | 💬 | „Mi volt a meglepő?" | 3p |
| 0:54 → 0:55 | 🎤 | Átkötés F2-be | 1p |

### Részletek

**0:30 — Márton monológja (2p)**
- 🖥 **Csinálom:** Megnyitom a `Feladat_1.1.md` szituáció szekcióját
- 📍 **Olvasom (lassan, beszédes hangon):** „Figyelj, elfelejtettem mondani tegnap — csütörtökön lesz egy meeting egy pályázati tanácsadóval. Valami AFM-es elektromos járműflotta pályázat, elég sok pénz. De ahhoz hogy értelmes dolgokat mondjak neki, tudnom kéne mi a helyzet a cégnél rendszer-szinten. Tudnál nekem egy gyors összefoglalót csinálni?"
- 📍 **Mondom:** „Csütörtökig van időd. 30+ fájl van a TransOffice/ mappában. Hogyan kezdesz hozzá?"

**0:32 — A klasszikus út (2p)**
- 📍 **Mondom:** „Régen ez 1-2 nap lett volna: megnyitod mind a 30 fájlt, kézzel jegyzetelsz, Excelben átlapozol, kérdezel anyut telefonon. Most viszont meghallgassátok mit csinál a Cowork."

**0:34 — DEMO (8p) — ez a fő WOW**
- 🖥 **Csinálom:** Cowork-be írom be a promptot (Appendix A.1)
- 📍 **Mondom közben (narrálás):** „Itt a mappa, ezt látjátok — 30+ fájl. Nézzétek mit csinál most a Cowork: olvas, párhuzamosan olvas, és **összevet**..."
- 🖥 **Csinálom:** Várok kb. 30-60 mp-et amíg fut
- 📍 **Mondom (amíg a Cowork dolgozik):** „Figyeljétek meg: nem csak elolvas, hanem **rangsorol**. Megmondja melyik a fontos. És felteszi a kérdéseket amiket ti tettetek volna fel."
- 🖥 **Csinálom:** Mutatom a kimenetet — kiemelek 2-3 dolgot, NEM olvasok fel mindent
- ⚠️ **Vigyázz:** Ha túl gyors a kimenet és tömör, magyarázd el. Ha túl bő, mondd: „Ezt nem fogjuk most felolvasni — letöltheted majd."

**0:42 — HANDS-ON (5p) — első mikro-aktivitás**
- 📍 **Mondom:** „Most ti jöttök. Mindenki nyissa ki a Cowork-et a saját laptopon (vagy csatlakozzon hozzám a képernyő-megosztással ha még nincs Pro). **1 kérdést** tegyél fel a Cowork-nek: bármilyet, amit te megkérdeznél a fájlokról."
- 📍 **Példák amit dobok:**
  - „Hány aktív ügyfél van?"
  - „Melyik a legrégebbi nem frissített Excel?"
  - „Van itt valami pénzügyi ellentmondás?"
- 🖥 **Csinálom:** Körbejárok (vagy minden résztvevő mutat), 2-3 válasz közösen megnézünk
- ⚠️ **Vigyázz:** Egyiküknek sem fog működni az **első kérdése úgy ahogy elképzelte** — ez normális. Mondd: „És most kérdezzünk pontosabban. Mit hagytál ki a kontextusból?"

**0:47 — DEMO: CLAUDE.md (4p)**
- 📍 **Mondom:** „Most jön a varázslat. A Cowork most felépít magának egy **project memory** fájlt — egy CLAUDE.md-t. Ez azt jelenti, hogy amikor legközelebb leülünk dolgozni, **nem kell elölről magyarázni**, hogy ki a TransOffice."
- 🖥 **Csinálom:** Bekérem a Cowork-től a CLAUDE.md-t (Appendix A.2 prompt)
- 📍 **Mondom:** „Látjátok — ez az `Operations & Systems Manager` szerep, a cég kontextusa, a fő fájlok. **Egy fájl, és minden alkalmaztáskor tudja a Cowork ki vagyok és hova tartozom.**"

**0:51 — „Mi volt a meglepő?" (3p)**
- 📍 **Mondom:** „Mielőtt továbbmegyünk: **valaki mondjon egy dolgot ami meglepő volt**. Bármit."
- ⚠️ **Vigyázz:** Várj türelmesen a választ. **Ne te beszélj.** Ha 10 mp után senki — adj egy konkrét kérdést („Tibi, te mit gondoltál?")

**0:54 — Átkötés F2-be (1p)**
- 📍 **Mondom:** „Oké, a fájlok rendben. De Márton közben odadob egy másik bombát. Másnap reggel összejön Enikővel egy sürgős meetingre — a pályázati tanácsadó **azt mondta, ezen a héten kell beadni**. Mit teszünk a meeting-jegyzetekkel?"

### Csúszás-terv
- Ha 3+ perc csúszol → kihagyhatod a "Mi volt a meglepő?" szekciót
- Ha 5+ perc csúszol → a HANDS-ON-t rövidítsd 3 percre (csak 1 résztvevő mutatja)
- Ha 8+ perc csúszol → kihagyhatod a CLAUDE.md DEMO-t (jegyezd fel, F2-be áttoljuk)

### Csúszás-mentő trükk
A CLAUDE.md generálást **át lehet vinni a F2 nyitóblokkjába** ha kell — ott a Cowork „még emlékszik a TransOffice-ra" momentum tökéletes.

---

## 🎬 F2 — Rend a TODO-k között
**Idő:** 0:55 → 1:20 (25 perc) · **Cél:** Mutasd be a Productivity plugint, ahogy a kaotikus meeting-transcriptből végrehajtható TODO-k lesznek

### Asset
- `Tananyag/TransOffice/meetings/meeting_transcript_20250224.md` (Enikő + Márton kétfős sürgős)
- `Tananyag/02_Meeting_Productivity/Feladat_2.1.md`, `Feladat_2.2.md`

### Felkészülés (T-2p)
- A meeting transcript előre megnyitva
- Cowork-ben: **Productivity plugin aktiválva**
- Üres TODO-lista a plugin-ben (semmi régi)

### Lépésről lépésre

| ⏱ | Mód | Lépés | Hossz |
|---|----|------|--------|
| 0:55 → 0:57 | 💬 | Átvezetés: „Sürgős meeting Enikővel" | 2p |
| 0:57 → 1:00 | 🎤 | Productivity plugin bemutatása | 3p |
| 1:00 → 1:08 | 🎤 | **DEMO 1:** Transcript → TODO-k a plugin-be | 8p |
| 1:08 → 1:11 | ✋ | **HANDS-ON:** „Mi a nyitott feladatom?" — új sessionben kérdezz | 3p |
| 1:11 → 1:18 | 🎤 | **DEMO 2:** TODO-kból email-vázlatok (F2.2) | 7p |
| 1:18 → 1:20 | 🎤 | Átkötés F3-ba | 2p |

### Részletek

**0:55 — Átvezetés (2p)**
- 📍 **Mondom:** „Másnap reggel. Márton odaszól Enikőnek: '15 perc múlva irodában, sürgős.' Az új ember (te) jelen vagy. Enikő hozza a számokat, Márton hozza az ideget. **A meetingen kiderül: 2 hónapja a radarjuk alatt van ez a pályázat, és senki nem nézte rendesen meg.**"

**0:57 — Productivity plugin bemutatása (3p)**
- 📍 **Mondom:** „A Cowork-nek van egy beépített **Productivity plugin**-ja. Ez NEM a ChatGPT. A ChatGPT elfelejti amit mondtál — a Cowork **megjegyzi** a TODO-kat, session-ök között is. Egy belső TODO-listát épít."
- 🖥 **Csinálom:** Megnyitom a plugin tab-et — üres állapot
- 📍 **Mondom:** „Nézzétek — most üres. Most behozzuk a meeting transcript-et."

**1:00 — DEMO 1: Transcript → TODO (8p)**
- 🖥 **Csinálom:** Behúzom a `meeting_transcript_20250224.md`-t a Cowork-be
- 📍 **Mondom:** „Itt a transcript. 4 oldal, két ember, kaotikus. Nézzétek mit csinál a Cowork."
- 🖥 **Csinálom:** Beírom a promptot (Appendix A.3)
- 📍 **Mondom közben:** „A plugin nem csak listát csinál — **felelőst is rendel**, **határidőt is becsül**, és **megjegyzi**. Nézzétek a kimenetet..."
- 🖥 **Csinálom:** Mutatom az elmentett TODO-kat a plugin tab-ban — kiemelek 2-3 érdekeset
- ⚠️ **Vigyázz:** Itt jó eséllyel megjelenik a **Béla bácsi említés** is a transcript-ben — DE most NE hangsúlyozd. Ez egy F4-es trigger lesz.

**1:08 — HANDS-ON: új session (3p)**
- 📍 **Mondom:** „És most a kulcsmomentum. Csukjuk be a Cowork chat-tabot. Nyissunk egy **újat**. És kérdezzétek meg: **„Mik a nyitott feladataim?""**
- 🖥 **Csinálom:** Új chat tab, beírom a kérdést
- 📍 **Mondom:** „Látjátok? Nem felejtette el. A ChatGPT-vel ez nem így működne."
- ⚠️ **Vigyázz:** Ez a momentum **a kulcs WOW** — várd meg amíg leesik a tantusz. Csendben hagyni. **Ne magyarázd túl.**

**1:11 — DEMO 2: TODO-kból emailek (7p)**
- 📍 **Mondom:** „A TODO-k megvannak. De mit kezdünk velük? Néhány ezt mondaná: 'átírom Word-be, formázom, elküldöm.' Helyette nézzétek mit csinál a Cowork."
- 🖥 **Csinálom:** Promptot beírom (Appendix A.4) — kérek 2 follow-up emailt + akciótervet
- 📍 **Mondom közben:** „Két különböző hangnem: Enikőhöz közvetlen, kollegális. A külsős könyvelőhöz formálisabb. Ugyanaz az adat, **két stílus, 30 mp**."
- 🖥 **Csinálom:** Mutatom a kimenetet — felolvasok 2-3 mondatot belőle

**1:18 — Átkötés F3-ba (2p)**
- 📍 **Mondom:** „A TODO-k megvannak. A levelek kész. De az első akadály ott áll: **a 94 oldalas pályázati kiírás**. Senki nem olvasta végig. Pályázhatunk-e egyáltalán? Erre 30 perc múlva válaszolunk."

### Csúszás-terv
- Ha 3+ perc csúszol → a DEMO 2-t rövidítsd 4 percre (csak 1 email + akcióterv)
- Ha 5+ perc csúszol → kihagyhatod a HANDS-ON-t (csak DEMO marad)

### Átmenet a szünetbe
- 📍 **Mondom:** „Most jön a kávészünet. **15 perc**, [10:35-kor folytatjuk]. Igyatok kávét, sétáljatok, kérdezzetek tőlem a szünetben ha van."

---

## ☕ SZÜNET 1
**Idő:** 1:20 → 1:35 (15 perc)

### Mit csinálsz a szünet alatt
1. **Indítsd újra a Cowork-öt** ha lassul (memória-felszabadítás)
2. **Vizet igyál**
3. **Mosdó**
4. **Töltsd az aksit** ha még nincs csatlakoztatva
5. **Készítsd elő az F3 promptot** (Appendix A.5) — copy-paste ready
6. **Ne dolgozz a laptopon** — a résztvevők kérdezni fognak, ők a fontosabbak

### Mit figyelj
- Ki marad a teremben és kérdez → **gold** (őket priorítsd a következő blokkokban)
- Ki megy ki és nem jön vissza 10 percig → szólj rájuk udvariasan
- Ha a csoport hangulata **fáradt** → az F3-ban növelje a sebességet
- Ha **lendületes** → az F3 részleteit ráhúzhatod

### Visszaindítás
- **Pontosan 1:35-kor:** „Visszajöttünk. Kávé volt? Akkor jön a 3. fázis. Itt **a 94 oldalas pályázati kiírás** kerül elő."

---

## 🎬 F3 — Pályázati elemzés
**Idő:** 1:35 → 2:05 (30 perc) · **Cél:** A résztvevők lássák ahogy az AI egy 94 oldalas dokumentumot **döntésalapú elemzéssé** alakít

### Asset
- `Tananyag/03_Dontes_Elemzes/Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md`
- `Tananyag/03_Dontes_Elemzes/Pelda_outputok/` (3 minta-output ha szükség lesz)

### Felkészülés (T-2p)
- A pályázati kiírás MD-je projekt-kontextusba adva
- Egy üres chat-tab
- Productivity plugin még aktív (előző session-ből megvannak a TODO-k)

### Lépésről lépésre

| ⏱ | Mód | Lépés | Hossz |
|---|----|------|--------|
| 1:35 → 1:38 | 💬 | Átvezetés: „És itt a 94 oldal" | 3p |
| 1:38 → 1:48 | 🎤 | **DEMO 1 (F3.1):** Eligibility check — pályázhatunk-e? | 10p |
| 1:48 → 1:51 | ✋ | **HANDS-ON:** 1 kritérium ellenőrzése (pl. „CR-08 járműflotta") | 3p |
| 1:51 → 1:57 | 🎤 | **DEMO 2 (F3.2):** 17 melléklet × cégadatok gap analízis | 6p |
| 1:57 → 2:00 | ✋ | **HANDS-ON:** 1 melléklet gap (pl. „M-11 járműflotta-leltár") | 3p |
| 2:00 → 2:03 | 🎤 | **DEMO 3 (F3.3):** Data Completion Board | 3p |
| 2:03 → 2:05 | 🎤 | Átkötés F4-be | 2p |

### Részletek

**1:35 — Átvezetés (3p)**
- 🖥 **Csinálom:** Megnyitom a 94 oldalas pályázati kiírás MD-jét — gyorsan görgetve
- 📍 **Mondom:** „Ez egy 94 oldalas, románul írt, jogszabály-stílusú pályázati kiírás. Egy normál ember **2-3 nap** alatt rágja át magát rajta — és nagy a hibalehetőség. A Cowork-kel **30 perc múlva eldöntjük, pályázhatunk-e**. És nem csak igen/nem — hanem **strukturáltan, indoklással, kockázatokkal**."
- 📍 **Mondom:** „Ez nem összefoglalás. Ez **döntéstámogatás**."

**1:38 — DEMO 1: Eligibility (10p)**
- 🖥 **Csinálom:** Beírom a promptot (Appendix A.5)
- 📍 **Mondom közben:** „Figyeljétek meg: a Cowork most **párhuzamosan olvas két dolgot** — a pályázati kiírást és a TransOffice cégadatokat (amik már a CLAUDE.md-ben vannak). És **összeveti**."
- 🖥 **Csinálom:** Várok kb. 60-90 mp-ig
- 📍 **Mondom (amíg dolgozik):** „Egy emberi tanácsadó ezt **napokig** csinálná. És valószínűleg drágábban."
- 🖥 **Csinálom:** Mutatom a 12 eligibility kritérium táblázatát — kiemelek 3-4 érdekes pontot
- 📍 **Mondom:** „Látjátok — 10 ✅, 2 ⚠️. A 2 figyelmeztetés: a pénzügy és a telephely-bérleti viszony. **Ez a 2 ⚠️ lesz az F4 startja.**"

**1:48 — HANDS-ON (3p)**
- 📍 **Mondom:** „Most ti jöttök. Válasszatok 1 kritériumot — pl. CR-08, a járműflotta. Kérdezzétek meg külön: 'Teljesítjük-e CR-08-at? Részletesen, indoklással.'"
- 🖥 **Csinálom:** 1-2 résztvevő bemutatja a saját kimenetét
- ⚠️ **Vigyázz:** Ha valaki **mást kap mint én** — örülj neki, és magyarázd el miért: „A Cowork minden kérdést új kontextusban értelmez."

**1:51 — DEMO 2: Gap analízis (6p)**
- 🖥 **Csinálom:** Új chat-tab, prompt: „Listázd ki a 17 kötelező mellékletet és minden mellékletre jelöld: VAN / NINCS / RÉSZBEN a TransOffice cégadatok alapján."
- 📍 **Mondom közben:** „Ez itt egy **gap analízis** — az AI nem csak listáz, hanem **összevet és értékel**. Ami megvan, ami hiányzik, ami részben — és **honnan szerezzük be**."
- 🖥 **Csinálom:** Mutatom a kimenetet — 17 sor, 3 oszlop (név, státusz, akció)

**1:57 — HANDS-ON (3p)**
- 📍 **Mondom:** „Kérdezzétek meg külön: 'A M-11 számú mellékletet — a járműflotta-leltárt — hogyan állítanám össze, és kitől szerezném be?'"
- 🖥 **Csinálom:** 1-2 résztvevő bemutatja

**2:00 — DEMO 3: Data Completion Board (3p)**
- 📍 **Mondom:** „Most jön a coup de grâce. Ez az egész elemzés átalakul **akciótervvé**."
- 🖥 **Csinálom:** Prompt: „Az eligibility + gap analízisből generálj Data Completion Board-ot: oszlopok = Tétel, Felelős, Határidő, Forrás, Státusz."
- 🖥 **Csinálom:** Mutatom a táblát — 14 sor, mindegyik felelőssel
- 📍 **Mondom:** „**Ezt egy tanácsadó 3000 EUR-ért adná.** 30 perc, ingyen."

**2:03 — Átkötés F4-be (2p)**
- 📍 **Mondom:** „A tábla megvan: 8 felelős, 14 határidős feladat, 3 kockázat. De **most jön a neheze**. Ezeket az adatokat be is kell szerezni. Email a könyvelőnek románul. Bérleti szerződés ellenőrzés. Prezentáció a CEO-nak. **3 ember, 3 stílus, 35 perc.**"

### Csúszás-terv
- Ha 3+ perc csúszol → a 2 HANDS-ON közül kihagyod az egyiket
- Ha 5+ perc csúszol → a DEMO 3-at rövidítsd 1 percre (csak megmutatod, nem építed)
- Ha 8+ perc csúszol → kihagyhatod a DEMO 3-at (a Pelda_outputok mappából csak megmutatod a kész táblát)

### Vészterv
- Ha a Cowork **vissza-vissza akad** a 94 oldalon → használd a `Pelda_outputok/` mappát mint backup-ot: „itt vannak előre legenerált válaszok demonstrációs célra"

---

## 🎬 F4 — Multi-persona kommunikáció
**Idő:** 2:05 → 2:40 (35 perc) · **Cél:** 3 különböző célközönséghez 3 különböző stílusú kimenet — Béla bácsi cross-document momentum

### Asset
- `Tananyag/TransOffice/szerzodes_chirie_TransOffice_2018.docx` (bérleti szerződés)
- `Tananyag/04_Legal_Szerzodes/emails/bela_bacsi_valasz/email.md`
- `Tananyag/04_Legal_Szerzodes/emails/mihaela_konyvelo_valasz/email.md` + `bilant_TransOffice_2023_2024.xlsx`

### Felkészülés (T-2p)
- Legal plugin aktiválva
- A bérleti szerződés docx letöltve, megnyitható
- A 2 válasz-email és Excel előkészítve (de NE nyisd meg — a workshop dramaturgiához tartozik a „megérkezés")

### Lépésről lépésre

| ⏱ | Mód | Lépés | Hossz |
|---|----|------|--------|
| 2:05 → 2:08 | 💬 | Átvezetés: „3 ember, 3 stílus" | 3p |
| 2:08 → 2:20 | 🎤 | **F4.1 DEMO — Legal sub-flow:** Bérleti szerződés + Béla bácsi felfedezés | 12p |
| 2:20 → 2:31 | 🎤 | **F4.2 DEMO — Pénzügy:** Mihaela email + Excel feldolgozás | 11p |
| 2:31 → 2:38 | 🎤 | **F4.3 DEMO — CEO PPTX:** 5 slide + ✋ MICRO: „slide újrahangolása saját szavakkal" | 7p |
| 2:38 → 2:40 | 🎤 | Átkötés SZÜNET 2-be | 2p |

### Részletek

**2:05 — Átvezetés (3p)**
- 📍 **Mondom:** „A Data Completion Board megvan. Most ki kell tölteni. **3 ember**, akiket meg kell keresnünk: a tulajdonos (Béla bácsi), a könyvelő (Mihaela), és a főnök (Márton). **3 stílus** — 3 lépés, 35 perc."

#### F4.1 — Legal sub-flow (12p) — ez a Béla bácsi WOW

**2:08 — Bérleti szerződés mélységi ellenőrzése**
- 🖥 **Csinálom:** Behúzom a `szerzodes_chirie_TransOffice_2018.docx`-et a Cowork-be
- 📍 **Mondom:** „Ez egy 7 oldalas bérleti szerződés románul. A telephelyünk a Béla bácsié — a TransOffice ott bérel. **A pályázathoz be kell mutatnunk** hogy a telephely 5 évig stabil. Olvassa át a Cowork, hogy stimmel-e."
- 🖥 **Csinálom:** Prompt (Appendix A.6) — kérek deep-check + cross-document referenciák
- 📍 **Mondom közben:** „Figyeljétek meg ezt — most a Cowork **nemcsak ezt a szerződést olvassa, hanem a többi fájlt is**, hogy keressen kapcsolódó dolgokat..."
- 🖥 **Csinálom:** Várok 60-90 mp-ig

**2:11 — A Béla bácsi felfedezés** — *ez a workshop egyik legjobb momentuma*
- 🖥 **Csinálom:** Mutatom a kimenetet — a Cowork **megtalálja** hogy a meeting transcript-ben van egy említés Béla bácsiról ("említette hogy szeretné eladni az egyik telephelyét")
- 📍 **Mondom (lassan, drámaian):** „**Itt egy fontos dolog**. A Cowork nemcsak a szerződést olvasta — visszanézte a meeting transcript-et is. És talált egy mondatot, ami **a múlt héten elhangzott**: Béla bácsi említette, hogy szeretné eladni az egyik területét. Lehet, hogy nálunk lesz a következő. **Ez egy red flag.**"
- ⚠️ **Vigyázz:** Ha a Cowork NEM találja meg automatikusan → mondd: „Cowork, nézd meg a meeting transcript-et is — van-e Béla bácsi említés?" — most már megtalálja
- 📍 **Mondom:** „És most mit teszünk? **Levelet írunk Béla bácsinak.** Megkérdezzük közvetlenül."

**2:15 — Email Béla bácsinak**
- 🖥 **Csinálom:** Prompt: „Írj udvarias levelet Béla bácsinak — Kovács Márton nevében — kérdezve hogy mi a helyzet a bérleményünkkel a következő 5 évre. Hangnem: tiszteletteljes, közvetlen, magyaros (Béla bácsi 70 éves)."
- 🖥 **Csinálom:** Mutatom a kimenetet
- 📍 **Mondom:** „És most a varázslat. A workshop fiktív világban folyik — de tegyük fel hogy ez a levél elment. **Béla bácsi válaszolt is.**"
- 🖥 **Csinálom:** Megnyitom a `bela_bacsi_valasz/email.md`-t
- 📍 **Mondom (felolvasok 2-3 mondatot):** „...szóval Béla bácsi azt írja hogy a bérleményünk **biztos a következő 5 évre**, de hozzátenné, hogy ha eladni is fogja a területet, **csak a TransOffice-nak adná el**. Tehát nemcsak nincs veszély — **vételi lehetőség is nyílt**."

**2:19 — DCB frissítés**
- 🖥 **Csinálom:** Prompt: „Frissítsd a Data Completion Board-ot — a bérleti kockázat státusza most VAN (zöld). Adj hozzá egy új sort: 'Béla bácsi vételi lehetőség — F5 üzleti tervhez.'"
- 📍 **Mondom:** „Ezt nevezzük **cross-document elemzésnek**. Egy bérleti szerződés → egy meeting transcript → egy email → egy frissített DCB. **Az AI köti össze a szálakat.**"

#### F4.2 — Pénzügy sub-flow (11p)

**2:20 — Email Mihaelának**
- 🖥 **Csinálom:** Prompt: „Most írj emailt **románul** Mihaela Florian-nek, a külsős könyvelőnek. Kérjünk pénzügyi adatokat a 2023 és 2024 évre: árbevétel, EBITDA, alkalmazotti adatok. Hangnem: professzionális de közvetlen. A pályázat AFM Mobilitate Verde 2025."
- 🖥 **Csinálom:** Mutatom a román email-t
- 📍 **Mondom:** „Látjátok — a Cowork **románul ír**, és a hangnem stimmel. Mihaela ezt két nap múlva válaszolja. **Tegyük fel ez megtörtént.**"

**2:24 — Excel feldolgozás**
- 🖥 **Csinálom:** Megnyitom a `mihaela_konyvelo_valasz/email.md`-t és a `bilant_TransOffice_2023_2024.xlsx`-et
- 📍 **Mondom:** „Mihaela visszaküldte. Megnyitottuk. **30 sor, 8 oszlop**. Egy emberi szem 10 percig keresgélne benne. Nézzétek mit csinál a Cowork."
- 🖥 **Csinálom:** Prompt (Appendix A.7) — kérek 5 KPI + EBITDA számítás + trendelemzés
- 📍 **Mondom közben:** „A Cowork most **kiszámolja az EBITDA-t** — egy könyvelő ezt szokta. És **megnézi a trendet**: 2023 → 2024 — nőttünk vagy csökkentünk?"
- 🖥 **Csinálom:** Mutatom a kimenetet — EBITDA, marginok, trend

**2:29 — Pénzügyi értelmezés**
- 📍 **Mondom:** „A számok megvannak: 2024 EBITDA 12% — sokkal jobb mint 2023. Ez a pályázatban **erős érv**. És **az adatok kompatibilisek** az F3-as eligibility check-kel. ✅"

#### F4.3 — CEO PPTX (7p)

**2:31 — DEMO: 5 slide CEO prezentáció**
- 📍 **Mondom:** „Márton meeting Mihaelával, most. 8 perc múlva visszajön és **látni akarja: hol tartunk?** Készítsünk egy 5-slide-os prezentációt a Cowork-kel."
- 🖥 **Csinálom:** Prompt (Appendix A.8) — kérek 5 slide PPTX: 1) Helyzet, 2) Eligibility ✅, 3) Pénzügyi készség ✅, 4) Béla bácsi (zöld), 5) Akcióterv
- 🖥 **Csinálom:** Várok 1-2 percig — közben kérdezz: „Mit gondoltok, hogyan érezné magát Márton?"
- 🖥 **Csinálom:** Megnyitom a .pptx-et — slide-ról slide-ra mutatom

**2:35 — ✋ MICRO HANDS-ON: „Slide újrahangolása saját szavakkal" (lásd hands-on javítás)**
- 📍 **Mondom:** „Most ti jöttök. Nézzétek meg az 5 slide-ot. **Melyik slide-on hangzik a legidegenebbül a szöveg** — hogyan mondaná egy magyar/erdélyi CEO? Válasszatok egy slide-ot, és **diktáljátok a Cowork-nek hogyan ÍRNÁTOK át 2-3 mondatban**."
- 🖥 **Csinálom:** Várok 2 percet — közben körbejárok, 1-2 példát közösen megnézünk
- 📍 **Mondom:** „Látjátok — **emberi hangra hangolható**. Az AI nem egy idegen sablon, hanem a ti eszközötök."

**2:38 — Átkötés SZÜNET 2-be (2p)**
- 📍 **Mondom:** „A 3 ember megvan. A DCB frissítve. Márton már szól: **rábólintok, pályázunk**. Most jön a kávészünet — 10 perc. Utána a pályázat **össze is áll**."

### Csúszás-terv F4-re
- Ha 3+ perc csúszol → a CEO prezentáció MICRO-t kihagyod (csak DEMO)
- Ha 5+ perc csúszol → a Mihaela DEMO Excel-elemzést rövidítsd 5 percre
- Ha 8+ perc csúszol → a Béla bácsi sztorit GYORSÍTSD (NE hagyd ki — ez a workshop egyik csúcsa)

---

## ☕ SZÜNET 2
**Idő:** 2:40 → 2:50 (10 perc)

### Mit csinálsz
1. **Idd meg a kávét**
2. **Készítsd elő a Plan de afaceri promptot** (Appendix A.9) — ez a következő DEMO
3. **Készítsd elő a form HTML-t** — `Tananyag/05_Kommunikacio_Email/formular_depunere_AFM_Mobilitate_Verde.html` egy browser tab-ban
4. **Ellenőrizd:** a Cowork még válaszol? Frissítsd az ablakot ha kell

### Mit figyelj
- A csoport energiája — F5 a **WOW blokk**, kell hozzá a megújult figyelem
- Ha látod hogy fáradtak → F5 nyitása legyen **lendületes és gyors**

### Visszaindítás
- 📍 **Mondom:** „És most jön a WOW. A pályázat **össze fog állni 35 perc alatt**."

---

## 🎬 F5 — Pályázat összeállítás
**Idő:** 2:50 → 3:25 (35 perc) · **Cél:** Vizuális csúcspont — a workshop kifutása

### Asset
- `Tananyag/05_Kommunikacio_Email/Plan_de_afaceri_TransOffice_AFM_2025.md` (előre meglévő minta)
- `Tananyag/05_Kommunikacio_Email/Dosar_complet_AFM_Mobilitate_Verde_2025.md` (csomag-checklist)
- `Tananyag/05_Kommunikacio_Email/formular_depunere_AFM_Mobilitate_Verde.html` (MySMIS form mockup)

### Felkészülés (T-1p)
- A form HTML egy browser tab-ban — előre megnyitva
- Cowork chat tisztára visszaállítva (üres session)
- Productivity plugin tab nyitva (a TODO-k ott vannak)

### Lépésről lépésre

| ⏱ | Mód | Lépés | Hossz |
|---|----|------|--------|
| 2:50 → 2:52 | 💬 | Átvezetés: „Most jön a WOW" | 2p |
| 2:52 → 3:05 | 🎤 | **F5.1 DEMO:** Üzleti terv generálás (Plan de afaceri) | 13p |
| 3:05 → 3:13 | 🎤 | **F5.2 DEMO:** Pályázati csomag (23 tételes) | 8p |
| 3:13 → 3:23 | 🎤 | **F5.3 DEMO + ✋ MICRO:** Form kitöltés („te töltöd ki ezt az 1 mezőt" + „Spot the error") | 10p |
| 3:23 → 3:25 | 🎤 | Átkötés F6-ba | 2p |

### Részletek

**2:50 — Átvezetés (2p)**
- 📍 **Mondom:** „Eddig **elemeztünk, kommunikáltunk, adatot szereztünk**. Most **összeáll** minden. Üzleti terv, csomag, form — 35 perc. **És nézzétek meg mit jelent ez:**"
- 🖥 **Csinálom:** Mutatom 30 mp-ig a TransOffice fájl-mappát F1-ből (káosz emlékeztető)
- 📍 **Mondom:** „...innen indultunk."

#### F5.1 — Üzleti terv generálás (13p)

**2:52 — Generálás**
- 🖥 **Csinálom:** Prompt (Appendix A.9) — kérek **teljes Plan de afaceri**-t a Cowork-től: minden szekció (Cégbemutató, Piac, Pénzügyi terv, Marketing, Megvalósítás)
- 📍 **Mondom közben:** „A Cowork most az **eddigi munkából** építi össze: F1 cégadatok + F3 eligibility + F4 EBITDA + Béla bácsi vételi opció. **Nem kell semmit újra elmagyarázni** — minden már a kontextusban van."
- 🖥 **Csinálom:** Várok 2-3 percig — közben **CSENDBEN**, hogy a résztvevők lássák a folyamatot

**2:57 — Eredmény bemutatása**
- 🖥 **Csinálom:** Görgetem a kész Plan de afaceri-t — kiemelek 3-4 érdekes részt
- 📍 **Mondom:** „260 sor, **románul**, profi minőség. Egy tanácsadó 3-5 napig csinálja, 2000-3000 EUR-ért. Mi most **2 perc** alatt generáltuk."

**3:00 — ✋ MICRO HANDS-ON: B-terv bekezdés**
- 📍 **Mondom:** „Egy dolog hiányzik még. **A Plan B-zóna**. Mi van ha ELUTASÍTANAK? Diktáljatok a Cowork-nek hogyan írna erre egy **300 szavas bekezdést** az üzleti tervbe."
- 🖥 **Csinálom:** 1-2 résztvevő példáját közösen megnézzük

#### F5.2 — Pályázati csomag (8p)

**3:05 — Csomag-checklist generálás**
- 🖥 **Csinálom:** Prompt: „Készíts egy 23-tételes pályázati csomag-checklistet a Plan de afaceri + a Data Completion Board alapján. Oszlopok: tételszám, dokumentum, státusz (van/hiányzik), forrás, felelős."
- 🖥 **Csinálom:** Mutatom a táblát
- 📍 **Mondom:** „23 tétel — mindegyiknél tudjuk **hol van, ki kapja, mikor**. **Egyetlen táblázat — egy üzleti karrier könyvtárrá tömörítve.**"

**3:09 — ✋ MICRO: „Mi hiányzik még?"**
- 📍 **Mondom:** „Nézzétek meg a táblát. **Mi az 1 dolog amit kifelejtettünk?**"
- ⚠️ **Vigyázz:** Várj türelmesen 30 mp-et. Ha senki — adj egy hint: „Például egy banki dokumentum?"

#### F5.3 — Form kitöltés (10p) — visual WOW

**3:13 — Form bemutatása**
- 🖥 **Csinálom:** Átkapcsolok a browser tab-ra: `formular_depunere_AFM_Mobilitate_Verde.html`
- 📍 **Mondom:** „Ez itt a pályázati form — **40 mező**, románul. A MySMIS rendszer mockup-ja. **Egy embernek ezt kitölteni** 2-3 óra. Nézzétek mit csinál a Cowork."

**3:14 — Cowork-asszisztált form kitöltés**
- 🖥 **Csinálom:** Prompt: „Tölts ki minden mezőt a formban — használd a Plan de afaceri + Dosar complet + Data Completion Board adatokat. Generálj egy **CSV-t** ami minden mezőhöz tartalmazza az értéket."
- 🖥 **Csinálom:** Várok 1-2 percig — mutatom a kimenetet, **másolom át manuálisan** 5-6 mezőbe a form-ban (gyorsan, hogy lendületes legyen)

**3:17 — ✋ MICRO HANDS-ON: „Te töltöd ki ezt az 1 mezőt"** (hands-on javítás!)
- 📍 **Mondom:** „Megállunk itt egy mezőnél: **„Descrierea proiectului — Proiectului în maxim 300 cuvinte"**. **Most te töltöd ki.** Diktáld a Cowork-nek: hogyan írná te a saját stílusoddal."
- 🖥 **Csinálom:** 1 résztvevő dictate-el, a Cowork generál, beírjuk a form-ba
- 📍 **Mondom:** „Látjátok — **a forma a tiéd lett. Az AI csak a kezed**."

**3:20 — ✋ MICRO HANDS-ON: „Spot the error"** (hands-on javítás!)
- 📍 **Mondom:** „Utolsó kihívás. **A formban 1-2 hiba van.** Pl. lehet, hogy az árbevétel 7 millió RON-ként van beírva, miközben 1.8 millió. **2 perc** — találjátok meg. Kiabáljatok ki amit találtok."
- ⚠️ **Vigyázz:** **Tényleg adj be 1-2 hibát** előzetesen — pl. szándékos elgépelés a CUI-ban vagy az árbevételben. Versengő, mókás hangulat.
- 🖥 **Csinálom:** Aki elsőként megtalál egy hibát, közösen kijavítjuk

**3:23 — Átkötés F6-ba (2p)**
- 📍 **Mondom:** „A pályázat **be van adva**. Eddig a film. **De Márton közben mondja: 'Várj — a weboldalunk katasztrofális. 2012 óta nem nyúltunk hozzá. Mit szólnátok ha az utolsó fél órában megcsinálnánk az újat is?'**"

### Csúszás-terv F5-re
- Ha 5+ perc csúszol → F5.2-t rövidítsd 4 percre (csak megmutatod a kész checklist-et)
- Ha 8+ perc csúszol → F5.3 SPOT THE ERROR mikrot kihagyod
- Ha 10+ perc csúszol → F5.3-at csak 5 percre rövidítsd, kihagyod a MICRO-kat (de **F6-ot ne sértsd**)

---

## 🎬 F6 — Web redesign
**Idő:** 3:25 → 3:50 (25 perc) · **Cél:** Vizuális payoff a fáradt csoportnak — a kreatív AI bemutatása

### Asset
- `Tananyag/06_Marketing_Honlap/website/old/transoffice_old_website.html` (Comic Sans 2012-es rémálom)
- `Tananyag/06_Marketing_Honlap/Feladat_6.1_Redesign_es_variaciok.md`

### Felkészülés (T-1p)
- A régi weboldal **előre nyitva** browser tab-ban
- Cowork chat tisztára visszaállítva
- 3 üres browser tab előkészítve (a 3 új variánsnak)

### Lépésről lépésre

| ⏱ | Mód | Lépés | Hossz |
|---|----|------|--------|
| 3:25 → 3:30 | 🎤 | A régi oldal elemzése — közös nevetés | 5p |
| 3:30 → 3:38 | 🎤 | **F6.1 DEMO:** 3 variáns generálás (Modern / Klasszikus / Erdélyi) | 8p |
| 3:38 → 3:46 | ✋ | **F6.2 HANDS-ON:** mindenki generál egy saját variánst | 8p |
| 3:46 → 3:50 | 🎤 | Átkötés ZÁRÁS-ba | 4p |

### Részletek

**3:25 — A régi oldal (5p)** — *itt szükséges hogy mindenki nevessen*
- 🖥 **Csinálom:** Átkapcsolok a `transoffice_old_website.html` browser tab-ra
- 📍 **Mondom (drámai felzaklatott hangon):** „Hölgyeim és Uraim — **TransOffice Trade SRL, 2012-ben**. Comic Sans betűtípus. Animált csillagok. **Vendégkönyv**. Egy számláló: 14.872 látogató. **Best viewed in Internet Explorer 8 or higher.**"
- 🖥 **Csinálom:** Scrollozok le-fel, minden bizarr elemet megmutatok 3-4 mp-ig
- ⚠️ **Vigyázz:** **Hagyd hogy nevessenek**. Ez a workshop legjobb pillanata. A nevetés energiát ad.
- 📍 **Mondom:** „Márton azt mondja: 'Ez a cégünk arca. Szégyen.' De most fél óra van. **Tudunk-e ebből valamit csinálni?**"

#### F6.1 — 3 variáns generálás (8p)

**3:30 — Variáns 1: Modern (clean B2B)**
- 🖥 **Csinálom:** Prompt (Appendix A.10): „Készíts modern, clean B2B weboldal-variánst a TransOffice számára HTML-ben. Színek: kék/fehér/szürke. Tartalmazza: hero, szolgáltatások, csapat, kapcsolat. Tartalmazza az AFM elektromos járműflotta projektünket is."
- 🖥 **Csinálom:** Várok 60-90 mp-ig, megnyitom egy új tab-ban
- 📍 **Mondom:** „Tiszta, modern, professzionális. Egy B2B ügyfél itt **bizalmat érez**."

**3:33 — Variáns 2: Klasszikus (konzervatív)**
- 🖥 **Csinálom:** Prompt: „És most egy klasszikus változatot — konzervatív, tiszteletet sugárzó. Színek: barna/krém/sötétkék. 20 éves megbízhatóság a fő üzenet."
- 🖥 **Csinálom:** Várok, megnyitom új tab-ban
- 📍 **Mondom:** „Egy állami intézmény, könyvelőiroda, ügyvédi iroda itt **otthon érzi magát**."

**3:36 — Variáns 3: Erdélyi (helyi karakter)**
- 🖥 **Csinálom:** Prompt: „És most egy erdélyi variánst — meleg, helyi, közösségi. Színek: meleg téglavörös/krém/sötétzöld. Hivatkozz Székelyudvarhelyre, helyi értékekre, családi cég jellegre."
- 🖥 **Csinálom:** Várok, megnyitom új tab-ban
- 📍 **Mondom:** „A helyi közösség itt **a sajátjának érzi**."

**3:37 — A 3 variáns összehasonlítása (1p)**
- 🖥 **Csinálom:** Gyorsan átkapcsolom a 3 tab-ot mellettébe
- 📍 **Mondom:** „**5 perc alatt 3 weboldal**. Mind működő, mind más stílusú. **Egy designer csapat 3 hét. Egy AI 3 perc.**"

#### F6.2 — Mindenki saját variáns (8p)

**3:38 — Felkészülés**
- 📍 **Mondom:** „Most ti jöttök. **Mindenki ki választ egyet** a 3 variáns közül, és **egy dolgot változtat rajta**: szín, szlogen, képi koncepció. Bármi. **Diktáld a Cowork-nek**, generáljon, mutasd meg a szomszédodnak."
- 🖥 **Csinálom:** Megnyitom a `Feladat_6.2_Sajat_varians.md`-t — átfutom a sablont
- 📍 **Mondom példák:**
  - „Tedd az erdélyi variánsot lila színbe"
  - „Adj hozzá egy 'Hívjon most' bottom-bar gombot a modern verzióhoz"
  - „Cseréld le a szlogent 'Erdély logisztikai partnere'-re"

**3:40 — Készítés ideje**
- 🖥 **Csinálom:** **Körbejárok**, segítek 2-3 résztvevőnek aki elakadt
- ⚠️ **Vigyázz:** Egyik résztvevőnek **biztosan nem fog rendesen sikerülni** — légy türelmes és segítőkész. „Próbáljuk meg másképp."

**3:44 — Bemutatások (2 perc)**
- 📍 **Mondom:** „Ki készített valami **menőt**? Mutasd meg!"
- 🖥 **Csinálom:** 1-2 résztvevő prevezeti a sajátját — projektoron mutatjuk
- ⚠️ **Vigyázz:** **Ne folyjanak túl a bemutatások** — 4 perc kemény limit

**3:46 — Átkötés ZÁRÁS-ba (4p)**
- 📍 **Mondom (lágy hangon):** „**4 óra alatt** mit csináltunk? Visszanézzünk."
- 🖥 **Csinálom:** Átkapcsolok az F1 régi mappa nézetére → F6 új weboldalakra (split screen ha lehetséges)
- 📍 **Mondom:** „Innen indultunk... ide értünk. **A kérdés most nem hogy mit csinál az AI — hanem hogy MIT csinál Veled az AI?**"

### Csúszás-terv F6-ra
- Ha 3+ perc csúszol → csak 2 variánst generálsz (Modern + Erdélyi)
- Ha 5+ perc csúszol → kihagyod a HANDS-ON-t, csak a 3 variánst mutatod meg
- Ha 8+ perc csúszol → a régi oldal nevetést csak 3 percig, és csak 1 variánst (Modern)
- **F6 sose legyen 0 perc** — ez a workshop vizuális csúcsa, **valamilyen formában** mindenképp legyen

---

## 🎬 ZÁRÁS
**Idő:** 3:50 → 4:00 (10 perc) · **Cél:** Elviszik a tanulságot, közös élmény-záró pont

### Lépésről lépésre

| ⏱ | Mód | Lépés | Hossz |
|---|----|------|--------|
| 3:50 → 3:53 | 🎤 | Visszatekintés a 6 fázisra | 3p |
| 3:53 → 3:57 | 💬 | **„1 mondat amit ma elviszek"** — körkörös | 4p |
| 3:57 → 3:59 | 🎤 | Otthoni gyakorláshoz: bónusz feladatok | 2p |
| 3:59 → 4:00 | 🎤 | Búcsú | 1p |

### Részletek

**3:50 — Visszatekintés (3p)**
- 📍 **Mondom:** „Mit tettünk ma:"
- 📍 **Mondom (lassan, hangsúlyosan, ujjakon számolva):**
  - „**F1** — 30 fájl kaotikus → rendezett CLAUDE.md"
  - „**F2** — kaotikus meeting → 14 mentett TODO"
  - „**F3** — 94 oldalas pályázati kiírás → eligibility + gap + akcióterv"
  - „**F4** — Béla bácsi felfedezés + Mihaela EBITDA + Márton PPTX"
  - „**F5** — teljes Plan de afaceri + 23 tételes csomag + form"
  - „**F6** — Comic Sans → 3 modern weboldal"
- 📍 **Mondom:** „Eddig egy ember 5-7 nap. Ma 4 óra."

**3:53 — „1 mondat amit ma elviszek" (4p)** (hands-on javítás záráshoz!)
- 📍 **Mondom:** „Most utolsó körünk: **mindenki 1 mondatban — mi az 1 dolog amit ma elviszel**. Nem több, nem kevesebb."
- 🖥 **Csinálom:** Körbejárok, mindenki sorrendben mondja, **bólintok, nem kommentálok**
- ⚠️ **Vigyázz:** **Ne kommentáld a mondatokat** — csak figyelj, bólints, „Köszönöm." A vélemények nem cserélhetőek.

**3:57 — Bónusz feladatok (2p)**
- 📍 **Mondom:** „A Tananyag mappában találtok **18 bónusz feladatot** — minden fázishoz 3-4 db. Otthon, a saját tempótokban kipróbálhatjátok. **Ne másold a TransOffice-t — vidd át a saját életedre.** Saját szerződéseden, saját meetingeden, saját pályázatodon."
- 🖥 **Csinálom:** Megmutatom a Tananyag mappa-szerkezetét egy utolsó alkalommal

**3:59 — Búcsú (1p)**
- 📍 **Mondom:** „Ennyi volt. **Köszönöm**. Ha kérdés van, **most az utolsó 5 percben** szóljatok. Holnap is elérhető vagyok email-en."
- 🖥 **Csinálom:** Vízzel köszöntsd magad, lélegezz egyet
- 📍 **Mondom:** „Vigyázzatok magatokra. **Találkozunk a következő szinten.**"

### Csúszás-terv ZÁRÁS-ra
- Ha 2+ perc csúszol → a visszatekintést rövidítsd 1 percre
- Ha 5+ perc csúszol → kihagyod a bónusz feladat-bemutatást (de utalsz rá email-ben)
- ⚠️ **A „1 mondat amit elviszek" körkérdést SOHA ne hagyd ki** — ez a workshop pszichológiai zárása

---

## 📎 Appendix A — Prompt library

### A.1 — F1: Mappa-áttekintés
```
Nézd át a TransOffice/ mappa teljes tartalmát. Készíts egy strukturált
összefoglalót Márton számára (1-2 oldalas), amely tartalmazza:

1. Cég alapadatok — mit csinálunk, hol, hányan vagyunk
2. Ügyfélkör — hány aktív ügyfelünk van, kik a legnagyobbak
3. Pénzügyi helyzet — árbevétel, trend
4. Jelenlegi rendszerek — hogyan működik az admin most
5. Beszállítók — kik, milyen feltételekkel
6. Azonosított problémák — inkonzisztenciák, hiányosságok
7. Javaslat — 3-5 prioritás amit a pályázatban érdemes lenne megcélozni

Ha találsz furcsát (eltérő számok, hiányzó adatok), jelöld kérdőjellel.
```

### A.2 — F1: CLAUDE.md generálás
```
Készíts egy CLAUDE.md fájlt a project-rootban, ami project memory-ként
működik majd a Cowork-nek. Tartalmazza:

- Cég neve, székhelye, méret
- Az én szerepem: Operations & Systems Manager
- A legfontosabb fájlok és mappák
- A jelenlegi fő küldetésem (AFM Mobilitate Verde pályázat)
- A kulcs-személyek (Márton, Enikő, Mihaela, Béla bácsi)

Legyen rövid, működjön session-ök között.
```

### A.3 — F2: Meeting transcript → TODO
```
Olvasd el ezt a meeting transcriptet. Ez egy sürgős megbeszélés volt
egy EU pályázatról (elektromos autó flotta, AFM Mobilitate Verde 2025).

Kérek:
1. Helyzet összefoglaló (3-5 mondat)
2. TODO lista: Ki → Mit → Mikorra → Prioritás
3. Hiányzó információk (amik nélkül nem lehet pályázni)
4. Blokkolók: melyik TODO függ a másiktól

Mentsd el a TODO-kat a feladatkezelőbe (Productivity plugin).
```

### A.4 — F2: TODO-kból emailek
```
A mentett TODO-k alapján:
1. Írj follow-up emailt Enikőnek (rövid, konkrét, az ő feladataival)
2. Írj emailt a külsős könyvelőnek románul (pénzügyi adatok kérése a pályázathoz)
3. Akcióterv: lépések a pályázat beadásáig, felelősökkel

Hangnem: professzionális de közvetlen, kis cég vagyunk.
```

### A.5 — F3: Eligibility check
```
Olvasd át a Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md
fájlt és vesd össze a TransOffice cégadatokkal (CLAUDE.md alapján).

Listázd ki az ÖSSZES eligibility kritériumot. Minden kritériumra jelöld:
✅ TELJESÍTJÜK / ⚠️ RÉSZBEN / ❌ NEM TELJESÍTJÜK
+ rövid indoklás (max 2 mondat / kritérium)

A végén egy döntés: PÁLYÁZHATUNK / NEM PÁLYÁZHATUNK / FELTÉTELESEN
+ a top 3 kockázat amit el kell intézni.
```

### A.6 — F4.1: Bérleti szerződés deep-check
```
Olvasd el a szerzodes_chirie_TransOffice_2018.docx-et alaposan.
A TransOffice mint bérlő szempontjából:

1. Listázd a top 5 kockázati pontot
2. Hasonlítsd össze a TransOffice más fájljaiból nyert kontextussal —
   keress kapcsolódó dolgokat (meeting transcript, email-ek, jegyzetek).
3. Bármilyen red flag — fontos hogy ÉSZREVEDD ha a tulajdonosi szándék
   változhat (eladás, hosszabbítás megtagadása)
4. Akcióterv: mit teszünk a pályázat előtti 7 napban
```

### A.7 — F4.2: Mihaela Excel feldolgozás
```
Itt van Mihaela visszaküldött bilanță: bilant_TransOffice_2023_2024.xlsx
Számítsd ki és mutasd be:

1. Árbevétel 2023 vs 2024 (RON-ban + %)
2. EBITDA 2023 vs 2024 (RON-ban + marzs %)
3. Alkalmazottak száma 2023 vs 2024
4. Trend értelmezése — emelkedünk vagy csökkenünk?
5. Pályázati szempontból: melyik 3 KPI a legerősebb érv?

Készíts egy strukturált jelentést a pályázathoz (max 1 oldal).
```

### A.8 — F4.3: CEO prezentáció
```
Készíts egy 5 slide-os PPTX prezentációt Mártonnak az AFM Mobilitate Verde
pályázat aktuális állásáról. Slide-onkénti felépítés:

Slide 1: Helyzet — hol állunk a Data Completion Board-on
Slide 2: Eligibility check — ✅ pályázhatunk
Slide 3: Pénzügyi készség — EBITDA 2024, trend
Slide 4: Béla bácsi (telephely) — zöld, sőt vételi opció
Slide 5: Akcióterv — a következő 7 nap

Stílus: tiszta, üzleti, magyar nyelven. Mindegyik slide tartalmazzon
1 fő számot vagy állítást + 2-3 alpontot.
```

### A.9 — F5.1: Plan de afaceri (üzleti terv)
```
Készíts egy teljes Plan de afaceri-t (románul) a TransOffice számára
az AFM Mobilitate Verde 2025 pályázathoz. Tartalmazza:

1. Rezumat executiv (1 oldal)
2. Prezentarea companiei (cégbemutató + Béla bácsi telephely)
3. Analiza pieței (B2B irodai logisztika Hargita megye)
4. Proiect propus — 5 elektromos jármű + 2 töltőpont
5. Plan financiar — 18 hónapos cash flow, EBITDA forecast 5 évre
6. Plan de marketing — hogyan kommunikáljuk a zöld átállást
7. Plan de implementare — milestone-ok M1-M18
8. Echipa managerială — Márton + Mihaela + a többi

Hossz: 25-40 oldal. Stílus: profi, román pályázati formátum.
Vedd alapul: F1 cégadatok + F4 Mihaela EBITDA + F4 Béla bácsi vételi opció.
```

### A.10 — F6.1: Modern variáns
```
Készíts egy modern, clean B2B weboldal-variánst a TransOffice számára HTML-ben.
Egyetlen fájlban (inline CSS + JS).

- Színek: kék (#1976d2), fehér, szürke árnyalatai
- Tipográfia: Inter / system-ui, modern san-serif
- Hero szekció: cég neve + 1 mondatos pozícionálás
- Szolgáltatások: 3-4 kártya icon-okkal
- Új projekt szekció: AFM elektromos járműflotta (zöld átállás)
- Csapat: Márton + Enikő bemutatása (1-1 mondat)
- Kapcsolat: cím (Székelyudvarhely), email, telefon, térkép-link

Reszponzív, mobile-friendly. Egy A4-re kinyomtatható ha kell.
```

---

## 📎 Appendix B — Q&A best practices

### Gyakori kérdések és gyors válaszok

**Q: „És ezt mindenki megveheti? Csak Claude Pro kell?"**
- A: „Igen — Claude Pro ($20/hó). A Cowork desktop alkalmazás ingyen letölthető hozzá. Plusz egy Obsidian (ingyenes)."

**Q: „És az adataim hova mennek?"**
- A: „A Cowork lokálisan dolgozik a fájljaiddal — a fájlok nem mennek fel a cloud-ra. A kérdéseid Claude-nak küldéskor mennek át, de Anthropic-nak vannak adatvédelmi szabályozásai. Részletek: anthropic.com/privacy."

**Q: „Miért nem a ChatGPT?"**
- A: „A ChatGPT remek eszköz egyedi feladatokra. De a Cowork **összerakja a kontextust**: emlékszik, file-okat kezel, plugin-eket használ. **Munkafolyamat, nem chat.**"

**Q: „Mennyit tévedhet az AI?"**
- A: „Pár %-ban. Mindig az **ember** dönt — az AI **első szempár**. A pályázatot **ne** add be ember-ellenőrzés nélkül."

**Q: „Tudja a Cowork mind a 24 nyelvet?"**
- A: „Igen, könnyedén. Magyar, román, angol — gyakran egy chatben mind a hármat váltogatva."

**Q: „És ha nem értek hozzá technikailag?"**
- A: „Pont ezért nem tool-tanulás ez. Az AI **a te szavaiddal beszél**. Ha kérdezel, ő válaszol — magyarul."

### Mit csinálj ha **NEM tudod a választ**
- 📍 „Nagyon jó kérdés — őszintén, ezt most nem tudom. **Megnézem és visszajelzek email-ben** vagy a következő alkalmunkkor."
- ⚠️ **SOHA ne találj ki választ.** A hitelesség értékesebb mint a gyors válasz.

### Mit csinálj ha valaki **akadékoskodik**
- 📍 **Tisztelet:** „Értem mit mondasz. **Mi a tapasztalatod?** Mi jött be eddig?"
- ⚠️ **NE** védd magad. **NE** vitatkozz. **Vedd komolyan**.
- Ha tényleg téves az állítás, halkan és tényszerűen javítsd: „A te tapasztalatod más volt. Az enyém ez — de kipróbálom amit te mondasz."

### Mit csinálj ha valaki **megfagyott** (nem kérdez, nem reagál)
- 📍 **Privát kapcsolat:** szünetben odamész, halkan: „Minden rendben? Hagyjak teret, vagy van kérdés?"
- ⚠️ **NE** mondj a csoport előtt: „És [Név], te mit gondolsz?" — ez ránehezíti

---

## 📎 Appendix C — Vészforgatókönyv

### Ha a Cowork **lefagy** vagy NEM válaszol
1. **Frissítsd az ablakot** (Cmd+R / Ctrl+R)
2. Ha még nem megy: **indítsd újra** a Cowork desktop-ot
3. Ha még nem megy: használd a **Claude.ai web-verziót** ugyanazzal a fiókkal (a Pro plugin-ek ott is)
4. Ha **WiFi probléma**: kapcsolj a **mobile hotspotra** (előre készítve!)
5. **Plan B**: a `Pelda_outputok/` mappa minden F3 demohoz előre legenerált választ tartalmaz

### Ha **WiFi teljesen kiszakad**
- 📍 **Mondom:** „Adott egy 10 perces előrelátható szünet — pont jó kávészünetnek. Visszajövünk amint a WiFi visszajön. Addig kérdezzetek."
- Plan B: az **előre letöltött PDF outputokat** mutatod meg (van a `Műhely/03_Dontes_Elemzes/Palyazat_kiiras_BUILD/`-ben)

### Ha **projektor meghal**
- Mindenki nyissa fel a saját laptopot, csatlakozz screen-sharinggel **Zoom / Teams** linken keresztül
- Előre legyen meg egy Zoom-link a tarsolyodban

### Ha **a csoport totál fáradt** (több mint 3 ember bólogat ülve)
- Adj egy **2 perces állva-kávé** szünetet, NEM tervezett
- 📍 „Felálltunk 2 percre. Nyújtózás, kávé."
- F6-ot **kezdd erősen** (régi oldal nagyon emelt, drámai hangon)

### Ha **valaki rosszul van**
- ⚠️ Állj le. Kérdezd: „Minden rendben?"
- Ha komoly: kérj segítséget (irodai segéd, recepció)
- Folytasd a workshopot amint biztosítva van

### Ha **idejétkorán végezel** (csúszás-mentő trükkök)
- Hagyj **plusz Q&A időt** a végén
- Mutasd be a **bónusz feladatokat** részletesebben
- Egy résztvevő **saját szituációját** dolgozd fel a Cowork-kel közösen (élő probléma-megoldás)

### Ha **csúszol és nem fér be minden**
- F3-F4 között legyen **kemény time-box**
- F6 az utolsó **vágható** fázis (de még 10 percben is hatékony)
- A ZÁRÁS „1 mondat" körkérdést **soha ne hagyd ki**

---

## 📜 Verzió-előzmények

| Verzió | Dátum | Változás |
|--------|-------|----------|
| **1.0** | 2026-05-12 | Első kiadás. 240 perces forgatókönyv, mind 6 fázis részletezve, 10 prompt library, Q&A best practices, vészforgatókönyv. A hands-on javítások (F4.3 slide újrahangolás, F5.3 te töltöd ki + spot the error, zárás "1 mondat") **beépítve** a forgatókönyvbe. |

### Tervezett v1.1 (dry-run után)
- Tényleges időmérések beillesztése (mennyit tartott TÉNYLEG)
- Új csúszás-mentő trükkök
- Új Q&A-k a tényleges kérdésekből

### Tervezett v2.0 (második workshop után)
- 2 workshop tapasztalatainak konszolidálása
- A bónusz feladatok élő-bevezetésének opciói

---

**Készítette:** Claude Cowork — Ignis Academy
**Kapcsolat:** Szabolcs · exarlabs@gmail.com
**Utolsó frissítés:** 2026-05-12
