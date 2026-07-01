---
title: "Regio Consult — szkennelt PDF konverzió + OCR token-stratégia (2026-06-30)"
date: 2026-06-30
author: Becze Szabolcs
status: active
version: 1.0
description: "A #1 fájdalom (szkennelt PDF -> használható adat) konverziós stratégiája. Subscription-alapú (nem API) OCR token-mérleg valós méréssel a fiktív szkennelt ajánlaton: ~2316 képtoken/oldal OCR-input vs ~595 token md-eredmény. Vektorizálás vs. markdown összevetés, ajánlott munkafolyamat, és a fiktív demo-asset (oferta_szkennelt + OCR md)."
id: 399fccc8-f49c-4f3e-b087-16b21e5d9f6e
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, kepzes, halado, regio-consult, ocr, konverzio, token, palyazat]
---

# Szkennelt PDF: konverzió + OCR token-stratégia

> Ez a #1 fájdalomra (szkennelt PDF → használható adat) ad választ. Demo-asset: `fiktiv_pelda/oferta_szkennelt_Napsugar.png/.pdf` (kép-only, **0 kinyerhető szöveg**) → `fiktiv_pelda/oferta_szkennelt_Napsugar_OCR.md` (OCR-eredmény). Az OCR-t **subscription-ön** (Cowork-vízió) futtattuk, nem API-n.

## 1. Token-mérleg (valós mérés a fiktív oldalon)

A fiktív szkennelt ajánlat A4 @150 DPI (1240×1754 px), pont mint a valós `Oferta`. A vízió a képet ≤1568 px hosszú élre méretezi (1108×1568), a token ≈ (sz×m)/750.

| | Egy oldal | 12 oldal | 225 oldal (mint a valós Oferta) |
|---|---:|---:|---:|
| **OCR-input (kép)** | ~2 316 token | ~27 800 token | **~521 000 token** |
| **OCR-eredmény (md)** | ~595 token | ~7 100 token | **~134 000 token** |

Mit jelent ez **subscription-ön** (nem API, tehát nem dollár, hanem context + használati limit):
- Egy **200k context-ablakba ~86 szkennelt oldal** OCR-inputja fér. A 225 oldalas Oferta tehát **~3 körre** darabolandó (nem megy egy session-ben).
- Max / Team előfizetésen egy ilyen **egyszeri** OCR-futás a heti limitnek kis része, simán belefér. Nem a pénz a korlát, hanem a context-ablak (darabolás) és a sebesség.
- **A kulcs:** OCR-ezz **egyszer**, mentsd **md/strukturált** formába, és onnantól az AI a ~134k tokenes (vagy szeletelt) md-t olvassa, nem a fél milliós képtömeget. **Soha nem fizeted újra a kép-OCR-t.**

## 2. Vektorizálás vs. markdown — mi a jó célformátum?

| Szempont | „Vektorizálás" (kereshető PDF, OCR-szövegréteg) | **Markdown / strukturált tábla (xlsx, csv)** |
|---|---|---|
| Mivel | Adobe Acrobat Pro OCR, vagy OCRmyPDF | Cowork-vízió → md, vagy Adobe „Export to Excel" |
| Eredmény | ugyanaz a nagy PDF + rejtett szövegréteg | pici, tiszta, strukturált szöveg |
| AI token-költség | **gyakran nem csökken** — az AI sokszor így is képként olvassa az oldalt, ha nem nyered ki előbb a szöveget | **drámaian kevesebb** (kb. 4-8x, lásd fenti tábla) |
| Pontosság számoknál | OCR-függő, ellenőrizni kell | OCR-függő, de **ellenőrizhető** (kontroll-összeg a md-ben) |
| Újrahasználat / verziózás | nehéz (bináris PDF) | **könnyű** (diff-elhető, git/Obsidian-barát) |
| Emberi keresés / archívum | jó (kereshető PDF) | jó |

**Ajánlás:** numerikus ajánlat-/deviz-adatnál a célforma **strukturált tábla (md vagy közvetlenül xlsx/csv)**, nem PDF. A „vektorizálás" (kereshető PDF) hasznos **emberi archívumnak** és **elő-lépésnek** (az Adobe Export-to-Excel pont egy OCR+tábla lépés), de a tartós, AI-barát végpont a **md/strukturált**. A `..._OCR.md` fájlban a végén szándékosan van egy **kontroll-összeg** — ez az OCR-hibák kiszűrésének fegyelme.

## 3. Ajánlott munkafolyamat a #1 fájdalomra (ezt tanítjuk)

1. **Először kérj vektoros / Excel exportot** a tervezőtől / a forrásból. A vektoros `F1-F4` típus gyakorlatilag ingyen és pontos (pdftotext / közvetlen kinyerés). Ez a legolcsóbb és legpontosabb út.
2. **Ha csak szkennelt van:** OCR **egyszer** (Cowork-vízió vagy Adobe Pro), majd **ellenőrizd kontroll-összeggel** (a tételek összege = feltüntetett végösszeg).
3. **Mentsd md/xlsx-be** a saját struktúrátokba (pl. a projekt `Editabil/` mappájába). Onnantól az AI a tiszta adatot olvassa, és a Centralizator/összevetés már a #2 (templét) world-ban megy.
4. **Ne darálj feleslegesen:** ne add be újra meg újra a 225 oldalas képet; a konvertált md a munkapéldány.

## 4. Demo a workshopon (a kontraszt, amit be akarsz mutatni)

- Megnyitjuk a `01_forras_oferta_Napsugar.xlsx`-t (vektoros): tiszta, ingyen, pontos.
- Megnyitjuk a `oferta_szkennelt_Napsugar.pdf`-t: ugyanaz, de **kép** — `pdftotext` 0 karaktert ad.
- Élőben OCR-ezzük (Cowork): kijön a `..._OCR.md`, és megmutatjuk a token-mérleget (fenti tábla) → **„ennyit égetünk, ezért éri meg egyszer konvertálni és md-ben tárolni"**.
- Tanulság: *formátum-triázs* (vektoros vs. szkennelt) + *egyszeri konverzió md-be* + *kontroll-összeg*.

## 5. A teljes fiktív készlet (mind a `fiktiv_pelda/`-ban)

| Fájl | Szerep |
|---|---|
| `01_forras_oferta_Napsugar.xlsx` | forrás-ajánlat (vektoros, strukturált) |
| `02_deviz_general_URES_templet.xlsx` | üres deviz-templét (szürke input, levédett) |
| `03_deviz_general_KITOLTOTT.xlsx` | kitöltött deviz (megoldókulcs) |
| `04_anexaB_uzleti_terv_URES_templet.xlsx` | üres üzleti terv (Ipoteze→Venituri/Cheltuieli/CPP/Indicatori) |
| `05_anexaB_uzleti_terv_KITOLTOTT.xlsx` | kitöltött üzleti terv |
| `oferta_szkennelt_Napsugar.pdf/.png` | **fiktív szkennelt** ajánlat (kép-only, OCR-hez) |
| `oferta_szkennelt_Napsugar_OCR.md` | az OCR-eredmény (md) + kontroll-összeg |

Minden teljesen fiktív, szabadon használható tananyagban / microsite-on.
