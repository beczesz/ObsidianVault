---
title: "Feladat 3.3 — Data Completion Board és responsibility map"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Strukturált akciótervét a pályázati mellékletek kitöltésére, amely felelősöket, határidőket, bemeneti függéseket és kockázatokat tartalmaz. Az Operations Managernek és Mártonnak szükséges, hogy napi szinten követhessék a 23 dokumentum elkészültét és biztosítsák az április 30-as beadást."
description_source: auto
description_hash: cf6dabd2f5147bb0
id: cef70ed9-3255-4cdf-993c-3fa04baf1ced
index_schema_version: 1
bdos_index: true
---
# Feladat 3.3 — Data Completion Board és responsibility map

## Szituáció

Megvan az eligibility (3.1: pályázhatunk), megvan a gap-elemzés (3.2: 23 melléklet, 6 piros, 11 sárga). De Márton fejében most ott zúg a következő kérdés:

> "Oké, megvan a lista. De ki csinál mit, mikorra? Ha most nem osztjuk szét és nem rögzítjük valahol, holnaputánra szétesik. Csináljunk egy táblát — egy közös munkatábla, amiben látjuk: ki dolgozik min, mikor adja le, mit kell ahhoz előbb megcsinálni. Olyan kanban-szerű."

> "És ami fontos: ezt **élő** táblának kell lennie. Nem egyszer kitölteni és elfelejteni. Naponta ránézünk, frissítjük."

## Feladat

A 3.2 gap-elemzéséből készíts **Data Completion Board**-ot — egy strukturált akciótervet, ami már önmagában is munkaeszköz. Ez nem összefoglaló dokumentum, hanem **élő munkatábla**.

## Elvárt kimenet

Egy `data_completion_board.md` fájl, ami tartalmazza:

### 1. Áttekintés (dashboard sor)

```
📊 PÁLYÁZAT: AFM Mobilitate Verde IMM 2025
🗓️ HATÁRIDŐ: 2025.04.30
⏰ HÁTRALÉVŐ: X munkanap
📋 ÖSSZES MELLÉKLET: 23 (17 dokumentum + 6 nyilatkozat)
✅ KÉSZ: 0 / 23
🟡 FOLYAMATBAN: 0 / 23
⏳ HÁTRA: 23 / 23
🚨 KRITIKUS (lejárhat): X / 23
```

### 2. Felelősök tábla (responsibility map)

| Felelős | Szerep | Hozzárendelt mellékletek | Becsült munkaóra |
|---------|--------|-------------------------|------------------|
| Te (Operations Manager) | Koordinátor + AI | M-11, M-13, N-01..N-06 | 8-12 ó |
| Enikő (könyvelő) | Pénzügy | M-05, M-06, M-07, M-08, N-02 | 4-6 ó |
| Külső könyvelő | Mérleghitelesítés | M-05 (hitelesítés) | - (külsős) |
| Bíró Attila (raktárvezető) | Flotta | M-11 input, M-12 | 3-4 ó |
| Márton (ügyvezető) | Aláírások, döntések | M-02, M-13 jóváhagyás, UBO | 2-3 ó |
| Ilona (volt admin) | Régi dokumentum-archeológia | M-01, M-04 (telefonon) | 1-2 ó |
| Külső szolgáltató | Fordítás, közjegyző | M-03 UBO, fordítások | - (költség) |

### 3. Akcióterv táblázat (a fő tábla)

| ID | Melléklet | Felelős | Bemenet (mit kell előbb?) | Határidő | Státusz | Megjegyzés |
|----|-----------|---------|---------------------------|----------|---------|------------|
| T-01 | M-01 Cégkivonat | Enikő | - | +1 nap | ⏳ TODO | ONRC online, 50 RON |
| T-02 | M-06 Certificat fiscal | Enikő | - | +1 nap | ⏳ TODO | max. 30 napos szabály — a beadás előtt 1 hétre időzítsük |
| T-03 | M-11 Járműflotta-leltár | Te + Attila | meglévő Excelek átnézése | +3 nap | ⏳ TODO | jelenleg "3? 4?" — pontosítani kell |
| T-04 | M-05 Mérleg 2023-24 | Enikő + külsős | - | +5 nap | ⏳ TODO | mérlegképes hitelesítés szükséges |
| T-05 | M-13 Üzleti terv | Te + Márton | M-11 kész | +10 nap | ⏳ TODO | kockázatelemzés + 5 éves cash flow |
| ... | ... | ... | ... | ... | ... | ... |

### 4. Kritikus út (Gantt-szerű blokk)

```
Hét 1 (most):  M-01 ✓ M-06 ✓ M-11 (folyamatban)
Hét 2:         M-05 ✓ M-12 ✓ N-01..N-06
Hét 3:         M-13 (üzleti terv) ←—— függ M-11-től
Hét 4:         M-15 (dealer árajánlatok) ←—— függ M-13-tól
Hét 5:         M-06 frissítés (30 napos!) + konszolidáció + beadás
```

### 5. Kockázatok és mitigation

| Kockázat | Valószínűség | Hatás | Mitigation |
|----------|--------------|-------|------------|
| M-11 járműadatok hiányosak | Magas | Magas (kizáró) | Attila + telephelyi körbenézés azonnal |
| M-06 lejár (30 nap) | Magas | Magas | Beadás előtti héten újra beszerezni |
| M-03 UBO közjegyző | Közepes | Közepes | Időpontot foglalni a héten |
| M-05 könyvelő nem ér rá | Közepes | Közepes | Email **azonnal**, ne tegyük holnapra |
| Forrás kimerül 04.30 előtt | Közepes | Magas | Beadás célja max. 03.31. |

### 6. Napi sync javaslat

5 perces napi stand-up Mártonnal és Enikővel:
- mi készült el tegnap?
- min dolgozol ma?
- mi blokkol?

A Productivity plugin minden TODO-t kezel — a tábla egyetlen igazsága a `data_completion_board.md` és a Cowork TODO-store.

## Prompt javaslat

```
A 3.2-ben elkészült gap analysis alapján generálj egy Data Completion Board-ot a 
data_completion_board.md néven.

A struktúra:

1. Dashboard fejléc (határidő, hátralévő nap, ✅ / 🟡 / ⏳ / 🚨 számok)
2. Responsibility map: ki melyik mellékletért felel + becsült munkaóra
3. Akcióterv táblázat: 23 sor (M-01 .. M-17 + N-01 .. N-06)
   - ID, melléklet, felelős, bemeneti függés, határidő, státusz, megjegyzés
4. Kritikus út: heti bontásban mi mire épül
5. Kockázatok + mitigation
6. Napi sync javaslat

Felelősök listája:
- Te (Operations Manager) — koordináció + AI munka
- Enikő (könyvelő) — pénzügyi mellékletek
- Külső könyvelő — mérleghitelesítés
- Bíró Attila — járműadatok input
- Márton (ügyvezető) — aláírások, jóváhagyások
- Ilona (volt admin, telefonos) — régi dokumentumok megtalálása
- Külső szolgáltató — közjegyző, fordítás

A határidő 2025.04.30. Tervezzük úgy, hogy 03.31-ig le legyen zárva (időbeli ráhagyás).

Mentsd el a táblát + a TODO-kat a Productivity pluginbe is, hogy session-ök között követhető legyen.
```

## Tanulási pont

- A Cowork output **nem statikus dokumentum, hanem munkaeszköz** — a tábla egyszerre dashboard, naplózó és kanban
- A **felelős-határidős struktúra önmagában is delegálási eszköz** — kinyomtathatod, e-mail-ben elküldheted, nyitva tarthatod naponta
- A **Productivity plugin integráció** miatt minden sor egy mentett TODO — emlékszik rá session-ök között (F2 visszhangja)
- Az AI itt **nem csak listát ír**, hanem **strukturált döntési rendszert** — kockázatokkal, függésekkel, kritikus úttal

## Tippek

- A **kritikus út azonosítása** kulcsfontosságú: M-13 üzleti terv = nagyjából 1 hét, és **csak akkor írható**, ha M-11 (járműflotta) megvan
- A **30 napos érvényességű dokumentumok** (M-06 certificat fiscal) **a végén** szerezhetők be, nem az elején — különben lejárnak
- A **delegálás** kritikus: ha minden Te csinálsz, megfulladsz. Az AI segíthet **email-tervezetet** írni Enikőnek, Attilának, Ilonának (ezt F4-ben részletezzük)
- A workshop résztvevői itt látják, hogy **az AI nem csak elemző, hanem projektmenedzser is**

## Checkpoint

**WOW (te demózod):**
- A 3.2 gap-elemzésből egy prompttal generálsz **teljes Data Completion Board-ot** Markdown táblákkal
- Megmutatod a 6 blokkot egymás után: dashboard → felelősök → akcióterv → kritikus út → kockázatok → napi sync
- A Productivity pluginben is megjelennek a TODO-k
- Punchline: "Ez **másnap is itt lesz**. Ez **2 hét múlva is itt lesz**. Az AI emlékszik. Itt nincs Excel, ami eltűnik."

**MICRO HANDS-ON (ők csinálják):**
- Mindenki kiválaszt egy sort a 23-ból
- Áthúzzák a felelőst (pl. "ez ne Enikő legyen, hanem én") VAGY módosítják a határidőt
- Az AI újraszámolja a kritikus utat — látják, hogyan **mozdul** a tábla
- 2-3 perc, az élmény: **élő tábla, nem statikus dokumentum**

**FLOW tovább:**
- Visszaülünk
- Megmutatod a "Naponta ránézek erre"-flow-t: új session, "mutasd a Data Completion Board-ot" — kész, ott van
- Átkötés F4-be: "A tábla megvan. Most kezdődik a tényleges munka: emaileket küldeni, Excel-eket olvasni, szerződést átnézni. Hogyan segít ezekben az AI mint operátor?"

## Időkeret

- Workshopon: ~7-10 perc (5p demo + 2-3p hands-on + 1-2p átkötés)
- Cél: a résztvevők lássák, hogy **a végeredmény nem dokumentum, hanem munkarendszer** — ami másnap is működik

## Értékelési szempontok (instructor számára)

A résztvevő sikeresen részt vett, ha:
- [ ] Látta, hogy a Data Completion Board strukturált (dashboard + tábla + kritikus út)
- [ ] Megtapasztalta, hogy a felelős/határidő módosítás esetén a kritikus út újraszámolódik
- [ ] Felismeri, hogy ez **élő munkaeszköz**, nem egyszer kitöltendő űrlap
- [ ] Az "1 sor módosítás" hands-on-t megcsinálta

## Összegző WOW (F3 zárás)

A 30 perces F3 végén Márton előtt:
- 1 db **eligibility riport** (pályázhatunk: igen, indoklással)
- 1 db **gap analysis** (23 melléklet, 6 piros, 11 sárga, 6 zöld)
- 1 db **Data Completion Board** (felelős-határidő tábla, kritikus út, kockázatok)
- 23 db **mentett TODO** a Productivity pluginben

Ez **3 nap munkája volt** klasszikusan. Itt **30 perc**.

És ami fontos: **másnap mindez ott lesz.**
