---
title: Microsite Factory — Infrastructure Research
version: 0.1
date: 2026-05-11
author: Becze Szabolcs (research by Claude + general-purpose agent)
status: research-complete · decision-pending
description: Cloudflare Pages vs Netlify összehasonlítás Microsite Factory-hoz. Direct Upload API, custom domain, staging, árazás. 5 statikus marketing site profilra.
id: 96c08ab2-3ef4-47fd-9353-ff7d9a2f51a0
index_schema_version: 1
---

# Infrastructure — Cloudflare vs Netlify

## Jelenlegi állapot (Netlify, DH design hub)

**Workflow (lásd `02_Areas/Deák Húsüzlet/CLAUDE.md`):**
- Tisztán API-alapú atomi zip-deploy, NEM git push CI/CD
- Site: `deakhus.netlify.app`, Site ID-vel és `NETLIFY_TOKEN`-nel
- Egyetlen `curl` POST `/api/v1/sites/{id}/deploys` Bearer token-nel, zip body
- Pre-deploy Python validator, build-szám sync (`index.html` inline MANIFEST vs `manifest.json`)
- Personal plan: $9/hó (frissítve 2026-04 óta), 1000 kredit/hó, 1 production deploy = 15 kredit → **~66 deploy/hó plafon**

**A profil amit le kell fednünk:**
- 5 statikus marketing site (Deák-szerű komplexitás)
- ~1000 unique visitor/site/hó (≈5k össz)
- ~100 deploy/hó össz (≈20/site)
- ~5 GB bandwidth/hó

## Cloudflare Pages — válasz a 6 kulcskérdésre

### 1. Direct Upload API

**Létezik**, de NEM egy darab zip endpoint mint Netlify-on — **4-5 lépéses flow**:

1. `GET /accounts/{id}/pages/projects/{name}/upload-token` — JWT lekérés (5 perc TTL)
2. Kliens-oldali manifest készítés: minden fájlhoz `path`, `contentType`, base64 body, hash (blake3 v. MD5), length
3. `POST /pages/assets/upload` — asset bucket batch (max 50 MB / batch)
4. `POST /pages/assets/upsert-hashes` — hash regisztráció
5. `POST /accounts/{id}/pages/projects/{name}/deployments` (multipart/form-data) — manifest + opcionális `branch=staging`

**Auth:** egyetlen API token, scope: `Account → Cloudflare Pages → Edit` (account-level, nincs per-project scope).

**Pragmatikus tanács:** A Microsite Factory Python wrappere mögött **Wrangler CLI headless hívás** (`npx wrangler pages deploy ./dist --project-name=X`) ugyanezt az API-t használja és letakarítja a 4-5 lépés bonyolultságát. Ha „no CLI, csak REST" hard requirement, a fenti recept teljes — de a Netlify-os 1-curl elegancia eltűnik.

### 2. Custom domain API

```bash
POST /accounts/{id}/pages/projects/{name}/domains
{"name":"deakhusuzem.hu"}
```

**DNS-feltételek:**
- **Apex (`example.com`):** KÖTELEZŐ Cloudflare zone (nameserver-csere a registrarnál, egyszeri)
- **Subdomain (`www.`, `staging.`):** mehet külső DNS-sel is CNAME-mel `<project>.pages.dev`-re

**SSL:** Universal SSL automatikus, ~15 perc–pár óra (általában percek).

**5 site-ra javaslat:** vidd át mind az 5 zónát Cloudflare DNS-re — ingyen, apex+staging alias mindenhol megy.

### 3. Staging deployment

**Elegánsabb mint Netlify-on.** Direct Upload-nál a `/deployments` POST-hoz `branch=staging` param → preview deploy. Két URL: immutable `<hash>.<project>.pages.dev` + alias `staging.<project>.pages.dev`.

**Custom subdomain a stagingre (`staging.deakhusuzem.hu`):** Pages dashboardban "custom branch alias" feature. **Feltétel: proxied Cloudflare DNS** (orange cloud). Külső DNS-en NEM megy.

**Promote staging → production:** nincs natív "promote" gomb. Második deploy `branch` paraméter nélkül, ugyanazokkal a hash-ekkel (asset-ek már upserted → gyors).

### 4. 5 site / 5 domain / 1 account

| Limit | Free | Pro |
|-------|------|-----|
| Projects/account | 100 soft | 100 soft |
| Custom domains/project | 100 | 250 |
| Preview deploys | korlátlan | korlátlan |
| Concurrent builds | 1 | 5 (Direct Upload-nál nem releváns) |

5 ≪ 100 projekt. **Architektúra: 1 projekt = 1 site** (külön history, rollback, domain-set).

### 5. Ár — a megadott profilra

**Cloudflare Pages: $0/hó.** A Free tier kényelmesen elviszi. Konkrétan:

- **Bandwidth: unlimited & free** (Cloudflare killer feature)
- **Builds: 500/hó Free-n.** DE: **Direct Upload NEM számít buildnek** — a Cloudflare nem clone-ozza a gitet, nem futtat build commandot. A "build" limit csak git-integrated projekteknél él. Direct Upload deploy darabszámra **nincs limit** Free-n (csak ~500/nap/projekt soft rate-limit).
- **Files/deployment:** 20,000 Free-n, 100,000 Paid-en. 5-20 HTML-hez közelébe sem ér.
- **Requests:** statikus asseteknek free & unlimited. Csak ha Pages Functions / SSR kell és túllépné a 100k req/nap-ot, akkor **Workers Paid $5/hó**.

**Tisztán statikus marketing landingnél gyakorlatilag soha nem ütközik fizetős küszöbbe.**

### 6. TCO összehasonlítás

| Tétel | Netlify Personal | Cloudflare Pages |
|-------|------------------|------------------|
| Havidíj alap | **$9** (frissítve 2026-04) | **$0** |
| 100 deploy/hó | +$5 overage (≈) | $0 |
| 5 GB bandwidth | benne van | $0 (unlimited) |
| 5 site, 5 domain | benne van | $0 |
| **Total/hó** | **~$14** | **$0** |
| **Éves** | **~$168** | **$0** |

Megtakarítás: ~$168/év, plusz **nincs deploy-cap stressz**.

## Gotchas

**Direct Upload:**
- Asset upload batch max 50 MB → batch-elni nagy site-on
- Single file max 25 MiB (landingnél irreleváns)
- ~500 deploy/nap/projekt soft rate-limit
- Multipart POST formattingre érzékeny — Pythonban `requests-toolbelt` MultipartEncoder ajánlott, NEM stdlib
- JWT 300s TTL → lassú kapcsolatnál refresh kellhet

**DNS / SSL:**
- Apex kötelezően Cloudflare zone
- Preview custom domain CSAK proxied Cloudflare DNS-en
- CNAME-bind előtt ne adj manuálisan CNAME-et → 522 error

**Cloudflare-specifikus:**
- HTML root path cache invalidation lassú lehet deploy után → `purge_cache` API call ajánlott
- Nincs natív atomic rollback gomb — `/deployments/{id}/retry`-szerűen megy, működik, csak nem one-click
- Project név immutable, része a `*.pages.dev` URL-nek
- API token account-szintű (Pages Edit) — egy compromised token mind az 5 site-ra érvényes. **Workaround:** külön Cloudflare account per ügyfél, vagy Cloudflare for Teams.

**Mit NEM kapsz Netlify-hoz képest:**
- 1-curl atomic zip deploy (4-5 hívás kell)
- Form submissions backend
- Beépített A/B split testing

## Ajánlás

**Go: Cloudflare Pages.** $0 vs $14/hó, unlimited bandwidth, jóval nagyobb deploy-headroom. Az egyetlen reális tradeoff: a Direct Upload Python wrapper komplexebb (4-5 lépés vs 1) — de **egyszeri implementációs munka**, utána absztrahálva ugyanúgy „egy parancs" lesz a Microsite Factory-ból.

**Kompromisszum-opció:** Direct Upload helyett **Wrangler CLI subprocess hívás** — minden API-tisztaságot megőriz a workflow szintjén, csak `npx wrangler` dep-pel többet ad.

## Architektúra-vázlat (Cloudflare-en)

```
Microsite Factory (Python wrapper)
  ├── impeccable polish (local)        ← capability-import
  ├── pre-deploy-check.py              ← portolva DH-ról
  ├── deploy.py
  │     ├── --branch=staging           → staging.<project>.example.com (CF preview alias)
  │     └── --production               → example.com (CF Pages production)
  └── per-site config (project_id, custom domain)
```

**Per-ügyfél izoláció:**
- 1 Cloudflare projekt / ügyfél (vagy / kampány)
- 1 zone / ügyfél domain — Cloudflare DNS-re átvíve
- Token-stratégia kérdés még nyitva: egy account-szintű vs ügyfél-szintű account-ok

## Források

- [Cloudflare Pages REST API overview](https://developers.cloudflare.com/pages/configuration/api/)
- [Direct Upload (Pages docs)](https://developers.cloudflare.com/pages/get-started/direct-upload/)
- [Reverse-engineering the CF Pages Deployment API — Hunter Shaw](https://hunterashaw.com/reverse-engineering-the-cloudflare-pages-deployment-api/)
- [API: Add domain endpoint](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/create/)
- [Add a custom domain to a branch](https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/)
- [Pages Limits](https://developers.cloudflare.com/pages/platform/limits/)
- [Pages Functions Pricing](https://developers.cloudflare.com/pages/functions/pricing/)
- [Netlify pricing update — April 2026](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/)

## Cloudflare account snapshot (Exarlabs@gmail.com, 2026-05-11)

- **Account ID:** `f2166aa3fcc9e0e7b888aaaeb4db0517`
- **Plan:** Workers Free (100k req/nap)
- **Workers/Pages projektek:** 0 (tiszta lap)
- **R2:** 1 bucket előzményi (`future-builders-backups`, EU) — backup, NEM Microsite Factory
- Account szinten elérhető és releváns: Web Analytics, Zaraz, WAF, Email Routing, Turnstile, Secrets Store, Bulk redirects, Audit logs, Custom dashboards (New), Trace (Beta), AI Gateway, Workers AI, Browser Run, Workflows

### Microsite Factory feature-prioritás

**Essential:** Workers & Pages · Domains/Registrations · Account API tokens
**Erősen hasznos:** Web Analytics · R2 · Workers KV · D1 · Workers (form handler) · Email Routing · Email Sending (Beta) · Images/Transformations · Turnstile · Secrets Store · Zaraz · WAF · Bulk redirects · Notifications · Audit logs
**Érdekes később:** AI Gateway (LLM observability) · Workers AI (CF saját LLM) · Vectorize/AI Search (in-site RAG) · Workflows (deploy pipeline durable engine) · Browser Run (pre-deploy Lighthouse + screenshot) · Stream
**Irreleváns nálunk:** Magic Networks, VPC, Hyperdrive, Tunnels, Mesh, Load Balancing, Pipelines, RealtimeKit, TURN, MoQ, Workers for Platforms, Containers, Durable Objects, Queues, Zero Trust

### Két ki nem aknázott „felhő" lehetőség

- **Browser Run** — headless Chrome a CF edge-en → automatikus Lighthouse audit, screenshot, visual regression test pre-deploy validator-ként
- **Workflows** — a Microsite Factory deploy pipeline-ja CF-en futhat (build → polish → upload → deploy → DNS check → cache purge → notify) durable módon, nem csak lokálisan a Python wrapperben

## Open follow-ups

- [ ] Token-stratégia: egy account-token mind az 5 site-ra vs külön CF account ügyfelenként
- [ ] Wrangler CLI subprocess vs raw REST API — végleges döntés a Python wrapperhez
- [ ] Cache-purge automatika a deploy után (Cloudflare API)
- [ ] Rollback mechanizmus tervezése
- [ ] Per-site config formátum (TOML/YAML/JSON)
