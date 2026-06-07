---
title: AI-Usage-Analytics
date: 2026-05-27
author: Becze Szabolcs
status: active
description: OpenWebUI / LiteLLM napi tag-szintű használati export és a Sonrisa belső vLLM (Qwen3.5-397B-NVFP4) szerver log elemzése egy közös tab-alapú HTML dashboardban. CPS AI-Native OS irányhoz kapcsolódó megfigyelési réteg.
tags: [cps, ai-ops, openwebui, litellm, vllm, analytics]
id: 5904f0bd-437a-444a-baa3-cddb6e70666c
index_schema_version: 1
---

# AI-Usage-Analytics

Sonrisa belső AI infrastruktúra megfigyelési felülete. **Három nézet** egy dashboardban (felső tab-sor):

1. **User-használat (CSV)** — OpenWebUI/LiteLLM napi tag-szintű export per user.
2. **vLLM Server (logok)** — Qwen3.5-397B-NVFP4 inference server runtime metrikái (köztük **token-throughput** prompt+generation tok/s, KV cache, prefix hit, concurrency, HTTP/errors).
3. **GPU telemetria** — `nvidia-smi dmon` 4× GPU: összes + per-GPU fogyasztás, hőmérséklet, SM compute util, memory-bandwidth util, PCIe sávszél, SM-megoszlás histogram. (2026-05-29-én hozzáadva.)

### Időablak-szűrő (Heti / Havi / Teljes)

A fejlécben globális szűrő (`Heti` = utolsó 7 nap, `Havi` = utolsó 30 nap, `Teljes`). Reload-alapú (hash + reload), minden tabra hat: a user-, server- és áram-metrikák az adott ablakra számolódnak újra a nyers sorokból + log-szériából.

### Költségkalkulátor (4. tab) — saját OPEX vs AWS Bedrock

Interaktív kalkulátor (`Költségkalkulátor` tab). Bemenetek szerkeszthetők (OPEX tételek EUR/hó, időszak nap, userek, összes token millióban, input/output arány); alapértékek a statisztikából (92 user, 44 nap, 4,16 Mrd token, ~97% input). Kimenet **EUR + HUF + költség/1M token + költség/user/hó**, és összehasonlító tábla + diagram az AWS Bedrock modellekkel (azonos token-volumenre).

OPEX forrás: `Infarm OPEX.xlsx` (havi €2801,11). Bedrock árak (on-demand, us-east-1, May 2026, a `build_dashboard.py` `calc.bedrock` listájában szerkeszthető): Claude Sonnet 4.5 $3/$15, DeepSeek-R1 $1,35/$5,40, Nova Pro $0,80/$3,20, Llama 3.3 70B $0,72/$0,72, Nova Micro $0,035/$0,14 per 1M.

**Eredmény (44 nap, 4,16 Mrd token):** saját ≈ **€0,99 / 1M token (350 Ft)**. Bedrock-hoz képest: Claude Sonnet (frontier) **2,95× drágább**, DeepSeek-R1 **1,29× drágább**, Nova Pro 0,76×, Llama 70B 0,63×, Nova Micro 0,03×. Vagyis frontier-minőségnél (a Qwen3.5-397B oda tartozik) mi olcsóbbak vagyunk; kis modelleknél a Bedrock olcsóbb. (Fix OPEX → nagy volumennél nyom le a per-token költség.)

### Áramköltség-számítás

Ár: **150 Ft/kWh** (1500 Ft / 10 kWh, user-megadott 2026-05-29) ≈ **€0,42/kWh** (FX 354,18 Ft/EUR az OPEX-ből). Konstansok a `build_dashboard.py` tetején (`ELECTRICITY_HUF_PER_KWH`, `HUF_PER_EUR`).

Energia-modell: óránként `aktív_óraarány × 712 W (aktív 4-GPU) + (1 − arány) × 58 W (idle)` → Wh, a vLLM log per-órás aktív mintaarányából, a GPU-teljesítmény szinteket a `nvidia_smi.log` adja. A server + GPU tabon külön áramköltség-kártya: energia (kWh), költség HUF + EUR, napi átlag, 30-napos vetítés. **Teljes 28 nap ≈ 351 kWh ≈ 52 722 Ft / €148,86** (csak GPU; teljes szerver + hűtés ennél több). Megjegyzés: GPU-only becslés, az OPEX `Fogyasztás` sora 100 000 Ft körül van.

## Mit tartalmaz

- `build_dashboard.py` — Python szkript, **három forrásból** parsol (CSV + vLLM log + nvidia-smi dmon log) és egy self-contained HTML dashboardot generál (Chart.js, no backend, no build).
- `dashboard.html` — generált, böngészőben megnyitható dashboard. Adatok beágyazva.
- `capacity_analysis.py` — kapacitás-elemző szkript (concurrency / KV / throughput / GPU eloszlások). Lásd `knowledge-base/08_capacity-analysis.md`.

## Input formátumok

### CSV (LiteLLM admin export)
Oszlopok: `Date, Tag, Tag ID, Key Alias, Key ID, Spend ($), Requests, Successful Requests, Failed Requests, Total Tokens, Prompt Tokens, Completion Tokens`. A Tag ID-ban van az `x-openwebui-user-email: <email>` minta. Két kulcs: `open-webui-local` ($0) és `open-webui-external` (fizetős).

### vLLM logok (Docker stdout dump)
`<container>  | <log content>` formátum. Releváns sortípusok:
- `INFO MM-DD HH:MM:SS [loggers.py:271] Engine 000: Avg prompt throughput: ... Generation throughput: ... Running: ... Waiting: ... GPU KV cache usage: ...% Prefix cache hit rate: ...%` — periodikus throughput minta (~5-15 mp gyakorisággal).
- `INFO:    <ip> - "POST /v1/chat/completions HTTP/1.1" <status>` — HTTP access log (timestamp nélkül).
- `ERROR MM-DD HH:MM:SS [...]` — modul-szintű timed errorok.
- `ERROR:    Exception in ASGI application` — ASGI exception starter (stack-trace előtti sor).

A parser óránként bucketeli a throughput-mintákat (avg + max) és külön számolja a timed errorokat / warningokat / ASGI exceptionöket. A HTTP requesteket státusz + endpoint + metódus bontásban összesíti.

### nvidia-smi dmon log (`raw/nvidia_smi.log`)
Fix oszlopos dmon kimenet: `gpu pwr gtemp mtemp sm mem enc dec jpg ofa mclk pclk ... rxpci txpci`. GPU-nként egy sor per mintavételi időpont (idx 0..3 ciklikusan). A parser minden ciklust egy időlépéssé csoportosít, és per-timestep aggregál (összfogyasztás, átlag SM/mem util, max hőmérséklet, PCIe) + per-GPU sorozatok + aktív/idle statisztika (aktív = mclk > 1000 MHz). Időbélyeg nincs → x-tengely = eltelt perc (~25s/minta).

## Aktuális snapshot

**User-használat (2026-04-13 → 2026-05-27):**
- 917 sor, 44 nap, 92 user · 171,863 req, 0 failed · 4.16B token (96% prompt / 4% completion) · $5.35

**vLLM Server (2026-04-29 → 2026-05-27, 113 MB log):**
- 139,263 throughput minta, 677 aktív óra · 240,924 HTTP req, 98.4% success rate · 3,932 4xx / 1 5xx
- 17,879 modul error, 3,678 ASGI exception, 30 warning
- Peak: 19,281 prompt tok/s, 905 generation tok/s, 32 concurrent reqs

**GPU telemetria (`nvidia_smi.log`, 4× GPU, ~3 óra ablak):**
- 430 minta (~25s/minta), 78.6% aktív duty cycle
- Fogyasztás aktív 712 W (4 GPU), csúcs 1153 W; idle 15 W/GPU
- SM compute util aktív átlag 66.2%, P95 100% (compute-kötött); mem-BW util csak 25%; max hőmérséklet 88°C
- Az SM-megoszlás bimodális: vagy idle vagy 81-100% → bursty workload, sok duty-cycle headroom

## Újrafuttatás új exporttal

1. `CSV_PATH` a `build_dashboard.py` tetején a friss LiteLLM exportra mutasson (jelenleg `~/Downloads`). `LOG_PATH` és `GPU_PATH` alapból az in-repo `raw/logs.out` és `raw/nvidia_smi.log` (reprodukálható).
2. `python build_dashboard.py` — új `dashboard.html` (CSV + vLLM log + GPU log mindhárom beágyazva).
3. Élőben: `python -m http.server 8141` a `stats/` mappából, majd `http://127.0.0.1:8141/dashboard.html`.

## Kapcsolódó

- [[project_cps_aiops_direction]] — CPS AI-Native OS stratégiai irány: ez az adat a "használat megfigyelési réteg" pillérhez tartozik
- CPS Constitution — Sonrisa AI értékáram
