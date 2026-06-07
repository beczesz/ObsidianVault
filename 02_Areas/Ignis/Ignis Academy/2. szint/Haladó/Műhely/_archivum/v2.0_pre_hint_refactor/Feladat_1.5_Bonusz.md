---
title: "(Bónusz) Feladat 1.5 — Szerződés-kockázatelemzés"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Sürgős kockázatelemzési feladat a BicoToner szerződésről: három forrásból érkezett jelzés a számla eltérésről, a lejárat előtti 90 napos felmondási határidőről (március 3-ig!) és a büntetési kamatokról. Az esperti a szerződést (románul) kell elemezni a Claude-dal, összehasonlítani a PaperWorld feltételekkel, azonosít"
description_source: auto
description_hash: 9d775118689f6710
id: 3228d146-1285-4625-9e43-5827a6024d07
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 1.5 — Szerződés-kockázatelemzés

## Szituáció

Három független forrásból jön a jelzés hogy valami nem stimmel a BicoToner-rel:

1. **Ilona cetlije:** "A BicoToner számla nem stimmel - 15%-ot számolnak de 12% van a szerződésben???"
2. **Márton email-emlékeztetője:** "BicoToner szerződés LEJÁR jövő nyáron (jún 1) - DE 90 nappal előtte kell szólni ha ki akarunk lépni!! Tehát MÁRCIUS ELEJÉIG dönteni kell!!!"
3. **BicoToner fizetési felszólítás emailje:** "...penalitatile de intarziere sunt de 0,1% pe zi... Art. 3.5 suspendare livrari fara notificare..."

Ez sürgős. Ha nem cselekszünk időben, automatikusan megújul egy előnytelen szerződés 2 évre.

## Feladat

Nyisd meg a `szerzodes_BicoToner_2022.docx` fájlt a Claude-dal és kérd meg hogy:

1. **Elemezze a szerződést** kockázati szempontból (románul van — a Claude érti!)
2. **Hasonlítsa össze** a PaperWorld szerződéssel — mi a különbség a feltételekben?
3. **Listázza ki** a problémás/előnytelen pontokat
4. **Javasoljon akciótervet** — mit csináljunk, meddig, mi a határidő?

### Javasolt prompt:

> "Olvasd el a szerzodes_BicoToner_2022.docx fájlt. Ez egy beszállítói szerződés románul. Elemezd kockázati szempontból: milyen problémás vagy előnytelen feltételek vannak benne a mi (TransOffice Trade SRL = Cumpărător) szempontunkból? Hasonlítsd össze a szerzodes_PaperWorld_2021 feltételeivel is. Készíts egy kockázati összefoglalót és akciótervet."

## Elvárt kimenet

### Kockázati összefoglaló

| # | Cikkely | Probléma | Kockázat | Összehasonlítás PaperWorld-del |
|---|---------|----------|----------|-------------------------------|
| 1 | Art. 3.4 | 0,1%/nap büntetés | Dupla a PW-hez képest (0,05%) | PW: 0,05%/nap |
| 2 | Art. 3.5 | Szüneteltetés értesítés nélkül 15 nap után | Szállítás leállhat bármikor | PW: nincs ilyen |
| 3 | Art. 4.3 | 150 RON büntetés ha 8-12 közt nem fogadjuk | Irreális elvárás raktárnál | PW: nincs ilyen |
| 4 | Art. 5.1 | Min. 5000 RON/negyedév kötelezettség | Vásárlási kényszer | PW: nincs minimum |
| 5 | Art. 6.2 | 90 napos felmondás + 2 éves auto-megújulás | Ha lekéssük → 2 év újra | PW: 60 nap + 1 év |
| 6 | Art. 6.3 | 10% exit penalty | Kilépni is drága | PW: 30 nap notif., kész |
| 7 | Art. 7.1 | 70% exclusivity | Nem vehetünk máshonnan tonert | PW: nincs ilyen |
| 8 | Art. 8.1 | Brassói illetékesség | Ha pereskedünk, oda kell menni | PW: Bukarest (szintén nem mi) |

### Akcióterv

| # | Teendő | Határidő | Felelős | Prioritás |
|---|--------|----------|---------|-----------|
| 1 | Ellenőrizni: tényleg 15%-ot számláznak-e (vs szerződéses 15%) | 1 hét | Te + Enikő | Magas |
| 2 | Döntés: felmondani vagy újratárgyalni? | Febr. vége | Márton | KRITIKUS |
| 3 | Ha felmondás: levelet küldeni 90 nappal jún. 1 előtt = **márc. 3-ig!** | Márc. 3. | Márton (aláírás) | KRITIKUS |
| 4 | Alternatív toner-beszállítót keresni | 2 hét | Te | Magas |
| 5 | Jogi konzultáció az exclusivity záradékról | 2 hét | Márton | Közepes |

## Hogyan csináld

1. Add meg a Claude-nak mindkét szerződést
2. Kérd az összehasonlító elemzést
3. Ha a Claude nem találja meg az összeset: "Van-e olyan cikkely ami kiszolgáltatottá tesz minket? Mi történik ha késve fizetünk?"
4. Az akciótervet kérd konkrét dátumokkal

## Tanulás

- **AI mint jogi első-szűrő** — nem helyettesíti az ügyvédet, de percek alatt kiszúrja a red flag-eket
- **Többnyelvű elemzés** — a szerződés románul van, az összefoglaló magyarul → az AI fordít és elemez egyszerre
- **Összehasonlító elemzés** — két dokumentum egymás mellé tétele → ami kézzel fél óra, AI-val 2 perc
- Előkészítés a **Fázis 4-re** (Legal plugin) — ott majd pluginnal csináljuk ugyanezt, strukturáltabban
