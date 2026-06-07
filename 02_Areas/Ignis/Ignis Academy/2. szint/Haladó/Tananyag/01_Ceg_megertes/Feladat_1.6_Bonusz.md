---
title: "(Bónusz) Feladat 1.6 — Pályázati one-pager"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Professzionális egy oldalas pályázati dokumentum sablonja a TransOffice Trade SRL számára, amely tartalmazza a cég bemutatását, jelenlegi működési helyzetét, digitalizációs igényeket és pályázati célokat potenciális tanácsadó előtt."
description_source: auto
description_hash: 4c01fc0d64b374d1
id: 61d29c49-5f49-463f-a73c-e60f5f3f39e5
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 1.6 — Pályázati one-pager

## Szituáció

Csütörtök van. A meeting a pályázati tanácsadóval 2 óra múlva. Márton szól:

> "Csináltál összefoglalót ugye? Az jó nekem, de kéne valami ami profibb — egy one-pager amit odaadok a tanácsadónak. Olyasmi mint egy pitch: ki vagyunk, hol tartunk, mire kérnénk pénzt. Max 1 oldal, legyen profi kinézetű. Ha van rajta a logónk is, az extra."

## Feladat

Készíts egy 1 oldalas, professzionális dokumentumot (Word) a pályázati tanácsadó számára, a korábbi feladatokból összegyűjtött információk alapján.

### A one-pager tartalmazzon:

1. **Fejléc** — TransOffice Trade SRL, Székelyudvarhely (+ cím, telefon, email)
2. **Cég bemutatkozás** (2-3 mondat) — mit csinálunk, mióta, mekkora piac
3. **Számok** — árbevétel, ügyfelek száma, alkalmazottak, területi lefedettség
4. **Jelenlegi helyzet** — hogyan működik most (Excel, papír, email → nincs rendszer)
5. **Digitalizációs igények** — konkrét lista (CRM, raktár, weboldal, folyamat-automatizálás)
6. **Pályázati cél** — mit vennénk/építenénk a támogatásból
7. **Várt eredmény** — mit hozna a digitalizáció (hatékonyság, ügyfélmegtartás, növekedés)

## Hint

Kérd a Cowork-öt egy 1-oldalas, professzionális Word-dokumentumra (.docx) a pályázati tanácsadónak — fejléccel, 5-7 szekcióval, kiemelt számokkal. Ha az első verzió túl száraz, mondd: 'Tedd élvezetesebbé, de tartsd üzletinek.'


## Elvárt kimenet

`palyazat_onepager.docx` — professzionális kinézetű:
- Céges fejléc (név, cím, elérhetőség)
- Tiszta szekciók, jól olvasható
- Adatok kiemelve (félkövér számok)
- Maximum 1 A4 oldal

## Extra kihívás

Ha elkészült:
> "Készíts egy 2. verziót is románul (az egész dokumentum legyen románul), mert a pályázatot románul kell beadni."

## Hogyan csináld

1. A CLAUDE.md kontextus + a korábbi összefoglaló (ceg_attekintes.md) = minden adat megvan
2. Egy prompttal kérd a Word fájlt
3. Nyisd meg, nézd meg — ha valami nem tetszik, iterálj ("A számok szekciót tedd táblázatba", "A fejléc legyen kék")
4. A Cowork létrehozza a .docx fájlt közvetlenül a mappádba

## Tanulás

- **AI mint dokumentum-generátor** — nem csak szöveget ír, hanem formáz is (fejléc, táblázat, stílusok)
- **Forrásból generálás** — nem neked kell kitalálni mit írj, az AI összefoglalja a meglévő infóból
- **Iteráció** — az első verzió ritkán tökéletes, de 2-3 kör finomítás után profi output
- **Többnyelvű output** — ugyanaz az adat, más nyelven = 30 másodperc
- A "gondolkodástól a kész, nyomtatható outputig" → **10 perc**
