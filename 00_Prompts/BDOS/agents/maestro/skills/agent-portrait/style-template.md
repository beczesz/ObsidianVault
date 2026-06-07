---
title: Agent Portrait, Universal Style Template
date: 2026-05-27
status: active
description: A BDOS agent-portré-család közös vizuális nyelve. Minden per-agent prompt erre épül. Pixar Renderman 3D robot stílus, warm-neutral gradient háttér, terracotta accent.
tags: [maestro, agent-portrait, style-system, visual-identity]
id: 3d30ab17-000a-4699-8048-5d06754f4229
index_schema_version: 1
---

# Universal Style Template

Ez a minden agent-prompt **kötelező alapja**. A per-agent fájlok ezt importálják (mentálisan) és csak a per-agent variables-t cserélik.

## Base text (changes only if DESIGN.md changes)

```text
A friendly humanoid robot character rendered in Pixar Renderman 3D animation
style. Studio portrait composition, chest-up framing, square 1:1 aspect ratio.

Lighting: soft cinematic three-point setup. Key light from the upper-front
left at warm 4500K. Fill light from the lower-right, subtle. Rim light from
behind, slightly warmer, picking out the edge of the robot's head and shoulder.

Background: a solid warm-neutral gradient — cream (#faf9f5) at the top
transitioning to a tinted neutral toward the bottom. NO environmental detail,
NO scene props beyond what's specified for this agent. The gradient should
feel like a Pixar studio shot, not a realistic location.

The robot occupies 55-65% of the frame, centered.

Subtle terracotta accent (#D97757) is present somewhere — paint chip on a
panel, etched logo on a chest plate, a single light reflection, or trim of
an accessory. This terracotta token is the family signature.

Robot proportions: clearly non-human. A slightly oversized head with smooth
matte plastic finish (not metallic-shiny). Segmented limb joints with visible
articulation lines. Eye-LEDs are the primary emotional channel — their
shape, size, and tint communicate the agent's mood and role.

Color grading: warm, gallery-quality, slightly desaturated. Avoid neon,
avoid harsh saturation. The image should feel like a stylized 3D film
character poster, not a video-game render.

No text, no labels, no logos visible in the image.

The silhouette must be distinctive — when shrunk to a 64×64 thumbnail, the
viewer should still recognize WHICH agent it is.
```

## Per-agent variables to fill

| Variable | Required | Description |
|---|---|---|
| `agent_role` | yes | One-line identity, drives pose and prop choice |
| `color_signature` | yes | Primary hue beyond the terracotta accent (e.g. "warm green-teal") |
| `prop` | yes | Hand-held or floating object — symbolic of the agent's function |
| `pose` | yes | Body language matching the agent's mode (active/calm/leaning/etc.) |
| `ambient_motif` | no | Optional subtle environmental hint floating around (NOT a scene) |
| `eye_expression` | yes | Eye-LED shape and color, telegraphs personality |
| `material_note` | no | Optional textural detail (leather patch, metal panel, fabric scarf) |

## Family-coherence checklist

Before saving a new portrait prompt, verify:

- [ ] Same base render style as the others (Pixar Renderman 3D)
- [ ] Same composition (chest-up, square, centered)
- [ ] Same lighting setup
- [ ] Same background type (warm-neutral gradient, no scene)
- [ ] Terracotta accent present
- [ ] Eye-LEDs as the main expression channel
- [ ] Silhouette is recognizably DIFFERENT from the other 6
- [ ] No text, no logos, no realistic environments

If a candidate breaks one of these, it doesn't belong in the family — either revise the prompt or rethink the visual choice.
