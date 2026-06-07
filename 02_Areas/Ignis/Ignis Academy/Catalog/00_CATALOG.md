---
title: Ignis Academy — Képzési katalógus
date: 2026-05-29
author: Becze Szabolcs
status: active
version: 0.1.0
description: Az Ignis Academy (az Ignis ernyőmárka profit-orientált képzési ága) teljes képzési katalógusának forrás-az-igazságra indexe. Ernyő-pozicionálás + 2 szolgáltatás-vonal (AI-kompetenciák, Szervezetfejlesztés) + 4 képzés egységes metaadattal. Ezt olvassa a tervezett ignis-academy.html dashboard.
id: be0238d7-068a-4310-bc39-33ed3f10f1d5
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, catalog, kepzes, positioning]
---

# Ignis Academy — Képzési katalógus

> **Forrás-az-igazságra.** Ez a fájl + a `Catalog/*/COURSE.md` per-képzés fájlok adják a teljes
> kínálat strukturált képét. A tervezett `_dashboards/ignis-academy.html` dashboard ezt rendereli
> (per-record pattern). A nehéz tananyagok a helyükön maradnak; innen `lives_in` linkkel hivatkozunk rájuk.

## Márka-architektúra

```
IGNIS  (egységes ernyőmárka)
├── IgnisCafe        — közösségi tér (nonprofit / közösségi)  → 02_Areas/Ignis/IgnisXY/
└── Ignis Academy    — profit-orientált képzések              → ITT
    ├── 1. vonal · AI-kompetenciák          → Tájoló · Műhely · Műhely+
    └── 2. vonal · Szervezetfejlesztés      → A 7 szokás
```

## Ernyő-pozicionálás (Ignis Academy)

- **Market category:** gyakorlati digitális munkamódszerek és modern eszközhasználat (NEM „AI képzés").
- **Best-fit ügyfél:** digitálisan bizonytalan, nem-technikai tudásmunkás és KKV-vezető (35-55), a „digitális bizonytalanság" tengely mentén, nem korosztály szerint.
- **Villain (Miller):** a digitális káosz + a lemaradástól való félelem + „túl sok eszköz egyszerre".
- **Vezérelv:** az AI nem a termék, hanem eszköz egy jobb munkavégzéshez. Bizalmi oktatási márka, anti-hype.
- **Ernyő-tagline:** ⏳ döntésre vár (jelöltek a `Brand/05_ERNYO...`-ban; ChatGPT a „bizalmi" irányt ajánlotta).

## A kínálat (4 képzés)

| # | Képzés | Vonal | Szint | Forma | Státusz | Ár | Részletek |
|---|---|---|---|---|---|---|---|
| 1 | **Tájoló** | AI-kompetenciák | belépő | self-serve (PDF + 24 slide + webinar) | ✅ él | TBD | [tajolo/COURSE.md](tajolo/COURSE.md) |
| 2 | **Műhely** | AI-kompetenciák | core | élő 4h workshop (10-15 fő) | ✅ kész | TBD | [muhely/COURSE.md](muhely/COURSE.md) |
| 3 | **Műhely+** | AI-kompetenciák | haladó | TBD (specializált) | ⏳ tervezett | TBD | [muhely-plus/COURSE.md](muhely-plus/COURSE.md) |
| 4 | **A 7 szokás** | Szervezetfejlesztés | prémium | 1 napos vezetői tréning | ⏳ tervezett | TBD | [het-szokas/COURSE.md](het-szokas/COURSE.md) |

> **Tájoló és Műhely NEM szekvenciális** (nem kezdő→haladó). Két párhuzamos tengely:
> Tájoló = *hogyan gondolkodj* AI-jal (időtálló mindset), Műhely = *hogyan dolgozz* AI-jal (eszközfüggő praxis).
> Cross-sell: Tájoló → vágy a Műhelyre (felemelő funnel); Műhely → ráismerés a Tájolóban (mélyítő funnel).

## Szint-modell (a `tier` mező magyarázata)

| tier | Jelentés | Belépési küszöb |
|---|---|---|
| `belepo` | gondolkodási alap, alacsony elköteleződés | self-serve, olcsó/ingyenes |
| `core` | megtapasztaló, fő transzformáció | élő, közepes ár |
| `halado` | specializált elmélyítés | élő, magasabb ár |
| `premium` | vezetői, prémium pozícionálás | 1 nap, prémium ár |

## Nyitott kérdések (a kínálat szintjén)

1. **Árazás** — egyik képzésnek sincs ára. Tájoló+Műhely bundle ár? (lásd messaging Q4)
2. **Végleges nevek** — „Tájoló" és „Műhely" munkanevek.
3. **Saját vizuális identitás** — a képzési márkának nincs logója/színe/tipója (jelenleg kölcsönzött partner-arculat).
4. **Műhely+ specializáció** — marketing / üzletfejlesztés / általános haladó? (D2)
5. **7 szokás besorolás** — az Ignis Academy alá, vagy önálló prémium vonal? (D3) — jelen modellben az Ignis Academy 2. vonala.
6. **Ernyő-tagline** döntés (D1).
7. **SaaS-folder reconciliation** — a `02_Areas/Ignis Academy/` (EU-pályázatos B2B SaaS platform) viszonya ehhez a képzési ághoz tisztázandó; jelen Catalog NEM érinti azt a mappát.

## Kapcsolódó anyagok

- Pozicionálás / messaging / design: `02_Areas/Ignis/Ignis Academy/2. szint/Pozicionalas/`
- Műhely teljes tananyaga: `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/`
- 7 szokás forrás: `02_Areas/Szervezet Fejlesztés/7 Szokás képzés.md`
- One-pager prototípus: `02_Areas/Ignis/Ignis Academy/2. szint/Pozicionalas/04_one-pager_v0.1.html`
