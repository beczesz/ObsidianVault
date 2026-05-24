---
title: Microsite Factory — Web Publishing Capability
version: 0.1-draft
date: 2026-05-11
author: Becze Szabolcs
status: design
description: BDOS capability — AI-assisted microsite generálás, polish, deploy és domain-binding. Brand-név: Microsite Factory. Bármely BDOS-projekt használhatja. Későbbi Ignis Academy tananyag-export gazdája.
id: c3429101-4288-4d8c-a8b7-d6f266eb69a7
index_schema_version: 1
---

# Microsite Factory

> **Mappanév (canonical):** `web-publishing` · **Brand-név (user-facing):** Microsite Factory

> **Státusz:** design / kidolgozás alatt. A pipeline-t és az agent-palettát még tervezzük.

> **Upstream:** [Brand Spine](../brand-to-site/CLAUDE.md) — az „mit építünk és miért" réteg. A Microsite Factory ott veszi át a folyamatot, ahol a Brand Spine 8. rétege (build + polish) átadja a kész HTML-t: deploy → DNS → SSL → analytics.

## Cél

Egy **replikálható munkamódszer + agent-csomag**, ami AI-eszközökkel teljes microsite életciklust kezel: ötlet → HTML generálás → polish → deploy → custom domain → SSL → analytics. Egy account, sok kliens, parancssorból orchestrálva.

Forrás-insight: ChatGPT brainstorm 2026-05-10 ([Cloud Code Desktop vs CLI](https://chatgpt.com/c/6a004d97-9838-8391-bcdd-e4fac1b1fce5)) — *„amit építesz, az gyakorlatilag kezd hasonlítani egy AI-assisted microsite deployment platformra."*

## Architektúra (working draft)

```
Claude Code  →  Impeccable polish  →  Deploy agent  →  Cloudflare/Netlify API
   ↓                  ↓                    ↓
generálja a       a11y / hierarchy /   Pages deploy + DNS bind + SSL +
landing HTML-t    visual polish        analytics aktiválás
```

Kettős hosting stratégia (ChatGPT javaslat):
- **Netlify** — development sandbox (preview deploy, design iteráció)
- **Cloudflare Pages** — production edge factory (API-first, granular tokenek, multi-domain orchestration)

## Tervezett agentek (todo)

| Agent | Felelősség |
|-------|------------|
| **Deploy Agent** | Pages deploy, build artefakt feltöltés, deploy-token kezelés |
| **Domain Agent** | DNS API hívások, SSL aktiválás, subdomain creation |
| **Polish Agent** | a11y, hierarchy, copy review — `impeccable` skill-re épülhet |
| **SEO Agent** | metadata, Open Graph, structured data generálás |

Még nincs eldöntve, melyik valódi BDOS-agentként élesedik (`agents/<name>.md`) és melyik marad skill / inline workflow.

## Precedens minták (a vault-ban már létezik)

- **Sonrisa CPS website workflow** — `02_Areas/Sonrisa/CPS/Marketing/website/CLAUDE.md` (HTML komponens-könyvtár, verziókövetés, Sellvio CMS)
- **DH design hub** — deakhus.netlify.app, Netlify deploy pipeline már él
- **`impeccable` skill** — UI/UX polish, már beépítve

Ezeket fogjuk absztrahálni egy projekt-független methodology-vá.

## Open questions

- [x] Név (user-facing): **Microsite Factory** ✅ (2026-05-11, Szabolcs)
- [ ] Cloudflare vs Netlify végleges választás — **research kész**, ajánlás: Cloudflare ($0 vs $14/hó). Lásd [infrastructure.md](infrastructure.md). *Felhasználói döntés folyamatban.*
- [ ] Hány agent szükséges valójában? (deploy + domain összevonható?)
- [ ] Repo-struktúra: monorepo (egy repo sok site-tal) vagy per-kliens?
- [ ] Token-stratégia: account-level vagy per-kliens?
- [ ] Ignis Academy tananyag-export formátum (mikor és hogyan)?

## Struktúra

```
capabilities/web-publishing/
├── CLAUDE.md            ← ITT — meta, belépő
├── infrastructure.md    ✅ Cloudflare research + dashboard-térkép
├── prototype/           ✅ microsite_deploy.py + README — működő (untested) skeleton
├── methodology.md       ✅ 13 szekciós tanulási prompt — fázisok, multi-session, anti-patternek, példa
├── requirements.md      ✅ developer-handoff brief — funkcionális + nem-funkcionális reqs
├── agents/              (TODO — deploy-, domain-, polish-, seo-agent)
└── teaching/            (TODO — későbbi Ignis Academy tananyag-export)
```

## Hivatkozott

- BDOS belépő: [`../../CLAUDE.md`](../../CLAUDE.md)
- Forrás brainstorm: [Cloud Code Desktop vs CLI (ChatGPT)](https://chatgpt.com/c/6a004d97-9838-8391-bcdd-e4fac1b1fce5)
- Sonrisa precedens: [`../../../../02_Areas/Sonrisa/CPS/Marketing/website/CLAUDE.md`](../../../../02_Areas/Sonrisa/CPS/Marketing/website/CLAUDE.md)
