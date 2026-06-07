---
title: Microsite Factory — Startup ötlet index
description: "ExarLabs startup ötlete: AI-asszisztált microsite gyár, amely üzleti briefből 20-30 perc alatt egyedi marketing weboldalt készít kisvállalkozások számára. BMC-t dolgoznak ki iteratívan, többügynök csapattal (Claude, ChatGPT, Perplexity, Gemini), magyar piacra célozva előbb fogászatok."
description_source: auto
description_hash: 0a9e5b51eb1a38f2
type: index
status: active
created: 2026-05-16
last_updated: 2026-05-16
owner: Szabolcs (ExarLabs)
id: b18b53a3-5ed8-42ce-a339-943c4642312c
index_schema_version: 1
---
# Microsite Factory — Startup index

> ExarLabs új startup ötlet: AI-asszisztált microsite gyár kisvállalkozásoknak. Egy üzleti briefből 20-30 perc alatt egyedi, stratégiailag átgondolt marketing weboldal — nem template, nem drag-and-drop.

## Státusz

**Fázis:** BMC kidolgozás (iteratív)
**Csapat:** Claude (orchestrator) + ChatGPT (Strategist, [meglévő chat](https://chatgpt.com/c/6a004d97-9838-8391-bcdd-e4fac1b1fce5)) + Perplexity (Researcher) + Gemini (Validator)
**Forrás dokumentum:** [BUSINESS_PLAN.md](./BUSINESS_PLAN.md) (importálva /Downloads-ból)

## Fájlok

| Fájl | Tartalom | Státusz |
|---|---|---|
| [BUSINESS_PLAN.md](./BUSINESS_PLAN.md) | Eredeti üzleti terv (2026-05-15) | v1.0 |
| [BMC.md](./BMC.md) | Business Model Canvas (iteratív) | **v0.5** |
| [chatgpt_chat_notes.md](./chatgpt_chat_notes.md) | ChatGPT Strategist Round 1 (7 insight) | v1.0 |
| [chatgpt_round2_notes.md](./chatgpt_round2_notes.md) | ChatGPT Round 2 (Gemini-reakció + deliverable-k) | v1.0 |
| [market_research.md](./market_research.md) | Perplexity Researcher — magyar piaci kontextus | v1.0 |
| [risks_validation.md](./risks_validation.md) | Gemini Validator + Claude pre-analízis | v2.0 |
| [references.md](./references.md) | Linkek vault-on belüli kapcsolódó anyagokhoz | v1.0 |
| [brainstorm/brainstorm_microsite_factory.md](./brainstorm/brainstorm_microsite_factory.md) | Orchestrator state file | active |

## Kapcsolódó vault anyagok

A `references.md` tartalmazza a teljes listát. Top 3:
1. [web-publishing capability (BDOS)](../../../00_Prompts/BDOS/capabilities/web-publishing/CLAUDE.md) — a belső eszköz oldal
2. [brand-to-site capability (Brand Spine + Maestro)](../../../00_Prompts/BDOS/capabilities/brand-to-site/CLAUDE.md) — upstream réteg
3. [Sonrisa CPS website precedens](../../Sonrisa/CPS/Marketing/website/CLAUDE.md) — élő működő példa

## Kulcs döntések (összegezve)

- **Termék vs. eszköz szétválasztása:** A BDOS `web-publishing/` a belső capability, ez a mappa a **piacra szánt startup terméket** dolgozza ki. Két különböző fókusz.
- **Célpiac első lépésben:** Magyar fogászatok (Sonrisa referencia adott).
- **Modell:** Done-for-you (mi készítjük) + recurring hosting/maintenance. NEM self-service platform (még).

## Következő lépések

1. ChatGPT chat importálása → insights kiemelés
2. Perplexity → piaci validáció (HU fogászat-piac, AI builder verseny 2026)
3. Gemini → kritika a 99% margin / lock-in narratíva / unsolicited demo taktikára
4. BMC v0.2 — szintézis után
