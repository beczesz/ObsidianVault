#!/usr/bin/env python3
"""Build a self-contained HTML dashboard from the OpenWebUI/LiteLLM tag_usage CSV."""

import csv
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_RAW = Path(__file__).parent / "raw"
CSV_PATH = Path(r"C:\Users\EvoComputers\Downloads\tag_usage_daily_with_keys_2026-05-27.csv")
LOG_PATH = BASE_RAW / "logs.out"               # in-repo copy (reproducible)
GPU_PATH = BASE_RAW / "nvidia_smi.log"          # nvidia-smi dmon snapshot
OUT_PATH = Path(__file__).parent / "dashboard.html"
LOG_YEAR = 2026  # The log lacks year info; CSV range tells us it's 2026.
GPU_SAMPLE_INTERVAL_S = 25  # nvidia-smi dmon sampling interval (approx, per case study)

# --- Electricity pricing (user-provided 2026-05-29) ---
ELECTRICITY_HUF_PER_KWH = 150.0   # 1500 Ft / 10 kWh
HUF_PER_EUR = 354.18              # FX from Infarm OPEX.xlsx (2026-05-28)

EMAIL_RE = re.compile(r"x-openwebui-user-email:\s*(\S+)")

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

HTTP_RE = re.compile(
    r'"(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+(\S+)\s+HTTP/[\d.]+"\s+(\d{3})'
)

# Lines that mark stand-alone ERROR events. `ERROR:    Exception in ASGI application`
# kicks off a multi-line traceback — we count those starter lines, not every traceback frame.
ASGI_ERROR_RE = re.compile(r"ERROR:\s+Exception in ASGI application")
TIMED_ERROR_RE = re.compile(r"ERROR\s+(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})\s+\[")
TIMED_WARN_RE = re.compile(r"WARNING\s+(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})\s+\[")


def extract_email(tag_id: str) -> str:
    m = EMAIL_RE.search(tag_id or "")
    return m.group(1) if m else (tag_id or "unknown")


def short_name(email: str) -> str:
    return email.split("@")[0] if "@" in email else email


def parse_logs(path: Path) -> dict:
    """Stream-parse the vLLM logs. Returns aggregates + hourly time-series."""
    if not path.exists():
        return {"available": False}

    # Hourly buckets keyed by "YYYY-MM-DD HH:00"
    hourly = defaultdict(lambda: {
        "samples": 0,
        "prompt_tps_sum": 0.0, "prompt_tps_max": 0.0,
        "gen_tps_sum": 0.0, "gen_tps_max": 0.0,
        "running_sum": 0, "running_max": 0,
        "waiting_sum": 0, "waiting_max": 0,
        "kv_sum": 0.0, "kv_max": 0.0,
        "prefix_sum": 0.0,
        "errors_timed": 0, "warnings_timed": 0,
        "active_samples": 0,
    })

    endpoint_status = defaultdict(lambda: defaultdict(int))  # endpoint -> status -> count
    method_count = defaultdict(int)
    status_count = defaultdict(int)
    asgi_errors_total = 0
    errors_timed_total = 0
    warnings_timed_total = 0
    sample_total = 0

    ts_min = None
    ts_max = None
    last_http_errors = []  # store recent non-2xx for the UI

    file_size = path.stat().st_size
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            # Most lines look like: "<prefix> | ...". Skip cheap rejection.
            if "loggers.py:271" in line:
                m = LOGGER_RE.search(line)
                if m:
                    mo, da, hh, mm, ss = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
                    p_tps = float(m.group(6))
                    g_tps = float(m.group(7))
                    run = int(m.group(8))
                    wait = int(m.group(9))
                    kv = float(m.group(10))
                    prefix = float(m.group(11))
                    bucket = f"{LOG_YEAR}-{mo}-{da} {hh}:00"
                    b = hourly[bucket]
                    b["samples"] += 1
                    b["prompt_tps_sum"] += p_tps
                    if p_tps > b["prompt_tps_max"]: b["prompt_tps_max"] = p_tps
                    b["gen_tps_sum"] += g_tps
                    if g_tps > b["gen_tps_max"]: b["gen_tps_max"] = g_tps
                    b["running_sum"] += run
                    if run > b["running_max"]: b["running_max"] = run
                    b["waiting_sum"] += wait
                    if wait > b["waiting_max"]: b["waiting_max"] = wait
                    b["kv_sum"] += kv
                    if kv > b["kv_max"]: b["kv_max"] = kv
                    b["prefix_sum"] += prefix
                    if g_tps > 0: b["active_samples"] += 1
                    sample_total += 1
                    ts = f"{LOG_YEAR}-{mo}-{da} {hh}:{mm}:{ss}"
                    if ts_min is None or ts < ts_min: ts_min = ts
                    if ts_max is None or ts > ts_max: ts_max = ts
                continue

            # HTTP access line (no per-line timestamp, just count)
            if 'HTTP/1.1"' in line:
                h = HTTP_RE.search(line)
                if h:
                    method, endpoint, status = h.group(1), h.group(2), h.group(3)
                    endpoint_status[endpoint][status] += 1
                    method_count[method] += 1
                    status_count[status] += 1
                    if status[0] in ("4", "5") and len(last_http_errors) < 50:
                        last_http_errors.append({"method": method, "endpoint": endpoint, "status": status})
                continue

            # Timed warning / error attached to a module + ASGI exception starters
            if "ERROR" in line:
                t = TIMED_ERROR_RE.search(line)
                if t:
                    mo, da, hh = t.group(1), t.group(2), t.group(3)
                    bucket = f"{LOG_YEAR}-{mo}-{da} {hh}:00"
                    hourly[bucket]["errors_timed"] += 1
                    errors_timed_total += 1
                elif ASGI_ERROR_RE.search(line):
                    asgi_errors_total += 1
                continue

            if "WARNING" in line:
                t = TIMED_WARN_RE.search(line)
                if t:
                    mo, da, hh = t.group(1), t.group(2), t.group(3)
                    bucket = f"{LOG_YEAR}-{mo}-{da} {hh}:00"
                    hourly[bucket]["warnings_timed"] += 1
                    warnings_timed_total += 1

    # Finalize hourly time-series
    series = []
    for bucket in sorted(hourly.keys()):
        b = hourly[bucket]
        n = b["samples"] or 1
        series.append({
            "bucket": bucket,
            "samples": b["samples"],
            "prompt_tps_avg": round(b["prompt_tps_sum"] / n, 2),
            "prompt_tps_max": round(b["prompt_tps_max"], 2),
            "gen_tps_avg": round(b["gen_tps_sum"] / n, 2),
            "gen_tps_max": round(b["gen_tps_max"], 2),
            "running_avg": round(b["running_sum"] / n, 2),
            "running_max": b["running_max"],
            "waiting_avg": round(b["waiting_sum"] / n, 2),
            "waiting_max": b["waiting_max"],
            "kv_avg": round(b["kv_sum"] / n, 2),
            "kv_max": round(b["kv_max"], 2),
            "prefix_avg": round(b["prefix_sum"] / n, 2),
            "errors": b["errors_timed"],
            "warnings": b["warnings_timed"],
            "samples_active": b["active_samples"],
        })

    # Endpoint summary (sorted by total)
    endpoints = []
    for ep, statuses in endpoint_status.items():
        total = sum(statuses.values())
        ok = sum(c for s, c in statuses.items() if s.startswith("2"))
        bad4 = sum(c for s, c in statuses.items() if s.startswith("4"))
        bad5 = sum(c for s, c in statuses.items() if s.startswith("5"))
        endpoints.append({
            "endpoint": ep,
            "total": total,
            "ok": ok,
            "client_err": bad4,
            "server_err": bad5,
            "success_rate": round(ok / total * 100, 2) if total else 0,
        })
    endpoints.sort(key=lambda e: e["total"], reverse=True)

    # Peak metrics across all hours
    peak_prompt = max((s["prompt_tps_max"] for s in series), default=0)
    peak_gen = max((s["gen_tps_max"] for s in series), default=0)
    peak_running = max((s["running_max"] for s in series), default=0)
    peak_kv = max((s["kv_max"] for s in series), default=0)

    total_http = sum(status_count.values())
    total_ok = sum(c for s, c in status_count.items() if s.startswith("2"))

    return {
        "available": True,
        "source": str(path),
        "file_size": file_size,
        "ts_min": ts_min,
        "ts_max": ts_max,
        "totals": {
            "throughput_samples": sample_total,
            "http_total": total_http,
            "http_2xx": total_ok,
            "http_4xx": sum(c for s, c in status_count.items() if s.startswith("4")),
            "http_5xx": sum(c for s, c in status_count.items() if s.startswith("5")),
            "success_rate": round(total_ok / total_http * 100, 2) if total_http else 0,
            "errors_timed": errors_timed_total,
            "asgi_errors": asgi_errors_total,
            "warnings_timed": warnings_timed_total,
            "peak_prompt_tps": round(peak_prompt, 2),
            "peak_gen_tps": round(peak_gen, 2),
            "peak_running": peak_running,
            "peak_kv": round(peak_kv, 2),
            "hours_active": len(series),
        },
        "series": series,
        "endpoints": endpoints,
        "status_count": dict(status_count),
        "method_count": dict(method_count),
        "sample_http_errors": last_http_errors,
    }


def _pctile(sorted_vals, p):
    if not sorted_vals:
        return 0
    k = (len(sorted_vals) - 1) * p / 100
    f = int(k)
    c = min(f + 1, len(sorted_vals) - 1)
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)


def parse_gpu(path: Path) -> dict:
    """Parse `nvidia-smi dmon` output (4x GPU). No timestamps -> use sample index.

    dmon prints one row per GPU per interval, cycling idx 0..N. We group every
    cycle (re-seeing a GPU index) into one timestep, then build per-timestep
    aggregates + per-GPU series + active/idle stats.
    Columns: gpu pwr gtemp mtemp sm mem enc dec jpg ofa mclk pclk pviol tviol
             fb bar1 ccpm sbecc dbecc pci rxpci txpci
    """
    if not path.exists():
        return {"available": False}

    timesteps = []          # list of {idx: {pwr,temp,sm,mem,mclk,rx,tx}}
    cur = {}
    n_gpus = 0

    def flush():
        nonlocal cur
        if cur:
            timesteps.append(cur)
            cur = {}

    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if line.lstrip().startswith("#"):
                continue
            p = line.split()
            if len(p) < 11:
                continue
            try:
                idx = int(p[0]); pwr = float(p[1]); temp = float(p[2])
                sm = float(p[4]); mem = float(p[5]); mclk = float(p[10])
                rx = float(p[20]) if len(p) > 20 and p[20] != "-" else 0.0
                tx = float(p[21]) if len(p) > 21 and p[21] != "-" else 0.0
            except (ValueError, IndexError):
                continue
            if idx in cur:
                flush()
            cur[idx] = {"pwr": pwr, "temp": temp, "sm": sm, "mem": mem, "mclk": mclk, "rx": rx, "tx": tx}
            n_gpus = max(n_gpus, idx + 1)
    flush()

    labels, power_total, sm_avg, mem_avg, temp_max, pcie = [], [], [], [], [], []
    per_gpu_power = [[] for _ in range(n_gpus)]
    per_gpu_temp = [[] for _ in range(n_gpus)]
    # active/idle stats accumulators
    act_total_pwr, act_pg_pwr, act_sm, act_mem, act_temp, idle_pg_pwr = [], [], [], [], [], []

    for i, ts in enumerate(timesteps):
        gpus = [ts[g] for g in sorted(ts)]
        tot_pwr = sum(g["pwr"] for g in gpus)
        avg_sm = sum(g["sm"] for g in gpus) / len(gpus)
        avg_mem = sum(g["mem"] for g in gpus) / len(gpus)
        mx_temp = max(g["temp"] for g in gpus)
        pci = sum(g["rx"] + g["tx"] for g in gpus)
        active = max(g["mclk"] for g in gpus) > 1000  # clocked up = serving

        labels.append(round(i * GPU_SAMPLE_INTERVAL_S / 60, 1))  # elapsed minutes
        power_total.append(round(tot_pwr, 1))
        sm_avg.append(round(avg_sm, 1))
        mem_avg.append(round(avg_mem, 1))
        temp_max.append(round(mx_temp, 1))
        pcie.append(round(pci, 1))
        for g in range(n_gpus):
            per_gpu_power[g].append(round(ts[g]["pwr"], 1) if g in ts else None)
            per_gpu_temp[g].append(round(ts[g]["temp"], 1) if g in ts else None)

        if active:
            act_total_pwr.append(tot_pwr)
            act_sm.append(avg_sm)
            act_mem.append(avg_mem)
            act_temp.append(mx_temp)
            for g in gpus:
                act_pg_pwr.append(g["pwr"])
        else:
            for g in gpus:
                idle_pg_pwr.append(g["pwr"])

    act_total_pwr.sort(); act_pg_pwr.sort(); act_sm.sort(); act_mem.sort(); act_temp.sort()

    def _mean(xs):
        return round(sum(xs) / len(xs), 1) if xs else 0

    return {
        "available": True,
        "source": str(path),
        "n_gpus": n_gpus,
        "interval_s": GPU_SAMPLE_INTERVAL_S,
        "labels": labels,
        "power_total": power_total,
        "sm_avg": sm_avg,
        "mem_avg": mem_avg,
        "temp_max": temp_max,
        "pcie": pcie,
        "per_gpu_power": per_gpu_power,
        "per_gpu_temp": per_gpu_temp,
        "totals": {
            "samples": len(timesteps),
            "active": len(act_total_pwr),
            "idle": len(timesteps) - len(act_total_pwr),
            "duty_cycle": round(len(act_total_pwr) / len(timesteps) * 100, 1) if timesteps else 0,
            "power_total_active_avg": _mean(act_total_pwr),
            "power_total_active_max": round(act_total_pwr[-1], 1) if act_total_pwr else 0,
            "power_pg_active_avg": _mean(act_pg_pwr),
            "power_pg_idle_avg": _mean(idle_pg_pwr),
            "sm_active_avg": _mean(act_sm),
            "sm_active_p95": round(_pctile(act_sm, 95), 1),
            "sm_active_max": round(act_sm[-1], 1) if act_sm else 0,
            "mem_active_avg": _mean(act_mem),
            "mem_active_max": round(act_mem[-1], 1) if act_mem else 0,
            "temp_active_avg": _mean(act_temp),
            "temp_active_max": round(act_temp[-1], 1) if act_temp else 0,
        },
    }


def main() -> None:
    rows = []
    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "date": r["Date"],
                "email": extract_email(r["Tag ID"]),
                "key_alias": r["Key Alias"],
                "spend": float(r["Spend ($)"] or 0),
                "requests": int(r["Requests"] or 0),
                "success": int(r["Successful Requests"] or 0),
                "failed": int(r["Failed Requests"] or 0),
                "tokens": int(r["Total Tokens"] or 0),
                "prompt_tokens": int(r["Prompt Tokens"] or 0),
                "completion_tokens": int(r["Completion Tokens"] or 0),
            })

    if not rows:
        print("No data!")
        sys.exit(1)

    # Totals
    totals = {
        "rows": len(rows),
        "users": len({r["email"] for r in rows}),
        "days": len({r["date"] for r in rows}),
        "requests": sum(r["requests"] for r in rows),
        "tokens": sum(r["tokens"] for r in rows),
        "prompt_tokens": sum(r["prompt_tokens"] for r in rows),
        "completion_tokens": sum(r["completion_tokens"] for r in rows),
        "spend": round(sum(r["spend"] for r in rows), 4),
        "failed": sum(r["failed"] for r in rows),
        "date_min": min(r["date"] for r in rows),
        "date_max": max(r["date"] for r in rows),
    }

    # Daily aggregation
    by_date = defaultdict(lambda: {"requests": 0, "tokens": 0, "spend": 0.0, "users": set()})
    for r in rows:
        d = by_date[r["date"]]
        d["requests"] += r["requests"]
        d["tokens"] += r["tokens"]
        d["spend"] += r["spend"]
        d["users"].add(r["email"])
    daily = [
        {
            "date": date,
            "requests": v["requests"],
            "tokens": v["tokens"],
            "spend": round(v["spend"], 4),
            "active_users": len(v["users"]),
        }
        for date, v in sorted(by_date.items())
    ]

    # Per user aggregation
    by_user = defaultdict(lambda: {"requests": 0, "tokens": 0, "prompt_tokens": 0,
                                    "completion_tokens": 0, "spend": 0.0, "active_days": set(),
                                    "keys": set()})
    for r in rows:
        u = by_user[r["email"]]
        u["requests"] += r["requests"]
        u["tokens"] += r["tokens"]
        u["prompt_tokens"] += r["prompt_tokens"]
        u["completion_tokens"] += r["completion_tokens"]
        u["spend"] += r["spend"]
        u["active_days"].add(r["date"])
        u["keys"].add(r["key_alias"])
    users = [
        {
            "email": email,
            "name": short_name(email),
            "requests": v["requests"],
            "tokens": v["tokens"],
            "prompt_tokens": v["prompt_tokens"],
            "completion_tokens": v["completion_tokens"],
            "spend": round(v["spend"], 4),
            "active_days": len(v["active_days"]),
            "keys": sorted(v["keys"]),
        }
        for email, v in by_user.items()
    ]
    users.sort(key=lambda u: u["tokens"], reverse=True)

    # By key (local vs external)
    by_key = defaultdict(lambda: {"requests": 0, "tokens": 0, "spend": 0.0, "users": set()})
    for r in rows:
        k = by_key[r["key_alias"]]
        k["requests"] += r["requests"]
        k["tokens"] += r["tokens"]
        k["spend"] += r["spend"]
        k["users"].add(r["email"])
    keys = [
        {
            "key_alias": ka,
            "requests": v["requests"],
            "tokens": v["tokens"],
            "spend": round(v["spend"], 4),
            "users": len(v["users"]),
        }
        for ka, v in by_key.items()
    ]
    keys.sort(key=lambda k: k["tokens"], reverse=True)

    print("Parsing logs...")
    logs = parse_logs(LOG_PATH)
    if logs.get("available"):
        lt = logs["totals"]
        print(f"  log samples={lt['throughput_samples']:,}  http={lt['http_total']:,}"
              f"  errors={lt['errors_timed']:,}  asgi_excs={lt['asgi_errors']:,}")
        print(f"  peak prompt={lt['peak_prompt_tps']} tok/s  peak gen={lt['peak_gen_tps']} tok/s"
              f"  peak running={lt['peak_running']}")
    else:
        print(f"  logs not found at {LOG_PATH}")

    print("Parsing GPU telemetry...")
    gpu = parse_gpu(GPU_PATH)
    if gpu.get("available"):
        gt = gpu["totals"]
        print(f"  gpu samples={gt['samples']:,} ({gt['active']:,} active / {gt['idle']:,} idle, {gt['duty_cycle']}% duty)")
        print(f"  power active avg={gt['power_total_active_avg']}W (4-GPU)  SM active avg={gt['sm_active_avg']}%  temp max={gt['temp_active_max']}C")
    else:
        print(f"  GPU log not found at {GPU_PATH}")

    # --- Energy model: per-hour energy from active fraction x GPU power levels ---
    if gpu.get("available"):
        p_active = gpu["totals"]["power_total_active_avg"] or 712.0      # 4-GPU watts when serving
        p_idle = (gpu["totals"]["power_pg_idle_avg"] or 15.0) * gpu["n_gpus"]  # 4-GPU watts idle
    else:
        p_active, p_idle = 712.0, 60.0
    if logs.get("available"):
        for s in logs["series"]:
            n = s["samples"] or 1
            af = s["samples_active"] / n
            s["active_frac"] = round(af, 4)
            s["energy_wh"] = round(af * p_active + (1 - af) * p_idle, 1)  # 1-hour bucket -> Wh
        total_wh = sum(s["energy_wh"] for s in logs["series"])
        logs["energy_total"] = {
            "kwh": round(total_wh / 1000, 1),
            "huf": round(total_wh / 1000 * ELECTRICITY_HUF_PER_KWH, 0),
            "eur": round(total_wh / 1000 * ELECTRICITY_HUF_PER_KWH / HUF_PER_EUR, 2),
        }
        print(f"  energy total={logs['energy_total']['kwh']} kWh  "
              f"= {logs['energy_total']['huf']:,.0f} Ft / {logs['energy_total']['eur']:,.2f} EUR "
              f"(active {p_active:.0f}W / idle {p_idle:.0f}W @ {ELECTRICITY_HUF_PER_KWH} Ft/kWh)")

    data = {
        "totals": totals,
        "daily": daily,
        "users": users,
        "keys": keys,
        "logs": logs,
        "gpu": gpu,
        "power": {
            "huf_per_kwh": ELECTRICITY_HUF_PER_KWH,
            "huf_per_eur": HUF_PER_EUR,
            "eur_per_kwh": round(ELECTRICITY_HUF_PER_KWH / HUF_PER_EUR, 4),
            "gpu_active_w": round(p_active, 1),
            "gpu_idle_w": round(p_idle, 1),
        },
        "calc": {
            # Infarm OPEX.xlsx (havi, 2026-05-28). Editable in the UI.
            "opex_eur": {"CPS Support": 2000.0, "AWS": 428.78, "Lenovo hosting": 89.99, "Aram (power)": 282.34},
            "fx": {"eur_huf": HUF_PER_EUR, "usd_eur": 0.8576, "usd_huf": 303.73},
            "defaults": {
                "users": totals["users"],
                "days": totals["days"],
                "tokens": totals["tokens"],
                "input_pct": round(totals["prompt_tokens"] / totals["tokens"] * 100, 1) if totals["tokens"] else 96.0,
            },
            # AWS Bedrock on-demand, us-east-1, per 1M tokens (May 2026, editable).
            "bedrock": [
                {"name": "Claude Sonnet 4.5", "pin": 3.00, "pout": 15.00, "tier": "frontier (≈ Qwen3.5-397B minoseg)"},
                {"name": "DeepSeek-R1", "pin": 1.35, "pout": 5.40, "tier": "open frontier reasoning"},
                {"name": "Amazon Nova Pro", "pin": 0.80, "pout": 3.20, "tier": "Amazon mid-tier"},
                {"name": "Llama 3.3 70B", "pin": 0.72, "pout": 0.72, "tier": "open mid (70B)"},
                {"name": "Amazon Nova Micro", "pin": 0.035, "pout": 0.14, "tier": "tiny / sok mas modell olcsobb"},
            ],
        },
        "rows": [
            {"d": r["date"], "n": short_name(r["email"]), "e": r["email"], "k": r["key_alias"],
             "rq": r["requests"], "tk": r["tokens"], "pt": r["prompt_tokens"],
             "ct": r["completion_tokens"], "sp": r["spend"]}
            for r in rows
        ],
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(CSV_PATH),
    }

    html = HTML_TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    OUT_PATH.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT_PATH}  ({OUT_PATH.stat().st_size:,} bytes)")
    print(f"  rows={totals['rows']}  users={totals['users']}  days={totals['days']}")
    print(f"  requests={totals['requests']:,}  tokens={totals['tokens']:,}  spend=${totals['spend']:.4f}")


HTML_TEMPLATE = r"""<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<title>Sonrisa AI Usage Dashboard</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<style>
  :root{
    --bg:#0b1020; --panel:#121a2e; --panel-2:#1a2440; --border:#26314f;
    --ink:#e9ecf5; --ink-dim:#9aa3bf; --accent:#7c9cff; --accent-2:#56e0c1;
    --warn:#ffb96b; --danger:#ff6b8a; --good:#56e0c1;
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0;background:var(--bg);color:var(--ink);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,sans-serif;
    font-feature-settings:"tnum" 1, "cv11" 1;}
  header{padding:28px 36px 16px;border-bottom:1px solid var(--border)}
  h1{font-size:22px;margin:0 0 4px;letter-spacing:-0.02em}
  .sub{color:var(--ink-dim);font-size:13px}
  main{padding:24px 36px 64px;max-width:1400px;margin:0 auto}
  .kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin-bottom:24px}
  .kpi{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:16px 18px}
  .kpi .label{color:var(--ink-dim);font-size:11px;text-transform:uppercase;letter-spacing:0.08em;font-weight:600}
  .kpi .value{font-size:26px;font-weight:600;margin-top:6px;letter-spacing:-0.02em}
  .kpi .delta{font-size:12px;color:var(--ink-dim);margin-top:4px}
  .grid{display:grid;grid-template-columns:2fr 1fr;gap:18px;margin-bottom:18px}
  @media (max-width:900px){.grid{grid-template-columns:1fr}}
  .card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:18px}
  .card h2{font-size:13px;font-weight:600;letter-spacing:0.04em;text-transform:uppercase;color:var(--ink-dim);margin:0 0 12px}
  .card .chart-wrap{position:relative;height:280px}
  .card-lg .chart-wrap{height:340px}
  table{width:100%;border-collapse:collapse;font-size:13px}
  th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--border)}
  th{color:var(--ink-dim);font-weight:500;font-size:11px;text-transform:uppercase;letter-spacing:0.06em;cursor:pointer;user-select:none}
  th:hover{color:var(--ink)}
  tbody tr:hover{background:var(--panel-2)}
  td.num{text-align:right;font-variant-numeric:tabular-nums}
  .pill{display:inline-block;padding:2px 8px;border-radius:999px;font-size:11px;border:1px solid var(--border);color:var(--ink-dim)}
  .pill.local{color:var(--good);border-color:rgba(86,224,193,0.3);background:rgba(86,224,193,0.08)}
  .pill.external{color:var(--warn);border-color:rgba(255,185,107,0.3);background:rgba(255,185,107,0.08)}
  footer{margin-top:36px;color:var(--ink-dim);font-size:12px;text-align:center}
  .tabs{display:flex;gap:4px;margin-bottom:12px}
  .tab{padding:6px 12px;border-radius:8px;background:transparent;border:1px solid var(--border);color:var(--ink-dim);cursor:pointer;font-size:12px}
  .tab.active{background:var(--panel-2);color:var(--ink);border-color:var(--accent)}
  .row{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
  .legend{font-size:12px;color:var(--ink-dim)}
  .legend span{display:inline-block;width:10px;height:10px;border-radius:2px;vertical-align:middle;margin-right:4px}
  nav.tabs-top{display:flex;gap:2px;padding:0 36px;border-bottom:1px solid var(--border);background:var(--bg);position:sticky;top:0;z-index:10}
  nav.tabs-top button{background:transparent;border:none;color:var(--ink-dim);padding:14px 18px;font-size:13px;font-weight:500;cursor:pointer;border-bottom:2px solid transparent;letter-spacing:-0.01em}
  nav.tabs-top button:hover{color:var(--ink)}
  nav.tabs-top button.active{color:var(--ink);border-bottom-color:var(--accent)}
  .tabpanel{display:none}
  .tabpanel.active{display:block}
  .endpoint-pill{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11px;background:var(--panel-2);padding:2px 6px;border-radius:4px}
  .status-pill{display:inline-block;padding:2px 8px;border-radius:999px;font-size:11px;font-variant-numeric:tabular-nums;font-weight:500}
  .s2{background:rgba(86,224,193,0.15);color:#56e0c1}
  .s4{background:rgba(255,185,107,0.15);color:#ffb96b}
  .s5{background:rgba(255,107,138,0.15);color:#ff6b8a}
  .filterbar{display:flex;align-items:center;gap:18px;margin-top:14px;flex-wrap:wrap}
  .winfilter{display:flex;gap:4px;background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:4px}
  .winbtn{padding:6px 16px;border-radius:7px;background:transparent;border:none;color:var(--ink-dim);cursor:pointer;font-size:13px;font-weight:600}
  .winbtn.active{background:var(--accent);color:#0b1020}
  .elecref{font-size:12px;color:var(--ink-dim)}
  .elecref strong{color:var(--accent-2)}
  .elecgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}
  .elecstat{background:var(--panel-2);border:1px solid var(--border);border-radius:10px;padding:14px 16px}
  .elecstat .label{color:var(--ink-dim);font-size:11px;text-transform:uppercase;letter-spacing:0.06em;font-weight:600}
  .elecstat .value{font-size:22px;font-weight:600;margin-top:6px;color:var(--accent-2);letter-spacing:-0.02em}
  .eleccard h2 span{color:var(--accent-2);text-transform:none;letter-spacing:0;font-weight:600}
  .elecstat .sub2{font-size:12px;color:var(--ink-dim);margin-top:3px;font-weight:500}
  .calcrow{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:7px 0;border-bottom:1px solid var(--border)}
  .calcrow span{font-size:13px;color:var(--ink-dim)}
  .calcin{width:140px;padding:6px 10px;background:var(--panel-2);border:1px solid var(--border);border-radius:6px;color:var(--ink);font-size:13px;text-align:right;font-variant-numeric:tabular-nums}
  .calcin:focus{outline:none;border-color:var(--accent)}
  .calclabel{font-size:11px;color:var(--ink-dim);text-transform:uppercase;letter-spacing:0.06em;font-weight:600;margin:10px 0 4px}
  td .tier{color:var(--ink-dim);font-size:11px;margin-top:2px}
  tr.ourrow{background:rgba(86,224,193,0.08)}
  tr.ourrow td{border-bottom:1px solid rgba(86,224,193,0.25)}
</style>
</head>
<body>
<header>
  <h1>Sonrisa AI Usage — OpenWebUI / LiteLLM</h1>
  <div class="sub" id="sub"></div>
  <div class="filterbar">
    <div class="winfilter" id="winFilter">
      <button class="winbtn" data-win="weekly">Heti</button>
      <button class="winbtn" data-win="monthly">Havi</button>
      <button class="winbtn active" data-win="all">Teljes</button>
    </div>
    <div class="elecref" id="elecRef"></div>
  </div>
</header>
<nav class="tabs-top" id="topTabs">
  <button class="active" data-panel="usage">User-használat (CSV)</button>
  <button data-panel="server">vLLM Server (logok)</button>
  <button data-panel="gpu">GPU telemetria</button>
  <button data-panel="calc">Költségkalkulátor</button>
</nav>
<main id="panel-usage" class="tabpanel active">
  <section class="kpis" id="kpis"></section>

  <div class="grid">
    <div class="card card-lg">
      <div class="row">
        <h2>Napi használat</h2>
        <div class="tabs" id="dailyTabs">
          <button class="tab active" data-metric="tokens">Tokenek</button>
          <button class="tab" data-metric="requests">Requestek</button>
          <button class="tab" data-metric="active_users">Aktív userek</button>
          <button class="tab" data-metric="spend">Költség ($)</button>
        </div>
      </div>
      <div class="chart-wrap"><canvas id="dailyChart"></canvas></div>
    </div>
    <div class="card">
      <h2>Lokális vs Külső API</h2>
      <div class="chart-wrap"><canvas id="keyChart"></canvas></div>
      <div id="keyLegend" class="legend" style="margin-top:8px"></div>
    </div>
  </div>

  <div class="grid">
    <div class="card card-lg">
      <h2>Top 15 user — tokenek</h2>
      <div class="chart-wrap"><canvas id="userChart"></canvas></div>
    </div>
    <div class="card">
      <h2>Token-szerkezet</h2>
      <div class="chart-wrap"><canvas id="tokenSplitChart"></canvas></div>
    </div>
  </div>

  <div class="card">
    <div class="row">
      <h2>User-ek teljes listája</h2>
      <input id="search" placeholder="szűrés név alapján…" style="padding:6px 10px;background:var(--panel-2);border:1px solid var(--border);border-radius:6px;color:var(--ink);font-size:13px;width:240px">
    </div>
    <div style="max-height:480px;overflow-y:auto">
      <table id="usersTable">
        <thead>
          <tr>
            <th data-key="name">User</th>
            <th data-key="requests" class="num">Requestek</th>
            <th data-key="tokens" class="num">Total tokens</th>
            <th data-key="prompt_tokens" class="num">Prompt</th>
            <th data-key="completion_tokens" class="num">Completion</th>
            <th data-key="spend" class="num">Spend ($)</th>
            <th data-key="active_days" class="num">Aktív napok</th>
            <th>Kulcs</th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>
  </div>

  <footer id="footer"></footer>
</main>

<main id="panel-server" class="tabpanel">
  <div class="card eleccard" style="margin-bottom:18px">
    <h2>⚡ Áramköltség — <span id="elecServerWin"></span></h2>
    <div class="elecgrid" id="elecServer"></div>
  </div>
  <section class="kpis" id="serverKpis"></section>

  <div class="grid">
    <div class="card card-lg">
      <div class="row">
        <h2>Throughput időben</h2>
        <div class="tabs" id="thptTabs">
          <button class="tab active" data-metric="tps">Tokens / s</button>
          <button class="tab" data-metric="reqs">Aktív requestek</button>
          <button class="tab" data-metric="cache">KV cache + Prefix hit</button>
          <button class="tab" data-metric="errors">Errors / Warnings</button>
        </div>
      </div>
      <div class="chart-wrap"><canvas id="thptChart"></canvas></div>
    </div>
    <div class="card">
      <h2>HTTP status</h2>
      <div class="chart-wrap"><canvas id="statusChart"></canvas></div>
      <div id="statusLegend" class="legend" style="margin-top:8px"></div>
    </div>
  </div>

  <div class="grid">
    <div class="card card-lg">
      <h2>Endpoint forgalom (HTTP)</h2>
      <table id="endpointsTable">
        <thead>
          <tr>
            <th>Endpoint</th>
            <th class="num">Total</th>
            <th class="num">2xx</th>
            <th class="num">4xx</th>
            <th class="num">5xx</th>
            <th class="num">Success</th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>
    <div class="card">
      <h2>Hiba-minták (non-2xx)</h2>
      <div id="errorSamples" style="font-size:12px;max-height:340px;overflow-y:auto"></div>
    </div>
  </div>

  <footer id="serverFooter"></footer>
</main>

<main id="panel-gpu" class="tabpanel">
  <div class="sub" id="gpuSub" style="margin-bottom:18px"></div>
  <div class="card eleccard" style="margin-bottom:18px">
    <h2>⚡ Áramköltség — <span id="elecGpuWin"></span></h2>
    <div class="elecgrid" id="elecGpu"></div>
  </div>
  <section class="kpis" id="gpuKpis"></section>

  <div class="grid">
    <div class="card card-lg">
      <h2>Összes fogyasztás — 4 GPU együtt (W)</h2>
      <div class="chart-wrap"><canvas id="gpuPowerTotalChart"></canvas></div>
    </div>
    <div class="card">
      <h2>Throughput-emlékeztető (log)</h2>
      <div id="gpuThptNote" style="font-size:13px;line-height:1.7"></div>
    </div>
  </div>

  <div class="grid">
    <div class="card card-lg">
      <h2>Fogyasztás GPU-nként (W)</h2>
      <div class="chart-wrap"><canvas id="gpuPowerPerChart"></canvas></div>
    </div>
    <div class="card">
      <h2>Hőmérséklet GPU-nként (°C)</h2>
      <div class="chart-wrap"><canvas id="gpuTempChart"></canvas></div>
    </div>
  </div>

  <div class="grid">
    <div class="card card-lg">
      <div class="row">
        <h2>Kihasználtság időben</h2>
        <div class="tabs" id="gpuUtilTabs">
          <button class="tab active" data-metric="sm">SM compute (%)</button>
          <button class="tab" data-metric="mem">Memory bandwidth (%)</button>
          <button class="tab" data-metric="pcie">PCIe (MB/s)</button>
          <button class="tab" data-metric="temp">Max temp (°C)</button>
        </div>
      </div>
      <div class="chart-wrap"><canvas id="gpuUtilChart"></canvas></div>
    </div>
    <div class="card">
      <h2>SM kihasználtság megoszlás</h2>
      <div class="chart-wrap"><canvas id="gpuSmHistChart"></canvas></div>
    </div>
  </div>

  <footer id="gpuFooter"></footer>
</main>

<main id="panel-calc" class="tabpanel">
  <div class="sub" id="calcSub" style="margin-bottom:18px"></div>
  <div class="grid">
    <div class="card">
      <h2>Bemenetek (szerkeszthető)</h2>
      <div id="calcInputs"></div>
    </div>
    <div class="card eleccard">
      <h2>⚙️ Saját költség — Inference Farm</h2>
      <div class="elecgrid" id="calcOurs"></div>
    </div>
  </div>

  <div class="card">
    <h2>Összehasonlítás — AWS Bedrock (azonos token-volumen, <span id="calcSplitLabel"></span>)</h2>
    <table id="calcTable">
      <thead><tr>
        <th>Modell</th>
        <th class="num">Időszak (EUR)</th>
        <th class="num">Időszak (HUF)</th>
        <th class="num">/ 1M token (EUR)</th>
        <th class="num">vs saját</th>
      </tr></thead>
      <tbody></tbody>
    </table>
    <div style="font-size:12px;color:var(--ink-dim);margin-top:10px" id="calcNote"></div>
  </div>

  <div class="card card-lg">
    <h2>Költség / 1M token — saját vs Bedrock</h2>
    <div class="chart-wrap"><canvas id="calcChart"></canvas></div>
  </div>

  <footer id="calcFooter"></footer>
</main>

<script>
const DATA = __DATA__;

// ===== Global time-window filter (Heti / Havi / Teljes) — reload-based =====
// Mutates DATA in place BEFORE rendering, so every chart/KPI reflects the window.
const WINDOW = (location.hash.replace('#','') || 'all');
const WIN_LABEL = {weekly:'utolsó 7 nap', monthly:'utolsó 30 nap', all:'teljes időszak'};
(function applyWindow(){
  if(WINDOW === 'all') return;
  const latest = DATA.totals.date_max;
  const days = WINDOW === 'weekly' ? 6 : 29;
  const d = new Date(latest + 'T00:00:00Z'); d.setUTCDate(d.getUTCDate() - days);
  const cut = d.toISOString().slice(0,10);
  const inWin = s => s >= cut;

  if(DATA.rows){
    const rows = DATA.rows.filter(r => inWin(r.d));
    const bd={}, bu={}, bk={};
    let rq=0,tk=0,pt=0,ct=0,sp=0; const us=new Set();
    for(const r of rows){
      rq+=r.rq;tk+=r.tk;pt+=r.pt;ct+=r.ct;sp+=r.sp;us.add(r.e);
      (bd[r.d]=bd[r.d]||{requests:0,tokens:0,spend:0,u:new Set()}); bd[r.d].requests+=r.rq;bd[r.d].tokens+=r.tk;bd[r.d].spend+=r.sp;bd[r.d].u.add(r.e);
      (bu[r.e]=bu[r.e]||{email:r.e,name:r.n,requests:0,tokens:0,prompt_tokens:0,completion_tokens:0,spend:0,d:new Set(),k:new Set()});
      const u=bu[r.e]; u.requests+=r.rq;u.tokens+=r.tk;u.prompt_tokens+=r.pt;u.completion_tokens+=r.ct;u.spend+=r.sp;u.d.add(r.d);u.k.add(r.k);
      (bk[r.k]=bk[r.k]||{key_alias:r.k,requests:0,tokens:0,spend:0,u:new Set()}); bk[r.k].requests+=r.rq;bk[r.k].tokens+=r.tk;bk[r.k].spend+=r.sp;bk[r.k].u.add(r.e);
    }
    const dates = rows.map(r=>r.d).sort();
    DATA.daily = Object.entries(bd).sort().map(([dd,v])=>({date:dd,requests:v.requests,tokens:v.tokens,spend:Math.round(v.spend*10000)/10000,active_users:v.u.size}));
    DATA.users = Object.values(bu).map(u=>({name:u.name,email:u.email,requests:u.requests,tokens:u.tokens,prompt_tokens:u.prompt_tokens,completion_tokens:u.completion_tokens,spend:Math.round(u.spend*10000)/10000,active_days:u.d.size,keys:[...u.k].sort()})).sort((a,b)=>b.tokens-a.tokens);
    DATA.keys = Object.values(bk).map(k=>({key_alias:k.key_alias,requests:k.requests,tokens:k.tokens,spend:Math.round(k.spend*10000)/10000,users:k.u.size})).sort((a,b)=>b.tokens-a.tokens);
    DATA.totals = Object.assign({}, DATA.totals, {requests:rq,tokens:tk,prompt_tokens:pt,completion_tokens:ct,spend:Math.round(sp*10000)/10000,users:us.size,days:DATA.daily.length,rows:rows.length,failed:0,date_min:dates[0]||DATA.totals.date_min,date_max:dates[dates.length-1]||DATA.totals.date_max});
  }

  if(DATA.logs && DATA.logs.available){
    const fs = DATA.logs.series.filter(s => inWin(s.bucket.slice(0,10)));
    DATA.logs.series = fs;
    const t = DATA.logs.totals;
    t.throughput_samples = fs.reduce((a,s)=>a+s.samples,0);
    t.hours_active = fs.length;
    t.errors_timed = fs.reduce((a,s)=>a+s.errors,0);
    t.warnings_timed = fs.reduce((a,s)=>a+s.warnings,0);
    t.peak_gen_tps = fs.reduce((a,s)=>Math.max(a,s.gen_tps_max),0);
    t.peak_prompt_tps = fs.reduce((a,s)=>Math.max(a,s.prompt_tps_max),0);
    t.peak_running = fs.reduce((a,s)=>Math.max(a,s.running_max),0);
    DATA.logs.ts_min = fs.length ? fs[0].bucket : DATA.logs.ts_min;
    DATA.logs.ts_max = fs.length ? fs[fs.length-1].bucket : DATA.logs.ts_max;
  }
})();

const fmt = new Intl.NumberFormat("hu-HU");
const fmtUSD = n => "$" + (Math.round(n*10000)/10000).toLocaleString("en-US",{minimumFractionDigits:n<1?4:2,maximumFractionDigits:4});
const fmtCompact = new Intl.NumberFormat("en-US",{notation:"compact",maximumFractionDigits:1});

Chart.defaults.color = "#9aa3bf";
Chart.defaults.borderColor = "#26314f";
Chart.defaults.font.family = "-apple-system,BlinkMacSystemFont,Segoe UI,Inter,Roboto,sans-serif";

// Subtitle
document.getElementById("sub").textContent =
  `${DATA.totals.date_min} → ${DATA.totals.date_max} · ${DATA.totals.days} nap · ${DATA.totals.users} user · ${DATA.totals.rows.toLocaleString("hu-HU")} sor`;

// KPIs
const kpis = [
  {label:"Total requests", value:fmt.format(DATA.totals.requests)},
  {label:"Total tokens", value:fmtCompact.format(DATA.totals.tokens)},
  {label:"Prompt tokens", value:fmtCompact.format(DATA.totals.prompt_tokens)},
  {label:"Completion tokens", value:fmtCompact.format(DATA.totals.completion_tokens)},
  {label:"Total spend", value:fmtUSD(DATA.totals.spend)},
  {label:"Aktív userek", value:fmt.format(DATA.totals.users)},
  {label:"Lefedett napok", value:fmt.format(DATA.totals.days)},
  {label:"Failed requests", value:fmt.format(DATA.totals.failed)},
];
document.getElementById("kpis").innerHTML = kpis.map(k =>
  `<div class="kpi"><div class="label">${k.label}</div><div class="value">${k.value}</div></div>`
).join("");

// Daily chart
const dailyCtx = document.getElementById("dailyChart").getContext("2d");
const dailyLabels = DATA.daily.map(d=>d.date);
let dailyChart;

function drawDaily(metric){
  const values = DATA.daily.map(d=>d[metric]);
  const grad = dailyCtx.createLinearGradient(0,0,0,300);
  grad.addColorStop(0,"rgba(124,156,255,0.45)");
  grad.addColorStop(1,"rgba(124,156,255,0.02)");
  if(dailyChart) dailyChart.destroy();
  dailyChart = new Chart(dailyCtx, {
    type:"line",
    data:{labels:dailyLabels, datasets:[{
      label:metric, data:values, borderColor:"#7c9cff",
      backgroundColor:grad, fill:true, tension:0.3,
      pointRadius:0, pointHoverRadius:5, borderWidth:2,
    }]},
    options:{
      responsive:true, maintainAspectRatio:false,
      plugins:{legend:{display:false},
        tooltip:{callbacks:{label: ctx => {
          const v = ctx.parsed.y;
          if(metric==="spend") return fmtUSD(v);
          return fmt.format(v);
        }}}},
      scales:{
        x:{grid:{display:false},ticks:{maxTicksLimit:12, autoSkip:true}},
        y:{grid:{color:"rgba(38,49,79,0.5)"},ticks:{callback:v => fmtCompact.format(v)}}
      }
    }
  });
}
drawDaily("tokens");
document.querySelectorAll("#dailyTabs .tab").forEach(btn=>{
  btn.addEventListener("click",()=>{
    document.querySelectorAll("#dailyTabs .tab").forEach(b=>b.classList.remove("active"));
    btn.classList.add("active");
    drawDaily(btn.dataset.metric);
  });
});

// Key chart (local vs external) — doughnut
const keyCtx = document.getElementById("keyChart").getContext("2d");
new Chart(keyCtx, {
  type:"doughnut",
  data:{
    labels:DATA.keys.map(k=>k.key_alias),
    datasets:[{
      data:DATA.keys.map(k=>k.tokens),
      backgroundColor:["#56e0c1","#ffb96b","#7c9cff"],
      borderColor:"#121a2e", borderWidth:2,
    }]
  },
  options:{
    responsive:true, maintainAspectRatio:false, cutout:"65%",
    plugins:{
      legend:{position:"bottom", labels:{boxWidth:10}},
      tooltip:{callbacks:{label:ctx => `${ctx.label}: ${fmtCompact.format(ctx.parsed)} tok`}}
    }
  }
});
document.getElementById("keyLegend").innerHTML = DATA.keys.map(k =>
  `<div style="margin-top:4px"><strong>${k.key_alias}</strong> — ${fmt.format(k.requests)} req · ${fmtCompact.format(k.tokens)} tok · ${fmtUSD(k.spend)} · ${k.users} user</div>`
).join("");

// Top users bar chart
const topUsers = DATA.users.slice(0,15);
new Chart(document.getElementById("userChart").getContext("2d"), {
  type:"bar",
  data:{
    labels:topUsers.map(u=>u.name),
    datasets:[{
      label:"Total tokens",
      data:topUsers.map(u=>u.tokens),
      backgroundColor:"#7c9cff",
      borderRadius:4,
    }]
  },
  options:{
    indexAxis:"y", responsive:true, maintainAspectRatio:false,
    plugins:{legend:{display:false},
      tooltip:{callbacks:{label:ctx => fmt.format(ctx.parsed.x) + " tokens"}}},
    scales:{
      x:{grid:{color:"rgba(38,49,79,0.5)"},ticks:{callback:v=>fmtCompact.format(v)}},
      y:{grid:{display:false}}
    }
  }
});

// Token split
new Chart(document.getElementById("tokenSplitChart").getContext("2d"), {
  type:"doughnut",
  data:{
    labels:["Prompt", "Completion"],
    datasets:[{
      data:[DATA.totals.prompt_tokens, DATA.totals.completion_tokens],
      backgroundColor:["#7c9cff","#56e0c1"],
      borderColor:"#121a2e", borderWidth:2,
    }]
  },
  options:{
    responsive:true, maintainAspectRatio:false, cutout:"65%",
    plugins:{
      legend:{position:"bottom", labels:{boxWidth:10}},
      tooltip:{callbacks:{label:ctx => `${ctx.label}: ${fmtCompact.format(ctx.parsed)} (${(ctx.parsed/DATA.totals.tokens*100).toFixed(1)}%)`}}
    }
  }
});

// Users table
let sortKey = "tokens", sortDir = -1;
function renderUsers(){
  const q = document.getElementById("search").value.toLowerCase();
  const rows = DATA.users
    .filter(u => !q || u.name.toLowerCase().includes(q) || u.email.toLowerCase().includes(q))
    .slice()
    .sort((a,b)=>{
      const va=a[sortKey], vb=b[sortKey];
      if(typeof va==="string") return sortDir * va.localeCompare(vb);
      return sortDir * (va - vb);
    });
  const tbody = document.querySelector("#usersTable tbody");
  tbody.innerHTML = rows.map(u => `
    <tr>
      <td>${u.name}<div style="color:var(--ink-dim);font-size:11px">${u.email}</div></td>
      <td class="num">${fmt.format(u.requests)}</td>
      <td class="num">${fmt.format(u.tokens)}</td>
      <td class="num">${fmt.format(u.prompt_tokens)}</td>
      <td class="num">${fmt.format(u.completion_tokens)}</td>
      <td class="num">${u.spend > 0 ? fmtUSD(u.spend) : "—"}</td>
      <td class="num">${u.active_days}</td>
      <td>${u.keys.map(k => `<span class="pill ${k.includes('external')?'external':'local'}">${k.replace('open-webui-','')}</span>`).join(" ")}</td>
    </tr>
  `).join("");
}
document.querySelectorAll("#usersTable th").forEach(th=>{
  th.addEventListener("click",()=>{
    const k = th.dataset.key;
    if(!k) return;
    if(sortKey===k) sortDir = -sortDir; else { sortKey=k; sortDir=-1; }
    renderUsers();
  });
});
document.getElementById("search").addEventListener("input", renderUsers);
renderUsers();

document.getElementById("footer").textContent =
  `Generálva: ${DATA.generated_at} · Forrás: ${DATA.source}`;

// =============== Top-level tabs ===============
document.querySelectorAll("#topTabs button").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll("#topTabs button").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".tabpanel").forEach(p => p.classList.remove("active"));
    btn.classList.add("active");
    document.getElementById("panel-" + btn.dataset.panel).classList.add("active");
    // Resize charts that were hidden (Chart.js needs explicit resize after display:none toggle)
    setTimeout(() => Object.values(Chart.instances || {}).forEach(c => c.resize && c.resize()), 50);
  });
});

// =============== Server / Logs tab ===============
const L = DATA.logs;
if (L && L.available) {
  const lt = L.totals;
  const fmtPct = n => (n||0).toFixed(1) + "%";
  const serverKpis = [
    {label:"Throughput minták", value:fmt.format(lt.throughput_samples)},
    {label:"Aktív órák", value:fmt.format(lt.hours_active)},
    {label:"HTTP requests", value:fmt.format(lt.http_total)},
    {label:"Success rate", value:fmtPct(lt.success_rate)},
    {label:"HTTP 4xx", value:fmt.format(lt.http_4xx)},
    {label:"HTTP 5xx", value:fmt.format(lt.http_5xx)},
    {label:"Module errors", value:fmt.format(lt.errors_timed)},
    {label:"ASGI exceptions", value:fmt.format(lt.asgi_errors)},
    {label:"Warnings", value:fmt.format(lt.warnings_timed)},
    {label:"Peak prompt tok/s", value:fmt.format(Math.round(lt.peak_prompt_tps))},
    {label:"Peak generation tok/s", value:fmt.format(Math.round(lt.peak_gen_tps))},
    {label:"Peak concurrent reqs", value:fmt.format(lt.peak_running)},
  ];
  document.getElementById("serverKpis").innerHTML = serverKpis.map(k =>
    `<div class="kpi"><div class="label">${k.label}</div><div class="value">${k.value}</div></div>`
  ).join("");

  const series = L.series;
  const labels = series.map(s => s.bucket.replace(`${new Date().getFullYear()}-`, ""));

  const thptCtx = document.getElementById("thptChart").getContext("2d");
  let thptChart;

  function drawThpt(metric){
    if(thptChart) thptChart.destroy();
    let datasets, yScale = {};
    if(metric === "tps"){
      datasets = [
        {label:"Prompt avg tok/s", data:series.map(s=>s.prompt_tps_avg), borderColor:"#7c9cff", backgroundColor:"rgba(124,156,255,0.15)", fill:true, tension:0.3, pointRadius:0, borderWidth:2},
        {label:"Generation avg tok/s", data:series.map(s=>s.gen_tps_avg), borderColor:"#56e0c1", backgroundColor:"rgba(86,224,193,0.10)", fill:true, tension:0.3, pointRadius:0, borderWidth:2},
      ];
    } else if(metric === "reqs"){
      datasets = [
        {label:"Running avg", data:series.map(s=>s.running_avg), borderColor:"#7c9cff", backgroundColor:"rgba(124,156,255,0.2)", fill:true, tension:0.3, pointRadius:0, borderWidth:2},
        {label:"Waiting avg", data:series.map(s=>s.waiting_avg), borderColor:"#ffb96b", backgroundColor:"rgba(255,185,107,0.2)", fill:true, tension:0.3, pointRadius:0, borderWidth:2},
        {label:"Running max", data:series.map(s=>s.running_max), borderColor:"#ff6b8a", borderDash:[3,3], fill:false, tension:0.3, pointRadius:0, borderWidth:1},
      ];
    } else if(metric === "cache"){
      datasets = [
        {label:"GPU KV cache %", data:series.map(s=>s.kv_avg), borderColor:"#7c9cff", backgroundColor:"rgba(124,156,255,0.15)", fill:true, tension:0.3, pointRadius:0, borderWidth:2},
        {label:"Prefix cache hit %", data:series.map(s=>s.prefix_avg), borderColor:"#56e0c1", fill:false, tension:0.3, pointRadius:0, borderWidth:2},
      ];
      yScale = {y:{min:0, max:100, ticks:{callback:v=>v+"%"}, grid:{color:"rgba(38,49,79,0.5)"}}};
    } else { // errors
      datasets = [
        {label:"Errors", data:series.map(s=>s.errors), backgroundColor:"#ff6b8a", borderColor:"#ff6b8a", borderWidth:1, type:"bar"},
        {label:"Warnings", data:series.map(s=>s.warnings), backgroundColor:"#ffb96b", borderColor:"#ffb96b", borderWidth:1, type:"bar"},
      ];
    }
    thptChart = new Chart(thptCtx, {
      type:"line",
      data:{labels, datasets},
      options:{
        responsive:true, maintainAspectRatio:false,
        interaction:{mode:"index", intersect:false},
        plugins:{legend:{position:"top", labels:{boxWidth:10, font:{size:11}}}},
        scales:Object.assign({
          x:{grid:{display:false}, ticks:{maxTicksLimit:14, autoSkip:true, font:{size:10}}},
          y:{grid:{color:"rgba(38,49,79,0.5)"}, ticks:{callback:v=>fmtCompact.format(v)}, beginAtZero:true}
        }, yScale)
      }
    });
  }
  drawThpt("tps");
  document.querySelectorAll("#thptTabs .tab").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("#thptTabs .tab").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      drawThpt(btn.dataset.metric);
    });
  });

  // Status doughnut
  const statusLabels = Object.keys(L.status_count).sort();
  const statusColors = statusLabels.map(s => s.startsWith("2") ? "#56e0c1" : s.startsWith("4") ? "#ffb96b" : s.startsWith("5") ? "#ff6b8a" : "#7c9cff");
  new Chart(document.getElementById("statusChart").getContext("2d"), {
    type:"doughnut",
    data:{
      labels:statusLabels,
      datasets:[{
        data:statusLabels.map(s=>L.status_count[s]),
        backgroundColor:statusColors,
        borderColor:"#121a2e", borderWidth:2,
      }]
    },
    options:{
      responsive:true, maintainAspectRatio:false, cutout:"60%",
      plugins:{
        legend:{position:"bottom", labels:{boxWidth:10}},
        tooltip:{callbacks:{label:ctx => `HTTP ${ctx.label}: ${fmt.format(ctx.parsed)}`}}
      }
    }
  });
  document.getElementById("statusLegend").innerHTML = statusLabels.map(s => {
    const cls = s.startsWith("2") ? "s2" : s.startsWith("4") ? "s4" : "s5";
    return `<span class="status-pill ${cls}">${s}</span> ${fmt.format(L.status_count[s])}`;
  }).join("  ");

  // Endpoints table
  const tbody = document.querySelector("#endpointsTable tbody");
  tbody.innerHTML = L.endpoints.slice(0, 30).map(e => `
    <tr>
      <td><span class="endpoint-pill">${e.endpoint}</span></td>
      <td class="num">${fmt.format(e.total)}</td>
      <td class="num"><span class="status-pill s2">${fmt.format(e.ok)}</span></td>
      <td class="num">${e.client_err ? `<span class="status-pill s4">${fmt.format(e.client_err)}</span>` : "—"}</td>
      <td class="num">${e.server_err ? `<span class="status-pill s5">${fmt.format(e.server_err)}</span>` : "—"}</td>
      <td class="num">${e.success_rate.toFixed(1)}%</td>
    </tr>
  `).join("");

  // Error samples
  const errs = L.sample_http_errors;
  if(errs.length === 0){
    document.getElementById("errorSamples").innerHTML = '<div style="color:var(--ink-dim);padding:12px">Nincs rögzített non-2xx mintakérés.</div>';
  } else {
    document.getElementById("errorSamples").innerHTML = errs.map(e => {
      const cls = e.status.startsWith("4") ? "s4" : "s5";
      return `<div style="padding:6px 0;border-bottom:1px solid var(--border)"><span class="status-pill ${cls}">${e.status}</span> <span style="font-family:ui-monospace,monospace;font-size:11px">${e.method} ${e.endpoint}</span></div>`;
    }).join("");
  }

  document.getElementById("serverFooter").textContent =
    `Log időszak: ${L.ts_min} → ${L.ts_max} · ${(L.file_size/1024/1024).toFixed(1)} MB · Forrás: ${L.source}`;
} else {
  document.getElementById("serverKpis").innerHTML =
    '<div style="color:var(--ink-dim);padding:20px">Nincs log fájl betöltve.</div>';
}

// =============== GPU telemetry tab ===============
const G = DATA.gpu;
if (G && G.available) {
  const gt = G.totals;
  document.getElementById("gpuSub").textContent =
    `nvidia-smi dmon · ${G.n_gpus}× GPU · ${fmt.format(gt.samples)} minta (~${G.interval_s}s/minta, ~${(gt.samples*G.interval_s/3600).toFixed(1)} óra ablak) · ${gt.duty_cycle}% aktív duty cycle`;

  const gpuKpis = [
    {label:"GPU-k", value:G.n_gpus + "×"},
    {label:"Minták", value:fmt.format(gt.samples)},
    {label:"Aktív duty cycle", value:gt.duty_cycle + "%"},
    {label:"Fogyasztás aktív (4 GPU)", value:Math.round(gt.power_total_active_avg)+" W"},
    {label:"Csúcs fogyasztás (4 GPU)", value:Math.round(gt.power_total_active_max)+" W"},
    {label:"SM util aktív (átlag)", value:gt.sm_active_avg+"%"},
    {label:"SM util P95", value:gt.sm_active_p95+"%"},
    {label:"Mem-BW util aktív", value:gt.mem_active_avg+"%"},
    {label:"Hőmérséklet max", value:gt.temp_active_max+"°C"},
    {label:"Idle fogyasztás/GPU", value:Math.round(gt.power_pg_idle_avg)+" W"},
  ];
  document.getElementById("gpuKpis").innerHTML = gpuKpis.map(k =>
    `<div class="kpi"><div class="label">${k.label}</div><div class="value">${k.value}</div></div>`
  ).join("");

  const GCOLORS = ["#7c9cff","#56e0c1","#ffb96b","#ff6b8a","#b388ff","#4dd0e1"];
  const gpuBaseOpts = (yOpts) => ({
    responsive:true, maintainAspectRatio:false,
    interaction:{mode:"index", intersect:false},
    plugins:{legend:{position:"top", labels:{boxWidth:10, font:{size:11}}},
      tooltip:{callbacks:{title: items => "Perc: " + (items[0] ? items[0].label : "")}}},
    scales:{
      x:{grid:{display:false}, title:{display:true, text:"eltelt perc", color:"#9aa3bf", font:{size:10}}, ticks:{maxTicksLimit:14, autoSkip:true, font:{size:10}}},
      y:Object.assign({grid:{color:"rgba(38,49,79,0.5)"}, beginAtZero:true}, yOpts || {})
    }
  });

  // Total power (4 GPU)
  new Chart(document.getElementById("gpuPowerTotalChart").getContext("2d"), {
    type:"line",
    data:{labels:G.labels, datasets:[{label:"4-GPU total (W)", data:G.power_total, borderColor:"#ffb96b", backgroundColor:"rgba(255,185,107,0.15)", fill:true, tension:0.25, pointRadius:0, borderWidth:2}]},
    options:gpuBaseOpts({ticks:{callback:v=>v+" W"}})
  });

  // Per-GPU power
  new Chart(document.getElementById("gpuPowerPerChart").getContext("2d"), {
    type:"line",
    data:{labels:G.labels, datasets:G.per_gpu_power.map((arr,i)=>({label:"GPU "+i, data:arr, borderColor:GCOLORS[i%GCOLORS.length], fill:false, tension:0.25, pointRadius:0, borderWidth:1.5, spanGaps:true}))},
    options:gpuBaseOpts({ticks:{callback:v=>v+" W"}})
  });

  // Per-GPU temperature
  new Chart(document.getElementById("gpuTempChart").getContext("2d"), {
    type:"line",
    data:{labels:G.labels, datasets:G.per_gpu_temp.map((arr,i)=>({label:"GPU "+i, data:arr, borderColor:GCOLORS[i%GCOLORS.length], fill:false, tension:0.25, pointRadius:0, borderWidth:1.5, spanGaps:true}))},
    options:gpuBaseOpts({ticks:{callback:v=>v+"°C"}})
  });

  // Utilization-over-time with tabs
  const gpuUtilCtx = document.getElementById("gpuUtilChart").getContext("2d");
  let gpuUtilChart;
  function drawGpuUtil(metric){
    if(gpuUtilChart) gpuUtilChart.destroy();
    let d, yOpts;
    if(metric==="sm"){ d={label:"SM compute (avg %)", data:G.sm_avg, borderColor:"#7c9cff", backgroundColor:"rgba(124,156,255,0.15)"}; yOpts={max:100, ticks:{callback:v=>v+"%"}}; }
    else if(metric==="mem"){ d={label:"Memory bandwidth (avg %)", data:G.mem_avg, borderColor:"#56e0c1", backgroundColor:"rgba(86,224,193,0.12)"}; yOpts={max:100, ticks:{callback:v=>v+"%"}}; }
    else if(metric==="pcie"){ d={label:"PCIe rx+tx (MB/s)", data:G.pcie, borderColor:"#b388ff", backgroundColor:"rgba(179,136,255,0.12)"}; yOpts={ticks:{callback:v=>fmtCompact.format(v)}}; }
    else { d={label:"Max temp (°C)", data:G.temp_max, borderColor:"#ff6b8a", backgroundColor:"rgba(255,107,138,0.12)"}; yOpts={ticks:{callback:v=>v+"°C"}}; }
    gpuUtilChart = new Chart(gpuUtilCtx, {type:"line",
      data:{labels:G.labels, datasets:[Object.assign({fill:true, tension:0.25, pointRadius:0, borderWidth:2}, d)]},
      options:gpuBaseOpts(yOpts)});
  }
  drawGpuUtil("sm");
  document.querySelectorAll("#gpuUtilTabs .tab").forEach(btn=>{
    btn.addEventListener("click",()=>{
      document.querySelectorAll("#gpuUtilTabs .tab").forEach(b=>b.classList.remove("active"));
      btn.classList.add("active");
      drawGpuUtil(btn.dataset.metric);
    });
  });

  // SM utilization distribution
  const smB = [0,0,0,0,0,0];
  const smL = ["0% (idle)","1-20%","21-40%","41-60%","61-80%","81-100%"];
  G.sm_avg.forEach(v=>{ if(v<=0)smB[0]++; else if(v<=20)smB[1]++; else if(v<=40)smB[2]++; else if(v<=60)smB[3]++; else if(v<=80)smB[4]++; else smB[5]++; });
  new Chart(document.getElementById("gpuSmHistChart").getContext("2d"), {
    type:"bar",
    data:{labels:smL, datasets:[{label:"Minták", data:smB, backgroundColor:"#7c9cff", borderRadius:4}]},
    options:{responsive:true, maintainAspectRatio:false, plugins:{legend:{display:false}},
      scales:{x:{grid:{display:false}, ticks:{font:{size:10}}}, y:{grid:{color:"rgba(38,49,79,0.5)"}, beginAtZero:true}}}
  });

  // Throughput reminder — ties GPU usage to token throughput + capacity
  if (L && L.available) {
    const lt = L.totals;
    document.getElementById("gpuThptNote").innerHTML =
      `<div style="color:var(--ink-dim);margin-bottom:8px">Token-throughput a vLLM logból (Server fül):</div>
       <div>Peak generation: <strong>${fmt.format(Math.round(lt.peak_gen_tps))}</strong> tok/s</div>
       <div>Peak prompt: <strong>${fmt.format(Math.round(lt.peak_prompt_tps))}</strong> tok/s</div>
       <div>Peak concurrent: <strong>${lt.peak_running}</strong> / 32 slot</div>
       <div style="margin-top:10px;color:var(--ink-dim);line-height:1.6">GPU ~${gt.duty_cycle}% idő aktív; SM P95 ${gt.sm_active_p95}% (compute-kötött), de mem-BW csak ${gt.mem_active_avg}%. Bőven van fejlődési tér. Kapacitás-elemzés: <em>knowledge-base/08_capacity-analysis.md</em></div>`;
  }

  document.getElementById("gpuFooter").textContent =
    `Forrás: ${G.source} · ${G.n_gpus}× GPU · ~${G.interval_s}s mintavételezés`;
} else {
  document.getElementById("gpuKpis").innerHTML =
    '<div style="color:var(--ink-dim);padding:20px">Nincs GPU telemetria betöltve.</div>';
}

// ===== Electricity cost (HUF + EUR) — reflects the active window =====
(function(){
  const P = DATA.power || {huf_per_kwh:150, eur_per_kwh:0.4235, huf_per_eur:354.18, gpu_active_w:712, gpu_idle_w:60};
  const fmtHUF = n => fmt.format(Math.round(n)) + " Ft";
  const fmtEUR = n => "€" + (Math.round(n*100)/100).toLocaleString("hu-HU",{minimumFractionDigits:2,maximumFractionDigits:2});
  let kwh = 0, days = 0;
  if(DATA.logs && DATA.logs.available){
    kwh = DATA.logs.series.reduce((a,s)=>a+(s.energy_wh||0),0)/1000;
    days = new Set(DATA.logs.series.map(s=>s.bucket.slice(0,10))).size;
  }
  const huf = kwh*P.huf_per_kwh, eur = kwh*P.eur_per_kwh, dd = days||1;
  const grid = `
    <div class="elecstat"><div class="label">Energia · ${WIN_LABEL[WINDOW]}</div><div class="value">${fmt.format(Math.round(kwh))} kWh</div></div>
    <div class="elecstat"><div class="label">Áramköltség (HUF)</div><div class="value">${fmtHUF(huf)}</div></div>
    <div class="elecstat"><div class="label">Áramköltség (EUR)</div><div class="value">${fmtEUR(eur)}</div></div>
    <div class="elecstat"><div class="label">Napi átlag</div><div class="value">${fmtHUF(huf/dd)}</div></div>
    <div class="elecstat"><div class="label">Havi vetítés (30 nap)</div><div class="value">${fmtHUF(huf/dd*30)}<div style="font-size:12px;color:var(--ink-dim);margin-top:3px">${fmtEUR(eur/dd*30)}</div></div></div>`;
  ["elecServer","elecGpu"].forEach(id=>{const el=document.getElementById(id); if(el) el.innerHTML=grid;});
  ["elecServerWin","elecGpuWin"].forEach(id=>{const el=document.getElementById(id); if(el) el.textContent=WIN_LABEL[WINDOW];});
  const ref=document.getElementById("elecRef");
  if(ref) ref.innerHTML = `⚡ Áram: <strong>${fmt.format(P.huf_per_kwh)} Ft/kWh</strong> (1500 Ft / 10 kWh) ≈ <strong>${fmtEUR(P.eur_per_kwh)}/kWh</strong> · alap: ${Math.round(P.gpu_active_w)} W aktív / ${Math.round(P.gpu_idle_w)} W idle (4 GPU) × aktív óraarány`;
  const sub=document.getElementById("sub");
  if(sub) sub.textContent += " · " + WIN_LABEL[WINDOW];
  // filter buttons -> set hash + reload
  document.querySelectorAll("#winFilter .winbtn").forEach(b=>{
    if(b.dataset.win === WINDOW) b.classList.add("active"); else b.classList.remove("active");
    b.addEventListener("click", ()=>{ location.hash = b.dataset.win; location.reload(); });
  });
})();

// ===== Cost calculator (saját OPEX vs AWS Bedrock) =====
(function(){
  const C = DATA.calc; if(!C) return;
  const fmtHUF = n => fmt.format(Math.round(n)) + " Ft";
  const fmtEUR = n => "€" + (Math.round(n*100)/100).toLocaleString("hu-HU",{minimumFractionDigits:2,maximumFractionDigits:2});
  const fmtEUR4 = n => "€" + (Math.round(n*10000)/10000).toLocaleString("hu-HU",{minimumFractionDigits:2,maximumFractionDigits:4});
  const eur2huf = C.fx.eur_huf, usd2eur = C.fx.usd_eur, usd2huf = C.fx.usd_huf;
  const D = C.defaults;

  document.getElementById("calcSub").textContent =
    `Alapértékek a statisztikából: ${fmt.format(D.users)} user · ${fmt.format(D.days)} nap · ${(D.tokens/1e9).toFixed(2)} Mrd token. Minden mező szerkeszthető. (Független a felső idő-szűrőtől.)`;

  const opexItems = Object.entries(C.opex_eur);
  document.getElementById("calcInputs").innerHTML =
    `<div class="calclabel">OPEX tételek (EUR / hó)</div>` +
    opexItems.map(([k,v],i)=>`<div class="calcrow"><span>${k}</span><input type="number" class="calcin opex" data-i="${i}" value="${v}" step="1"></div>`).join("") +
    `<div class="calclabel">Használat</div>` +
    `<div class="calcrow"><span>Időszak (nap)</span><input type="number" id="ci_days" class="calcin" value="${D.days}"></div>` +
    `<div class="calcrow"><span>Userek száma</span><input type="number" id="ci_users" class="calcin" value="${D.users}"></div>` +
    `<div class="calcrow"><span>Összes token (millió)</span><input type="number" id="ci_tokens" class="calcin" value="${Math.round(D.tokens/1e6)}"></div>` +
    `<div class="calcrow"><span>Input token arány (%)</span><input type="number" id="ci_inpct" class="calcin" value="${D.input_pct}" min="0" max="100"></div>`;

  function read(){
    const opex = [...document.querySelectorAll(".calcin.opex")].reduce((a,el)=>a+(parseFloat(el.value)||0),0);
    return {
      opexMonthEUR: opex,
      days: Math.max(0.01, parseFloat(document.getElementById("ci_days").value)||1),
      users: Math.max(1, parseFloat(document.getElementById("ci_users").value)||1),
      tokM: Math.max(0, (parseFloat(document.getElementById("ci_tokens").value)||0)),
      inpct: Math.min(1, Math.max(0, (parseFloat(document.getElementById("ci_inpct").value)||0)/100)),
    };
  }

  let calcChart;
  function recompute(){
    const x = read();
    const months = x.days/30;
    const ourPeriodEUR = x.opexMonthEUR*months;
    const our1M = x.tokM>0 ? ourPeriodEUR/x.tokM : 0;
    const ourUserMonthEUR = x.opexMonthEUR/x.users;

    document.getElementById("calcOurs").innerHTML = `
      <div class="elecstat"><div class="label">Időszak költsége (${Math.round(x.days)} nap)</div><div class="value">${fmtEUR(ourPeriodEUR)}<div class="sub2">${fmtHUF(ourPeriodEUR*eur2huf)}</div></div></div>
      <div class="elecstat"><div class="label">Havi költség</div><div class="value">${fmtEUR(x.opexMonthEUR)}<div class="sub2">${fmtHUF(x.opexMonthEUR*eur2huf)}</div></div></div>
      <div class="elecstat"><div class="label">Költség / 1M token</div><div class="value">${fmtEUR4(our1M)}<div class="sub2">${fmtHUF(our1M*eur2huf)}</div></div></div>
      <div class="elecstat"><div class="label">Költség / user / hó</div><div class="value">${fmtEUR(ourUserMonthEUR)}<div class="sub2">${fmtHUF(ourUserMonthEUR*eur2huf)}</div></div></div>`;

    document.getElementById("calcSplitLabel").textContent = `${Math.round(x.inpct*100)}% input / ${Math.round((1-x.inpct)*100)}% output`;

    const tin = x.tokM*x.inpct, tout = x.tokM*(1-x.inpct);
    const rows = C.bedrock.map(m=>{
      const usd = tin*m.pin + tout*m.pout;
      const eur = usd*usd2eur;
      const per1M = x.tokM>0 ? eur/x.tokM : 0;
      const ratio = ourPeriodEUR>0 ? eur/ourPeriodEUR : 0;
      return {m, eur, huf:eur*eur2huf, per1M, ratio};
    });
    const tb = document.querySelector("#calcTable tbody");
    tb.innerHTML =
      `<tr class="ourrow"><td><strong>Inference Farm (saját)</strong><div class="tier">Qwen3.5-397B · privát · fix OPEX</div></td>
        <td class="num">${fmtEUR(ourPeriodEUR)}</td><td class="num">${fmtHUF(ourPeriodEUR*eur2huf)}</td>
        <td class="num">${fmtEUR4(our1M)}</td><td class="num">1.00×</td></tr>` +
      rows.map(r=>{
        const col = r.ratio>=1 ? "var(--good)" : "var(--danger)";
        return `<tr><td>${r.m.name}<div class="tier">${r.m.tier}</div></td>
        <td class="num">${fmtEUR(r.eur)}</td><td class="num">${fmtHUF(r.huf)}</td>
        <td class="num">${fmtEUR4(r.per1M)}</td>
        <td class="num"><span style="color:${col};font-weight:600">${r.ratio.toFixed(2)}×</span></td></tr>`;
      }).join("");

    document.getElementById("calcNote").innerHTML =
      `A Bedrock soroknál a <strong>vs saját</strong> azt mutatja, hányszorosa a saját időszaki költségünknek (>1 = drágább, mint nálunk). ` +
      `Token-bontás: ${fmt.format(Math.round(tin))}M input + ${fmt.format(Math.round(tout))}M output. ` +
      `Bedrock = on-demand, us-east-1, May 2026 (szerkeszthető a forrásban). A saját költség fix OPEX, nem skálázódik token-nel — ezért 1M-re vetítve a volumen csökkenti.`;

    const labels = ["Saját (Inference Farm)"].concat(C.bedrock.map(m=>m.name));
    const data1M = [our1M].concat(rows.map(r=>r.per1M));
    const colors = ["#56e0c1"].concat(C.bedrock.map(()=>"#7c9cff"));
    if(calcChart) calcChart.destroy();
    calcChart = new Chart(document.getElementById("calcChart").getContext("2d"), {
      type:"bar",
      data:{labels, datasets:[{label:"EUR / 1M token", data:data1M, backgroundColor:colors, borderRadius:4}]},
      options:{indexAxis:"y", responsive:true, maintainAspectRatio:false,
        plugins:{legend:{display:false}, tooltip:{callbacks:{label:ctx=>fmtEUR4(ctx.parsed.x)+" / 1M  ("+fmtHUF(ctx.parsed.x*eur2huf)+")"}}},
        scales:{x:{grid:{color:"rgba(38,49,79,0.5)"}, ticks:{callback:v=>"€"+v.toFixed(2)}}, y:{grid:{display:false}}}}
    });
  }
  document.querySelectorAll("#calcInputs .calcin").forEach(el=>el.addEventListener("input", recompute));
  recompute();
  document.getElementById("calcFooter").textContent =
    `OPEX: Infarm OPEX.xlsx (2026-05-28) · FX 1 EUR = ${eur2huf} Ft, 1 USD = ${usd2eur} EUR · Bedrock árak: AWS on-demand becslés`;
})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
