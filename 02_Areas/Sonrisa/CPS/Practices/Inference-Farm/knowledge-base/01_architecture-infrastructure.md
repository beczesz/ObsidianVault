---
title: "Inference Farm — Architecture & Infrastructure"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "Technical architecture of the CPS AWS Inference Farm (infarm): Terraform/Terragrunt IaC stack on AWS eu-central-1, the full set of infrastructure layers (networking, VPN, ECS vLLM, LiteLLM gateway, Open WebUI, Ray, Grafana), GPU instance families, image builds with Packer, secrets via SOPS/KMS, the RunPod benchmark pipeline, and the Blackwell-GPU vLLM server setup for MiniMax M2.1. Live service URLs included. Extracted from the AwsInFarm IaC repo README and setup guides on SharePoint."
practice_area: cps-inference-farm
type: technical-reference
audience: internal-engineering
provenance: "Extracted by Forge from CloudPlatformServices-Inferencefarm/AwsInFarm/README.md + blackwell-vllm-setup.md (modified 2026-05-27) and AWS Inference Farm.loop meeting notes, on 2026-05-29."
id: cf6fd0b3-8651-40df-bdf2-7cc114550db7
index_schema_version: 1
bdos_index: false
---

# Inference Farm — Architecture & Infrastructure

> Source: `AwsInFarm` IaC repository (`README.md`, `blackwell-vllm-setup.md`) on the canonical IF SharePoint site. See [00_SOURCE_INDEX.md](00_SOURCE_INDEX.md).

## Overview

`infarm` is a scalable AWS infrastructure for LLM inference, built as **Infrastructure-as-Code** with **Terraform + Terragrunt**. It deploys GPU-powered AWS workloads for running LLMs, plus the supporting platform services (gateway, UI, monitoring, secrets) to operate them as a team.

| Aspect | Choice |
|---|---|
| Cloud provider | AWS — primary region `eu-central-1` |
| IaC stack | Terraform + Terragrunt, remote state in S3 with native state locking |
| Image builds | Packer for EC2 AMIs (CUDA, NVIDIA drivers, vLLM preinstalled) + Docker images for ECS |
| Compute | ECS (EC2 launch type) and Auto Scaling Groups on NVIDIA GPU instances (G5 family: `g5.xlarge`, `g5.12xlarge`, …) |
| Secrets | AWS KMS-backed SOPS (KMS key provisioned by the `sops-kms-key` layer) |
| Platform services | Open WebUI front-end, LiteLLM gateway (OpenAI-compatible), Grafana dashboards, Site-to-Site VPN for private access |
| Serving engine | vLLM (also supports LLaMA, Mistral, Falcon, Qwen, MiniMax, …) |
| AWS profile (convention) | `awsfarm` |

## Live service URLs

- **Frontend (Open WebUI):** `https://ai.sonrisa.hu`
- **Grafana (via ALB):** `http://grafana-alb-from-terraform-415582780.eu-central-1.elb.amazonaws.com`
- **Benchmark ALB target (example):** `http://infarm-alb-from-terraform-1314266603.eu-central-1.elb.amazonaws.com`
- **Internal AI-adoption inference farm (distinct track):** `chat.int.sonrisa.hu`
- **Contact for access/issues:** `ai@sonrisa.hu`

## Repository layout

```
.
├── infra/                       # Terraform + Terragrunt infrastructure
│   ├── env/                     # Environment / region configuration (Terragrunt)
│   │   ├── org.hcl              # Org-wide defaults (state backend, providers, tags)
│   │   └── eu-central-1/dev/    # Per-environment layer instantiations
│   └── layers/                  # Reusable Terraform modules ("layers")
├── pipeline/                    # Automated vLLM benchmark pipeline (RunPod)
├── runpod/                      # RunPod helper scripts (pod lifecycle, WebUI updates)
├── open-webui-functions/        # Custom Open WebUI functions / tools
├── grafana-dashboards/          # Exported Grafana dashboards (vLLM, Open WebUI)
├── scripts/                     # Utility scripts (e.g. benchmark JSON → CSV)
├── blackwell-vllm-setup.md      # Reference guide for Blackwell GPU + vLLM
└── README.md
```

## Deployed topology (from `infarm.drawio.png`)

The architecture diagram (in [../stats/raw/infarm.drawio.png](../stats/raw/infarm.drawio.png)) shows a **hybrid AWS + on-prem** deployment spanning two AWS accounts and the Sonrisa office:

**AWS account `382113323075` ("CPS - Infarm")** — the main VPC:
- Public subnets `10.16.101.0/24`, `10.16.102.0/24`, `10.16.103.0/24`; private subnets `10.16.1.0/24`, `10.16.2.0/24`, `10.16.3.0/24`.
- **Internet-facing ALB (open-webui)** + AWS Certificate Manager (`ai.sonrisa.hu`) → **ECS `open-webui-service`** (`open-webui-container`) with a dedicated **RDS Postgres**; CloudWatch logs.
- **Internet-facing ALB (litellm)** → **ECS `litellm-service`** (Task) with its own **RDS Postgres**; CloudWatch logs.
- **ECR pull-through cache (GitHub)** → `ghcr/open-webui/open-webui`.
- **ECR pull-through cache (Docker Hub)** → `docker-hub/grafana/grafana`.

**AWS account `911406043488` ("Sonrisa SYS")** — Amazon Route 53 hosting `ai.sonrisa.hu` DNS.

**Access:** Sonrisa **Site-to-Site VPN** fronts the ALBs for private office access.

**On-prem — "Sonrisa BUD · Duna Tower"** — the LiteLLM gateway also routes to two on-prem vLLM hosts:
| Host | Models (endpoint) |
|---|---|
| `192.168.9.49` | `MiniMaxAI/MiniMax-M2.1` (`:8000/v1`), `qwen3-vl-8b-instruct-vllm-1` (`:8001/v1`) |
| `192.168.9.190` | `Qwen/Qwen3-4B` (`:8000/v1`), `Qwen/Qwen2.5-VL-7B-Instruct` (`:8001/v1`), `Qwen/Qwen3-Embedding-0.6B` (`:8002/v1`) |

So **LiteLLM is the unifying gateway** over both AWS-hosted and on-prem (Duna Tower) model servers; Open WebUI is the user front-end; Postgres backs each.

> **Open question (for deeper dig):** the production logs (`logs.out`) are from `nvidia/Qwen3.5-397B-A17B-NVFP4` on 4 GPUs (NVFP4 = Blackwell). The diagram's on-prem Duna Tower hosts only show *smaller* models, and the 397B isn't explicitly placed there. Whether the 397B runs on AWS Blackwell instances or an (undiagrammed) on-prem Blackwell server is not fully pinned from these artifacts. The blackwell-vllm-setup.md guide targets on-prem Blackwell.

## Infrastructure layers (Terragrunt)

Each subdirectory under `infra/layers/` is an independent Terraform layer composed via Terragrunt:

| Layer | Purpose |
|---|---|
| `networking` | VPC, subnets, routing |
| `vpc-endpoints` | Private connectivity to AWS services |
| `vpn-s2s` | Site-to-Site VPN for private access from the office network |
| `sops-kms-key` | KMS key used to encrypt SOPS secrets |
| `users` | IAM users, groups, access policies |
| `ecr-pullthrough-cache` | ECR pull-through cache for upstream registries |
| `storage-hf-models` | Shared storage for HuggingFace model artifacts |
| `ecs-llm-template` | ECS service template for vLLM-style inference workloads |
| `ray-cluster` | Ray cluster for distributed inference / batch jobs |
| `litellm` | LiteLLM gateway (ECS + RDS) — unified OpenAI-compatible API |
| `open-webui` | Open WebUI front-end |
| `rds-open-webui` | Managed Postgres for Open WebUI |
| `grafana` / `rds-grafana` / `alb-grafana` | Grafana stack + database + ALB |
| `nlb` | Internal NLB fronting selected services |

## Deployment workflow

Layers are deployed via Terragrunt from the matching directory under `infra/env/`. Example for the `litellm` layer in `eu-central-1/dev`:

```bash
cd infra/env/eu-central-1/dev/litellm
AWS_PROFILE=awsfarm terragrunt init
AWS_PROFILE=awsfarm terragrunt plan
AWS_PROFILE=awsfarm terragrunt apply
```

- Remote state: S3 bucket `terragrunt-infarm-<env>-<region>`, native locking (`use_lockfile = true`), encryption at rest, per-layer state keys via `path_relative_to_include()`.
- S3 backend, AWS provider, and default tags are generated centrally from `infra/env/org.hcl`.
- Consistent tags injected automatically: `project`, `environment`, `layer`, `managed_by`.

### Secrets (SOPS)

The KMS key is provisioned by the `sops-kms-key` layer and its ARN is wired in automatically. Edit encrypted secrets with:

```bash
AWS_PROFILE=awsfarm sops edit ./dev/secrets.enc.yaml
```

All secrets live in SOPS-encrypted YAML per environment — never commit plaintext credentials.

### Image preparation (Packer)

- **EC2 AMI** — installs NVIDIA GPU drivers, CUDA toolkit, Python, and the selected LLM runtimes. Used by the ECS EC2 launch type and by ASGs.
- **Docker image** — GPU-ready container images for ECS-backed services, bundling model code, runtime, and libraries.
- For Blackwell-class GPUs (B100 / B200), see the Blackwell setup section below.

## Conventions & best practices

- **Official AWS Terraform modules** — relies on the community `terraform-aws-modules` collection (VPC, ECS, IAM, ECR, CloudWatch) for tested, well-architected defaults.
- **Modular Terragrunt layering** — clean separation of concerns, DRY environment config, reusable per-service modules.
- **Remote state & locking** — S3 backend with native locking and encryption.
- **Consistent tagging** via the AWS provider's `default_tags`.
- **Secrets** always SOPS-encrypted.

Terraform modules in use: `iam`, `ecr`, `vpc`, `ecs`, `cloudwatch` (all `terraform-aws-modules`).

## Blackwell GPU + vLLM server setup (MiniMax M2.1)

Reference for setting up a Blackwell server (B200 / B100) to run vLLM with **MiniMax M2.1** on **Ubuntu 22.04**.

**Prerequisites:** Ubuntu 22.04, NVIDIA Blackwell GPU, internet for drivers/containers.

1. **NVIDIA driver** — purge any prior install (`apt-get purge '*nvidia*'`), install headers + build tools, then install the **open** variant: `nvidia-driver-580-open`. Reboot, verify with `nvidia-smi`.
2. **Docker** — official install script (`get.docker.com`), add user to `docker` group.
3. **NVIDIA Container Toolkit** — add NVIDIA repo, enable experimental, pin version `1.18.1-1`, configure the `nvidia` runtime in `/etc/docker/daemon.json`, restart Docker.
4. **MiniMax M2.1 via docker-compose** — vLLM OpenAI image (nightly), NVIDIA runtime, port 8000, HF cache volume. Key vLLM args:
   - `--model MiniMaxAI/MiniMax-M2.1`
   - `--gpu_memory_utilization 0.78`
   - `--tensor-parallel-size 4`
   - `--trust-remote-code`
   - `--enable-auto-tool-choice`
   - `--tool-call-parser minimax_m2`
   - `--reasoning-parser minimax_m2_append_think`
   - env: `HF_TOKEN`, `SAFETENSORS_FAST_GPU=1`, `ipc: host`
5. **Verify:** `curl localhost:8000/v1/models`.

**OpenAI-compatible API endpoints:** `POST /v1/chat/completions`, `POST /v1/completions`, `POST /v1/embeddings`, `GET /v1/models`.

Troubleshooting: `docker compose logs vllm`, `docker compose exec vllm nvidia-smi`, `watch -n 1 nvidia-smi`. Tune `gpu_memory_utilization` and `tensor_parallel_size` to GPU count/memory; consider quantization for memory efficiency. For production: replace `HF_TOKEN` placeholder, firewall port 8000, add authentication.

## Benchmark pipeline (RunPod)

The repo ships ad-hoc benchmark commands (vLLM `bench serve`) plus a fully automated pipeline (`pipeline/run.py`) that provisions a RunPod GPU pod, runs a request-rate sweep, then tears it down.

```bash
# Standard run
python pipeline/run.py --model Qwen/Qwen3-32B

# Custom rates / prompt count
python pipeline/run.py --model Qwen/Qwen3-32B --request-rates 1,2,5,10 --num-prompts 100

# Custom image + vLLM args (e.g. MiniMax M2 with its tool-call parser)
python pipeline/run.py --model MiniMaxAI/MiniMax-M2 \
  --docker-image bakonyip/vllm-minimax-m2:latest \
  --extra-vllm-args "--tool-call-parser minimax_m2 --trust-remote-code"
```

Required env: `RUNPOD_API_KEY` (pod lifecycle), `VLLM_API_KEY` (benchmark requests). Sweep rates used: `1 2 3 4 5 10 15 20 25 30`, 300 prompts, `random` dataset. Results post-processed with `scripts/convert_json_to_csv.py`. See [03_benchmarks-model-sizing.md](03_benchmarks-model-sizing.md) for results.

## Related

- Performance in production → [02_performance-case-study.md](02_performance-case-study.md)
- Architecture diagram (visual): `infarm.drawio.png` on the canonical site (linked in source index)
