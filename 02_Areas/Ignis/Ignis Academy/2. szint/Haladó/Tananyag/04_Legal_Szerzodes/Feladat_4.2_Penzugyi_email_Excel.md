---
title: "Feladat 4.2 (Stáció 4.B) — Felkérő email Mihaelának (románul)"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Felkérő email sablon Mihaela Ionescu könyvelőhöz románul, amelyet a Cowork 30-60 másodperc alatt ír meg Márton nevében az AFM Mobilitate Verde 2026 pályázathoz szükséges 2024-2025 évi pénzügyi adatok (bilanț, cont de profit și pierdere, EBITDA, alkalmazotti létszám) bekéréséhez, 3 na"
description_source: auto
description_hash: 785892292613d2f3
id: 224332fa-8857-4b69-bf6c-c9f3e3b8c6fb
index_schema_version: 1
bdos_index: true
---
# Feladat 4.2 (Stáció 4.B) — Felkérő email Mihaelának (románul)

> **Típus:** ⏸ STÁCIÓ — saját laptopon, copy-paste prompt
> **Idő:** ~5 perc · **Mód:** egyénileg

---

## Szituáció

Az F3 gap-analízisében a Cowork **kibukta** a második piros pontot:

> **A pályázat előírja:** „Solicitantul demonstrează **stabilitatea financiară pe ultimii 2 ani fiscali încheiați**" — vagyis a **2024 és 2025 lezárt mérleg** szükséges (bilanț + cont de profit și pierdere + EBITDA + alkalmazotti adatok).
>
> **A TransOffice-on:** ezek az adatok a **külsős könyvelőnél** (Mihaela Ionescu) vannak, nem nálunk. A `Kovacs_Ilona/eves_jelentes_2022.xlsx` a legfrissebb amit nálunk találunk — 4 évvel elavult.

**A megoldás:** **emailt írunk Mihaelának románul** és kérjük a 2024+2025 pénzügyi adatokat.

**A te dolgod most:** írd meg ezt a felkérő emailt Márton nevében a saját Cowork-eden.

---

## A stáció prompt

Másold ki és illeszd be a saját Cowork-jébe:

```
Írj egy emailt Mihaela Ionescu-nak (mihaela.ionescu@contabilpro.ro,
a TransOffice külsős könyvelője) Márton nevében. A helyzet:

- Pályázunk az AFM Mobilitate Verde 2026 programra (elektromos járműflotta)
- Beadási határidő: 2026-08-31, ora 16:00 — ~1 hét van vissza
- A pályázat előírja: az utolsó 2 lezárt pénzügyi év mérlege és pénzügyi
  helyzete (bilanț + cont de profit și pierdere + EBITDA + alkalmazotti
  létszám) — tehát 2024 és 2025
- Mihaela a könyvelő, ezek az adatok nála vannak

Kérjük meg Mihaelát hogy:
- Küldje át a 2024 és 2025 bilanț + cont de profit și pierdere kivonatot
- Mellékeljen 1 sor EBITDA-t és az alkalmazotti létszámot (FTE)
- Határidő: 3 napon belül (a pályázati beadáshoz időben kelljen
  fel tudjuk dolgozni)

Hangnem: románul, professzionális de közvetlen — Mihaela 45 éves,
részmunkaidős, precíz. Max 8 mondat.
```

---

## Elvárt eredmény

A Cowork 30-60 másodperc alatt:
- Megszólítja Mihaelát **románul** (pl. „Bună ziua, Mihaela")
- **Magyarázza el a pályázat helyzetét** (AFM Mobilitate Verde 2026, határidő)
- **Konkrétan** kéri a 4 dolgot: bilanț + cont P&L + EBITDA + alkalmazotti adatok
- **2024 + 2025** évekre (utolsó 2 lezárt)
- Határidő-megjelölés (3 nap)
- **Románul**, professzionális hangnem
- Maximum 8 mondat

---

## Az email folytatása (a Cowork DEMO-ban kapja meg)

Miután az email „elment" Mihaelának, az oktató a kivetítőn **megmutatja a választ** (a `emails/mihaela_konyvelo_valasz/email.md`-ből):

> *„Épp Görögbe indultam a családdal, de gyorsan összedobtam a számokat. Csatolom az Excelt, benne van minden: bilanț, eredménykimutatás, EBITDA, létszám..."*

**+ Mellékelve: `bilant_TransOffice_2024_2025.xlsx`** — a Cowork élesben kiszámolja az **EBITDA margint** és bemutatja a 2024 vs 2025 trendet.

---

## A WOW-pillanat — páros megbeszélés (1 perc)

Ha párban vagy:
- **Mennyire formális** a sajátod vs. a párod — mindketten „professzionális de közvetlen"?
- **Hogyan szólítja meg** Mihaelát? Vornévvel vagy keresztnévvel?
- **Mennyire konkrétan** kéri a 4 adatot — listázza vagy szövegben?

---

## Tipp

Ha az email **túl formális** (mintha hivatalos megkeresés lenne), mondd: *„Tedd közvetlenebbé — kollegális, Mihaela már régóta ismeri Mártont."*

Ha **a román nem ülne tökéletesen**, kérdezz vissza: *„Nézd át a román nyelvtant — magánvállalkozói-szakmai stílus."*

Ha **a 3 napos határidő túl szoros**, mondd: *„Tedd 1 hetessé, ne tűnjön sürgetésnek."*

---

## Tanulás

- **Az AI mint kétnyelvű kommunikátor**: a meeting magyarul zajlott, a Béla bácsi email magyarul készült, **de Mihaelának románul írunk** — egyetlen Cowork-folyamatban, kontextus-megszakítás nélkül.
- **A piros pont → akció lánc**: az F3-ban kibukott "stabilitatea financiară pe ultimii 2 ani" → konkrét, határidős email-kérés.
- **A nyelvi-regiszteri váltás** (Béla bácsi családi-magyar → Mihaela professzionális-román) **az AI superpower** — kézzel ezt csak kétnyelvű ember tudná, és 20-30 perc.

---

## Otthoni elmélyítés

A saját Excel-jeiddel — bónusz feladatok:
- `Feladat_4.6_Bonusz_Excel_dashboard.md` — banki kivonatból vezetői dashboard
- `Feladat_4.7_Bonusz_Prezi_celkozonseg.md` — prezentáció 3 célközönségnek

---

**Verzió:** 2.1 (Stáció modell — felkérő email románul)
