# 🎬 Oktatói segédlet v2.0 — Ignis Academy Haladó AI Workshop

> **Verzió:** 2.1 (instructor-led + stációk modell, dátum-pivot 2026, F4 felkérő emailek)
> **Készült:** 2026-05-12 · **Frissítve:** 2026-05-14
> **Hossz:** 4 óra (240 perc) — délelőtt 9:00 → 13:00 példa
> **Csoport:** 10-15 fő (5-7 pár), HBC közösség
> **Eszközök:** Oktatói laptop + projektor, minden résztvevő saját laptopja, Claude Cowork Pro
> **Pedagógia:** Az oktató kivetítve végigviszi a narratívát és a demókat. A résztvevők **fix stációkon** dolgoznak a saját laptopjukon — izolált, 3-5 perces feladatok F1 után bárki meg tudja csinálni.
> **Tananyag-verzió:** v1.2 (2026-os pivot)

---

## 📋 Tartalomjegyzék

1. [Hogyan használd ezt a segédletet](#hogyan)
2. [Pre-workshop checklist](#pre)
3. [Idővonalas áttekintés](#ido)
4. [Bevezető (0:00 → 0:22)](#bev)
5. [F1 — Káoszból rendszer (0:22 → 0:47)](#f1)
6. [F2 — Rend a TODO-k között (0:47 → 1:12)](#f2)
7. [SZÜNET 1 (1:12 → 1:27)](#sz1)
8. [F3 — Pályázati elemzés (1:27 → 1:57)](#f3)
9. [F4 — Multi-persona kommunikáció (1:57 → 2:34)](#f4)
10. [SZÜNET 2 (2:34 → 2:44)](#sz2)
11. [F5 — Pályázat összeállítás (2:44 → 3:19)](#f5)
12. [F6 — Web redesign (3:19 → 3:37)](#f6)
13. [Zárás (3:37 → 3:50)](#zar)
14. [Appendix A — Minden prompt egy helyen](#appA)
15. [Vészforgatókönyv](#vesz)

---

## Hogyan használd ezt a segédletet  <a id="hogyan"></a>

Ez egy **élő segítség** — workshop közben pillantasz rá. **A workshop modellje:**

- 🎤 **Az oktató (te) kivetíti a laptopját** és a teljes narratívát végigviszi
- 🖥 **A résztvevők figyelnek** a kivetítőre — látják a demókat élőben
- ⏸ **Stációknál** megállsz, a résztvevők előveszik a saját laptopjukat és 3-5 percig egy izolált mini-feladatot csinálnak
- 🔄 **Visszatérünk** a kivetítőhöz, közös megbeszélés, megyünk tovább

**Jelölések a segédletben:**
- 🎤 **[OKTATÓ]** — te beszélsz / mutatod
- ⏸ **[STÁCIÓ]** — a résztvevők dolgoznak (mindenki saját laptopján)
- 💬 **[BESZÉLGETÉS]** — közös megbeszélés
- 📝 **PROMPT:** — pontos szöveg amit beírsz a Cowork-be (vagy a résztvevők)
- 📍 **MONDOM:** — pontos mondat amit te mondasz
- ⚠️ **VIGYÁZZ:** — gyakori hiba

---

## Pre-workshop checklist (T-30p)  <a id="pre"></a>

**Technikai (10 perc):**

| ☐ | Tétel |
|---|-------|
| ☐ | Projektor + laptop + WiFi működik |
| ☐ | Claude Cowork desktop megnyitva, bejelentkezve (Pro account) |
| ☐ | Productivity + Legal plugin aktiválva a Cowork-ben |
| ☐ | A **`TransOffice/`** mappa előkészítve az oktatói laptopon (referencia példányként) |
| ☐ | A **résztvevők TransOffice-ai** előkészítve (USB-stick / GDrive link kéznél) |
| ☐ | Mobil hotspot bekapcsolva (vész esetére) |

**Asseteket előkészíteni (10 perc):**

| ☐ | Tétel |
|---|-------|
| ☐ | `Feladat_1.1.md` előre megnyitva egy böngésző-tabban (a tanulók látják a copy-paste promptot) |
| ☐ | `meeting_transcript_20260825.srt` letöltve a saját gépedre |
| ☐ | `Ghidul-solicitantului-Mobilitate-Verde-IMM-2026.md` letöltve |
| ☐ | `szerzodes_chirie_TransOffice_2018.docx` letöltve |
| ☐ | `bilant_TransOffice_2024_2025.xlsx` letöltve |
| ☐ | `formular_depunere_AFM_Mobilitate_Verde.html` browser tab nyitva |
| ☐ | `transoffice_old_website.html` browser tab nyitva |

**Mentális (10 perc):**

| ☐ | Tétel |
|---|-------|
| ☐ | Olvasd át a Story Book-ot egyszer |
| ☐ | Ellenőrizd a 2 szünet időpontját — írd táblára (pl. 10:35 és 11:42) |
| ☐ | Készíts pohár vizet |
| ☐ | 1 perc csendes lélegzés |

---

## Idővonalas áttekintés  <a id="ido"></a>

| Idő | Szegmens | Hossz | Stációk |
|---|---|---|---|
| 0:00 → 0:22 | **Bevezető** | 22p | 1 micro-bemutatkozás |
| 0:22 → 0:47 | **F1 — Káoszból rendszer** | 25p | **MINDENKI** (kivétel) |
| 0:47 → 1:12 | **F2 — TODO-k** | 25p | 1 stáció (Follow-up email) |
| 1:12 → 1:27 | ☕ **SZÜNET 1** | 15p | — |
| 1:27 → 1:57 | **F3 — Pályázati elemzés** | 30p | 2 stáció (1 kritérium + 1 melléklet) |
| 1:57 → 2:34 | **F4 — Multi-persona** | 37p | 2 stáció (Béla bácsi válasz + EBITDA) |
| 2:34 → 2:44 | ☕ **SZÜNET 2** | 10p | — |
| 2:44 → 3:19 | **F5 — Pályázat összeáll.** | 35p | 2 stáció (Form-katalog + Idő-becslés) |
| 3:19 → 3:37 | **F6 — Web redesign** | 18p | 1 nagy stáció (3 saját variáns) |
| 3:37 → 3:50 | **Zárás** | 13p | Anonim „1 mondat" |

**Példa óratervezéssel:** 9:00 → 13:00, szünetek: 10:12 és 11:34.

---

## 🎬 BEVEZETŐ (0:00 → 0:22)  <a id="bev"></a>

**Cél:** Mindenki helyén legyen, megismerjék a kerettet, megérezzék a stake-eket.

| Idő | Mód | Mit |
|---|---|---|
| 0:00-0:03 | 🎤 OKTATÓ | Üdvözlés |
| 0:03-0:07 | ⏸ STÁCIÓ | „1 dolog amit várok" mini-bemutatkozás |
| 0:07-0:13 | 🎤 OKTATÓ | Workshop ív + film-metafora |
| 0:13-0:18 | 🎤 OKTATÓ | TransOffice + Márton + pisztolymisszió |
| 0:18-0:22 | 🎤 OKTATÓ | Szabályok + idő-jelölés |

### 0:00-0:03 — Üdvözlés

📍 **MONDOM:** *„Sziasztok! Köszönöm hogy itt vagytok. 4 óra alatt egy fiktív céget fogunk a káoszból kihúzni — beadunk vele egy 200 000 eurós EU-pályázatot. És megérzitek mit jelent ha az AI mellettetek dolgozik."*

⚠️ **VIGYÁZZ:** Ne mondd hogy „megtanítom" — mondd hogy „megtapasztaljátok". Ez nem tool-tanulás.

### 0:03-0:07 — ⏸ STÁCIÓ: „1 dolog amit várok"

📍 **MONDOM:** *„Egy gyors kör. Mindenki 1 mondatban: ki vagy, mivel foglalkozol, és **1 dolog amit ma várok az AI-tól**. Csak 1 mondat — nem előadás."*

🖥 **CSINÁLOM:** Körbejárok, kb. 4 perc 12-15 főre.

⚠️ **VIGYÁZZ:** A „1 dolog amit várok" **pozitív** — nem hierarchikus mint a „hány %-ban használod". Egy kezdő is biztonságban szólalhat meg.

### 0:07-0:13 — Workshop ív

📍 **MONDOM:** *„A workshop egy film. Ti vagytok az új Operations Manager a TransOffice-nél. 4 óra alatt végigvisszük a céget a káoszból a beadott pályázatig. 6 felvonás — F1-F6. Mindegyik 20-35 perces. A film közben:*
- *Én végigviszem a narratívát a saját gépemen, kivetítve. Megmutatok valamit.*
- *Stációknál megálljatok. Előveszitek a saját laptopjaitokat, kipróbáljátok ti is — 3-5 perc.*
- *Aztán visszatérünk."*

🖥 **CSINÁLOM:** Mutatom a 6 fázis listáját az Obsidian-ban / a kivetítőn.

### 0:13-0:18 — TransOffice bemutatása

🖥 **CSINÁLOM:** Megnyitom a `Ceg_leiras_TransOffice.md`-t **csak a fő képet** — nem olvasok fel.

📍 **MONDOM:** *„TransOffice Trade SRL. Székelyudvarhely. 22 éves cég, irodai eszközök B2B. Az anyu kezelte az admint 20 évig. Most a fia (Kovács Márton) átvette — és a fia tudja: az anyu fejében volt minden. Excel-dzsungel, email-káosz. Ti vagytok az új ember, aki rendet rak."*

📍 **MONDOM:** *„És van egy kemény határidő: az AFM Mobilitate Verde pályázat. 200 000 euró elektromos járműflottára. **Péntekig** be kell adni vagy lemarad. **Egy hét, egy ember, egy káosz, egy AI.**"*

⚠️ **VIGYÁZZ:** **Tömör maradj** — 5 perc, nem 10. A részletek F1-ben jönnek elő.

### 0:18-0:22 — Szabályok

📍 **MONDOM:** *„Két szabály. Egy: kérdezz bátran, bármikor. Két: ha lassú vagyok vagy túl gyors, szóljatok. Két szünet lesz: kb. [10:12] és kb. [11:34]. Most kezdjük!"*

---

## 🎬 F1 — Káoszból rendszer (0:22 → 0:47, 25 perc)  <a id="f1"></a>

**Cél:** Mindenki saját TransOffice-án ugyanazt a promptot futtatja → saját rendezett mappa, saját CLAUDE.md, saját kivonat.
**Modell:** **Kivétel — ez az egyetlen fázis ahol mindenki egyszerre dolgozik a saját laptopján.**

| Idő | Mód | Mit |
|---|---|---|
| 0:22-0:25 | 🎤 OKTATÓ | Felvezetés + a Feladat_1.1 megnyitása |
| 0:25-0:27 | 🎤 OKTATÓ | Cowork-projekt setup demó |
| 0:27-0:42 | ⏸ STÁCIÓ | Mindenki copy-paste a promptot, Cowork dolgozik |
| 0:42-0:45 | 💬 BESZÉLGETÉS | Páros megbeszélés |
| 0:45-0:47 | 🎤 OKTATÓ | Átkötés F2-be |

### 0:22-0:25 — Felvezetés

🖥 **CSINÁLOM:** Megnyitom a `Tananyag/01_Ceg_megertes/Feladat_1.1.md`-t a kivetítőn. Mindenki lássa.

📍 **MONDOM:** *„Olvassuk el együtt a szituációt. Márton odajön a második kávéval..."* — felolvasom a Márton-monológot.

📍 **MONDOM:** *„Mindenki nyissa ki a saját laptopján a Cowork-öt és a `Feladat_1.1.md`-t. A 3. lépésnél van egy szürke kódblokk — ez a prompt. Ezt fogjátok bemásolni a Cowork-be. Mind a 15-en. Egyszerre."*

### 0:25-0:27 — Cowork-projekt setup

🖥 **CSINÁLOM:** Megmutatom a kivetítőn:
1. Új Cowork-projekt
2. `TransOffice/` mappa hozzáadása projekt-kontextusként
3. Üres chat-tab

📍 **MONDOM:** *„Mindenki itt áll a saját gépén? Ki ne tudja még megnyitni?"* — várok 30 mp-et.

### 0:27-0:42 — ⏸ STÁCIÓ (15 perc): „Mindenki rendet tesz"

📍 **MONDOM:** *„Másoljátok ki a promptot a Feladat_1.1.md 3. lépéséből, illeszétek a Cowork chat-be, és nyomjátok el. **Csak figyeljétek hogy mit csinál.** Ha készen van, nézzétek át az outputot."*

📝 **PROMPT (amit ők másolnak):**
```
Az új munkatárs vagyok a TransOffice cégnél, ma az első napom.

A TransOffice mappában találod a cégünk összes dokumentumát. Rendetlenség
van — évek alatt gyűlt össze mindenféle dokumentum, és senki nem nézte át
őket.

Légy szíves, segíts rendbe tenni:

1. Először a jelenlegi mappáról készíts egy biztonsági másolatot, hogy
   bármikor vissza tudjam keresni a fileokat.

2. Kezd el egyenként átnézni a fileokat és kategorizálni.

3. Legyen egy Kuka mappa is — abba másolj minden olyan filet, ami szemét,
   elavult, vagy nem releváns.

4. Gyere egy javaslattal, hogy hogyan rendezzük az anyagot, és rendezd is
   el úgy.

5. Készíts nekem egy kivonatot arról, mit találtál és mit csináltál.

Készíts egy CLAUDE.md fájlt is — ez lesz a hosszútávú memóriád. Minden új
munkamenetben elsőként ezt fogod elolvasni.

Ha bármi nem világos, kérdezz vissza.
```

🖥 **CSINÁLOM közben:** Én is futtatom a saját gépemen — kivetítve. A résztvevők látják mit csinál a Cowork (kivetítő = referencia).

⚠️ **VIGYÁZZ:** Egyiküknek **biztosan nem fog elindulni** valami (rossz mappa, nincs projekt, lassú net). Légy türelmes, segíts. Ne hagyd, hogy lemaradjon.

### 0:42-0:45 — 💬 Páros megbeszélés (3 perc)

📍 **MONDOM:** *„Páronként mutassátok meg egymásnak:*
- *Mit dobott a Kukába a Cowork? Egyezett a 2 listátok?*
- *A CLAUDE.md-be ki került be a csapatba és kit hagyott ki?*
- *Mit írna át máshogy?"*

🖥 **CSINÁLOM:** Körbejárok. Hallom mit beszélnek. **Ne avatkozz be, hagyd őket.**

### 0:45-0:47 — Átkötés F2-be

📍 **MONDOM:** *„Oké, a fájlok rendben. **Mindenkinek van egy CLAUDE.md-je** — ezt mostantól F6-ig használjuk. De Márton közben besüllyed egy sürgős meetingre Enikővel. Itt jön az F2."*

---

## 🎬 F2 — Rend a TODO-k között (0:47 → 1:12, 25 perc)  <a id="f2"></a>

**Cél:** A Productivity plugin bemutatása. Egy SRT-transcript → TODO lista, ami **session-ök között is megmarad**.
**Stáció:** 1 db (Follow-up email Enikőnek a látott TODO lista alapján).

| Idő | Mód | Mit |
|---|---|---|
| 0:47-0:50 | 🎤 OKTATÓ | Átvezetés + Productivity plugin bemutatás |
| 0:50-0:58 | 🎤 OKTATÓ | DEMO: SRT-transcript → TODO (Productivity plugin) |
| 0:58-1:01 | 🎤 OKTATÓ | „Session-ök közötti memória" mágia (új chat) |
| 1:01-1:08 | ⏸ STÁCIÓ | Follow-up email Enikőnek |
| 1:08-1:10 | 💬 BESZÉLGETÉS | „Kinek mit írt a Cowork?" |
| 1:10-1:12 | 🎤 OKTATÓ | Átkötés F3-ba |

### 0:47-0:50 — Átvezetés

📍 **MONDOM:** *„Másnap reggel. Márton odaszól Enikőnek: '15 perc múlva irodában, sürgős.' A meeting kaotikus — kiderül, hogy ez a pályázat 2 hónapja a radarjuk alatt van, és **a forrás kifut**. Valaki felvette a meetinget — ez egy SRT transcript fájl, mintha egy AI transcribe-olta volna."*

📍 **MONDOM:** *„A Cowork-nek van egy **Productivity plugin**-ja, ami **nem ChatGPT**. A ChatGPT elfelejti amit mondtál. A Cowork **megjegyzi a TODO-kat session-ök között**."*

### 0:50-0:58 — DEMO: SRT-transcript → TODO

🖥 **CSINÁLOM:** A Cowork-be behúzom a `meeting_transcript_20260825.srt` fájlt. Új chat-tab.

📝 **PROMPT (én írom be):**
```
Olvasd el ezt a meeting transcriptet. Sürgős megbeszélés egy EU pályázatról
(AFM Mobilitate Verde 2026 — elektromos járműflotta).

Kérek:
1. Helyzet összefoglaló (3-5 mondat)
2. TODO lista: Ki → Mit → Mikorra → Prioritás
3. Hiányzó információk (amik nélkül nem lehet pályázni)
4. Blokkolók: melyik TODO függ a másiktól

A TODO-kat mentsd el a Productivity pluginbe.
```

📍 **MONDOM közben:** *„Nézzétek — a Cowork olvas. Strukturál. A 'kedd' szóból dátumot készít. A 'Béla bácsi szilveszteri megjegyzéséből' TODO-t csinál — pedig az csak egy mellékmondat volt. Ezt **kézzel** egy ember **fél órán** át írná át jegyzetből."*

🖥 **CSINÁLOM:** Mutatom a Productivity plugin tab-ot — látszanak az elmentett TODO-k.

⚠️ **VIGYÁZZ:** Ha a Béla bácsi-szál említve van a TODO-listán, **NE húzd alá** itt. Most még nem foglalkozunk vele. Az F4-ben jön a csúcs.

### 0:58-1:01 — „Session-ök közötti memória" (3 perc)

📍 **MONDOM:** *„És most a varázslat. Bezárom ezt a chatet. Új sessiont nyitok. **Egy üreset.**"*

🖥 **CSINÁLOM:** Új chat-tab.

📝 **PROMPT (én írom be):**
```
Mik a nyitott feladataim?
```

📍 **MONDOM:** *„És nézzétek — emlékszik. A ChatGPT-vel ez nem így megy. **Csendes pillanat.** Ez **a Cowork erőssége**."*

⚠️ **VIGYÁZZ:** **Hagyj rá 5-10 másodperc csendet.** Hadd lássák. Ne magyarázd túl.

### 1:01-1:08 — ⏸ STÁCIÓ 2.A: Follow-up email Enikőnek (7 perc)

📍 **MONDOM:** *„Most ti következtek. A TODO lista ott van — a kivetítőn látjátok, és a saját Cowork-jeiteken **a CLAUDE.md-ben** is van valami arról hogy mire pályázunk. Mindenki nyissa meg a saját Cowork-jét, új chat-tab. Másoljátok be ezt a promptot."*

📝 **PROMPT (ők másolják):**
```
Olvasd el a CLAUDE.md-t. Ez alapján és a workshop-vezetőtől látott TODO
lista alapján: írj egy 4-5 mondatos follow-up emailt Enikőnek arról,
hogy mik a feladatai a következő 3 napban az AFM pályázat előkészítésében.

Hangnem: kollegális, konkrét, határidős.

Magyarul írd.
```

🖥 **CSINÁLOM:** Körbejárok. Pár perc múlva: *„Ha kész vagy, mutasd meg a párodnak."*

⚠️ **VIGYÁZZ:** Egyiknek-másiknak más TODO lehet (mindenki saját CLAUDE.md-jétől függ). Ez **normális** — a workshop ezt **dicséri**, nem hibáztatja.

### 1:08-1:10 — 💬 Páros megbeszélés (2 perc)

📍 **MONDOM:** *„30 másodperc — mutasd meg a párodnak. Kinek hangzik élesebbnek? Mit emelne ki?"*

### 1:10-1:12 — Átkötés F3-ba

📍 **MONDOM:** *„A TODO-k megvannak, a levelek kész. De most jön az első kemény akadály: **a 94 oldalas pályázati kiírás**. Senki nem olvasta végig. **Pályázhatunk-e egyáltalán?** Erre 30 perc múlva válaszolunk."*

📍 **MONDOM:** *„De előtte — szünet. 15 perc. Találkozunk [10:27]-kor."*

---

## ☕ SZÜNET 1 (1:12 → 1:27, 15 perc)  <a id="sz1"></a>

### Mit csinálsz a szünet alatt
1. **Frissítsd a Cowork-öt** (memória-felszabadítás)
2. **Vizet igyál**
3. **Készítsd elő az F3 promptot** (Appendix A.3) — legyen kéznél copy-paste
4. **Töltsd az aksit**
5. **Ne dolgozz** — a résztvevők kérdeznek szünetben

### Visszaindítás (1:27)

📍 **MONDOM:** *„Visszajöttünk. Most a 94 oldalas pályázati kiírás. Készen álltok?"*

---

## 🎬 F3 — Pályázati elemzés (1:27 → 1:57, 30 perc)  <a id="f3"></a>

**Cél:** A 94 oldalas pályázati kiírás → strukturált eligibility tábla + gap analízis + Data Completion Board.
**Stációk:** 2 db (1 kritérium ellenőrzése + 1 melléklet beszerzési útja).

| Idő | Mód | Mit |
|---|---|---|
| 1:27-1:30 | 🎤 OKTATÓ | „És itt a 94 oldal" |
| 1:30-1:40 | 🎤 OKTATÓ | F3.1 DEMO: Eligibility check |
| 1:40-1:43 | ⏸ STÁCIÓ | 1 kritérium ellenőrzése |
| 1:43-1:51 | 🎤 OKTATÓ | F3.2 DEMO: Gap analízis (17 melléklet) |
| 1:51-1:54 | ⏸ STÁCIÓ | 1 melléklet beszerzési útja |
| 1:54-1:57 | 🎤 OKTATÓ | F3.3 DEMO: Data Completion Board + átkötés |

### 1:27-1:30 — Felvezetés

🖥 **CSINÁLOM:** Megnyitom a `Ghidul-solicitantului-Mobilitate-Verde-IMM-2026.pdf` borítóját — gyorsan görgetek, lássák hogy **valódi 94 oldalas dokumentum**.

📍 **MONDOM:** *„Ez egy 94 oldalas, románul írt, jogszabály-stílusú pályázati kiírás. Egy ember **2-3 nap alatt** olvassa át. A Cowork-kel **5 perc múlva eldöntjük, pályázhatunk-e**. Nem csak igen/nem — strukturáltan, indoklással, kockázatokkal."*

### 1:30-1:40 — F3.1 DEMO: Eligibility check (10 perc)

🖥 **CSINÁLOM:** A pályázati kiírás MD verzióját behúzom a Cowork-be projekt-kontextusként.

📝 **PROMPT (én írom be):**
```
Olvasd át a Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-
2025.md fájlt és vesd össze a TransOffice cégadatokkal (a CLAUDE.md
alapján).

Listázd ki az ÖSSZES eligibility kritériumot. Minden kritériumra jelöld:
✅ TELJESÍTJÜK / ⚠️ RÉSZBEN / ❌ NEM TELJESÍTJÜK
+ rövid indoklás (max 2 mondat / kritérium)

A végén egy döntés: PÁLYÁZHATUNK / NEM PÁLYÁZHATUNK / FELTÉTELESEN
+ a top 3 kockázat amit el kell intézni.
```

📍 **MONDOM közben:** *„A Cowork most **párhuzamosan olvas két dolgot**: a pályázati kiírást és a TransOffice cégadatokat. **Egy tanácsadó ezt 3 napig csinálná. Egy tanácsadó óradíja 100 EUR/óra. Ez most 3000 EUR-os tanács — ingyen."*

🖥 **CSINÁLOM:** Várok 60-90 mp. Megjelenik a kimenet. Mutatom: 12 kritérium, 10 ✅, 2 ⚠️. **Kiemelek 2-3 érdekes pontot.**

### 1:40-1:43 — ⏸ STÁCIÓ 3.A: 1 kritérium ellenőrzése (3 perc)

📍 **MONDOM:** *„Most ti következtek. Mindenki saját Cowork-jén — másoljátok be ezt:"*

📝 **PROMPT (ők másolják):**
```
Olvasd el a Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-
2025.md-ben a CR-08 (járműflotta) kritériumot. A TransOffice teljesíti-e?
Részletesen, indoklással. Maximum 5 mondat.
```

🖥 **CSINÁLOM:** Körbejárok, ha valaki más kritériumot szeretne, hagyom.

### 1:43-1:51 — F3.2 DEMO: Gap analízis (8 perc)

📝 **PROMPT (én írom be):**
```
Most listázd ki a 17 kötelező mellékletet a pályázathoz. Minden
mellékletre jelöld a TransOffice cégadatok (CLAUDE.md + TransOffice/
mappa) alapján: VAN / NINCS / RÉSZBEN. Ahol RÉSZBEN vagy NINCS, írd
oda kitől kell beszerezni és milyen formátumban.
```

🖥 **CSINÁLOM:** Mutatom a 17 soros táblát. **Kiemelek 3-4 piros tételt.**

📍 **MONDOM:** *„Látjátok — 17 dokumentum. 6 piros, 5 sárga, 6 zöld. **Ez az F4-es stáció lista**: itt fogjuk megszerezni a pirosakat."*

### 1:51-1:54 — ⏸ STÁCIÓ 3.B: 1 melléklet beszerzési útja (3 perc)

📝 **PROMPT (ők másolják):**
```
Az M-11 (járműflotta-leltár) mellékletet hogyan állítanám össze?
Kitől kapok adatot, milyen formátumban, hány napos a folyamat?
Maximum 6 mondat.
```

### 1:54-1:57 — F3.3 DEMO: Data Completion Board (3 perc)

📝 **PROMPT (én írom be):**
```
Az eligibility + gap analízisből generálj Data Completion Board-ot:
oszlopok = Tétel, Felelős, Határidő, Forrás, Státusz. Csoportosítsd
3 fázis szerint: BEADÁS ELŐTT / ELBÍRÁLÁS ALATT / MEGVALÓSÍTÁS ALATT.
```

🖥 **CSINÁLOM:** Mutatom a táblát.

### 🔍 A 2 piros pont kiemelése — iteráció + vizualizáció

A Cowork outputja itt valószínűleg **hosszú** (~50 tétel, 3 oszlopban). A résztvevőknek vizuálisan **össze kell pontosítani** a 2 fő blocker-re. Két lépés:

**1) Iteráció — egy plusz kérdés a Cowork-höz** (NEM súgás, csak absztrakció):

📝 **PROMPT (én írom be):**
```
A Data Completion Board alapján foglald össze 3 mondatban:
mi a top 2-3 P0 blocker amit a beadás előtt feltétlenül meg kell oldani?
```

→ A Cowork **maga** absztrahálja: 🔴 telephely + 🔴 pénzügy (+ esetleg jármű-leltár).

**2) Vizualizáció** — a kivetítőn **odamutatok** vagy **kijelölöm** a 2 piros tételt a Data Completion Board-on. A résztvevők **látják** vizuálisan a 2 piros pontot.

📍 **MONDOM:** *„Látjátok itt — 🔴 **Béla bácsi telephely**. És itt — 🔴 **Mihaela pénzügyi adatok**. **A többi 12 tétel rendben lesz.** Ez a 2 az amit F4-ben **két emaillel** megoldunk. Egy magyar, egy román."*

⚠️ **VIGYÁZZ:** Ha 3. blocker is kibukik (pl. jármű-leltár) — **ne hangsúlyozd** itt. Tedd félre: *„Van egy harmadik is, azt később elintézzük."* A 3. piros pont a bónusz feladat anyaga.

📍 **MONDOM (átkötés F4-be):** *„**Ez a táblát egy tanácsadó 3000 EUR-ért adja. 5 perc, ingyen.** Most jön a neheze: két emailt írunk. **F4 következik.**"*

---

## 🎬 F4 — Multi-persona kommunikáció (1:57 → 2:34, 37 perc)  <a id="f4"></a>

**Cél:** A 2 piros pont megoldása **2 Cowork-eszközzel** (Legal plugin + Excel-elemzés) és **2 felkérő emaillel**. A tanulók mindkét emailt **saját Cowork-jén** írják meg, az oktató bemutatja a 2 Cowork-eszközt + a záró CEO PPT-t.
**Stációk:** 2 db (Béla bácsi magyarul + Mihaela románul) · **DEMO-k:** 2 fő (Legal + Excel) + 1 záró (CEO PPT).

**Modell:** 2 fő Cowork-eszköz (Legal plugin + Excel-elemzés) köré szervezve, a 2 felkérő email pillérei + záró CEO PPT látványosság.

| Idő | Mód | Mit |
|---|---|---|
| 1:57-2:00 | 🎤 OKTATÓ | Átvezetés: „3 ember, **2 piros pont, 2 Cowork-eszköz**" |
| 2:00-2:08 | 🎤 **PONT 1** — OKTATÓ | **Legal plugin DEMO**: bérleti szerződés deep-check → 2028 lejárat vs 5 év követelmény → Béla bácsi cross-doc red flag |
| 2:08-2:13 | ⏸ STÁCIÓ 4.A | Felkérő email **Béla bácsinak** (magyarul) |
| 2:13-2:15 | 🎤 OKTATÓ | A válasz beérkezik (rövid bemutatás) |
| 2:15-2:20 | ⏸ STÁCIÓ 4.B | Felkérő email **Mihaelának** (románul) |
| 2:20-2:28 | 🎤 **PONT 2** — OKTATÓ | **Excel-elemzés DEMO**: Mihaela válasza + bilanc 2024+2025 + EBITDA + KPI trend |
| 2:28-2:34 | 🎤 ZÁRÁS — OKTATÓ | **CEO update PPT** generálás (látványos záró WOW) |

### 1:57-2:00 — Átvezetés

📍 **MONDOM:** *„A Data Completion Board kész — 14 feladat, 8 felelős. **2 piros pont van**: a telephely-stabilitás (Béla bácsi) és a pénzügyi adatok (Mihaela). **2 piros pont — 2 Cowork-eszköz — 2 email.** A Legal plugin felfedezi az elsőt, az Excel-elemzés lezárja a másodikat. Ti írjátok meg a két emailt. **Egy magyar, egy román.** A végén Márton megkapja az 5 slide-os PPT-t."*

### 2:00-2:05 — F4.1 DEMO: Bérleti szerződés deep-check + Béla bácsi cross-doc (5 perc) ← **A WOW PILLANAT**

🖥 **CSINÁLOM:** Behúzom a `szerzodes_chirie_TransOffice_2018.docx`-et a Cowork-be.

📝 **PROMPT (én írom be):**
```
Olvasd el a szerzodes_chirie_TransOffice_2018.docx-et. A TransOffice
mint bérlő szempontjából:

1. Listázd a top 5 kockázati pontot
2. Hasonlítsd össze a TransOffice mappájában lévő MÁS fájlokkal —
   keress kapcsolódó információt (meeting transcript, emailek,
   jegyzetek). Bármilyen red flag fontos.
3. A pályázat (AFM Mobilitate Verde 2026, beadás 2026-08-31) 5 év
   telephely-stabilitást és töltőpont-engedélyt követel — teljesítjük?
```

📍 **MONDOM közben:** *„Figyeljétek: a Cowork most NEM CSAK ezt a szerződést olvassa. Visszanéz a többi fájlra is — meeting transcript, emailek..."*

🖥 **CSINÁLOM:** Várok 60-90 mp. Megjelenik a kimenet.

📍 **MONDOM (lassan, drámaian):** *„**Itt egy fontos dolog.** A Cowork talált valamit. Visszanézte a meeting transcriptet — emlékeztek a 6. jelenetre? Béla bácsi szilveszterkor megemlítette hogy szeretné eladni az egyik területét. **Lehet hogy a miénk lesz a következő.** Ez egy red flag a pályázathoz."*

📍 **MONDOM:** *„És nézzétek a másik bajt: a szerződés 2028-ig megy → 2026-ban beadva csak **~2 év marad**. A pályázat **5 év stabilitást követel** + a tulajdonosnak **írásban kell engedélyt adnia a töltőpontra**. Két kérdés, egy ember. **Levelet írunk Béla bácsinak.**"*

### 2:05-2:10 — ⏸ STÁCIÓ 4.A: Felkérő email Béla bácsinak (5 perc)

📍 **MONDOM:** *„Most ti következtek. Mindenki saját Cowork-jén — másoljátok be ezt:"*

📝 **PROMPT (ők másolják):**
```
Írj egy emailt Béla bácsi (a telephely-tulajdonos, 70 éves családi ismerős)
számára Márton nevében. A helyzet:

- A jelenlegi bérleti szerződésünk 2028-ig megy
- Egy EU pályázathoz (AFM Mobilitate Verde 2026, elektromos járműflotta)
  a telephely-bérletnek 2026-08-31-től számítva legalább 5 évig kell
  érvényesnek lennie — tehát 2031-08-31-ig
- Plusz: a tulajdonosnak írásban (acord scris) kell engedélyt adnia a
  töltőállomás telepítésére

Két dolgot kérjünk tőle az emailben:
1. act adițional a szerződés meghosszabbítására (min. 2031-ig, ideálisan
   tovább)
2. acord scris a töltőpont telepítésére

Hangnem: tisztelettudó, közvetlen, magyaros — Béla bácsi régi ismerős, 70 éves.
Max 8 mondat. Magyarul írd.
```

🖥 **CSINÁLOM:** Körbejárok. *„Tetszik, ahogy Tibi fogalmazta!"* — pozitív megerősítés. **Senkit ne hagyj le.**

### 2:10-2:13 — F4.1 DEMO: Béla bácsi válasza (3 perc)

📍 **MONDOM:** *„Tegyük fel hogy mindenki Cowork-jéből egy email elment. **Most lássuk a választ.**"*

🖥 **CSINÁLOM:** Megnyitom a `emails/bela_bacsi_valasz/email.md`-t a kivetítőn — felolvasok belőle:

> *„Szia Márton, Nyugi, a Băieșenilor-t nem adom el, az családi. Amit mondtam szilveszterkor az a Sub Cetate-i föld, ahhoz nincs közötök. Ha kell a pályázathoz, meghosszabbítjuk a szerződést 2035-ig, nekem jó. Közjegyzői papírt is aláírok ha az kell..."*

📍 **MONDOM:** *„**Mindkét piros pont megoldva.** 5 év? Nem, **9 év** (2035-ig)! Acord scris? Igen, közjegyzőileg! És **vételi opció** is — Béla bácsi említette hogy csak nekünk adja el ha eladna. **Bonus.**"*

🖥 **CSINÁLOM:** Visszatérek a saját Cowork-emhez, rögzítem a DCB-t:

📝 **PROMPT (én írom be):**
```
Béla bácsi visszaválaszolt: 2035-ig meghosszabbítja a szerződést +
közjegyzőileg + vételi opció. Frissítsd a Data Completion Board-ot:
a 'telephely-stabilitás' státusza most ✅ ZÖLD. Bővítsd a megjegyzéssel:
„vételi opció további lépés F5-ben."
```

### 2:13-2:18 — ⏸ STÁCIÓ 4.B: Felkérő email Mihaelának (románul) (5 perc)

📍 **MONDOM:** *„Második piros pont: a pénzügyi adatok. Az utolsó 2 lezárt év (2024+2025) bilancot kell. **Nálunk nincs** — Mihaela külsős könyvelőnél van. **Mihaelának románul írunk.** Másoljátok be:"*

📝 **PROMPT (ők másolják):**
```
Írj egy emailt Mihaela Ionescu-nak (mihaela.ionescu@contabilpro.ro,
a TransOffice külsős könyvelője) Márton nevében. A helyzet:

- Pályázunk az AFM Mobilitate Verde 2026 programra (elektromos járműflotta)
- Beadási határidő: 2026-08-31, ora 16:00 — ~1 hét van vissza
- A pályázat előírja: az utolsó 2 lezárt pénzügyi év mérlege és pénzügyi
  helyzete (bilanț + cont de profit și pierdere + EBITDA + alkalmazotti
  létszám) — tehát 2024 és 2025
- Mihaela a könyvelő, ezek az adatok nála vannak

Kérjük meg Mihaelát hogy:
- Küldje át a 2024 és 2025 bilanț + cont de profit și pierdere kivonatot
- Mellékeljen 1 sor EBITDA-t és az alkalmazotti létszámot (FTE)
- Határidő: 3 napon belül (a pályázati beadáshoz időben kelljen
  fel tudjuk dolgozni)

Hangnem: románul, professzionális de közvetlen — Mihaela 45 éves,
részmunkaidős, precíz. Max 8 mondat.
```

🖥 **CSINÁLOM:** Körbejárok. **Az erdélyiek számára** ez a kétnyelvű váltás **kifejezetten értékes** pillanat — magyar Béla bácsinak, román Mihaelának, **ugyanaz a Cowork**, **5 perc különbség**.

### 2:18-2:24 — F4.2 DEMO: Mihaela válasza + Excel-elemzés (6 perc)

📍 **MONDOM:** *„Mihaela 2 nappal később visszaválaszolt. Itt az email — és a melléklet."*

🖥 **CSINÁLOM:** Megnyitom a `emails/mihaela_konyvelo_valasz/email.md`-t.

> *„Épp Görögbe indultam a családdal, de gyorsan összedobtam a számokat. Csatolom az Excelt, benne van minden: bilanț, eredménykimutatás, EBITDA, létszám..."*

🖥 **CSINÁLOM:** Behúzom a `bilant_TransOffice_2024_2025.xlsx`-et a Cowork-be.

📝 **PROMPT (én írom be):**
```
Itt van Mihaela visszaküldött bilance-Excelje (2024+2025).
Számítsd ki és mutasd be:

1. Árbevétel 2024 vs 2025 (RON-ban + %)
2. EBITDA 2024 vs 2025 (RON-ban + marzs %)
3. Alkalmazottak száma 2024 vs 2025
4. Trend értelmezése — emelkedünk vagy csökkenünk?
5. Pályázati szempontból: melyik 3 KPI a legerősebb érv?

És az utolsó: az EBITDA margin 2025-re — pontos százalék.
```

🖥 **CSINÁLOM:** Várok 30-60 mp. Mutatom a strukturált jelentést.

📍 **MONDOM:** *„**Mindkét piros pont megoldva.** Pénzügyi stabilitás: ✅, telephely: ✅. **Most jöhet Márton.**"*

### 2:24-2:34 — F4.3 DEMO: CEO update PPT (10 perc)

📍 **MONDOM:** *„Márton 11-kor visszajön az ügyfél-meetingről. **8 perc múlva** prezentációt akar. Cowork-kel: 5 perc."*

📝 **PROMPT (én írom be):**
```
Készíts egy 5 slide-os PPTX prezentációt Mártonnak az AFM Mobilitate
Verde 2026 pályázat aktuális állásáról. Slide-onkénti felépítés:

Slide 1: Helyzet — hol állunk a Data Completion Board-on
Slide 2: Eligibility check — ✅ pályázhatunk
Slide 3: Pénzügyi készség — EBITDA 2025 marzs, trend 2024→2025
Slide 4: Béla bácsi (telephely) — zöld (2035-ig), sőt vételi opció
Slide 5: Akcióterv — a következő 7 nap a beadásig

Stílus: tiszta, üzleti, magyar nyelven.
```

🖥 **CSINÁLOM:** Várok 1-2 perc. Megnyitom a kész .pptx-et. Slide-ról slide-ra mutatom.

📍 **MONDOM:** *„**Letölthető, prezentálható.** Holnap reggel Mártonnal. **És nézzétek — ez a 4 órás munka outputja eddig**: rendezett mappa (F1), TODO-k (F2), pályázat-elemzés (F3), és most **3 dokumentum** (2 email + 1 PPT) — minden az előző fázisok kontextusából."*

📍 **MONDOM:** *„Itt a szünet. 10 perc."*

---

## ☕ SZÜNET 2 (2:34 → 2:44, 10 perc)  <a id="sz2"></a>

### Mit csinálsz
1. Idd meg a kávét
2. **Készítsd elő a Plan de afaceri promptot** (Appendix A.5)
3. **Nyisd meg a `formular_depunere_AFM_Mobilitate_Verde.html`-t** egy fülön
4. Ellenőrizd a Cowork-öt — frissítsd ha lassú

### Visszaindítás

📍 **MONDOM:** *„Visszajöttünk. Most jön a WOW. **A pályázat össze fog állni.**"*

---

## 🎬 F5 — Pályázat összeállítás (2:44 → 3:19, 35 perc)  <a id="f5"></a>

**Cél:** Vizuális csúcspont. A teljes Plan de afaceri + 23 tételes csomag + form-kitöltés.
**Stációk:** 2 db (Form-katalogizáló + Manuális idő-becslés) — együtt drámailag mutatják a Cowork ROI-ját.

| Idő | Mód | Mit |
|---|---|---|
| 2:44-2:46 | 🎤 OKTATÓ | „Most jön a WOW" |
| 2:46-2:58 | 🎤 OKTATÓ | F5.1 DEMO: Plan de afaceri |
| 2:58-3:05 | 🎤 OKTATÓ | F5.2 DEMO: 23 tételes csomag |
| 3:05-3:10 | ⏸ STÁCIÓ 5.A | Form-katalogizáló (mezők kategorizálása) |
| 3:10-3:15 | ⏸ STÁCIÓ 5.B | Manuális idő-becslés |
| 3:15-3:19 | 🎤 OKTATÓ | F5.3 DEMO: Form-kitöltés AI-jal + összevetés |

### 2:44-2:46 — Átvezetés

🖥 **CSINÁLOM:** Mutatom 20 mp-ig a TransOffice fájl-mappát F1-ből (káosz emlékeztető).

📍 **MONDOM:** *„...innen indultunk. Most összeállítjuk a teljes pályázatot."*

### 2:46-2:58 — F5.1 DEMO: Plan de afaceri (12 perc)

📝 **PROMPT (én írom be):**
```
Készíts egy teljes Plan de afaceri-t (románul) a TransOffice számára
az AFM Mobilitate Verde 2026 pályázathoz. Tartalmazza:

1. Rezumat executiv
2. Prezentarea companiei (Béla bácsi telephely-stabilitással)
3. Analiza pieței (B2B irodai logisztika Hargita megye)
4. Proiect propus — 5 elektromos jármű + 2 töltőpont
5. Plan financiar — 18 hónapos cash flow, EBITDA forecast 5 évre
6. Plan de marketing
7. Plan de implementare — M1-M18 milestone-ok
8. Echipa managerială

Hossz: 25-40 oldal. Stílus: profi, román pályázati formátum.
Vedd alapul: F1 cégadatok + F3 eligibility + F4 EBITDA +
F4 Béla bácsi vételi opció.
```

🖥 **CSINÁLOM:** Várok 2-3 perc — **CSENDBEN**. Hadd lássák.

🖥 **CSINÁLOM:** Görgetem a kész doksit. Kiemelek 3-4 fejezetet.

📍 **MONDOM:** *„260 sor, **románul**, profi minőség. Tanácsadó 3-5 nap, 2-3000 EUR. Mi: 2 perc."*

### 2:58-3:05 — F5.2 DEMO: 23 tételes csomag (7 perc)

📝 **PROMPT (én írom be):**
```
Készíts egy 23-tételes pályázati csomag-checklistet a Plan de afaceri
+ Data Completion Board alapján. Oszlopok: tételszám, dokumentum,
státusz (van/hiányzik/folyamatban), forrás, felelős.
```

🖥 **CSINÁLOM:** Mutatom a táblát.

📍 **MONDOM:** *„23 tétel — mindegyiknél tudjuk hol van, ki kapja, mikor."*

### 3:05-3:10 — ⏸ STÁCIÓ 5.A: Form-katalogizáló (5 perc)

📍 **MONDOM:** *„Most ti következtek. **Tanuljunk meg összefoglalni egy formot.** Nyissátok meg a saját Cowork-jeiteken — kapjatok egy gyors katalogizálót a pályázati formról."*

🖥 **CSINÁLOM:** Megosztom a `formular_depunere_AFM_Mobilitate_Verde.html` linket (vagy fájlt).

📝 **PROMPT (ők másolják):**
```
Itt a pályázati formunk: formular_depunere_AFM_Mobilitate_Verde.html

Nyisd meg, és listázd ki az ÖSSZES mezőt kategória szerint csoportosítva
(pl. Cégadatok, Pénzügy, Projektleírás, Mellékletek). Minden mezőhöz írd:
- kötelező-e
- milyen formátumban kell kitölteni (szöveg / szám / dátum / fájl)

A kimenet egy strukturált tábla legyen.
```

🖥 **CSINÁLOM:** Körbejárok. Pár perc múlva: *„Mindenki látja? Hány mező van összesen?"*

### 3:10-3:15 — ⏸ STÁCIÓ 5.B: Manuális idő-becslés (5 perc) ← **KONTRASZT-PILLANAT**

📍 **MONDOM:** *„Most a következő stáció. **Becsüljétek meg: ha NEM AI-val, csak kézzel kellene kitölteni, mennyi idő lenne?** Másoljátok be:"*

📝 **PROMPT (ők másolják):**
```
A formular_depunere_AFM_Mobilitate_Verde.html alapján: ha MINDEN
információ a kezedben van (cégadatok, pénzügyi számok, projektleírás
megfogalmazva), és csak MANUÁLISAN, gondolkodás nélkül kell beírnod
minden mezőt — mennyi időbe telne a teljes form kitöltése?

Számítsd ki mezőkként (kb. mennyi idő egy egyszerű mezőre, mennyi
egy hosszabb szöveges mezőre, mennyi egy file-feltöltésre), és
összesítve. Adj egy reális percszámot.
```

🖥 **CSINÁLOM:** *„Aki kész, mondja az eredményt szóban."* — 2-3 ember válaszol: *„85 perc", „2 óra", „90 perc"*.

📍 **MONDOM:** *„Tehát kb. **1,5-2 óra manuálisan**, ha minden adat a kezünkben van. **Nézzük mit csinál a Cowork.**"*

### 3:15-3:19 — F5.3 DEMO: Form-kitöltés AI-jal (4 perc) ← **WOW**

🖥 **CSINÁLOM:** A saját Cowork-jén.

📝 **PROMPT (én írom be):**
```
Tölts ki minden mezőt a formular_depunere_AFM_Mobilitate_Verde.html
formban. Használd a Plan de afaceri + Dosar complet + Data Completion
Board adatokat. Generálj egy CSV-t ami minden mezőhöz tartalmazza
az értéket.
```

🖥 **CSINÁLOM:** Várok 60-90 mp. A CSV elkészül. Mutatom 5-6 mezőt élőben kitöltve a form-mockup-on.

📍 **MONDOM:** *„**90 mp.** A ti becslésetek 90 PERC volt. **60× gyorsabb. És hibátlanul.**"*

📍 **MONDOM:** *„**Itt a pályázat. Be van adva. Eddig a film. De Márton közben mondja...**"* — átkötés F6-ba.

---

## 🎬 F6 — Web redesign (3:19 → 3:37, 18 perc)  <a id="f6"></a>

**Cél:** Vizuális payoff. Az AI mint designer + builder.
**Stáció:** 1 db, **nagy** — mindenki saját 3 variánst generál különböző stílusban.

| Idő | Mód | Mit |
|---|---|---|
| 3:19-3:23 | 🎤 OKTATÓ | Régi oldal elemzése (Comic Sans) |
| 3:23-3:28 | 🎤 OKTATÓ | DEMO: 1 referencia variáns (Modern) |
| 3:28-3:35 | ⏸ STÁCIÓ | Mindenki 3 variáns saját stílusban |
| 3:35-3:37 | 💬 BESZÉLGETÉS | Bemutatók (2-3 résztvevő) |

### 3:19-3:23 — Comic Sans nevetés (4 perc)

🖥 **CSINÁLOM:** Átkapcsolok a `transoffice_old_website.html` browser tab-ra. Scrollozok le-fel — látsszanak a bizarr elemek.

📍 **MONDOM (drámai felzaklatott hangon):** *„Hölgyeim és Uraim — TransOffice Trade SRL, 2012-ben. Comic Sans. Animált csillagok. Vendégkönyv. 14 872 látogató. **Best viewed in Internet Explorer 8.**"*

⚠️ **VIGYÁZZ:** **Hagyd hogy nevessenek.** Ez a workshop legjobb pillanata. 3:19-kor a fáradt csoportnak energia kell.

📍 **MONDOM:** *„Márton: 'Ez a cégünk arca. Szégyen.' De most fél óra van. **Tudunk-e ebből valamit csinálni?**"*

### 3:23-3:28 — DEMO: 1 referencia variáns (5 perc)

📝 **PROMPT (én írom be):**
```
Készíts egy modern, clean B2B weboldal-variánst a TransOffice számára
HTML-ben. Egyetlen fájlban (inline CSS).

- Színek: kék, fehér, szürke
- Tipográfia: modern sans-serif (Inter / system-ui)
- Hero szekció: cég neve + 1 mondatos pozícionálás
- Szolgáltatások: 3-4 kártya icon-okkal
- AFM elektromos járműflotta szekció: 5 jármű, 2 töltőpont, 5,2t CO2/év
- Csapat: Márton + Enikő
- Kapcsolat: Székelyudvarhely cím

Reszponzív, mobile-friendly.
```

🖥 **CSINÁLOM:** Várok 60-90 mp. Megnyitom új browser tab-ban.

📍 **MONDOM:** *„Tiszta, modern, professzionális. **5 perc.** Egy designer csapat 3 hét, 5-8 000 RON."*

### 3:28-3:35 — ⏸ STÁCIÓ 6: Mindenki 3 saját variáns (7 perc)

📍 **MONDOM:** *„Most ti következtek. **Mindenki generáljon 3 variánst eltérő stílusban.** Itt a prompt — egyetlen szóváltoztatással új arcot kap a cég. Tegyétek el magatoknak a 3 verziót."*

📝 **PROMPT (ők másolják) — első variáns:**
```
Készíts egy [STÍLUS] weboldal-variánst a TransOffice számára HTML-ben,
inline CSS-szel. Egy fájl.

Tartalmazza:
- Hero (cég neve + pozícionálás)
- Szolgáltatások (3-4 kártya)
- AFM zöld átállás szekció (5 jármű, 2 töltőpont)
- Csapat (Márton, Enikő)
- Kapcsolat (Székelyudvarhely)

Reszponzív, mobile-friendly. Egyetlen HTML fájl.
```

📍 **MONDOM:** *„A `[STÍLUS]` helyére másoljatok be 3 különbözőt:*
- *Variáns 1: **'klasszikus, konzervatív, intézményi'**;*
- *Variáns 2: **'erdélyi, meleg, helyi karakter'**;*
- *Variáns 3: **bármi amit ti elképzeltek** — pl. 'startup-os energikus', 'minimal japán-zen', 'retró-90-es'..."*

🖥 **CSINÁLOM:** Körbejárok. **Hagyom hogy kísérletezzenek.**

⚠️ **VIGYÁZZ:** Egyiküknek a 3 variáns nem fog elférni 7 percbe. **Az is OK** ha csak 2 készül. **A kísérletezés a lényeg.**

### 3:35-3:37 — 💬 Bemutatók (2 perc)

📍 **MONDOM:** *„Ki készített valami menőt? Mutasd meg!"*

🖥 **CSINÁLOM:** 1-2 résztvevő prevezeti a sajátját a kivetítőn (USB / GDrive / képernyőmegosztás).

⚠️ **VIGYÁZZ:** **2 perc kemény limit** — ne folyjanak túl a bemutatók.

📍 **MONDOM:** *„Innen indultunk... ide értünk. Most jön a zárás."*

---

## 🎬 ZÁRÁS (3:37 → 3:50, 13 perc)  <a id="zar"></a>

**Cél:** Elviszik a tanulságot, közös élmény-záró pont.

| Idő | Mód | Mit |
|---|---|---|
| 3:37-3:40 | 🎤 OKTATÓ | Visszatekintés a 6 fázisra |
| 3:40-3:46 | ⏸ STÁCIÓ | Anonim „1 mondat amit elviszek" |
| 3:46-3:48 | 🎤 OKTATÓ | Bónusz feladatok bemutatása |
| 3:48-3:50 | 🎤 OKTATÓ | Búcsú |

### 3:37-3:40 — Visszatekintés (3 perc)

📍 **MONDOM (lassan, hangsúlyosan, ujjakon számolva):**
- *„F1 — 30 fájl kaotikus → rendezett mappa + CLAUDE.md"*
- *„F2 — kaotikus meeting → 14 mentett TODO"*
- *„F3 — 94 oldalas pályázati kiírás → eligibility + gap + akcióterv"*
- *„F4 — Béla bácsi cross-doc felfedezés + Mihaela EBITDA + Márton PPTX"*
- *„F5 — teljes Plan de afaceri + 23 tételes csomag + 90 perces form 90 másodperc alatt"*
- *„F6 — Comic Sans → 3 modern weboldal mindenkitől"*

📍 **MONDOM:** *„Régen egy ember 5-7 napos munkája. Ma: 4 óra."*

### 3:40-3:46 — ⏸ STÁCIÓ: Anonim „1 mondat amit elviszek" (6 perc)

📍 **MONDOM:** *„Utolsó körünk. Mindenki **1 mondatban** írja meg: **mi az 1 dolog amit ma elviszel?** Anonim — nem kell megosztanod. Másoljátok be a Cowork-be ezt:"*

📝 **PROMPT (ők másolják) — a saját Cowork-jükben:**
```
Egy mondatban: a mai workshopból mi az 1 dolog amit elviszek a saját
életembe, a saját cégemnél, a saját munkámban? Légy konkrét.
```

📍 **MONDOM:** *„Aki akarja, megoszthatja velünk. Aki nem, az is jó — eltette magának."*

🖥 **CSINÁLOM:** Körbejárok. 1-2 mondatot elolvasok hangosan a saját laptopomon (a sajátomat). *„Nálam pl.: ...."*

📍 **MONDOM:** *„Ki szeretne megosztani? Akinek tetszik."* — 3-4 önkéntes szólhat.

⚠️ **VIGYÁZZ:** **Ne kommentáld** amit hallasz. Bólints, „Köszönöm."

### 3:46-3:48 — Bónusz feladatok (2 perc)

📍 **MONDOM:** *„A Tananyag mappában találtok **18 bónusz feladatot** — minden fázishoz 3-4 db. Otthon, a saját tempótokban kipróbálhatjátok. **A lényeg: ne másold a TransOffice-t — vidd át a saját életedre.** Saját szerződéseden, saját meetingeden, saját pályázatodon."*

### 3:48-3:50 — Búcsú (2 perc)

📍 **MONDOM:** *„Ennyi volt. **Köszönöm.** Ha kérdés van, **most** szóljatok. Holnap email-en is elérhető vagyok."*

📍 **MONDOM:** *„Vigyázzatok magatokra. **Találkozunk a következő szinten.**"*

---

## 📎 Appendix A — Minden prompt egy helyen  <a id="appA"></a>

### A.1 — F1 STÁCIÓ (ők másolják)
```
Az új munkatárs vagyok a TransOffice cégnél, ma az első napom.

A TransOffice mappában találod a cégünk összes dokumentumát. Rendetlenség
van — évek alatt gyűlt össze mindenféle dokumentum, és senki nem nézte át
őket.

Légy szíves, segíts rendbe tenni:

1. Először a jelenlegi mappáról készíts egy biztonsági másolatot, hogy
   bármikor vissza tudjam keresni a fileokat.
2. Kezd el egyenként átnézni a fileokat és kategorizálni.
3. Legyen egy Kuka mappa is — abba másolj minden olyan filet, ami szemét,
   elavult, vagy nem releváns.
4. Gyere egy javaslattal, hogy hogyan rendezzük az anyagot, és rendezd is
   el úgy.
5. Készíts nekem egy kivonatot arról, mit találtál és mit csináltál.

Készíts egy CLAUDE.md fájlt is — ez lesz a hosszútávú memóriád. Minden új
munkamenetben elsőként ezt fogod elolvasni.

Ha bármi nem világos, kérdezz vissza.
```

### A.2 — F2 DEMO (én)
```
Olvasd el ezt a meeting transcriptet. Sürgős megbeszélés egy EU pályázatról
(AFM Mobilitate Verde 2026 — elektromos járműflotta).

Kérek:
1. Helyzet összefoglaló (3-5 mondat)
2. TODO lista: Ki → Mit → Mikorra → Prioritás
3. Hiányzó információk (amik nélkül nem lehet pályázni)
4. Blokkolók: melyik TODO függ a másiktól

A TODO-kat mentsd el a Productivity pluginbe.
```

### A.3 — F2 STÁCIÓ (ők másolják)
```
Olvasd el a CLAUDE.md-t. Ez alapján és a workshop-vezetőtől látott TODO
lista alapján: írj egy 4-5 mondatos follow-up emailt Enikőnek arról,
hogy mik a feladatai a következő 3 napban az AFM pályázat előkészítésében.

Hangnem: kollegális, konkrét, határidős. Magyarul írd.
```

### A.4 — F3.1 DEMO (én)
```
Olvasd át a Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-
2025.md fájlt és vesd össze a TransOffice cégadatokkal (CLAUDE.md alapján).

Listázd ki az ÖSSZES eligibility kritériumot. Minden kritériumra jelöld:
✅ TELJESÍTJÜK / ⚠️ RÉSZBEN / ❌ NEM TELJESÍTJÜK
+ rövid indoklás (max 2 mondat / kritérium)

A végén egy döntés: PÁLYÁZHATUNK / NEM PÁLYÁZHATUNK / FELTÉTELESEN
+ a top 3 kockázat amit el kell intézni.
```

### A.5 — F3 STÁCIÓ 3.A (ők másolják)
```
Olvasd el a Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-
2025.md-ben a CR-08 (járműflotta) kritériumot. A TransOffice teljesíti-e?
Részletesen, indoklással. Maximum 5 mondat.
```

### A.6 — F3.2 DEMO (én)
```
Most listázd ki a 17 kötelező mellékletet a pályázathoz. Minden
mellékletre jelöld a TransOffice cégadatok (CLAUDE.md + TransOffice/
mappa) alapján: VAN / NINCS / RÉSZBEN. Ahol RÉSZBEN vagy NINCS, írd
oda kitől kell beszerezni és milyen formátumban.
```

### A.7 — F3 STÁCIÓ 3.B (ők másolják)
```
Az M-11 (járműflotta-leltár) mellékletet hogyan állítanám össze?
Kitől kapok adatot, milyen formátumban, hány napos a folyamat?
Maximum 6 mondat.
```

### A.8 — F3.3 DEMO (én)
```
Az eligibility + gap analízisből generálj Data Completion Board-ot:
oszlopok = Tétel, Felelős, Határidő, Forrás, Státusz. Csoportosítsd
3 fázis szerint: BEADÁS ELŐTT / ELBÍRÁLÁS ALATT / MEGVALÓSÍTÁS ALATT.
```

### A.9 — F4.1 DEMO (én) — bérleti szerződés + cross-doc
```
Olvasd el a szerzodes_chirie_TransOffice_2018.docx-et. A TransOffice
mint bérlő szempontjából:

1. Listázd a top 5 kockázati pontot
2. Hasonlítsd össze a TransOffice mappájában lévő MÁS fájlokkal —
   keress kapcsolódó információt (meeting transcript, emailek,
   jegyzetek). Bármilyen red flag fontos.
3. A pályázat (AFM Mobilitate Verde 2026, beadás 2026-08-31) 5 év
   telephely-stabilitást és töltőpont-engedélyt követel — teljesítjük?
```

### A.10 — F4.1 STÁCIÓ (ők másolják) — felkérő email Béla bácsinak
```
Írj egy emailt Béla bácsi (a telephely-tulajdonos, 70 éves családi ismerős)
számára Márton nevében. A helyzet:

- A jelenlegi bérleti szerződésünk 2028-ig megy
- Egy EU pályázathoz (AFM Mobilitate Verde 2026, elektromos járműflotta)
  a telephely-bérletnek 2026-08-31-től számítva legalább 5 évig kell
  érvényesnek lennie — tehát 2031-08-31-ig
- Plusz: a tulajdonosnak írásban (acord scris) kell engedélyt adnia a
  töltőállomás telepítésére

Két dolgot kérjünk tőle az emailben:
1. act adițional a szerződés meghosszabbítására (min. 2031-ig, ideálisan
   tovább)
2. acord scris a töltőpont telepítésére

Hangnem: tisztelettudó, közvetlen, magyaros — Béla bácsi régi ismerős, 70 éves.
Max 8 mondat. Magyarul írd.
```

### A.11 — F4.1 második DEMO (én) — DCB frissítés a válasz után
```
Béla bácsi visszaválaszolt: 2035-ig meghosszabbítja a szerződést +
közjegyzőileg + vételi opció. Frissítsd a Data Completion Board-ot:
a 'telephely-stabilitás' státusza most ✅ ZÖLD. Bővítsd a megjegyzéssel:
„vételi opció további lépés F5-ben."
```

### A.12 — F4.2 STÁCIÓ (ők másolják) — felkérő email Mihaelának románul
```
Írj egy emailt Mihaela Ionescu-nak (mihaela.ionescu@contabilpro.ro,
a TransOffice külsős könyvelője) Márton nevében. A helyzet:

- Pályázunk az AFM Mobilitate Verde 2026 programra (elektromos járműflotta)
- Beadási határidő: 2026-08-31, ora 16:00 — ~1 hét van vissza
- A pályázat előírja: az utolsó 2 lezárt pénzügyi év mérlege és pénzügyi
  helyzete (bilanț + cont de profit și pierdere + EBITDA + alkalmazotti
  létszám) — tehát 2024 és 2025
- Mihaela a könyvelő, ezek az adatok nála vannak

Kérjük meg Mihaelát hogy:
- Küldje át a 2024 és 2025 bilanț + cont de profit și pierdere kivonatot
- Mellékeljen 1 sor EBITDA-t és az alkalmazotti létszámot (FTE)
- Határidő: 3 napon belül (a pályázati beadáshoz időben kelljen
  fel tudjuk dolgozni)

Hangnem: románul, professzionális de közvetlen — Mihaela 45 éves,
részmunkaidős, precíz. Max 8 mondat.
```

### A.13 — F4.2 DEMO (én) — Mihaela bilanc Excel elemzés
```
Itt van Mihaela visszaküldött bilance-Excelje (2024+2025).
Számítsd ki és mutasd be:

1. Árbevétel 2024 vs 2025 (RON-ban + %)
2. EBITDA 2024 vs 2025 (RON-ban + marzs %)
3. Alkalmazottak száma 2024 vs 2025
4. Trend értelmezése — emelkedünk vagy csökkenünk?
5. Pályázati szempontból: melyik 3 KPI a legerősebb érv?

És az utolsó: az EBITDA margin 2025-re — pontos százalék.
```

### A.14 — F4.3 DEMO (én) — CEO update PPT
```
Készíts egy 5 slide-os PPTX prezentációt Mártonnak az AFM Mobilitate
Verde 2026 pályázat aktuális állásáról. Slide-onkénti felépítés:

Slide 1: Helyzet — hol állunk a Data Completion Board-on
Slide 2: Eligibility check — ✅ pályázhatunk
Slide 3: Pénzügyi készség — EBITDA 2025 marzs, trend 2024→2025
Slide 4: Béla bácsi (telephely) — zöld (2035-ig), sőt vételi opció
Slide 5: Akcióterv — a következő 7 nap a beadásig

Stílus: tiszta, üzleti, magyar nyelven.
```

### A.15 — F5.1 DEMO (én)
```
Készíts egy teljes Plan de afaceri-t (románul) a TransOffice számára
az AFM Mobilitate Verde 2026 pályázathoz. Tartalmazza:

1. Rezumat executiv
2. Prezentarea companiei (Béla bácsi telephely-stabilitással)
3. Analiza pieței
4. Proiect propus — 5 elektromos jármű + 2 töltőpont
5. Plan financiar — 18 hónapos cash flow, EBITDA forecast
6. Plan de marketing
7. Plan de implementare — M1-M18
8. Echipa managerială

Hossz: 25-40 oldal. Stílus: profi, román pályázati formátum.
Vedd alapul: F1 cégadatok + F3 eligibility + F4 EBITDA + F4 Béla bácsi.
```

### A.16 — F5.2 DEMO (én)
```
Készíts egy 23-tételes pályázati csomag-checklistet a Plan de afaceri
+ Data Completion Board alapján. Oszlopok: tételszám, dokumentum,
státusz (van/hiányzik/folyamatban), forrás, felelős.
```

### A.17 — F5 STÁCIÓ 5.A (ők másolják)
```
Itt a pályázati formunk: formular_depunere_AFM_Mobilitate_Verde.html

Nyisd meg, és listázd ki az ÖSSZES mezőt kategória szerint csoportosítva
(pl. Cégadatok, Pénzügy, Projektleírás, Mellékletek). Minden mezőhöz írd:
- kötelező-e
- milyen formátumban kell kitölteni (szöveg / szám / dátum / fájl)

A kimenet egy strukturált tábla legyen.
```

### A.18 — F5 STÁCIÓ 5.B (ők másolják)
```
A formular_depunere_AFM_Mobilitate_Verde.html alapján: ha MINDEN
információ a kezedben van (cégadatok, pénzügyi számok, projektleírás
megfogalmazva), és csak MANUÁLISAN, gondolkodás nélkül kell beírnod
minden mezőt — mennyi időbe telne a teljes form kitöltése?

Számítsd ki mezőkként (kb. mennyi idő egy egyszerű mezőre, mennyi
egy hosszabb szöveges mezőre, mennyi egy file-feltöltésre), és
összesítve. Adj egy reális percszámot.
```

### A.19 — F5.3 DEMO (én) — Form-kitöltés AI-jal
```
Tölts ki minden mezőt a formular_depunere_AFM_Mobilitate_Verde.html
formban. Használd a Plan de afaceri + Dosar complet + Data Completion
Board adatokat. Generálj egy CSV-t ami minden mezőhöz tartalmazza
az értéket.
```

### A.20 — F6 DEMO (én) — Modern referencia
```
Készíts egy modern, clean B2B weboldal-variánst a TransOffice számára
HTML-ben. Egyetlen fájlban (inline CSS).

- Színek: kék, fehér, szürke
- Tipográfia: modern sans-serif
- Hero (cég neve + pozícionálás)
- Szolgáltatások: 3-4 kártya icon-okkal
- AFM elektromos járműflotta szekció: 5 jármű, 2 töltőpont, 5,2t CO2/év
- Csapat: Márton + Enikő
- Kapcsolat: Székelyudvarhely cím

Reszponzív, mobile-friendly.
```

### A.21 — F6 STÁCIÓ (ők másolják — 3-szor, [STÍLUS] cserével)
```
Készíts egy [STÍLUS] weboldal-variánst a TransOffice számára HTML-ben,
inline CSS-szel. Egy fájl.

Tartalmazza:
- Hero (cég neve + pozícionálás)
- Szolgáltatások (3-4 kártya)
- AFM zöld átállás szekció (5 jármű, 2 töltőpont)
- Csapat (Márton, Enikő)
- Kapcsolat (Székelyudvarhely)

Reszponzív, mobile-friendly. Egyetlen HTML fájl.
```

[STÍLUS]-példák: `klasszikus, konzervatív, intézményi` / `erdélyi, meleg, helyi karakter` / `startup-os energikus` / `minimal japán-zen` / `retró-90-es`

### A.22 — Zárás STÁCIÓ (ők másolják)
```
Egy mondatban: a mai workshopból mi az 1 dolog amit elviszek a saját
életembe, a saját cégemnél, a saját munkámban? Légy konkrét.
```

---

## 🚨 Vészforgatókönyv  <a id="vesz"></a>

### Ha a Cowork **lefagy**
1. Frissítsd az ablakot (Cmd+R)
2. Indítsd újra a Cowork desktop-ot
3. Használd a **Claude.ai web-verziót** (Pro plugin-ek ott is)
4. Plan B: a `Pelda_outputok/` mappa minden F3 demohoz előre legenerált választ tartalmaz

### Ha **WiFi kiszakad**
- 📍 *„10 perces kávészünet."* — kapcsolj **mobil hotspotra** (előre tesztelve)
- Plan B: az előre letöltött PDF outputok kinyomtatva

### Ha **a csoport totál fáradt**
- Adj **2 perces állva-kávé** szünetet
- F6-ot kezdd erősen (régi oldal nagyon emelt, drámai)

### Ha **idejétkorán végezel**
- Hagyj **plusz Q&A időt** a végén
- Mutasd be a **bónusz feladatokat** részletesebben
- Egy résztvevő **saját szituációját** dolgozd fel a Cowork-kel közösen

### Ha **csúszol és nem fér be minden**
- F3 és F4 között legyen **kemény time-box**
- F6 az utolsó **vágható** fázis (még 10 percben is hatékony)
- A „1 mondat" záró STÁCIÓ-t **soha ne hagyd ki**

---

## 📜 Verzió-előzmények

| Verzió | Dátum | Változás |
|---|---|---|
| **1.0** | 2026-05-12 | Első kiadás — minden fázis részletezve, 70/20/10 ígérve. |
| **2.0** | 2026-05-12 | **Páros-mód + stációk modell.** Az oktató kivetítve végigviszi a narratívát. A résztvevők stációknál (F1 kivételével) 1-2 izolált mini-feladatot csinálnak saját laptopukon. F1 = mindenki saját laptopján parallel mode. Új F5 stáció-pár: form-katalogizáló + manuális idő-becslés → kontraszt-pillanat az AI-form-kitöltéssel. 23 prompt egy helyen az Appendix A-ban. |
| **2.1** | 2026-05-14 | **Dátum-pivot 2025 → 2026:** kiírás IMM-2026, beadási határidő 2026-08-31, meeting 2026-08-25, bilanc 2024+2025. **F4 új modell:** mindkét stáció a tanuló írja a felkérő emailt (Béla bácsi magyarul + Mihaela románul), az oktatói DEMO-k a válaszokat mutatják. **F1 prompt v2.1:** rövidebb, akcióközpontú (5 lépés + Kuka mappa + CLAUDE.md). Bónusz fájlok hint-stílusra átírva (22 db), DEMO-fájlok kibővítve „Otthoni változat" prompttal (4 db). Appendix A: 22 prompt, renumerált. |

---

**Készítette:** Claude (Cowork)
**Kapcsolat:** Szabolcs · exarlabs@gmail.com
**Utolsó frissítés:** 2026-05-12
