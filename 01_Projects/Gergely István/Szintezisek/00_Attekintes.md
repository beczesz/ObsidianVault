---
title: "Gergely István — cég 2025 adatainak áttekintése"
type: synthesis-overview
project: Gergely István
period: 2025
currency: RON (lei)
created: 2026-05-21
source_files:
  - 2025 PTOT xlsx.xlsx
  - 2025ZGYxlsx.xlsx
  - Adaos total 2025xlsx.xlsx
  - P2025 SZAMLAxlsx.xlsx
  - TOTAL GERDIT 2025xlsx.xlsx
tags: [synthesis, retail, finance, romania]
id: 78400be7-5d36-4208-bd0d-57caee044418
index_schema_version: 1
---

# Áttekintés — mit látunk az 5 fájlban

## Mi ez a cég?
Egy **romániai (székelyföldi) vegyes kiskereskedelmi + nagykereskedelmi vállalkozás**, valószínűleg
egy bolthálózat raktárkezelő szoftverének (WinMENTOR-szerű) exportjaiból. A számok **lej-ben (RON)**
vannak, az áfa neve **TVA**. A cégnek **6 gestiune-ja** (raktár/telephely/üzlet-egysége) van:

| Gestiune | Jelleg (feltételezés) | Cikkszám (PTOT) | Számlák (GERDIT) | Számla-érték áfa nélkül |
|---|---|---:|---:|---:|
| **BIRGITA** | bolt | 3 516 | 399 | 1 375 802 |
| **MUSKATLI** | bolt | 4 426 | 414 | 1 491 778 |
| **NAGYKERESKEDES** | nagykereskedés (B2B) | 278 | 1 341 | 660 272 |
| **SZEGEDI** | bolt | 3 250 | 389 | 925 533 |
| **VEGYESKE** | vegyesbolt | 3 323 | 366 | 891 325 |
| **ZETEKINCSE** | bolt (2025-ben nyílt) | 2 620 | 139 | 278 952 |

> A ZETEKINCSE nyitókészlete 0 → **év közben nyílt új egység**.
> A NAGYKERESKEDES kevés cikket tart (278), de sok számlát ad ki (1 341) → tipikus nagyker profil.

## A két mérési rendszer
A cég pénzügyét **két csatornán** méri:

1. **Kasszás kiskereskedelem** → `Adaos total 2025` (kategóriánkénti árrés).
   - Összforgalom (eladási ár áfa nélkül): **4 928 463 lei**, árrés (adaos): **1 169 996 lei**, 53 753 dokumentum.
2. **Számlás (factura) értékesítés B2B partnereknek** → `2025ZGY` (partner szerint) + `P2025 SZAMLA` (idő szerint, profittal).
   - Összérték áfa nélkül: **~696 000 lei**, profit: **168 851 lei (24,25%)**, 37 partner, 3 499 számla.

Ezt egészíti ki:
- `TOTAL GERDIT 2025` → **számla-regiszter** gestiune-onként (összesen ~5,62 M lei áfa nélkül).
- `2025 PTOT` → **készletmozgás** (mennyiségi, db) cikkenként és gestiune-onként.

## Igazolt összefüggések
- **`2025ZGY` ÖSSZESEN (695 612) ≈ `P2025 SZAMLA` ÖSSZESEN (696 177)** → ugyanaz a számlás értékesítés,
  egyszer **partner szerint**, egyszer **idő (hét/nap) szerint** bontva. Lásd [[02_ZGY_partnerek]] és [[04_P2025_szamla_profit]].
- ✅ **`TOTAL GERDIT` (5 623 663) = `Adaos` kasszás (4 928 463) + `P2025` számlás (696 177)** = 5 624 640,
  eltérés **−977 lei (0,017%)** → a GERDIT a **teljes árbevétel** telephelyenként, **eladás (nem beszerzés)**.
  A teljes 2025-ös árbevétel **~5,62 M lei**: ~88% kasszás kiskereskedelem, ~12% B2B számlás.
  Részletek: [[06_Tovabbi_felismeresek]] és [[05_GERDIT_szamlaregiszter]].

## Nyitott kérdések / feltételezések
- ~~A `TOTAL GERDIT` eladás vagy beszerzés?~~ **MEGOLDVA: eladás** (lásd fent).
- Az `Adaos` 4,93 M kasszás forgalma a **teljes hálózatra** vonatkozik (mind a 6 egység), nem csak egy boltra.
- A gestiune-ok pontos jellege (melyik bolt, melyik nagyker) feltételezés a névből — **erősítsd meg**.

## Számszerű "nagy kép" (2025)
- Kiskereskedelmi kasszás forgalom (áfa n.): **~4,93 M lei**, ráírt árrés: **~1,17 M lei** (~24% a beszerzésre).
- Számlás B2B értékesítés (áfa n.): **~0,70 M lei**, profit: **0,17 M lei** (24,3%).
- Átlagos árrés szint mindkét csatornán **~24%** — konzisztens.

## Egyedi szintézisek
- [[01_PTOT_keszletmozgas]] — készlet és mennyiségi forgás
- [[02_ZGY_partnerek]] — B2B vevők rangsora
- [[03_Adaos_arres]] — árrés kategóriánként
- [[04_P2025_szamla_profit]] — számlás profit időben
- [[05_GERDIT_szamlaregiszter]] — számla-regiszter
- [[06_Tovabbi_felismeresek]] — mélyebb adatbányászat (csatorna-egyezés, készlet-egészség, áfa, szezonalitás)
