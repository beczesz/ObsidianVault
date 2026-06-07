---
title: "Inference Farm — Usage Statistics (Q1 2026)"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "Q1 2026 usage statistics for the Sonrisa internal Inference Farm: 668,507 total requests and 5.77 billion total tokens processed, broken down by project (KnowledgeVault, Cloud Platform Services, Oracle-MÁV, Sagemcom-NAV-NTAK, YETTEL-Grip, Boeing, etc.) and by top users. This is the internal AI-adoption usage signal cited in CTO-Office strategy material ('Inference Farm processed 5.77B tokens in Q1 2026'). Source: AI_Inference_Farm_Statistics_2026_Q1.xlsx."
practice_area: cps-inference-farm
type: usage-stats
audience: internal-business
provenance: "Extracted by Forge on 2026-05-29 from ctooffice/Strategy/AI Adoption/06-AI-tools-tracking/AI_Inference_Farm_Statistics_2026_Q1.xlsx (modified 2026-03-02). Measures the internal AI-adoption inference farm (chat.int.sonrisa.hu), not external CPS customer billing."
id: 949a10ce-e135-4ff3-835c-2a06a2abc45f
index_schema_version: 1
bdos_index: false
---

# Usage Statistics — Q1 2026

> Source: `AI_Inference_Farm_Statistics_2026_Q1.xlsx`. **Internal** AI-adoption usage (employees + internal projects), not external CPS customer billing. This is the "5.77B tokens in Q1 2026" figure cited in CTO-Office strategy docs.

## Totals (Q1 2026, all models, all dates)

- **Total requests:** 668,507
- **Total tokens:** 5,773,156,822 (≈ 5.77 billion)

## By project (CustomerStats)

| Project | Requests | Total tokens |
|---|---|---|
| (blank / unattributed) | 449,105 | 2,939,317,434 |
| KnowledgeVault (billable) | 54,075 | 572,399,305 |
| Knowledgevault | 46,374 | 167,602,550 |
| Cloud Platform Services | 17,464 | 513,389,189 |
| Oracle-MÁV | 36,668 | 372,632,085 |
| SpinWheel | 9,800 | 357,552,661 |
| Sagemcom-NAV-NTAK (SS-K) | 7,983 | 239,171,735 |
| Continuity-Support | 10,370 | 237,198,783 |
| YETTEL-Grip | 18,563 | 148,984,319 |
| Boeing | 7,653 | 74,290,900 |
| Diligent UI modernization 2026 (Dev Team) | 2,923 | 65,076,155 |
| IDOMSOFT-Legacy | 2,947 | 52,949,132 |
| Princess House | 640 | 17,593,621 |
| Diligent Boards-Hydra (VInczeP) | 3,186 | 11,467,877 |
| Sagem-IDOM | 215 | 1,640,449 |
| Diligent Entities 2026 (Halo) | 235 | 885,785 |
| Oracle-MÁV (kicsik) | 100 | 389,727 |
| Synlab SDN | 88 | 384,556 |
| Collinear-Verity-1 | 55 | 97,695 |
| Consultancy | 36 | 79,335 |
| Global Blue 2.0 | 15 | 31,947 |
| Diligent | 12 | 21,582 |
| **Grand total** | **668,507** | **5,773,156,822** |

## Top users (by requests)

| User | Requests | Total tokens |
|---|---|---|
| Priegl Roland | 313,002 | 940,942,384 |
| Mihályi Miklós | 48,873 | 461,667,001 |
| Kasztl Richárd | 32,834 | 198,533,868 |
| Dezső Kende | 21,360 | 56,644,668 |
| Barczai Mátyás | 21,024 | 61,470,154 |
| Veres Péter | 18,157 | 162,280,883 |
| Pribyll Rómeó | 17,877 | 562,173,751 |
| Rédey Bálint | 16,054 | 196,519,644 |
| Zsolt Dobos | 13,605 | 70,982,339 |
| Attila Szász | 9,685 | 183,862,409 |
| Ceclan Sándor | 8,829 | 285,031,949 |
| Csorba Vince | 8,322 | 90,865,463 |

(90+ users total in the workbook; long tail omitted. CPS-relevant names present: Vaida Márk-Ádám 1,530 req; Peter Bakonyi 1,285; Becze Szabolcs 1,067; Kovács Marcell 1,249; Póda Sándor 614; Molnár Dániel 270; Török Bálint 95; Szántó Zoltán 74; Bánfi István 36.)

## Reading notes

- The largest single bucket is **unattributed** (449k requests / 2.94B tokens) — projects/users without a tag. Token-attribution hygiene is an open item (ties to the per-project tracking requirement in [04_business-model-pricing.md](04_business-model-pricing.md)).
- Highest token-intensity per request: SpinWheel (~36k tok/req), Sagemcom-NAV-NTAK (~30k), Continuity-Support (~23k), Cloud Platform Services (~29k) — RAG/long-context heavy workloads.
- Priegl Roland alone is ~47% of all requests — a single power user / automated pipeline.

## Related

- Token measurement params behind these stats → [04_business-model-pricing.md](04_business-model-pricing.md)
- The two-faces-of-IF context (internal vs commercial) → [00_SOURCE_INDEX.md](00_SOURCE_INDEX.md)
