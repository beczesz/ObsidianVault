---
title: "Haladó deck (Regio Consult) — dia-terv"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "Az Ignis Academy Haladó (3. szint) képzés Regio Consult-ra szabott HTML-natív prezentációjának (deck-regio/index.html) teljes dia-terve: mind a 46 dia sorrendben, szekciókba rendezve, a 6 feladat (F1-F6) feladat/koncepció/animáció hármasaival. A narratíva a TransOffice pályázó-KKV helyett a Regio tanácsadó-szerep 3 napi fájdalmára (szkennelt PDF, deviz-templét, monitoring) épül, a Napsugár Tejüzem fiktív példaprojekttel. Vetítés böngészőből, teljes képernyőn."
id: 6aca4d3f-e005-41e8-9cc8-2d0a48236e14
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, prezentacio, dia-terv, deck, animacio]
---

# Haladó deck (Regio Consult) — dia-terv

> Az **Ignis Academy Haladó** (3. szint, 4 órás hands-on workshop) prezentációja, a **Regio Consult** EU pályázati tanácsadó cégre szabva. HTML-natív, egyetlen fájl: [`index.html`](index.html). **46 dia.** Vetítés böngészőből, teljes képernyőn (F11). A design system az Alapozó/Mester deckkel közös: navy alap, narancs vezérszín, Space Grotesk / Source Sans 3 / JetBrains Mono, geometrikus Ignis-logó.

## A keret-eltolás (mi változott a TransOffice-verzióhoz képest)

A tanuló **nem** egy kaotikus KKV operatív vezetője, aki AFM pályázatot ad be. A tanuló **Regio-tanácsadó**, aki a saját, **erősen strukturált** rendszerére ültet AI-t, és **három konkrét napi fájdalmat** old meg vele:
1. Szkennelt, kép-only ajánlat → használható adat (OCR, formátum-triázs, token-mérleg).
2. Levédett, képletvezérelt deviz-templét kitöltése forrásból (a killer-demo).
3. Monitoring: a kivitelezés (situații de lucrări) követése a szerződéshez mérve egy Centralizatorban.

A fiktív, újrahasználható példaprojekt: **Napsugár Tejüzem SRL** (Cristuru Secuiesc, Harghita) tejfeldolgozó-bővítése. Deviz TOTAL fără TVA 6 455 000 lei, cu TVA (19%) 7 681 450 lei, ajánlat 5 375 000 lei, curs 4,97 lei/EUR.

## Felépítés egy pillantásra

| Szekció | Diák | Mit csinál |
|---|---|---|
| **Nyitány** | 1-5 | Beköszön, elhelyez a programban, 3 alapelv, felvázolja a víziót |
| **Az ipari ↔ kognitív narratíva** | 6 | A „miért most" idővonal (scrollozható) |
| **A workshop teste** | 7-12 | Módszer, a példaprojekt, a küldetés (3 fájdalom), a 6 fázis, a tét |
| **A 6 feladat (F1-F6)** | F1-F6 blokkok | Feladatonként 3 dia: feladat → animáció-koncepció → élő animáció + a köztes fundamentum-diák (markdown, Obsidian, Skill/Plugin/Connector) |
| **Zárás** | h13-h17 + mc | Hazaviszel, összegzés, hol vagyunk most, „hova tovább: agentek", ExarLabs (halk), Q&A, köszönöm |

## A dia-sorrend

### Nyitány
1. **`h1`** — Welcome: „A 10x produktivitás-növekedés kora" (cím + intro: saját strukturált rendszerre AI, 3 fájdalom, 4 órás)
2. **`h2`** — Öt szint, egy fejlődési út („ma itt: 3. Haladó, a Regio napi munkájára szabva"; a csapat NEM járt 1-2-n)
3. **`h3`** — Három alapelv, amire építünk (Ethos / Logos / Pathos / Thelos; neutrális, nem feltételez korábbi Alapozót)
4. **`h4`** — A Haladó szint víziója (a saját strukturált rendszer + AI Cowork a saját fájljaikon)
5. **`h5`** — Videó: „Ilyen a jövő munkája az AI-jal" (`assets/jovo-munkaja.mp4`, változatlan)

### Az ipari ↔ kognitív narratíva
6. **`h6`** — Idővonal: Ipari forradalom ↔ Kognitív forradalom (**scrollozható**, változatlan)

### A workshop teste
7. **`h7`** — Felváltva dolgozunk (módszer: kivetített narratíva ↔ Cowork + Microsoft 365 / OneDrive / SharePoint + Markdown; Obsidian opcionális)
8. **`h8`** — A főszereplő: Napsugár Tejüzem (Regio-projekt, 6 tény: beneficiar, helyszín, projekt, beruházás, finanszírozás, a tanácsadó szerep)
9. **`h9`** — A küldetés: három napi fájdalom, AI-jal (szkennelt→adat, deviz-templét, monitoring)
10. **`h10`** — Hat fázis, egy történet (az új F1-F6 agenda)
11. **`h11`** — A tét: 4 óra vs 160 óra (kézi ellenőrzés / templét-építés / monitoring vs. Cowork; 40x)
12. **`h12`** — „A sebesség nem az egyetlen hozadék" (reveal, változatlan)

### Tananyag-letöltő
- **`hurl`** — Töltsd le, és kövesd élőben (`ignis.academy/halado/tananyag`, jelszó `ignis387`)

### A 6 feladat (F1-F6) — feladatonként 3 dia + fundamentum-diák

| # | Feladat-dia (`*a`) | Koncepció (`*b`) | Élő animáció (`*c`) |
|---|---|---|---|
| **F1** | Tanítsd be az AI-t a strukturált rendszeredre | storyboard | fájlok → RC-mappák (Cerere de finanțare … Monitorizare) + CLAUDE.md |
| **F2** | Rend a TODO-k között (ügyfél-egyeztetés) | storyboard | egyeztetés-leirat sorai → feladatkártyák |
| **F3** | Szkennelt ajánlat → használható adat | storyboard | 225 szkennelt oldal → OCR → md tábla + token-mérleg (kinyerve / kézzel) |
| **F4** | Ajánlatkérés vs. ajánlat tételes összevetése | storyboard | 4 forrás (deviz, ajánlat, centralizator, contract) → tételes eltérés |
| **F5** | Deviz-templét kitöltése forrásból (killer-demo) | storyboard | forrás-tételek → szürke input-cellák → aggregált Deviz General (TVA, TOTAL) |
| **F6** | Monitoring: Centralizator kitöltése | storyboard | üres Centralizator → SL1/SL2/SL3 + Rest de executat |

Fundamentum-diák (Szabolcs kötelezőnek jelölte, F1 és F2 között, illetve F4 és F5 között):
- **`hmd`** — Markdown: mi van a dokumentum alatt? (PDF vs md, a Napsugár üzleti terv példáján)
- **`hob`** — Obsidian: opcionális szerkesztő (a markdown a fájlrendszeren/SharePointon él; a demó jegyzetek Regio/Napsugár témájúak)
- **`hobd`** — Obsidian élő demó (koncepció)
- **`hspc`** — Skill / Plugin / Connector áttekintő (Skill: team-megosztott deviz-kitöltő; Connector: Outlook/M365)
- **`hcskill`** — Mi egy Skill? (interaktív; deviz-kitöltő skill, team plan)
- **`hcplugin`** — Mi egy Plugin? (Legal, finanszírozási szerződés)
- **`hcconn`** — Mi egy Connector? (Outlook, tervező emailje a Napsugár ajánlatról)

(id-k: `f1a`/`f1b`/`f1c` … `f6a`/`f6b`/`f6c`.)

### Zárás
- **`h13`** — Amit ma hazaviszel (1 dolog + bónusz feladatok; takeaway: CLAUDE.md a sztenderdből, skill-megosztás, szkennelt→md, templét, monitoring)
- **`h14`** — Összegzés: Mit tanultunk ma? (4 cap: sztenderd mint kontextus, szkennelt→adat, templét-kitöltés, monitoring)
- **`h15`** — Hol tartasz most (fejlődési út; light, a kapcsolattartó már járt Mesteren, ezért nem oversell)
- **`h16`** — Hova tovább: agentek (a Mester-promo helyett egyetlen, halk „jövőbeli opció" dia: indexelő + lektor agent, explicit Haladó-scope-on kívül)
- **`mc5`** — ExarLabs weboldal (halk, „ha egyszer fejlesztés kell", peer-hang)
- **`mc6`** — ExarLabs egyedi szoftver (halk, „ha egyszer kell")
- **`mc7`** — Q&A
- **`h17`** — Köszönöm (`ignis.academy · hello@exar.ro`)

## Törölt diák (a TransOffice-verzióhoz képest)
- **`m5`** (Mester vízió), **`ko`** (élő tudástár canvas), **`mc3b`** (AI Natív vállalat intro), **`aiv`** (AI Natív vállalat canvas) — a teljes multi-diás Mester-promo, összevonva egyetlen `h16` „hova tovább" diává. Az agentek explicit Haladó-scope-on kívül.
- **`mc4`** (ExarLabs „segítünk 200 000 EUR pályázatban") — törölve: a Regio maga professzionális pályázati tanácsadó, ezt neki felajánlani helytelen.
- A `ko` és `aiv` canvas-animációk JS-blokkjai is eltávolítva (a hozzájuk tartozó CSS inert maradt).

## Interakciós modell

- **Léptetés:** `←` / `→`, `Space`, `PageUp`/`PageDown` (távirányító-barát), vagy kattintás a dián (előre) / jobbklikk (vissza).
- **Animációk (F1c-F6c):** a diára lépve **maguktól elindulnak** (esemény-vezérelt, `slideshown`); a színpadra kattintva **újrajátszhatók**. A színpad `.noadvance`, így a rajta való kattintás nem ugrik diát.
- **Idővonal (h6):** a fejléc fix, a tartalom a dián belül görgethető (egér/trackpad).
- **Reload-megőrzés:** `#N` az URL-ben → ott folytatja.

## Vetítés és export

- **Ajánlott:** böngészőből, teljes képernyőn (`F11`). A 6 animáció HTML-natív (élő JS/CSS).
- **pptx/pdf:** lehetséges, de az **animációs diák ott élettelenek** (statikus kép). Ha kell, a `*c` diákról külön rövid képernyővideó javasolt.
- **Lokális szerver fejlesztéshez:** `python3 -m http.server` a `deck-regio/` mappában.

## Megjegyzések

- A szerkesztés **a HTML-ben** történik, egyetlen `index.html`.
- A fiktív számok a `../fiktiv_pelda/README.md`-ből, a stratégia a `../01_adaptacio_strategia_v0.1.md` / `../02_anyag_attekintes_2026-06-30.md` / `../03_konverzio_es_OCR_strategia_2026-06-30.md` fájlokból.
- A valódi RC-ügyféladatok (`../raw/`) KONFIDENCIÁLISAK; a deckben minden anonimizált / fiktív.
