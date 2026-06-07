---
type: practice
id: 4a9f7c3e-b528-4d61-9e84-1c6f0a3b7d52
practice: "Inference Farm"
unit: "Sonrisa/CPS"
unit_display: "Cloud Platform Services"
unit_short: "CPS"
slug: cps-inference-farm
owner: "Becze Szabolcs (CPS lead) + Ceclan Sanyi (technical lead)"
status: active
maturity_stage: maturing
description: "CPS practice area for private LLM inference infrastructure as managed service. Productized as Sonrisa LLMaaS — LIVE in production on AWS (account 382113323075, ~$863/mo as of 2026-05) with OpenAI-compatible API + web interface + token-based packages (€500–5,000/mo). Pillar 1 of the broader CPS AI-Native Operating System strategic direction (the 'kernel' on which Pillars 2-3 — Agentic AIOps + FinOps Automation — depend). Internal usage stable, external client motion underway: Merkantil banking AID deployment is the first paying external engagement, Discovery 2026-05-27."

# Productization fields
service_brand: "Sonrisa LLMaaS"
aws_account: "382113323075 (CPS - Infarm)"
aws_monthly_spend_usd: 863
live_url_planned: "sonrisa.io/llmaas"
stack:
  compute: "AWS EC2 G5.12XL (GPU)"
  model_serving: "vLLM (PagedAttention)"
  models: ["Qwen-32B", "DeepSeek Coder", "Llama 3.1", "custom fine-tuned"]
  api: "OpenAI-compatible REST"
  ui: "OpenUI web interface"
  region: "EU-West (data residency)"
service_packages:
  starter:      { eur_month: 500,   tokens_m: 10,   support: "business-hours" }
  professional: { eur_month: 2000,  tokens_m: 50,   support: "8/5 response" }
  enterprise:   { eur_month: 5000,  tokens_m: 150,  support: "24/7 SLA" }
  dedicated:    { eur_month: null,  tokens_m: null, support: "premium, custom" }
overage_eur_per_1k_tokens: 0.004

# At-a-glance (Forge dashboard card — kept in sync by Forge)
strategic_directions:
  - "Pillar 1 of CPS AI-Native OS — the private inference substrate that Pillars 2-3 (Agentic AIOps + FinOps Automation) depend on"
  - "LIVE PRODUCT on AWS — Sonrisa LLMaaS (acct 382113323075, ~$863/mo, vLLM + Qwen/DeepSeek/Llama)"
  - "First external client motion: Merkantil banking AID deployment in flight (Discovery 2026-05-27)"
next_step: "Send AID infra deployment pricing to Miklós Nándor by EOD (post Merkantil Discovery call output)"
deadline: 2026-05-27
blocker: "Awaiting Merkantil post-call logs and design patterns from user"
top_todos:
  - "Finalize sizing baseline for 20-50 concurrent AID users on Merkantil banking workload"
  - "Decide AWS-native (existing LLMaaS) vs new-deployment-per-client tier model for external sales"
  - "Resolve strategic Q: substrate sold standalone vs bundled into AI-Native OS (parent strategy open Q)"

tags: [practice, cps, inference, llm-ops, aws, gpu, banking-grade, regulated, llmaas, ai-native-os-pillar-1, live-production]
created: 2025-08
last_signal: 2026-05-27
related_engagements:
  - merkantil
  - mvmi
  - cchbc-tender
related_practices:
  - "CPS Agentic AIOps (Pillar 2 of AI-Native OS, consumes this substrate)"
  - "CPS FinOps / Cost Optimization (Pillar 3 of AI-Native OS)"
counts:
  open_questions: 20
  related_engagements: 3
  learnings_active: 0
  learnings_proposed: 0
bdos_index: false
index_schema_version: 1
---

# Inference Farm — CPS Practice Area

> **Status 2026-05-27:** `active` / `maturing`. **LIVE PRODUCT** on AWS as **Sonrisa LLMaaS** (account 382113323075, ~$863/mo). Internal usage stable. **Pillar 1 of the CPS AI-Native OS strategic direction.** First external paying-client motion: Merkantil banking AID deployment in Discovery (call 2026-05-27 12:00).

> 📚 **Knowledge base (2026-05-29):** All Inference Farm knowledge from Sonrisa SharePoint has been consolidated and organized into [[knowledge-base/00_SOURCE_INDEX|knowledge-base/]] — architecture & IaC, the Qwen3.5-397B production case study, benchmarks & model sizing, business model & pricing, strategy & requirements, and Q1 2026 usage stats. Start at [[knowledge-base/00_SOURCE_INDEX|00_SOURCE_INDEX.md]] for the full source catalog with SharePoint links.

## Mission

Operate **private LLM inference infrastructure** as a productized managed service for clients who cannot or will not use public LLM endpoints. Primary sectors: banking, healthcare, gov, regulated EU enterprises. Already productized as **Sonrisa LLMaaS** — OpenAI-compatible API + web UI + multi-model serving (Qwen-32B / DeepSeek / Llama) on AWS GPU substrate.

A practice értelme: amikor egy ügyfél azt mondja "kell egy LLM infra de nem mehet publikus felhőbe", CPS ne null-ról árazzon — **az LLMaaS már él és produkcióban van**, csak az ügyfél-specifikus deployment + sizing + onboarding szállítást végezzük.

## Scope

**In scope:**
- Sonrisa LLMaaS productized service (Starter / Professional / Enterprise / Dedicated packages)
- GPU/CPU compute sizing for client-specific LLM workloads
- Model serving stack — **vLLM** with PagedAttention (live)
- Kubernetes / container orchestration for inference workloads
- Observability (Prometheus, Grafana, log shipping, GPU utilization)
- CI/CD for model + skill deployment
- Security hardening for banking-grade compliance (ISO 27001 ready, SOC2 alignment design-target)
- 24/7 on-call rotation for Enterprise tier customers
- FinOps for GPU cost optimization
- Custom fine-tuning (LoRA / QLoRA) for client-specific domains

**Out of scope:**
- Model pre-training from scratch (CPS-nek nincs ilyen capability-je)
- Agent framework development (AID team owns)
- Application-layer products that consume the substrate (KodeSage, Hermes/OpenClaw orchestration — separate units)
- Pure public-cloud-API resale (Azure OpenAI / Bedrock standalone — that would be a different "Cloud-Native AI Services" practice)

## Productization status

**Live: Sonrisa LLMaaS.** Full service description in [[proposals/01-sonrisa-llmaas-platform-description|proposals/01-sonrisa-llmaas-platform-description.md]]. AWS partner positioning in [[proposals/02-aws-ace-opportunity-summary|proposals/02-aws-ace-opportunity-summary.md]].

**Current pricing (productized):**

| Package | EUR/month | Tokens | Support |
|---|---|---|---|
| Starter | €500 | 10M | Business hours |
| Professional | €2,000 | 50M | 8/5 response |
| Enterprise | €5,000 | 150M | 24/7 SLA |
| Dedicated | Custom | Unlimited | Premium |

Overage: €0.004/1K tokens (40-60% cheaper than OpenAI equivalent).

**Reference architecture (production, AWS):**

| Layer | Component | Status |
|---|---|---|
| Compute | AWS EC2 G5.12XL GPU instances | ✅ Live |
| Model serving | vLLM (PagedAttention backend) | ✅ Live |
| Models | Qwen-32B (coding), DeepSeek Coder (docs), Llama 3.1 (general) | ✅ Live |
| API | OpenAI-compatible REST + streaming | ✅ Live |
| UI | OpenUI web interface | ✅ Live |
| Auth | API keys, RBAC, SSO/SAML (Enterprise) | ✅ Live |
| Observability | CloudWatch + Prometheus + Grafana | ✅ Live |
| Network | AWS VPC, ELB, optional VPC peering | ✅ Live |
| Region | EU-West (data residency) | ✅ Live |
| Token metering | Per-user / per-project quotas + billing reports | ✅ Live |
| Audit logging | Full request/response logging | ✅ Live |

**Internal usage:** stable. **External pilots:** target 3-5 in 2026. **Merkantil:** first paying external engagement underway (Discovery call 2026-05-27).

## Strategic positioning

**Pillar 1 of CPS AI-Native Operating System.** See [[research/02-strategic-positioning-pillar-1|research/02-strategic-positioning-pillar-1.md]] for the full context.

The Inference Farm is the **"kernel"** of the broader AI-Native OS direction. Pillars 2-3 (Agentic AIOps + FinOps Automation) consume this substrate for their agent inference needs. Without Pillar 1, Pillars 2-3 lose the "private/sovereign" promise.

**Open strategic question** (from parent strategy):
- Substrate go-to-market: **LLMaaS sold standalone, bundled into the OS, or both?**

This shapes how we package Merkantil and future external deals.

## Why this practice area

1. **Already productized + live** — not a research bet, real revenue motion possible
2. **Banking + DORA 2026 pressure** — on-prem inference egyre kötelezőbb regulált szektorokban
3. **Multiple workstreams compatibility** — egy inference farm KIszolgálja AID-et, helpdesk RAG-ot, contract analysis-t, Q&A bot-okat, credit decisioning-et → strategic asset, nem single-use
4. **Pillar 1 of AI-Native OS** — strategic foundation, nem szigetelt szolgáltatás
5. **CPS expertise overlap** — AWS depth (Póda, E9+ Architect), Azure depth (MVMI Azure DevOps), Kubernetes depth (MVMI Omni Support OpenShift)
6. **Cost advantage proven** — 40-60% cheaper than public APIs at equivalent token volumes

## Sub-practice candidates (when evidence diversifies)

Inference Farm later may bifurcate:
- **AWS-native inference** (current default — Sonrisa LLMaaS as-is, multi-tenant shared)
- **Azure-native inference** (Azure OpenAI private endpoint + AKS — when an Azure-locked client requires)
- **Pure on-prem inference** (vLLM/Ollama + bare-metal GPU — when client has data-center constraint)
- **Hybrid** (control plane in Sonrisa-cloud, inference on-prem at client)

Most: egy area, egy NOTES, később felbontható ha az evidence sokféleségben jön. Merkantil engagement formálisan adja a 4. ("hybrid"-jellegű) verziót.

## Materials in this practice area

```
Inference-Farm/
├── NOTES.md                                                  ← ITT (canonical)
├── _inbox/                                                   ← raw dump-ok
├── research/
│   ├── 01-open-source-models-survey-2025-08.md              ← 14-model survey (moved 2026-05-27)
│   └── 02-strategic-positioning-pillar-1.md                 ← Pillar 1 context (extract 2026-05-27)
├── patterns/                                                 ← (üres, 3+ evidence kell)
├── decisions/                                                ← (üres, ADR-jelölt: model-selection, stack-choice)
├── experiments/                                              ← (üres)
├── proposals/
│   ├── 01-sonrisa-llmaas-platform-description.md            ← Full LLMaaS offer (moved 2026-05-27)
│   └── 02-aws-ace-opportunity-summary.md                    ← AWS Partner positioning (moved 2026-05-27)
├── learnings/00_INDEX.md                                    ← Forge structured learnings (üres)
├── related-projects.md                                       ← engagement cross-links
└── open-questions.md                                         ← 20 nyitott kérdés
```

## Folder structure convention

Lásd Forge canonical [`00_Prompts/BDOS/agents/forge.md`](../../../../../00_Prompts/BDOS/agents/forge.md) §5.

## Related engagements

Lásd: [[related-projects]]

## Open questions

Lásd: [[open-questions]] (20 active questions across sizing / stack / banking / integration / packaging / talent / strategic)

## Forge log (append-only)

| Date | Event |
|---|---|
| 2026-05-29 | **Dashboard: cost calculator (saját OPEX vs AWS Bedrock).** Added 4th tab `Költségkalkulátor` to `build_dashboard.py`. Editable inputs (OPEX tételek a `Infarm OPEX.xlsx`-ből: €2801,11/hó; időszak/userek/token/input-arány a statisztikából: 92 user, 44 nap, 4,16 Mrd token, ~97% input). Kimenet **EUR + HUF + €/1M token + €/user/hó**, és Bedrock-összehasonlító tábla + diagram. Bedrock árak szerkeszthetők (`calc.bedrock`). **Eredmény: saját ≈ €0,99/1M token (350 Ft)** — Claude Sonnet 2,95×, DeepSeek-R1 1,29× drágább (frontier-nél olcsóbbak vagyunk); Nova Pro/Llama 70B/Nova Micro olcsóbb (de gyengébb modellek). Üzleti olvasat + a legacy "40-60% cheaper" állítás pontosítása: [[knowledge-base/04_business-model-pricing]]. Verifikálva böngészőben (JS-eval, nincs console error). |
| 2026-05-29 | **Dashboard: electricity cost + time-window filter.** User gave electricity price **1500 Ft / 10 kWh (= 150 Ft/kWh ≈ €0,42/kWh)**. Added to `build_dashboard.py`: (1) per-hour energy model (`active_fraction × 712 W active + idle × 58 W`, GPU power from nvidia_smi, active fraction from vLLM log) → energy + cost in **HUF and EUR**, shown as a cost card (energy kWh, HUF, EUR, daily avg, 30-day projection) on the Server + GPU tabs; (2) a global **Heti / Havi / Teljes** (7d / 30d / all) time-window filter in the header, reload-based, recomputing every tab from raw rows + log series. Full-period ≈ **351 kWh ≈ 52 722 Ft / €148,86** (GPU-only; OPEX power line ~100k Ft incl. full server). Verified in-browser: filter switches correctly (weekly = 75 kWh / 11 221 Ft / €31,68), no console errors. README + [[knowledge-base/07_analytics-telemetry]] updated. |
| 2026-05-29 | **Dashboard: GPU telemetry + token throughput incorporated.** Extended `stats/build_dashboard.py` with an `nvidia-smi dmon` parser and a third top-level tab **"GPU telemetria"** (4-GPU total + per-GPU power, per-GPU temp, SM/mem-BW/PCIe/temp util-over-time with tabs, SM-distribution histogram, KPI strip). Token throughput confirmed present (Server view default "Tokens/s" tab: prompt + generation tok/s + peak KPIs). Pointed `LOG_PATH`/`GPU_PATH` at the in-repo `raw/` copies for reproducible regen. Regenerated `dashboard.html` (302 KB) and **verified in-browser** (no console errors, all GPU charts render): 430 samples, 78.6% duty cycle, 712 W active / 1153 W peak (4-GPU), SM 66% avg / 100% P95, mem-BW 25%, 88°C max, 15 W idle/GPU; SM histogram bimodal (idle vs 81-100%). README + [[knowledge-base/07_analytics-telemetry]] updated. |
| 2026-05-29 | **Capacity analysis (deeper dig).** Ran `stats/capacity_analysis.py` over 139,263 engine samples + 1,720 GPU samples → [[knowledge-base/08_capacity-analysis]]. Verdict: single 4-GPU box serves ~125 users as-is, ~250 after raising `max_num_seqs` (binding limit is the 32-slot cap, not GPU memory/throughput — KV peaks 46%, throughput ~9% of ~900 tok/s ceiling, GPUs idle 22%). TTFT not in production logs (only queue depth); needs a `vllm bench serve` sweep to quantify. |
| 2026-05-29 | **stats/ review + analytics integration.** Reviewed `stats/dashboard.html` (AI-Usage-Analytics: 2 views — OpenWebUI/LiteLLM per-user usage from CSV + vLLM server runtime from logs) and identified every `raw/` artifact: `logs.out` (113 MB / 752,800-line vLLM Docker stdout, container `vllm-qwen35-397b-nvfp4-1`, 2026-04-29→05-27), `nvidia_smi.log` (dmon, 4× GPU, ~450 samples), `infarm.drawio.png` (architecture diagram), generated `vllm_dashboard.html` + `gpu_dashboard2.html`, plus duplicate README/blackwell docs. Added [[knowledge-base/07_analytics-telemetry|knowledge-base/07_analytics-telemetry.md]]. Diagram revealed **hybrid topology** — AWS acct 382113323075 (Infarm VPC: open-webui + litellm ECS, RDS, ECR pull-through, ACM ai.sonrisa.hu) + AWS acct 911406043488 (Sonrisa SYS, Route53) + **on-prem Duna Tower** vLLM hosts (192.168.9.49: MiniMax-M2.1 + qwen3-vl-8b; 192.168.9.190: Qwen3-4B + Qwen2.5-VL-7B + Qwen3-Embedding-0.6B), LiteLLM as unifying gateway — folded into [[knowledge-base/01_architecture-infrastructure]]. Registered the whole knowledge-base in [[learnings/00_INDEX]]. Open for deeper dig: reconcile CSV 4.16B vs Q1 5.77B token figures; characterize 17.9k module errors + 3.7k ASGI exceptions; pin where the 397B physically runs (AWS Blackwell vs on-prem). |
| 2026-05-29 | **SharePoint knowledge consolidation.** Forge swept org-wide Sonrisa SharePoint (Microsoft Graph, 154 raw hits) for strictly-Inference-Farm content and extracted it into a new `knowledge-base/` folder: `00_SOURCE_INDEX.md` (catalog of ~20 source docs + links) plus 6 topic notes (architecture & IaC, Qwen3.5-397B production case study, benchmarks & model sizing, business model & pricing, strategy & requirements, Q1 2026 usage stats). Sources spanned 5 clusters: canonical IF site (`CloudPlatformServices-Inferencefarm/AwsInFarm`), Sales/BD (`sites/sales/.../Business development/Inference Farm`), Cloud Guild Technical, CTO-Office stats, and personal OneDrives (Ceclan, Bakonyi, Becze). Office docs read as text; HTML dashboards / drawio diagram / raw logs linked; OneNote (.one) + Loop (.loop) inaccessible via Graph, linked only. Excluded out-of-strict-scope noise (CTO Pulse, manifestos, AI-policy docs, CVs, timesheets). Surfaced **two-faces-of-IF** distinction: internal AI-adoption farm (`chat.int.sonrisa.hu`, 5.77B tokens Q1 2026) vs commercial CPS LLMaaS (`ai.sonrisa.hu`). Flagged for follow-up: the "40-60% cheaper" cost claim needs review (per website-copy doc), and token-attribution hygiene (449k requests unattributed in Q1 stats). |
| 2026-05-29 | **Legacy folder retired.** Deleted the 4 breadcrumb stubs and the now-empty `02_Areas/Sonrisa/CPS/Services/Inference Farm/` folder (user decision, 2026-05-29). Before deletion, rewired all 7 live inbound references to the new canonical practice paths: `CPS/TASKS.md`, `CPS/01_PROJECT_STATE.md`, `CPS/Marketing/website/llmaas-landing-page-structure.md`, `CPS/Strategy/AI Ops/01_STRATEGY.md`, `CPS/Strategy/AI Ops/aiops.md`, `CPS/Accounts/Leads/CCHBC/brainstorm_cchbc-aiops-tiers.md`, `Sonrisa/00_KNOWLEDGE_MAP.md`. The `provenance:` frontmatter on the migrated files retained as historical record. Migration fully complete: no content remains under `Services/`. |
| 2026-05-27 | **Practice area consolidation (Librarian-assisted).** Forge collected all pre-existing Inference Farm content scattered across the vault and moved it under this practice area. **4 files relocated** from legacy `02_Areas/Sonrisa/CPS/Services/Inference Farm/`: (1) Description.md → `proposals/01-sonrisa-llmaas-platform-description.md`; (2) LLMaaS — ACE Opportunity Summary.md → `proposals/02-aws-ace-opportunity-summary.md`; (3) Open Source Models.md → `research/01-open-source-models-survey-2025-08.md`; (4) Open Source Models - Extended.md → SUPERSEDED (near-duplicate of #3). **1 new extract:** `research/02-strategic-positioning-pillar-1.md` from `02_Areas/Sonrisa/CPS/Strategy/AI Ops/01_STRATEGY.md` (the source-of-truth strategy doc remains at that location — extract is a practice-scoped summary). Breadcrumb files left in the old `Services/Inference Farm/` location pointing to the new paths (legacy wikilink safety). **Maturity reassessment:** `forming/research` → `active/maturing`. Reality is the LLMaaS is LIVE PRODUCT (AWS acct 382113323075, ~$863/mo, productized with 4 service tiers €500-5,000/mo). Was undervalued in the v0.1 NOTES. **Strategic context added:** Pillar 1 of CPS AI-Native OS direction. **Open strategic Q tracked:** substrate go-to-market (standalone vs bundled). Counts: open_questions 20 (no change), related_engagements 2 → 3 (added CCHBC tender as referencing engagement). |
| 2026-05-27 | Practice area létrehozva. Triggered by Merkantil Discovery call 12:00 (CPS plugged in for AID infra deployment sizing). Awaiting Merkantil logs + design pattern dump from user. Reference architecture: Sonrisa-internal AID stack. Initial maturity: `forming` / `research` (later corrected to `active` / `maturing` via the consolidation pass — see entry above). |
