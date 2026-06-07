---
title: "Inference Farm — Production Performance Case Study (Qwen3.5-397B-NVFP4)"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "Distilled production performance case study of the AWS Inference Farm running nvidia/Qwen3.5-397B-A17B-NVFP4 on a 4-GPU vLLM deployment, observation period 29 April – 27 May 2025. Covers throughput (79 tok/s avg, 905 tok/s peak), prefix cache efficiency (70% avg, 94.7% max), KV cache headroom (2.4% used → 10-15x scale room), GPU telemetry (power, temperature, SM utilization), energy profile, the performance scorecard, and sales positioning (frontier-class quality on 4 GPUs via NVFP4). Source: InFarm_CaseStudy.docx (Sales-confidential)."
practice_area: cps-inference-farm
type: case-study
audience: internal-engineering-sales
provenance: "Extracted by Forge from CloudPlatformServices-Inferencefarm/AwsInFarm/InFarm_CaseStudy.docx (Confidential – Sales Use Only), modified 2026-05-27, on 2026-05-29. Underlying data: 139,263 vLLM engine log entries + 430 nvidia-smi dmon samples."
id: 0b64dd28-dd6a-440b-999b-4fef2429f382
index_schema_version: 1
bdos_index: false
---

# Production Performance Case Study — Qwen3.5-397B-NVFP4

> **Confidential — Sales Use Only.** Source: `InFarm_CaseStudy.docx`. Observation period **29 April – 27 May 2025** (28 continuous days production traffic) + a 3-hour GPU telemetry window during peak hours (13:00–16:00 EEST, 27 May 2025).

## Executive summary

Real-world inference performance of a **4-GPU production deployment** running `nvidia/Qwen3.5-397B-A17B-NVFP4` via vLLM.

- Sustained generation throughput **79 tok/s average**, up to **905 tok/s** at peak bursts.
- **78%** of sampled time the server was actively serving inference.
- Prefix cache hit rate **70% average**, reaching **94.7%** — sharply reducing compute load.
- GPU SM utilization **P50 = 98%** during active inference — compute fully utilized when busy.
- KV cache headroom: average only **2.4% used** — capacity for much higher concurrency.
- Thermal headroom maintained: avg **74°C** active, max **88°C** — within safe range.

## Setup configuration

| Parameter | Value |
|---|---|
| Model | `nvidia/Qwen3.5-397B-A17B-NVFP4` |
| Architecture | Mixture of Experts (MoE) — 397B total / ~17B active params per token |
| Quantization | NVFP4 (weights) + FP8 KV cache |
| Inference engine | vLLM v0.19.2 (Async V1 Engine) |
| GPU configuration | 4× GPU — Tensor Parallel (TP=4) + Expert Parallel (EP=4) |
| GPU VRAM used | ~89 GB per GPU (weights + KV cache + CUDA graphs) |
| Max context length | 131,072 tokens (128k) |
| Max concurrent requests | 32 (`max_num_seqs`) |
| Max batched tokens | 32,768 per step (chunked prefill enabled) |
| Prefix caching | Enabled (Mamba align mode) |
| Attention backend | FlashInfer (FP8 attention) |
| Expert routing | 512 experts total / 128 per GPU (linear placement) |

## Throughput (28-day analysis)

Derived from 139,263 vLLM engine log entries. "Active" = windows where generation throughput > 0.

| Metric | Average | Peak | P50 | P95 |
|---|---|---|---|---|
| Generation throughput | 79.4 tok/s | 905.3 tok/s | 71.8 tok/s | 195.0 tok/s |
| Prompt throughput | 846 tok/s | 19,281 tok/s | 209 tok/s | 5,113 tok/s |

Prompt throughput benefits heavily from the prefix cache (cached prefixes need no recomputation → burst up to ~19,280 tok/s on high cache-hit scenarios).

## Cache efficiency

**Prefix (KV) cache hit rate:** average 69.7%, P50 79.1%, max 94.7%. Most incoming prompts reuse previously computed attention keys/values → lower latency, higher effective throughput.

**GPU KV cache memory:** average utilization **2.42%**, P95 6.9%, max 45.9% → **headroom for 10–15× more load**.

## Concurrency & capacity

Configured for up to 32 simultaneous requests. During the period, **average active concurrency = 1.17 requests** (max observed 32).

> **Key insight:** the server is currently underloaded. KV cache headroom (2.4% avg) suggests it can serve **5–10× more concurrent users** before memory pressure — significant traffic growth absorbed with no hardware change.

## GPU telemetry — peak hours (3h window, 430 samples)

All 4 GPUs ran in parallel (tensor + expert parallel). Aggressive power-gating: clock drops to **405 MHz (~15–17 W/GPU)** when idle, ramps to **13,365 MHz (~160–288 W/GPU)** within ms of a new request.

**Power (W):**

| | GPU 0 | GPU 1 | GPU 2 | GPU 3 |
|---|---|---|---|---|
| Avg (all) | 100 | 89 | 89 | 87 |
| Avg (active) | 162 | 146 | 149 | 146 |
| Avg (idle) | 17 | 15 | 11 | 9 |
| Max | 287 | 264 | 272 | 269 |

**Temperature (°C):**

| | GPU 0 | GPU 1 | GPU 2 | GPU 3 |
|---|---|---|---|---|
| Avg (active) | 67.0 | 62.2 | 64.4 | 59.1 |
| Max observed | 86 | 83 | 85 | 80 |

**Energy profile:**

| State | 4-GPU total power | Notes |
|---|---|---|
| Active (inference) | 718 W avg / 1,153 W peak | mclk = 13,365 MHz |
| Idle (no requests) | ~62 W avg | mclk = 405 MHz, power-gated |
| Est. 3h consumption | ~1.78 kWh | 78% active duty cycle |
| PCIe transfer (3h) | ~58 GB RX + ~60 GB TX | tensor-parallel communication |

## What this setup equates to

Despite 397B total params, each forward pass activates only ~17B → inference speed comparable to a **dense 70B model**, but with higher quality/reasoning.

| Dimension | Positioning |
|---|---|
| Model quality tier | Equivalent to GPT-4-class frontier models (397B MoE, chain-of-thought, Qwen3 series) |
| Speed vs dense | 79 tok/s avg ≈ dense 70B at similar batch sizes, with superior output quality |
| Context window | 128k tokens — long docs, multi-turn, large codebases |
| Concurrent users | Up to 32; current avg 1.17 → large scale room without hardware upgrade |
| Cost efficiency | NVFP4 reduces memory ~50% vs BF16 → 397B on 4× GPU instead of 8× |
| Prefix caching impact | ~70% hit rate → ~70% of prompt tokens served instantly → ~3× throughput vs no-cache |

## Performance scorecard

| Metric | Value | Rating | Notes |
|---|---|---|---|
| Generation throughput (avg) | 79.4 tok/s | ★★★★☆ | Good for 397B MoE |
| Generation throughput (peak) | 905 tok/s | ★★★★★ | Excellent burst capacity |
| Prefix cache efficiency | 69.7% avg | ★★★★★ | Very high — ~3× compute reduction |
| KV cache headroom | 2.4% used | ★★★★★ | Massive room to scale |
| GPU compute utilization | 98% P50 (active) | ★★★★★ | Fully utilized when busy |
| GPU thermal safety | avg 74°C, max 88°C | ★★★★☆ | Good headroom, monitor peaks |
| Energy efficiency | 15 W idle / 180 W active | ★★★★★ | Excellent power-gating |
| Concurrency capacity | 32 req, avg 1.17 | ★★★☆☆ | Underloaded — room to grow |

## Recommendations

- **Scale-up:** KV cache only 2.4% used → 10–15× more concurrent users at current context length before more GPU memory needed. With avg concurrency 1.17 vs limit 32, add load balancing / more clients immediately, no infra change. Consider continuous-batching tuning beyond `max_num_seqs=32`.
- **Monitoring:** GPU temps peak 86–88°C at load → alert above 85°C. PCIe during active inference avg 2.5 GB/s, peak 18 GB/s — current headroom sufficient.
- **Sales positioning:** Qwen3.5-397B (frontier-equivalent quality) runs fully on-prem / private cloud; NVFP4 enables a 400B+ model on 4 GPUs vs 8+ for naive BF16; 128k context + 32 concurrent users → enterprise workloads (document Q&A, code generation, agentic pipelines).

## Related

- Live dashboards: `vllm_dashboard.html`, `gpu_dashboard3.html` on the canonical site (linked in [00_SOURCE_INDEX.md](00_SOURCE_INDEX.md))
- Architecture → [01_architecture-infrastructure.md](01_architecture-infrastructure.md)
- Earlier (2025) benchmarks on smaller models → [03_benchmarks-model-sizing.md](03_benchmarks-model-sizing.md)
