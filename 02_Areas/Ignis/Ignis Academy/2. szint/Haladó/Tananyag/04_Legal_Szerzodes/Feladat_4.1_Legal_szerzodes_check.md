---
title: "Feladat 4.1 (Stáció 4.A) — Felkérő email Béla bácsinak"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Olyan email szövegét kell elkészíteni, amelyben Márton Béla bácsitól kéri a bérleti szerződés 2031-ig történő meghosszabbítását és a töltőpont telepítésére vonatkozó írásos engedélyt egy EU-s pályázat teljesítéséhez; a hangnem családias, tiszteletteljes és magyaros, maximum 8 mondatban."
description_source: auto
description_hash: 097da1a8cc50ccce
id: 95af243d-0e07-47c7-893a-87fe92cd5347
index_schema_version: 1
bdos_index: true
---
# Feladat 4.1 (Stáció 4.A) — Felkérő email Béla bácsinak

> **Típus:** ⏸ STÁCIÓ — saját laptopon, copy-paste prompt
> **Idő:** ~5 perc · **Mód:** egyénileg

---

## Szituáció

Az F3 gap-analízisében a Cowork **kibukta** az első piros pontot:

> **A pályázat előírja:** a telephely-bérlet **legalább 5 évig érvényes legyen a beadás dátumától számítva** (2026-08-31 → **2031-08-31**), **ÉS** a tulajdonosnak **írásban kell engedélyt adnia** a töltőpont telepítésére (acord scris pentru instalarea stației de reîncărcare).
>
> **A jelenlegi szerződés:** TransOffice 2018-2028 — vagyis **2026-ban beadva csak ~2 év marad**. Plusz töltőpont-engedély: **nincs**.

**A megoldás:** **Béla bácsival írásban** kérjük az `act adițional`-t a szerződés meghosszabbítására + külön az `acord scris` a töltőpontra.

**A te dolgod most:** írd meg ezt a felkérő emailt Márton nevében a saját Cowork-eden.

---

## A stáció prompt

Másold ki és illeszd be a saját Cowork-jébe:

```
Írj egy emailt Béla bácsi (a telephely-tulajdonos, 70 éves családi ismerős)
számára Márton nevében. A helyzet:

- A jelenlegi bérleti szerződésünk 2028-ig megy
- Egy EU pályázathoz (AFM Mobilitate Verde 2026, elektromos járműflotta)
  a telephely-bérletnek 2026-08-31-től számítva legalább 5 évig kell
  érvényesnek lennie — tehát 2031-08-31-ig
- Plusz: a tulajdonosnak írásban (acord scris) kell engedélyt adnia a
  töltőállomás telepítésére

Két dolgot kérjünk tőle az emailben:
1. act adițional a szerződés meghosszabbítására (min. 2031-ig, ideálisan
   tovább)
2. acord scris a töltőpont telepítésére

Hangnem: tisztelettudó, közvetlen, magyaros — Béla bácsi régi ismerős, 70 éves.
Max 8 mondat. Magyarul írd.
```

---

## Elvárt eredmény

A Cowork 30-60 másodperc alatt:
- Megszólítja Béla bácsit (tiszteletteljes, közvetlen, magyaros)
- **Magyarázza el a pályázat helyzetét** (5 év + töltőpont)
- **Konkrétan** kéri a 2 dolgot (act adițional + acord scris)
- Marad **udvarias** és **családias** (Béla bácsi régi ismerős, nem ügyfél)
- Maximum 8 mondatban
- Magyarul

---

## Az email folytatása (a Cowork DEMO-ban kapja meg)

Miután az email „elment" Béla bácsinak, az oktató a kivetítőn **megmutatja a választ** (a `emails/bela_bacsi_valasz/email.md`-ből):

> *„Szia Márton, Nyugi, a Băieșenilor-t nem adom el, az családi... Ha kell a pályázathoz, meghosszabbítjuk a szerződést 2035-ig, nekem jó. Közjegyzői papírt is aláírok ha az kell..."*

→ **Mindkét piros pont megoldva.** A Data Completion Board frissül zöldre.

---

## A WOW-pillanat — páros megbeszélés (1 perc)

Ha párban vagy:
- **Mennyire melegen szólítja meg** Béla bácsit a sajátod vs. a párod?
- **Mennyire konkrét** a 2 kérés (act adițional + acord scris)?
- **Hogyan magyarázza a pályázati kontextust** — érti egy 70 éves olvasó?

---

## Tipp

Ha az email **túl üzleties / hűvös**, mondd: *„Tedd melegebbre, családiasabbra. Béla bácsi régi ismerős."*

Ha **túl hosszú vagy szakszó-ízű** (act adițional, acord proprietar túl jogászos), mondd: *„Egyszerűbben, mintha egy 70 éves rokonnak magyaráznád."*

---

## Tanulás

- **Az AI mint kétnyelvű kommunikátor**: a pályázati követelmények románul érkeznek (act adițional, acord scris), de az emailt magyaros családi hangnemben írja meg a Cowork.
- **A piros pont → akció lánc**: a Cowork F3-ban felfedezte → most konkrét kérés-emaillé alakítja, dátumokkal és specifikus jogi kifejezésekkel.

---

## Otthoni elmélyítés

A saját szerződéseiddel — bónusz feladatok:
- `Feladat_4.4_Bonusz_Sajat_szerzodes.md` — saját szerződés deep-check
- `Feladat_4.5_Bonusz_Email_hangnem.md` — ugyanaz az email 3 hangnemben

---

**Verzió:** 2.1 (Stáció modell — felkérő email)
