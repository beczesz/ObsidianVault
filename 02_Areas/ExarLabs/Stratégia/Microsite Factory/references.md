---
title: References — Microsite Factory
description: "Collection of internal capability documentation, infrastructure decisions, and strategic references for the Microsite Factory project, including Brand Spine framework, live precedent from Sonrisa CPS, deployment skeleton, and positioning within ExarLabs' 2026 strategy targeting SMBs in healthcare and other industries."
description_source: auto
description_hash: d53628e83bd62043
type: references
created: 2026-05-16
id: cfbe582a-01a5-4574-9e53-5f8bff922f48
index_schema_version: 1
---
# References — kapcsolódó vault anyagok

## Belső capability (BDOS — eszköz oldal)

- **[web-publishing/CLAUDE.md](../../../00_Prompts/BDOS/capabilities/web-publishing/CLAUDE.md)** — A Microsite Factory capability fő leírása. AI-asszisztált microsite életciklus (HTML generálás → polish → deploy → DNS → SSL → analytics). Status: design.
- **[web-publishing/infrastructure.md](../../../00_Prompts/BDOS/capabilities/web-publishing/infrastructure.md)** — Cloudflare Pages vs Netlify kutatás. Döntés: CF Pages. Per-ügyfél izoláció, TCO $0.
- **[web-publishing/requirements.md](../../../00_Prompts/BDOS/capabilities/web-publishing/requirements.md)** — Developer requirements brief, F1-F10 MUST, tech stack döntések.
- **[web-publishing/prototype/](../../../00_Prompts/BDOS/capabilities/web-publishing/prototype/)** — Működő (untested) Python deploy skeleton, microsite_deploy.py.

## Upstream réteg (Brand Spine)

- **[brand-to-site/CLAUDE.md](../../../00_Prompts/BDOS/capabilities/brand-to-site/CLAUDE.md)** — Brand Spine v0.3, 7 réteg + Lean/Standard/Premium tier. Lean tier kifejezetten kisvállalkozásoknak. Maestro agent v0.1 LIVE.

## Élő precedens

- **[Sonrisa CPS Website](../../Sonrisa/CPS/Marketing/website/CLAUDE.md)** — Élő, működő példa (sonrisa.hu/en/cps-services). HTML komponens-könyvtár, Sellvio CMS, deploy workflow, verification script. A Microsite Factory ezt absztrakálja.

## Stratégiai kontextus

- **[ExarLabs/Stratégia/Stratégia 2026.md](../Stratégia%202026.md)** — Egészségügy (fogászat) explicit célpiac. "€5000-es weboldal most €20-ért elkészíthető" — value prop alapja.
- **[ExarLabs/Stratégia/Területek.md](../Területek.md)** — Boring tech analógiák: OpenTable, Fresha, Mindbody. Template-elhetőség más iparágakra.
- **[Deák Platform pilot-concept](../../resources/Deák%20Platform/pilot-concept.md)** — Boring tech for local SMB pilot. Validációs sablon — "if the model works → validated template for other local businesses."

## BMC sablon-példa

- **[BMC - Ignis Academy v2.3](../../resources/Ignis%20-%20LMS/BMC%20-%20Ignis%20Academy%20-%20v2.3.md)** — Strukturális BMC példa más ExarLabs ventureből. Value Proposition, Customer Segments, Revenue Streams struktúra.

## Külső források (importálandó)

- **ChatGPT chat (2026-05-16):** https://chatgpt.com/c/6a004d97-9838-8391-bcdd-e4fac1b1fce5
  - Status: import folyamatban
- **BUSINESS_PLAN.md (Downloads, 2026-05-15):** lokálisan a /Downloads-ban → bemásolva ebbe a mappába is.
