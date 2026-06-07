#!/usr/bin/env python3
"""Capacity analysis of the vLLM Inference Farm from raw production logs.

Parses logs.out (vLLM engine throughput samples) and nvidia_smi.log (GPU dmon)
to characterize the current operating point and extrapolate headroom.
"""
import re
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent / "raw"
LOG = BASE / "logs.out"
GPU = BASE / "nvidia_smi.log"

LOGGER_RE = re.compile(
    r"(?:INFO|WARNING)\s+(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})\s+"
    r"\[loggers\.py:271\].*?"
    r"Avg prompt throughput:\s*([\d.]+)\s*tokens/s,\s*"
    r"Avg generation throughput:\s*([\d.]+)\s*tokens/s,\s*"
    r"Running:\s*(\d+)\s*reqs,\s*"
    r"Waiting:\s*(\d+)\s*reqs,\s*"
    r"GPU KV cache usage:\s*([\d.]+)%,\s*"
    r"Prefix cache hit rate:\s*([\d.]+)%"
)
HTTP_COMPLETION_RE = re.compile(r'"POST /v1/chat/completions HTTP/[\d.]+"\s+(\d{3})')
TS_RE = re.compile(r"(?:INFO|WARNING|ERROR)\s+(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})\s+\[")


def pct(sorted_vals, p):
    if not sorted_vals:
        return 0
    k = (len(sorted_vals) - 1) * p / 100
    f = int(k)
    c = min(f + 1, len(sorted_vals) - 1)
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)


# --- Parse logs.out ---
running, waiting, kv, gen_tps_active, prompt_tps_active, prefix = [], [], [], [], [], []
# per running-level: kv sum/count, gen sum/count  (the concurrency->KV curve)
by_running = defaultdict(lambda: {"kv": [], "gen": [], "n": 0})
waiting_pos = 0  # samples with waiting>0
running_at_32 = 0
hourly_reqs = defaultdict(int)
hourly_running_max = defaultdict(int)
hourly_kv_max = defaultdict(float)
status_counts = defaultdict(int)
cur_hour = None
total_completions = 0

with LOG.open("r", encoding="utf-8", errors="replace") as f:
    for line in f:
        if "[loggers.py:271]" in line:
            m = LOGGER_RE.search(line)
            if m:
                mo, da, hh = m.group(1), m.group(2), m.group(3)
                p_tps, g_tps = float(m.group(6)), float(m.group(7))
                run, wait = int(m.group(8)), int(m.group(9))
                kvc, pfx = float(m.group(10)), float(m.group(11))
                running.append(run); waiting.append(wait); kv.append(kvc); prefix.append(pfx)
                by_running[run]["kv"].append(kvc); by_running[run]["gen"].append(g_tps); by_running[run]["n"] += 1
                if wait > 0: waiting_pos += 1
                if run >= 32: running_at_32 += 1
                if g_tps > 0: gen_tps_active.append(g_tps)
                if p_tps > 0: prompt_tps_active.append(p_tps)
                cur_hour = f"{mo}-{da} {hh}:00"
                hourly_running_max[cur_hour] = max(hourly_running_max[cur_hour], run)
                hourly_kv_max[cur_hour] = max(hourly_kv_max[cur_hour], kvc)
            continue
        mh = HTTP_COMPLETION_RE.search(line)
        if mh:
            status_counts[mh.group(1)] += 1
            total_completions += 1
            if cur_hour:
                hourly_reqs[cur_hour] += 1
            continue
        mt = TS_RE.search(line)
        if mt:
            cur_hour = f"{mt.group(1)}-{mt.group(2)} {mt.group(3)}:00"

running.sort(); waiting.sort(); kv.sort(); gen_tps_active.sort(); prompt_tps_active.sort()
n = len(running)

print("=" * 70)
print(f"LOGS.OUT  — {n:,} engine throughput samples")
print("=" * 70)
print(f"\nCONCURRENCY (Running reqs in-batch):")
for p in (50, 90, 95, 99, 100):
    print(f"  P{p:<3}: {pct(running,p):.0f}")
print(f"  mean: {sum(running)/n:.2f}   max: {running[-1]}")
print(f"  samples at max_num_seqs=32 (saturated): {running_at_32:,} ({running_at_32/n*100:.2f}%)")

print(f"\nQUEUE (Waiting reqs):")
print(f"  samples with waiting>0: {waiting_pos:,} ({waiting_pos/n*100:.2f}%)")
for p in (95, 99, 100):
    print(f"  P{p:<3}: {pct(waiting,p):.0f}")
print(f"  max waiting: {waiting[-1]}")

print(f"\nGPU KV CACHE USAGE (%):")
for p in (50, 90, 95, 99, 100):
    print(f"  P{p:<3}: {pct(kv,p):.2f}%")
print(f"  mean: {sum(kv)/n:.2f}%")

print(f"\nGENERATION THROUGHPUT (tok/s, active samples only, n={len(gen_tps_active):,}):")
for p in (50, 90, 95, 99, 100):
    print(f"  P{p:<3}: {pct(gen_tps_active,p):.1f}")
print(f"  mean: {sum(gen_tps_active)/len(gen_tps_active):.1f}")
print(f"\nPROMPT THROUGHPUT (tok/s, active, n={len(prompt_tps_active):,}): mean {sum(prompt_tps_active)/len(prompt_tps_active):.0f}, P95 {pct(prompt_tps_active,95):.0f}, max {prompt_tps_active[-1]:.0f}")
print(f"PREFIX CACHE HIT: mean {sum(prefix)/len(prefix):.1f}%")

print(f"\nCONCURRENCY -> KV CACHE & THROUGHPUT curve (the extrapolation basis):")
print(f"  {'running':>7} | {'samples':>8} | {'avg KV%':>8} | {'avg gen tok/s':>13}")
for r in sorted(by_running):
    d = by_running[r]
    if d["n"] < 20:  # skip sparse buckets
        continue
    avg_kv = sum(d["kv"])/len(d["kv"])
    avg_gen = sum(d["gen"])/len(d["gen"])
    print(f"  {r:>7} | {d['n']:>8,} | {avg_kv:>7.2f}% | {avg_gen:>13.1f}")

print(f"\nHTTP /v1/chat/completions: {total_completions:,} total")
for s in sorted(status_counts):
    print(f"  {s}: {status_counts[s]:,}")

# Peak request hours
top_hours = sorted(hourly_reqs.items(), key=lambda x: -x[1])[:10]
print(f"\nTOP 10 BUSIEST HOURS (chat completions/hour):")
for h, c in top_hours:
    print(f"  {h}: {c:,} req/h  (peak running {hourly_running_max.get(h,0)}, peak KV {hourly_kv_max.get(h,0):.1f}%)")
active_hours = [h for h,c in hourly_reqs.items() if c>0]
print(f"\n  active hours with traffic: {len(active_hours)}")
if active_hours:
    rates = sorted(hourly_reqs[h] for h in active_hours)
    print(f"  req/hour  median {pct(rates,50):.0f}, P95 {pct(rates,95):.0f}, max {rates[-1]:,}")

# --- Parse nvidia_smi.log ---
print("\n" + "=" * 70)
print("NVIDIA_SMI.LOG — GPU dmon")
print("=" * 70)
gpu_rows = []
with GPU.open() as f:
    for line in f:
        if line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 8:
            continue
        try:
            idx = int(parts[0]); pwr = float(parts[1]); gtemp = float(parts[2])
            sm = float(parts[4]); mem = float(parts[5]); mclk = float(parts[10])
        except (ValueError, IndexError):
            continue
        gpu_rows.append((idx, pwr, gtemp, sm, mem, mclk))

active = [r for r in gpu_rows if r[5] > 1000]   # mclk high => active
idle = [r for r in gpu_rows if r[5] <= 1000]
print(f"  total samples: {len(gpu_rows):,}  (active {len(active):,} / idle {len(idle):,})")
if active:
    sm_a = sorted(r[3] for r in active)
    print(f"  SM util (active):  mean {sum(sm_a)/len(sm_a):.1f}%  P50 {pct(sm_a,50):.0f}%  P95 {pct(sm_a,95):.0f}%  max {sm_a[-1]:.0f}%")
    mem_a = sorted(r[4] for r in active)
    print(f"  MEM-BW util (active): mean {sum(mem_a)/len(mem_a):.1f}%  P95 {pct(mem_a,95):.0f}%  max {mem_a[-1]:.0f}%")
    pwr_a = sorted(r[1] for r in active)
    print(f"  power/GPU (active): mean {sum(pwr_a)/len(pwr_a):.0f}W  max {pwr_a[-1]:.0f}W")
    t_a = sorted(r[2] for r in active)
    print(f"  temp (active): mean {sum(t_a)/len(t_a):.0f}C  max {t_a[-1]:.0f}C")
if idle:
    print(f"  power/GPU (idle): mean {sum(r[1] for r in idle)/len(idle):.0f}W")
