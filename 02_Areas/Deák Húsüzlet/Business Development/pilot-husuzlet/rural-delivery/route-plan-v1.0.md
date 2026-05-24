# Falusi Route — Útvonal dokumentáció

**Dátum:** 2026-05-02
**Forrás:** Google Maps útvonaltervezés (Szabolcs által megtervezett)
**Kapcsolódó spec:** `rural-route-spec-v1.0.md`
**Jira:** DH-184

---

## Útvonal áttekintés

**Típus:** Körkörös hurok (loop) — Székelyudvarhelyről indul, Székelykeresztúr felé megy, majd visszatér Udvarhelyre
**Kiindulópont:** Székelyudvarhely (Deák Húsmíves üzem)
**Célpont (fordulópont):** Cristuru Secuiesc (Székelykeresztúr)
**Teljes távolság:** ~55 km
**Menetidő megállás nélkül:** ~1 óra 5 perc
**Becsült menetidő kiszállításokkal:** ~3-4 óra (megállók számától függően)
**Főbb utak:** DJ 137 (déli szár), DJ 13C (északi szár), DJ 13A (visszaút)

---

## A hurok logikája

Székelyudvarhely egy kisváros (~31.000 lakos). A route egy hurkot ír le délnyugati irányba Székelykeresztúr felé, majd északon vissza:

```
         SZÉKELYUDVARHELY (start/finish)
            ↓                    ↑
    [déli szár - DJ 137]    [északi szár - DJ 13C/13A]
            ↓                    ↑
        Feliceni             Bulgăreni/Bisericani
            ↓                    ↑
        Tăureni              Morăreni
            ↓                    ↑
         Mugeni              Mihăileni
            ↓                    ↑
        Dejuțiu              Cobătești
            ↓                    ↑
    Porumbenii Mari          Şimonești
            ↓                    ↑
    Porumbenii Mici          Rugănești
            ↓                    ↑
        Beteşti                  ↑
            ↓                    ↑
        SZÉKELYKERESZTÚR ────────┘
           (fordulópont)
```

**Lényeg:** A sofőr Udvarhelyről elindul déli irányba a 137-es úton, végigmegy a falvakon, elér Székelykeresztúrra (fordulópont), majd az északi 13C/13A úton más falvakon keresztül jön vissza Udvarhelyre. Egy teljes kör, nem kell ugyanazon az úton visszajönni.

---

## Települések az útvonal mentén

### Déli szár: Udvarhely → Székelykeresztúr (DJ 137)

| # | Település (RO) | Település (HU) | Típus | Megjegyzés |
|---|----------------|-----------------|-------|------------|
| — | **START: Székelyudvarhely** | **Székelyudvarhely** | Kisváros | Deák Húsmíves üzem — indulás |
| 1 | Feliceni | Felsőboldogfalva | Falu | |
| 2 | Tăureni | Bikafalva | Falu | |
| 3 | Mugeni | Bögöz | Község | Nagyobb település |
| 4 | Dejuțiu | Dezsőfalva | Falu | |
| 5 | Porumbenii Mari | Nagygalambfalva | Falu | |
| 6 | Porumbenii Mici | Kisgalambfalva | Falu | |
| 7 | Beteşti | Betfalva | Falu | Székelykeresztúr előtt |
| 8 | **Cristuru Secuiesc** | **Székelykeresztúr** | **Kisváros** | **Fordulópont (~8.800 lakos)** |

### Északi szár: Székelykeresztúr → vissza Udvarhelyre (DJ 13C / 13A)

| # | Település (RO) | Település (HU) | Típus | Megjegyzés |
|---|----------------|-----------------|-------|------------|
| 9 | Rugăneşti | Rugonfalva | Falu | |
| 10 | Şimoneşti | Siménfalva | Falu | |
| 11 | Cobăteşti | Kobátfalva | Falu | |
| 12 | Mihăileni | Csíkszentmihály | Falu | |
| 13 | Morăreni | Malomfalva | Falu | |
| 14 | Bulgăreni / Bisericani | — | Falu | Visszaút Udvarhelyre |
| — | **FINISH: Székelyudvarhely** | **Székelyudvarhely** | Kisváros | Visszaérkezés |

---

## Route economics (korrigált, 55 km)

| Tétel | Összeg |
|-------|--------|
| Üzemanyag (~55 km) | ~55 RON |
| Sofőr (3-4 óra x 30 RON) | ~100-120 RON |
| Amortizáció + egyéb | ~25 RON |
| **Összes OPEX / route** | **~190 RON** |

| Rendelés/route | Költség/rendelés | Fedezet (120 RON AOV, 20% margin) | Eredmény |
|---------------|-----------------|-----------------------------------|----------|
| 5 | 38 RON | 24 RON | **-14 RON** |
| 8 | 24 RON | 24 RON | **±0 (breakeven)** |
| 10 | 19 RON | 24 RON | **+5 RON** |
| 15 | 12,7 RON | 24 RON | **+11,3 RON** |

**Breakeven:** ~8 rendelés/route (korrigált, alacsonyabb OPEX a rövidebb táv miatt).

---

## Phase 1 — javasolt 3 megállópont

A teljes 14 település helyett 3 stratégiai megálló az induláshoz:

| Prioritás | Település | Szár | Miért |
|-----------|-----------|------|-------|
| **P1** | **Cristuru Secuiesc** | Fordulópont | Legnagyobb (~8.800 lakos), kisváros |
| **P2** | **Mugeni / Bögöz** | Déli | Nagyobb község a déli száron |
| **P3** | **Şimoneşti** | Északi | Nagyobb falu az északi száron |

---

## Versenytárs-check

A route-on **NINCS** szervezett hússzállítási szolgáltatás. Kaufland/Lidl csak Udvarhelyen, Bringo/Tazz nem megy ki falvakra, helyi boltok nem szállítanak. Kék óceán.

---

## Szezonalitás

| Időszak | Hatás |
|---------|-------|
| Ősz-tél (okt-feb) | **Csúcs** — több főzés, nincs házi vágás |
| Tavasz (márc-ápr) | Közepes — húsvéti csúcs |
| Nyár (máj-szept) | **Mélypont** — házi vágás, kert, grillezés |
