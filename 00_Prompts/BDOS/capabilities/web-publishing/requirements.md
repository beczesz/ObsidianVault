---
title: Microsite Factory — Developer Requirements Brief
version: 0.1
date: 2026-05-12
author: Becze Szabolcs
status: draft
audience: fejlesztő (külső / partner)
description: Egy oldalas tömör átadó-dokumentum. Mit építünk, miért, mit kérünk a fejlesztőtől.
id: feb06603-5bd7-4e53-9bc4-ccdf274bda60
index_schema_version: 1
---

# Microsite Factory — Developer Requirements

## 1. Mit építünk

Egy **AI-asszisztált microsite-gyárat** — eszközcsomag amellyel egy ember (jelenleg Szabolcs) 1-2 óra alatt egy új marketing landing oldalt képes kiadni egy ügyfél domain-jére, ismételhető workflow-val.

Nem CMS, nem SaaS termék, nem ügyfélnek eladott szoftver. **Belső operatív eszköz** — a saját üzletfejlesztési és pályázati / marketing munkáinkat gyorsítja.

## 2. Üzleti cél

- Kampány-microsite-okat *órák alatt*, ne hetek alatt, indítsunk
- 5+ párhuzamos ügyfél / kampány microsite menedzselhető egy emberrel
- Minden microsite ugyanolyan struktúrával — egyszerű kézbevétel, csere, javítás
- Költség: a teljes hosting/infra havidíj <$10 az első 5-10 microsite-ig
- Tananyaggá lehessen tenni az Ignis Academy oktatási vonalához (későbbi cél)

## 3. Tech stack — eldöntött

- **Hosting:** Cloudflare Pages (statikus HTML/CSS/JS, Direct Upload API)
- **DNS / SSL:** Cloudflare (a domain-ek átkerülnek CF zone-ba)
- **Build:** nincs framework — vanilla HTML/CSS/JS. Opcionális minimal asset-pipeline (cp / minify).
- **Deploy script:** Python (`microsite_deploy.py`), CF Pages REST API, atomi zip-szerű deploy
- **Token:** account-szintű API token (Pages: Edit, Workers Scripts: Edit), `.env`-ben tárolva
- **Verziókezelés:** semver + monoton build számláló (manifest.json)
- **Form-handling / dynamic:** Cloudflare Workers (későbbi iteráció)
- **Analytics:** Cloudflare Web Analytics + opcionálisan Zaraz (server-side GA/Meta Pixel)
- **Form captcha:** Cloudflare Turnstile (későbbi)
- **Image-optimalizáció:** Cloudflare Images / Transformations (későbbi)

**Nem használunk:** Vercel, Netlify (jelenleg DH design-hubon van Netlify, ezt migráljuk), AWS, Next.js, Astro, Webflow, Wordpress.

## 4. Funkcionális követelmények

### MUST (v0.1 — első verzió)

- [F1] **Új microsite projekt** létrehozható egy template-skeletonból egy paranccsal
- [F2] Minden microsite projekt **azonos struktúrát** követ (`src/`, `dist/`, `brief.md`, `microsite.config.json`, `manifest.json`, `history.md`)
- [F3] **Lokális preview** — szerkesztés közbeni élő (auto-reload nem feltétlen, de fájl-megnyitás OK)
- [F4] **Pre-deploy validáció** — script (`pre-deploy-check.py`) ellenőrzi: index.html létezik, asset-ek feloldhatók, meta-tagek kitöltve, manifest build-szám sync. Failure esetén exit 1 → deploy nem indul.
- [F5] **Staging deploy** — egy paranccsal a `<project>.pages.dev` staging alias-ra (vagy `staging.<custom-domain>`-re ha be van kötve). Custom branch név `staging` (CF Pages preview deployment).
- [F6] **Production deploy** — egy paranccsal a production custom domainre (`<custom-domain>`).
- [F7] **Custom domain bind** — CF API-n a Pages projekthez köthető a végleges domain (apex + www + staging.)
- [F8] **SSL aktiválás** — Cloudflare Universal SSL automatikusan a kötés után
- [F9] **Deploy history** — `history.md`-be írja a build, dátum, deploy ID, változás-summary, deploy-státusz
- [F10] **Rollback** — Cloudflare deployment history alapján visszaállítható egy előző build (jelenleg dashboardon, később API-ból)

### SHOULD (v0.2)

- [F11] **Site registry** — egy központi fájl/script ami listázza az összes microsite-ot (név, ügyfél, státusz, prod URL, utolsó deploy dátum, CF projekt ID)
- [F12] **Cache purge automatika** — production deploy után CF zone-cache purge HTML root path-okra
- [F13] **Lighthouse audit** — deploy után automatikus Lighthouse score generálás (CF Browser Run-nal)
- [F14] **A/B variant deploy** — két variáns ugyanazon URL-en, CF Workers split

### MAYBE (v0.3+)

- [F15] **Form-handler Worker** — lead-form POST → CF Worker → email forward + opcionális D1 tárolás
- [F16] **Visual regression testing** — Browser Run screenshot + diff
- [F17] **Multi-language site** (`/hu/`, `/en/`)
- [F18] **Slack / Telegram deploy-notification**

## 5. Non-functional követelmények

| Téma | Cél |
|------|-----|
| **Lighthouse Performance** | >90 mobile, >95 desktop |
| **Lighthouse Accessibility** | >95 |
| **Lighthouse SEO** | >95 (meta + OG + sitemap) |
| **Lighthouse Best Practices** | >95 |
| **Page weight (compressed)** | <500 KB hero LCP-ig |
| **First Contentful Paint** | <1.5s 4G-n |
| **Time to Interactive** | <2.5s 4G-n |
| **Mobile-first** | minden design 320px-től induljon |
| **Browser support** | utolsó 2 verzió: Chrome, Safari, Firefox, Edge |
| **GDPR** | cookie-banner csak ha tényleg kell — alapesetben CF Web Analytics elég, no cookies |
| **a11y** | semantic HTML5, alt-szöveg minden képnél, color contrast WCAG AA, fókusz-stílusok |

## 6. Workflow a fejlesztő szempontjából

Egy új microsite-ot a fejlesztő így vesz át / fejleszt tovább:

1. Claude Code al fejleszthet
2. Claude Code al deployolható
3. Minimális effort
4. Maximáis idő a designon és a tartalmán az oldalnak.

**Token kezelés:** a CF token NEM kerül commit-ba. A `.env` fájlt Szabolcstól külön kapja meg a fejlesztő (1Password vagy hasonló secret-share-en). A `.env.example` mutatja a struktúrát.

## 7. Mit NEM kell csinálni (kizárások)

- ❌ NE válaszd át a hosting-ot (Netlify, Vercel, AWS) — Cloudflare-en maradunk
- ❌ NE adj hozzá framework-öt (Next, Astro, Vue, React) v0.1-ben
- ❌ NE használj inline JavaScript-et `index.html`-ben — minden JS külön fájlban
- ❌ NE használj stock-fotót — minden image valós (kliens / Szabolcs adja)
- ❌ NE adj hozzá Google Analytics scriptet közvetlenül — CF Web Analytics vagy Zaraz az engedélyezett útja
- ❌ NE deploy-olj egyenest production-re; mindig staging-en át
- ❌ NE töröld / módosítsd a régi deploy-okat CF dashboardon (audit history)
- ❌ NE használj jQuery-t vagy más legacy lib-et
- ❌ NE commit-old a `.env`-et, tokent, kulcsot

## 8. Acceptance criteria — egy microsite „kész"

Egy microsite-ra azt mondjuk hogy „kész és publikálható", ha:

1. ✅ Pre-deploy-check passes
2. ✅ Staging URL működik, két különböző böngészőben + 1 valódi mobile-on tesztelve
3. ✅ Lighthouse score teljesíti az 5. pont küszöbeit
4. ✅ Custom domain (prod + staging) be van kötve, SSL aktív
5. ✅ `history.md` aktualizálva
6. ✅ `microsite.config.json` `version` mező bumpolva
7. ✅ Szabolcs jóváhagyása dokumentálva (`history.md`-ben + ügyfél-jóváhagyás külön)

## 9. Atadás-mód

A fejlesztő kapja:
- ✏️ **Ez a `requirements.md`** (ez a fájl)
- 📖 **`methodology.md`** — részletes munkamódszer (5 fázis, anti-patternek, konkrét példa)
- 🏗️ **`infrastructure.md`** — Cloudflare API, dashboard-térkép, gotchas
- 🐍 **`prototype/microsite_deploy.py`** — deploy script
- 🔐 **`.env`** — token + account ID (külön csatornán, NEM email/chat/git)
- 🌐 **CF dashboard read-only invite** — opcionális, ha látnia kell a deploy-státuszokat
- 📁 **Példa-projekt** — első sikeres microsite (pl. `02_Areas/Deák Húsüzlet/microsite-husvet-2026/`) referencia-ként

## 10. Open questions a fejlesztőnek

Kérlek, miután átolvastad, válaszolj az alábbiakra (e-mailben / dokumentumban):

1. Van-e tapasztalatod **Cloudflare Pages Direct Upload API-val**? (Ha nem, ez egy 5-lépéses flow — a `microsite_deploy.py` mutatja.)
2. Mennyi időt becsülnél **egy átlagos microsite végigvitelére** (brief → prod, ~5 oldalszekció, lead-form)?
3. Van-e javaslatod a **template-stratégiára** (egy general skeleton, vagy 3-5 témamódú)?
4. Mit változtatnál a `microsite_deploy.py` scripten? (Hibakezelés? Logging? Progress UI?)
5. Vállalsz-e **24-órás SLA-t** staging deploy-okra production-ben lévő microsite-ok hotfix-jeire?

## 11. Időkeret, költség

- v0.1 működő prototípus: **2026-05** (mostani sprint)
- Első éles microsite (DH-húsvét vagy Sonrisa-llmaas) production-ben: **2026-05-30**
- v0.2 (site registry, cache purge, Lighthouse audit): **2026-06**
- Becsült teljes capability-fejlesztési óraidő (Szabolcs + külső fejlesztő közösen): **40-60 óra v1.0-ig**

Cloudflare havi költség első 5 microsite-on: **$0** (Free tier elég).

---

## Kapcsolat

**Capability owner:** Becze Szabolcs (beczesz.szabolcs@gmail.com)
**BDOS belépő:** [`../../CLAUDE.md`](../../CLAUDE.md)
**Capability belépő:** [`CLAUDE.md`](CLAUDE.md)
