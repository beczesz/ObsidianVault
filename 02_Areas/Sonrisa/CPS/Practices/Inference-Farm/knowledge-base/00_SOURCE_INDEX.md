---
title: "Inference Farm Knowledge Base — SharePoint Source Index"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "Master catalog of all Inference Farm knowledge consolidated from Sonrisa SharePoint into the CPS practice area on 2026-05-29. Lists every source document (canonical IF site, Sales/BD folder, Cloud Guild Technical, CTO Office stats, personal OneDrives), its SharePoint location, type, last-modified date, retrieval status, and which knowledge-base note distills it. Entry point for anyone tracing a vault fact back to its original SharePoint source."
practice_area: cps-inference-farm
type: source-index
audience: internal-engineering
provenance: "Compiled by Forge (Practice Steward) via Microsoft Graph SharePoint search, 2026-05-29. Extraction pass over org-wide SharePoint, strictly Inference-Farm-scoped."
id: 49598174-10ac-488f-a034-01ed872cf726
index_schema_version: 1
bdos_index: false
---

# Inference Farm Knowledge Base — Source Index

> Consolidated **2026-05-29** by Forge from Sonrisa SharePoint. All knowledge below was extracted into the topic notes in this `knowledge-base/` folder. This index maps every distilled fact back to its SharePoint source so the original is always traceable.

## How this folder is organized

| Note | Covers |
|---|---|
| [01_architecture-infrastructure.md](01_architecture-infrastructure.md) | AWS IaC stack (Terraform/Terragrunt), architecture layers, deployment, Blackwell + vLLM server setup, monitoring, live URLs |
| [02_performance-case-study.md](02_performance-case-study.md) | Production performance case study — Qwen3.5-397B-NVFP4 on 4 GPUs (Apr–May 2025) |
| [03_benchmarks-model-sizing.md](03_benchmarks-model-sizing.md) | vLLM benchmarks, instance/cost comparison, model right-sizing, open-source model scoring, load-test design |
| [04_business-model-pricing.md](04_business-model-pricing.md) | OPEX, pricing tiers (A–D), margins, token-based pricing measurement parameters |
| [05_strategy-requirements.md](05_strategy-requirements.md) | LLMaaS business plan, 10-area strategy checklist, AI integration requirements |
| [06_usage-statistics.md](06_usage-statistics.md) | Q1 2026 internal usage (5.77B tokens, by project & user) |
| [07_analytics-telemetry.md](07_analytics-telemetry.md) | The `stats/` analytics pipeline: dashboards + raw telemetry (logs.out, nvidia-smi) identified |
| [08_capacity-analysis.md](08_capacity-analysis.md) | Data-driven capacity model: current limit, headroom to 200+ users, binding constraint |

## Important context: two faces of the Inference Farm

The knowledge below spans **two related uses of the same private inference capability**:

1. **Internal AI-adoption inference farm** (`chat.int.sonrisa.hu`) — CTO-Office driven, employees + internal projects (e.g. KnowledgeVault). This is what the Q1 2026 usage stats measure.
2. **CPS commercial AWS Inference Farm / LLMaaS** (`ai.sonrisa.hu`, AWS profile `awsfarm`) — the productized, customer-facing service this practice area owns. The 2026 case study (Qwen3.5-397B-NVFP4) and the `AwsInFarm` IaC repo are this track.

The 2025 business-plan and benchmark material predates the productization and used smaller models (Qwen3-32B, QwQ-32B, Qwen3-14B). The timeline matters when reading cost/perf numbers.

## Source catalog

### Cluster 1 — Canonical IF site (`CloudPlatformServices-Inferencefarm`)

| Document | Type | Modified | Status | Distilled into |
|---|---|---|---|---|
| [README.md](https://sonrisakft.sharepoint.com/sites/CloudPlatformServices-Inferencefarm/Megosztott%20dokumentumok/AwsInFarm/README.md) | IaC repo readme | 2026-05-27 | ✅ extracted | 01 |
| [blackwell-vllm-setup.md](https://sonrisakft.sharepoint.com/sites/CloudPlatformServices-Inferencefarm/Megosztott%20dokumentumok/AwsInFarm/blackwell-vllm-setup.md) | Setup guide | 2026-05-27 | ✅ extracted | 01 |
| [InFarm_CaseStudy.docx](https://sonrisakft.sharepoint.com/sites/CloudPlatformServices-Inferencefarm/Megosztott%20dokumentumok/AwsInFarm/InFarm_CaseStudy.docx) | Performance case study | 2026-05-27 | ✅ extracted | 02 |
| [Infarm OPEX.xlsx](https://sonrisakft.sharepoint.com/sites/CloudPlatformServices-Inferencefarm/Megosztott%20dokumentumok/Infarm%20OPEX.xlsx) | Monthly fixed costs | 2026-05-28 | ✅ extracted | 04 |
| [vllm_dashboard.html](https://sonrisakft.sharepoint.com/sites/CloudPlatformServices-Inferencefarm/Megosztott%20dokumentumok/AwsInFarm/vllm_dashboard.html) | Live stats dashboard | 2026-05-27 | 🔗 linked (stats in 02) | 02 |
| [gpu_dashboard3.html](https://sonrisakft.sharepoint.com/sites/CloudPlatformServices-Inferencefarm/Megosztott%20dokumentumok/AwsInFarm/) | GPU telemetry dashboard | 2026-05-27 | 🔗 linked | 02 |
| [infarm.drawio.png](https://sonrisakft.sharepoint.com/sites/CloudPlatformServices-Inferencefarm/Megosztott%20dokumentumok/AwsInFarm/) | Architecture diagram | 2026-05-27 | 🔗 linked (layers in 01) | 01 |
| logs.out, nvidia_smi.log | Raw telemetry | 2026-05-27 | ⏭️ skipped (raw logs) | — |

### Cluster 2 — Sales / Business Development (`sites/sales/.../Business development/Inference Farm`)

| Document | Type | Modified | Status | Distilled into |
|---|---|---|---|---|
| [Plan.docx](https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/General/Planning/Services/Cloud%20Platform%20Services/Business%20development/Inference%20Farm/Plan.docx) | Merged LLMaaS business plan | 2025-09-05 | ✅ extracted | 05 |
| [Planning.docx](https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/General/Planning/Services/Cloud%20Platform%20Services/Business%20development/Inference%20Farm/Planning.docx) | 10-area strategy checklist | 2025-07-31 | ✅ extracted | 05 |
| [Inference Farm - Business Plan.xlsx](https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/General/Planning/Services/Cloud%20Platform%20Services/Business%20development/Inference%20Farm/Inference%20Farm%20-%20Business%20Plan.xlsx) | Cost model + pricing tiers | 2025-08-28 | ✅ extracted | 04 |
| [OpenSource Model Comparison.xlsx](https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/General/Planning/Services/Cloud%20Platform%20Services/Business%20development/Inference%20Farm/OpenSource%20Model%20Comparison.xlsx) | 20-dimension model scoring | 2025-09-05 | ✅ extracted | 03 |
| [AWS farm main goals.odt](https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/General/Planning/Services/Cloud%20Platform%20Services/Business%20development/Inference%20Farm/AWS%20farm%20main%20goals.odt) | Goals + model machine reqs | 2025-08-22 | ✅ extracted | 03 |
| [Benchmark.docx](https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/General/Planning/Services/Cloud%20Platform%20Services/Business%20development/Inference%20Farm/Benchmark.docx) | Load-test design | 2025-08-06 | ✅ extracted | 03 |
| Comparison/ (Open Notebook.one) | OneNote section | 2025-08-06 | ⚠️ inaccessible (OneNote format) | — |

### Cluster 3 — Cloud Guild Technical (`sites/cloudguild/.../Technical/Inference Farm`)

| Document | Type | Modified | Status | Distilled into |
|---|---|---|---|---|
| [Metrics.docx](https://sonrisakft.sharepoint.com/sites/cloudguild/Megosztott%20dokumentumok/Technical/Inference%20Farm/Metrics.docx) | Token-pricing measurement params | 2025-07-29 | ✅ extracted | 04 |

### Cluster 4 — CTO Office stats

| Document | Type | Modified | Status | Distilled into |
|---|---|---|---|---|
| [AI_Inference_Farm_Statistics_2026_Q1.xlsx](https://sonrisakft.sharepoint.com/sites/ctooffice/Megosztott%20dokumentumok/Strategy/AI%20Adoption/06-AI-tools-tracking/AI_Inference_Farm_Statistics_2026_Q1.xlsx) | Q1 2026 usage stats | 2026-03-02 | ✅ extracted | 06 |

### Cluster 5 — Offer + personal OneDrives

| Document | Type | Modified | Status | Distilled into |
|---|---|---|---|---|
| [AI Integration Requirement Document.docx](https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/General/Planning/Services/Cloud%20Platform%20Services/offers/AWS%20Inference%20Infra/AI%20Integration%20Requirement%20Document.docx) | Requirements (Bedrock vs self-host) | 2025-06-21 | ✅ extracted | 05 |
| [vllm_benchmark_overview_upd.docx](https://sonrisakft-my.sharepoint.com/personal/ceclan_sandor_sonrisa_hu/Documents/vllm_benchmark_overview_upd.docx) | Sept 2025 benchmark + cost summary | 2025-09-16 | ✅ extracted | 03 |
| [LLM_model_right_sizing.xlsx](https://sonrisakft-my.sharepoint.com/personal/ceclan_sandor_sonrisa_hu/Documents/LLM_model_right_sizing.xlsx) | Model right-sizing + tiers | 2025-06-27 | ✅ extracted (≈Business Plan.xlsx) | 03, 04 |
| [vLLM benchmark.xlsx](https://sonrisakft-my.sharepoint.com/personal/bakonyi_peter_sonrisa_hu/Documents/vLLM%20benchmark.xlsx) | Raw benchmark workbook (v4) | 2025-11-06 | 🔗 linked (summarized by overview doc) | 03 |
| [benchmark test.pdf](https://sonrisakft-my.sharepoint.com/personal/becze_szabolcs_sonrisa_hu/Documents/Microsoft%20Teams%20Chat%20Files/benchmark%20test.pdf) | Benchmark (Teams share) | 2025-08-06 | 🔗 linked | 03 |
| [AWS Inference Farm.loop](https://sonrisakft-my.sharepoint.com/personal/ceclan_sandor_sonrisa_hu/Documents/Meetings/AWS%20Inference%20Farm.loop) | Meeting loop (Grafana/frontend URLs + agenda) | 2025-10-16 | ⚠️ inaccessible format (URLs captured in 01) | 01 |

## Excluded (out of strict scope)

Passing-mention documents NOT pulled in (mention IF as one item among many): CTO Pulse episodes, AI Strategy Manifestos, AI Adoption Initiative pages, responsible-AI policy docs, weekly CTO meeting summaries, Póda Sándor CV/profile, all timesheets / activity reports, AI Competency customer tracker, StarDD bootstrap memo.

## Local stats mirror (in-vault)

Beyond SharePoint, the practice carries a local analytics mirror at [../stats/](../stats/) — the `dashboard.html` (AI-Usage-Analytics), `build_dashboard.py` generator, and `raw/` telemetry (113 MB `logs.out`, `nvidia_smi.log`, `infarm.drawio.png`, generated `vllm_dashboard.html` + `gpu_dashboard2.html`). Identified in [07_analytics-telemetry.md](07_analytics-telemetry.md). These raw artifacts are the local copies of the SharePoint `AwsInFarm` telemetry and the data behind the [performance case study](02_performance-case-study.md).

## Retrieval method

All documents accessed via Microsoft Graph (SharePoint/OneDrive) on 2026-05-29. Office formats (.docx, .xlsx, .odt, .pdf) were read as text; HTML dashboards, the .drawio.png diagram, and raw logs were linked rather than transcribed; OneNote (.one) and Loop (.loop) formats are not text-readable via Graph and are linked only.
