---
title: 00_OPEN_QUESTIONS — Ignis (scoped)
date: 2026-06-03
author: Becze Szabolcs
status: active
description: Nyitott kérdések az Ignis területre. Üzleti, pozicionálási, tartalmi és struktúra-szintű kérdések, amelyek döntést vagy tisztázást igényelnek az Ignis Academy képzési vonalak és az IgnisXY közösségi tér fejlesztéséhez.
id: 7f3a2e41-bc09-4d8e-a12f-001ignis00004
index_schema_version: 1
bdos_index: true
generated_by: librarian v0.8.3
generated_at: 2026-06-03
scope: 02_Areas/Ignis
mode: index
---

# 00_OPEN_QUESTIONS — Ignis (scoped)

> Nyitott kérdések forrás-referenciával. Prioritás: `KRITIKUS` | `FONTOS` | `ALACSONY`

---

## Üzleti kérdések

### [KRITIKUS] Árazás — egyik képzésnek sincs ára
- Tájoló: ingyenes lead-magnet vagy fizetős?
- Műhely: in-company ár? Nyitott workshop ár? Csoportméret-alapú vagy fix?
- Bundle ár (Tájoló+Műhely)?
- **Forrás:** `Catalog/00_CATALOG.md` §Nyitott kérdések; `tajolo/COURSE.md` §Nyitott kérdések; `muhely/COURSE.md` §Nyitott kérdések

### [KRITIKUS] SaaS platform és képzési ág viszonya
- A `02_Areas/Ignis Academy/` (EU-pályázatos B2B SaaS platform) más entitás mint ez a képzési ág — de milyen a viszonyuk?
- Melyik az ernyő, melyik az ág?
- **Forrás:** `Catalog/00_CATALOG.md` §Nyitott kérdések #7

### [FONTOS] Nyitott workshop indítása
- A Műhely jelenleg in-company (HBC). Mikor indul nyitott (bárki által foglalható) workshop?
- Helyszín, dátum, kapacitás?
- **Forrás:** `muhely/COURSE.md` §Nyitott kérdések; `2. szint/Haladó/CLAUDE.md` §Kidolgozási státusz

---

## Pozicionálási / naming kérdések

### [FONTOS] Ernyő-tagline döntés (D1)
- Az Ignis Academy ernyőnek nincs végleges tagline-ja.
- ChatGPT „bizalmi" irányt javasolt, de döntés nem született.
- **Forrás:** `Catalog/00_CATALOG.md` §Ernyő-pozicionálás; `Pozicionalas/05_ERNYO_HIERARCHIA_osszehangolas.md`

### [FONTOS] „Tájoló" és „Műhely" — végleges nevek
- Mindkét képzés neve munkanév (working title).
- Mi a végleges márkanév? Megtartjuk a munkaneveket?
- **Forrás:** `tajolo/COURSE.md` §Nyitott kérdések; `muhely/COURSE.md` §Nyitott kérdések; `Pozicionalas/03_MESSAGING_ARCHITECTURE.md` bevezető

### [FONTOS] Ignis Academy vizuális identitás
- Nincs saját logó, szín, tipó.
- Jelenleg kölcsönzött partner-arculat (Hallenbeck IT + APN Promise + Sonrisa co-brand).
- Mikor lesz saját vizuális identitás?
- **Forrás:** `Catalog/00_CATALOG.md` §Nyitott kérdések #3

---

## Tartalmi kérdések

### [KRITIKUS] Prompt Library — nincs elkezdve
- A Műhely tananyag egyetlen hiányzó eleme a Prompt Library.
- Mikor készül el?
- **Forrás:** `2. szint/Haladó/CLAUDE.md` §Kidolgozási státusz (sorban: `Prompt library | ❌ nem kezdődött`)

### [FONTOS] Műhely+ specializáció döntés (D2)
- Marketing, üzletfejlesztés vagy általános haladó irány?
- A döntés blokkolja a tananyag-fejlesztés indítását.
- **Forrás:** `Catalog/muhely-plus/COURSE.md` §Nyitott döntés (D2)

### [FONTOS] 7 szokás képzés indítása
- Transcriptek megvannak (8 × ~34 000 szó összesen). Agenda és részletes leírás még hiányzik.
- Prémium hangolás és naming nincs.
- **Forrás:** `Catalog/het-szokas/COURSE.md` §Következő lépések; `7 szokás/Transcriptek/README.md`

### [ALACSONY] Korábbi 16 diás Tájoló prezentáció sorsa
- `1. szint/Diaképek/_korabbi-16-dia/` — megőrizve, de „ha biztosan elavult, törölhető"
- Törölhető-e?
- **Forrás:** `1. szint/README.md` §Nyitott pont

### [ALACSONY] Tájoló EN forrás szinkron
- A `tajolo/COURSE.md` a `04_Archive/.../28_AI_Tips_Course_Material_EN.md`-re mutat.
- Az `1. szint/Tananyag/ai_learning_material_v0.4.md` kapcsolata ehhez?
- **Forrás:** `tajolo/COURSE.md` §Forrás

---

## Struktúra / vault kérdések

### [FONTOS] TransOffice dry-run másolatok konszenzusa
- 6 féle TransOffice-másolat van a `2. szint/Haladó/` mappában.
- Melyik a kanonikus? (Valószínűleg `TransOffice_LIVE/`, 94 fájl)
- A többi mind archiválandó? Tidy mód szükséges.
- **Forrás:** `00_GAPS.md` GAP-1

### [FONTOS] Palyazat/ mappa tartalmának megértése
- `Ignis Academy/Palyazat/` tartalmát nem vizsgálta a Librarian (üresnek tűnik vagy minimálisan töltött).
- Mi van benne?

### [ALACSONY] IgnisCafe és Ignis Academy stratégiai viszonya
- A Napló.md utal arra, hogy az Ignis jövője kérdéses: „Pár tíz diák tud róla? Nem is önfenntartó..."
- Ez 2025-12-26-os napló. Hogyan alakult azóta?
- **Forrás:** `IgnisXY/Napló.md`

### [ALACSONY] Marketing/ mappa (gyökér)
- `Marketing/21 Alkalom - Előlap.png` — egyetlen fájl. Mi ez? Aktív anyag?
- **Forrás:** könyvtár-lista alapján

---

## Technikai kérdések

### [FONTOS] _FELTOLTENDO/ — feltöltés megtörtént-e?
- `_FELTOLTENDO/` mappában van `Tananyag_Halado_v1.2.zip` és `Ghidul-IMM-2026.pdf`.
- Feltöltve a hosting platformra (`/files/` mappa)? Ellenőrizendő.
- A `tananyag_letolto.html` ezekre hivatkozik.
- **Forrás:** `_FELTOLTENDO/_README.md`
