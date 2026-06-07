---
title: "Inference Farm — Analytics, Dashboards & Raw Telemetry"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "Inventory and identification of the stats/ analytics pipeline for the Inference Farm: the AI-Usage-Analytics dashboard (dashboard.html — two views: OpenWebUI/LiteLLM per-user usage from CSV, and vLLM server runtime from logs), the build_dashboard.py generator, and the raw/ source artifacts (113 MB vLLM stdout logs.out, nvidia-smi dmon nvidia_smi.log, the infarm architecture diagram, plus the generated vllm_dashboard.html and gpu_dashboard2.html). Documents each file's format, period, and what it feeds. Companion to the production case study (02)."
practice_area: cps-inference-farm
type: data-inventory
audience: internal-engineering
provenance: "Compiled by Forge on 2026-05-29 from local mirror at Practices/Inference-Farm/stats/ (README.md, build_dashboard.py, dashboard.html, raw/*). Raw artifacts are the local copies of the SharePoint AwsInFarm telemetry."
id: d135fbbb-b4b1-4dce-bd4b-311c25304155
index_schema_version: 1
bdos_index: false
---

# Analytics, Dashboards & Raw Telemetry

> Location: [../stats/](../stats/). This note identifies **what each file is**. Deeper analysis of the data itself is a separate, follow-up pass.

## The pipeline at a glance

`build_dashboard.py` ingests **two independent data sources** and emits one self-contained `dashboard.html` (Chart.js, no backend):

1. **OpenWebUI / LiteLLM usage CSV** — per-user, per-day billing/usage export (the *who used what* view).
2. **vLLM server logs** (`logs.out`) — the inference engine's runtime metrics (the *how the server behaved* view).

Two further standalone dashboards (`vllm_dashboard.html`, `gpu_dashboard2.html`) visualize the server logs and GPU telemetry separately — these are the visuals behind the [production case study](02_performance-case-study.md).

## File-by-file identification

### `stats/` (top level)

| File | What it is |
|---|---|
| `README.md` | Describes the AI-Usage-Analytics project, input formats, and the current snapshot. |
| `build_dashboard.py` | ~900-line Python generator. Stream-parses the CSV + `logs.out` with regexes, hourly-buckets the throughput samples, aggregates HTTP/errors, and writes `dashboard.html`. Paths configured at top (`CSV_PATH`, `LOG_PATH`); `LOG_YEAR=2026` (logs lack a year). Rerun: `python build_dashboard.py`; serve at `http://localhost:8141/dashboard.html`. |
| `dashboard.html` | Generated combined dashboard, "**Sonrisa AI Usage — OpenWebUI / LiteLLM**" (255 KB, data embedded). |

### `dashboard.html` structure (three views, as of 2026-05-29)

**View 1 — Napi használat (user usage, from CSV):**
- Daily usage chart, tabs: Tokens / Requests / Active users / Spend ($)
- Local vs External API split (keys `open-webui-local` $0 vs `open-webui-external` paid)
- Top 15 users by tokens
- Token structure (prompt vs completion)
- Full user list

**View 2 — vLLM Server (from logs):**
- Throughput over time, tabs: **Tokens/s (prompt + generation)** / Active requests / KV cache + Prefix hit / Errors+Warnings
- HTTP status breakdown
- Endpoint traffic (HTTP, by endpoint + method)
- Error patterns (non-2xx)

**View 3 — GPU telemetria (from `nvidia_smi.log`, added 2026-05-29):**
- KPI strip: GPUs, samples, duty cycle, active 4-GPU power (712 W) + peak (1153 W), SM util avg/P95 (66%/100%), mem-BW util (25%), max temp (88°C), idle power/GPU (15 W)
- Total 4-GPU power over time (power-gating waveform)
- Per-GPU power + per-GPU temperature
- Utilization-over-time, tabs: SM compute % / Memory bandwidth % / PCIe MB/s / Max temp °C
- SM utilization distribution histogram (bimodal: idle vs 81–100%)
- Token-throughput reminder panel cross-linking to the Server view + [08_capacity-analysis.md](08_capacity-analysis.md)

> Token throughput is the default tab of the Server view's throughput chart (prompt + generation tok/s), plus peak-tok/s KPIs. The GPU view adds the hardware side. Both were the 2026-05-29 "incorporate GPU usage and token throughput" pass.

**View 4 — Költségkalkulátor (cost calculator, added 2026-05-29):**
- Editable inputs (OPEX items €/mo, period days, users, total tokens, input/output split), seeded from the real stats (92 users, 44 days, 4.16B tokens, ~97% input).
- Our-cost card: period + monthly cost, **cost / 1M token**, cost / user / month — all in **EUR + HUF**.
- AWS Bedrock comparison table + bar chart (same token volume): each model's period cost (EUR + HUF), €/1M, and ×-vs-ours. Bedrock rates editable in `build_dashboard.py` (`calc.bedrock`).
- Headline result: self-host ≈ **€0.99 / 1M token** — ~3× cheaper than Claude Sonnet (frontier), ~1.3× cheaper than DeepSeek-R1, but pricier than small models (Llama 70B, Nova Pro). See [04_business-model-pricing.md](04_business-model-pricing.md) for the business read.

**Global time-window filter + electricity cost (added 2026-05-29):**
- Header filter **Heti / Havi / Teljes** (last 7 days / last 30 days / all) — reload-based (`#weekly`/`#monthly`/`#all` hash), recomputes every tab's metrics from the raw rows + log series.
- **Electricity cost card** on the Server + GPU tabs: energy (kWh), cost in **HUF and EUR**, daily average, 30-day projection — for the selected window. Price **150 Ft/kWh** (1500 Ft / 10 kWh) ≈ €0.42/kWh. Energy modelled per-hour as `active_fraction × 712 W + idle × 58 W` (GPU power levels from `nvidia_smi.log`, active fraction from the vLLM log). Full 28 days ≈ **351 kWh ≈ 52,722 Ft / €148.86** (GPU-only). Constants live at the top of `build_dashboard.py`.

### `stats/raw/` — source artifacts

| File | Size | What it is | Feeds |
|---|---|---|---|
| `logs.out` | 113 MB / 752,800 lines | Raw vLLM Docker **stdout dump** from container `vllm-qwen35-397b-nvfp4-1`. Period **2026-04-29 06:44 → 2026-05-27 10:50**. Holds the periodic `loggers.py:271` throughput samples (139,263 of them), HTTP access logs, and errors. | dashboard.html (View 2), vllm_dashboard.html, case study §3–5 |
| `nvidia_smi.log` | 277 KB / 1,800 lines | `nvidia-smi dmon` output, **4× GPU**, ~450 samples. Columns: pwr, gtemp, sm%, mem%, mclk, pclk, fb (~89 GB used/GPU), rxpci/txpci. Idle 405 MHz/~13–19 W; active 13,365 MHz/84 W+. | gpu_dashboard2.html, case study §6–7 (GPU telemetry) |
| `infarm.drawio.png` | 313 KB | **Architecture diagram** (hybrid AWS + on-prem). See [01_architecture-infrastructure.md](01_architecture-infrastructure.md) "Deployed topology". | architecture note |
| `vllm_dashboard.html` | 156 KB | Generated dashboard "**vLLM · Qwen3.5-397B-NVFP4 · Inference Farm**". 6 charts: generation throughput, prompt throughput, GPU KV cache %, prefix cache hit %, active requests (max/hr), activity ratio. | (viz of logs.out) |
| `gpu_dashboard2.html` | 196 KB | Generated dashboard "**GPU Stats – nvidia-smi dmon · 4× GPU**". 6 charts: total power, per-GPU power, per-GPU temp, SM util, memory bandwidth, PCIe bandwidth. | (viz of nvidia_smi.log) |
| `README.md` | 10 KB | The `AwsInFarm` IaC repo README — duplicate of the canonical source already distilled in [01_architecture-infrastructure.md](01_architecture-infrastructure.md). |
| `blackwell-vllm-setup.md` | 6 KB | Blackwell + vLLM (MiniMax M2.1) setup guide — duplicate, distilled in [01](01_architecture-infrastructure.md). |

> Note: SharePoint carries `gpu_dashboard3.html` (a newer revision); the local mirror has `gpu_dashboard2.html`. The CSV source (`tag_usage_daily_with_keys_2026-05-27.csv`) is **not** in `raw/` — `build_dashboard.py` reads it from `~/Downloads`.

## Production model config (from logs.out header)

The server process behind the logs:
- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` (served as `Qwen/Qwen3.5-397B-NVFP4`)
- vLLM `0.19.2rc1.dev134+gfe9c3d6c5`
- `tensor_parallel_size=4`, `enable_expert_parallel=True`, `gpu_memory_utilization=0.9`
- `max_model_len=131072`, `max_num_batched_tokens=32768`, `max_num_seqs=32`
- `enable_prefix_caching=True`, `enable_chunked_prefill=True`
- `tool_call_parser=qwen3_coder`, `reasoning_parser=qwen3`, `trust_remote_code=True`

## Current data snapshots

**User usage (CSV, 2026-04-13 → 2026-05-27):** 917 rows · 44 days · 92 users · 171,863 requests · 0 failed · 4.16B tokens (96% prompt / 4% completion) · $5.35 spend.

**vLLM server (logs.out, 2026-04-29 → 2026-05-27):** 139,263 throughput samples · 677 active hours · 240,924 HTTP requests · 98.4% success · 3,932 4xx / 1 5xx · 17,879 module errors · 3,678 ASGI exceptions · 30 warnings. Peak: 19,281 prompt tok/s, 905 generation tok/s, 32 concurrent requests.

## Open threads (for the deeper-dig pass)

- **Two usage numbers don't share scope/period:** CSV usage (4.16B tokens, 92 users, from 04-13) is OpenWebUI/LiteLLM-fronted traffic; the Q1 stats workbook ([06_usage-statistics.md](06_usage-statistics.md)) reports 5.77B tokens for Q1 — different windows and pipelines. Reconcile before quoting a single "usage" figure.
- **Error volume:** 17,879 module errors + 3,678 ASGI exceptions over the window — not yet characterized (root cause vs benign).
- **Where the 397B physically runs** (AWS vs on-prem Blackwell) is not 100% pinned from these files alone — see the architecture note's open question.

## Related

- Production performance interpretation → [02_performance-case-study.md](02_performance-case-study.md)
- Deployed topology → [01_architecture-infrastructure.md](01_architecture-infrastructure.md)
- Q1 2026 token accounting → [06_usage-statistics.md](06_usage-statistics.md)
