---
name: episode-prep
description: >
  A Navigátor Podcast epizód-előkészítési workflow-ja. Használd, amikor
  "meghívó", "felkészülési kérdések", "epizód előkészítés", "vendég dokumentumok",
  "meghívólevél", "podcast előkészítés", vagy "EP előkészítés" témában
  kap feladatot a felhasználó.
version: 0.2.0
id: 22112ee5-81de-4e80-98ce-9d3d7a81f016
index_schema_version: 1
---

# Navigátor Podcast — Epizód előkészítési kontextus

## Workflow áttekintése

Minden epizódhoz két fő dokumentumot kell előkészíteni:

1. **Meghívólevél** (.docx + .pdf) — a vendégnek küldendő személyes meghívó
2. **Felkészülési kérdések** (.docx + .pdf) — részletes kérdéssor a felvétel előtt

## Szükséges adatok minden epizódhoz

| Adat | Leírás |
|------|--------|
| `EP_SZAM` | Epizód száma (pl. 45) |
| `VENDEG_NEV` | Vendég teljes neve (pl. Kovács János) |
| `VENDEG_MEGSZOLITAS` | Keresztnév (pl. János) |
| `EP_TEMA` | Epizód témája röviden |
| `EP_DIR` | Epizód mappa elérési útja |
| `OUTPUT` | Kimeneti fájl neve |

## Állandó adatok

| Adat | Érték |
|------|-------|
| Kérdőív URL | `https://forms.gle/DHhrhskNd7KXRkgG6` |
| Helyszín | Média Műhely |
| Google Drive mappa ID | `1nurxaGUjqgWAdIGuyoLesaPzawqCWJpx` |
| Template Drive ID | `1XHLMOpg4T079rDLk8baO9lqe-4_q_zwY` |
| Template Drive URL | `https://docs.google.com/document/d/1XHLMOpg4T079rDLk8baO9lqe-4_q_zwY/edit` |

## Scripts

A generáló scriptek a plugin `scripts/` mappájában találhatók:

- `create_meghivo.js` — meghívólevél .docx generátor
- `create_kerdesek2.js` — felkészülési kérdések .docx generátor
- `create_meghivo_template.js` — template .docx újrageneráláshoz

## Technikai követelmények

- **docx npm csomag** szükséges: `npm install docx`
- **LibreOffice** szükséges PDF-hez: `libreoffice --headless --convert-to pdf`
- JS fájlokat **heredoc**-kal írj bash-ből (encoding hibák elkerülése)
- Magyar `„"` idézőjelek: `\u201E` / `\u201D` JS-ben
- Hiperhivatkozáshoz `ExternalHyperlink` kell (sima TextRun nem elég)

## Jocko-idézetek

Az epizód mappájában találhatók a Jocko fordítás fájlok (`#1 - ?.md` ... `#9 - ?.md`).
Ezeket a `create_kerdesek2.js` script olvassa be a felkészülési kérdésekhez.
