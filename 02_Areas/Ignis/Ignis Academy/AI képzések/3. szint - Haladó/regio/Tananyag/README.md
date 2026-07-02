---
title: "Ignis Academy: Haladó AI Workshop (Regio Consult)"
date: 2026-07-01
author: Becze Szabolcs
status: active
version: 1.0
description: "Ez egy 4 órás interaktív AI workshop tananyaga a Regio Consult pályázati tanácsadó csapatnak. A résztvevők a saját, strukturált projekt-felépítésükre ültetnek AI-t (Cowork), és a napi fő fájdalmukat oldják meg egyetlen összefüggő fiktív projekten (Napsugár Tejüzem): rendrakás + CLAUDE.md-lánc, egyeztetés → feladatlista, connectorok/skillek/pluginok, szkennelt PDF kiolvasása, deviz-értelmezés + ajánlat-összevetés, és a killer-demó: levédett deviz-templét kitöltése skillel. 6 fázisos, élő demó-alapú curriculum, az eredeti Haladó (TransOffice) pedagógiájára építve, Regio-adaptálva."
id: 2f9c1e84-7a63-4d21-b8e6-5c0a9f3d2b17
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, tananyag, workshop, napsugar]
---
# Ignis Academy: Haladó AI Workshop (Regio Consult)
## Tananyag-csomag

> **Verzió:** 1.0 (Regio Consult adaptáció, a TransOffice Haladó v1.2 pedagógiájára építve)
> **Kiadás dátuma:** 2026-07-01
> **Időkeret:** 4 óra (csütörtök, 11:00 kezdés, 12:30 brunch-szünet)
> **Célközönség:** 21 fős Regio Consult csapat, pályázati szakértők, 3 iroda
> **Nyelv:** magyar (a projekt-assetek román pályázati dokumentumok)

---

## Mi ez?

Ez egy **élő, vezetett 4 órás AI workshop tananyaga**, amelyet kifejezetten a Regio Consult csapatra szabtunk.

Az eredeti Haladó workshop a káoszról szólt: egy rendetlen KKV-t kellett rendbe tenni. A Regionál **fordított a helyzet**: nálatok erős struktúra van, tudatosan strukturált, sztenderdizált mapparendszer, amiben bárki fél óra alatt átvesz egy ismeretlen projektet. Ez erősség, nem probléma. A workshop tehát nem rendet rak, hanem **megtanítja az AI-t a ti strukturált rendszeretekre**, és a napi ismétlődő szakmunkát gyorsítja fel.

**A workshop egy film:** a résztvevő egy Regio-tanácsadó, aki egyetlen ügyfél-projektet visz végig (Napsugár Tejüzem, egy tejfeldolgozó-beruházás), és 4 óra alatt a három legfájdalmasabb napi feladatát oldja meg AI-val.

**Módszer:** *„Narrated Live Experience"*: 70% élő demó, 20% mikro-hands-on, 10% szabad próbálkozás. Az oktató narrál, a résztvevők belépnek a kulcs-pillanatokban. Van hely a szabad kérdezz-felelekre is (a kapcsolattartó kifejezett kérése).

---

## A 3 fő fájdalom, amit megoldunk

A 2026-06-29-i igényfelmérő meetingből, a Regio saját prioritási sorrendjében:

1. **Szkennelt PDF, használható adattá** (a legnehezebb): állami platformról letöltött, kép-only ajánlatokat kell tételesen egyeztetni. Reality-check: mit tud az AI, mit nem (még).
2. **Levédett, képletvezérelt Excel-templétek kezelése** (a legáltalánosabb): a deviz general és üzleti terv templétek kitöltése. **Ez a workshop killer-demója.**
3. **Pályázatépítés** (a legkevésbé sürgős, ebben már profik): csak könnyű érintés, nem ebből indulunk.

**Fontos scope-határ:** ez a **Haladó** szint, nem a Mester. **Agentet nem építünk** (az túl komplex, az a Mester szintje). A cél: alapok és eszközök átadása, hogy a csapat **maga tudja automatizálni magát**.

---

## Hogyan használd ezt a csomagot?

### Oktatóként
1. Olvasd el a `00_Bevezetes/Ceg_leiras_Regio_Napsugar.md` fájlt: a fiktív cég és a Napsugár projekt teljes kontextusa.
2. Menj végig a 6 fázis (01 → 06) `README_FX.md` és `Feladat_X.X.md` fájljain.
3. A `RegioConsult/` mappa a workshop **kiindulási környezete**: 3 projekt (2 rendezett + a káosz Napsugár), a belső standard (`Internal_Standard.docx`) és a kötelező üres template (`RC_Template_URES.docx`).
4. A workshop során a Cowork-kel ezeken a fájlokon dolgozunk: auditálunk, rendet rakunk, bekötünk, kiolvasunk, összevetünk, kitöltünk.

### Résztvevőként
1. Nyisd meg a `RegioConsult/` mappát a Cowork-ben: ez lesz a munkakörnyezeted.
2. Kövesd a feladatleírásokat fázisonként (`01_Struktura_CLAUDE` → `06_Deviz_Skill`).
3. Minden fázisnak van egy `README_FX.md` (áttekintés) és 2-3 `Feladat_X.X.md` (konkrét feladat, copy-paste prompttal).

---

## Mappastruktúra

```
Tananyag/
├── README.md                                ← Ez a fájl
├── 00_Bevezetes/
│   └── Ceg_leiras_Regio_Napsugar.md          ← A fiktív cég + Napsugár projekt kontextusa
│
├── RegioConsult/                            ← A KIINDULÁSI KÖRNYEZET (RC strukturált rendszer)
│   ├── Internal_Standard.docx                ← a belső standard (a mérce, F1-audit)
│   ├── RC_Template_URES.docx                 ← a kötelező üres template (fejléc/lábléc)
│   ├── 00_General_info/
│   └── Projects/
│       ├── PAN_Malomkert_Panzio/             ← rendezett, compliant referencia
│       ├── KER_Zold_Kerteszet/               ← rendezett, compliant referencia
│       └── THR_Napsugar_Tejuzem/             ← a KÁOSZ (F1 rendrakás tárgya), saját CLAUDE.md
│           ├── 02_Editabil/                  (hiteles HG 907 kiírás-deviz)
│           └── 08_Dosare_de_achizitii/04.04_DAL_Lucrari/  (szkennelt ajánlat + OCR-md + antemăsurătoare)
│
├── 01_Struktura_CLAUDE/                     ← F1: Rendrakás + standard-audit + CLAUDE.md-lánc (35p)
├── 02_Egyeztetes_TODO/                      ← F2: Rend a TODO-k között (25p)
├── 03_Connectors_Skills_Plugins/            ← F3: Connectorok, skillek, pluginok (30p)
├── 04_Szkennelt_PDF/                        ← F4: Szkennelt ajánlat → adat (35p)
├── 05_Osszevetes/                           ← F5: Deviz-értelmezés + ajánlat-összevetés (30p)
├── 06_Deviz_Skill/                          ← F6: Deviz-templét kitöltő skill (45p, KILLER)
└── _gyakorlo_peldak/                         ← minta bemenetek a "saját fájlos" otthoni bónuszokhoz
```

---

## A 6 fázis a workshop ívén

| # | Fázis | Idő | Lényeg | Fő eszköz |
|---|-------|-----|--------|-----------|
| **F1** | Rendrakás + standard-audit | 35p | A strukturált RC-rendszer auditja, rendrakás, egymásba ágyazott CLAUDE.md-lánc | Cowork alapok, fájlrendszer, OneDrive/SharePoint, markdown, CLAUDE.md |
| **F2** | Rend a TODO-k között | 25p | Egyeztetés-leirat → mentett, session-ök közt élő feladatlista | Productivity / kontextus-perzisztencia |
| **F3** | Connectorok, skillek, pluginok | 30p | A rendszer kinyílik: MS365 connector (befut az ajánlat), skillek és pluginok elméletben + gyakorlatban | Connector (MS365), skill-alapok, pluginok, a saját RC-pluginok iránya |
| **F4** | Szkennelt ajánlat → adat | 35p | 200 oldalas kép-PDF reality-check: mit tud OCR, mit nem | OCR, vektoros vs. szkennelt, formátum-triázs, token-mérleg |
| **F5** | Deviz-értelmezés + ajánlat-összevetés | 30p | Az AI érti a HG 907 devizt, majd tételesen összeveti az ajánlattal, eltérés-kimutatás | Excel-értés, több forrás keresztellenőrzése |
| **F6** | Deviz-templét kitöltő skill | 45p | Levédett templét kitöltése forrásból egy team-skillel (a workshop csúcspontja) | **Skill éles használata**, levédett cellák, csapat-megosztás |

---

## Mit fogsz csinálni

A workshop végére (4 óra alatt):
1. **Rendbe rakod** és betanítod a Regio strukturált rendszerét az AI-nak (standard-audit, CLAUDE.md szabálykönyv-lánc, a meglévőt nem bolygatva).
2. **Rendet raksz a teendők között**: egy egyeztetés-leiratból session-ök közt élő feladatlistát csinálsz.
3. **Bekötöd** az AI-t a rendszereitekbe (MS365 connector), és megismered a **skilleket és pluginokat** elméletben és gyakorlatban.
4. **Kiolvasol** egy szkennelt ajánlatot használható adattá, és őszintén látod hol a határ.
5. **Értelmezed** a HG 907 devizt, és tételesen **összeveted** az ajánlattal, megtalálva az eltérést, amit kézzel kihagynál.
6. **Kitöltesz** egy levédett deviz-templétet forrásból, egy **skillel**, amit a csapatod megoszthat (a workshop csúcspontja).

És a legfontosabb: **átéled** mit jelent az AI-val együtt dolgozni a saját rendszereden, nem tool-tanulás, hanem perspektíva-váltás.

---

## Mit kell hozzá

- **Claude Cowork** (Team plan, ~18 EUR/seat/hó): a Cowork desktop alkalmazás + a **skill-megosztás** miatt (a Team plan kulcs a killer-demóhoz).
- **Microsoft 365 / OneDrive / SharePoint**: a közös projekt-struktúra, ahol a Cowork a fájlokon dolgozik.
- **Obsidian** (ingyenes, opcionális): a markdown-fájlok kényelmes szerkesztéséhez.
- **Egy laptop**, Chrome browser, megbízható internet (a helyszíni wifit előzetesen tesztelni kell: 21 ember egyszerre dolgozik).

---

## Licenc és felhasználás

Ez a tananyag az **Ignis Academy** szellemi terméke. A **Napsugár Tejüzem SRL** és minden szereplő **fiktív**, oktatási célra készült; a valós Regio Consult ügyféladatok nem részei a csomagnak. A struktúra a Regio belső sztenderdjének logikáját követi, valós ügyfélnév, CUI és összeg nélkül.

A tananyagot kizárólag a Regio Consult csapata használhatja a workshopon és az azt követő gyakorláshoz. Tovább nem terjeszthető.

---

**Verzió:** 1.1 (F3 Connectors/Skills/Plugins beszúrva, Monitoring kivéve) · **Készítette:** Ignis Academy · **Kapcsolat:** hello@exar.ro · **Utolsó frissítés:** 2026-07-02
