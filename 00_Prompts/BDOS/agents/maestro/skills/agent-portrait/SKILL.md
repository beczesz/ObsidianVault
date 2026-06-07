---
name: maestro-agent-portrait
version: 0.1.0
date: 2026-05-27
author: Becze Szabolcs
status: active
description: Maestro skill — egy adott BDOS agenthez Pixar-stílusú humanoid robot profil-kép prompt-ot javasol, a vault-családi vizuális nyelv szerint. Universal style template + per-agent semantic detail. Used: ChatGPT image-gen, DALL-E, Midjourney, Sora image, vagy bármely text-to-image modell. Reusable: új agent bemutatáskor (Maestro `team-introduce` mode) automatikusan generálható egy konzisztens portré.
tags: [maestro, agent-family, visual-identity, branding]
id: a3c7f9e1-2b4d-4e8a-9c5f-1d8b3a6e2c97
index_schema_version: 1
bdos_index: true
---

# Maestro Agent Portrait Skill

> **Cél:** minden BDOS agentnek **konzisztens, mégis distinkt** Pixar-stílusú robot-portré legyen, ami a profil-kép helyén (avatar, dashboard agent-card, AGENTS_INDEX) szerepelhet.
>
> **Miért Maestro skillje:** Maestro vezeti az agent családot — ő dönti el, milyen "nyelvet beszélnek" együtt. A portrék is egy ilyen családi-nyelv.

---

## A skill két módja

### A. **`portrait list`** — meglévő agent-prompt-ok listája

A `portraits/` mappa egy fájlt tartalmaz minden élő agentre. Mindegyikben a kész text-to-image prompt + identity-mapping (mit jelent vizuálisan minden elem).

### B. **`portrait propose --agent <name>`** — új agent prompt javaslata

Ha új agent jön a családba, Maestro a kanonikus agent-definíciójából (description, mission, role) javasol egy portrait-prompt-ot a **style template** szerint. User véleményezi, finomítják, mentik `portraits/<name>.md`-be.

---

## Universal Style Template

Mindig kötelező része minden generált prompt-nak — ez biztosítja a **családi-koherenciát**.

```text
A friendly humanoid robot character in Pixar Renderman 3D animation style.
Studio portrait, chest-up composition, square 1:1 aspect ratio.
Soft cinematic three-point lighting with a warm rim light.
The robot occupies 55-65% of the frame, centered.
Background: solid warm-neutral gradient (cream-to-tinted-neutral), no environmental detail.
Subtle terracotta accent (#D97757) somewhere in the design — paint chip, logo etch, light reflection, or accessory trim — present in every agent portrait.
Robot proportions: clearly non-human (chunky head, expressive eye-LEDs that telegraph emotion via shape/color, segmented limb joints), but warm and approachable.
The face has a soft matte finish, not metallic-shiny.
No text, no labels, no logos visible in the image.
Color grading: warm, slightly desaturated, gallery-quality.
The silhouette must be distinctive — recognizable at thumbnail size.
```

### Per-agent variables

Each agent prompt adds the following on top of the universal template:

| Variable | What it controls | Example |
|---|---|---|
| `agent_role` | One-line identity (used in pose + prop) | "knowledge librarian who organizes infinite indexed memories" |
| `color_signature` | The agent's primary hue (besides terracotta accent) | warm green-teal, OKLCH ~lch(60% 0.1 170) |
| `prop` | Hand-held or floating object that signals function | "a glowing leather-bound book with wikilink-shaped page corners" |
| `pose` | Body language matching the agent's mode | "seated, leaning slightly forward in attentive listening" |
| `ambient_motif` | Subtle environmental hint (NOT a full scene) | "indexed-card fireflies drifting softly in the background gradient" |
| `eye_expression` | Eye-LED shape/intensity (the main emotional channel) | "calm half-moon LEDs in pale gold" |
| `material_note` | Optional textural detail | "small leather-textured patches on the shoulders" |

---

## How to use

### Generating an image with an existing prompt

1. Open the desired agent file: `portraits/<agent>.md`
2. Copy the **Final Prompt** block (the consolidated text)
3. Paste into ChatGPT (DALL-E), Midjourney, or another text-to-image tool
4. Optional: pass `--ar 1:1 --style raw` (Midjourney) for tighter control
5. Iterate 2-3 times, pick the one with the best silhouette test

### Proposing a prompt for a NEW agent

1. Read the new agent's canonical definition (`00_Prompts/BDOS/agents/<name>.md`):
   - `description` field — the identity in one sentence
   - The "Mission" / "Identity" section — what they do
   - Any visual hints in the description (e.g. Presto's "magician who translates, not tricks")
2. Fill in the seven per-agent variables (table above) by inference from the identity
3. Assemble: universal template + per-agent block
4. Present to user for confirmation; iterate; save as `portraits/<name>.md`
5. Optionally add to the BDOS Backlog item if it triggered a wider visual-update

### When to invoke this skill

- **Maestro `team-introduce` mode** — auto-call when scaffolding a new agent
- **User direct request** — "javasolj profilkép-promptot a <name> agentnek"
- **Visual refresh** — annual or when DESIGN.md updates

---

## Why Pixar style

The vault DESIGN.md tone is "calm, professional, restrained" and "earned familiarity over novelty" (PRODUCT.md). The Pixar 3D-robot aesthetic delivers:

- **Warm, not cold** — these agents are collaborators, not enterprise software
- **Stylized non-human** — clearly tools, not people; no uncanny-valley
- **Family-coherent** — same render style across all agents = visual unity
- **Approachable for non-technical viewers** — when shown to clients/partners on the dashboard, robots-as-helpers reads instantly
- **Distinctive silhouettes possible** — the medium is rich enough to encode 7+ unique identities without confusion

The opposite ends (corporate-blue-glowing-AI-logo, or cyberpunk-anime-robot) would either feel cold/template, or too loud for the vault's restrained aesthetic.

---

## Files in this skill

```
agent-portrait/
├── SKILL.md                ← ITT — the contract
├── style-template.md       ← detailed universal template + variable reference
├── portraits/
│   ├── librarian.md
│   ├── maestro.md
│   ├── curator.md
│   ├── presto.md
│   ├── sage.md
│   ├── broker.md
│   └── forge.md
└── _template.md            ← scaffold for new agents
```

---

## Maintenance

- When an agent's role changes substantially (e.g. Presto v0.5 → v0.8 with seed/draft/prepare pipeline), revisit the portrait
- When DESIGN.md updates the accent color or base palette, run a family-refresh
- Keep `portraits/<name>.md` versioned in the audit-trail (small comment block at the bottom)
