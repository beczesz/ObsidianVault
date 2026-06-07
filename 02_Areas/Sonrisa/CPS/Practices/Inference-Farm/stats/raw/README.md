---
title: "AWS Inference Farm (`infarm`)"
date: 2026-05-28
author: Becze Szabolcs
status: active
description: "Modular Terraform and Terragrunt infrastructure for deploying GPU-based LLM inference on AWS with ECS, auto-scaling, and platform services like LiteLLM gateway and Open WebUI. Intended for teams building cost-efficient cloud-native LLM deployments."
description_source: auto
description_hash: e9ee32efaa5fd042
id: 1e689766-6dc2-467d-afa8-8d00f05f8a2d
index_schema_version: 1
bdos_index: true
---
# AWS Inference Farm (`infarm`)

Scalable AWS infrastructure for LLM inference, built with **Terraform**, **Terragrunt**.

This repository provides a modular, Infrastructure-as-Code setup for deploying GPU-powered AWS workloads tailored to running large language models — together with the supporting platform services (gateway, UI, monitoring, secrets management) needed to operate them in a team.

---

## Table of Contents

- [Overview](#overview)
- [Repository Layout](#repository-layout)
- [Architecture Components](#architecture-components)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Configure the AWS Profile](#configure-the-aws-profile)
  - [SOPS Setup](#sops-setup)
  - [Deploying a Layer](#deploying-a-layer)
- [Image Preparation with Packer](#image-preparation-with-packer)
- [Benchmarking](#benchmarking)
  - [Single Run](#single-run)
  - [Sweep Across Request Rates](#sweep-across-request-rates)
  - [Automated RunPod Pipeline](#automated-runpod-pipeline)
- [Conventions and Best Practices](#conventions-and-best-practices)
- [References](#references)

---

## Overview

- **Cloud provider:** AWS (primary region: `eu-central-1`)
- **IaC stack:** Terraform + Terragrunt with remote state in S3 and state locking
- **Image builds:** Packer for EC2 AMIs (preconfigured with CUDA, NVIDIA drivers, vLLM runtime) and Docker images for ECS
- **Compute:** ECS (EC2 launch type) and Auto Scaling Groups on NVIDIA GPU instances (G5 family — e.g. `g5.xlarge`, `g5.12xlarge`)
- **Secrets:** AWS KMS-backed SOPS, with the KMS key provisioned by the `sops-kms-key` layer
- **Platform services:** Open WebUI front-end, LiteLLM gateway, Grafana dashboards, and a Site-to-Site VPN for private access
- **Designed for:** teams deploying open-source or proprietary LLMs (vLLM, LLaMA, Mistral, Falcon, Qwen, MiniMax, …) in a cost-efficient, cloud-native way

## Repository Layout

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

## Architecture Components

Each subdirectory under [`infra/layers/`](infra/layers/) is an independent Terraform layer composed via Terragrunt:

| Layer | Purpose |
|---|---|
| `networking` | VPC, subnets, routing |
| `vpc-endpoints` | Private connectivity to AWS services |
| `vpn-s2s` | Site-to-Site VPN for private access from the office network |
| `sops-kms-key` | KMS key used to encrypt SOPS secrets |
| `users` | IAM users, groups, and access policies |
| `ecr-pullthrough-cache` | ECR pull-through cache for upstream registries |
| `storage-hf-models` | Shared storage for HuggingFace model artifacts |
| `ecs-llm-template` | ECS service template for vLLM-style inference workloads |
| `ray-cluster` | Ray cluster for distributed inference / batch jobs |
| `litellm` | LiteLLM gateway (ECS + RDS) — unified OpenAI-compatible API |
| `open-webui` | Open WebUI front-end |
| `rds-open-webui` | Managed Postgres for Open WebUI |
| `grafana` / `rds-grafana` / `alb-grafana` | Grafana stack and its database / ALB |
| `nlb` | Internal NLB fronting selected services |

## Getting Started

### Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Terraform](https://developer.hashicorp.com/terraform/install) `>= 1.11.4`
- [Terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/install/)
- [Packer](https://developer.hashicorp.com/packer/install) (only for image builds)
- [SOPS](https://github.com/getsops/sops) (for editing encrypted secrets)

> The examples below assume the AWS profile is named **`awsfarm`**.

### Configure the AWS Profile

```bash
aws configure --profile awsfarm
```

Verify access:

```bash
aws sts get-caller-identity --profile awsfarm
```

### SOPS Setup

The KMS key used by SOPS is provisioned by the `sops-kms-key` layer and its ARN is wired in automatically — no manual configuration is required.

Edit encrypted secrets:

```bash
AWS_PROFILE=awsfarm sops edit ./dev/secrets.enc.yaml
```

### Deploying a Layer

All layers are deployed via Terragrunt from the corresponding directory under [`infra/env/`](infra/env/). For example, to apply the `litellm` layer in `eu-central-1/dev`:

```bash
cd infra/env/eu-central-1/dev/litellm
AWS_PROFILE=awsfarm terragrunt init
AWS_PROFILE=awsfarm terragrunt plan
AWS_PROFILE=awsfarm terragrunt apply
```

Remote state is stored in an S3 bucket (`terragrunt-infarm-<env>-<region>`) with native state locking enabled. The S3 backend, AWS provider, and default tags are generated centrally from [`infra/env/org.hcl`](infra/env/org.hcl).

## Image Preparation with Packer

- **EC2 AMI** — installs NVIDIA GPU drivers, CUDA toolkit, Python, and the selected LLM runtimes. Used by the ECS EC2 launch type and by Auto Scaling Groups.
- **Docker image** — GPU-ready container images for ECS-backed services, bundling model code, runtime, and libraries.

Example Packer templates and helper scripts are included to make builds reproducible.

For Blackwell-class GPUs (B100 / B200), see [`blackwell-vllm-setup.md`](blackwell-vllm-setup.md).

## Benchmarking

The repository ships with both ad-hoc benchmark commands (using vLLM's built-in `bench serve`) and a fully automated pipeline that provisions a RunPod GPU, runs a sweep, then tears the pod down.

### Single Run

```bash
docker run --rm --platform linux/amd64 \
  --entrypoint '' \
  -v "$(pwd)/result:/result" \
  -e HUGGING_FACE_HUB_TOKEN \
  -ti vllm/vllm-openai:latest \
  bash -c '
    pip3 install pandas datasets && \
    cd benchmarks && \
    vllm bench serve \
      --backend vllm \
      --base-url http://infarm-alb-from-terraform-1314266603.eu-central-1.elb.amazonaws.com \
      --model Qwen/Qwen3-32B \
      --tokenizer Qwen/Qwen3-32B \
      --dataset-name random \
      --request-rate "$request_rate" \
      --num-prompts 300 \
      --save-result
    mkdir -p /result
    cp *.json /result
  '
```

### Sweep Across Request Rates

```bash
export HUGGING_FACE_HUB_TOKEN=XXXXX
export TRANSFORMERS_OFFLINE=0
pip3 install pandas datasets

for request_rate in 1 2 3 4 5 10 15 20 25 30; do
  echo "Running benchmark with request rate: $request_rate"
  vllm bench serve \
    --backend vllm \
    --base-url http://localhost:8000 \
    --model Qwen/Qwen3-32B \
    --tokenizer Qwen/Qwen3-32B \
    --dataset-name random \
    --request-rate "$request_rate" \
    --num-prompts 300 \
    --save-result
done
```

### Automated RunPod Pipeline

[`pipeline/run.py`](pipeline/run.py) creates a vLLM-capable RunPod pod, runs the benchmark sweep against it, and deletes the pod when finished.

```bash
# Standard run
python pipeline/run.py --model Qwen/Qwen3-32B

# Custom rates / prompt count
python pipeline/run.py --model Qwen/Qwen3-32B \
  --request-rates 1,2,5,10 --num-prompts 100

# Custom image and vLLM args (e.g. MiniMax M2 with its tool-call parser)
python pipeline/run.py \
  --model MiniMaxAI/MiniMax-M2 \
  --docker-image bakonyip/vllm-minimax-m2:latest \
  --extra-vllm-args "--tool-call-parser minimax_m2 --trust-remote-code"
```

Required environment variables:

| Variable | Description |
|---|---|
| `RUNPOD_API_KEY` | RunPod API key (pod lifecycle) |
| `VLLM_API_KEY` | API key sent with benchmark requests |

Results can be post-processed with [`scripts/convert_json_to_csv.py`](scripts/convert_json_to_csv.py).

## Conventions and Best Practices

- **Official AWS Terraform modules** — we rely on the community-maintained [`terraform-aws-modules`](https://github.com/terraform-aws-modules) collection for VPC, ECS, IAM, ECR, CloudWatch, etc. This buys us tested, well-architected defaults and lowers maintenance overhead across Terraform upgrades.
- **Modular Terragrunt layering** — clean separation of concerns, DRY environment configuration, and reusable modules per service.
- **Remote state & locking** — S3 backend with native locking (`use_lockfile = true`), encryption at rest, per-layer state keys derived from `path_relative_to_include()`.
- **Consistent tagging** — `project`, `environment`, `layer`, and `managed_by` tags are injected automatically by the AWS provider's `default_tags`.
- **Secrets** — all secrets live in SOPS-encrypted YAML under each environment; never commit plaintext credentials.

## References

Terraform modules in use:

- [iam](https://registry.terraform.io/modules/terraform-aws-modules/iam/aws/latest)
- [ecr](https://registry.terraform.io/modules/terraform-aws-modules/ecr/aws/latest)
- [vpc](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest)
- [ecs](https://registry.terraform.io/modules/terraform-aws-modules/ecs/aws/latest)
- [cloudwatch](https://registry.terraform.io/modules/terraform-aws-modules/cloudwatch/aws/latest)

Useful AWS documentation:

- [EC2 instance types per region (eu-west-1 example)](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-regions.html#instance-types-eu-west-1)
