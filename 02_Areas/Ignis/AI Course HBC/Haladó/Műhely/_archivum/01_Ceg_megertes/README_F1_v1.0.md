# F1 — Rend a fájlok között (Káoszból rendszer)
**Időkeret:** 20-25 perc
**Fázis a workshopban:** 1/6 — a workshop első tapasztalata

## Narratív összefoglaló
**F1 = rend a fájlok között. F2 = rend a TODO-k között. F3 = rend a döntésben.**

Az első nap reggele. Márton kávéval fogad, lerakja a laptopot eléd:

> *"Ez lesz a géped. Rádobtam egy mappát mindennel ami van. Igazából fogalmam sincs mi van benne pontosan — anyám rakta össze. A jelszavakat felírtam egy cetlire, ott van a billentyűzet alatt. Csütörtökön lesz egy meeting egy pályázati tanácsadóval — valami AFM elektromos járműflotta pályázat. Tudnom kéne mi a helyzet a cégnél rendszer-szinten ahhoz hogy értelmes dolgokat mondjak neki. Ha tudsz AI-t használni, az plusz."*

Te megnyitod a `TransOffice/` mappát: **30+ fájl**, 5 ügyféllista, kéziratos cetlik, dupla szerződések, Ilona receptjei és unokafotója a „fontos dokumentumok" között.

Itt kezdődik a workshop **első tapasztalata**: az AI nem csak válaszol kérdésekre, hanem **átnéz egy egész fájlhalmazt egyszerre** és strukturált összefoglalót készít. És tudja menteni a kontextust egy `CLAUDE.md`-ben, ami a következő session-ben is élni fog.

## Tanulási célok

1. **Multi-file kezelés** — a Cowork egyszerre több tucat fájlt olvas és értelmez (Excel, docx, txt, PDF)
2. **CLAUDE.md koncepció** — az AI „hosszútávú memóriája" egy markdown fájlban
3. **Inkonzisztencia-felismerés** — a Cowork észreveszi ha 3 ügyféllista 3 különböző számot mutat
4. **AI mint kontextus-építő** — nem egyszeri lekérdezés, hanem perzisztens rendszer

## Feladatok

| # | Feladat | Idő | Output |
|---|---------|-----|--------|
| 1.1 | Cég-áttekintés Mártonnak (1-2 oldalas összefoglaló) | ~10-12p | `ceg_attekintes.md` |
| 1.2 | CLAUDE.md készítés (cégmemória) | ~8-10p | `CLAUDE.md` |
| 1.3 (bónusz) | Inkonzisztencia audit | (otthon) | `audit_inkonzisztenciak.md` |
| 1.4 (bónusz) | Ügyfél adategységesítés | (otthon) | egységes ügyféllista |
| 1.5 (bónusz) | Szerződéskockázat elemzés (BicoToner) | (otthon) | jogi kockázati riport |
| 1.6 (bónusz) | Pályázati one-pager | (otthon) | összefoglaló dokumentum |

A workshopon **csak F1.1 és F1.2** kerül sorra. A bónusz feladatok otthoni / haladó gyakorláshoz.

## Kulcs üzenet

A ChatGPT-ben minden új beszélgetés tiszta lap. A Cowork-ben a **CLAUDE.md egy állandó memória** — másnap, jövő héten is itt van a kontextus. Ez a különbség a tranzakció és a folyamat között.

## Delivery design

| Fázis | Ki | Mit | Idő |
|-------|-----|------|-----|
| WOW (1.1) | Te (demo) | Megmutatod ahogy a Cowork 30+ fájlt egyszerre átnéz, strukturált riportot készít | ~8p |
| MICRO HANDS-ON | Ők | Mindenki kiválaszt 3 fájlt és kér egy mini summary-t | ~5p |
| WOW (1.2) | Te (demo) | A `CLAUDE.md` készítés + új session megnyitása → kontextus megmarad | ~5p |
| FLOW tovább | Te | Átkötés F2-be: „A fájlok rendben vannak. De Márton most jött át — nem a fájlok a fő probléma, hanem hogy a meetingekből semmi nem marad meg." | ~2p |

## Átmenet F2-be

*"A fájlok rendben vannak. De Márton most jött át — nem a fájlok a fő probléma. A csütörtöki meetingen ki fog derülni: az a pályázat amit említett, már 2 hónapja a radarjuk alatt van, csak senkinek nem volt rá ideje rendesen ránézni. Most viszont a forrás kifut, és a meetingen Enikővel végre szóba kerül — kaotikusan, sok TODO-val."*

## Asset-ek

- `Tananyag/TransOffice/` mappa — a 30+ kaotikus fájl, ez a kiindulópont (rootban a Tananyag-ban)
- `Tananyag/00_Bevezetes/Ceg_leiras_TransOffice.md` — a fiktív cég teljes kontextusa (oktatói referencia)
