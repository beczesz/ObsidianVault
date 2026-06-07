---
title: "Jelen Cowork session összefoglaló"
date: 2026-05-12
author: Becze Szabolcs
status: active
description: "Egy 4 órás Claude Cowork workshop részletes előkészítése: TransOffice Trade SRL fiktív cégre épülő szimulációs tananyag (27 fájl), hat fázis feladatleírása, szállítási design és bevezető/zárás scriptjei. Projektvezetők és tananyag-fejlesztők számára."
description_source: auto
description_hash: ac9e43c36f9ee602
id: 632f7c08-b1bf-4199-ac51-96a9898e5857
index_schema_version: 1
bdos_index: true
---
# Jelen Cowork session összefoglaló

> Utolsó frissítés: 2026-05-06

---

## Amit ebben a Cowork session-ben csináltunk

### 1. Logisztika & előfeltételek kidolgozása
- Claude Pro pricing kutatás ($20/hó, azonnali lemondás = 1 hónap hozzáférés)
- Guest Pass nem skálázható (3x 7 nap per Max account)
- Kvóta: ~45 üzenet / 5 órás ablak (4 órás kurzushoz elegendő)
- Részletes dokumentáció: `01_Logisztika és előfeltételek.md`

### 2. TransOffice Trade SRL fiktív cég
- Teljes cégleírás: `Tananyag/00_Bevezetes/Ceg_leiras_TransOffice.md`
- Székelyudvarhely, generációváltás, 12 alkalmazott
- B2B irodai kellékek kereskedelme

### 3. Szimulációs fájlok generálása (27 db)
- 3 Excel ügyféllisták (eltérő névvariánsokkal, hiányzó adatokkal)
- Árlista (elavult 2023), rendelésnapló (megállt 2024 okt), készlet (3 hónapos)
- 2 szerződés (PaperWorld = normál, BicoToner = 6 rejtett probléma)
- Meeting jegyzet (kaotikus), emailek (5 típus), Ilona személyes fájljai (zaj)
- Mappa: `Tananyag/TransOffice/`

### 4. Fázis 1 feladatleírások (F1.1–F1.6)
- F1.1: Core — Rendszeráttekintés pályázati meeting-re
- F1.2: Core — CLAUDE.md készítés (context persistence)
- F1.3: Bónusz — Inkonzisztencia audit
- F1.4: Bónusz — Ügyfél adategységesítés
- F1.5: Bónusz — Szerződéskockázat elemzés (BicoToner)
- F1.6: Bónusz — Pályázati one-pager
- Mappa: `Tananyag/01_Ceg_megertes/`

### 5. ChatGPT konverzáció szintézis (v0.2)
- Teljes konverzáció újra-feldolgozva (2026-05-06)
- Új tartalom átvéve:
  - Bevezető script (finomított, 8 blokkos, használható)
  - Zárás script (7 blokkos, használható)
  - Részletes időzítés (240 perc / 4 óra, szünetekkel)
  - Per-task bontás (tanulás, sub-flow, output)
  - Delivery design arányok (40% demo / 30% közös / 30% ők)
  - Kockázatok és megoldások
  - Metaforák és paradigmaváltás analógiák
  - Claude Cowork elnevezés / branding
  - Narratív PDF összefoglaló (vezetőknek)

---

## Jelenlegi állapot

### Kész
- [x] Logisztika & előfeltételek
- [x] Cég leírás (TransOffice Trade SRL)
- [x] 27 szimulációs fájl
- [x] Fázis 1 feladatleírások (6 db)
- [x] ChatGPT szintézis v0.2 (teljes)
- [x] Bevezető script
- [x] Zárás script
- [x] Időzítés (4 óra)

### Következő
- [ ] Fázis 2 kidolgozás: meeting transcript + productivity plugin
- [ ] Fázis 3 kidolgozás: adatelemzés + döntéshozatal
- [ ] Fázis 4 kidolgozás: kommunikáció + legal plugin
- [ ] Fázis 5 kidolgozás: pályázat beadás + automation
- [ ] Fázis 6 kidolgozás: web redesign
- [ ] Prompt library
- [ ] Delivery design finomhangolás (mi demo, mi hands-on, mi homework)
- [ ] Asset-ek gyártása (meeting transcript, pályázati form, rossz weboldal)


---

## Session 3 (2026-05-07) — ChatGPT v0.3 tartalom kinyerés

### Mi történt
- Újra végigolvastuk a ChatGPT beszélgetést (az Executive PDF generálás utáni rész)
- Szabolcs egy mély filozófiai blokkot írt az eszterga metaforáról és az AI mint operációs rendszer koncepcióról
- ChatGPT részletesen kidolgozta az ipari forradalom párhuzamot
- Radikálisan megváltozott a delivery design: 40/30/30 → **70/20/10**
- Új pedagógiai modell: "Narrated Live Experience" + checkpoint pedagógia

### Új fájl
- `05_ChatGPT szintézis v0.3 - Filozófia és delivery.md` (230 sor)

### Kinyert új tartalom
1. **Eszterga metafora** — mély analógia (gőzgép vs szerszámgép = ChatGPT vs Cowork)
2. **Ipari forradalom párhuzam táblázat** (1698-1800 vs 2010-2026)
3. **OS analógia** (memória=markdown KB, file system=local folders, stb.)
4. **Delivery design 70/20/10** — felülírja a korábbi 40/30/30-at
5. **"Narrated Live Experience"** formátum — Apple keynote, nem IT tréning
6. **Checkpoint pedagógia** — háromfázisú ritmus (WOW → MICRO HANDS-ON → FLOW)
7. **MUST HAVE hands-on lista** (5 pont: prompt, meeting, Excel, form, web)
8. **F1 mikro-koreográfia** (8 perc demo + 5 perc hands-on + 2 perc flow)
9. **Összehúzhatóság** — akár 2-2.5 óra is elég lehet
10. **Pozicionálás** — "guided future experience", nem kurzus

### Frissítve
- 02_ChatGPT szintézis v0.2: delivery design arányoknál cross-reference a v0.3-ra

### Session 3 folytatás (2026-05-07, délután)
**F2 — Meeting feldolgozás kidolgozása**

Elkészült:
1. **`meetings/` mappa** létrehozva a `TransOffice/` alatt
2. **`meeting_transcript_20250224.md`** — Teljes, 12 perces meeting transcript (127 sor)
   - Résztvevők: Márton, Enikő, Attila
   - Témák: papírkészlet, PaperWorld áremelés, BicoToner szerződés, email káosz, leltár, AI kurzus
   - Tudatosan a korábbi meeting jegyzetekre épül (visszatérő témák)
3. Korábbi meeting docx fájlok bemásolva a meetings/ mappába
4. **Feladat_2.1** — Meeting transcript feldolgozása (transcript → summary + to-do + kockázatok)
5. **Feladat_2.2** — Meeting-ek összehasonlítása (cross-document elemzés, trendek, pattern recognition)
6. **Feladat_2.3** — Follow-up email és action items (végrehajtható output generálás)
7. **README_F2.md** — F2 fázis összefoglaló (delivery design, checkpoint ritmus, átmenet F3-ba)

A transcript úgy van megírva, hogy:
- Természetes beszédstílus (hezitálás, félbeszakítás, humor)
- Visszahivatkozik korábbi meeting témáira (continuity)
- Tartalmaz: döntéseket, to-do-kat, nyitott kérdéseket, kockázatokat, dependency-ket
- Érett az AI feldolgozásra (elég komplex, hogy a strukturálás valódi értéket adjon)
