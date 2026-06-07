---
schema: forge.practice-learnings.area.v1
generated_at: null
practice_area: "cps-inference-farm"
counts:
  active: 0
  proposed: 0
  retired: 0
description: Forge structured learnings élő indexe a CPS Inference Farm practice area-hoz. Per-area tanulságok (NEM cross-area meta — az `agents/forge/practice-learnings/` mappában él). Tanulságok ahogy a practice area érlelődik: deployment patterns, sizing rules, vendor-comparison results, banking-compliance recipes.
id: e6b3d918-2f47-4c5a-89d1-7b4e6c8a3f29
index_schema_version: 1
bdos_index: false
---

# Inference Farm — Structured Learnings Index

Per-area tanulságok. **Forge `learn` mód karbantartja.** Lifecycle: `proposed → active → retired`.

## Knowledge base (reference material)

> A practice consolidated reference knowledge-base-je (NEM structured learning, hanem forrás-derived dokumentáció) itt él: [`../knowledge-base/`](../knowledge-base/00_SOURCE_INDEX.md). 2026-05-29-én Forge a teljes Sonrisa SharePoint Inference-Farm tudást ide extraktálta + organizálta. Belépő: [00_SOURCE_INDEX.md](../knowledge-base/00_SOURCE_INDEX.md).

| Note | Tartalom |
|---|---|
| [00_SOURCE_INDEX](../knowledge-base/00_SOURCE_INDEX.md) | Forrás-katalógus (minden SharePoint doc + link) |
| [01_architecture-infrastructure](../knowledge-base/01_architecture-infrastructure.md) | IaC stack, hibrid AWS + on-prem topológia, vLLM/LiteLLM/Open WebUI, Blackwell setup |
| [02_performance-case-study](../knowledge-base/02_performance-case-study.md) | Qwen3.5-397B-NVFP4 produkciós teljesítmény (4 GPU) |
| [03_benchmarks-model-sizing](../knowledge-base/03_benchmarks-model-sizing.md) | Benchmarkok, instance-költségek, model right-sizing, 20-dim scoring |
| [04_business-model-pricing](../knowledge-base/04_business-model-pricing.md) | OPEX, tier-ek (A–D), margók, token-árazási mérőszámok |
| [05_strategy-requirements](../knowledge-base/05_strategy-requirements.md) | LLMaaS terv, roadmap, 10-területes checklist, követelmények |
| [06_usage-statistics](../knowledge-base/06_usage-statistics.md) | Q1 2026 használat (5.77B token) |
| [07_analytics-telemetry](../knowledge-base/07_analytics-telemetry.md) | `stats/` dashboard + raw telemetria (logs.out, nvidia-smi, dashboardok) |
| [08_capacity-analysis](../knowledge-base/08_capacity-analysis.md) | Adat-vezérelt kapacitás-modell: jelenlegi limit, headroom 200+ userig, kötő constraint |

Amikor ezekből confirmed tanulság kristályosodik ki (pl. `sizing-rule`, `cost-anchor`), az ide a structured learnings listába kerül.

## Active (0)
*Üres — practice area most jött létre (2026-05-27), nincsenek confirmed learnings.*

## Proposed (0)
## Retired (0)

---

## Cap

- Max **15 active learning**, max **2000 token** preamble
- Sorrend: `confidence DESC, last_applied_at DESC`

## Tanulság-típus jelölt-vocabulary

Inference Farm-specifikus tanulság-típusok (v0.2-ben Forge `learn` mód véglegesíti). Induló jelöltek:

| Típus | Mit rögzít |
|---|---|
| `sizing-rule` | hány GPU / mekkora VRAM kell egy adott user-count + token-throughput-hoz |
| `model-fit-pattern` | mely modell (vLLM via Llama vs Qwen vs Mistral) milyen banki / üzleti workload-hoz fit |
| `stack-decision` | vLLM vs Ollama vs TGI vs SGLang trade-off mintázat ügyfélkörnyezetben |
| `security-recipe` | banki compliance-re érvényesített hardening receptek (ISO 27001 controls) |
| `cost-anchor` | egy adott sizing-tier (small/medium/large) anchor árazás referencia |
| `integration-pattern` | hogyan integrálódik a farm Camunda / n8n / KodeSage / RAG stack-ekhez |
| `incident-pattern` | gyakori incidens-típusok és válaszok (OOM, latency spike, GPU thermal throttling) |
| `vendor-quirk` | hardver vagy szoftver vendor-specifikus furcsaságok amik repeatable headache-t okoznak |

(Ezek a jelöltek — Forge `learn` mód a végén v0.2-ben pinneli a stable type-vocabularyt.)
