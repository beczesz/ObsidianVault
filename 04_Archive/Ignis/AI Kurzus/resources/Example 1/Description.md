# Sonrisa LLMaaS Platform

**Enterprise LLM-as-a-Service for Secure AI Inference**

---

## Executive Summary

Sonrisa LLMaaS is a **self-hosted Large Language Model platform** built on AWS infrastructure, delivering secure, token-based access to open-source AI models for enterprise clients. The platform enables organizations to leverage powerful LLMs for coding assistance, document generation, and everyday productivity tasks—without sending sensitive data to external providers.

|Attribute|Detail|
|---|---|
|**Deployment**|AWS (EU-Central, customer VPC optional)|
|**Models**|Qwen-32B, DeepSeek, Llama variants, custom fine-tuned|
|**Access**|API (OpenAI-compatible) + Web Interface|
|**Pricing**|Token-based with tiered packages|
|**Target Users**|Development teams, knowledge workers, enterprises with data sovereignty requirements|

---

## The Problem We Solve

Organizations increasingly depend on generative AI for productivity, but public LLM services create significant barriers:

### Data Privacy & Compliance Risk

Sending proprietary code, business documents, and sensitive data to external APIs risks breaches and violates internal policies—especially critical for regulated industries and EU-based companies subject to GDPR.

### Unpredictable & Escalating Costs

Per-token pricing from OpenAI, Anthropic, and Azure scales unpredictably. Enterprises face 20-30% higher costs than self-hosted alternatives, with potential for runaway expenses and no cost ceilings.

### Vendor Lock-In

Limited ability to fine-tune models on proprietary data, no control over model updates or deprecation, and strategic dependency on external providers.

### Performance Constraints

Shared infrastructure means variable latency and throughput limitations under heavy load—problematic for real-time coding assistance or high-volume document processing.

---

## Our Solution

### Secure, Self-Hosted LLM Infrastructure

Sonrisa LLMaaS abstracts the complexity of GPU infrastructure, model deployment, and operations into a simple, metered service. Your data never leaves controlled infrastructure.

```
┌─────────────────────────────────────────────────────────────┐
│                     Sonrisa LLMaaS                          │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐       │
│  │   Web UI    │   │  REST API   │   │  IDE Plugin │       │
│  │  (OpenUI)   │   │ (OpenAI-   │   │  (VS Code)  │       │
│  │             │   │ compatible) │   │             │       │
│  └──────┬──────┘   └──────┬──────┘   └──────┬──────┘       │
│         │                 │                  │              │
│         └─────────────────┼──────────────────┘              │
│                           ▼                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Load Balancer & Rate Limiting           │   │
│  │              Token Metering & Authentication         │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│         ┌─────────────────┼─────────────────┐              │
│         ▼                 ▼                 ▼              │
│  ┌───────────┐     ┌───────────┐     ┌───────────┐        │
│  │  Qwen-32B │     │ DeepSeek  │     │   Llama   │        │
│  │   (Code)  │     │  (General)│     │  (Custom) │        │
│  └───────────┘     └───────────┘     └───────────┘        │
│                                                             │
│  AWS GPU Infrastructure (G5.12XL) | Auto-Scaling | EU-West │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Capabilities

### Model Selection & Performance

|Model|Best For|Context Window|Inference Speed|
|---|---|---|---|
|**Qwen-32B**|Code generation, refactoring, explanation|32K tokens|~50 tokens/sec|
|**DeepSeek Coder**|Technical documentation, debugging|16K tokens|~80 tokens/sec|
|**Llama 3.1**|General productivity, writing, analysis|128K tokens|~60 tokens/sec|
|**Custom Fine-tuned**|Domain-specific tasks|Varies|Optimized|

### Technical Features

- **OpenAI-Compatible API** — Drop-in replacement; works with existing tooling, LangChain, LlamaIndex
- **Streaming Support** — Real-time token streaming for responsive UX
- **RAG Integration** — Retrieval-augmented generation with your documents
- **Fine-Tuning** — LoRA/QLoRA support for domain adaptation
- **Multi-Model Routing** — Automatic model selection based on task type
- **vLLM Backend** — High-throughput serving with PagedAttention

### Security & Compliance

- **Data Sovereignty** — All processing within your designated AWS region
- **No External Calls** — Models run entirely on controlled infrastructure
- **Encryption** — TLS in transit, AES-256 at rest
- **Access Control** — RBAC, API key management, per-user quotas
- **Audit Logging** — Complete request/response logging for compliance
- **SOC2 Alignment** — Designed for enterprise audit requirements

---

## Service Packages

|Package|Monthly Price|Included Tokens|Support|Use Case|
|---|---|---|---|---|
|**Starter**|€500|10M tokens|Business hours|Small teams, evaluation|
|**Professional**|€2,000|50M tokens|8/5 response|Development teams|
|**Enterprise**|€5,000|150M tokens|24/7 SLA|Organization-wide|
|**Dedicated**|Custom|Unlimited|Premium|High-volume, custom models|

**Overage:** €0.004/1K tokens (40-60% cheaper than OpenAI equivalent)

### What's Included

All packages include:

- Web interface access
- API access (OpenAI-compatible)
- Usage dashboard & analytics
- Token metering & billing reports
- Model updates & maintenance
- Security patches

Enterprise & Dedicated add:

- Dedicated inference capacity
- Custom model fine-tuning
- Private VPC deployment option
- Dedicated account manager
- Quarterly architecture reviews

---

## Business Impact

### Cost Savings

|Comparison|Public API|Sonrisa LLMaaS|Savings|
|---|---|---|---|
|50M tokens/month|~€1,500|€500-800|**40-60%**|
|200M tokens/month|~€6,000|€2,000-3,000|**50-65%**|
|1B tokens/month|~€30,000|€8,000-12,000|**60-70%**|

### Productivity Gains

- **20% faster** code review and documentation
- **30% reduction** in repetitive writing tasks
- **15% improvement** in developer velocity (measured by commit frequency)

### Risk Reduction

- **Zero** external data exposure
- **99.5%** uptime SLA
- **Complete** audit trail for compliance

---

## Technical Requirements

### Client-Side

- API calls via HTTPS (any language/framework)
- Optional: VS Code extension, JetBrains plugin

### Network

- Outbound HTTPS to LLMaaS endpoint
- Optional: VPC peering for private connectivity

### Authentication

- API key (per user or per project)
- Optional: SSO/SAML integration (Enterprise)

---

## Implementation Timeline

|Phase|Duration|Deliverables|
|---|---|---|
|**Onboarding**|1 week|Account setup, API keys, initial training|
|**Pilot**|2-4 weeks|Limited team rollout, usage monitoring|
|**Expansion**|4-8 weeks|Organization-wide deployment|
|**Optimization**|Ongoing|Fine-tuning, custom integrations|

---

## Why Sonrisa

### AWS-Native Expertise

Built by Sonrisa's Cloud Platform Services team with 300+ engineers and deep AWS expertise. We manage the infrastructure so you focus on building.

### Open-Source Foundation

No proprietary lock-in. Models are open-source (Apache 2.0, MIT). You can self-host or migrate anytime.

### EU-Based Delivery

Headquartered in Budapest with EU data residency. Full GDPR compliance and data sovereignty.

### Proven Track Record

Serving enterprise clients including Lufthansa, Oracle, and Diligent with mission-critical cloud infrastructure.

---

## Getting Started

1. **Request Demo** — 30-minute walkthrough of capabilities
2. **Pilot Agreement** — 30-day trial with Starter package
3. **Integration Support** — API setup and team onboarding
4. **Go Live** — Production deployment with full support

---

## Contact

**Sonrisa Technologies — Cloud Platform Services**

- **Email:** cps@sonrisa.hu
- **Web:** sonrisa.io/llmaas
- **AWS Partner:** Select Tier | Services Path

---

_Sonrisa LLMaaS — Enterprise AI Without Compromise_