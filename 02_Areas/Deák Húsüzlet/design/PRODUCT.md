# Product

## Register

product

## Users

Digitally-open local buyers, 25–45 years old, living in Székelyudvarhely (Újvárhely), Romania (~30,000 population). They already shop at the physical Deák Húsmíves store and know the butcher personally. They are not early adopters — they buy meat out of habit, not curiosity. They are time-pressed (families, work), they trust local craftsmen over chains, and they have mild friction with anything that feels "tech for tech's sake."

Their primary job: get quality meat for the week without having to think about it. They don't want to optimize — they want to make a good decision without effort.

Secondary user: the courier/operator who manages and delivers orders from a mobile device in the field.

## Product Purpose

Deák Húsmíves Online Platform (deakhus.ro) is a mobile-first PWA for online ordering and home delivery of artisan meat products. It is not a webshop, not a marketplace, not a discount platform — it is a **decision-support system** that helps users order better (smarter basket, less waste, right quantities) and rewards habitual reordering.

The platform is a pilot for the LocalBasket vision: one platform, two modes (Daily + Local Market). DH is the proof-of-concept.

North Star KPI: Second Order Rate within 14 days (target ≥40%).

## Brand Personality

Warm, direct, unhurried. Like a trusted local craftsman who says little but means everything he says. Not an influencer, not a chef, not a marketer — a reliable, practically-minded person who helps you make good decisions.

Voice: "Hajnalban készül. Ma nálad." Short sentences. No marketing bullshit. No hype. No pressure. No urgency theatre.

The brand does not excite — it reassures. The emotional target: "I made a good decision. I don't have to think about this."

Primary language: Hungarian (85% of audience). Romanian is secondary, always adapted — never translated verbatim.

## Anti-references

- **Wolt / Foodpanda**: Aggressive discount-driven UX, countdown timers, FOMO mechanics. Wrong register entirely.
- **Supermarket e-commerce** (Kaufland, Penny): Industrial, cold, price-first. Opposite of artisan warmth.
- **Premium artisan e-commerce** (fancy packaging, serif-everything, lifestyle photography): Too elevated, too urban. Deák is local craft, not Michelin-adjacent.
- **Tech startup aesthetic**: Purple gradients, glassmorphism, hero metrics, SaaS dashboard patterns. The AI slop default. Explicitly forbidden.
- **ANY pattern with**: `border-left` accent stripes, gradient text, nested cards, identical icon+heading+text card grids, modal as first thought.
- **Copy patterns to avoid**: "INCREDIBLE DEAL!", "Order NOW!", "Premium quality", "Optimize your", "Save money", "Experience our range", "Leverage synergies".

## Design Principles

1. **Calm confidence over excitement.** The interface never raises its voice. No countdown timers, no FOMO, no flashing elements. Certainty and reliability are the emotional notes.
2. **Concrete over abstract.** "37 products. Choose, we deliver." beats "Explore our wide selection." Every label earns its place.
3. **Warmth through restraint.** Cream backgrounds, burgundi red used sparingly, Lucide icons not emoji. The warmth comes from proportion and tone, not decoration.
4. **System over impulse.** The UX reinforces weekly routine, reorder habits, and basket optimization — not impulse buying. Savings are shown as "you came out ahead", not "you saved".
5. **Local identity without nostalgia.** This is a modern product for a local community. Not rustic, not artisanal-cliché. The craft is real — the interface reflects that through honesty, not aesthetic cosplay.

## Accessibility & Inclusion

- WCAG AA as baseline target.
- Touch targets minimum 44×44px — non-negotiable on mobile.
- All interactive elements keyboard-accessible.
- No reliance on color alone for state (always icon + color + label for status badges).
- Hungarian primary language; Romanian secondary labels on legal pages and status badges.
- Reduced motion: animations are already short (120–180ms) and purposeful — respect `prefers-reduced-motion` by removing transitions, not replacing with jarring snaps.
