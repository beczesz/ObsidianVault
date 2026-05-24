---
title: 00_GAPS
generated_by: librarian v0.3
generated_at: 2026-05-11
scope: 02_Areas/Navigátor Podcast
mode: index
file_count: 214
id: f8970061-842d-46fc-8510-681ba130b2e0
index_schema_version: 1
---

# Navigátor Podcast — Gaps / Inconsistencies / Librarian Log

> Inkonzisztenciák, duplikációk, elavult fájlok, broken/feszült referenciák, scope-on kívüli kapcsolódások, librarian futás logja.

## 1. Verziókonfliktus: project state vs. claudemd vs. tényleges fájlok

| # | Probléma | Hely |
|---|----------|------|
| G1 | `CLAUDE.md` "Fontos fájlok" táblázat (sor 83-92) több Synthesis/ fájlt "❌ Újragenerálandó"-ként listáz (plan.md, channel.md, end_screen_plan.md, cards_and_pinned_comments_plan.md, synthesis_map.md, new_video_checklist.md) — **de mindegyik létezik a `Synthesis/` mappában.** | `CLAUDE.md:81-91` vs. ls `Synthesis/` |
| G2 | `01_PROJECT_STATE.md` v0.5 dátuma 2026-04-09 — azóta lezárult EP40 publikálás (2026-04-10), EP41 publikálás (2026-04-20), playlist audit (2026-04-11). State nincs frissítve. | `01_PROJECT_STATE.md:5,82` vs. `CLAUDE.md:99,113,118` |
| G3 | `01_PROJECT_STATE.md` "Utolsó kiadott epizód: EP41 – Eberlein Éva (szexuális nevelés), megjelent 2026-03-18" — de CLAUDE.md szerint EP39=Eberlein Éva (a 2026-04-08 EP-számozás korrekció után). EP41 = Gergely István / Fegyelem (2026-04-20). | `01_PROJECT_STATE.md:16` vs. `CLAUDE.md:97-100`, `Synthesis/synthesis_map.md:70` |
| G4 | `01_PROJECT_STATE.md` Last Updated szakaszt frissíteni — v0.6-ra emelendő, EP40+EP41 launch + EP-számozás korrekció reflektálva. | `01_PROJECT_STATE.md:81-83` |
| G5 | `Synthesis/szintézis.md` frontmatter "episodes_analyzed" csak 6 epizódot listáz (EP27 + EP14 + EP36 + EP37 + EP29 + EP28), de plan.md szerint 39 Gold Standard kész. A `szintézis.md` szándék szerint "folyamatosan bővül" — vagy frontmatter elmaradt, vagy a cross-ep szintézis valóban csak 6 epizódra épül. | `Synthesis/szintézis.md:5-12` vs. `Synthesis/plan.md:79` |

## 2. Duplikációk / törlendők (plan.md jelölte)

| # | Fájl | Megjegyzés | Forrás |
|---|------|-----------|--------|
| D1 | `**szintezis.md` (64 B üres placeholder, Synthesis/-ben) | Törlendő (plan.md jelölte). Megjegyzés: a `find` nem találta, lehet már törölve, vagy a `**` prefix tipo. | `Synthesis/plan.md:269` |
| D2 | `**Csatorna Audit Terv v0.1-v0.3.md` | Elavult verziók, csak v0.4 az aktív | `Synthesis/plan.md:270` |
| D3 | `**episode_roadmap.md` (9,183 B) | Elavult, plan.md-be olvadt | `Synthesis/plan.md:271` |
| D4 | `**EP41 - Eberlein Éva.md` (24,940 B) duplikátum — EP39 a helyes | `Synthesis/plan.md:272` |
| D5 | `WP39_Fegyelmezes_YouTube_Metadata.md` (6,354 B) ↔ `WP40_Fegyelmezes_YouTube_Metadata.md` (6,354 B, **byte-identikus méret**) — feltehető duplikátum/átnevezés szándék. `WP40_Final_YouTube_Metadata.md` (7,053 B) a végleges. | gyökér: `WP39_*` és `WP40_*` |
| D6 | `Episodes/Navigátor Podcast Plugin/EP41 - ChatGPT jegyzetek.md` ↔ `Episodes/Archive/EP41 - Fegyelem = szabadság/EP41 - ChatGPT jegyzetek.md` — két helyen szerepelhet ugyanaz a jegyzet (nem ellenőrzött tartalmilag). | listing |

## 3. Naming / strukturális inkonzisztencia

| # | Megfigyelés | Forrás |
|---|-------------|--------|
| N1 | `Synthesis/Csakabaj/Episodes/` fájl-elnevezés keverék: `CSAKABAJ_S01E21–E26_SYNTHESIS.md` (új formátum) + `EP01_*.md`–`EP51_*.md` (régi formátum) ugyanabban a mappában | `Synthesis/Csakabaj/Episodes/` |
| N2 | `prompts/Genreal.md` — feltehető tipo `General.md` helyett | `prompts/Genreal.md` |
| N3 | `Synthesis/Podcast/EP29 - Dr. Lőrinczi Kincső.md` szintézis fájlnév vs. `01_PROJECT_STATE.md:16` "EP41 – Eberlein Éva" tévedés (lásd G3) | — |
| N4 | EP-számozás-korrekció a YouTube címek alapján rögzítve `synthesis_map.md`-ban (átnevezés tábla sor 164-178), de az Episodes/Archive/ mappákban még a régi EP-számok láthatók (pl. `EP38 - Gál Ildikó - Örökbefogadás`, `EP39 - Gál Ildikó - Fegyelmezés 1`, `EP41 - Eberlein Éva`). | `Synthesis/synthesis_map.md:164-178`, `Episodes/Archive/` |

## 4. Csakabaj scope

| # | Megfigyelés | Hely |
|---|-------------|------|
| C1 | A `Synthesis/Csakabaj/` egy külön (Józsa Levi) podcast szintézis-archívuma (51 epizód) benchmark célból a Navigátor Podcast unit-on belül. Strukturálisan ide tartozik, de fogalmilag egy másik podcast. Megfontolandó dedikált sub-unit (`02_Areas/Csakabaj Podcast/`) vagy `03_Resources/` alá emelni. | `Synthesis/Csakabaj/` (51 ep fájl + map) |

## 5. Cross-scope references (csak naplózva, nem indexelve)

| # | Hivatkozás | Cél scope | Hely |
|---|-----------|-----------|------|
| X1 | `CLAUDE.md` hivatkozik a `00_Prompts/BDOS/agents/` mappára (librarian.md, plugin specifikációk) | `00_Prompts/` (vault root) | implicit (skill-rendszerből) |
| X2 | `.claude/` skill regisztrációk (`navigator-podcast:*` skillek) — 9+ skill | `.claude/` (vault root) | system reminder |
| X3 | `~/.youtube-mcp/` config (client_secret.json, token.json) | OS home, nem vault | `01_PROJECT_STATE.md:102` |
| X4 | Google Drive mappa link | extern | `CLAUDE.md:75`, `01_PROJECT_STATE.md:106` |
| X5 | YouTube Studio + Social Blade dashboardok | extern | `CLAUDE.md:76`, `Utils.md:3` |

## 6. Üres / minimal fájlok

| # | Fájl | Méret | Megjegyzés |
|---|------|-------|------------|
| M1 | `Küldetés.md` | 311 B | Csak misszió-rövid kivonat — duplikálja az `A Navigátor Podcast Alkotmánya.md` Misszió szakaszát |
| M2 | `Utils.md` | 329 B | 2 link + 2-elemű TODO (1 lezárt, 1 üres) |
| M3 | EP44 / EP45 epizód-mappák — felkészülés `01_PROJECT_STATE.md:43` szerint "üresek" | több | tartalmilag valójában meghívó+kérdés-szett van, de Gold Standard hiányzik |

## 7. Stale / lejárt

| # | Tétel | Lejárt | Hely |
|---|------|--------|------|
| L1 | Farkas Kinga (EP45 gyász) vendég felkérés | 2026-02-24 | `01_PROJECT_STATE.md:42`, `kanban.md` |
| L2 | Webinar feladat | 2026-03-24 | `01_PROJECT_STATE.md:42` |
| L3 | Patreon kampány (4 hetes, 2026 március–április) — lezárult, eredmény nem értékelt | 2026-04 | `Patreon/Patreon Kampányterv 2026.md`, `01_PROJECT_STATE.md:44` |

## 8. Librarian akciók logja

| Időpont | Akció | Részlet |
|---------|------|---------|
| 2026-05-11 | `index` futás | scope=`02_Areas/Navigátor Podcast/`, depth=FULL, include_archive=true (scoped futás). 214 md fájl szkennelve, 5 output fájl generálva a scope gyökerébe. Nem-md tartalom (pdf/docx/srt/png/zip) csak listing-szinten. |
| 2026-05-11 | Read | `librarian.md` v0.3 canonical, `CLAUDE.md`, `01_PROJECT_STATE.md`, `kanban.md`, `Utils.md`, `Küldetés.md`, `Alkotmánya.md`, `Synthesis/plan.md`, `Synthesis/synthesis_map.md`, `Synthesis/channel.md` (részben), `Synthesis/szintézis.md` (részben), `Synthesis/Snapshot/SNAPSHOT_RULES.md` (részben), `Synthesis/Csakabaj/synthesis_map.md` (részben), `memory/projects/navigator-podcast.md` (részben), `Patreon/Patreon Kampányterv 2026.md` (részben). |
| 2026-05-11 | Nincs módosítás | Index mód: csak Read + Write a 5 output fájlhoz. Tidy / Edit / törlés NEM történt. |
