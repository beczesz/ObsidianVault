---
title: Inference Farm — Open Questions
date: 2026-05-27
description: Nyitott kérdések a CPS Inference Farm practice area körül. Forge `reflect` mód periodikusan átfut és vagy `research/`-ba forward-eli (külső kutatást igénylő) vagy `_inbox/`-ba (várjuk hogy egy engagement evidence-t hozzon). Lezárt kérdések áthelyeződnek `decisions/` ADR formájában. Live working document — gyakori szerkesztés várt.
bdos_index: false
id: 4d24e1c0-6e13-4667-9e06-21bd87502f0d
index_schema_version: 1
---

# Inference Farm — Open Questions

> Élő nyitott-kérdés-lista. Forge `reflect` mód karbantartja. Lezárás formái:
> - Külső kutatás → forward to `research/<topic>.md`
> - Engagement evidence várása → continue itt vagy `_inbox/`
> - Lezárt döntés → áthelyezés `decisions/ADR-N-<slug>.md`-be

## Sizing & capacity

- [ ] **Q-001:** Mekkora GPU sizing reális egy ~20-50 párhuzamos AID-user mellé banki workload-on? (Merkantil-on dependent — első evidence várható)
- [ ] **Q-002:** Mennyi VRAM kell egy 70B paraméteres modell quantized inference-éhez (Q4_K_M vs Q5_K_M trade-off)?
- [ ] **Q-003:** Single-tenant vs multi-tenant deployment ugyanazon a farm-on — mikor melyik szempont nyer (cost vs isolation)?

## Stack & technology

- [ ] **Q-004:** vLLM vs Ollama vs TGI vs SGLang — banki kontextusban melyik a defaultunk? (Igényel benchmark experiment → `experiments/`)
- [ ] **Q-005:** Melyik open-weights modell-családot pinneljük első default-ként? (Llama 3 / Qwen / Mistral)
- [ ] **Q-006:** Azure OpenAI private endpoint mint potenciális alternatív stack-tier — érdemes-e a practice area-ba felvenni "Cloud-Native" sub-practice-ként?

## Banking compliance

- [ ] **Q-007:** Pontosan mely ISO 27001 kontroll-set vonatkozik az inference workload-ra (vs. általános IT)?
- [ ] **Q-008:** DORA 2026 mit követel meg konkrétan AI-érintő infra-tól banki kontextusban?
- [ ] **Q-009:** Audit trail formátum — milyen mélységű loggolás kell egy LLM inference-call-ra hogy regulator-konform legyen?

## Integration

- [ ] **Q-010:** Camunda BPMN engine + on-prem LLM endpoint — referencia integrációs minta? (Merkantil email router triggered)
- [ ] **Q-011:** n8n + on-prem LLM endpoint — workflow-call SLA elvárások?
- [ ] **Q-012:** KodeSage és külön AID inference-farm együttélése — co-existence vs konfliktus?

## Packaging & pricing

- [ ] **Q-013:** Egyszeri setup + havi managed árazás (MVMI Azure DevOps minta) reális struktúra-e az Inference Farm-ra?
- [ ] **Q-014:** Setup-tier sizing (small / medium / large) — milyen user-count / throughput küszöb választja el?
- [ ] **Q-015:** Hardware ownership: Sonrisa-cloud vs ügyfél-on-prem vs hybrid — mikor melyiket ajánljuk?

## Talent & operations

- [ ] **Q-016:** Hány CPS-engineer (FTE) tud egy inference farm-ot stabil 24/7-ben üzemeltetni? Ceclan + Szántó + Póda + ki még?
- [ ] **Q-017:** Mely existing CPS-team-member-nek van AI/ML/inference depth-je beyond AWS/Azure DevOps?
- [ ] **Q-018:** Recruitment-igény: AI Platform Engineer szerep szükséges? (vs. existing devops/SRE training)

## Strategic

- [ ] **Q-019:** Merkantil az első — mi a következő banki / regulált ügyfél amit célzunk Inference Farm-mal?
- [ ] **Q-020:** Marketing / Presto: kell-e Inference Farm-specific case study a Merkantil-engagement után?

## Closed (moved to decisions/ as ADRs)

*Üres — még nincs lezárt kérdés.*

---

## Change log

| Date | Event |
|---|---|
| 2026-05-27 | Fájl létrehozva. 20 nyitott kérdés rögzítve sizing / stack / banking / integration / packaging / talent / strategic kategóriákban. |
