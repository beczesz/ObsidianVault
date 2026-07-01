---
title: "Feladat 4.1: Tételenkénti kereszt-összevetés (DEMO)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F4 oktatói demó: az AI egyszerre nézi a deviz general Cap. 4-et (ajánlatkérés) és a kivitelező OCR-ből kinyert ajánlatát, tételesen összeveti a mennyiségeket és összegeket, és megtalálja a 60 000 lej eltérést (4.6 Active necorporale hiányzik az ajánlatból). Végösszeg-kontrollal validál."
id: 8916aec1-2708-4e6b-9f3d-3e5a1b7f6c4d
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f4, feladat, demo]
---
# Feladat 4.1: Tételenkénti kereszt-összevetés (DEMO)

> **Típus:** 🎤 OKTATÓI DEMO · **Idő:** ~12 perc

---

## Szituáció

Két dokumentum van előtted:
- **Az ajánlatkérés:** a deviz general **Cap. 4** (investiția de bază), a ti kiírásotok, tételesen (construcții, montaj, utilaje, dotări, active necorporale).
- **Az ajánlat:** a kivitelező tételsora, amit az F3-ban OCR-rel gépi-olvashatóvá tettünk.

A kérdés: fedi-e az ajánlat a kiírást, tételről tételre, mennyiségre és összegre? Ez a kollégáknál a leghosszabb kézi meló.

---

## A demó menete

### 1. lépés: Az AI összeveti a két forrást

```
Két forrásom van a Napsugár projektben:
1. Az ajánlatkérés: a deviz general Cap. 4 (investiția de bază) tételei.
2. Az ajánlat: a kivitelező OCR-ből kinyert tételsora (oferta_OCR.md).

Vesd össze őket tételesen (4.1 Construcții, 4.2 Montaj, 4.3 Utilaje,
4.5 Dotări, 4.6 Active necorporale). Minden tételhez: mennyi a devizben,
mennyi az ajánlatban, mennyi az eltérés. A végén add meg a Cap. 4 összeget
mindkét oldalon, és az eltérést. Ahol eltérés van, emeld ki, és írd le,
mi lehet az oka. Minden érték fără TVA, lei.
```

### 2. lépés: Az eredmény (a megtalált eltérés)

Az AI kiadja a táblát (vö. `Pelda_output/osszevetes_EREDMENY.md`):

| Deviz-tétel | Ajánlatkérés | Ajánlat | Eltérés |
|---|---:|---:|---:|
| 4.1 Construcții și instalații | 3 190 000 | 3 190 000 | 0 |
| 4.2 Montaj utilaje | 95 000 | 95 000 | 0 |
| 4.3 Utilaje cu montaj | 1 850 000 | 1 850 000 | 0 |
| 4.5 Dotări | 240 000 | 240 000 | 0 |
| **4.6 Active necorporale** | **60 000** | **0** | **−60 000** |
| **Cap. 4 összesen** | **5 435 000** | **5 375 000** | **−60 000** |

A négy nagy tétel fillérre egyezik, a **4.6 Active necorporale (szoftver, 60 000 lej)** viszont hiányzik az ajánlatból. Ez nem a kivitelező munkája, hanem külön beszerzés (DAF Furnizare), vagy tisztázni kell a beneficiárral.

### 3. lépés: A WOW

Ez az a tétel, amit egy fáradt szem, tíz oldal egyeztetés után **könnyen átugrik**. Az AI, ami egyszerre tartja a két dokumentumot, azonnal kiszúrja. És a **végösszeg-kontroll** (5 435 000 vs. 5 375 000 = pont 60 000) matematikailag is igazolja: nincs más rejtett eltérés.

---

## Amit a résztvevők megfigyelnek
- Hogyan tart az AI **két dokumentumot egyszerre**, és hogyan párosít tételeket.
- Hogy nem csak „stimmel"-t mond, hanem a **hiányt** is megtalálja.
- Hogy a végösszeg-kontroll megerősíti: nincs több eltérés.

---

## Tanulás

A kereszt-dokumentum ellenőrzés a kézi munka egyik legfárasztóbb, leghibázósabb fajtája: két lista, sok sor, könnyű átsiklani. Az AI itt a legerősebb, mert nem fárad el, és a végösszeg-kontrollal matematikailag lezárja a kérdést. De a döntés a tiéd: a 4.6-ot tisztázni kell, azt ember dönti el, hogyan.

---

## Mi következik (F4 stáció)
A résztvevők most az eltérésből cselekvést csinálnak: egy eltérés-riportot vagy egy tisztázó kérdést a beneficiárnak.

---

## Időkeret
- Összevetés demó: 5 perc
- Az eltérés + kontroll: 4 perc
- Megbeszélés: 3 perc
- **Össze: 12 perc**

**Verzió:** 1.0 (Regio adaptáció)
