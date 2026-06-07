---
title: YouTube Skill — Integration Candidates (temp tracker)
date: 2026-05-27
author: Becze Szabolcs
status: review
description: Ideiglenes tracker arról, mit érdemes a `/youtube` skill (Agrici Daniel, 14 sub-skill + 9 reference) anyagából a BDOS-be (Presto/Navigator runbook/Channel DNA/Sage learnings) integrálni. Mind a 14 sub-skill értékelve 2026-05-27.
tags: [bdos, youtube, skill-evaluation, integration-plan]
id: b1cbb45f-6e61-4500-a8db-9edf43041ab5
index_schema_version: 1
---

# YouTube Skill — Integration Candidates

Cél: a `~/.claude/skills/youtube/` (Agrici Daniel, 14 sub-skill + 9 reference) sub-skillenként eldönteni mit emelünk át a BDOS-be.

## Status — TELJES (14/14 értékelve)

| # | Sub-skill | Fit | Verdict | Integráció-célpont |
|---|-----------|------|---------|---------------------|
| 1 | `analyze` | 🔴 | Generic, nem fit. API-lag aware-ség hiányzik. | **Nem integrálandó.** Saját pub-snapshot template + channel.md baseline erősebb. |
| 2 | `repurpose` | 🟡 | 1/7 platform fit (Shorts only). Blog/email/podcast/community = üres halmaz. | **Részleges**: Shorts hook-quality 3-pillér + cadence pattern → reel-factory + runbook |
| 3 | `hook` | 🟡 | Theory jó, English spoken-word-re kalibrált | **5-mechanizmus taxonómia** → `navigator-podcast:hook-v0.4` |
| 4 | `thumbnail` | 🟢 | Synergy + mobile-legibility értékes | **5 synergy rule + 168×94px test** → Navigator-YT.md thumbnail §4 |
| 5 | `competitor` | 🟢 | **NINCS alternatíva nálunk** — anchor value-prop | **Teljes integráció**, magyar versenytársakkal. Lehet: `/pres-competitor` Presto skill |
| 6 | `ideate` | 🟡 | Keyword-trend ≠ Navigator guest-based | **Composite score framework (/40)** → Sage atomic ranking |
| 7 | `seo` | 🟡 | Navigator-plugin dedikáltabb magyarul | **JSON-LD VideoObject + 10-15 tag stratégia** → navigator-plugin |
| 8 | `script` | 🔴 | Long-form interjú ≠ retention-engineered short | Nincs |
| 9 | `strategy` | ❌ | Strategic North Star v0.1.0 erősebb | Nincs |
| 10 | `calendar` | ❌ | Runbook + Marketing Board calendar erősebb | Nincs |
| 11 | `shorts` | 🟡 | Reel-Factory capability létezik | **Viewed-vs-Swiped >60% + 13s/60s + loop setup** → reel-factory LEARNINGS.md |
| 12 | `monetize` | 🔴 | US-bias (RPM/CPC, brand deals) | Nincs |
| 13 | `audit` | 🟡 | Fázis 4a lefutott, Q2-Q3-ra | 4-agent recipe megőrizve, futás nem aktuális |
| 14 | `metadata` | 🟡 | Navigator-plugin dedikáltabb | **Pre-publish 14-item SEO checklist** → runbook §pre-publish gate |

## Reference fájlok (9 db)

| File | Tartalom | Érték BDOS-nek |
|---|---|---|
| `references/algorithm-guide.md` | 3-system architecture, CTR/AVD benchmarks, 2024-2025 changes | 🟢 Magas — Navigator-YT.md ref |
| `references/seo-playbook.md` | Title/desc/tags/chapters/hashtags + VideoObject schema | 🟢 Magas — Navigator-YT DNA |
| `references/retention-scripting-guide.md` | Hook frameworks, pattern interrupts | 🟡 Közepes — long-form ≠ short |
| `references/thumbnail-ctr-guide.md` | CTR by niche, face psychology, A/B testing | 🟢 Magas — Navigator-YT thumbnail §4 |
| `references/shorts-playbook.md` | Shorts algorithm, format specs | 🟢 Magas — reel-factory |
| `references/analytics-guide.md` | Metrics hierarchy, funnel ratios, RPM/CPM | 🟡 Közepes — channel.md ref |
| `references/monetization-guide.md` | YPP tiers, brand deal rates | 🔴 Alacsony — US-bias |
| `references/repurposing-guide.md` | Hub/Hero/Help, cross-platform workflows | 🟢 Magas — runbook |
| `references/dataforseo-integration.md` | DataForSEO MCP tool reference | 🟡 Közepes — csak ha DataForSEO MCP-t integrálunk |

## Konkrét átemelési items (per integration-target)

### A) `Navigator-YT.md` Channel DNA
- `algorithm-guide.md` ref pointer + key benchmark táblázat
- `seo-playbook.md` title/desc/tags/chapters rules
- `thumbnail-ctr-guide.md` face psychology + 5-rule synergy check + 168×94px test
- `analytics-guide.md` benchmark források

### B) `Marketing/Runbooks/episode-launch.md`
- **Pre-publish 14-item SEO checklist** (metadata.md-ből)
- **Repurpose Hub/Hero/Help workflow** (repurposing-guide.md-ből)
- **Reel-cadence** (Clip 1 elsőre, 2-3 nap spacing) — már korábbi feltételezésnek
- **§T+1 reel-wave**: viewed-vs-swiped >60% threshold

### C) Navigator-plugin (`/hook`, `/thumbnail`, `/leiras`, `/cim`)
- **`/hook-v0.4`**: 5-mechanism taxonómia (Shock/Problem-Agitation/Story-Open/Curiosity-Gap/Social Proof)
- **`/leiras`-v0.4**: JSON-LD VideoObject schema generálás
- **`/cim`-v0.4**: 10-15 tag prioritized + tag character-budget validator
- **`/thumbnail`-v0.4**: synergy check (title↔thumbnail info-split) + mobile-legibility test

### D) `capabilities/reel-factory/LEARNINGS.md`
- **Shorts hook-quality 3-pillér** (scroll-stop 1-3s / standalone / loop setup)
- **Viewed-vs-Swiped >60% prediction threshold**
- **13s/60s sweet spot rule, 30-45s dead zone elkerülése**
- **Visual change min 3s rule**

### E) Új Presto skill: `/pres-competitor` (Phase 2 candidate)
- 4-agent recipe (top-video / keyword-gap / format-gap / audience-gap)
- Magyar versenytárs lista bootstrap: Csakabaj, Bulvár Pszichológia, Hangoló, stb.
- DataForSEO MCP-vel ha élesítünk, vagy manual via Chrome MCP

### F) Sage cognition layer
- **Composite score framework (Search × CTR × Feasibility × Niche × /40)** — atomic ranking-ra adaptálva

## Skill maradjon vagy menjen?

**Javaslat: MARADJON, mint reference-library.**

- A 9 reference fájl önmagában is érték (markdown, olvasható, ha mástól nem hivatkozunk rá)
- A `/youtube competitor` egyedi capability — nincs nálunk alternatíva
- Az integráció **NEM teljes átemelés** — a reference-ek a helyükön maradnak (`~/.claude/skills/youtube/`), és a Navigator-plugin/runbook **rájuk hivatkozik** (link), nem duplikálja
- Slash command-ot **nem készítünk** a többi 13 sub-skillre — eseti `Skill(youtube, args=...)` hívás elég

## NE integrálódjon

- Bármi US-monetization (RPM/CPC, brand deal rate cards)
- DataForSEO MCP-függő funkciók amíg nincs DataForSEO MCP setup
- `script`, `strategy`, `calendar` sub-skillek (duplikáció / nem-fit)

## Plugin #2 — `claude-code-youtube-mcp` (wynandw87) — 2026-05-28

**Verdict: NE installáljuk most.**

- Repo clean (TS + @modelcontextprotocol/sdk + zod, postinstall ártalmatlan banner)
- Anchor value-prop = `get_most_replayed` heatmap, **igényel ~50K view/videó** — Navigator csúcs ~10K. Üres adat.
- 10 tool blokkolt (kvótád 0, Google audit)
- 5 tool duplikálja `mcp__youtube__` (pauling-ai) MCP-t
- Repo marad `/tmp/claude-code-youtube-mcp/` alatt, 2 perc install ha kell

**Mikor újragondolni:** Navigator 50K+ view-s videó / kvóta-rendezés / competitor (Csakabaj) heatmap-elés.

## Plugin #3 — `claude-video` (`/watch`, Brad Automates) — 2026-05-28

**Verdict: 🟢 MEGTARTVA — valódi új capability.**

- Telepítve manuálisan: `~/.claude/skills/watch/` (natív Claude Code plugin, nincs npm build)
- **Vizuális videó-megértés** — Claude Read-eli a frame-eket JPEG-ként. SEMMI eddigi eszköz nem adta.
- Komplementer a reel-factory-val: az **gyárt** (reel.mp4), ez **lát** (frame understanding).
- Smoke-test EP43 0:00–0:30: frame extraction ✅, focused-mode ✅. Caption 429 (yt-dlp rate-limit, transient).
- **Patch:** lokális faster-whisper `large-v3-turbo` backend hozzáadva (eredetileg API-only). Offline, ingyen, magyar ASR. Patch őrizve: `capabilities/reel-factory/patches/`.
- **faster-whisper 1.2.1 telepítve** (`pip install --user`).

**Use case-ek:** versenytárs-hook elemzés, saját reel-preview publikálás előtt, thumbnail-moment vadászat, hook retroaudit.

**Gap:** caption-429 (yt-dlp JS-runtime hiány → `deno` telepítése segíthet). Saját epizódoknál van full SRT, ott nem számít.

## 3-plugin összefoglaló — mivel lettünk gazdagabbak

| Plugin | Net új capability | Verdict |
|---|---|---|
| **claude-youtube** (14 sub-skill) | Referencia-tudás + 1 egyedi (`competitor` recipe) | 🟡 Reference-library, cherry-pick |
| **claude-code-youtube-mcp** | Semmi használható (heatmap 50K-view-t kér, kvóta 0) | 🔴 NEM telepítve, `/tmp`-ben |
| **`/watch`** | **Vizuális videó-megértés** — valódi új érzékszerv | 🟢 Élesben, lokális-Whisper patch-csel |

**Bottom line:** 3 pluginból ~1.5 hozott valódi értéket. `/watch` = az igazi nyereség. claude-youtube = tudás-réteg integrálásra. claude-code-youtube-mcp = későbbre eltéve.

## Következő lépés

1. ✅ Mind a 3 plugin értékelve
2. **Integráció-PR-ek** (jelen lista alapján) — Navigator-plugin/runbook/reel-factory/DNA, sub-skillenként külön commit
3. **`/pres-competitor` Presto skill** scope-olása (competitor sub-skill + `/watch` mint data-source)
4. **EP43 Day 0 snapshot** (esedékes ~16:00)
