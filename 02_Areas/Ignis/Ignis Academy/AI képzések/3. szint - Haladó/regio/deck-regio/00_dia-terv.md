---
title: "Haladó deck (Regio Consult) — dia-terv"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "Az Ignis Academy Haladó (3. szint) képzés Regio Consult-ra szabott HTML-natív prezentációjának (deck-regio/index.html) dia-terve: 44 dia sorrendben, szekciókba rendezve, a 6 fázissal (F1-F6). 2026-07-02 nagy átrendezés: új F3 = Connectorok/Skillek/Pluginok (a korábbi S/P/C fundamentum-diákból + MS365-connector élő demó), a monitoring-fázis teljesen kivéve, a többi fázis eltolva (volt F3 OCR → F4, volt F4 összevetés → F5, volt F5 deviz-skill → F6). A narratíva a Regio tanácsadó-szerep napi fájdalmaira épül, a Napsugár Tejüzem fiktív példaprojekttel. Vetítés böngészőből, teljes képernyőn."
id: 6aca4d3f-e005-41e8-9cc8-2d0a48236e14
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, prezentacio, dia-terv, deck, animacio]
---

# Haladó deck (Regio Consult) — dia-terv

> Az **Ignis Academy Haladó** (3. szint, 4 órás hands-on workshop) prezentációja, a **Regio Consult** EU pályázati tanácsadó cégre szabva. HTML-natív, egyetlen fájl: [`index.html`](index.html). **44 dia.** Vetítés böngészőből, teljes képernyőn (F11). A design system az Alapozó/Mester deckkel közös: navy alap, narancs vezérszín, Space Grotesk / Source Sans 3 / JetBrains Mono, geometrikus Ignis-logó.

## A 6 fázis (2026-07-02 átrendezés után)

1. **F1 — Rendrakás + standard-audit + CLAUDE.md-lánc**
2. **F2 — Rend a TODO-k között** (ügyfél-egyeztetés → feladatlista)
3. **F3 — Connectorok, Skillek, Pluginok (ÚJ)**: a rendszer kinyílik. MS365 connector (befut a kivitelező ajánlata emailben), majd a skill és plugin fogalma elméletben + gyakorlatban. Sorrend: Connector → Skill → Plugin.
4. **F4 — Szkennelt ajánlat → használható adat** (OCR, formátum-triázs, token-mérleg) [volt F3]
5. **F5 — Deviz-értelmezés + ajánlat-összevetés** (az AI érti a HG 907 devizt, majd tételesen összeveti) [volt F4]
6. **F6 — Deviz-templét kitöltése forrásból, skillel** (a killer-demo) [volt F5]

A **monitoring / Centralizator** fázis (volt F6) teljesen kikerült.

## A keret-eltolás (mi a szerep)

A tanuló **Regio-tanácsadó**, aki a saját, **erősen strukturált** rendszerére ültet AI-t. A workshop nem rendet erőltet rá egy kaotikus cégre, hanem a meglévő struktúrát tanítja meg az AI-nak, majd a napi ismétlődő szakmunkát gyorsítja fel. A fiktív, újrahasználható példaprojekt: **Napsugár Tejüzem SRL** tejfeldolgozó-bővítése. Deviz TOTAL fără TVA 6 455 000 lei, cu TVA (19%) 7 681 450 lei, Cap. 4 = 5 435 000, ajánlat 5 375 000 lei (a hiányzó 4.6 Active necorporale 60 000 miatt).

## Felépítés egy pillantásra

| Szekció | Diák | Mit csinál |
|---|---|---|
| **Nyitány** | h1-h5 | Beköszön, elhelyez a programban, 3 alapelv, vízió, videó |
| **Ipari ↔ kognitív** | h6 | A „miért most" idővonal (scrollozható) |
| **A workshop teste** | h7-h12 | Módszer, példaprojekt, küldetés, a 6 fázis (agenda), a tét, mélyebbre |
| **Tananyag-letöltő** | hurl | `ignis.academy/halado/tananyag`, jelszó `ignis387` |
| **F1** | f1a/f1b/f1c | Rendrakás + standard, CLAUDE.md-lánc |
| fundamentum | hmd, hob, hobd | Markdown + Obsidian |
| **F2** | f2a/f2b/f2c | Egyeztetés → feladatlista |
| **F3 (ÚJ)** | hspc, hcconn, hcskill, hcplugin | Connector/Skill/Plugin áttekintő + 3.1 Connector (MS365) + 3.2 Skill + 3.3 Plugin |
| **F4** | f3a/f3b/f3c | Szkennelt ajánlat → md (OCR) |
| **F5** | f4a/f4b/f4c | Deviz-értelmezés + ajánlat-összevetés |
| **F6** | f5a/f5b/f5c | Deviz-templét kitöltése skillel (killer) |
| **Zárás** | h13-h17, ko, mc5-mc7 | Hazaviszel, összegzés, fejlődési út, agentek, ExarLabs, Q&A, köszönöm |

> **Fontos ID-megjegyzés:** a DOM-sorrend adja a dia-sorrendet, az ID-k csak animáció-eseményhez + URL-hash-hez kellenek. Az átrendezéskor az ID-ket NEM neveztük át (kockázatos a JS-csatolás miatt), csak a látható fázis-címkéket. Ezért a régi ID-k a NEW fázist mutatják: `f3*` = F4 (OCR), `f4*` = F5 (összevetés), `f5*` = F6 (deviz-skill). A hat élő animáció (`f1c`, `f2c`, `f3c`, `f4c`, `f5c`) ID-je változatlan, a JS ehhez kötődik.

## Az F-blokkok (feladatonként 3 dia: feladat → koncepció → élő animáció)

| Fázis | ID-k | Feladat-dia (`*a`) | Élő animáció (`*c`) |
|---|---|---|---|
| **F1** | f1a/b/c | Tanítsd be az AI-t a strukturált rendszeredre | fájlok → RC-mappák + CLAUDE.md |
| **F2** | f2a/b/c | Rend a TODO-k között | egyeztetés-leirat sorai → feladatkártyák |
| **F3** | hspc + hcconn/hcskill/hcplugin | Connector/Skill/Plugin (interaktív „aktiváld" kártyák) | (nincs *c animáció, interaktív kártyák) |
| **F4** | f3a/b/c | Szkennelt ajánlat → adat | 200 szkennelt oldal → OCR → md tábla |
| **F5** | f4a/b/c | Deviz-értelmezés + összevetés | források → tételes eltérés (a 60 000 lej hiány) |
| **F6** | f5a/b/c | Deviz-templét kitöltése forrásból | forrás-tételek → szürke input-cellák → aggregált Deviz General |

## Interakciós modell

- **Léptetés:** `←` / `→`, `Space`, `PageUp`/`PageDown`, vagy kattintás a dián (előre) / jobbklikk (vissza).
- **Animációk (`f1c`-`f5c`):** a diára lépve maguktól elindulnak (`slideshown` esemény); a színpadra kattintva újrajátszhatók.
- **Interaktív F3-kártyák (`hcconn`/`hcskill`/`hcplugin`):** az „Aktiváld / Csatlakoztasd / Telepítsd" gombra a before→after állapot vált.
- **Reload-megőrzés:** `#N` az URL-ben → ott folytatja.

## Vetítés és export

- **Ajánlott:** böngészőből, teljes képernyőn (`F11`).
- **Lokális szerver:** `python3 -m http.server` a `deck-regio/` mappában (launch.json: `ignis-halado-regio-deck`, port 8153).
- **pptx/pdf:** lehetséges, de az animációs diák ott statikusak.

## Megjegyzések

- A szerkesztés **a HTML-ben** történik, egyetlen `index.html`.
- A tananyag-forrás a `../Tananyag/`; a valódi RC-ügyféladatok (`../raw/`) KONFIDENCIÁLISAK, a deckben minden anonimizált / fiktív.
