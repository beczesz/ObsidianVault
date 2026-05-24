---
topic: Brand Spine capability — modell-javítás (multi-AI)
created: 2026-05-13
last_updated: 2026-05-13
status: active
description: Multi-AI brainstorm (ChatGPT, Perplexity, Gemini) a Brand Spine capability v0.2 tervezéséhez. Eredmény: 7+1 rétegű Decision Spine modell, Lean/Standard/Premium tier-ek, teljes tool-stack. A capabilities/brand-to-site/CLAUDE.md upstream forrása.
id: aef34ce4-b198-43ac-b4fa-f6f8985050cc
index_schema_version: 1
---

# Brainstorm: Brand Spine capability javítása

## Team
| AI | Role | URL |
|----|------|-----|
| ChatGPT | Strategist | https://chatgpt.com/c/6a03f757-8ad4-8388-b06d-899b5d28bb33 |
| Perplexity | Researcher | https://www.perplexity.ai/search/f813a850-f471-483b-87cc-1af09798c168 |
| Gemini | Validator | https://gemini.google.com/app/efd2be42c066f5a3 |

## Sessions
| Date | Team | Key Outcome |
|------|------|-------------|
| 2026-05-13 | ChatGPT (Strategist) + Perplexity (Researcher) + Gemini (Validator) | v0.1 → v0.2 átdolgozás: 8 réteg → 7 rétegű "Decision Spine" + Pulse loop + Lean/Standard/Premium tier-ek; nevesített frameworkök beépítése; konkrét jobb/kiegészítő toolok azonosítva |

## AI Session Links
- ChatGPT (Strategist): https://chatgpt.com/c/6a03f757-8ad4-8388-b06d-899b5d28bb33 (2026-05-13)
- Perplexity (Researcher): https://www.perplexity.ai/search/f813a850-f471-483b-87cc-1af09798c168 (2026-05-13)
- Gemini (Validator): https://gemini.google.com/app/efd2be42c066f5a3 (2026-05-13)

## Key Insights

### Konvergencia (mindhárom AI egyetért)
- **A lineáris vízesés a fő hiba** — kell feedback loop; copy + wireframe EGYÜTT születik (ChatGPT + Gemini); a proof/trust külön súlyt kap (ChatGPT); HIÁNYZIK a mérés/iteráció loop (Gemini "Pulse")
- **Brand asset audit = input, nem réteg** — mindhárom egyetért, ez már jó volt a v0.1-ben
- **Design system túl korán** — előbb kell egy Creative Direction / art direction réteg, csak utána a formalizált design system + tokenek (ChatGPT; Brad Frost: a tokenek "subatomic", az atomokban nyerik értelmüket → build réteg)
- **HIÁNYZIK:** Offer / Conversion architecture (ChatGPT), Proof architecture (ChatGPT), Audience/JTBD reality (ChatGPT + Perplexity), Competition (Gemini), Analytics/iteráció (Gemini)
- **"Alkotmány" → "Brand Core / Operating Belief"** átnevezés (ChatGPT) — nem kell 20 oldalas manifesto
- **Túlmérnökölés-kockázat kisvállalkozásnál** ("Húsüzlet-szindróma" — Gemini): analízis-paralízis; teljes BMC overkill; enterprise site-ot szül, ahol egy egyoldalas + Google Maps profil is elég. Egy hentesnek bizalom + konverzió kell (nyitvatartás, cím, árlista, rendelés gomb), nem narratíva. → kell egy "Lean" tier.

### Nevesített frameworkök, amiket be kell építeni (forrás: Perplexity, sourced)
- **April Dunford — Obviously Awesome** (5 komponensű pozicionálás: competitive alternatives → differentiated capabilities → value → best-fit customers → market category) — a legteljesebb stratégiai gerinc, "a pozicionálás megelőzi a brandinget" → 3. réteg
- **StoryBrand BrandScript** (Donald Miller, 7 elem: Character/vevő → Problem → Guide/márka → Plan → CTA → Avoid Failure → End in Success; + PEACE framework) → messaging + copy
- **Jobs-to-be-Done** (Christensen — "felbérelünk" egy terméket egy feladatra) — kombinálni StoryBrand-del: JTBD a mélymotivációt tárja fel, StoryBrand narratívába önti → audience réteg
- **Kapferer Brand Identity Prism** (6 facet; a Physique = a visual identity közvetlen specifikációja) → creative direction
- **Atomic Design** (Brad Frost: tokens → atoms → molecules → organisms → templates → pages) → build réteg
- **W3C Design Tokens (DTCG)** — stabil spec 2025.10, vendor-semleges token formátum → design system
- **Content-First** (UX Collective 8 lépés: core message → content hierarchy → IA → wireframe szöveggel) → IA + copy együtt
- **Double Diamond** (Design Council: Discover → Define → Develop → Deliver) → folyamat meta-keret
- Golden Circle (Sinek) / Brand Pyramid → csak a Brand Core rétegben, önmagában kevés
- **Nincs egyetlen end-to-end framework** — a gyakorlók összefűznek. Ramotion ügynökség sorrendje: business goals → JTBD/pains → egy positioning statement → vizuális+verbális brand rendszer → design foundations + komponens könyvtár → navigáció & page hierarchy → design→dev→QA→launch

### Konkrét jobb / kiegészítő toolok (forrás: Perplexity, GitHub-linkekkel)
- **brand-toolkit** (jgerton/GitHub, MIT, Claude Code plugin) — 10 skill: Positioning (Dunford), Messaging (StoryBrand), Voice (NN/g + Aaker), Visual identity (Chris Do stylescape); megosztott `brand-brief.md` YAML, confidence score (validated/researched/assumed), anti-slop rendszer. → az 1–3. réteghez. `git clone https://github.com/jgerton/brand-toolkit.git`
- **marketingskills** (coreyhaines31/GitHub, MIT, 5700+ ⭐) — 23–30 skill: CRO, copywriting, SEO audit, analytics, email, pricing. → copy + Pulse réteg. `npx add-skill coreyhaines31/marketingskills`
- **designer-skills** (Owl-Listener/GitHub, 977 ⭐) — 87 skill / 27 parancs / 8 plugin, teljes design lifecycle; design-systems plugin: token coverage, naming consistency, a11y, theming audit; `/strategize` parancs. → design system audit. `/plugin marketplace add Owl-Listener/designer-skills`
- **ux-pilot** (Sakaax/GitHub, free) — 376 UX szabály, 161 paletta, 57 fontpár, 67 UI stílus → **kiegészítő** az ui-ux-pro-max-hoz, nem helyettesítő; kulcskülönbség: **dialógus-első** (strukturált discovery flow generálás előtt) + élő böngésző-előnézet. `/plugin marketplace add Sakaax/ux-pilot`
- **Dembrandt** (CLI, MCP) — bármely weboldal design rendszerét → W3C DTCG JSON; Playwright render + computed style. → **brand asset audit** + versenytárs-analízis. `npm i -g dembrandt; dembrandt competitor.com --dtcg`
- **Tokven** (tokven.dev) — AI design token generátor brand briefből, WCAG AA validációval light/dark; DO/NEVER irányelvek
- **Style Dictionary** (Amazon), **Tokens Studio**, **branding MCP server** (Forge Space) — token build pipeline
- **impeccable** (pbakaus/GitHub) — az Anthropic frontend-design skillre épül (277k telepítés), 7 referencia fájl, 17 slash parancs, anti-pattern lista; Tessl benchmark 0.82/1.00 (+0.35 az alap felett) → **MARAD**, jól teljesít

## Decisions Made
- 2026-05-13 — Capability létrehozva v0.1-draft (8 rétegű modell) — Szabolcs
- 2026-05-13 — v0.2-re átdolgozás a multi-AI session alapján: 7 rétegű Decision Spine + Pulse loop + Lean(5)/Standard(7)/Premium(9) tier-ek; nevesített frameworkök beépítve; tool-stack bővítve (brand-toolkit, ux-pilot, designer-skills, marketingskills, Dembrandt, Tokven) — Claude (orchestrator), jóváhagyásra vár

## Open Questions
- [ ] Brand-név végleges? ("Brand Spine" working; alt: Decision Spine, Constitution-to-Site)
- [ ] Telepítsük-e a feltárt toolokat? (brand-toolkit, ux-pilot, designer-skills, marketingskills) — vagy egyelőre csak dokumentáljuk?
- [ ] A "Pulse" loop (analytics/iteráció) — kötődjön-e a Microsite Factory analytics-rétegéhez?
- [ ] DH pilot: a Lean (5) tier-rel fussunk neki?

## Context References
- ../capabilities/brand-to-site/CLAUDE.md
- ../capabilities/brand-to-site/diagram.html
- ../capabilities/web-publishing/CLAUDE.md (downstream)

## Raw Notes
### 2026-05-13 — multi-AI session
- ChatGPT (Strategist): a v0.1 keveri a stratégiai/input/gyártási/gate rétegeket; javasolt 7 rétegű modell (Brand Core → Market+Audience Reality → Positioning+Offer → Messaging+Proof Architecture → Narrative UX/IA → Creative Direction+Design System → Build+Polish+Quality Gate); + 5 rétegű Lean és 9 rétegű Premium variáns; "a szép weboldal nem designból indul, hanem abból, hogy pontosan tudjuk: kinek, milyen döntési pillanatban, milyen új hitet kell elfogadnia, hogy cselekedjen"
- Gemini (Validator): lineáris vízesés = fő gyengeség, nincs feedback loop, nincs competition, nincs analytics; "Húsüzlet-szindróma" = analízis-paralízis; csendben feltételezi hogy a vízió stabil (a piac diktál), hogy az AI eszközök hibátlanok (kockázati forrás), hogy a szépség = konverzió (lassú/zavaró is lehet); javasolt "Core-Shell Model": MAG (üzleti cél + value prop + üzenet) → SZERKEZET (copy-first wireframe) → HÉJ (design system + build) → PULZUS (analytics + iteráció)
- Perplexity (Researcher): nincs egyetlen end-to-end framework, a profik összefűznek; részletes tool-lista GitHub-linkekkel (lásd Key Insights); a brand-toolkit Claude Code plugin pont a Ramotion-féle sorrendet automatizálja
