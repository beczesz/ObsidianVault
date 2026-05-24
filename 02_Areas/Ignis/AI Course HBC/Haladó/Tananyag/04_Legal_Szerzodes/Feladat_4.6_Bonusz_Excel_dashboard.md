# (Bónusz) Feladat 4.6 — Excelből vezetői dashboard

## Szituáció

Az F4.2-ben Mihaela elküldött egy strukturált Excel-t pénzügyi adatokkal. De a nyers Excel **nem mond el semmit** Mártonnak — szám-tenger, oszlopok, sorok.

A Cowork képes az Excel-adatból azonnal **vezetői dashboardot** generálni — egy egyoldalas vizuális összefoglalót, ami a fontos számokat látványosan mutatja.

## Feladat

Vegyél egy számokkal teli Excel-fájlt (lehet TransOffice-ból, lehet saját életedből — banki kivonat, költségvetés, projekt-controlling tábla) és kérd meg a Cowork-öt, hogy dashboard-ot generáljon belőle.

### Forrás lehet:
- TransOffice: `eves_jelentes_2022.xlsx` vagy a Mihaela által visszaküldött Excel
- Saját banki kivonat (CSV vagy XLSX)
- Saját költségvetés-tábla
- Egy projektben használt controlling-tábla
- Egy értékesítési riport

## Hint

Vegyél egy Excel-t (banki kivonat / költségvetés / projekt-controlling — bármi tabular). Kérj egy egyoldalas HTML dashboard-ot: 4 KPI csempe + 1-2 grafikon + 1 'business commentary' bekezdés. Mobile-friendly legyen.


## Elvárt kimenet

`dashboard_[YYYY_MM].html` — egy önálló HTML fájl ami:
- Megnyitható böngészőben
- Vizuálisan vonzó
- 1 képernyőre fér
- Print-barát (PDF-ként ki lehet menteni)

## Extra kihívás

Miután megvan a dashboard, kérdezd meg:
> "Adj egy 'business commentary' szöveget hozzá (max 200 szó) — egy CEO-stílusú elemzés a számok mögötti történetről. Mi a jó, mi az aggasztó, mi a következő lépés?"

A Cowork így nemcsak vizualizál, hanem **értelmezi** is a számokat.

## Tipp

A dashboard HTML formátum azért hasznos, mert:
- Megnyitható bármelyik gépen, nem kell külön szoftver
- E-mailben elküldhető (mellékletként vagy beágyazva)
- PDF-ré nyomtatható
- Reprodukálható havonta (új Excel + ugyanaz a prompt = új dashboard)

## Tanulás

- A Cowork **összekapcsolja az adatot és a vizualizációt** — nincs köztes lépés (Power BI, Tableau, etc.)
- Egy havi dashboard előállítása 2 perc → érdemes **havi rituálévá** tenni
- A "business commentary" az igazi érték: nem a számok, hanem a **mit jelentenek**
- Ha sablonossá teszed, a Cowork akár automatizálhatja (havi scheduled task)
