---
title: "Inference Farm — Business Model, OPEX & Pricing"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "The Inference Farm / LLMaaS commercial model: monthly OPEX breakdown (~€2,801/mo fixed: CPS support, AWS, Lenovo hosting, power), the 4-tier service model (Tier A 24/7 dedicated → Tier D shared, Qwen3-32B 4-bit on g5.12xlarge), per-tier cost/margin/subscription economics (margins 48%–498%), on-demand vs spot instance cost simulation with per-1M-token cost ($0.56–$4.72), and the token-based pricing measurement parameters the DevOps team must capture (TPS, TTFT, ITL, GPU/VRAM util, per-user/project/model token tracking, AWS cost params). Source: Infarm OPEX.xlsx, Inference Farm - Business Plan.xlsx, Metrics.docx."
practice_area: cps-inference-farm
type: business-reference
audience: internal-business-engineering
provenance: "Extracted by Forge on 2026-05-29 from: Infarm OPEX.xlsx (modified 2026-05-28, FX as of 5/28/2026), Inference Farm - Business Plan.xlsx (2025-08-28) ≈ LLM_model_right_sizing.xlsx, Metrics.docx (cloudguild, 2025-07-29, Hungarian)."
id: 75fb7509-215d-413c-9bd9-c4554a2025d9
index_schema_version: 1
bdos_index: false
---

# Business Model, OPEX & Pricing

> Sources: `Infarm OPEX.xlsx`, `Inference Farm - Business Plan.xlsx`, `Metrics.docx`. See [00_SOURCE_INDEX.md](00_SOURCE_INDEX.md).

## Monthly OPEX — fixed costs

Source: `Infarm OPEX.xlsx` (last updated 5/28/2026). FX used: 1 USD = 303.73 HUF, 1 EUR = 354.18 HUF, 1 USD = 0.8576 EUR.

| Item | Amount | EUR | Note |
|---|---|---|---|
| CPS Support | €2,000.00 | €2,000.00 | |
| AWS cost | ~$500/mo | €428.78 | ~500 USD/mo rounded |
| Lenovo server hosting | $100/mo + 1,500 Ft | €89.99 | 100 USD/mo + 1500 Ft / 10kW |
| Consumption (power) | 100,000 Ft | €282.34 | range 50k–150k Ft, midpoint 100k |
| **Total monthly** | **101,500 Ft + above** | **€2,801.11** | Monthly total in EUR |

## Service tiers (LLMaaS pricing model)

Source: `Inference Farm - Business Plan.xlsx`. All tiers run **Qwen3-32B 4-bit on `g5.12xlarge`** (96 GB VRAM, max ~1200 TPS).

| Tier | Schedule | Environment | TPS min | TPM max (tokens/mo) | Clients max |
|---|---|---|---|---|---|
| Tier A | 24/7 | Dedicated | 1200 | 500,000,000 | 1 |
| Tier B | 5/8 | Dedicated | 1200 | 100,000,000 | 1 |
| Tier C | 5/8 | Shared | 600 | 100,000,000 | 2 |
| Tier D | 5/8 | Shared | 60 | 20,000,000 | 20 |

### Per-tier economics

| Tier | VM util | Cost/month | Cost/client | Subscription/mo | Margin | Subs revenue |
|---|---|---|---|---|---|---|
| A | 100% | $1,347.67 | $1,013.07 | $1,500.00 | 48% | $1,500.00 |
| B | 24% | $167.30 | $167.30 | $300.00 | 79% | $300.00 |
| C | 24% | $167.30 | $83.65 | $150.00 | 79% | $300.00 (2 clients) |
| D | 24% | $167.30 | $8.36 | $50.00 | 498% | $1,000.00 (20 clients) |

> Shared tiers (C/D) amortize one VM across many clients → far higher margins. Tier D (20 clients × $50) yields the best margin profile; Tier A dedicated is the lowest margin but highest per-client revenue.

## Instance cost simulation (on-demand vs spot)

Source: `Inference Farm - Business Plan.xlsx` / `LLM_model_right_sizing.xlsx`. Based on HuggingFace "Llama 2 on SageMaker" benchmark. 160 operating hours/month assumed.

**`g5.2xlarge` (24 GB VRAM, on-demand $1.212/h, spot $0.509/h, ~71 TPS, ~41M tokens/mo):**

| Mix | Monthly cost | $/1M tokens |
|---|---|---|
| 100% On-Demand | $193.92 | ≈ $4.72 |
| 50/50 | $137.68 | ≈ $3.30 |
| 80/20 (spot-heavy) | $103.94 | ≈ $2.65 |
| 100% Spot | $81.44 | $1.99 |

**`g5.12xlarge` (96 GB VRAM, on-demand $6.3317/h, spot $2.4515/h, ~1214 TPS, ~699M tokens/mo):**

| Mix | Monthly cost | $/1M tokens |
|---|---|---|
| 100% On-Demand | $1,013.07 | $1.45 |
| 50/50 | $702.66 | $1.01 |
| 80/20 (spot-heavy) | $516.41 | $0.74 |
| 100% Spot | $392.24 | $0.56 |

> The larger `g5.12xlarge` is dramatically more cost-efficient per token ($0.56–$1.45 vs $1.99–$4.72). Spot cuts cost ~60% but spot interruptions (2-min warning) require handling: ASG spot-only + interruption handling + automatic restart (e.g. Lambda / Step Functions). Capacity not guaranteed; possible startup latency.

## Token-based pricing measurement parameters

Source: `Metrics.docx` (DevOps team brief, Hungarian original). Parameters that must be measured continuously to drive token-based pricing, quota tuning, and business decisions.

**1. LLM inference performance & resource use (GPU level):**
Output TPS, TTFT, inter-token latency (ITL), prompt-processing speed, GPU utilization (%), GPU/VRAM (KV cache) utilization, average batch size, context window length.

**2. Token tracking & usage (application level):**
Input tokens/request, output tokens/request, User ID, Project ID, Model ID (e.g. Qwen-32B, DeepSeek), request timestamp, request status (2xx billable vs 4xx/5xx), total request/input-token/output-token counts per user/project/model.

**3. Infrastructure cost params (AWS level):**
EC2 runtime hours (G5.12XL), S3 storage GB, S3 request counts, data transfer out (GB), cross-AZ transfer (GB), API Gateway request count, other AWS service costs (CloudWatch, Load Balancer).

**DevOps notes:**
- Use the **same tokenizer** for counting as the model (Qwen-32B / DeepSeek) — inaccurate tokenization → wrong billing.
- Log to a scalable store (DynamoDB / PostgreSQL) supporting per-user / per-project aggregation.
- Real-time dashboards (CloudWatch / Grafana) for TPS, TTFT, GPU utilization.
- AWS cost allocation tags to map infra cost to projects/services.
- Alerts on quota approach/breach and performance anomalies.

## Headline business numbers (from the plan)

- **40–60% cost savings** vs public APIs (e.g. $0.005/token internal vs $0.01+ public). *(Note: the website copy doc flags this "40–60% cheaper" claim as needing review/update — see open items.)*
- Target gross margin **50–60%+**.
- POC budget **~$500/month**; MVP investment ~$5–10K; payback 3–6 months.
- Public APIs run **20–30% higher** cost than in-house at scale.

## Cost vs AWS Bedrock (measured, 2026-05-29)

Computed in the dashboard cost calculator ([stats/dashboard.html](../stats/dashboard.html) → Költségkalkulátor) from the real usage: **92 users · 44 days · 4.16B tokens · ~97% input / 3% output**, against OPEX €2,801.11/mo.

**Our self-hosted cost at this volume: ≈ €0.99 / 1M tokens (≈ 350 Ft).** Period cost €4,108 (1.46 mo); €30.45 / user / month.

Same token volume on AWS Bedrock (on-demand, us-east-1, May 2026 rates):

| Option | €/1M token | Period € | vs ours | Tier |
|---|---|---|---|---|
| **Inference Farm (Qwen3.5-397B, private)** | **€0.99** | €4,108 | **1.0×** | frontier, private |
| Claude Sonnet 4.5 ($3/$15) | €2.91 | €12,121 | **2.95× dearer** | frontier (comparable quality) |
| DeepSeek-R1 ($1.35/$5.40) | €1.27 | €5,296 | **1.29× dearer** | open frontier |
| Amazon Nova Pro ($0.80/$3.20) | €0.75 | €3,138 | 0.76× (cheaper) | mid-tier |
| Llama 3.3 70B ($0.72/$0.72) | €0.62 | €2,570 | 0.63× (cheaper) | open 70B |
| Amazon Nova Micro ($0.035/$0.14) | €0.03 | €137 | 0.03× (cheaper) | tiny |

**Read:** at this volume the fixed OPEX is amortized to ~€0.99/1M, so the farm **beats every frontier-class hosted option** (Claude ~3×, DeepSeek-R1 ~1.3×) while keeping data fully private — that is the real value story. Against *small* models (Llama 70B, Nova Pro, Nova Micro) Bedrock is cheaper, but those are far weaker than a 397B MoE. **Caveat on the legacy "40-60% cheaper than OpenAI" claim:** true vs frontier APIs at high volume; NOT true vs small hosted models, and the fixed-OPEX economics only work at scale (low volume → high €/1M). Quote it as "frontier-class quality at mid-tier model prices, fully private."

## Related

- Underlying benchmarks/cost data → [03_benchmarks-model-sizing.md](03_benchmarks-model-sizing.md)
- Full strategy & roadmap → [05_strategy-requirements.md](05_strategy-requirements.md)
- Customer-facing platform description → [../proposals/01-sonrisa-llmaas-platform-description.md](../proposals/01-sonrisa-llmaas-platform-description.md)
