---
topic: Platform Pricing / Revenue Share Model (DH)
created: 2026-04-15
last_updated: 2026-04-16
status: VALIDATED — meeting results confirm model
id: f80fa874-63c6-406d-9842-febc829188b0
index_schema_version: 1
---

# Brainstorm: Platform Pricing / Revenue Share Model

## Sessions
| Date | AI(s) Used | Key Outcome |
|------|-----------|-------------|
| 2026-04-15 | ChatGPT (Deák custom GPT) | **Paradigmaváltás:** nem jutalék, hanem savings pool elosztás. Frame: retail cost (20%) - online cost (6%) = 14% savings. |
| 2026-04-15 | Claude (szintézis) | Meeting checklist v2 - adatkérő kérdések struktúra + savings pool logika. |
| 2026-04-15 | Perplexity | Marketplace benchmarks: eMAG (7-25%), Allegro (4-15%), Wolt/Glovo (25-30%), La Ruche (20%), FarmDrop (15%). |
| 2026-04-15 | ChatGPT (2. iteráció) | KRITIKUS REFRAMING: benchmarkok = value extraction, DHOP = value creation. Platform 2-4% (start), 5-10% (scale). |
| **2026-04-15** | **Meeting (Szabolcs + Deák tulajdonosok)** | **MEGÁLLAPODÁS: 19,5% retail cost validálva. Phase 1: Customer 3% / Platform 6,6% / Deák 9,9%.** |
| 2026-04-16 | ChatGPT (post-meeting elemzés) | "Valid, élesben tesztelhető economic system." 2 kockázat: customer share alacsony + phase triggerek definiálandók. |

## AI Session Links
- ChatGPT: https://chatgpt.com/g/g-p-69cbee4a04c481918a2a738959b92361-deak/c/69da0a38-ce68-8391-bfb4-a2bbf24a66e7
- Perplexity: https://www.perplexity.ai/search/hogyan-mukodik-az-emag-marketp-DS_HTtItTeW_tY9RrZK8.g

## MEETING OUTCOME (2026-04-15) — LEGFONTOSABB SZEKCIÓ

### Validált adat
- **Retail inefficiency = 19,5%** (becsült 20% vs. mért 19,5% - szinte tökéletes)
- Konkrét boltok konkrét költségeit vizsgálták közösen

### Megállapodott elosztás — Phase 1 (Pilot)
| Kategória | % | 100.000 LEI forgalomnál |
|-----------|---|------------------------|
| Customer kedvezmény | **3%** | 3.000 LEI |
| Platform (Exar Labs) | **6,6%** | 6.600 LEI |
| Deák profit | **9,9%** | 9.900 LEI |
| **Összesen** | **19,5%** | **19.500 LEI** |

### Fázisterv
| Fázis | Platform % | Trigger |
|-------|-----------|---------|
| Phase 1 (Pilot) | **6,6%** | Indulás |
| Phase 2 (Scale) | **~7-9%** | Repeat rate >= 40% + heti rendelési szokás |
| Phase 3 (Multi-product) | **~9-12%** | AOV nő + cross-sell működik |

### ChatGPT értékelés a meetingről
- "Ez egy valid, élesben tesztelhető economic system."
- Jó: valós cost-alapú, Deák nyer az elején (9,9%), van customer share
- Kockázat: customer 3% alacsony, phase triggerek definiálandók
- Kritikus metrika: retention (ha nincs repeat -> újra kell osztani)

## Key Insights

### 1. A kérdés ROSSZ megfogalmazása (kritikus\!)
- Rossz: "Mennyi jutalékot kérjek?" - deal-negotiation frame, zero-sum
- Jó: "Hogyan osztjuk el a rendszerben keletkező hatékonysági nyereséget?" - positive-sum
- **Forrás:** ChatGPT, msg 36

### 2. A savings pool formula
```
Savings pool = Retail cost ratio - Online incremental costs
             = 19,5% (MÉRT\!)     - (~6%)
             = ~13,5% "új érték" minden rendelésnél
```
**Forrás:** ChatGPT, msg 38 | **VALIDÁLVA a tárgyaláson**

### 3. Az elosztás logikája (pre-meeting terv vs. tényleges)
| Szereplő | Terv (ChatGPT) | Tényleges megállapodás |
|----------|---------------|----------------------|
| Customer | 40-60% (pl. 7%) | **3%** (alacsonyabb) |
| Supplier (Deák) | 20-40% (pl. 4%) | **9,9%** (magasabb\!) |
| Platform (Exar Labs) | 15-30% (pl. 3%) | **6,6%** (magasabb) |

### 4. "Retention > Revenue" (early stage axiom)
- Customer share alacsonyabb lett mint tervezve (3% vs 7%)
- DE a Deák erős buy-in (9,9%) kompenzálja - motiváció magas
- **Forrás:** ChatGPT, msg 38, section 6

### 5. Ipari benchmark kontextus
| Platform típus | Commission | DHOP Phase 1 |
|----------------|-----------|-------------|
| eMAG | 7-25% | 6,6% - ALATTA |
| Wolt/Glovo | 25-30% | 6,6% - MÉLYEN ALATTA |
| La Ruche | 20% | 6,6% - ALATTA |
| FarmDrop | 15% | 6,6% - ALATTA |

## Decisions Made

### D-1 (2026-04-15): Framework váltás
- **Döntés:** Savings pool frame, NEM sávos %-modell.
- **Eredmény:** SIKERES - a meetingen ez a frame működött.

### D-2 (2026-04-15): Adatkérés prioritás
- **Döntés:** ELŐSZÖR adatot kérünk, NEM %-ot tárgyalunk.
- **Eredmény:** SIKERES - konkrét boltok költségeit közösen vizsgálták.

### D-3 (2026-04-15): Benchmark-alapú pozicionálás
- **Döntés:** Ipari benchmarkokat használjuk mint VÉDŐ pajzsot.
- **Eredmény:** Nem kellett használni - a közös modellezés elég volt.

### D-4 (2026-04-15): Platform részesedés korrekció
- **Döntés:** Platform start: 2-4% forgalomból.
- **Eredmény:** 6,6% lett - MAGASABB mint a terv, DE a cost-alapú modell indokolja.

### D-5 (2026-04-15): Tárgyalási frame végleges
- **Eredmény:** A frame MŰKÖDÖTT - közös realitás-építés lett belőle.

### D-6 (2026-04-15): A valódi versenyelőny
- **Nem:** alacsony commission. **Hanem:** measurable savings + habit loop.

### D-7 (2026-04-15, POST-MEETING): Megállapodott számok
- **Phase 1:** Customer 3% / Platform 6,6% / Deák 9,9% (= 19,5%)
- **Phase 2:** Platform ~7-9% (trigger: repeat >= 40%)
- **Phase 3:** Platform ~9-12% (trigger: AOV + cross-sell)

## Open Questions

- [x] ~~Mai meeting eredménye~~ -> SIKERES, számok megállapodva
- [ ] [HUMAN] Melyik testvér a döntéshozó? (Tisztázódott-e?)
- [ ] [CLAUDE] Szerződés/megállapodás draftelése
- [ ] Phase 2 trigger pontos definíció (40% repeat rate?)
- [ ] Savings perception mérés beépítése az app-ba
- [ ] Week 1-2 monitoring dashboard

## Context References

- `Business Development/pilot-husuzlet/deak-meeting-results-2026-04-15.md` (meeting jegyzőkönyv)
- `Business Development/pilot-husuzlet/BMC-v2.2.md` (szekció 5: Revenue Streams)
- `Business Development/pilot-husuzlet/deak-meeting-checklist-2026-04-15.md` (meeting előkészítő)
- `Business Development/pilot-husuzlet/market research/marketplace-benchmarks-2026-04-15.md`
- `CLAUDE.md` (Szabolcs + Exar Labs kontextus)