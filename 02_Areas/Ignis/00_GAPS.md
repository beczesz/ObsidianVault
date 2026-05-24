---
title: 00_GAPS
generated_by: librarian v0.3
generated_at: 2026-05-11T00:00:00
scope: 02_Areas/Ignis/
mode: index
file_count: 144
id: ddadae06-7f13-48db-8d23-b8c683f82ce7
index_schema_version: 1
---

# 00_GAPS — Ignis inkonzisztenciák, hiányok, librarian-log

## G1 — Frontmatter teljes hiánya
**Megfigyelés:** A scope-on belüli markdown fájlok **gyakorlatilag egyikében sincs** YAML frontmatter (`title`, `status`, `version`, `created`, `updated`). Egyetlen fájl sem követi a vault frontmatter konvencióját.
**Hatás:** retrieve mód frontmatter-szűrés (`status`, `date`, `version`) nem alkalmazható erre a scope-ra.
**Akció:** audit-frontmatter-normalize futtatás javasolt (külön mód).

## G2 — Duplikált webinar_presentation.pptx
**Megfigyelés:** `AI Kurzus/webinar_presentation.pptx` és `AI Kurzus/presentation/webinar_presentation.pptx` egyaránt létezik.
**Akció (javaslat):** md5 check → ha azonos, tidy módban byte-azonos törlés a gyökérben (a `presentation/` mappa logikusabb hely).

## G3 — Cross-reference scope-on kívüli "Ignis Academy" unit-tal
**Megfigyelés:** A vault egy különálló helyén létezik egy "Ignis Academy" unit (~22 fájl) — feltehetően a `Haladó AI Workshop` tananyag egy korábbi/párhuzamos formátuma vagy szélesebb akadémia-keret.
**Bizonytalanság:** Nem volt felmérve ebben a scoped futásban. Lehetséges:
- (a) korábbi v0 a Haladó-tananyagnak → mergelni kellene
- (b) szélesebb akadémia-keret, amelyben a Haladó egy konkrét workshop → tier-2 csatolás kellene
- (c) elavult, archiválható tartalom
**Akció:** globális indexelés szükséges, hogy mindkettő tier-2 indexe összehasonlítható legyen.

## G4 — Üres/csonk tartalom: `AI Haladó Felhasználás.md`
**Megfigyelés:** A fájl deklarálja a 4-dimenzió struktúrát és a tipp-struktúrát (`Cím | Dimenzió | Alapelv | Leírás | Példa`), de a 4 dimenzió szekciói (Ethos/Logos/Pathos/Thelos) üresek (csak fejlécek).
**Akció:** content gap — vagy tartalmilag feltölteni, vagy átnevezni "Template"-re.

## G5 — Üres/csonk tartalom: `EP42 - AI Tips 2.md`
**Megfigyelés:** A bevezető és a "Tippek" struktúra megvan, de a konkrét tippek (1-4 dimenzió blokkok L36-tól) nincsenek kitöltve.
**Akció:** content gap.

## G6 — Rendszer fájlok / nem-tartalom
**Megfigyelés:** Az alábbi rendszer/temporary fájlok jelen vannak a scope-ban:
- `AI Kurzus/.DS_Store` (egyenes-mappa)
- `AI Kurzus/presentation/lu44629dnh.tmp`
- `Tananyag/01_Ceg_megertes/TransOffice_Admin/lu45pmb3.tmp`
- `Tananyag/01_Ceg_megertes/TransOffice_Admin/.~lock.szerzodes_PaperWorld_2021.pdf#` (LibreOffice lock — feltehetőleg árva)
- (csak `Ignis/` gyökérben volt `.DS_Store`)

**Akció:** tidy módban törölhetők. A `.~lock.` fájl csak akkor árva, ha senki nem nyitotta a dokumentumot — ellenőrzendő.

## G7 — Szándékos kaosz (FALSE POSITIVE figyelmeztetés)
**Megfigyelés:** A `Tananyag/01_Ceg_megertes/TransOffice_Admin/` mappa **szándékosan kaotikus** (27+ fájl, többszörös verziók, Ilona privát fájlok mint `receptek_krumplis.docx`, `foto_unoka_2023.txt`, `jelszavak.txt`). Ez a workshop F1 asset-je.
**Akció:** **TILOS** tidy/audit módban "rendrakni" — ez integráns tananyag.

## G8 — `_DEPRECATED_AFM_Electromobil_v1.md`
**Megfigyelés:** Önmegjelölő deprecated fájl: `Tananyag/03_Dontes_Elemzes/Palyazat_kiiras/_DEPRECATED_AFM_Electromobil_v1.md`. Mellette él a felváltó `Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md` (94 oldal).
**Akció:** törlés-jelölt vagy archive-ba mozgatás javasolt (tidy mode).

## G9 — Két párhuzamos memory-térkép
**Megfigyelés:** Az `AI Kurzus/CLAUDE.md` és `AI Kurzus/memory/projects/ai-kurzus-webinar.md` átfedő tartalmat hordoznak (people, dates, deliverables). Nem teljes duplikáció, de kockázat, hogy frissítéskor szétdrifteljen.
**Akció:** szerkezeti döntés szükséges — egyik a kanonikus, másik view, vagy összevonni.

## G10 — `Kovacs_Ilona/szamlak_2023/README.txt`
**Megfigyelés:** Egy mély-fészekben (TransOffice_Admin/Kovacs_Ilona/szamlak_2023/) egyetlen README.txt — a `szamlak_2023/` mappa tartalma egyébként nincs listázva. Lehet, hogy üres mappát jelez vagy beolvasási korlát miatt nem látszott.
**Akció:** ellenőrzendő — ha üres mappa, vagy szándékos workshop-asset, vagy tisztítandó.

## G11 — Tananyag/Haladó/Tananyag/README.md tartalom ismeretlen
**Megfigyelés:** A `Haladó/Tananyag/README.md` fájl létezik, de tartalmát ebben a futásban nem olvastam végig (méret/relevance miatt). Lehet, hogy ez egy szerepelt entry point.
**Akció:** retrieve módban olvasandó, ha workshop-tartalmi query érkezik.

---

## Librarian-akció log (ezen futás)

| Időpont | Akció | Cél |
|---|---|---|
| 2026-05-11 | index mód, scoped futás | `02_Areas/Ignis/` — 5 tier-2 indexfájl generálva |
| 2026-05-11 | NEM nyúltam tartalomhoz | csak olvasás + 5 indexfájl írása |
| 2026-05-11 | scope kívüli "Ignis Academy" — flag (G3) | nem érintettem |

**Megjegyzés:** Ez a futás `index` mód volt. Tidy/audit akciók (törlés, mozgatás, frontmatter-fix) **NEM** történtek — külön hívás szükséges.
