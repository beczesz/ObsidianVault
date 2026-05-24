# Műhely — Ignis Academy Haladó Workshop
## Fejlesztői és tervezői backstage

> **Ez a mappa NEM a tanulóé.** Itt tárolódik minden, ami a `Tananyag/` előállításához, fejlesztéséhez és karbantartásához kell.
>
> Ha új session-ben dolgozol a tananyagon, **mindig a `00_Tervezes/00_STORY_BOOK.md`-vel kezdj** — az a workshop élő narratívája.

---

## Mit tartalmaz a Műhely?

**Tisztított, élő anyagok** — csak ami aktív a fejlesztésben:

```
Műhely/
├── README.md                                ← Ez a fájl
│
├── 00_Tervezes/                             ← FÁZIS-FÜGGETLEN narratíva és tervezési doksik
│   ├── 00_STORY_BOOK.md                     ← 🌟 ELSŐKÉNT EZT OLVASD el minden új session-kor!
│   ├── 00_Bevezető_szöveg.md                ← Workshop bevezető script
│   ├── 01_Logisztika és előfeltételek.md
│   ├── 02_ChatGPT szintézis - Workshop struktúra.md  (master plan v0.2)
│   ├── 05_ChatGPT szintézis v0.3 - Filozófia és delivery.md
│   ├── 06_F4_narrativa_legal_plugin.md      ← A Béla bácsi-sztori részletes narratívája
│   └── 07_Versenytars_elemzes_ThrivenExus.md (+pdf)
│
├── 03_Dontes_Elemzes/                       ← F3: pályázati kiírás generálása
│   └── Palyazat_kiiras_BUILD/
│       ├── build_pdf.py                      ← weasyprint generálás
│       └── style.css                         ← PDF stílusok
│
├── 04_Legal_Szerzodes/                      ← F4: bérleti szerződés generálás
│   └── Szerzodes_BUILD/
│       ├── build_szerzodes.js                ← docx-js generálás
│       └── package.json
│
├── 06_Marketing_Honlap/                     ← F6: weboldal design source
│   └── website_design_source/
│       ├── design-system.md                  ← részletes ANAF design-system spec
│       ├── anaf-bundle1.css                  ← EREDETI ANAF CSS (200 KB)
│       └── inline-styles.css                 ← ANAF HTML-ből kinyert inline stílusok
│
└── _archivum/                               ← NEM aktív (lásd _archivum/README.md)
```

---

## Munkafolyamatok

### 1. Új narratíva-elem vagy fázis-finomítás

→ Frissítsd a **`00_Tervezes/00_STORY_BOOK.md`**-t. Verzió-szám emelése, dátum hozzáadása.

### 2. Pályázati kiírás PDF újragenerálása

```bash
cd Műhely/03_Dontes_Elemzes/Palyazat_kiiras_BUILD/
python3 build_pdf.py
# Output: Tananyag/03_Dontes_Elemzes/Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2026.pdf
```

### 3. Bérleti szerződés docx újragenerálása

```bash
cd Műhely/04_Legal_Szerzodes/Szerzodes_BUILD/
npm install            # ha node_modules még nincs
node build_szerzodes.js
# Output: Tananyag/TransOffice/szerzodes_chirie_TransOffice_2018.docx
```

### 4. Weboldal design-source ellenőrzése

A `06_Marketing_Honlap/website_design_source/design-system.md` az **igazi forrás**. Ha a Tananyag/06/website/old/design-system/anaf-style.css változik, a változásokat itt is dokumentáld.

---

## Fontos megjegyzések

- A `Műhely/` és a `Tananyag/` **hasonló struktúrával** rendelkezik (fázisszámozás 01-06), hogy könnyű legyen átkapcsolni.
- A `Tananyag/` **zip-elhető** — bele kell tudjon csomagolni, és a tanuló a kibontva használhassa.
- A `Műhely/` **NEM kerül a zip-be** — ez a szerző-fejlesztő munkamappa.
- Az `_archivum/` régi/elvetett anyagokat tartalmaz, lásd: `_archivum/README.md`.

---

**Verzió:** 2.0 (tisztított) · **Utolsó frissítés:** 2026-05-12
