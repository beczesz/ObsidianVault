# (Bónusz) Feladat 6.3 — Mobile-first variáns

## Szituáció

Az F6.1-ben generáltunk 3 desktop variánst. De **Romániában a B2B forgalom 65%-a mobiltelefonról jön** (Eurostat 2024). A „desktop első, mobil utána" megközelítés nem működik — **mobile-first** kell.

A Cowork-kel pár perc alatt át lehet alakítani az egyik variánsot mobile-első dizájnra.

## Feladat

Vedd az F6.1-ben kedvencednek talált variánst (Modern / Klasszikus / Erdélyi) és kérd meg a Cowork-öt, hogy alakítsa át **mobile-first** szemléletre.

## Hint

Vedd a kedvenc Modern/Klasszikus/Erdélyi variánsodat, és kérj egy mobile-first változatot: 375px-re optimalizálva, hamburger menü, bottom-bar CTA, lazy image loading. Teszteld Chrome DevTools mobile view-ban.


## Elvárt kimenet

`website/redesign/v_mobile_first.html` — egy önálló HTML fájl ami:
- Megnyitható mobilon (DevTools-ban is)
- Egy ujjal navigálható
- A fontos CTA gombok ergonomikus helyen vannak
- 3G-internet esetén is gyorsan tölt

## Tipp: hogyan teszteled

1. Nyisd meg böngészőben (Chrome / Safari)
2. Right-click → Inspect → Device toolbar (Cmd+Shift+M Mac, Ctrl+Shift+M Windows)
3. Válassz: iPhone SE (375px) vagy Pixel 5 (393px)
4. Próbálj végigscrollozni egy ujjal (egér helyett)
5. Próbáld megnyomni a CTA gombokat — könnyen találhatóak?

## Extra kihívás

> "Most készíts egy A/B-teszt vázlatot: ha mind a desktop, mind a mobile-first verziónk élesben lenne, **mit mérnél?** Listázz 5 metrikát (pl. bounce rate, scroll depth, CTA click-through) és **hogyan mérnéd ezt a Google Analytics 4-ben**."

## Tanulás

- **Mobile-first ≠ responsive** — ez egy más megközelítés (kis képernyőből építünk fel, nem kicsinyítünk)
- A Cowork az `@media` query-k mellett **strukturális változtatásokat** is megcsinál (nav→hamburger, multi-col→single-col)
- A bottom-bar CTA Romániában különösen hatékony — a felhasználók egyik kezükkel telefonálnak
- A mobile-first SEO-előny is: a Google **mobile-first indexing**-et használja 2020 óta
