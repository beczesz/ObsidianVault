# Feladat 4.2 (Stáció 4.B) — EBITDA margin saját számítás

> **Típus:** ⏸ STÁCIÓ — saját laptopon, copy-paste prompt
> **Idő:** ~3 perc · **Mód:** egyénileg

---

## Szituáció

Az oktató épp megmutatta:
1. Hogyan írt **románul** emailt Mihaelának (a külsős könyvelőnek) a pénzügyi adatok megkérésére
2. Mihaela 2 nappal később visszaküldte a `bilant_TransOffice_2024_2025.xlsx` fájlt
3. A Cowork élesben kiszámolta a fő KPI-okat: árbevétel, EBITDA, alkalmazottak — 2024 vs 2025 trend

Most ti következtek **egyetlen szám kiszámolására**: a **2024-es EBITDA margin** (%-ban).

---

## A stáció prompt

A `bilant_TransOffice_2024_2025.xlsx`-et a saját Cowork-edben már ismered (a kivetítőn az oktató behúzta — neked is van rá hivatkozás a CLAUDE.md-ben).

Másold ki és illeszd be a saját Cowork-jébe:

```
A Mihaelától kapott bilance-Excel alapján: számítsd ki az EBITDA
margint 2024-re (%-ban). Mutasd meg a képletet és az eredményt
1 mondatban.
```

---

## Elvárt eredmény

A Cowork 15-30 másodperc alatt:
- Megnyitja a `bilant_TransOffice_2024_2025.xlsx`-et
- Megmutatja a képletet (`EBITDA / Árbevétel × 100`)
- Egy konkrét %-os választ ad — pl. „4,6%"
- 1 mondatban

---

## A WOW-pillanat — közös ellenőrzés (1 perc)

Az oktató: *„Aki kész, mondja az eredményt szóban."* — 2-3 ember válaszol.

- **Ha mindenki ugyanazt mondja:** *„Látjátok? **Ugyanaz**."* — érzitek a determinizmust.
- **Ha valaki más számot mond:** *„Érdekes — miért?"* — vita-momentum az árbevétel-rendezetlenség vagy egyéb miatt.

---

## Tipp

Ha a Cowork **bizonytalan a számokban** (pl. „nem találom az árbevételt"), kérdezz vissza: *„Nézd meg a P&L lapot, a 'Cifra de afaceri' sorban."*

Ha az **EBITDA-t nem tudja kiszámolni közvetlenül**, mondd: *„Számítsd ki: Profit Brutto + Amortizare + Cheltuieli cu dobânzile."*

---

## Tanulás

- **Az AI mint Excel-elemző:** nem csak megnyit egy spreadsheet-et — **érti a kontextust**. „EBITDA" → automatikusan tudja melyik képlet kell.
- **A számológép-élmény:** régen ez egy könyvelő munkája volt. Most a Cowork **5 másodperc alatt**.

---

## Otthoni elmélyítés

A saját Excel-jeiddel — bónusz feladatok:
- `Feladat_4.6_Bonusz_Excel_dashboard.md` — banki kivonatból vezetői dashboard
- `Feladat_4.7_Bonusz_Prezi_celkozonseg.md` — prezentáció 3 célközönségnek

---

**Verzió:** 2.0 (Stáció modell)
