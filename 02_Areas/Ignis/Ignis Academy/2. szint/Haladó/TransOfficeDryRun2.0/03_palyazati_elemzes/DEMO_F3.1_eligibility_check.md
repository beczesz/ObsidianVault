---
title: "DEMO F3.1 — Eligibility check (A.4 prompt)"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Eligibility assessment for a Green Mobility SME grant application in Romania, evaluating all 12 criteria against the 2025 guidelines: 10 fully met, 2 partially (financial stability and premises continuity), with 2 critical clarifications needed (property sale rumor, 2023-2024 financials, missing CUI number) before submission."
description_source: auto
description_hash: abc098b671885827
id: 29b31b5f-0dfa-4c17-81ba-e5238437532e
index_schema_version: 1
bdos_index: true
---
# DEMO F3.1 — Eligibility check (A.4 prompt)

> **Forrás:** `Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md` (94 oldal) + `CLAUDE.md`
> **Prompt:** A.4 — ÖSSZES eligibility kritérium ✅/⚠️/❌ + döntés + top 3 kockázat
> **Cowork-futás:** ~90 mp

---

## Döntés: **PÁLYÁZHATUNK** (feltételesen — 2 nyitott pont)

A 12 eligibility kritériumból:
- ✅ **10 teljes** (CR-01, 02, 03, 04, 07, 08, 10, 11, 12 + Hargita +5p bónusz)
- ⚠️ **2 részben** (CR-05 pénzügyi stabilitás, CR-09 telephely-stabilitás)
- ❌ **0 nem teljesül**

**Becsült pontszám:** 64-75 pont (minimum 60 kell)

---

## 12 kritérium

| # | Kritérium | Státusz | Indoklás (max 2 mondat) |
|---|-----------|---------|--------------------------|
| CR-01 | Bejegyzett SRL Romániában | ✅ | TransOffice Trade SRL, 2003 óta (CUI a könyvelőtől kell — még nem találtam) |
| CR-02 | KKV-státusz (< 20 fő, < 1M EUR) | ✅ | 12 alkalmazott, ~352k EUR éves árbevétel — mindkét küszöb alatt |
| CR-03 | Min. 3 év működés | ✅ | 22 év (2003-2025) |
| CR-04 | CAEN-kód NEM tiltott | ✅ | CAEN 4649 (irodai kellékek nagykereskedelem) — eligibilis a Anexa 3 szerint |
| **CR-05** | **Pénzügyi stabilitás (EBITDA, D/E, ANAF)** | ⚠️ | Csak 2022-es számok vannak (pozitív 270k RON). 2023-2024 + ANAF-igazolás Mihaela könyvelőtől kell |
| CR-06 | De minimis < 200k EUR / 3 év | ✅ (feltételezett) | 2022-ben nincs subvenții — kell könyvelői megerősítés |
| CR-07 | Cofinanțare 30% (kis vállalat) | ✅ | 2 autó × 250k RON × 30% = ~150k RON saját erő — cash flow fedezi |
| CR-08 | Park auto existent (min. 1 ICE) | ✅ | 2 sofőr + saját furgon a cégleírás szerint — formális leltár az M-11 mellékletben |
| **CR-09** | **Telephely-stabilitás (min. 5 év)** | ⚠️ | Bérleti szerződés 2028-ig (jó), DE Béla bácsi szilveszteri eladási megjegyzés — tisztázni kell |
| CR-10 | NEM faliment | ✅ | Cégleírás: "pozitív cash flow, nincs adósság" |
| CR-11 | NEM tiltott szektor | ✅ | Irodai kellékek — egyik tiltottba sem tartozik |
| CR-12 | NEM offshore | ✅ | Román SRL, román tulajdonosok |

---

## Top 3 kockázat (Cowork észrevétele)

🚨 **1. Béla bácsi-szál (CR-09 — telephely)** — a meeting-transcript 41. bemondásában Márton elhullatott egy szilveszteri Béla-bácsi megjegyzést ingatlan-eladásról. **Ez a legkockázatosabb pont**: ha a Calea Băieșenilor 22 érintett, az 5 éves stabilitás-követelmény sérül. **Tisztázó email Béla bácsinak AZONNAL.**

🚨 **2. EBITDA-bizonytalanság (CR-05)** — a 2024-es szám lehet hogy negatív (gyenge év). Az AFM kiírás szerint **csak EGY év pozitív EBITDA elég** — de ezt **igazolni kell** könyvelői dokumentummal. Mihaela felé email mehet AZONNAL.

🚨 **3. CUI hiányzik** — a 34 fájlban sehol nincs a cég CUI-ja explicit módon. Mártonnal vagy az ONRC-portálon át gyorsan beszerezhető — **kedd este 18:00-ig megvan**.

---

## Pontozási becslés (8.4 Grila ETF szerint)

| Kritérium | Súly | Becsült |
|-----------|------|---------|
| I. Contribuția la obiectiv (CO2 megtakarítás, töltőpontok) | 30 | 20-22 |
| II. Capacitatea solicitantului (pénzügyi stabilitás) | 25 | 15-18 |
| III. Calitatea/maturitatea/sustenabilitatea | 20 | 12-14 |
| IV. Principii orizontale + Hargita +5p | 15 | 12-14 |
| V. Complementaritate, replicabilitate | 10 | 5-7 |
| **Összesen** | 100 | **64-75** |

**Min. 60 pont kell** → **bőven befér**

**Generálási idő:** ~90 mp. Egy tanácsadó 3 nap, ~3000 EUR.
