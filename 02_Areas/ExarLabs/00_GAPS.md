---
title: 00_GAPS
generated_by: librarian v0.3
generated_at: 2026-05-11
scope: 02_Areas/ExarLabs
mode: index
file_count: 48
id: 3ab113e3-420c-4e19-a56a-8ac40536ae60
index_schema_version: 1
---

# ExarLabs — Gaps, Inconsistencies, Cross-references

> A librarian csak flag-el, nem mozgat. Tidy mód külön hívással intézi.

## Cross-unit references (jelölés, NEM mozgatva)

Két ExarLabs-tematikájú fájl a Deák Húsüzlet unit alatt él. Tartalmilag az ExarLabs scope-ba illenének — de a hívó instrukciója szerint **nem mozgatjuk**, csak flag-eljük.

| Fájl (jelenlegi hely) | Tartalom | Javasolt új hely | Megjegyzés |
|---|---|---|---|
| `02_Areas/Deák Húsüzlet/memory/projects/exarlabs-strategia.md` | ExarLabs stratégia projektmemo | `02_Areas/ExarLabs/memory/projects/` vagy `Stratégia/` | A Deák unit memory-ban él, de ExarLabs scope-jellegű. |
| `02_Areas/Deák Húsüzlet/Business Development/strategy/24-month-roadmap.md` | 24 hónapos roadmap másolata/variánsa | `02_Areas/ExarLabs/Stratégia/` vagy `resources/Deák Platform/` | Lehet, hogy duplikál vagy variál a már meglévő ExarLabs verziókat (lásd duplikációk alább). Manuálisan ellenőrizendő. |

**Megjegyzés:** A felhasználó megjegyzése szerint "a legtisztább hely valószínűleg itt lenne" — de ez **review-ra vár**, librarian nem dönt.

## Duplikációk / lehetséges duplikációk

- **24 hónapos roadmap három példányban (legalább):**
  - `02_Areas/ExarLabs/Stratégia/24 honapos strategiai roadmap.md` (HU)
  - `02_Areas/ExarLabs/resources/Deák Platform/24-month-roadmap.md` (EN, v1.1, 2026-03-05)
  - `02_Areas/Deák Húsüzlet/Business Development/strategy/24-month-roadmap.md` (külső unit)
  — Egy a kanonikus? HU vs EN viszony? Variánsok-e vagy másolatok-e? Manuálisan összevetendő.

- **ExarLabs általános leírás vs. helyzetkép:**
  - `resources/ExarGroups/ExarLabs - általános leírás.md` (v0.1, 2026-03-04)
  - `Stratégia/Strategia.md` (v0.1, 2026-03-04) — szintén "kiindulási pont" leírás
  — Tartalmi átfedés gyanúja.

- **CLAUDE.md tartalmi átfedés** `memory/context/company.md`-vel — szándékos (memory pattern), nem hiba, csak jelzés.

## Hiányzó / sovány tartalom

- **`TASKS.md` (unit root) üres** — minden szekció üres.
- **`Anaf.md`** — 4 soros tartalmi stub, frontmatter nélkül, kontextus nélkül. Árva fájl-gyanús.
- **`memory/people/*.md`** — 10 fő, mindegyik 4-5 soros stub (név, role, level, company). Egyik sem tartalmaz történetet, kapcsolatokat, projektkötődést. Bővítendők.
- **`memory/glossary.md`** — minimális, 3 term.
- **`Clients/memory/glossary.md`** — "LTT" akronima `needs confirmation`.

## Frontmatter inkonzisztencia

- **Stratégia fájlok frontmatter:** `Stratégia/24 honapos strategiai roadmap.md` és `Stratégia/Strategia.md` (igen, ezek nem ugyanazok — utóbbi a 3 strat. opciós elemzés). HU roadmap **nincs** frontmatter; Strategia.md van.
- **`Anaf.md`** — nincs frontmatter.
- **`memory/people/*.md`** — nincs frontmatter, csak markdown header.
- **`CLAUDE.md`, `TASKS.md`** — nincs frontmatter (de ezek konvencióból szabad formátumúak).
- **`resources/Sonrisa-CPS/*.md`** — egyik fájlnak sincs frontmatter (BMC, Roadmap, Constitution, Strategy, Sonrisa general, CPS introduction).
- **`resources/Ignis - LMS/*.md`** — nincs frontmatter.
- **`resources/Media Műhely/*.md`** — nincs frontmatter.
- **`resources/Navigátor Podcast/Küldetés.md`** — speciális frontmatter (`significance` lista), nem szabványos.
- **`resources/Csapat és Kompetenciák/evaluation-guide.md`** — nincs frontmatter.

A `resources/ExarGroups/`, `resources/Szervezeti DNS/`, `resources/Deák Platform/`, `Stratégia/Stratégia 2026.md`, `Stratégia/Területek.md` mind rendelkeznek szabványos frontmatterrel — ez a minta a többi fájlra ki nem terjesztett.

## Bináris / nem-md fájlok (nem indexelhetők mélyen)

- `dashboard.html` (root + `Clients/` — két példány, érdemes md5-zel ellenőrizni byte-azonosság szempontjából)
- `general-utils.plugin` (root)
- `Clients/FedEx/*.docx`, `*.doc` (4 db szerződés)
- `.DS_Store` fájlok (root, `Stratégia/`, `Stratégia/resources/`, `resources/Ignis - LMS/`, `resources/`) — vault-hygiene szempontból törlendők (tidy mód)

## Üres mappák / kérdéses struktúra

- `Stratégia/resources/` — csak `.DS_Store`, érdemi tartalom nincs. Üres mappa.
- `resources/Sonrisa-CPS/` minőségileg ExarLabs-on belül lóg, miközben a Sonrisa szervezetileg független. Lehet, hogy `01_Projects/` vagy külön `02_Areas/Sonrisa/` mappa indokolt — de `00. Strategy.md` már hivatkozik `[[02_Areas/Sonrisa/CPS/...]]` belső linkre, ami **broken**: nincs ilyen mappa.

## Broken / lehetséges törött linkek

- `resources/Sonrisa-CPS/00. Strategy.md` — `[[02_Areas/Sonrisa/CPS/24_7 support]]`, `[[02_Areas/Sonrisa/CPS/Inference Farm]]`, `[[02_Areas/Sonrisa/CPS/CI_CD Managed Service]]`, `[[Low code automation]]` — cél fájlok nincsenek az ExarLabs scope-ban (és lehet, hogy globálisan sem).
- `resources/Ignis - LMS/North Star Metric - KPI - v.2.4.md` — `[[North Star Metric - KPI - v.2.4]]` önreferencia gyanú, ellenőrizendő.

## Librarian action log

- 2026-05-11: index futtatás — scope `02_Areas/ExarLabs/`, mode `index`, 5 fájl generálva (`00_INDEX.md`, `00_KNOWLEDGE_MAP.md`, `00_DECISIONS_INDEX.md`, `00_OPEN_QUESTIONS.md`, `00_GAPS.md`). Nem volt mozgatás vagy törlés. Cross-unit fájlok flagelve, nem érintve.
