---
title: 00_GAPS
generated_by: librarian v0.5
generated_at: 2026-05-19T00:00:00
scope: 01_Projects/Fókuszpont 2026 — Rövidvideók
mode: index
id: f9d04944-f8f7-4e5c-8879-c26210d8b90e
index_schema_version: 1
---

# 00_GAPS — Fókuszpont 2026 Rövidvideók

## Struktúra-hiányok

| # | Típus | Leírás | Javaslat |
|---|-------|--------|----------|
| G1 | Hiányzó fájlok | `brief.md`, `scripts/`, `assets/`, `production/`, `post/` — a tervezett mappa-struktúra egyetlen eleme sem létezik még | Létrehozás a következő munkamenetben (project state tervezi) |
| G2 | Nincs kreatív brief | A forgatókönyvírás előtt szükséges célközönség / hang / üzenet / vizuál döntés — ez a `brief.md` tartalma | Brief workshop Barna atyával (Q1 után) |

## Tartalom-hiányok (GAP-ok)

| # | Hiány | Következmény | Forrás |
|---|-------|-------------|--------|
| G3 | SRT / időzítés hiánya a 2024/25-ös scriptekhez | A brainstorm_state.md (l.35–36, l.110) várta az időzített scripteket — a 2024/25-ös fájlok csak szöveget tartalmaznak, nincs másodperces beosztás. A Reel #1 időzítési tervénél (0-10mp / 10-20mp / 20-30mp) szükség lenne a korábbi reelekre mint kalibrálóra | SRT-k hozzáadása `02_Areas/Fókuszpont/` alá |
| G4 | Nincs "Reel #1 forgatókönyv v1" | A pipeline (brainstorm_state.md l.119) szerint ez a következő lépés — az SRT-k beérkezése után Claude API-val megírható | Következő munkamenet |
| G5 | Nincs "Reel #2 forgatókönyv v1" | Szintén pipeline következő lépés | Reel #1 után |
| G6 | Nincs videóteljesítmény-adat a korábbi reelekről | Nem tudjuk, melyik csatornán mekkora elérést generált a 2024/25-ös reel — a célcsatorna-döntés (Q3) vakon hozható csak meg enélkül | Adatot hozni; dokumentálni |
| G7 | Ignis brand-doksi hiánya | `01_PROJECT_STATE.md` hivatkozik rá ("Ignis brand (külön doksi TBD)"), de nem létezik a vaultban | Külön fájl vagy mappa szükséges |
| G8 | ChatGPT chat teljes szövege nem importálva | A brainstorm_state.md Raw Notes szekciójában csak 3 ChatGPT-válasz van — az összes fordulat importálva van-e? A forrás URL létezik, de a chat-folytatás veszhet | Ellenőrzés és archivál, ha hiányos |

## Inkonzisztenciák

| # | Inkonzisztencia | Forrás |
|---|----------------|--------|
| G9 | A brainstorm_state.md (l.35) azt írja "Szabolcs jelenleg tölti le" a tavalyi scripteket — most már megvannak a vaultban, de a `brainstorm_state.md` state nem frissítve | Szerkesztő frissítse a brainstorm_state.md "Source Material" szekcióját |
| G10 | Q5 (célközönség) nincs döntve, de a Reel #2 leírása ("fiatalok hívnak fiatalokat") már implicit dönt a fiatal célcsoport mellett | Explicit döntést dokumentálni a brief-ben |

## Librarian akció-log

| Időpont | Akció | Mit | Miért |
|---------|-------|-----|-------|
| 2026-05-19 | WRITE | `00_INDEX.md` | Projekt index generálva |
| 2026-05-19 | WRITE | `00_KNOWLEDGE_MAP.md` | Domaintérkép generálva |
| 2026-05-19 | WRITE | `00_DECISIONS_INDEX.md` | Döntések kinyerve (19 db) |
| 2026-05-19 | WRITE | `00_OPEN_QUESTIONS.md` | Nyitott kérdések kinyerve (14 db + leblokkolók) |
| 2026-05-19 | WRITE | `00_GAPS.md` | Ez a fájl |
