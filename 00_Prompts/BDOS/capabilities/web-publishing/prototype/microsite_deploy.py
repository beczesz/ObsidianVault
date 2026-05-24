#!/usr/bin/env python3
"""
Microsite Factory — Cloudflare Pages Direct Upload deploy script.

Usage:
    microsite_deploy.py <site-dir> --project=<name> [--branch=staging]

Env vars required:
    CF_API_TOKEN   — Cloudflare API token (Pages Edit + Zone DNS Edit scope)
    CF_ACCOUNT_ID  — Cloudflare account ID

Status: prototype v0.1 — DH/Netlify workflow port to Cloudflare.
"""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import requests
from blake3 import blake3
from requests_toolbelt import MultipartEncoder

CF_API = "https://api.cloudflare.com/client/v4"
ASSET_BATCH_BYTES = 50 * 1024 * 1024  # 50 MB per upload batch
SINGLE_FILE_MAX = 25 * 1024 * 1024     # 25 MiB CF limit
POLL_INTERVAL_S = 3
POLL_MAX = 30


@dataclass
class Config:
    token: str
    account_id: str
    project: str
    site_dir: Path
    branch: str | None  # None = production


def load_config() -> Config:
    p = argparse.ArgumentParser(description="Cloudflare Pages atomic deploy")
    p.add_argument("site_dir", type=Path, help="Path to site root")
    p.add_argument("--project", required=True, help="CF Pages project name")
    p.add_argument("--branch", default=None, help="Optional branch (e.g. staging)")
    args = p.parse_args()

    token = os.environ.get("CF_API_TOKEN")
    account_id = os.environ.get("CF_ACCOUNT_ID")
    if not token or not account_id:
        sys.exit("ERROR: CF_API_TOKEN and CF_ACCOUNT_ID must be set in env.")
    if not args.site_dir.is_dir():
        sys.exit(f"ERROR: {args.site_dir} is not a directory.")

    return Config(
        token=token,
        account_id=account_id,
        project=args.project,
        site_dir=args.site_dir.resolve(),
        branch=args.branch,
    )


def pre_deploy_check(site_dir: Path) -> None:
    """Run optional pre-deploy validator script if present (DH convention)."""
    script = site_dir / "pre-deploy-check.py"
    if script.exists():
        import subprocess
        print(f"→ Running {script.name}")
        result = subprocess.run([sys.executable, str(script)], cwd=site_dir)
        if result.returncode != 0:
            sys.exit(f"ERROR: pre-deploy-check failed ({result.returncode}).")
    index = site_dir / "index.html"
    if not index.exists():
        sys.exit(f"ERROR: {index} missing.")


def collect_files(site_dir: Path) -> list[tuple[str, Path]]:
    """Return list of (rel_path, abs_path), rel_path starts with '/'."""
    files = []
    for p in site_dir.rglob("*"):
        if not p.is_file():
            continue
        if any(seg.startswith(".") for seg in p.relative_to(site_dir).parts):
            continue  # skip dotfiles
        if p.name == "pre-deploy-check.py":
            continue
        if p.stat().st_size > SINGLE_FILE_MAX:
            sys.exit(f"ERROR: {p} exceeds 25 MiB CF limit; use R2 for large assets.")
        rel = "/" + str(p.relative_to(site_dir)).replace(os.sep, "/")
        files.append((rel, p))
    return files


def hash_file(path: Path) -> str:
    return blake3(path.read_bytes()).hexdigest()[:32]


def get_upload_jwt(cfg: Config) -> str:
    url = f"{CF_API}/accounts/{cfg.account_id}/pages/projects/{cfg.project}/upload-token"
    r = requests.get(url, headers={"Authorization": f"Bearer {cfg.token}"}, timeout=30)
    r.raise_for_status()
    return r.json()["result"]["jwt"]


def upload_assets(jwt: str, manifest: list[dict]) -> None:
    """POST batches to /pages/assets/upload until all hashes are uploaded."""
    url = f"{CF_API}/pages/assets/upload"
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    batch, batch_bytes = [], 0
    total_uploaded = 0

    def flush():
        nonlocal batch, batch_bytes, total_uploaded
        if not batch:
            return
        r = requests.post(url, headers=headers, data=json.dumps(batch), timeout=120)
        r.raise_for_status()
        total_uploaded += len(batch)
        print(f"   uploaded {total_uploaded}/{len(manifest)} assets ({batch_bytes//1024} KB)")
        batch, batch_bytes = [], 0

    for entry in manifest:
        b64 = entry["_b64"]
        size = len(b64)
        if batch_bytes + size > ASSET_BATCH_BYTES:
            flush()
        batch.append({
            "key": entry["hash"],
            "value": b64,
            "metadata": {"contentType": entry["contentType"]},
            "base64": True,
        })
        batch_bytes += size
    flush()


def upsert_hashes(jwt: str, hashes: list[str]) -> None:
    url = f"{CF_API}/pages/assets/upsert-hashes"
    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"},
        data=json.dumps({"hashes": hashes}),
        timeout=60,
    )
    r.raise_for_status()


def create_deployment(cfg: Config, manifest_map: dict[str, str]) -> dict:
    """POST manifest as multipart/form-data to create the deployment."""
    url = f"{CF_API}/accounts/{cfg.account_id}/pages/projects/{cfg.project}/deployments"
    fields = {"manifest": json.dumps(manifest_map)}
    if cfg.branch:
        fields["branch"] = cfg.branch
    mp = MultipartEncoder(fields=fields)
    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {cfg.token}", "Content-Type": mp.content_type},
        data=mp,
        timeout=120,
    )
    r.raise_for_status()
    return r.json()["result"]


def poll_deployment(cfg: Config, deployment_id: str) -> dict:
    url = f"{CF_API}/accounts/{cfg.account_id}/pages/projects/{cfg.project}/deployments/{deployment_id}"
    for i in range(POLL_MAX):
        time.sleep(POLL_INTERVAL_S)
        r = requests.get(url, headers={"Authorization": f"Bearer {cfg.token}"}, timeout=30)
        r.raise_for_status()
        d = r.json()["result"]
        stage = d.get("latest_stage", {}).get("name", "?")
        status = d.get("latest_stage", {}).get("status", "?")
        print(f"   [{i+1}] {stage}: {status}")
        if status == "success" and stage == "deploy":
            return d
        if status == "failure":
            sys.exit(f"ERROR: deployment failed at stage '{stage}'.")
    sys.exit("ERROR: deployment polling timeout.")


def main() -> None:
    cfg = load_config()
    target = "staging" if cfg.branch else "production"
    print(f"→ Microsite Factory deploy: {cfg.project} ({target})")
    print(f"   site_dir: {cfg.site_dir}")

    pre_deploy_check(cfg.site_dir)
    files = collect_files(cfg.site_dir)
    print(f"→ Collected {len(files)} files.")

    print("→ Hashing + encoding assets...")
    manifest = []
    for rel, abs_path in files:
        data = abs_path.read_bytes()
        ctype = mimetypes.guess_type(abs_path.name)[0] or "application/octet-stream"
        manifest.append({
            "path": rel,
            "hash": blake3(data).hexdigest()[:32],
            "contentType": ctype,
            "_b64": base64.b64encode(data).decode(),
        })

    print("→ Requesting upload JWT...")
    jwt = get_upload_jwt(cfg)

    print(f"→ Uploading {len(manifest)} assets...")
    upload_assets(jwt, manifest)

    print("→ Registering hashes...")
    upsert_hashes(jwt, [m["hash"] for m in manifest])

    print(f"→ Creating deployment ({target})...")
    manifest_map = {m["path"]: m["hash"] for m in manifest}
    deployment = create_deployment(cfg, manifest_map)
    deployment_id = deployment["id"]
    print(f"   deployment_id: {deployment_id}")

    print("→ Polling status...")
    final = poll_deployment(cfg, deployment_id)
    url = final.get("url") or f"https://{deployment_id}.{cfg.project}.pages.dev"
    print(f"\n✓ Deployed: {url}")


if __name__ == "__main__":
    main()
