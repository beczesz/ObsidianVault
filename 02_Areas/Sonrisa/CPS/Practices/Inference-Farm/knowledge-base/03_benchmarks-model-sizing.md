---
title: "Inference Farm — Benchmarks, Instance Costs & Model Sizing"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "Consolidated 2025 benchmark + sizing knowledge for the Inference Farm: vLLM throughput/latency benchmarks (TTFT, TPOT, ITL) for Qwen3-14B / QwQ-32B / Qwen3-32B / Qwen3-Coder-480B across AWS G5/G6/G6e/P3/G4dn and Scaleway/Lambda/Runpod instances with EU on-demand pricing; per-model machine requirements; the 20-dimension open-source model scoring matrix; model right-sizing rules of thumb (Qwen3-32B AWQ 4-bit, 2×48GB cards); and the LLMaaS load-test design (Locust, scenarios, thresholds). Source: vllm_benchmark_overview_upd.docx, OpenSource Model Comparison.xlsx, AWS farm main goals.odt, Benchmark.docx, LLM_model_right_sizing.xlsx."
practice_area: cps-inference-farm
type: benchmark-reference
audience: internal-engineering
provenance: "Extracted by Forge on 2026-05-29 from: vllm_benchmark_overview_upd.docx (Ceclan, 2025-09-16), OpenSource Model Comparison.xlsx (2025-09-05), AWS farm main goals.odt (2025-08-22), Benchmark.docx (2025-08-06), LLM_model_right_sizing.xlsx (2025-06-27), vLLM benchmark.xlsx v4 (Bakonyi). Numbers are 2025-era, smaller models — predate the Qwen3.5-397B production case study."
id: 464c6177-3644-42c6-939f-9525f52e5ca7
index_schema_version: 1
bdos_index: false
---

# Benchmarks, Instance Costs & Model Sizing

> **Era note:** this is 2025 benchmark/sizing work on smaller models (Qwen3-14B/32B, QwQ-32B, 480B-Coder). The current production deployment runs Qwen3.5-397B-NVFP4 — see [02_performance-case-study.md](02_performance-case-study.md). Kept for cost-model and sizing reasoning.

## vLLM benchmark + cost summary (September 2025)

Source: `vllm_benchmark_overview_upd.docx` (summary of `vLLM benchmark.xlsx` v4). Benchmarks evaluate throughput, latency (TTFT, TPOT, ITL) and scalability under stepped RPS for Qwen models on AWS GPU instances, focused on EU regions (eu-central-1 / Frankfurt; Scaleway Paris/AMS). Specs ~90% aligned with AWS official + Vantage pricing (Sept 2025).

### Key observations

- Smaller models (14B) scale efficiently to high RPS on mid-tier instances (`g5.12xlarge`, `g6.12xlarge`, ~$6–7/h).
- Larger models (32B, 480B) need more VRAM and show latency-throughput trade-offs.
- Quantized models (AWQ 4-bit) cut VRAM but increase latency, limiting real-time use.
- `g5.12xlarge`, `g6.12xlarge`, `p3.8xlarge`, `g4dn.12xlarge` are cost-effective alternatives to high-VRAM `g6e` for the 65–96 GB VRAM range.
- Scaleway competitive in EU: A100 ~$2.70/h, L40S ~$3.00/h.
- AWS prices reflect ~25% EU premium over US base, after a 45% GPU price cut in June 2025.

### Highlighted model benchmarks (1024 in / 128 out tokens, 300 prompts)

**QwQ-32B on `g6e.12xlarge`** (192 GB VRAM, 4× L40S; min VRAM 59.58 GB): efficient for moderate loads, TTFT <100 ms at low RPS. Peaks ~8.9 req/s (~1090 tok/s) at 50 RPS, but TTFT spikes ~2.2 s at max load. Cost ~$10.49/h on-demand (~$7,561/mo 24/7); reserved 1y ~$6.15/h.

| RPS | Throughput (req/s) | Output tok/s | Mean TTFT (ms) | Mean TPOT (ms) | P99 ITL (ms) |
|---|---|---|---|---|---|
| 1 | 0.99 | 121 | 71 | 34 | 46 |
| 10 | 7.39 | 903 | 180 | 109 | 156 |
| 50 | 8.92 | 1090 | 2189 | 178 | 386 |

**Qwen3-32B on `g6.12xlarge`** (96 GB VRAM, 1× L40S; min VRAM 59.58 GB): saturates ~1.07 req/s around 2 RPS (~130 tok/s); TTFT viable (<1.5 s) up to 1 RPS but queues heavily beyond → >54 s delays at 2+ RPS due to VRAM limits on 96 GB. Suits low-concurrency, cost-sensitive work. Cost ~$6.32/h (~$4,553/mo 24/7); reserved 1y ~$3.75/h.

**Qwen3-Coder-480B-A35B-Instruct on 3× `g6e.48xlarge`** (1152 GB total VRAM, 24× L40S; min VRAM 892.62 GB): excels at low-load coding (TTFT ~99 ms at 2 RPS) but degrades >3 RPS. Cost ~$90.39/h on-demand (~$65,081/mo 24/7); reserved 1y ~$58k/mo.

### Affordable baselines (Qwen3-14B, ~68 ms TTFT / ~37 ms TPOT at 4 RPS)

| Instance | VRAM | $/h (on-demand) | Notes |
|---|---|---|---|
| AWS `g5.12xlarge` | 96 GB | $7.09 | Affordable baseline |
| AWS `g6.12xlarge` | 96 GB | $6.32 | Slightly cheaper than g5, similar perf |
| AWS `p3.8xlarge` | 64 GB | $14.61 | Higher cost; training-heavy |
| AWS `g4dn.12xlarge` | 64 GB | $4.51 | Cheapest AWS; ~10–20% higher latency |
| Lambda Labs GH200 | 96 GB | $1.49 | ~2× better cost-efficiency than AWS |
| Runpod A100 | 80 GB | $1.64 | Secure Cloud |
| Vultr A100 | 80 GB | $2.99 | |
| Scaleway 1× A100 | 80 GB | $2.70 | Paris/AMS, EU-optimized |
| Scaleway 1× L40S | 96 GB | $3.00 | Paris/AMS |

**Less-trusted (reliability concerns):** vast.ai GH200 96 GB ~$6.50/h (unverified EU); LeaderGPU 6× T4 96 GB ~$1.37/h (NL, monthly ≈€985/mo); Hyperstack RTX A6000 48 GB ~$0.50/h (unverified). Use with caution for production.

Ultra-cheap-but-slow: QwQ-32B-AWQ (4-bit, 18 GB) on `g6.xlarge` (24 GB, ~$1.80/h) → at 0.5 RPS only 0.22 req/s, 28 tok/s, TTFT ~369 s (not real-time viable).

## Per-model machine requirements (AWS)

Source: `AWS farm main goals.odt`. Original operating goal: run models **5 days/week, 8h/day = 40h/week**, cost-effectively, evaluating AWS / GCP / Azure, with a no-downtime guarantee for customers.

| Model | Params | AWS instance | Memory | Notes |
|---|---|---|---|---|
| QwQ-32B | 32.5B (64 layers, GQA 40Q/8KV) | `g6e.12xlarge` | 384 GiB, 48 vCPU, 100 Gb net | Causal LM, RoPE/SwiGLU/RMSNorm |
| Qwen3-14B | 14.8B (40 layers) | `g5.12xlarge` | 192 GiB, 48 vCPU, 40 Gb net | 32k native ctx, 131k with YaRN |
| gemma-3-1b-it | ~1B | `g4dn.xlarge` | 16 GiB, 4 vCPU, up to 25 Gb net | Small/cheap |

## Model right-sizing rules of thumb

Source: `LLM_model_right_sizing.xlsx` + engineering notes.

- Qwen 2.5 72B is obsolete — current **Qwen3-32B** does the same and there is no 72B in the series.
- Best to host with **vLLM + AWQ 4-bit quantization** → ~⅓ the memory (~5–8% quality loss vs unquantized).
- Context length significantly drives memory use.
- Kodesage recommended: 3× L40/L40s (48 GB cards); 2× ran 72B Qwen AWQ at 128k context fine, 3rd card for the embedder. **Rule of thumb: 2× 48 GB cards is enough for very good performance.**
- Trend: smaller models (30–40B) are getting stronger.

## Open-source model scoring matrix (20 dimensions)

Source: `OpenSource Model Comparison.xlsx`. Scores models per use case (Coding Assistant / Chat UI / API Integration) across 4 dimension groups; weighted impact 1 (minimal) → 5 (critical).

**Dimension groups:**
- **A. Model capabilities** — multilingual, coding, reasoning, instruction-following, RAG-friendliness, multimodal.
- **B. Performance & deployment** — context window, model size, VRAM footprint, quantization quality, inference speed, cold-start time.
- **C. Engineering & integration** — vLLM compatibility, fine-tuning (LoRA/QLoRA/PEFT), RAG integration (LangChain/LlamaIndex), streaming, prompt-format standard.
- **D. License & ecosystem** — license type, community/tooling, benchmark transparency.

**Use-case weighted totals (higher = more demanding profile):** Coding Assistant 54, Chat UI 52, API Integration 48. (e.g. coding weights coding-performance/reasoning at 5; chat weights instruction-following/streaming/inference-speed at 5; API weights VRAM/quantization/inference-speed/cold-start at 5.)

**Model families evaluated:** Qwen 3 (0.6B → 235B MoE), Qwen 2.5 Coder (1.5B → 32B), Qwen Math, Qwen VL, DeepSeek V3 (671B/37B active), DeepSeek Coder V2 (16B → 236B), DeepSeek R1 (Lite/Full/Zero), LLaMA 3.1/3.2/3.3 (1B → 405B, incl. Vision), Gemma 3 (1B → 27B, incl. Vision).

## LLMaaS load-test design

Source: `Benchmark.docx`. Goal: simulate real traffic, find bottlenecks (a 3000 ms TTFT was the trigger concern), validate optimizations.

- **Environment:** vLLM on EC2 NVIDIA GPUs (g5.12xlarge 4× A10G, or inf2.48xlarge Inferentia2 for cost). Docker via ECR, OpenAI-compatible endpoint. Baseline optimizations: PagedAttention, AWQ 4-bit, tensor parallelism.
- **Tools:** Locust (primary), alternatives k6 / JMeter; run on separate EC2/Fargate. Monitoring: CloudWatch, X-Ray, Prometheus/Grafana.
- **Scenarios:** baseline (1–10 users) → ramp-up (10→100 over 5–10 min) → spike (200 instant) → endurance (50 users, 1–2h); mixed prompt types (70% short / 30% long); 3–5 iterations each, 5–15 min/run.
- **Metrics:** TTFT, TPOT/ITL, TPS, E2EL, throughput (RPS); GPU/CPU util, VRAM, network I/O, queue depth; error rate, P99 latency; cost per 1M tokens.

**Target thresholds (2025 competitive LLMaaS):**

| Metric | Target |
|---|---|
| TTFT | <200–500 ms (interactive); <2 s (batch) |
| TPOT/ITL | <30–200 ms/token |
| TPS | >50–100 per instance; >20–50 per user |
| E2EL / P99 | <1–2 s median; P99 <2–5 s |
| Throughput (RPS) | >10–50 per instance |
| Error rate | <1% |
| GPU/CPU util | 70–90% (avoid >95% or <50%) |
| Memory | <80% VRAM |
| Cost / 1M tokens | <$0.2–0.5 |
| Uptime | >99.9% |

## Related

- Cost model + pricing tiers built on these numbers → [04_business-model-pricing.md](04_business-model-pricing.md)
- Production performance (current) → [02_performance-case-study.md](02_performance-case-study.md)
- Deeper model survey (Aug 2025, 14 families) → [../research/01-open-source-models-survey-2025-08.md](../research/01-open-source-models-survey-2025-08.md)
