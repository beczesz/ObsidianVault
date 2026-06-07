---
title: "DEMO CAMPAIGN — BDOS Positioning Q2 2026"
schema: presto.campaign.v2
campaign_id: bdos-positioning-q2-2026
date: 2026-05-25
author: Becze Szabolcs
status: draft
description: Demonstrációs példa-kampány. A BDOS Q2 2026 pozícionálási esernyő-kampánya, amely a markdown-as-substrate tézist terjeszti LinkedIn, X és blog csatornákon, ExarLabs és Personal területeken.
id: a8f53664-1ce5-4d32-ba7d-3a1208e64fd2
index_schema_version: 1
bdos_index: false
example: true
# ============================================================
# PLACEHOLDER / ILLUSTRATIVE EXAMPLE
# Ez a fájl a Marketing Engine v0.2 modell demonstrációja.
# Nem valódi kampány-elem — a status: example és example: true
# mezők jelzik ezt minden agentnek és olvasónak.
# ============================================================

seed_id: seed-2026-05-25-001

intents:
  - goal: thought-leadership
    area: ExarLabs
    notes: "Technical-philosophical positioning — BDOS mint AI-native metodológia"
  - goal: community
    area: Personal
    notes: "Developer community connection — X thread formátum, közvetlen hang"
  - goal: seo-lead-gen
    area: ExarLabs
    notes: "Organikus elérés — blog formátum, keresési szándék: AI-native operations"

areas:
  - ExarLabs
  - Personal

channels:
  - linkedin
  - x-twitter
  - blog

publications:
  - publication_id: linkedin-2026-05-28-001
    area: ExarLabs
    channel: linkedin
    publication_status: draft
  - publication_id: x-2026-05-29-001
    area: Personal
    channel: x-twitter
    publication_status: draft
  - publication_id: blog-2026-06-01-001
    area: ExarLabs
    channel: blog
    publication_status: draft

stage: draft
status: in_progress

start_date: 2026-05-25
target_end_date: 2026-06-30

kpi_targets:
  total_reach: 8000
  total_leads: 15
  avg_engagement_rate: 0.055
  linkedin_impressions: 3000
  x_impressions: 2000
  blog_organic_visits: 3000

owner: Becze Szabolcs
tags: [bdos, positioning, markdown, q2-2026, thought-leadership]
---

## Brief

**Stratégiai szándék:** A BDOS metodológia — különösen a markdown-as-substrate alapelv — externális kommunikációban megjeleníteni. A célközönség azok a tech-vezető és fejlesztő profik, akik AI-native operations iránt érdeklődnek, de nem találnak konkrét, implementálható keretrendszert.

**Egységes narratíva:** "A legjobb AI-rendszer nem az AI fejében él — hanem a fájlrendszerben. A BDOS ezt az alapelvet viszi operacionális szintre."

**Per-Area adaptáció:**
- ExarLabs: technikai-filozofikus hang, angol, thought-leadership + SEO
- Personal: közvetlen fejlesztői hang, vegyesen (hu/en), community-building

**Miért most:** Q2 2026 — a BDOS Phase 3+ fázisban van, elég érett a külső kommunikációhoz. Az ExarLabs brand-building szempontjából ideális időpont a "AI-native company operations" narratíva megnyitásához.

## Coordination notes

**Egységes elemek:**
- A markdown-as-substrate tézis mindhárom publication-ben a mag
- Ugyanaz a szándék, különböző mélység: X thread = hook, LinkedIn = narratíva, Blog = teljes kifejtés
- Cross-linking: a blog poszt hivatkozza a LinkedIn-t és vice versa (ha published)

**Per-Area különbség:**
- LinkedIn (ExarLabs) — hosszú forma, technikai-filozofikus, angol, linked atomic-hoz
- X thread (Personal) — short burst sorozat, fejlesztői közeg, magyar/angol mix
- Blog (ExarLabs) — long-form, SEO-optimalizált, konkrét code examples / file struktúra

## Results summary

(kampány lezárásakor töltendő ki)

## Iteration history

- 2026-05-25 10:00 — created as example/demo by presto marketing-engine-v2 substrate build
