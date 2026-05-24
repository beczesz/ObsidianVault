---
title: 00_GAPS
generated_by: librarian v0.5
generated_at: 2026-05-11T14:00:00
scope: 02_Areas/Ignis Academy/
mode: index
file_count: 33
id: c7ce6c87-c60c-49f5-a4ae-47ce8362f09d
index_schema_version: 1
---

# Gaps, Inconsistencies & Librarian Action Log

## Inkonzisztenciák

### Frontmatter / metaadat hiány
- **Nincs YAML frontmatter** a következő fájlokban (csak `Pályázat/00_README.md`, `Research/Research Areas.md`, és néhány fájl tartalmaz):
  - `CLAUDE.md`, `Business Development/*.md` (mind a 3), `Startup Learning/*.md` (mind a 4 md), `Research/Gondolat Satretól.md`, `Research/LLM és a bal agyfélteke.md`, `Research/Összegzése az eddigi beszélgetéseknek.md`, `Pályázat/03_meetings/*.md`, `Pályázat/08_partners-network/*.md`, `Pályázat/09_timeline-naplo/*.md`, `memory/*.md`
- Hiányzik a `status`, `version`, `last_updated` mező a legtöbb fájlból

### Üres / nagyon rövid fájlok (stub-jelleg)
- `Pályázat/01_status.md` — 1 sor, csak külső link a regiocentru.ro felé. Nem tartalmaz konkrét status snapshot-ot.
- `Pályázat/09_timeline-naplo/TODO.md` — 3 sor, kérdés-jellegű, már átfedés van TASKS.md-vel
- `Pályázat/08_partners-network/Szovetsegesek.md` — utolsó sor "TODO Miklós Erni" kontextus nélkül
- `Startup Learning/Decisions to consider.md` — fragment, befejezetlen mondatok ("2." nyitott)
- `Resources.md` — 4 sor, csak 2 link (Dani cikk + WEF)
- `Research/Gondolat Satretól.md` — 6 fragment-jellegű pont, nem koherens

### Mappa-struktúra anomáliák
- `Pályázat/04_decisions/` — README említi, fizikailag NEM létezik a fájlrendszerben
- `Pályázat/05_correspondence/` — README említi, fizikailag NEM létezik
- `Pályázat/06_*/`, `Pályázat/07_*/` — nincsenek (számozási hiány 03 → 08)
- `Pályázat/02_dokumentumok/` — csak 1 PDF, nincs index vagy summary

### Duplikáció / átfedés
- `Pályázat/08_partners-network/Networking.md` és `Szovetsegesek.md` — részben átfednek (Dani Erzsébet, Süket Csaba, Láng Máté, Bustya Attila, Kolumbán Sándor szerepel mindkettőben)
- CLAUDE.md People tábla és `memory/glossary.md` Nicknames szekció — duplikálják ugyanazokat a személyeket
- `Pályázat/09_timeline-naplo/TODO.md` és `TASKS.md` — TASKS.md tartalmazza a TODO.md kérdéseit is

### Tartalmi inkonzisztenciák
- BMC v2.3 dátum `2025-11-14`, de `version: 2.3` nincs explicit frontmatter-ben
- BMC `5.1.1.` említ "weekly active users" definíciót, NSM v2.4 "monthly active users" — időegység mismatch (BMC `Decisions to consider.md:8-10` még "weekly", NSM már "monthly")
- `LLM és a bal agyfélteke.md` — "Dr. Dani **Eszter**" (`Resources.md:1`) vs. "Dr. Dani **Erzsébet**" (mindenhol máshol). A PDF szerző hivatalosan: **Erzsebet Dani** — Resources.md elírást tartalmaz.

## Broken links / hiányzó hivatkozások

- `Pályázat/00_README.md:51` hivatkozik `../../../01_Projects/Szervezet fejlesztés/Veszprém - Kecskemét körút/` — vault-on belüli path validation szükséges (másik scope, nem ellenőrzött)
- `Pályázat/00_README.md:50` hivatkozik `../../ExarLabs/Stratégia/Stratégia 2026.md` — másik scope (nem ellenőrzött)
- `Pályázat/09_timeline-naplo/Startup_naplo.md:5` `[[2025.11.28 Contestare - meeting v1.1]]` — wikilink ütközés, tényleges fájl: `2025-11-28_Contestare_v1.1.md` (eltérő szóköz/aláhúzás konvenció)
- BMC v2.3 `:18` `[[North Star Metric - KPI - v.2.4]]` — wikilink, OK (létezik a fájl)
- `Resources.md` hivatkozik `[[WEF_Future_of_Jobs_Report_2025.pdf]]` — nem található sem a scope-ban, sem máshol vault-szerte (csak hivatkozásként szerepel BMC-ben is) → BROKEN

## Cross-references audit / retrieve flag

- **`ExarLabs/Stratégia/Stratégia 2026.md`** (külső scope) — hivatkozza ezt a pályázatot mint bevételi forrás. Retrieve audit javasolt: szinkronban van-e a 275k EUR számszerűsítésben.
- **`Veszprém-Kecskemét körút`** (külső scope, `01_Projects/Szervezet fejlesztés/`) — Dani Erzsébet partner-építés. Retrieve audit javasolt: tartalmaz-e Ignis Academy-vel kompatibilis follow-up-ot.
- **`02_Areas/Ignis/`** (testvér mappa) — AFM Electromobil tananyag. **DISTINCT egység: NEM része ennek a pályázatnak**, csak névhasonlóság. Confusion risk magas → CLAUDE.md-be explicit megjegyzés javasolt.

## Külső / törölt struktúra

- **`02_Areas/Pályázat/Ignis-Academy-EU-275k/`** — 1-2 órája létezett (cleanup verified by user), most NEM létezik. A pályázat-tartalom most az `Ignis Academy/Pályázat/` alatt van. **Cleanup verified: `02_Areas/Pályázat/` nem létezik a top level-en.**

## Új fájlok (2026-05-11 reorg)

- `Startup Learning/YC_B2B_Startup_Metrics.srt` (2576 sor) — új YC transcript
- `Startup Learning/YC_Bootstrap_vs_VC.srt` (1356 sor) — új YC transcript
- `Research/HB067WP15_Dani_HY-DE_Model.pdf` — Dr. Dani Erzsébet hivatalos HY-DE cikk
- `Pályázat/02_dokumentumok/DECIZIE_APROBARE_2025-11-06.pdf` — hivatalos ADRC scrisoare
- `Pályázat/00_README.md` és számozott alkönyvtárak (03_meetings, 08_partners-network, 09_timeline-naplo) — új struktúra

## Stale fájl gyanú

- Egyik md fájl sincs explicit `status: archived` címkével, de tartalmi szempontból:
  - `Pályázat/09_timeline-naplo/Startup_naplo.md` — utolsó bejegyzés 2025.12.01, ma 2026-05-11 → 5+ hónap óta nincs frissítve
  - `Business Development/BMC - Ignis Academy - v2.3.md` — 2025-11-14, fél éves
  - Számos Research fájl dátum nélkül

## Librarian action log

| Timestamp | Action | Mit / Hova |
|---|---|---|
| 2026-05-11T14:00:00 | index generálás | 5 fájl létrehozva a scope gyökerében (`00_INDEX.md`, `00_KNOWLEDGE_MAP.md`, `00_DECISIONS_INDEX.md`, `00_OPEN_QUESTIONS.md`, `00_GAPS.md`) |
| 2026-05-11T14:00:00 | PDF extract | `pdftotext` használva `DECIZIE_APROBARE_2025-11-06.pdf` és `HB067WP15_Dani_HY-DE_Model.pdf` első 80-100 sorára topic detection-höz |

## Javaslatok következő tidy / audit futamhoz

1. Frontmatter normalizálás minden md-re (`status`, `version`, `last_updated`)
2. `Resources.md` "Dani Eszter" → "Dani Erzsébet" javítás
3. `Resources.md` `[[WEF_Future_of_Jobs_Report_2025.pdf]]` broken link feloldása
4. `Pályázat/09_timeline-naplo/Startup_naplo.md:5` wikilink javítás (`2025-11-28_Contestare_v1.1`)
5. `Pályázat/09_timeline-naplo/TODO.md` merge → TASKS.md (átfedés)
6. `Networking.md` és `Szovetsegesek.md` deduplikálás vagy egyesítés
7. `Pályázat/04_decisions/` és `Pályázat/05_correspondence/` mappák létrehozása vagy README-ből eltávolítás
8. `02_Areas/Ignis/` vs. `02_Areas/Ignis Academy/` disambiguation note CLAUDE.md-be
9. BMC v2.3 frontmatter formalizálás
10. `Decisions to consider.md` befejezése vagy archive
