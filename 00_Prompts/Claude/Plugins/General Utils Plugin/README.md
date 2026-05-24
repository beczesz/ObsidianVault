# General Utils Plugin

Altalanos segedeszközök Claude Cowork-hoz. Harom skill-t tartalmaz: semi-autonom multi-AI orkesztracio (ChatGPT + Perplexity + Claude), fajl YAML header kezeles, es projekt allapot motor.

## Skills

### 1. `think-agent-orchestrator-v0.6` -- Semi-Autonom Multi-AI Orkesztracio Motor

Claude mint kozponti intelligencia koordinalja a ChatGPT-t es a Perplexity-t, felautomata modban.

| Szereplo | Feladata |
|----------|----------|
| **Human** | Szandek, valosag, vegso dontes (csak blocking kerdeseknel) |
| **Perplexity** | Kutatas, tenyellenorzes, versenytars-elemzes, forrasok citatumokkal |
| **ChatGPT** | Brainstorming, kreativ ideacio, strategia, üzleti modellek |
| **Claude/Cowork** | **Orkesztracio** + vegrehajtas, szintezis, perzisztens tudas |

**v0.6 ujdonsagok (v0.5-hoz kepest):**
- Claude = **aktiv orkesztrator** — nem var utasitast, hanem proaktivan koordinal
- **Brainstorming State File** — topic-alapu markdown a perzisztens gondolkodashoz
- **Task-driven AI aktivacio** — Claude felismeri a feladat tipusat es automatikusan bevon AI-kat
- **Kollaborativ gondolkodasi loop** — ChatGPT otletel, Perplexity validál, Claude szintetizal
- **Context rekonstrukcio** — uj session-ök teljes kontextust epitik ujra fajlokbol + linkekbol
- **Local-first reasoning** — eloszor lokalis fajlokbol valaszol, csak utana kerdez AI-kat
- **Intelligens kerdeseskalacio** — batch-elt, strukturalt kerdesek a Human-nek
- **Multi-AI bővíthetoseg** — nyilt architektura uj AI eszkozök integralasahoz

**Mikor aktivalodik:**
- "think engine", "orchestrator", "gondolkodj", "jard korbe", "kutasd ki"
- "brainstorm with ChatGPT", "research with Perplexity"
- "piackutatas", "kockazatelemzes", komplex analitikai feladatok
- ChatGPT URL ( vagy ) beillesztese
- Perplexity URL () beillesztese

---

### 2. `file-header` -- YAML Frontmatter Header Kezeles

Hozzaad vagy frissit egy YAML metaadat blokkot barmely fajl elejehez.

**Mikor aktivalodik:**
- "adj headert a filehoz", "tegyel headert", "generalj headert"
- "frissitsd a headert" / "updateld a headert"
- "meta header", "YAML header", "frontmatter"

---

### 3. `project-engine` -- Projekt Allapot Motor

Letrehozza es karbantartja a  fajlt, amely a projekt egyetlen igazsagforrasa.

**Mikor aktivalodik:**
- "project state", "create project state", "update project state"
- "01_PROJECT_STATE", "project engine"
- "where are we", "project status", "initialize project"

## Telepites

Importald a  fajlt a Cowork app Plugins menujebol.

## Verziotortenet

-  -- 2026-04-11: think-agent-orchestrator v0.6 -- semi-autonom orkesztracio, brainstorming state file, task-driven AI aktivacio, kollaborativ thinking loop, context rekonstrukcio, local-first reasoning, kerdeseskalacio, multi-AI bővithetoseg
-  -- 2026-04-04: think-agent-orchestrator v0.5 -- confidence-based execution, two-speed ambiguity, operational override alert, upstream briefs, decision log
-  -- 2026-04-01: chatgpt-import + think-engine osszevonva think-agent-orchestrator-v0.4 skill-le; Perplexity szerepkor hozzaadva
-  -- 2026-03-31: project-engine es think-engine skill-ek hozzaadva
-  -- 2026-03-15: elso kiadas (chatgpt-import, file-header)
