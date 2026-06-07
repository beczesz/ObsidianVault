---
agent: <agent-slug>
agent_version: <x.y>
portrait_version: 0.1
date: <YYYY-MM-DD>
status: active
description: <Agent name> — <one-line role> — Pixar-stílusú robot profil-prompt. <One-sentence visual hook.>
tags: [agent-portrait, <agent-slug>, image-gen]
id: 6add0528-7902-4cc3-81f1-4048bec40106
index_schema_version: 1
---

# <Agent Name>, Pixar Portrait Prompt

## Identity mapping

| Variable | Value |
|---|---|
| `agent_role` | <one-line identity, derives pose+prop> |
| `color_signature` | <primary hue beyond family terracotta accent> |
| `prop` | <hand-held or floating object symbolizing function> |
| `pose` | <body language matching the mode> |
| `ambient_motif` | <optional subtle environmental hint, NOT a scene> |
| `eye_expression` | <eye-LED shape and color, primary emotional channel> |
| `material_note` | <optional textural detail with terracotta accent placement> |

## Final Prompt (copy-paste this)

```text
A friendly humanoid robot character rendered in Pixar Renderman 3D animation
style. Studio portrait composition, chest-up framing, square 1:1 aspect ratio.

The robot is <agent_role>. <Brief identity expansion in 1-2 sentences.>

The pose is <pose description>. <If prop is held, describe the hands.>

<Prop description as part of the scene.>

Eye-LEDs are <eye_expression>, conveying <emotional read>.

The robot's overall hue carries a <color_signature> signature — <one-line
mood association>.

<Material_note sentence ending with: "— the family signature.">

<Ambient_motif sentence if used. Otherwise omit.>

Lighting: soft cinematic three-point setup. Key light from upper-front left
at warm 4500K. Fill light from lower-right, subtle. Rim light from behind,
slightly warmer, picking out head and shoulder.

Background: solid warm-neutral gradient, cream (#faf9f5) at top transitioning
to a <color>-tinted neutral toward the bottom. NO environmental detail.

Robot proportions: clearly non-human. Slightly oversized head, smooth matte
plastic finish, not metallic-shiny. Segmented limb joints visible. The
robot occupies 55-65% of the frame, centered.

Color grading: warm, gallery-quality, slightly desaturated. No text, no
labels, no logos. Silhouette must be distinctive — recognizable at thumbnail
size by <silhouette signature>.
```

## Notes

- **Silhouette signature:** <what makes this agent recognizable at 64×64>
- **Differentiator vs. other agents:** <which existing agent it might be confused with, and why this one is different>
- **Mood:** <one-line atmosphere>

## Family-coherence check

Before saving, verify (per `style-template.md`):

- [ ] Same base render style as the others (Pixar Renderman 3D)
- [ ] Same composition (chest-up, square, centered)
- [ ] Same lighting setup
- [ ] Same background type (warm-neutral gradient, no scene)
- [ ] Terracotta accent present
- [ ] Eye-LEDs as the main expression channel
- [ ] Silhouette is recognizably DIFFERENT from the other agents
- [ ] No text, no logos, no realistic environments
