# Changelog

A Navigator Podcast Plugin változásainak naplója.
A formátum a [Keep a Changelog](https://keepachangelog.com/hu/1.0.0/) alapján készült,
a verziózás a [Semantic Versioning](https://semver.org/) elveit követi.

---

## [0.2.0] – 2026-03-15

### Hozzáadva

- `/meghivo` command: epizód előkészítés (meghívólevél + felkészülési kérdések generálás)
- `episode-prep` skill: epizód-előkészítési workflow, állandó adatok, script útmutató
- `scripts/` mappa: `create_meghivo.js`, `create_kerdesek2.js`, `create_meghivo_template.js`
- Meghívó TEMPLATE.docx sablon

### Módosítva

- `navigator-context` skill verziója 0.1.0 -> 0.2.0
- README.md frissítve az új functionalities-szel

### Konszolidált

- `navigator-plugin` és `navigator-plugin (1)` (azonos tartalmú duplikátumok) összevonva
- `Navigátor Podcast Plugin` (epizód-előkészítés) beolvasztva

---

## [0.1.0] – 2026-02-15

### Hozzáadva

- `/navigator-metadata` command: teljes YouTube metaadat generálás SRT fájlból
- `navigator-context` skill: podcast brand kontextus és YouTube stratégia
- `alkotmany.md`: a Navigátor Podcast alkotmánya (vízió, misszió, értékek)
- `README.md`: plugin dokumentáció és használati útmutató

---

## [0.2.0-pre] – 2026-02-15

### Módosítva

- Az egyetlen `/navigator-metadata` command szétbontva 5 külön commandra:
  - `/hook` — Cold Open / Hook javaslatok (5 db, virális pontszámmal)
  - `/cim` — YouTube cím generálás (5 High-CTR cím)
  - `/thumbnail` — Thumbnail szöveg javaslatok (5 db, max 3-4 szó)
  - `/leiras` — YouTube leírás és hashtagek (SEO-optimalizált)
  - `/idokod` — Pontos időkódok (10-12 kulcspillanat)

### Eltávolítva

- `/navigator-metadata` összevont command (helyette 5 külön command)
