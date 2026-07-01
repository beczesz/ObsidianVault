---
title: "Feladat 3.3: Token-mérleg: mit ér meg, hol a határ (STÁCIÓ)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F3 stáció: a résztvevők az AI-val megbecsültetik, mennyibe (időben, feldolgozásban) kerül egy nagy szkennelt PDF feldolgozása, és mérlegelik, mikor éri meg OCR-rel dolgozni és mikor jobb a vektoros / Excel-export beszerzése. A cél a józan döntés, nem a mindenáron automatizálás."
id: 34c15b7c-7253-4d3a-9a8e-8f0c7b2a6f4d
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f3, feladat, token]
---
# Feladat 3.3: Token-mérleg: mit ér meg, hol a határ (STÁCIÓ)

> **Típus:** ⏸ STÁCIÓ · **Idő:** ~8 perc

---

## Szituáció

Az OCR működik egy pár oldalas ajánlaton. De a valóságban néha egy **353 oldalas, 300 MB-os** szkennelt technikai dokumentáció érkezik. Ott a kérdés már nem az, hogy „megtudja-e csinálni", hanem hogy **megéri-e**. A kép-oldalak feldolgozása drága (sok token, sok idő), és minél nagyobb, annál nő a hibalehetőség is.

A profi döntés: melyik utat választom?
- **OCR-rel feldolgozom** (ha nincs jobb, és a kontroll-összeg tartható),
- vagy **beszerzem a vektoros / Excel-exportot** a forrástól (a tervező szinte mindig tudja Excelben adni), és azzal dolgozom, ami gyorsabb és pontosabb.

---

## A stáció prompt

```
Van egy szkennelt, kép-only technikai dokumentációnk, kb. 350 oldal.
Csak a benne lévő tételes költségvetést (deviz) kell kinyernünk, ami kb.
15 oldal az egészből.

Segíts dönteni: érdemes-e a teljes 350 oldalt OCR-rel feldolgoztatni,
vagy okosabb csak a releváns 15 oldalt kivágni és azt kiolvasni, vagy
inkább a tervezőtől bekérni a vektoros / Excel változatot?
Sorold fel az opciók előnyét/hátrányát, és mondd meg, te melyiket
javasolnád és miért.
```

---

## Elvárt eredmény

Az AI három józan opciót ad: (1) csak a releváns oldalak kivágása és OCR-je (a legtöbbször ez a nyerő), (2) a vektoros export bekérése (a legpontosabb, ha megkapod), (3) teljes OCR (csak ha nincs más). A tanulság: **nem a mennyiség a kérdés, hanem a stratégia.**

---

## Miért ez a stáció

A ti világotokban a szkennelt PDF a legnagyobb fájdalom, és pont ezért itt a legnagyobb a csalódás kockázata. Ez a stáció a **reális elvárás**: az AI nem varázspálca a 300 MB-os szörnyhöz, de nagyon jó eszköz, ha okosan használod (releváns oldalak, kontroll-összeg, vektoros alternatíva). A cél a hatékony döntés, nem a mindenáron való automatizálás.

---

## Tanulás

Az AI-val dolgozni nem azt jelenti, hogy mindent rá kell tolni. A legnagyobb hatékonyságot a **jó triázs + jó stratégia** adja: a releváns rész kivágása, a vektoros út preferálása, a kontroll fegyelme. Ez a különbség a frusztrált és a hatékony AI-használó között.

## Otthoni elmélyítés
- `Feladat_3.6_Bonusz_Vektoros_export.md`, hogyan kérd be a vektoros/Excel exportot

**Verzió:** 1.0 (Regio adaptáció)
