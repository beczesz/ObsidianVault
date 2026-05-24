# (Bónusz) Feladat 2.3 — Email-szál TODO-k

## Szituáció

A meeting transcript nem az egyetlen forrás. A napi munka 80%-a emailben zajlik — és minden Outlook/Gmail-szál tele van rejtett feladatokkal: "majd visszahívlak", "küldd át a számlát", "kérdezd meg Enikőt erről". Ezek soha nem kerülnek a TODO listára, és pont ezek esnek ki.

A Productivity plugin nem törődik vele, honnan jön a szöveg — bármilyen szöveg-bemenetből kinyeri a feladatokat.

## Feladat

Vegyél egy saját email-szálat (vagy másold be egy fiktív, 5-8 emailes szálat — pl. egy ügyfél kommunikációt egy projektről) és kérd meg a Cowork-öt, hogy:

1. Olvassa végig az egész szálat
2. Nyerje ki a vállalt és kiosztott feladatokat
3. Mentse el a Productivity plugin-be — ki, mit, mikorra

### Javasolt prompt:

> "Itt egy 8 emailes szál egy ügyféllel egy weboldal-projektről. Olvasd át kronologikus sorrendben, és nyerd ki MINDEN feladatot ami benne van — vállalásokat, kéréseket, határidőket. Mentsd el TODO-ként: Ki → Mit → Mikorra → Státusz. A homályosakat is jelöld meg (státusz: 'tisztázandó')."

## Elvárt kimenet

A Productivity plugin-ben elmentett TODO lista:

| # | Ki | Mit | Mikorra | Forrás (email tárgy) | Státusz |
|---|----|----|---------|----------------------|---------|
| 1 | Én | Árajánlat küldés | 2025-03-05 | „Re: Új honlap igények" | nyitott |
| 2 | Ügyfél | Logó vector átküldése | határidő nincs | „Logó" | tisztázandó |
| 3 | Én | Visszahívni Tibit | hét végéig | „Telefonhívás" | nyitott |

## Tipp

Ha nincs valós email-szálad amit szeretnél megosztani, használhatsz egy fiktív sablont — pl. egy ügyfél-kommunikációt egy weboldal projektről, vagy egy beszállító egyeztetést. A lényeg, hogy 5+ üzenet legyen benne, többszereplős.

## Tanulás

- A Productivity plugin **forrás-agnosztikus** — meeting, email, Slack, jegyzet, bármi
- Az emailekben rejtett feladatok kinyerésével **havonta 10-20 elveszett TODO-t** lehet megmenteni
- A "tisztázandó" státusz egy fontos AI-érték: az ember szövegben megengedi a homályt, az AI explicitté teszi
