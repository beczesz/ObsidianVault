---
name: episode-prep-v0.3
description: >
  A Navigátor Podcast epizód-előkészítési workflow-ja. Használd, amikor
  "meghívó", "felkészülési kérdések", "epizód előkészítés", "vendég dokumentumok",
  "meghívólevél", "podcast előkészítés", vagy "EP előkészítés" témában
  kap feladatot a felhasználó. A v0.3 verzió cross-referencia képességgel rendelkezik:
  ha a vendég vagy téma korábban már szerepelt, automatikusan hivatkozik a korábbi
  epizód szintézisére és teljesítményére.
version: 0.3.0
id: 1511ad30-f7e2-4641-9137-5399756bfbb6
index_schema_version: 1
---

# Navigátor Podcast — Epizód előkészítési kontextus (v0.3)

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

---

## v0.3 — Cross-referencia képesség

### Mikor és hogyan használd

Amikor epizódot készítesz elő, **nézd meg a Synthesis/ mappát**: van-e korábbi epizód
ugyanazzal a vendéggel vagy hasonló témával. Ha igen, használd a szintézis adatait
a felkészülési kérdések gazdagítására.

### Lépések

1. Keresd meg a Synthesis/Podcast/ és Synthesis/Series/ mappákat
2. Ha a vendég korábban szerepelt (pl. Bencze Edit: EP06, EP14, EP28):
   - Olvasd be a korábbi szintézist
   - Hivatkozz a korábbi epizód legérdekesebb pontjaira a kérdésekben
   - Pl.: „A korábbi beszélgetésünkben X témát érintettük — azóta változott-e a véleményed?"
3. Ha a téma korábban felmerült más vendéggel:
   - Pl.: AI-témában EP17, EP18, EP31, EP32 → ezekből konkrét ellenpont-kérdéseket generálhatsz
4. A meghívólevélben hivatkozz a vendég korábbi epizódjára (ha volt), mint a kapcsolat bizonyítéka

### Példa cross-referenciára

```
Vendég: Bencze Edit (EP47 – új téma: szorongás)
Korábbi epizódok: EP06 (4,800 views), EP14 (72,236 views), EP28 (12,483 views)

Felkészülési kérdés javaslatba beépítve:
→ „Az EP14-es beszélgetésünk a nárcizmusról a csatornánk legnézettebb videója lett
   (72K+ megtekintés). Az akkori beszélgetésben felmerült, hogy a szorongás és a
   nárcisztikus kapcsolatok összefonódnak. Hogyan látod ezt ma?"
```

Ez a cross-referencia nemcsak a felkészülést gazdagítja, hanem a későbbi metadata
generálásnál is erős hook-anyagot ad (sorozat-hatás = magasabb end-screen CTR).
