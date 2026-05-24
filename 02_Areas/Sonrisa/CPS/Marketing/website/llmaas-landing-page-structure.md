# Sonrisa LLMaaS Landing Page — Structure & Copy (v2)

**Strategic positioning:** "Your own AI. We manage it."
**Wedge → Moat model:** Platform access (start fast) → Managed LLM infrastructure (full ownership)
**Tone:** Direct, confident, no hype. Like a senior engineer explaining to a CTO over coffee.

> **PRICING PHILOSOPHY (internal note):**
> We do NOT compete on token price. OpenAI GPT-4o costs ~$2.50/1M input tokens —
> we cannot beat that and shouldn't try. Our value is privacy, control, and managed
> operations. The shared platform is priced as a "private AI platform for your team"
> (comparable to ChatGPT Team at ~€300/mo or GitHub Copilot Business at ~€190/mo
> for 10 users), NOT as a cheaper-per-token alternative. All "40-60% cheaper" claims
> have been removed.

---

## SECTION 1: HERO

**Eyebrow badge:** LIVE · AWS GPU Infrastructure

**Headline:**
Your Own Private AI. Fully Managed.

**Subtitle:**
Run open-source LLMs on infrastructure you control — without hiring ML engineers.

**Body:**
Your team already uses AI every day. But sending company data to ChatGPT or Copilot isn't a strategy — it's a risk. We deploy, optimize, and manage private LLM infrastructure so you get the same capabilities with full data control.

**CTA primary:** Talk to Us
**CTA secondary:** See How It Works

---

## SECTION 2: TRUST BAR

"Trusted by engineering teams across Europe"

Oracle · Yettel · SYNLAB · Magyar Államkincstár · Global Blue · Lufthansa Systems · Diligent

---

## SECTION 3: "SOUND FAMILIAR?"

*This replaces the traditional "problem" section. Inspired by Palark's "Frequent Origins" but written as recognizable scenarios the buyer identifies with.*

**Section title:** Sound familiar?

**Scenario 1: "Security flagged it"**
Your developers use ChatGPT daily — but your security team just sent a company-wide email saying it's not allowed. Now productivity dropped and nobody has an alternative.

**Scenario 2: "The costs aren't predictable"**
You started with a few API keys for OpenAI. Six months later the invoice is 3x what you expected, and nobody can tell finance exactly what they're paying for.

**Scenario 3: "We need to own this"**
Your CTO wants AI capabilities but refuses to send proprietary code and customer data to external providers. GDPR, internal policy, or just common sense — the data has to stay yours.

**Scenario 4: "We don't have ML engineers"**
You know self-hosted LLMs exist, but who sets up the GPU infrastructure? Who keeps models updated? Who handles scaling? You're a product company, not an AI lab.

**Closing line:**
If any of this sounds like your Monday morning — we can help.

---

## SECTION 4: "WHAT WE DO"

*The core offer. Two paths, clearly separated.*

**Section title:** What we do

**Intro paragraph:**
We help companies run private AI — from first API call to fully managed infrastructure. Start fast with our shared platform, or go straight to a dedicated setup. Either way, your data never leaves controlled EU infrastructure.

---

### Path A: Shared LLM Platform (The Wedge)

**Card title:** Start with our platform
**Subtitle:** Get an API key today. No infrastructure decisions needed.

**Description:**
Access open-source models (Qwen, DeepSeek, Llama) through an OpenAI-compatible API and web interface. EU-hosted, ready in a day. Perfect for evaluation, small teams, or your first private AI project.

**Key points:**
- OpenAI-compatible API — drop-in replacement for existing tooling
- Web chat interface for non-technical users
- Up to 10 users included
- All data stays on Sonrisa-managed EU infrastructure
- Usage dashboard with monthly reporting

**Starting at:** €500/month — Private AI platform for your team
**What's included:** All models, API + web access, up to 10 users, business hours support, usage dashboard
**CTA:** Request Access

---

### Path B: Managed LLM Infrastructure (The Moat)

**Card title:** Your own AI, managed by us
**Subtitle:** Dedicated infrastructure. Your models. Our operations.

**Description:**
We deploy and manage a complete LLM stack on infrastructure you control — AWS, on-prem, or hybrid. You pick the models. We handle GPUs, scaling, updates, monitoring, and 24/7 operations. No ML team required.

**Key points:**
- Deploy on YOUR AWS account or on-premises servers
- Any open-source model from Hugging Face — LLMs, code models, image models
- Fine-tuning with LoRA/QLoRA on your proprietary data
- Full observability — dashboards, usage tracking, prompt analytics
- Integration with your tools (IDE plugins, Slack, internal apps, CI/CD)
- 24/7 operations, model updates, and security patches

**Starting at:** €1,000 setup + from €200/month managed ops
**CTA:** Let's Discuss Your Setup

---

### Visual: The Journey

```
[Start with our platform]  →  [Grow usage & teams]  →  [Move to dedicated infra]
   €500/mo shared              validate the value          your own stack, we manage
   API key in 1 day            prove the ROI               full ownership & control
```

**Caption:** Most customers start on our shared platform. When AI becomes strategic, we migrate you to your own infrastructure with zero downtime.

---

## SECTION 5: "WHAT THIS LOOKS LIKE" (Technical Proof)

*Show, don't tell. This is where developers get convinced.*

**Section title:** What this looks like

### Model Showcase Table

| Model | Best for | Speed | Context |
|-------|----------|-------|---------|
| Qwen 32B | Code generation, refactoring | ~50 tok/sec | 32K |
| DeepSeek Coder | Documentation, debugging | ~80 tok/sec | 16K |
| Llama 3.1 | General writing, analysis | ~60 tok/sec | 128K |
| Custom fine-tuned | Your domain-specific tasks | Optimized | Varies |

### API Code Snippet

```bash
# Drop-in replacement for OpenAI
curl https://llm.yourcompany.io/v1/chat/completions \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"model": "qwen-32b", "messages": [...]}'
```

**Callout:** Same API. Same SDKs. Same IDE plugins. Just a different endpoint — one that keeps your data private.

---

## SECTION 6: "WHY COMPANIES SWITCH"

*Concrete business outcomes. Lead with privacy and control, not cost.*

**Section title:** Why companies switch to private AI

**Stat card 1:**
**Zero** external data exposure
Your code, documents, and business data never leave controlled infrastructure. Complete audit trail for compliance.

**Stat card 2:**
**Predictable** monthly cost
Flat platform fee — no per-token surprises, no runaway bills. Know exactly what AI costs your team each month.

**Stat card 3:**
**1 week** to production
From first call to live platform. No 6-month procurement cycle. No ML hiring.

**Stat card 4:**
**No lock-in**
Open-source models (Apache 2.0, MIT). Migrate or self-host anytime. Your data, your models, your choice.

---

## SECTION 7: COMPARISON TABLE

*Direct, honest comparison. Focus on privacy and control, not token pricing.*

**Section title:** How it compares

| | Public APIs (OpenAI, Azure) | Sonrisa Shared Platform | Sonrisa Managed Infra |
|---|---|---|---|
| **Your data** | Sent to external servers | EU-hosted, Sonrisa-controlled | Stays on YOUR infrastructure |
| **Cost model** | Per-token, unpredictable at scale | Flat monthly, predictable | Setup + monthly ops |
| **Vendor lock-in** | High — proprietary models | Low — open-source models | None — you own everything |
| **Custom fine-tuning** | Limited, expensive | On request | Full LoRA/QLoRA support |
| **GDPR compliance** | Complex, requires DPA review | Built-in | Built-in, your control |
| **Getting started** | API key in minutes | API key in 1 day | 1-2 weeks deployment |
| **Who manages infra** | Provider | Sonrisa | Sonrisa (on your infra) |
| **User limits** | Per-seat pricing | Up to 10 users included | Unlimited |
| **Best for** | Quick experiments, no privacy needs | Teams validating private AI | Organizations going all-in |

> **Note:** Public APIs may be cheaper per-token for low-volume use. Our value is
> privacy, data control, and managed operations — not competing on raw token price.
> For companies where data sovereignty matters, the cost of a data breach or
> compliance violation far outweighs the platform fee.

---

## SECTION 8: SECURITY & COMPLIANCE

*Short and trust-building. Gate requirement for enterprise buyers.*

**Section title:** Security & Compliance

Six cards:

1. **EU Data Sovereignty** — All processing within your designated AWS region or on-prem. No data transfer outside your control.
2. **Encryption** — TLS in transit, AES-256 at rest. API key management with per-user quotas.
3. **No External Calls** — Models run entirely on controlled infrastructure. Zero third-party AI involvement.
4. **Audit-Ready** — Complete request/response logging. SOC2-aligned design.
5. **Access Control** — RBAC, SSO/SAML integration, per-user API keys, project isolation.
6. **Air-Gap Support** — For high-security environments, we support fully air-gapped deployments.

---

## SECTION 9: "HOW TO GET STARTED"

*Simple, low-friction. Two tracks matching the two paths.*

**Section title:** How to get started

### Track A: Shared Platform
1. **Talk to us** (30 min) — We understand your use case and recommend models
2. **Get access** (1 day) — API keys, web interface, team onboarding
3. **Use it** (ongoing) — Flat monthly fee with usage reporting

### Track B: Managed Infrastructure
1. **Discovery call** (30 min) — Understand your requirements, infrastructure, and goals
2. **Architecture & setup** (1-2 weeks) — Deploy on your AWS or on-prem, configure models
3. **Pilot** (30 days) — Limited rollout with monitoring and optimization
4. **Go live** (ongoing) — 24/7 managed operations, updates, and quarterly reviews

**Pricing summary:**

| | Shared Platform | Managed: Basic | Managed: Pro |
|---|---|---|---|
| **Setup** | None | €1,000 | €1,000 |
| **Monthly** | €500/month | €200/month | €1,000/month |
| **Users** | Up to 10 | Unlimited | Unlimited |
| **Models** | All standard models | Any from Hugging Face | Any + custom fine-tuned |
| **Support** | Business hours | 8/5 | 24/7 |
| **Includes** | API + Web UI, usage dashboard | Deployment, updates, basic monitoring | Everything in Basic + performance monitoring, model analysis |
| **Infrastructure** | Sonrisa-managed (EU) | Your AWS / on-prem | Your AWS / on-prem |

> **Need more users on the shared platform?** Contact us for team pricing.
> **Not sure which path?** Start shared — we'll migrate you when you're ready.

---

## SECTION 10: MID-PAGE CTA

**Headline:** Not sure which path is right?

**Body:**
Let's talk it through. 30 minutes, no commitment. You'll get honest advice on whether private AI makes sense for your team — and if so, which approach fits.

**CTA:** Book a Call

---

## SECTION 11: BOTTOM CTA

**Headline:** Your team is already using AI. The question is whether you control it.

**Body:**
We'll help you figure that out.

**CTA primary:** Talk to Us
**CTA secondary:** Learn about Sonrisa CPS →

---

## NOTES FOR DESIGN

**Key differences from previous wireframe:**
1. Two-path structure is the centerpiece — shared platform (wedge) vs managed infra (moat)
2. "Sound familiar?" section replaces abstract problem cards — more empathetic, scenario-based
3. Comparison table now has 3 columns (public APIs vs shared vs managed) — shows the journey
4. Pricing is simpler and more Palark-like — setup fee + monthly, not 4 tier cards
5. "How to get started" has two clear tracks matching the two paths
6. Bottom CTA is conversational, not salesy — matches Sonrisa's values (alázat, személyes kapcsolatok)
7. Case study / social proof section can be added later when first customer story is available

**What stays from the previous wireframe:**
- Sonrisa green color palette and Inter typography
- Trust bar with real client logos
- API code snippet (technical proof)
- Model showcase table
- Security & compliance cards
- Overall page rhythm (alternating light/dark sections)

**Critical messaging corrections (v2):**
- ❌ REMOVED: All "40-60% cheaper than OpenAI" claims (inaccurate — OpenAI is now cheaper per-token)
- ❌ REMOVED: Token-count-based pricing framing (€500 for 10M tokens)
- ✅ REPLACED WITH: Platform-access pricing (€500/mo for up to 10 users, all models included)
- ✅ ADDED: Honest comparison note acknowledging public APIs may be cheaper per-token
- ✅ REFRAMED: Value proposition around privacy, control, and managed ops — not cost savings
- ✅ REFRAMED: "Predictable cost" instead of "cheaper" — flat fee vs unpredictable per-token billing

---

## DOCUMENTS THAT NEED UPDATING

The following files still contain the outdated "40-60% cheaper" claim and token-based pricing:

1. **Services/Inference Farm/Description.md** — Lines: "20-30% higher costs than self-hosted alternatives", "40-60% cheaper than OpenAI equivalent", entire Business Impact / Cost Savings table
2. **Services/Inference Farm/LLMaaS — ACE Opportunity Summary.md** — Lines: "40-60% savings", "Reducing OpenAI/Azure spend" as customer value
3. **BMC v1.3.md** — Check if cost claims are referenced in value proposition section

These should be updated before any customer-facing presentations.
