---
title: "Inference Farm — Capacity Analysis (current limit & headroom to 200 users)"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "Data-driven capacity analysis of the production Qwen3.5-397B-NVFP4 server from 139,263 vLLM engine samples (logs.out) + 1,720 nvidia-smi GPU samples. Establishes the current operating point at ~90-100 users (mean concurrency 1.17, peak ~25, queueing 0.12% of time, KV cache mostly <10%, GPUs idle 22% and compute-bound only in bursts), identifies the binding limit (max_num_seqs=32 batch slots, NOT GPU memory or throughput), and projects headroom: ~125 users on current config before peak queueing, ~250-400 users if max_num_seqs is raised (KV/throughput allow it). Notes that production TTFT is not logged and needs a benchmark sweep to quantify."
practice_area: cps-inference-farm
type: capacity-analysis
audience: internal-engineering-business
provenance: "Computed by Forge on 2026-05-29 via stats/capacity_analysis.py over stats/raw/logs.out (139,263 samples, 2026-04-29→05-27) and stats/raw/nvidia_smi.log (1,720 dmon samples). Single 4-GPU replica, vLLM 0.19.2, TP=4, EP, max_num_seqs=32, max_model_len=131072."
id: 572e0b5d-bf1d-4178-abb0-cbb4008b400d
index_schema_version: 1
bdos_index: false
---

# Capacity Analysis — Current Limit & Headroom

> Computed from raw production data via [../stats/capacity_analysis.py](../stats/capacity_analysis.py). Population: **~90–100 distinct users** (92 in the usage CSV). Single 4-GPU replica running Qwen3.5-397B-NVFP4. Window: 2026-04-29 → 05-27, 677 active hours.

## TL;DR

- The current setup is **heavily underutilized** at ~100 users. Average concurrency **1.17**, peak hour rarely above **25** simultaneous requests, KV cache typically **<10%**, queueing happens **0.12%** of the time.
- The **binding limit is `max_num_seqs = 32`** (the vLLM concurrent-request batch slot cap) — a *software setting*, not a hardware wall. GPU memory (KV cache) and token throughput both have large headroom.
- **At 200 users on the current config:** peak-hour demand (~50 concurrent bursts) would exceed the 32 slots → requests queue → TTFT spikes during 1–2 busy hours/day. Off-peak unaffected.
- **Headroom on current config:** ~**125–130 users** before peak hours start hitting the 32-slot wall with today's usage pattern.
- **Headroom with one tuning change** (raise `max_num_seqs` to ~64–128, which KV memory allows): roughly **250–400 users** before GPU compute / aggregate throughput become the real limit.
- **TTFT is not in the production logs** — only queue depth (a proxy). A `vllm bench serve` sweep on the 397B is required to draw a real TTFT-vs-load curve.

## Current operating point (measured)

| Metric | Value | Reading |
|---|---|---|
| Concurrency (Running) | mean 1.17 · P95 4 · P99 8 · max 32 | Almost always near-idle; bursts to a few dozen |
| Saturated samples (Running=32) | 4 of 139,263 (0.00%) | The 32-slot ceiling is essentially never hit today |
| Queue (Waiting>0) | 174 samples (0.12%), max 9 | Queueing is rare and shallow |
| GPU KV cache | mean 1.24% · P95 5.3% · P99 9.2% · max 45.9% | Memory is wide open; the 46% max is a long-context outlier |
| Generation throughput | mean 79.4 · P95 195 · max 905 tok/s | Aggregate token ceiling ~900 tok/s; ~9% used on average |
| Prompt throughput | mean 846 · max 19,281 tok/s | Prefix cache (66.5% hit) absorbs most prompt cost |
| Chat completions | 159,831 total (97.6% HTTP 200; 3,913 × 400) | ~5,700/day |
| Busiest hour | 2,249 req/h (peak running only 14) | High request rate ≠ high concurrency — requests are short |
| Req/hour (active hrs) | median 95 · P95 896 · max 2,249 | Very spiky, business-hours shaped |

**GPU telemetry (3h peak window, 4× GPU):** SM utilization when active mean 66.8%, **P50 98%** (compute-bound per step), memory-bandwidth util only 25% mean → **compute-bound, not memory-bandwidth-bound**. Power 179 W avg / 301 W max per GPU. Temp 74 °C avg / 88 °C max. GPUs idle 22% of the window.

## The scaling basis: concurrency → KV cache & throughput

Measured averages per concurrency level (the extrapolation curve):

| Running reqs | avg KV % | aggregate gen tok/s | per-request tok/s |
|---|---|---|---|
| 1 | 1.3% | 63 | 63 |
| 2 | 1.9% | 119 | 60 |
| 4 | 4.5% | 161 | 40 |
| 8 | 8.4% | 220 | 28 |
| 12 | 8.2% | 326 | 27 |
| 16 | 14.7% | 305 | 19 |
| 20 | 7.2% | 613 | 31 |
| 24 | 11.2% | 591 | 25 |

Two facts fall out:
1. **KV cache grows ~1% per concurrent request** (with variance from context length). At the 32-slot ceiling, KV ≈ 30–46% → memory is **not** the first limit. KV would only run out around **~70–100 concurrent** long-context requests.
2. **Per-request generation speed degrades gracefully** from ~63 tok/s (solo) to ~25 tok/s (busy) — still well above the ~20 tok/s readability floor even at high concurrency.

## Capacity model — what happens as users grow

Peak concurrency scales roughly linearly with users (concurrency ≈ arrival rate × request duration; today ~100 users → peak ~25, absolute max 32). The limits, in the order they bite:

| Limit | Threshold | First binds around |
|---|---|---|
| 1. `max_num_seqs` = 32 slots | peak concurrency > 32 → queueing → TTFT rises | **~125–130 users** (current config) |
| 2. KV cache memory | KV → 100% (≈ 70–100 concurrent, context-dependent) | ~250–350 users (after raising slots) |
| 3. Aggregate token throughput | ~900 tok/s ceiling | ~300–400 users (heavy-use) |
| 4. GPU compute (SM) | already P50 98% per active step; saturates with sustained load | overlaps 3 |

### At 200 users specifically

- **Current config (32 slots):** peak hours would see ~40–50 concurrent demand → exceeds 32 → **queueing during the 1–2 busiest hours/day**, TTFT spikes then. The other ~22 active hours/day stay fine. KV cache ~40–50% (OK). Aggregate throughput ~200–400 tok/s of the ~900 ceiling (OK).
- **With `max_num_seqs` raised to ~64** (KV memory and the ~900 tok/s ceiling both allow it): **200 users handled comfortably**, no queueing, per-user generation ~25–30 tok/s during peaks. This is a config change + restart, not new hardware.

### How many more users can we take?

- **Without touching anything:** ~25–30% more → **~125–130 users** before peak-hour queueing starts.
- **With the `max_num_seqs` bump (one setting):** ~**2.5–4×** → **~250–400 users** on the same 4-GPU box, at which point GPU compute / the ~900 tok/s aggregate ceiling becomes the genuine hardware limit.
- **Beyond that:** add replicas behind the LiteLLM/ALB layer (horizontal scale) — the architecture already supports it (ASG + ALB).

## What we have vs. what we'd need

| Question | Have it? | Source |
|---|---|---|
| Token throughput (aggregate + per-request) | ✅ Yes | logs.out throughput samples |
| Concurrency & queue depth | ✅ Yes | logs.out Running/Waiting |
| KV cache / GPU memory pressure | ✅ Yes | logs.out KV%, nvidia_smi FB |
| GPU usage (power, temp, SM, mem-BW) | ✅ Yes | nvidia_smi.log (3h peak window) |
| **TTFT (production)** | ❌ **No** | Not emitted by the engine logs — only queue depth as proxy |
| TTFT vs load curve | ⚠️ Partial | Benchmark workbook has it for *smaller* models (Qwen3-14B/32B), not the 397B |

## Caveats & assumptions

- Linear users→concurrency scaling assumes the **same usage pattern** (business-hours-spiky, short requests, 66% prefix-cache hit). A shift to long-context / agentic workloads would raise KV and per-request cost, lowering the user ceiling.
- GPU telemetry is a single 3-hour peak window (~450 samples/GPU), not the full 28 days — power/temp/SM figures are representative of peak, not necessarily worst-case.
- The 45.9% KV max shows long-context requests exist; under a heavier long-context mix the KV limit (limit 2) could bind sooner than 250 users.
- Single replica analyzed. Numbers are for one 4-GPU server.

## Recommended next step to make this exact

Run a controlled **`vllm bench serve` sweep** against the 397B (the repo's RunPod pipeline already does this — see [01_architecture-infrastructure.md](01_architecture-infrastructure.md) "Benchmark pipeline") at request rates spanning the projected 200-user peak, capturing **TTFT, TPOT, ITL** vs RPS. That converts the queue-depth proxy here into a hard latency-vs-load curve and pins the exact `max_num_seqs` sweet spot.

## Related

- Raw data identified → [07_analytics-telemetry.md](07_analytics-telemetry.md)
- Production performance context → [02_performance-case-study.md](02_performance-case-study.md)
- Benchmark/TTFT data for smaller models → [03_benchmarks-model-sizing.md](03_benchmarks-model-sizing.md)
