---
title: 00_GAPS
generated_by: librarian v0.5
generated_at: 2026-05-19T00:00:00
scope: 02_Areas/Fókuszpont
mode: index
id: d351a20f-0a74-45fe-99a1-e2604a579e7b
index_schema_version: 1
---

# 00_GAPS — Fókuszpont Referencia-archívum

## Struktúra-anomáliák

| # | Típus | Leírás | Fájl | Javaslat |
|---|-------|--------|------|----------|
| G1 | Elírás a fájlnévben | `Video scrip.md` — hiányzik a záró `t` a `script` szóból | `2025/Video scrip.md` | Átnevezés: `Video script.md` (tidy módban elvégezhető) |
| G2 | Frontmatter hiánya | Sem a 2024-es, sem a 2025-ös scriptfájlnak nincs YAML frontmatter (type, date, event, status, tags) | mindkét script | Frontmatter hozzáadása (tidy/normalize mód) |
| G3 | Hiányzó metaadat a dátumokról | A 2025-ös fájl két eseménydátumot említ (május 29. és június 18.) — nem egyértelmű, ez két külön előadás vagy egy esemény | `2025/Video scrip.md` l.15, l.33 | Szerkesztőtől tisztázandó |

## Hiányzó tartalom (GAP-ok)

| # | Hiány | Következmény |
|---|-------|-------------|
| G4 | Nincs 2023-as script | Nem tudjuk, volt-e Fókuszpont 2023-ban, vagy 2024 volt az első. A `01_PROJECT_STATE.md` "~2023 óta részt vesz" megjegyzi Szabolcs jelenlétét | Szerkesztőtől tisztázandó |
| G5 | Nincs kész videóra mutató link | A scriptekhez nem kapcsolódik sem YouTube-link, sem vault-fájl a kész videókról — a 2026-os projekt nem tudja összehasonlítani az előző évek kivitelezését | Hozzáadandó: `2024/finished_video_link.md` vagy frontmatter `youtube_id` mező |
| G6 | Nincs teljesítmény-adat a scriptekhez | A 2024/25-ös reeleknek mekkora volt a nézettségük, elérésük? Ez a 2026-os célcsatorna-döntéshez kritikus (vö. EP27 analitika, ahol a FB-dominancia kiderül) | Adatot hozni és dokumentálni |
| G7 | Hiányzó SRT / időzítés | A brainstorm_state.md (l.35–36, l.110) explicit várja a 2024/25-ös reel szövegét időzítéssel — a jelenlegi scriptfájlok csak szöveget tartalmaznak, nincs másodperces beosztás | SRT vagy időzített script hozzáadása a mappákba |

## Librarian akció-log

| Időpont | Akció | Mit | Miért |
|---------|-------|-----|-------|
| 2026-05-19 | WRITE | `00_INDEX.md` | Friss index generálva (2024/25 scriptek bekerültek) |
| 2026-05-19 | WRITE | `00_KNOWLEDGE_MAP.md` | Domaintérkép generálva |
| 2026-05-19 | WRITE | `00_DECISIONS_INDEX.md` | Implicit döntések kinyerve |
| 2026-05-19 | WRITE | `00_OPEN_QUESTIONS.md` | Nyitott kérdések kinyerve |
| 2026-05-19 | WRITE | `00_GAPS.md` | Ez a fájl |
