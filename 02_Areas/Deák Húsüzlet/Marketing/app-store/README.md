---
title: DH App Store Assets
date: 2026-05-12
author: Becze Szabolcs
status: draft
description: Play Store / App Store feltöltéshez generált asset csomag — 512×512 app icon + 1024×500 feature graphic (cream és burgundy variáns, HU és RO nyelv). Hibrid megközelítés: pig mascot az iconon, tisztán tipografikus feature graphic-ok.
version: 0.3
id: 06a2ad6e-82e8-4e6a-b988-9d4ce592f768
index_schema_version: 1
---

# DH App Store Assets — v0.3

Play Store és (későbbi) App Store listing feltöltéshez. Renderelt PNG-k az `out/`-ban, HTML source-k a `source/`-ban.

## Changelog

- **v0.3.1 (2026-05-12, jelen):** Icon redesign — mascot 88% → 74% + upward bias (top 8%, bottom 18%). Az előző verzióban a thumbs-up glove cuff a launcher edge-nél ragadt, "alja le van vágva" perception.
- **v0.3 (2026-05-12):** Hibrid — pig mascot **csak az iconon** (cream/white háttéren), feature graphic-ok visszaállítva a v0.1 tipografikus verzióra.
- **v0.2 (2026-05-12):** Pig mascot központi vizuális elemnek mindenhol (visszavonva v0.3-ban — feature graphic-on Szabolcs jobban szerette a tipografikus verziót).
- **v0.1 (2026-05-12 reggel):** Első verzió — DH monogram icon + tisztán tipografikus feature graphic.

## Mappastruktúra

```
Marketing/app-store/
├── README.md                              ← ez a fájl
├── source/                                ← HTML forrásfájlok + asset eszközök
│   ├── deak_face_logo.png                 ← Szabolcs választotta mascot (eredeti, RGB)
│   ├── pig-mascot.png                     ← előfeldolgozott mascot RGBA-val (alpha = transparent bg)
│   ├── icon.html                          ← AKTÍV: pig mascot icon
│   ├── icon-dh-monogram.html              ← FALLBACK: DH monogram (design-system §10 konform)
│   ├── feature-graphic-cream-hu.html
│   ├── feature-graphic-cream-ro.html
│   ├── feature-graphic-burgundy-hu.html
│   ├── feature-graphic-burgundy-ro.html
│   ├── render.js                          ← headless Chrome → PNG renderer
│   └── _extract-mascot.html               ← (archived, lásd lent — nem fut a renderben)
└── out/                                   ← deploy-ready PNG-k
    ├── icon-512.png                       ← 512×512, ~142 KB
    ├── feature-graphic-cream-hu.png       ← 1024×500, ~320 KB
    ├── feature-graphic-cream-ro.png       ← 1024×500, ~321 KB
    ├── feature-graphic-burgundy-hu.png    ← 1024×500, ~242 KB
    └── feature-graphic-burgundy-ro.png    ← 1024×500, ~244 KB
```

## Mascot előfeldolgozás workflow

A `deak_face_logo.png` az eredeti, **fehér háttérrel** (RGB, alpha nélkül). Erre szükség van egy transzparenciára-alakítás lépésre, hogy burgundy felületen ne legyen fehér négyzet a malac körül.

**Eszköz:** `C:\Users\EvoComputers\tmp-img-proc\extract-mascot.js` (npm install jimp csak ASCII-only path-on működik a vault Unicode-name miatt — ezért külön mappa).

**Algoritmus:**
1. Olvas a `deak_face_logo.png`-ből (2000×2000 RGB)
2. Flood-fill a négy sarokról csak fehér-küszöbös (R,G,B ≥ 240) pixeleken keresztül
3. A flood-elérhető pixelek alpha = 0 → háttér transzparens
4. A nem-elérhető fehér pixelek (chef hat, glove) **megmaradnak** opaque-ként
5. Anti-alias edge cleanup: szegélyen lévő közel-fehér pixelek puha alpha fade
6. Kiment `pig-mascot.png` (2000×2000 RGBA)

**Eredmény:** 44.5% pixel transparent (külső háttér), a kalap + kesztyű épségben marad.

Mikor kell újra futtatni:
```bash
cd ~/tmp-img-proc && node extract-mascot.js
```
→ csak akkor, ha a forrás `deak_face_logo.png` frissül.

## Asset specifikációk

### App icon — `out/icon-512.png`

| Mező | Érték |
|---|---|
| Méret | 512 × 512 px |
| Formátum | PNG (RGB) |
| Háttér | Cream `#FFFBF7` edge-to-edge + nagyon halvány burgundy-tinted vignette — Adaptive Icons-barát |
| Tartalom | Pig mascot (`pig-mascot.png`) 74%-os méretben, top 8% / left 13% pozícióval (upward bias) |
| Margók | Top ~8%, oldalak ~13%, **bottom ~18%** — szándékosan nagyobb alul, hogy a thumbs-up glove cuff ne ragadjon a launcher mask szélére |
| Shadow | drop-shadow(0 6px 16px rgba(60,30,30,0.12)) |

**Miért NEM rounded square?** A Google Play Adaptive Icons rendszere a launcheren maszkolja a sarkokat (kör, squircle, rounded rect — eszközfüggő). A feltöltött PNG-nek edge-to-edge szín-kitöltése kell legyen.

**Miért fehér (cream) háttér?** Szabolcs döntése — a mascot tisztán látszik egy semleges felületen, a kalap + kesztyű fehér részei kontrasztban maradnak a cream-tinted háttéren. (DESIGN.md §10 a malacot a PWA UI-ban tiltja, de Play Store launcher icon = marketing surface, ez engedélyezett.)

### Feature graphic — 4 variáns (tipografikus, mascot nélkül)

| Fájl | Háttér | Nyelv | Tipográfiai stratégia |
|---|---|---|---|
| `feature-graphic-cream-hu.png` | Cream `#FFFBF7` + paper grain | HU | Playfair-led, editorial. Centered wordmark 96px serif + italic tagline. |
| `feature-graphic-cream-ro.png` | Cream `#FFFBF7` + paper grain | RO | Ugyanaz, RO adaptáció (NEM fordítás). |
| `feature-graphic-burgundy-hu.png` | Burgundy `#9B2335` + warm noise | HU | Inter-led, confident modern. Centered wordmark 88px sans + medium tagline. |
| `feature-graphic-burgundy-ro.png` | Burgundy `#9B2335` + warm noise | RO | Ugyanaz, RO adaptáció. |

| Mező | Érték |
|---|---|
| Méret | 1024 × 500 px |
| Formátum | PNG (no transparency required) |
| Safe zone | Központi ~670×400 (a wordmark a bal 55%-ban, a mascot jobb 45%-ban — ha Google levág 100px-t bal-jobbról, mindkettő bent marad) |

## Impeccable design critique — `deak_face_logo.png`

Mielőtt elindultam a változtatással, a brand dokumentációra alapozva előírtam pár konfliktust. **Szabolcs explicit kéri a mascot lecserélést — ezt a döntést hajtom végre. A critique-ot azonban dokumentálom, mert a brand-rendszer ezt megköveteli.**

### Konfliktusok

1. **DESIGN.md §10 explicit:**
   > „A malac illusztráció **kizárólag print/marketing** — soha nem jelenik meg a PWA-ban"
   - **Feature graphic:** marketing surface → ✓ kompatibilis
   - **App icon:** a launcher-ikon UI-jellegű surface → ⚠️ design-system saját szabályával ellentétes
   - **Mitigation:** a Play Store icon nem ugyanaz, mint a PWA in-app icon. A user mobiltelefonján a Play Store-ról telepített app launcher icon-ját látja, ami marketing-near surface.

2. **PRODUCT.md design principle 5:** „Not rustic, not artisanal-cliché."
   - A thumbs-up-os, kalapos malac mascot a klasszikus "rustic butcher mascot" template, amit a PRODUCT.md kerülendőnek minősít.
   - **Mitigation:** kisvárosi (Székelyudvarhely) közönség, ahol az ismerős-jellegű mascot magasabb felismerhetőséget adhat, mint egy absztrakt monogram. Helyi kontextusban a "cuki" jobban működik.

3. **Brand voice §2 — három tengely (Egyszerű · Gyakorlatias · Nyugodt):**
   - A thumbs-up gesture egy fokkal salesman-pitch ("szuper, vegyél!"), feszül a "nyugodt" tengellyel.
   - **Mitigation:** a feature graphic-ban a wordmark dominálja a balra-eső térfelet, a mascot kiegészítő. A "calm confidence" tipográfiailag tartva.

4. **DESIGN.md banned patterns:** "Emoji anywhere in the app UI"
   - Thumbs-up gesture cartoon-szerű, emoji-rokon. A design-system tilolistájával rokon.
   - **Mitigation:** ez a DESIGN.md UI rule, NEM app store marketing asset rule.

### Conclusion

Szabolcs döntése áll. Az asset legenerálva. **DH monogram fallback megőrizve** `source/icon-dh-monogram.html`-ben — ha bármikor át akarunk térni (vagy a Play review elutasítja a cartoon mascotot), egy render parancs elég.

## Design rationale — két variáns, két hangulat

A két háttérvariáns NEM csak színswap. Két különböző brand-perszonalitást tesztel:

| Variáns | Tipográfia | Hangulat |
|---|---|---|
| **Cream** | Playfair Display 800 wordmark + italic tagline | Editorial, magazine-cover, csendes magabiztosság |
| **Burgundy** | Inter 800 wordmark + medium tagline | Modern, magabiztos, közvetlen |

A burgundy verzióban szándékosan **Inter-led** a tipográfia (nem Playfair), hogy ne essen bele a PRODUCT.md anti-reference-ébe ("Premium artisan e-commerce, serif-everything"). A cream marad Playfair, mert ott az editorial regiszter működik.

## Em-dash bann — kanonikus brand voice tagline

A kliens javasolt tagline („Friss hús – házhozszállítva") en-dasht használ. A brand voice §15 és az impeccable shared design laws is **tiltja**.

Az asset **a kanonikus brand voice fő headline-t használja** (brand_voice_v2.0 §14):
- HU: **„Friss. Tiszta. Házhoz."**
- RO: **„Proaspăt. Curat. Acasă."** (adaptáció, nem fordítás)

## Színek (DESIGN.md tokenek)

| Hex | Token | Hol használjuk |
|---|---|---|
| `#FFFBF7` | `--cream` | Cream variáns háttér + burgundy variáns wordmark |
| `#9B2335` | `--primary` | Burgundy variáns háttér + app icon háttér |
| `#7D1A2A` | `--primary-800` | Cream variáns wordmark |
| `#D4A574` | `--secondary` (Warm Sand) | Hairline rule, accent dots — minden variánsban |
| `#5C544C` | text-secondary | Cream variáns tagline szöveg |
| `#9C7841` | `--secondary-dark` | Cream variáns eyebrow letter-spaced caps |
| `#F4A3AF` | `--primary-400` | Burgundy variáns eyebrow + footer (pale rose tint) |

Nincs `#000` és nincs `#FFFFFF` — minden neutral warm-tinted, a DESIGN.md szabálya szerint.

## Tipográfia

| Variáns | Wordmark | Tagline | Eyebrow / footer |
|---|---|---|---|
| Cream | Playfair Display 800, 96px, −3 letter-spacing, primary-dark, egysoros | Playfair italic 700, 28px, neutral-secondary | Inter 500/600 caps, 12px, +4 letter-spacing |
| Burgundy | Inter 800, 88px, −3.5 letter-spacing, cream, egysoros | Inter 500, 26px, +0.5 letter-spacing, cream | Inter 600 caps, 12px, +5 letter-spacing |

Inter és Playfair Display ugyanaz a két font család, ami az app belsejében is fut (DESIGN.md §1). Cross-asset consistency.

## Play Console upload — útmutató

1. **Bejelentkezés:** [Play Console](https://play.google.com/console/) → DH developer account (DH-135 ticket még To Do — accountot regisztrálni kell, ha még nem történt meg).
2. **App létrehozása** (ha még nincs): `Create app` → name: **Deák Húsmíves**, default language: `Hungarian (hu-HU)`.
3. **Store listing → Main store listing:**
   - **App icon:** `out/icon-512.png`
   - **Feature graphic:** kezdetnek a **`feature-graphic-burgundy-hu.png`** (vagy `cream-hu` — Szabolcs választja)
4. **Localizations → Add language → Romanian (ro):**
   - **Feature graphic:** `feature-graphic-burgundy-ro.png` (vagy `cream-ro`, párosítsuk a HU választással)
5. **Title, short description, full description** — külön deliverable (`Marketing/app-store/store-listing-copy.md`, még nincs kész).

### Apple App Store (későbbre, Sprint 4 alatt)

- App icon: 1024 × 1024 (rounded square — iOS már nem maszkol annyira, mint Android adaptive)
- Screenshot set per device class (iPhone 6.7", 6.5", 5.5"; iPad 12.9", 12.9"-2 gen)
- Külön deliverable, itt nincs benne. A Sprint 4 v0.4 natív mobil release körül készül.

## Iteráció / újrarenderelés

Source HTML módosítás után:

```bash
node "C:/Users/EvoComputers/Obsidian/ideas-vault/02_Areas/Deák Húsüzlet/Marketing/app-store/source/render.js"
```

(A Unicode path miatt abszolút úttal hívd. A render.js maga relatív path-okat használ belül.)

## Icon fallback aktiválása

Ha a Play review elutasítja a cartoon mascotot, vissza tudunk térni a DH monogramra:

1. `cp source/icon-dh-monogram.html source/icon.html` (a monogram váltja a mascotot)
2. Re-render: `node "C:/Users/EvoComputers/Obsidian/ideas-vault/02_Areas/Deák Húsüzlet/Marketing/app-store/source/render.js"`

A feature graphic-ok már tipografikusak, semmi mascot — Play review-val nincs gondjuk.

## Nyitott döntések

- [ ] **Háttér variáns választás** — cream vs. burgundy → main HU + RO graphic
- [ ] **Mascot vs. monogram** — Play review után visszamehetünk monogramra, ha kell
- [ ] **Store listing copy** — title, short desc (80 char), full desc (4000 char) HU + RO
- [ ] **Screenshots set** (Play Store: min 2, max 8 screenshot a v0.3 app főképernyőiről)

## Kapcsolódó dokumentumok

- [`design/DESIGN.md`](../../design/DESIGN.md) — design system tokenek; **§10 explicit ban a malacra in-app**, marketing-ban engedélyezett
- [`design/PRODUCT.md`](../../design/PRODUCT.md) — brand context, anti-references
- [`Marketing/Brand/brand_voice_v2.0.md`](../Brand/brand_voice_v2.0.md) — voice spec, tagline kanonika
- [`Marketing/Brand/vizualis_identitas.md`](../Brand/vizualis_identitas.md) — ⚠️ régi palettával (`#C0392B`) — friss release után frissítendő `#9B2335`-re
- [`Marketing/Deák Logo Final.svg`](../Deák%20Logo%20Final.svg) — kanonikus logó (bikafej + wordmark)
- [`Marketing/deak_face_logo.png`](../deak_face_logo.png) — Szabolcs választotta mascot
- Jira: **DH-135** (App Store developer account) — még To Do
