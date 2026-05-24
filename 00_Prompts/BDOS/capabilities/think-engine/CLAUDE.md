---
title: Think Engine — multi-AI orchestration capability
date: 2026-05-22
author: Becze Szabolcs
status: active
version: 0.9
description: BDOS capability-pointer a Think Agent Orchestrator köré — semi-autonomous multi-AI orkesztráció (API + Chrome MCP hibrid), perzisztens state file mint tartós agy. Tartalmazza a csapatnak szánt interaktív bemutatót.
id: cc0a4f81-6b22-477d-a270-619af41ce9d8
index_schema_version: 1
---

# Think Engine — multi-AI orchestration capability

A **multi-AI cognition** képesség BDOS-pointere. A vault brainstorm-jai (pl. `../../brainstorm/brainstorm_brand-spine.md`) ezzel a motorral készülnek: Claude mint always-on karmester több AI-t (Opus, GPT-5, Perplexity, Copilot, második Claude-szál) hangol össze, párhuzamosan kérdezi őket, és egyetlen koherens szintézist ad vissza a felhasználónak, aki a döntési hatóság.

## A capability lényege

> **A brainstorm state file a tartós agy. Az AI-ok cserélhető gondolkodási felületek.**

- **Hibrid transport** — alapból API (gyors, strukturált, állapot nélküli → state file injektál kontextust), böngésző (Chrome MCP) csak négy esetben: voice mode, account-oldali adat, nincs API-alternatíva, élő emberi beszélgetés.
- **Perzisztens kogníció** — minden findings JSON a state file-ba kerül; a böngésző-insightot vissza kell szinkronizálni (drift-védelem).
- **Throughput-fegyelem** — fat promptok, strukturált Response Contract, párhuzamos aktiválás. Egy kör hossza = max(leglassabb tag), nem az összeg.

## Hol él mi

| Komponens | Hely |
|---|---|
| **Kanonikus skill (runtime)** | [`SKILL.md`](../../../Claude/Plugins/General%20Utils%20Plugin/skills/think-agent-orchestrator-v09/SKILL.md) — a Claude Code innen tölti, NE mozgasd |
| **Interaktív bemutató (csapat)** | [`bemutato.html`](bemutato.html) — önálló, egyfájlos prezentáció: orkesztrációs animáció, „egy kör" szimuláció, 8 lépéses hurok, transport döntési elv |

## Bemutató futtatása

Dupla katt a `bemutato.html`-re (bárhol megnyílik böngészőben), vagy a `think-engine-demo` dev-szerverrel: `localhost:8131/bemutato.html`.

## Hivatkozott

- BDOS belépő: [`../../CLAUDE.md`](../../CLAUDE.md)
- Multi-AI brainstorm precedens: [`../../brainstorm/brainstorm_brand-spine.md`](../../brainstorm/brainstorm_brand-spine.md)
