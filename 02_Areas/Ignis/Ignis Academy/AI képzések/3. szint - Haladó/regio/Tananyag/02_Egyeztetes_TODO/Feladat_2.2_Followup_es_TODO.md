---
title: "Feladat 2.2: Follow-up dokumentum a feladatlistából (STÁCIÓ)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F2 stáció: a résztvevők a kinyert Napsugár-feladatlista alapján egy státusz-jegyzetet készíttetnek a beneficiárnak, KÖTELEZŐEN a hivatalos RC_Template_URES.docx üres templatből (RegioConsult fejléc + lábléc + Verdana 9 Black Text 1 Lighter 25%). Nem nulláról, hanem a brandelt templatet kitöltve, a standard elnevezéssel a 10_Monitorizare mappába mentve. Az első saját, brand-konform kimenet."
id: c29a4468-0137-4b18-9f8c-6e7a5f9d4d2a
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f2, feladat, station]
---
# Feladat 2.2: Follow-up dokumentum a feladatlistából (STÁCIÓ)

> **Típus:** ⏸ STÁCIÓ (saját gépen) · **Idő:** ~7 perc

---

## Szituáció

Megvan a mentett feladatlista. A napi munkában ebből kimegy egy dokumentum a beneficiárnak. De a RegioConsult-nál **minden kimenő dokumentumnak kötelezően a hivatalos üres templatből kell indulnia:** `RC_Template_URES.docx`. Ez tartalmazza a RegioConsult **fejlécet** (logó), a **láblécet** (www.regioconsult.ro + a három iroda) és az alap **Verdana 9 (Black Text 1 Lighter 25%)** formátumot. Nem írunk dokumentumot nulláról: a templatet töltjük ki.

---

## A stáció prompt

**A) Státusz-jegyzet a beneficiárnak (a template-ből, KÖTELEZŐ):**
```
Nyisd meg a RC_Template_URES.docx üres templatet, és ABBA írd a dokumentumot.
NE készíts újat nulláról: a templatben már benne van a kötelező RegioConsult
fejléc, lábléc és a Verdana 9 (Black Text 1 Lighter 25%) formátum.

A feladatok_Napsugar.md alapján írj egy rövid, professzionális státusz-jegyzetet
a beneficiárnak (Napsugár Tejüzem ügyvezetése). Térj ki a 4.6 Active necorporale
(szoftver) tétel tisztázására, ami a devizben szerepel, de az ajánlatból hiányzik.
Hangnem: kollegális, világos. A végén az aláírás-blokk helye.

Mentsd a projekt 10_Monitorizare mappájába a standard elnevezéssel
(sorszám_KÓD_dokumentumnév_Iniciálé_dátum).
```

**B) Feladat-kártya a felelősnek (belső munkajegyzet):**
```
A feladatok_Napsugar.md-ből emeld ki a Kingára osztott feladatokat, és
készíts egy tömör, cselekvő feladat-kártyát: mit, mire, milyen forrásból,
milyen határidővel. Ez belső munkajegyzet, ide a template nem kötelező.
```

---

## Elvárt eredmény
Egy kész, **RegioConsult-branddel** (fejléc + lábléc), Verdana 9 (Black Text 1 Lighter 25%) formátumú dokumentum, ami a **template-ből** készült, a standard elnevezéssel a helyén (`10_Monitorizare`). NEM egy nulláról gyártott, brand nélküli fájl. Fontos tapasztalat: az AI a **mentett projekt-kontextusból** dolgozik, és a **kötelező templatet** használja.

---

## Miért ez a stáció
A feladatlista önmagában belső eszköz. Az érték akkor jön, amikor ebből **azonnal lesz kimenő kommunikáció**, a ti hivatalos arculatotokban. A **kötelező template** a lényeg: egy ügyfélnek menő dokumentum sosem lehet brand nélküli, nulláról gyártott fájl. A RegioConsult fejléc és lábléc, a Verdana 9 formátum minden kimenő dokumentumon egységes. Az AI a template-et tölti ki, te vezeted, és a végeredmény azonnal kiküldhető, arculat-helyesen.

---

## Tipp
Ha a hangnem nem stimmel, ne írd át kézzel: mondd meg az AI-nak (*„egy fokkal formálisabb", „rövidebben"*), és újragenerálja. A finomítás párbeszéd, nem újraírás.

## Otthoni elmélyítés
- `Feladat_2.5_Bonusz_Email_szal_TODO.md`, email-szálból teendők
- `Feladat_2.3_Bonusz_Sajat_egyeztetes.md`, a saját megbeszélésed feldolgozása

**Verzió:** 2.0 (kötelező RC template)
