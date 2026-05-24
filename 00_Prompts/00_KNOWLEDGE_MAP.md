---
title: 00_KNOWLEDGE_MAP
generated_by: librarian v0.5
generated_at: 2026-05-11T00:00:00
scope: 00_Prompts/
mode: index
id: 70e7728d-bf0b-4f2f-9da7-e0bc49515cbd
index_schema_version: 1
---

# 00_Prompts — Knowledge Map

> Ez a mappa rendszer-szintű — nem domain-tartalom, hanem az AI-kogníció infrastruktúrája.
> A vault többi részétől eltérően itt **meta-gondolkodás** él: hogyan gondolkodunk, nem miről.

---

## Réteg-struktúra

```
00_Prompts/
│
├── BDOS/                          ← Tier-1: Agent rendszer (AI-native cognition)
│   ├── agents/                    ← Kanonikus agent-definíciók
│   ├── capabilities/              ← Projekt-független képesség-csomagok
│   └── pilots/                    ← Élő projektek ahol a BDOS validálódik
│
└── Claude/                        ← Tier-2: Claude Cowork plugin-ok és skill-ek
    ├── Plugins/                   ← 5 plugin (General Utils, Personal Utils, Navigator, Sonrisa, Speed Reader)
    └── Skills/                    ← Standalone skill-ek (Sonrisa CPS dashboard)
```

---

## Domain-mátrix: melyik plugin melyik területhez kapcsolódik

| Plugin / Skill | BDOS | Navigátor Podcast | Sonrisa | Personal | Cross-domain |
|---|:---:|:---:|:---:|:---:|:---:|
| **Librarian** (BDOS/agents) | kizárólagos | - | - | - | - |
| **Microsite Factory** (BDOS/capabilities) | - | potenciális | potenciális | - | igen |
| **General Utils Plugin** | támogató | - | - | - | igen |
| **Personal Utils Plugin** | - | igen (monitor) | - | igen | - |
| **Navigator Plugin v0.3** | - | kizárólagos | - | - | - |
| **Sonrisa Management Plugin** | - | - | kizárólagos | - | - |
| **Speed Reader Plugin** | - | - | - | igen | igen |
| **Severity Addon** | - | - | - | - | igen (rendszerszintű) |

---

## BDOS kapcsolódási háló

```
BDOS/CLAUDE.md (belépő)
    │
    ├── agents/librarian.md ──────────► .claude/agents/librarian.md (registration)
    │       │                                   │
    │       │ 6 mód                             │ slash commands:
    │       ├── index ──────────────────────────┤ /lib-index
    │       ├── retrieve ───────────────────────┤ /lib-find
    │       ├── tidy ───────────────────────────┤ /lib-tidy
    │       ├── audit ──────────────────────────┤ /lib-audit
    │       ├── integrate ─────────────────────┤ /lib-integrate
    │       └── deep-clean ──────────────────── /lib-deepclean
    │
    ├── capabilities/web-publishing/CLAUDE.md ◄── 🚧 DESIGN PHASE
    │       │
    │       └── Precedensek a vault-ban:
    │           ├── DH: deakhus.netlify.app
    │           ├── Sonrisa: CPS website workflow
    │           └── `impeccable` skill (UI/UX polish)
    │
    └── pilots/deak-husuzlet.md ──────────► 02_Areas/Deák Húsüzlet/ (pointer)
            (valódi napló ott él)
```

---

## Navigator Plugin evolúció

```
navigator-podcast.plugin (v0.1, 2026-02-15) — LEGACY
    └── 1 command: /navigator-metadata
          │
          ▼
navigator-plugin-v0.2 (2026-03-15) — LEGACY (nem törölt)
    └── 6 command: /hook /cim /thumbnail /leiras /idokod /meghivo
    └── 2 skill: navigator-context, episode-prep
          │
          ▼
navigator-plugin-v0.3 (2026-04-06) — AKTÍV „Intelligens Motor"
    └── 9 command (+ cross-ref, csatorna-intelligencia)
    └── 3 skill (+ episode-synthesis-v0.3)
    └── Csatorna-intelligencia: 52 epizód szintéziséből
```

---

## Sonrisa CPS skill evolúció

```
cps-statistics-v0.3 (Sonrisa Management Plugin-ban) — statisztika
cps-dashboard-update-v0.1.skill — standalone legacy zip
sonrisa-cps-dashboard-update-v0.1.skill — standalone legacy zip (duplikátum?)
sonrisa-cps-dashboard-update-v1.0/ — AKTUÁLIS (könyvtár-alapú)
    └── SKILL.md + references/
        ├── brief-template.md
        ├── column-map.md
        └── formula-templates.md
```

---

## Kulcsszó-térkép (quick lookup)

| Ha keresed... | Hol van |
|---|---|
| Librarian agent spec | `BDOS/agents/librarian.md` |
| Agent regisztrációk | `.claude/agents/` (vault gyökér) |
| BDOS alapelvek | `BDOS/CLAUDE.md` |
| Microsite Factory terv | `BDOS/capabilities/web-publishing/CLAUDE.md` |
| DH BDOS pilot-napló | `02_Areas/Deák Húsüzlet/brainstorm/brainstorm_bdos.md` |
| Navigátor YouTube commandok | `Claude/Plugins/navigator-plugin-v0.3/commands/` |
| Navigátor csatorna-intelligencia | `Claude/Plugins/navigator-plugin-v0.3/skills/navigator-context-v0.3/references/csatorna-intelligencia.md` |
| Reggeli rutin | `Claude/Plugins/Personal Utils Plugin/commands/morning-v0.2.md` |
| Yahoo cleanup | `Claude/Plugins/Personal Utils Plugin/commands/yahoo-v0.2.md` |
| Sonrisa timesheet | `Claude/Plugins/Sonrisa Management Plugin/skills/cps-statistics-v0.3/` |
| Sonrisa dashboard update | `Claude/Skills/sonrisa-cps-dashboard-update-v1.0/SKILL.md` |
| Speed reading workflow | `Claude/Plugins/speed-reader-plugin/skills/speed-reader/SKILL.md` |
| Think engine orchestrátor | `Claude/Plugins/General Utils Plugin/skills/think-agent-orchestrator-v07/SKILL.md` |
| Precizitás addon | `Utils/Severity Addon.md` |
