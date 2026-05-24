---
title: 00_GAPS
generated_by: librarian v0.5
generated_at: 2026-05-22T10:00:00
scope: /Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/01_Projects/Gergely István
mode: index
file_count: 25
id: cb894bd4-47a2-48ba-8473-79dc63562ff6
index_schema_version: 1
---

# 00_GAPS — Gergely István projekt

> Inkonzisztenciák, struktúra-anomáliák, hiányzó linkek, adathiányok, Librarian akció-log.

---

## Struktúra-megjegyzések

### S-01 — Excel fájlok nem olvashatók Librarian által
- Az 5 forrásfájl (`.xlsx`) az elemzés kontextusában nem nyitható meg szövegként — tartalmuk kizárólag a szintézis markdown-okon keresztül érhető el.
- Következmény: az index a szintézisek leírásán alapul; ha az Excel tartalma és a szintézis eltér, az index torzít.
- Ajánlás: ha az Excel-ek frissülnek, a kapcsolódó szintézist is frissíteni kell.

### S-02 — Nincs CLAUDE.md a scope-ban
- A `Gergely István/` mappában nem található `CLAUDE.md` (projektszintű kontextus fájl).
- Következmény: agent-hívásokban nincs helyi override lehetőség.
- Ajánlás: ha a projekt folytatódik, érdemes `CLAUDE.md`-t létrehozni projekt-leírással és a tulajdonos kontaktjával.

### S-03 — .DS_Store jelen van
- Fájl: `Gergely István/.DS_Store`
- MacOS metafájl, nem tartalom. Nem indexelve.
- Ajánlás: `.gitignore` bővítése `.DS_Store` bejegyzéssel (ha git-en van a vault).

### S-04 — _build/ tartalmaz közbenső JSON fájlokat (v1)
- `_build/keszlet_holt.json` (109 KB) és `_build/keszlet_negativ.json` (31 KB) közbenső adatfájlok.
- Dokumentálva a `07_Dashboard_es_leszallitottak.md`-ben most már nincs explicit felsorolás róluk (csak "a három script újrafuttatásával" utalás).
- Megjegyzés: nem broken, csak dokumentáció szempontból implicit.

### S-05 — _build/ v1 és v2 pipeline párhuzamosan él
- A `_build/` tartalmaz mind v1 (`extract.py`, `make_dashboard.py`, `dashboard_data.json`), mind v2 (`extract_v2.py`, `make_dashboard_v2.py`, `data_v2.json`) fájlokat.
- Nincs README a `_build/` mappában, ami elmagyarázná melyik a "current" pipeline.
- Ajánlás: ha v2 a végleges, a v1 pipeline fájlokat érdemes `_build/v1_archive/`-ba mozgatni vagy README-vel dokumentálni a különbséget. (Nem blokkoló — a `07_Dashboard_es_leszallitottak.md` leírja a struktúrát.)

---

## Adathiányok (nem elérhetők a jelenlegi exportokból)

| # | Hiányzó adat | Következmény | Nyitott kérdés | Adatkérő pont |
|---|---|---|---|---|
| D-01 | Partner × idő kereszttábla (számlaszintű) | Melyik vevő felelős a novemberi mélypontért; partnerenkénti profit | F-07 | #2 |
| D-02 | Cikkszintű árrés (cikk → kategória mapping, pontos) | Besorolás csak ~74%-os; polc-optimalizálás korlátozott | F-05 | #3 |
| D-03 | Gestiune-szintű Adaos bontás (telephely-árrés) | Melyik bolt mennyire jövedelmező — jelenleg nem számolható | F-06 | #1 (legfontosabb) |
| D-04 | Gestiune-közi áthelyezések (belső mozgás) | Az Intrari pontossága bizonytalan | F-01 | — |
| D-05 | Személyzet, bérleti, rezsi adatok | Bruttó árrés ismert, nettó nyereség nem számítható | — | — |
| D-06 | Cikk × telephely értékesítési adat (pontos) | Teljes drill-down (cikk × gestiune × árrés) nem lehetséges | — | #4 (opcionális) |

---

## Belső konzisztencia-ellenőrzések

| # | Ellenőrzés | Eredmény |
|---|---|---|
| C-01 | ZGY összesen (695 612) ≈ P2025 összesen (696 177) | OK — 0,08% eltérés, kerekítési ok |
| C-02 | GERDIT összes számla (3 048) vs. P2025 számlák (3 499) | ELTÉRÉS — 451 db különbség; magyarázat: GERDIT minden csatornát tartalmaz (kasszás + számlás), P2025 csak a számlás csatornát |
| C-03 | Adaos kasszás + P2025 B2B ≈ GERDIT összes | OK — 5 624 640 vs. 5 623 663 RON; eltérés −977 lej (0,017%); GERDIT = eladás IGAZOLVA |
| C-04 | PTOT azonosság: Stoc final = Stoc initial + Intrari − Iesiri | Nem ellenőrizhető tételszinten (Excel nem olvasható); szintézis szerint igazolt |
| C-05 | Meta-kategória összesen ≈ Adaos kasszás forgalom | Közelítő — ~74% lefedettség; a maradék ~26% "besorolatlan" (nem jelenik meg a meta-kategóriákban) |

---

## Broken linkek / wikilink-ellenőrzés

A szintézisekben lévő `[[wikilink]]`-ek:

| Link | Forrás fájl | Cél | Állapot |
|---|---|---|---|
| `[[02_ZGY_partnerek]]` | 00_Attekintes.md | Szintezisek/02_ZGY_partnerek.md | OK |
| `[[04_P2025_szamla_profit]]` | 00_Attekintes.md | Szintezisek/04_P2025_szamla_profit.md | OK |
| `[[05_GERDIT_szamlaregiszter]]` | 00_Attekintes.md | Szintezisek/05_GERDIT_szamlaregiszter.md | OK |
| `[[01_PTOT_keszletmozgas]]` | 00_Attekintes.md | Szintezisek/01_PTOT_keszletmozgas.md | OK |
| `[[03_Adaos_arres]]` | 00_Attekintes.md | Szintezisek/03_Adaos_arres.md | OK |
| `[[03_Adaos_arres]]` | 01_PTOT_keszletmozgas.md | Szintezisek/03_Adaos_arres.md | OK |
| `[[05_GERDIT_szamlaregiszter]]` | 01_PTOT_keszletmozgas.md | Szintezisek/05_GERDIT_szamlaregiszter.md | OK |
| `[[00_Attekintes]]` | 01_PTOT_keszletmozgas.md | Szintezisek/00_Attekintes.md | OK |
| `[[04_P2025_szamla_profit]]` | 02_ZGY_partnerek.md | Szintezisek/04_P2025_szamla_profit.md | OK |
| `[[00_Attekintes]]` | 02_ZGY_partnerek.md | Szintezisek/00_Attekintes.md | OK |
| `[[00_Attekintes]]` | 03_Adaos_arres.md | Szintezisek/00_Attekintes.md | OK |
| `[[01_PTOT_keszletmozgas]]` | 03_Adaos_arres.md | Szintezisek/01_PTOT_keszletmozgas.md | OK |
| `[[02_ZGY_partnerek]]` | 04_P2025_szamla_profit.md | Szintezisek/02_ZGY_partnerek.md | OK |
| `[[05_GERDIT_szamlaregiszter]]` | 04_P2025_szamla_profit.md | Szintezisek/05_GERDIT_szamlaregiszter.md | OK |
| `[[00_Attekintes]]` | 04_P2025_szamla_profit.md | Szintezisek/00_Attekintes.md | OK |
| `[[00_Attekintes]]` | 05_GERDIT_szamlaregiszter.md | Szintezisek/00_Attekintes.md | OK |
| `[[01_PTOT_keszletmozgas]]` | 05_GERDIT_szamlaregiszter.md | Szintezisek/01_PTOT_keszletmozgas.md | OK |
| `[[04_P2025_szamla_profit]]` | 05_GERDIT_szamlaregiszter.md | Szintezisek/04_P2025_szamla_profit.md | OK |
| `[[05_GERDIT_szamlaregiszter]]` | 06_Tovabbi_felismeresek.md | Szintezisek/05_GERDIT_szamlaregiszter.md | OK |
| `[[02_ZGY_partnerek]]` | 06_Tovabbi_felismeresek.md | Szintezisek/02_ZGY_partnerek.md | OK |
| `[[03_Adaos_arres]]` | 06_Tovabbi_felismeresek.md | Szintezisek/03_Adaos_arres.md | OK |
| `[[01_PTOT_keszletmozgas]]` | 06_Tovabbi_felismeresek.md | Szintezisek/01_PTOT_keszletmozgas.md | OK |
| `[[00_Attekintes]]` | 06_Tovabbi_felismeresek.md | Szintezisek/00_Attekintes.md | OK |
| `[[00_Attekintes]]` | 07_Dashboard_es_leszallitottak.md | Szintezisek/00_Attekintes.md | OK |
| `[[06_Tovabbi_felismeresek]]` | 07_Dashboard_es_leszallitottak.md | Szintezisek/06_Tovabbi_felismeresek.md | OK |
| `[[07_Dashboard_es_leszallitottak]]` | 08_Adatkero_lista.md | Szintezisek/07_Dashboard_es_leszallitottak.md | OK |
| `[[00_Attekintes]]` | 08_Adatkero_lista.md | Szintezisek/00_Attekintes.md | OK |

> Minden wikilink feloldható — nincs broken link.

---

## Librarian akció-log

| Időpont | Akció | Mit | Miért |
|---|---|---|---|
| 2026-05-21 | WRITE | `00_INDEX.md` | Index mód 1. futás, scope: Gergely István |
| 2026-05-21 | WRITE | `00_KNOWLEDGE_MAP.md` | Index mód 1. futás |
| 2026-05-21 | WRITE | `00_DECISIONS_INDEX.md` | Index mód 1. futás |
| 2026-05-21 | WRITE | `00_OPEN_QUESTIONS.md` | Index mód 1. futás |
| 2026-05-21 | WRITE | `00_GAPS.md` | Index mód 1. futás |
| 2026-05-22 | OVERWRITE | `00_INDEX.md` | Index mód frissítés — +06, +07 szintézis, +Dashboard_2025.html, +Keszlet_problemak_2025.xlsx, +_build/ pipeline; file_count: 11→21 |
| 2026-05-22 | OVERWRITE | `00_KNOWLEDGE_MAP.md` | Adatfolyam kibővítve _build pipeline-nal; GERDIT=eladás igazolva; szezonalitás kettéválás hozzáadva |
| 2026-05-22 | OVERWRITE | `00_DECISIONS_INDEX.md` | É-01 lezárva (GERDIT=eladás megoldva); M-05 frissítve szezonalitás pontosítással |
| 2026-05-22 | OVERWRITE | `00_OPEN_QUESTIONS.md` | K-01 lezárva; F-05, F-06, F-07 hozzáadva (07-es szintézis alapján) |
| 2026-05-22 | OVERWRITE | `00_GAPS.md` | S-04 hozzáadva (_build JSON-ok); C-02 és C-03 frissítve; wikilink tábla kibővítve 06, 07 linkekkel |
| 2026-05-22 | OVERWRITE | `00_INDEX.md` | Index mód frissítés — +08_Adatkero_lista, +_build v2 fájlok (extract_v2, make_dashboard_v2, data_v2), meta-kategória táblázat, file_count: 21→25 |
| 2026-05-22 | OVERWRITE | `00_KNOWLEDGE_MAP.md` | Meta-kategóriák (valós érték, ~74% lefedettség), heti ritmus (kedd+péntek), szortiment (140/2496 cikk), ELV tervezési alapelv, v2 pipeline ág hozzáadva; 08_Adatkero_lista cross-ref |
| 2026-05-22 | OVERWRITE | `00_DECISIONS_INDEX.md` | M-06 (kulcsszavas kategorizálás ~74%), M-07 (ELV: ne becsülj semmit), É-03 (gestiune-profit nyitott) hozzáadva |
| 2026-05-22 | OVERWRITE | `00_OPEN_QUESTIONS.md` | F-05/F-06/F-07 adatkérő-hivatkozásokkal frissítve; A-05 (Egyéb/technikai 68,7%) hozzáadva |
| 2026-05-22 | OVERWRITE | `00_GAPS.md` | S-05 (_build v1/v2 párhuzam), D-06 (cikk×telephely adat), C-05 (meta-kategória lefedettség), 08-as wikilink-ek hozzáadva |
