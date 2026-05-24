---
title: 00_DECISIONS_INDEX
generated_by: librarian v0.5
generated_at: 2026-05-22T10:00:00
scope: /Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/01_Projects/Gergely István
mode: index
file_count: 25
id: 35bbb60a-2ebd-4f92-850d-33cc93eb7d95
index_schema_version: 1
---

# 00_DECISIONS_INDEX — Gergely István projekt

> Megjegyzés: Ez a projekt elemzési/szintézis munkát dokumentál, nem klasszikus döntéseket (ADR-eket). Az alábbiak az elemzés során tett módszertani és értelmezési döntések, amelyek az output minőségét befolyásolják.

---

## Módszertani döntések

### M-01 — Az árrés számítási alapja
- **Döntés:** Az `Adaos` mező árrés-%-ját az **eladási forgalomra** vetítve számítjuk (nem a beszerzésre).
- **Forrás:** `Szintezisek/03_Adaos_arres.md` — Végösszeg blokk
- **Indok:** A fájlban az `Adaos / Valoare vanzare` hányados adja a természetes árrés%-ot; a "~31% a beszerzésre rávetítve" megjegyzésként szerepel.

### M-02 — ZGY és P2025 azonosságának igazolása
- **Döntés:** A `2025ZGY` és `P2025 SZAMLA` adatforrások **ugyanazt** az értékesítési halmazt tükrözik (695 612 ≈ 696 177 RON — kerekítési eltérés).
- **Forrás:** `Szintezisek/00_Attekintes.md` — "Igazolt összefüggések" szakasz; `Szintezisek/04_P2025_szamla_profit.md`
- **Indok:** A két szám 0,08%-on belül egyezik; a számlák száma (3 499) mindkét fájlban konzisztens.

### M-03 — Gestiune-jellegek feltételezés alapján kezelve
- **Döntés:** A gestiune-ok jellege (bolt vs. nagyker) névből következtetett — **nem tekinthető igazolt ténynek**.
- **Forrás:** `Szintezisek/00_Attekintes.md` — lábj., "A gestiune-ok pontos jellege... feltételezés"
- **Indok:** A szoftverexportban nincs explicit típusmező; visszaigazolás a tulajdonostól szükséges (lásd OPEN_QUESTIONS K-02).

### M-04 — Mennyiségi összegek kezelése
- **Döntés:** A PTOT gestiune-szintű mennyiségi összegei **csak nagyságrendi jelzésként** értelmezhetők — különböző UM-ek (db, kg, l) keverednek.
- **Forrás:** `Szintezisek/01_PTOT_keszletmozgas.md` — "Gestiune-szintű összegzés" megjegyzés

### M-05 — November adat kezelése
- **Döntés:** A november kiemelkedően alacsony B2B forgalma (27 227 RON) **a B2B csatorna jelensége, nem az egész cégé** — a teljes árbevételben november 405 e lei, nincs összeomlás.
- **Forrás:** `Szintezisek/04_P2025_szamla_profit.md` — "November mély gödör"; `Szintezisek/06_Tovabbi_felismeresek.md` — "Szezonalitás" szakasz
- **Indok:** A 06-os szintézis igazolta, hogy a kasszás kiskereskedelem stabilizálja az évet; a novemberi gödör szezonvégi HoReCa/turizmus-csökkenésre utal.

### M-06 — Termék-kategorizálás módszere és korlátai
- **Döntés:** A dashboard v2 (data_v2.json) termék→meta-kategória besorolása **kulcsszavas** — a meglévő cikknév alapján automatikusan. Ez ~74%-os lefedettséget ad; a maradék "besorolatlan" (Egyéb / technikai).
- **Forrás:** `Szintezisek/07_Dashboard_es_leszallitottak.md` — "Mire költenek" táblázat lábj.
- **Indok:** A cikktörzs árucsoportja nem állt rendelkezésre; kulcsszavas becslés ez esetben elfogadható első lépésként. A pontos besoroláshoz adatkérő #3 (cikktörzs kategória-mapping) szükséges.
- **Következmény:** A meta-kategória arányok (~74% lefedettsége erejéig) megbízhatóak; a maradék ~26% részben besorolatlan, részben esetleg más csoportba kerülhet a pontos mapping után.

### M-07 — ELV: "ne becsülj semmit"
- **Döntés:** A dashboard v2-ből kikerült minden becsült adat (elsősorban: becsült profit/üzlet gestiune-szinten). Csak tényadat jelenik meg; ahol egy nézet csak hálózati szinten létezik, a panel ezt explicit jelzi.
- **Forrás:** `Szintezisek/07_Dashboard_es_leszallitottak.md` — "Tervezési elvek"
- **Indok:** A gestiune-szintű árrés nem áll rendelkezésre (csak hálózati összesített Adaos van); a hálózati átlag-árréssel (23,7%) becsült telephely-profit félrevezető lenne.

---

## Értelmezési döntések — LEZÁRTAK

### É-01 — GERDIT jellege (eladás vs. beszerzés) — LEZÁRVA
- **Állapot:** MEGOLDOTT — a GERDIT **eladási** számlákat tartalmaz
- **Bizonyíték:** Adaos kasszás (4 928 463) + P2025 B2B (696 177) = 5 624 640 ≈ GERDIT 5 623 663; eltérés −977 lej (0,017%)
- **Forrás:** `Szintezisek/06_Tovabbi_felismeresek.md` — "A csatornák összeállnak" szakasz
- **Következmény:** A GERDIT az összes telephely teljes értékesítési forgalmát tükrözi; a PTOT Intrari-val való párosítás (mint ha GERDIT = beszerzés lenne) **nem releváns**.

---

## Értelmezési döntések — FÜGGŐBEN

### É-02 — Besorolatlan "Total ..." sor az Adaos-ban
- **Állapot:** FÜGGŐBEN
- **Forrás:** `Szintezisek/03_Adaos_arres.md` — "Az első, név nélküli Total... sor" bekezdés
- **Következmény:** 70,2%-os árrés-sor (90 231 RON forgalom) — rendkívüli értéke miatt kategória-azonosítás szükséges.

### É-03 — Gestiune-szintű profit — NYITOTT, adatkérőre vár
- **Állapot:** NYITOTT — adatkérő #1 (telephelyi árrés/önköltség riport) megoldaná
- **Forrás:** `Szintezisek/08_Adatkero_lista.md` — #1 pont; `Szintezisek/07_Dashboard_es_leszallitottak.md` — "Tervezési elvek"
- **Következmény:** Jelenleg nem számolható valós profit üzletenként. A becsült adat szándékosan kikerült a dashboardból (ELV, M-07).
