---
title: "(Bónusz) Feladat 3.5 — Pályázati kockázat-lista (risk register)"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Pályázati kockázatok azonosítása és kezelési terv készítése az F3 Mobilitate Verde pályázathoz. Tartalmaz 8-10 strukturált kockázatot beadás, elbírálás és megvalósítás fázisokra bontva, valamint priorizálást az AI segítségével."
description_source: auto
description_hash: fdcfb0268b6cf39e
id: efcf060c-b100-4483-837b-f493a8bdc84d
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 3.5 — Pályázati kockázat-lista (risk register)

## Szituáció

Az F3-ban kiderült: pályázhatunk. De **pályázni és nyerni** két különböző dolog. Még megnyert pályázatból is lehet bajunk: ha a feltételek mást jelentenek mint amit gondoltunk, ha az utófinanszírozás megakad, ha lemarad egy határidő.

Egy jó pályázati előkészítés tartalmaz egy **risk register**-t: mi a 5-10 legnagyobb dolog ami félre tudna menni, és mit teszünk ellene.

## Feladat

Kérd meg a Cowork-öt, hogy a pályázati kiírás és a TransOffice cégadatok alapján készítsen kockázati listát.

### Javasolt prompt:

> "Olvasd át a `Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md`-t és a TransOffice cégadatokat. Készíts egy risk register-t a pályázathoz: a 8-10 legnagyobb kockázat **a pályázat beadása ÉS a nyertes pályázat lebonyolítása** alatt.
>
> Minden kockázathoz add meg:
> 1. Kockázat leírása (1 mondat)
> 2. Valószínűség (alacsony / közepes / magas)
> 3. Hatás (alacsony / közepes / magas / kritikus)
> 4. Csillapítás (mit teszünk ELLENE)
> 5. Trigger (mi a jel hogy bekövetkezik)
> 6. Felelős
>
> Csoportosítsd 3 fázis szerint: BEADÁS ELŐTT / ELBÍRÁLÁS ALATT / MEGVALÓSÍTÁS ALATT."

## Elvárt kimenet

`palyazat_risk_register.md` — táblázattal:

### Fázis 1: Beadás előtt

| # | Kockázat | Valószínűség | Hatás | Csillapítás | Trigger | Felelős |
|---|----------|--------------|-------|-------------|---------|---------|
| 1 | Béla bácsi nem ad újabb hosszabbítást | Közepes | Kritikus | Korai egyeztetés Béla bácsival, B-terv: új telephely | Telefonon morog | Márton |
| 2 | Bank nem ad bridge-finanszírozást | Közepes | Magas | 2 banknál párhuzamos kérelem | Visszadobott első kör | Enikő |
| ... | ... | ... | ... | ... | ... | ... |

### Fázis 2: Elbírálás alatt
...

### Fázis 3: Megvalósítás alatt
...

## Extra kihívás

Kérdezd meg a Cowork-öt:
> "A 10 kockázatból melyik 3 az amire ELŐSZÖR fókuszáljunk (legnagyobb hatás × legalacsonyabb csillapítási költség)? Adj sorrendet."

## Tipp

A risk register az egyik dolog, amire **a 200 EUR/nap-os tanácsadók 3 órán keresztül kérnek pénzt**. A Cowork-kel ez 5 perc — és nemcsak listáz, hanem priorizál is.

## Tanulás

- A risk register nem ijesztgetés — **mentális felkészülés**
- A leggyakoribb pályázati hiba: nem az hogy nem készülnek fel, hanem hogy csak a "best case"-re készülnek
- Az AI itt **strukturált gondolkodás-katalizátor** — ami magadtól 2 órás csapatmegbeszélés, AI-val 10 perces tabla
- Egy jó risk register **megérdemli a frissítést havonta** — a Cowork emlékszik, frissíthető
