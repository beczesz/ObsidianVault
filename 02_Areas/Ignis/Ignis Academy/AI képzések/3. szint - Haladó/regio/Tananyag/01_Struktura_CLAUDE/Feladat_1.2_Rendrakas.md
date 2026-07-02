---
title: "Feladat 1.2: Rendrakás a Napsugárban (CLAUDE.md, jelszó-figyelés, Kuka)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F1 második feladat: az AI a standard szerint rendet rak a káoszban lévő Napsugár projektben. Biztonsági másolatot készít, a fájlokat a helyes 10-mappás struktúrába rendezi, a duplikátumokat és az oda nem illő fájlokat (recept, nyaralás) egy Kuka mappába teszi, a jelszavak.txt-re KÜLÖN figyelmeztet (nem törli némán), és a projekt gyökerébe megírja a CLAUDE.md-t. Confirmation-gate: a résztvevő átnézi, mielőtt véglegesít."
id: 6b3d8f02-4a71-4e52-9c26-7d1f0b3e2c84
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, feladat, rendrakas, claude-md, biztonsag]
---
# Feladat 1.2: Rendrakás a Napsugárban

> **Idő:** 12 perc · **Mód:** oktatói demó + saját gépen · **Eredmény:** rendezett Napsugár + Kuka + CLAUDE.md + jelszó-figyelmeztetés

---

## Szituáció

Az audit (1.1) kimondta: a Napsugár káosz. Most jön a neheze, de az igazi WOW: nem kézzel pakolgatunk fél napig, hanem az AI a standard szerint rendet rak, mi pedig ellenőrzünk.

---

## Cél

Az AI a `Internal_Standard.docx` és a két rendezett projekt mintája alapján:
- Készít egy **biztonsági másolatot** a jelenlegi állapotról (mielőtt bármit mozgat).
- A szétdobált fájlokat a **helyes 10-mappás struktúrába** rendezi, a szabályos elnevezéssel.
- Egy **Kuka** mappába teszi a duplikátumokat (`Copy of...`, régi `NE HASZNALD`) és az oda nem illő fájlokat (`paprikas_krumpli_recept.txt`, `csaladi nyaralas 2024.txt`, `bevasarlolista.txt`, `~$deviz.tmp`).
- A `jelszavak.txt`-re **külön figyelmeztet**: nem törli és nem osztja meg, hanem jelzi, hogy ez érzékeny adat, és biztonságos helyre (jelszókezelőbe) valós.
- Megírja a projekt gyökerébe a **CLAUDE.md**-t (a projekt lényege + a standard).

---

## Hogyan csináld

### 1. lépés: A prompt

```
A THR_Napsugar_Tejuzem projekt káosz. Rakj benne rendet a Internal_Standard.docx
és a két rendezett projekt (PAN, KER) mintája szerint. Lépések:

1. Előbb készíts egy biztonsági másolatot a jelenlegi állapotról.
2. Hozd létre a standard 10-mappás struktúráját, és tedd a fájlokat a helyükre,
   a szabályos elnevezéssel (sorszám_dokumentumnév_Iniciálé_dátum).
3. Készíts egy Kuka mappát, és oda tedd a duplikátumokat és az oda nem illő
   fájlokat (recept, nyaralás, bevásárlólista, temp).
4. FONTOS: ha érzékeny adatot (pl. jelszavakat) találsz, NE töröld és NE tedd
   Kukába csak úgy. Jelezd külön, hogy ez biztonsági kockázat, és mondd meg,
   mit kellene vele tenni.
5. A projekt gyökerébe írj egy CLAUDE.md-t: a projekt lényege + a projekt
   kulcsszámai (beneficiar, fázis, beruházás összege, ha kiderül a fájlokból) +
   a standard szabályok, hogy minden új munkamenetben ezt olvasva a standard
   szerint dolgozz és azonnal tudd a projekt alapadatait.

Mielőtt véglegesíted, mutasd meg, mit hova tennél, és mit jelölsz szemétnek.
```

### 2. lépés: Nézd át, mielőtt véglegesíted
Az AI megmutatja a tervet. **Ellenőrizd:**
- A `jelszavak.txt`-re **figyelmeztet-e** (nem némán törli)?
- A `paprikas_krumpli_recept.txt` és társai a **Kukába** kerülnek-e?
- A legit fájlok (deviz, ajánlat-scan, anexa, centralizator, egyeztetés) a **helyes mappába**?
- Ha valamit rossz helyre tenne, szólj: *„A `contract finantare.txt` a 06_Contract_de_finantare-ba menjen."*

### 3. lépés: Véglegesítés
Ha jónak látod, engedd végrehajtani. A Napsugár mostantól a standard szerint áll, van Kuka, van CLAUDE.md, és tudod, hol a jelszó-probléma.

---

## Önellenőrzés

- [ ] Létrejött a **biztonsági másolat**.
- [ ] A Napsugár a **standard 10-mappás** struktúráját kapta, szabályos nevekkel.
- [ ] Van **Kuka** mappa a szeméttel (recept, nyaralás, duplikátumok, temp).
- [ ] A `jelszavak.txt`-re **külön figyelmeztetés** jött (nem tűnt el némán).
- [ ] Megszületett a projekt **CLAUDE.md**-je.

---

## A WOW-pillanat

Amit egy új munkatárs fél napig pakolna, az AI percek alatt megcsinálja, a **saját standardetek szerint**, a két rendezett projekt mintájára. És a `jelszavak.txt`-nél megáll: nem csak rendez, hanem **véd** is. Ez a különbség egy buta fájlrendező szkript és egy értő asszisztens között.

---

## Tanulás

**A rend beíródik a memóriába.** A CLAUDE.md nem csak egy dokumentum: mostantól minden session elején ezt olvasva az AI tudja, hogy néz ki a rend nálatok, és tartja is. **Bízz benne, de ellenőrizz:** a destruktív lépéseknél (Kuka, jelszó) az AI megmutatja a tervet, te döntesz. Az AI a kéz, te a fej.

---

## Mi következik (1.3)

A rend megvan, a CLAUDE.md megszületett. Teszteljük: új munkamenetben megkérdezzük, miről szól ez a projekt, és megnézzük, hogy fejből válaszol-e.

---

## Időkeret
- Prompt + terv-bemutatás: 4 perc
- Átnézés + finomítás: 4 perc
- Véglegesítés + eredmény: 4 perc
- **Össze: 12 perc**

**Verzió:** 2.0 (rendrakás ív)
