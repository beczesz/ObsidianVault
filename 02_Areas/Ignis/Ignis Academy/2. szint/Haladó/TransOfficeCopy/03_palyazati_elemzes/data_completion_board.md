---
title: "Data Completion Board — AFM Mobilitate Verde 2025"
date: 2026-05-12
author: Becze Szabolcs
status: active
description: "TransOffice Trade SRL pályázatának adatkezelő táblázata a Mobilitate Verde 2025 pályázatra: 23 melléklet és 2 eligibility-kritérium nyomon követése valós időben, 3 napos beadási időhorizonttal. Projekt-menedzsereknek és operációs csapatnak."
description_source: auto
description_hash: 91edf04028d9e84c
id: e5eca56c-da44-4490-8d69-2023ea572b77
index_schema_version: 1
bdos_index: true
---
# Data Completion Board — AFM Mobilitate Verde 2025
## TransOffice Trade SRL — Élő munkaeszköz

> **Készítette:** Cowork + Operations Manager
> **Verzió:** v1.0 (2025-02-25 este) — frissítendő naponta
> **Cél:** Egyetlen koherens státusz-tabella a 23 melléklet + 2 nyitott eligibility-kritérium kezelésére

---

## 🎯 Vezetői dashboard

| Metrika | Érték | Trend |
|---|---:|:---:|
| Mellékletek **zöld** | 8 / 23 (35%) | ↑ |
| Mellékletek **sárga** | 11 / 23 (48%) | → |
| Mellékletek **piros** | 4 / 23 (17%) | ↓ (volt 6) |
| Eligibility kritérium nyitott | 1 / 12 (CR-05/06 pénzügy) | → |
| Becsült pontszám | 65-73 / 100 | → |
| Pályázat-beadásra napok | 3 | ↓ |
| Kritikus út egészsége | 🟡 átlagos (Mihaela-válaszra vár) | → |

---

## 23-tételes Data Board

| ID | Tétel | Státusz | Felelős | Határidő | Forrás / Hol van? | Kockázat | Megjegyzés |
|---|---|:---:|---|---|---|---|---|
| M-01 | Cert. constatator ONRC | 🔴 | Enikő | sze. 12:00 | ONRC online portál | 🟢 alacsony | 20 RON, 2 óra |
| M-02 | Statutul societății | 🟡 | Enikő | sze. 14:00 | 2003-as akta, irodában | 🟢 alacsony | Scannelni kell |
| M-03 | Lista UBO közjegyzői | 🔴 | Márton | cs. 09:00 | BNP Munteanu | 🟡 közepes | 2 nap átfutás, **csü reggelre szoros** |
| M-04 | Cert. fiscal ANAF | 🔴 | Enikő | sze. 12:00 | ANAF SPV | 🟢 alacsony | 5 perc |
| M-05 | Cert. fiscal Primăria | 🔴 | Márton | cs. 16:00 | Primăria Odorheiu | 🟡 közepes | Személyes kiszállás |
| M-06 | Bilanț 2023 | 🔴 | Mihaela | sze. 18:00 | Mihaela birtokában | 🔴 **MAGAS** | Az egész pályázat ettől függ |
| M-07 | Bilanț 2024 | 🔴 | Mihaela | sze. 18:00 | Mihaela birtokában | 🔴 **MAGAS** | Lehet hogy negatív EBITDA — kezelés a Plan de afacerin (Plan B) |
| M-08 | Anexa 7 — Macheta financiară | 🟡 | Op.Mgr | cs. 22:00 | Cowork generálja M-06+M-07 alapján | 🟡 közepes | F5 része |
| M-09 | Declarație minimis (Anexa 11) | 🟡 | Mihaela + Márton | sze. 18:00 | Sablon + Mihaela megerősítés | 🟢 alacsony | Várhatóan üres lista (nincs subv. történet) |
| M-10 | Plan de afaceri (Anexa 6) | 🟡 | Op.Mgr | cs. 22:00 | Cowork generálja F5.1-ben | 🟡 közepes | 25-40 oldal románul |
| M-11 | Plan de înnoire a parcului (Anexa 13) | 🔴 | Bíró Attila + Márton | sze. 17:00 | szétszórt, fejben | 🟡 közepes | 30 perces leltár Attilával |
| M-12 | 3× ofertă furnizor (e-vehicul) | 🟡 | Márton | cs. 18:00 | Email-kérés 3 forgalmazóhoz | 🟡 közepes | Dacia Spring, BYD, Renault Kangoo E-Tech |
| M-13 | Studiul de piață | 🟡 | Op.Mgr | cs. 22:00 | Cowork generálja F5.1 cap. 3 | 🟢 alacsony | Online + AFM-mintaadatokból |
| M-14 | Contract de închiriere | 🟢 | — | kész | `szerzodes_chirie_TransOffice_2018.docx` | 🟢 alacsony | Másolva |
| M-15 | Acord proprietar pt. AC | 🔴 | Béla bácsi | cs. 12:00 | Email + közjegyző | 🟡 közepes | Béla bácsi a 02-26-i emailben felajánlotta |
| M-16 | Declarație notarială (5 év stab.) | 🟡 | Béla bácsi + közjegyző | cs. 14:00 | Közös időpont Munteanu BNP | 🟡 közepes | Béla bácsi vállalta |
| M-17 | Extras CF | 🔴 | Béla bácsi | sze. 16:00 | ANAF online | 🟢 alacsony | Béla bácsi szerzi be |
| M-18 | Autorizație de mediu | 🟢 | — | kész | Cégbejegyzés | 🟢 alacsony | Irodai tev. mentes |
| M-19 | Aviz ISC / racord electric AC | 🟡 | Márton + E-Distribution | (POST-pályázat) | E-Distribution Romania | 🟡 közepes | 30 napos átfutás — promiss intent declaration most |
| M-20 | Polițe CASCO/RCA | 🟢 | Op.Mgr | sze. 14:00 | Aktuális polícák | 🟢 alacsony | Bemásolni |
| M-21 | Declarație eligibilitate (Anexa 9) | 🟢 | Márton | pé. 09:00 | Sablon | 🟢 alacsony | Aláírás reggel |
| M-22 | Declarație cofinanțare (Anexa 10) | 🟢 | Márton + bank | pé. 12:00 | Sablon + banki igazolás | 🟢 alacsony | Bank levél péntekre |
| M-23 | Declarație DNSH (Anexa 12) | 🟢 | Márton | pé. 09:00 | Sablon | 🟢 alacsony | Aláírás reggel |

---

## Eligibility nyitott pontok

| ID | Kritérium | Felelős | Határidő | Státusz | Akció |
|---|---|---|---|:---:|---|
| CR-05 | EBITDA + D/E ratio + ANAF tartozás | Mihaela | sze. 18:00 | 🔴 → 🟡 | Mihaela emailes válasz; ha 2024 negatív, a 2023-as biztosítja a megfelelőséget |
| CR-06 | De minimis < 200k EUR / 3 év | Mihaela | sze. 18:00 | 🟡 | Várható: NIL — egyszerű megerősítés |
| CR-09 | Telephely stabilitás | Béla bácsi (megtörtént) | ✅ kész | 🟢 | A 02-26-i emaillel és csütörtöki közjegyzői declarațióval lezárt |

---

## Gantt-ütemterv (3 nap)

```
Szerda (2025-02-26)
├─ 08:00  Email Enikőnek + Mihaelának (kiment kedd este)
├─ 10:00  Enikő: M-01 + M-04 + M-20 (3 db kész)
├─ 12:00  M-01, M-04, M-20 zöldre
├─ 14:00  Op.Mgr: bérleti szerződés deep-check (F4.1) → Béla bácsi-email
├─ 16:00  Béla bácsi visszaírt — M-17 elindul, M-15+M-16 időpont egyeztetés
├─ 17:00  Bíró Attila + Márton: M-11 (jármű-leltár)
├─ 18:00  Mihaela válaszol (remény) — M-06, M-07, CR-05, CR-06 lezárás
├─ 22:00  CEO 5-slide PPT Mártonnak (F4.3)

Csütörtök (2025-02-27)
├─ 09:00  M-03 + M-21 + M-23 — Márton aláírások
├─ 12:00  M-15 — Béla bácsi acord proprietar (közjegyzőnél)
├─ 14:00  M-16 — declarație notarială (Munteanu BNP)
├─ 16:00  M-05 — Primăria Odorheiu (Márton személyesen)
├─ 18:00  M-12 — 3× ofertă furnizor (e-vehiculák) megérkezik
├─ 22:00  F5.1 Plan de afaceri kész (25-40 oldal)

Péntek (2025-02-28)
├─ 09:00  M-22 — banki cofinanțare-igazolás
├─ 12:00  F5.2 — 23-tételes csomag PDF-konszolidáció
├─ 16:00  F5.3 — MySMIS form kitöltés
├─ 23:00  ✅ BEADÁS (1 óra ráhagyás a szerver-akadásra)
```

---

## TOP 3 KOCKÁZAT

1. **Mihaela csúszik 24+ órát** → CR-05, M-06, M-07 nem zárható le → **stoppolunk pénteken**.
   - Mitigáció: Márton telefon szerdán 14h, agresszív sürgetés.
2. **EBITDA 2024 ténylegesen negatív, ÉS 2023 sem volt pozitív** → CR-05 nem teljesül.
   - Mitigáció: csak akkor adunk be, ha az egyik pozitív; egyébként **transparensen visszalépünk**.
3. **MySMIS portál péntek este lefagy** (forgalom-csúcs az utolsó napon).
   - Mitigáció: csütörtök este teljes csomag PDF-export "demoláltató" verzióban, korai péntek reggel próba-beadás (technical test).

---

## Élő frissítések — naplózás

| Időbélyeg | Esemény | Hatás |
|---|---|---|
| 2025-02-24 11:00 | Meeting Mártonnal + Enikővel | F2 TODO-lista létrejött |
| 2025-02-24 21:00 | Email Mihaelának kiküldve | M-06+M-07 várólista |
| 2025-02-25 09:00 | F3.1 eligibility-check kész | 10/12 ✅, 2 ⚠️ |
| 2025-02-25 14:00 | F3.2 gap-analízis kész | 17/23 zöld/sárga, 6 piros |
| 2025-02-25 16:00 | F3.3 Data Completion Board v1.0 generálva | élő munkaeszköz |
| **VÁRHATÓ:** 2025-02-26 09:00 | Béla bácsi-email feldolgozás (F4.1) | M-14 → zöld, M-15+M-16 elindul |
| **VÁRHATÓ:** 2025-02-26 18:00 | Mihaela-válasz feldolgozás (F4.2) | M-06+M-07 zöld, CR-05 + CR-06 zöld |
| **VÁRHATÓ:** 2025-02-26 22:00 | CEO PPT Mártonnak (F4.3) | Márton döntés: pályázunk ✅ |
| **VÁRHATÓ:** 2025-02-28 23:00 | BEADÁS | Pályázat státusz: SUBMITTED |
