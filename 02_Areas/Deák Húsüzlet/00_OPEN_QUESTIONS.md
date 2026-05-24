---
title: 00_OPEN_QUESTIONS
generated_by: librarian v0.3
generated_at: 2026-05-11T00:00:00
scope: 02_Areas/Deák Húsüzlet/
mode: index
file_count: 180
id: 8eece5ea-adc9-4e00-913f-c00310784c24
index_schema_version: 1
---

# DH — Open Questions (tier-2)

> Minden "Open Questions / Nyitott kérdések / TODO / döntésre vár" markerrel jelölt kérdés. Forrás-fájl + sor. **Nem priorizálva.**

---

## 1. LEGAL / COMPLIANCE (beta-blokkoló)

| # | Kérdés | Forrás |
|---|--------|--------|
| L-1 | **Ki a jogi szolgáltató?** Exar Labs SRL vagy Deák Húsmíves? (DH-133, BLOCKER) | `Business Development/pilot-husuzlet/legal.md:153` |
| L-2 | **ANSVSA élelmiszer-szállítási engedély?** Hűtőlánc dokumentálva? (DH-136) | `Business Development/pilot-husuzlet/legal.md:153` |
| L-3 | ±10% súlytolerancia szövege bekerüljön-e az ÁSZF-be? | `savings-engine/Ideas/v0.3-product-types-spec.md:308` (Q7) |

---

## 2. SAVINGS ENGINE / v0.3 specifikus

| # | Kérdés | Forrás |
|---|--------|--------|
| SE-1 | 150 RON-os ingyenes szállítási küszöb végleges? (BLOCKER) | `savings-engine/Ideas/v0.3-running-savings-counter-spec.md:172` (Q1) |
| SE-2 | 2% kedvezmény 300 RON felett — launch-kor lép érvénybe? (BLOCKER) | `savings-engine/Ideas/v0.3-running-savings-counter-spec.md:172` (Q2) |
| SE-3 | Savings összeg becsült vagy végleges ár alapján? (BLOCKER) | `savings-engine/Ideas/v0.3-post-order-recap-spec.md:113` (Q1) |
| SE-4 | Konkrét súlytartományokat a Deák mészáros mikor validálja? | `savings-engine/Ideas/v0.3-product-types-spec.md:308` (Q6) |
| SE-5 | DH-51 zóna szabály: Sprint 3-ba behúzni vagy v0.4-be tolni? | `01_PROJECT_STATE.md:100`, `dev-roadmap-v2.0.md` |
| SE-6 | Family Bundles spec — egyéb kérdések | `savings-engine/Ideas/v0.3-family-bundles-spec.md:160` |
| SE-7 | Reorder / Favorite orders / Product preferences / Shared basket kérdések | `savings-engine/Ideas/v0.3-reorder-last-order-spec.md:134`, `v0.4-favorite-orders-spec.md:141`, `v0.4-product-preferences-spec.md:242`, `v0.4-shared-basket-spec.md:96` |

---

## 3. PRODUCT CATALOG / Termékek

| # | Kérdés | Forrás |
|---|--------|--------|
| P-1 | Csirke termékek — `friss_csirkehus` vagy `friss_serteshus` alá? | `Products/meetings/2026-05-07_decisions.md:277`, `_unified-product-master.md:371` |
| P-2 | `roppanos_virsli` — `kolbasz_szalami`-ba vagy új `virsli`-ba? | `Products/meetings/2026-05-07_unified-product-master.md:377` |
| P-3 | Csirke mellcsont ára — Speaker 2 mondta „26", nem 100%-os | `Products/meetings/2026-05-07_decisions.md:280` |
| P-4 | Hasrész 3-4 sub-termékre bontás — pontosan hány? | `Products/meetings/2026-05-07_decisions.md:281` |
| P-5 | Internal code (014, stb.) JSON-ba? Új schema mező? | `Products/meetings/2026-05-07_decisions.md:282` |
| P-6 | Szezonális termékek megjelenítése | `Products/meetings/2026-05-07_decisions.md:283` |
| P-7 | Növendék szalámi bőr eltávolítás — termelő képzése | `Products/meetings/2026-05-07_decisions.md:284` |
| P-8 | Receptcikk feature — érdemes gyűjteni a tartalmat | `Products/meetings/2026-05-07_decisions.md:285` |
| P-9 | Felár szeletelésért / pácolásért? (Phase 1: NEM) | `product-variations/product-variations-spec-v1.0.md:355` (Q1) |
| P-10 | Maximum opció termékenként (most max 2 vs. max 3) | `product-variations/product-variations-spec-v1.0.md:355` (Q2) |
| P-11 | DH-173 termék testreszabás — top 5 SKU? Milyen opciók? | `brainstorm_dh-feature-prioritization.md:127` |

---

## 4. ZÓNA-DETEKCIÓ / Logisztika

| # | Kérdés | Forrás |
|---|--------|--------|
| Z-1 | Településlista a Keresztúri körhöz — melyik 14 falu? | `brainstorm/brainstorm_zona-detektacio.md:180` |
| Z-2 | Profil mentés: kiválasztást user profilba mentsük? | `brainstorm/brainstorm_zona-detektacio.md` |
| Z-3 | GPS permission prompt szövege | `brainstorm/brainstorm_zona-detektacio.md` |
| Z-4 | Phase 1 vs Phase 2 határ — Sprint 4 vagy 5? | `brainstorm/brainstorm_zona-detektacio.md` |

---

## 5. FALUSI ROUTE PILOT

| # | Kérdés | Forrás |
|---|--------|--------|
| R-1 | [SZABOLCS] Melyik falvak az első route? (Szentegyháza + Zetelaka) | `brainstorm/brainstorm_falusi-hazhozszallitas.md:168` |
| R-2 | [SZABOLCS] Deák kapacitás: heti 2 extra route? | uo. |
| R-3 | [SZABOLCS] Ki vezeti a szállítást? | uo. |
| R-4 | [SZABOLCS] Mikor indulhat a falusi pilot? | uo. |
| R-5 | [SZABOLCS] 120 RON küszöb reális? | uo. |
| R-6 | [CLAUDE] Route térkép: konkrét útvonaltervezés | uo. |
| R-7 | [CLAUDE] Founding 50 falusi kiterjesztés vagy külön cohort? | uo. |
| R-8 | Route-go threshold: 8 (breakeven) vagy 9-10 (cushion)? | `brainstorm/brainstorm_bmc-mega-review.md:357` |
| R-9 | Ambassador kompenzáció | uo. |
| R-10 | Single Courier helyettesítés — backup sofőr? | uo. |
| R-11 | Falusi second order target — 28 nap vagy más? | uo. |
| R-12 | Stop cap frissítés szükséges a route OPEX miatt? | uo. |
| R-13 | Sprint 4: route-ready platform VAGY natív mobil? | uo. |
| R-14 | Rural route spec részletes nyitott kérdései | `rural-delivery/rural-route-spec-v1.0.md:1058` |
| R-15 | Deák szállítási naprendje fix? | `brainstorm/brainstorm_retention-loop-decision-v1.md:169` |

---

## 6. FOUNDING 50

| # | Kérdés | Forrás |
|---|--------|--------|
| F-1 | Gratuláció modal szöveg | `brainstorm/brainstorm_founding50.md:64` |
| F-2 | Román nyelvű verziók szükségesek? | uo. |
| F-3 | Kampány indulás dátum | uo. |
| F-4 | Toborzási csatorna: bolt + QR + Facebook is? | uo. |
| F-5 | Budget cap: 50 fő × 3 hó × ingyenes szállítás | uo. |
| F-6 | Jira sub-taskokra bontás | uo. |

---

## 7. PRICING / REVENUE SHARE

| # | Kérdés | Forrás |
|---|--------|--------|
| RS-1 | [HUMAN] Melyik testvér a döntéshozó? | `brainstorm/brainstorm_deak-pricing-revenue-share.md:115` |
| RS-2 | [CLAUDE] Szerződés/megállapodás draftelése | uo. |
| RS-3 | Phase 2 trigger pontos definíció (40% repeat rate?) | uo. |
| RS-4 | Savings perception mérés beépítése az app-ba | uo. |
| RS-5 | Week 1-2 monitoring dashboard | uo. |
| RS-6 | Pénzügyi adatok (per-product margin, waste%, delivery) mikor? | `brainstorm_strategiai-attekintes-v1.md:151`, `brainstorm_retention-loop-decision-v1.md:169` |

---

## 8. KPI / MÉRÉS

| # | Kérdés | Forrás |
|---|--------|--------|
| K-1 | Magic Moment validálása — első sikeres rendelés vs. minőség? | `KPI Framework - v1.3.md:457` |
| K-2 | Retention period — 14 nap validált a szokásból? | uo. |
| K-3 | Margin reality — csomagolás + koordinációs idő beleszámít? | uo. |
| K-4 | Supplier conflict risk — Ibi bevonása | uo. |
| K-5 | Scaling threshold — milyen metrikák városba terjeszkedéshez? | uo. |

---

## 9. STRATÉGIA / PARTNERSHIP

| # | Kérdés | Forrás |
|---|--------|--------|
| ST-1 | Sonrisa szerződés exclusivity klauzula? (BLOCKER) | `brainstorm/brainstorm_frappe-partnership-strategy_SYNTHESIS.md:238` |
| ST-2 | €20k cap és 12 hó horizont elfogadható? | uo. |
| ST-3 | Vertikum-elsőbbség: Craft Food vagy edu (Ignis) vagy mindkettő? | uo. |
| ST-4 | Cert-jelölt 2 fejlesztő — konkrét nevek? | uo. |
| ST-5 | Lokalizációs csomag dev kapacitás (5-8 hét bench)? | uo. |
| ST-6 | Reális 12-hó revenue target Frappe partnership-re? | `brainstorm_frappe-partnership-strategy.md:70` |
| ST-7 | Mobil app Sprint 4 cél? | `brainstorm/brainstorm_dh-feature-prioritization.md:127` |
| ST-8 | Melyik az első falusi pilot település? | uo. |
| ST-9 | Shared Basket (DH-149) manuális MVP-vel tesztelhető? | uo. |
| ST-10 | Partnerségi megállapodás (írásbeli) mikor? | `brainstorm/brainstorm_strategiai-attekintes-v1.md:151` |
| ST-11 | "ENGINE v1" — savings calculation + margin + threshold | uo. |
| ST-12 | Decision Memo formátum | uo. |
| ST-13 | EU pályázatok rövid ellátási láncokra Romániában | uo., `brainstorm_dhop-valsag-pozicionalas.md:90` |
| ST-14 | "Heti ajánlott kosár" (L2 ROUTINE) melyik sprintbe? | `brainstorm/brainstorm_retention-loop-decision-v1.md:169` |
| ST-15 | Üzemanyag-áremelkedés hatása a Deákra? | `brainstorm/brainstorm_dhop-valsag-pozicionalas.md:90` |
| ST-16 | Más helyi termelő érdeklődne korai csatlakozásra? | uo. |
| ST-17 | Ki dönt a 2 testvér közül kritikus helyzetben? (governance SPOC) | `brainstorm/brainstorm_pre-launch-fears_SYNTHESIS.md` |

---

## 10. EXAR LABS 24-MONTH STRATEGY

| # | Kérdés | Forrás |
|---|--------|--------|
| E-1 | Mely 2-3 iparágban legyenek referenciák 2 év alatt? | `Business Development/strategy/24-month-roadmap.md:168` |
| E-2 | Revenue share % — sustainable a butcher pilothoz? | uo. |
| E-3 | Bench capacity több pilot között? | uo. |

---

## 11. MARKETING / GTM

| # | Kérdés | Forrás |
|---|--------|--------|
| M-1 | Május 1 vizuál (fotó/videó) — Szabolcs feladata | `brainstorm/brainstorm_majus1-grill-posztok.md:60` |
| M-2 | Poszt ütemezés — melyik napon melyiket | uo. |
| M-3 | Hiányzó / jövőbeli UI string-ek | `plugins/deak-design/context/ui-strings.md:348` |

---

## 12. BDOS / AGENT SYSTEM (new v0.3)

| # | Kérdés | Forrás |
|---|--------|--------|
| BD-1 | Következő agent prioritás — Product Strategist vs. Operations Steward vs. Validator? | `brainstorm/brainstorm_bdos.md` |
| BD-2 | Agent paletta 4-5 fő mellett megálljon (sprawl elkerülés) | uo. |
| BD-3 | Perplexity bekapcsolása — agent-based BD frameworks prior art | uo. |

---

## 13. EGYÉB

| # | Kérdés | Forrás |
|---|--------|--------|
| O-1 | DHOP-siker ötlettár v4.0 nyitott kérdései | `Business Development/pilot-husuzlet/market research/dhop-siker-otlettar-v4.0.md:303` |
| O-2 | Competitive advantage következő nyitott kérdés | `Business Development/strategy/competitive-advantage.md:128` |
| O-3 | Pre-launch fears multi-AI kérdéslista | `brainstorm/brainstorm_pre-launch-fears.md:62` |
| O-4 | Exar Labs stratégia következő nyitott kérdés | `memory/projects/exarlabs-strategia.md:50` |
| O-5 | DH Savings Engine Base Ideas — Open Questions / TODO | `Business Development/pilot-husuzlet/savings-engine/DH Savings Engine - Base Ideas.md:540` |
