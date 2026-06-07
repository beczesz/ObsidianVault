---
title: "Design System — Deák Húsmíves"
date: 2026-04-29
author: Becze Szabolcs
status: active
description: "Central design resource for the Deák Húsmíves PWA detailing mobile-first visual system: warm earthy color palette with burgundy accents, typography rules using Inter and Playfair Display, 4px spacing grid, and component guidelines for developers and designers."
description_source: auto
description_hash: 12a6ee2f88e7d2c9
id: f63fac19-297f-4a54-b7f8-871b2ab65dc3
index_schema_version: 1
bdos_index: true
---
# Design System — Deák Húsmíves

> Source of truth for the DH PWA visual system. Synced from `design/design-system.md` v2.0 (2026-04-21) and wireframe tokens. For impeccable context use: `cd design && node ~/.agents/skills/impeccable/scripts/load-context.mjs`

---

## Overview

Mobile-first PWA (Vue 3 + Tailwind CSS + Frappe UI). Target width: 375px. Max content width: 448px (`max-w-md`, `mx-auto`). The visual register is **warm, earthy, restrained** — cream-first ambient, burgundi red used sparingly as the signal color, warm gray neutrals throughout. No glassmorphism, no gradients in the UI layer, no pure black or white.

---

## Color

### Strategy: Restrained

One saturated accent (burgundi red) at ≤10% of any surface. Cream dominates. Red marks action and brand identity only.

### Brand Colors

| Role | Hex | Token | Usage |
|------|-----|-------|-------|
| Primary ("Butcher Red") | `#9B2335` | `--primary` | CTAs, active nav, prices, highlights, heart icon |
| Primary light | `#F9E0E3` | `--primary-light` | Hover backgrounds, out-for-delivery badge bg |
| Primary pale | `#F4E6E8` | `--primary-pale` | Icon tile backgrounds |
| Primary dark | `#7D1A2A` | `--primary-800` | Brand headings (Playfair Display only) |
| Secondary ("Warm Sand") | `#D4A574` | `--secondary` | Category badges, ready-for-delivery status |
| Secondary dark | `#9C7841` | `--secondary-dark` | Text on light gold backgrounds |

### Background Colors

| Role | Hex | Token | Usage |
|------|-----|-------|-------|
| Cream (app bg) | `#FFFBF7` | `--cream` | Primary app background — never pure white |
| Cream dark | `#F5EDE5` | `--cream-dark` | Subtle contrast blocks |
| Card | `#FFFFFF` | `--card` | Card surfaces, modal content |
| Page BG alt | `#FAF8F5` | `--bg` | Alternative page background |

### Functional Colors

| Role | Hex | Light BG | Usage |
|------|-----|----------|-------|
| Success | `#2D7A4F` | `#D4EDDA` | Delivered, savings, positive states |
| Warning | `#C4841D` | `#FEF3C7` | Processing, nudges |
| Error | `#C4302B` | — | Validation errors, destructive actions |
| Info | `#2B6CB0` | `#DBEAFE` | New order, informational |

### Warm Gray Scale (neutrals, always tinted toward cream)

| Role | Hex | Token | Usage |
|------|-----|-------|-------|
| Border light | `#E8E2DB` | `--border` | Card borders, dividers |
| Border strong | `#C5BCB3` | | Input borders |
| Text muted | `#8A8078` | `--text-muted` | Secondary text, placeholders |
| Text secondary | `#5C544C` | | Descriptions, helper text |
| Text primary | `#2C2825` | `--text` | Body text — near-black with warm tint |

### Absolute color rules

- Never `#000000` or `#FFFFFF` for text — always warm gray variants
- No gradient backgrounds in the UI layer — solid colors only
- No gradient text (`background-clip: text`) — forbidden
- Cream (`#FFFBF7`) is the ambient default; white (`#FFFFFF`) is reserved for card surfaces only

---

## Typography

### Typefaces

| Family | Type | Source | Usage |
|--------|------|--------|-------|
| **Inter** (variable) | Sans-serif | Self-hosted woff2/woff | All UI: body, buttons, labels, numbers, navigation |
| **Playfair Display** | Serif | Google Fonts | Brand headings only: login hero, section titles, brand name display |

**Playfair Display** is used exclusively via `.heading-brand`:
```css
.heading-brand {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  letter-spacing: -0.3px;
  color: #7D1A2A;
}
```
Never on body text or UI controls.

### Scale (mobile-first, 4px baseline grid)

| Role | Size | Weight | Line-height | Usage |
|------|------|--------|-------------|-------|
| Display | 24px | 700 | 32px | Page titles |
| H1 | 20px | 600 | 28px | Section titles |
| H2 | 18px | 600 | ~21px | Component headings, product names |
| Body | 16px | 400 | 24px | Main text, descriptions |
| Body strong | 16px | 500 | 24px | Prices, emphasis |
| Small | 14px | 400 | 20px | Helper text, timestamps |
| Caption | 12px | 500 | 16px | Badge labels, form errors |

**Used weights:** Inter 400 / 500 / 600 / 700 / 800. Playfair 600 / 700 / 800.

### Text rules

- Sentence case everywhere — no ALL CAPS, no Title Case on UI elements
- Body line length: cap at 65–75ch
- Hungarian primary; Romanian secondary labels and legal text
- Informative tone: `"Kész. Pénteken visszük."` not `"Order Confirmed Successfully"`

---

## Spacing

4px base unit. All spacing is a multiple of 4.

### Three Zones

| Zone | Tailwind | Pixels | Usage |
|------|----------|--------|-------|
| Tight | `p-1`–`p-2`, `gap-1`–`gap-2` | 4–8px | Icon-text gaps, badge padding, button internals |
| Standard | `p-3`–`p-4`, `gap-3`–`gap-4` | 12–16px | Card sections, form fields, list items |
| Spacious | `p-6`–`p-8`, `gap-6`–`gap-8` | 24–32px | Page sections, header-content separation |

### Fixed Conventions

| Element | Value | Notes |
|---------|-------|-------|
| Page side padding | `px-4` (16px) | Both sides, every page |
| Card inner padding | `p-4` (16px) | Consistent across all cards |
| Gap between cards | `gap-3` (12px) | |
| Gap between form fields | `gap-4` (16px) | |
| Section gap | `mt-6` / `gap-6` (24px) | |
| Content bottom (with nav) | `pb-20` (80px) | Clears fixed bottom nav |
| Content bottom (with CTA + nav) | `pb-36` (144px) | Clears fixed CTA + nav |

### Touch Targets

Minimum **44×44px** — non-negotiable. Bottom nav height: 65px + `env(safe-area-inset-bottom)`.

---

## Border Radius

Rounded, friendly forms — matches the warm local butcher character.

| Element | Value | Usage |
|---------|-------|-------|
| Buttons, inputs | `8px` (`rounded-lg`) | Interactive small elements |
| Cards, images | `12px` (`rounded-xl`) | Container elements |
| Modals, dialogs | `16px` (`rounded-2xl`) | Overlay elements |
| Badges, tags, pills | `9999px` (`rounded-full`) | Pill shapes |
| Bottom navigation | `0px` | Edge-to-edge |

---

## Elevation & Shadows

Minimal — soft, warm shadows. Cream background vs. white cards is already sufficient separation.

| Role | Value | Usage |
|------|-------|-------|
| Card default | `0 1px 2px rgba(0,0,0,0.08)` | Resting cards |
| Card hover | `0 3px 12px rgba(155,35,53,0.08)` | Hover (brand-tinted shadow) |
| Sticky elements | `shadow-md` | Bottom nav, sticky header |
| Bottom nav | `0 -2px 8px rgba(0,0,0,0.08)` | Reversed direction |
| Modal | `shadow-xl` | Overlay layer |

No inner shadow. No glassmorphism. Modals use flat dark backdrop `rgba(0,0,0,0.4–0.5)`.

---

## Layout

### Page Shell

```
+------------------------+
|  Header (sticky)       |  h-14 (56px), bg-white, border-bottom #E8E2DB
+------------------------+
|  Content (scrollable)  |  px-4, pb-20 (or pb-36 with fixed CTA)
+------------------------+
|  [Fixed CTA — optional]|  position: fixed, bottom after nav
+------------------------+
|  Bottom Nav (fixed)    |  h-16 (64px) + safe-area, bg-white
+------------------------+
```

### Navigation — Role-based tabs

| View | Tabs |
|------|------|
| Guest (3) | Products / Cart / Account |
| Customer (4) | Products / Cart / Orders / Account |
| Courier (2) | Deliveries / Account |
| Operator (5) | Overview / Orders / Products / Deliveries / Account |

Active tab: `#9B2335`. Inactive: `#8A8078`. Cart badge: 18px pill, `bg-primary`, white text.

`hideNav: true` on checkout flow routes (`/checkout/delivery`, `/checkout/confirm`, `/order-success`).

---

## Components

### Buttons

| Type | Background | Text | Usage |
|------|-----------|------|-------|
| Primary | `#9B2335` | `#FFFFFF` | Main CTA: "Megrendelem", "Hozzáadás" |
| Secondary | transparent, `#9B2335` border 2px | `#9B2335` | "Vissza", "Szerkesztés" |
| Danger | `#C4302B` | `#FFFFFF` | "Törlés", "Rendelés lemondása" |
| Disabled | `#E8E2DB` | `#8A8078` | Inactive state |

Sizes: default `h-10` (40px), large `h-12`–`h-14` (48–56px) for primary CTAs. `rounded-xl` on full-width buttons.

Fixed bottom CTA pattern:
```css
position: fixed; bottom: 0; left: 0; right: 0;
padding: 16px;
padding-bottom: calc(16px + env(safe-area-inset-bottom));
background: white;
box-shadow: 0 -2px 8px rgba(0,0,0,0.08);
```

### Status Badges

Pill shape (`rounded-full`), two sizes: sm (`text-xs px-2.5 py-0.5`), md (`text-sm px-3 py-1`).

| Status (HU) | Background | Text |
|-------------|-----------|------|
| Új rendelés | `#DBEAFE` | `#2B6CB0` |
| Folyamatban | `#FEF3C7` | `#C4841D` |
| Kiszállításra kész | `#F5EDDF` | `#9C7841` |
| Szállítás alatt | `#F9E0E3` | `#9B2335` |
| Kiszállítva / Lezárva | `#D4EDDA` | `#2D7A4F` |
| Törölve | `#EDEAE6` | `#5C544C` |

### Product Card

```
rounded-xl, border #E8E2DB, bg-white
Image: aspect-[4/3], bg-gray-200
Body: p-4
Category badge: text-xs, secondary color, rounded-full
Name: text-lg font-semibold
Price: text-base font-medium, color #9B2335 + " RON"
```
Unavailable state: `bg-gray-900/40` overlay on image.

### Icons

**Lucide SVG, inline only.** No icon fonts, no sprite sheets, no PNG, no emoji (ever).

- Size: 18×18px or 20×20px in UI; 28×28px for savings coin badge
- Stroke: `stroke-width: 2`, `stroke-linecap: round`, `stroke-linejoin: round`, `fill: none`
- Exception: filled heart (`fill` + `stroke: #9B2335`)
- Color: inherited from parent — icons never carry their own color token

Common icons: `truck`, `circle-check`, `shopping-cart`, `ban`, `package`, `flame`, `pencil`, `lightbulb`, `coins`, `rotate-ccw`, `star`, `heart`, `home`, `clipboard-list`, `user`, `chevron-right`

### Savings Engine UI

Progress bar: 8px track (`#E0D8D0`), fill gradient `#2E7D32 → #D4A574`, milestone bubbles at 50% and 100%.

Nudge messages:
- Below threshold: `#FFF3E0` bg, `#E65100` text
- Free delivery reached: `#E8F5E9` bg, `#2E7D32` text
- Both thresholds: gradient bg `#E8F5E9 → #FFF8E1`, `#1B5E20` text

Savings badge on order cards: green filled circle, `coins` icon, `-X RON`. Hidden via `visibility: hidden` (not `display: none`) when savings = 0.

---

## Motion

- Duration: 120–180ms
- Easing: ease-out (exponential curves — `ease-out-quart` or similar)
- No bounce, no elastic, no spring physics
- No animation of CSS layout properties
- No decorative animation — every motion must have a purpose
- Respect `prefers-reduced-motion`: disable transitions, do not replace with snaps
- Page transitions: flat — no slide-in/out

Documented micro-interactions:
- Heart fill: `scale(1) → 1.2 → 1`, 140ms ease-out, fill transition simultaneous
- Toast: 250ms translate-up + fade-in

---

## Absolute Bans

These patterns are explicitly forbidden in DH UI:

- `border-left` or `border-right` > 1px as colored accent (side-stripe cards)
- Gradient text (`background-clip: text` + gradient)
- Glassmorphism / blur cards
- Nested cards
- Pure `#000000` or `#FFFFFF` for text
- Emoji anywhere in the app UI
- Gradient backgrounds in the UI layer
- ALL CAPS in body text or button labels
- "Premium", "optimize", "save money", "incredible deal" copy
