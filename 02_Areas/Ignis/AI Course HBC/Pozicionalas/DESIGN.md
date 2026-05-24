# Design

## Theme & Scene

**Egyetlen mondat a fizikai jelenetről:**
*Egy 42 éves erdélyi KKV-tulajdonos a Friss Pékség mellett, kávéval, 11:32-kor egy szürkés tavaszi délelőttön a mobiljáról megnyitja az oldalt — a busz 8 perc múlva indul.*

Ebből következik:
- **Light theme**, melegített papír-háttér (nem stark-fehér, nem sötét).
- Az olvasás-érzet **kézikönyv-szerű** (manuál / field-guide lane), nem magazinos, nem SaaS-os.
- Generous spacing, mert a kávésbögre miatt nyugodt scroll-ütem kell.

## Color Strategy

**Választott stratégia:** Committed — **egy melegített okker** carries 25–35% of visible surface (mostly CTAs, kulcs-szavak, divider-ek, accent block-ok). Egyébként papír-fehér és melegített szénszín.

Az okker nem a Microsoft-kék, nem a SaaS-magenta, nem a startup-gradient — egy magyar/erdélyi népfőiskolás, **kézikönyv-borító okker**. *"Mint egy 1968-as agronómiai zsebkönyv borítója."*

### Palette (OKLCH)

| Token | OKLCH | Use |
|---|---|---|
| `--paper` | `oklch(0.97 0.008 85)` | Háttér. Hűvös papír, nem stark. |
| `--paper-deep` | `oklch(0.94 0.012 85)` | Alternatív szekció-háttér (rétegezett). |
| `--ink` | `oklch(0.22 0.008 60)` | Body text. Szénszín kissé melegre tintálva. |
| `--ink-soft` | `oklch(0.42 0.010 60)` | Másodlagos szöveg, metadata, sub-line. |
| `--rule` | `oklch(0.82 0.008 75)` | Vékony elválasztó vonalak. |
| `--ochre` | `oklch(0.68 0.135 75)` | Committed brand-szín. CTA-háttér, accent. |
| `--ochre-deep` | `oklch(0.52 0.130 65)` | Hover state, link szín, kulcs-szó kiemelés. |

### 4 Dimenzió color codes (mnemonikus, kis százalék)

Földszín-paletta. Mindegyik szöveggel kísérve, nem önmagában kommunikál.

| Dim | Token | OKLCH | Asszociáció |
|---|---|---|---|
| Ethos | `--dim-ethos` | `oklch(0.50 0.115 30)` | Agyagvörös (földhöz kötött, fizikai) |
| Logos | `--dim-logos` | `oklch(0.43 0.060 240)` | Palakék (gondolat, ég) |
| Pathos | `--dim-pathos` | `oklch(0.62 0.130 50)` | Meleg terra (emberi melegség) |
| Thelos | `--dim-thelos` | `oklch(0.36 0.055 160)` | Fenyőzöld (spiritual depth) |

Háttér-tinted változatok (10%-os opacity-vel a zsigeri "kapcsolódás" akcentusokhoz): ugyanaz, csak `oklch(0.94 chroma/4 hue)`.

## Typography

**Font selection — három brand-voice szó kiválasztása:**
*tömör, tanult, papíros.* (Nem "modern", nem "elegáns".)

**Reflex-reject ellenőrzés:** Fraunces, Newsreader, Lora, Crimson, Playfair, Cormorant, Inter, DM Sans, Space Grotesk, Plus Jakarta — mind tilos. Editorial-typographic lane — szándékosan elkerülve.

### Választott párosítás

**Display + Heading:** **EB Garamond** (Google Fonts) — szöveg-arcú, klasszikus könyvbetű, magyar diakritikákkal natívan. Nem trendi, nem AI-tipikus. *"Régi tankönyv-borító."* Súly: 500–700 a hierarchia-ugráshoz.

**Body:** **Atkinson Hyperlegible** (Google Fonts) — Braille Institute által tervezett accessibility-first sans. Magasan láthatóság-optimalizált, civic-érzet, **NEM a tipikus Inter / Plus Jakarta refresh**. Súly: 400 (regular), 600 (semibold) ahol kulcsszó kell.

**Numerals / dimenzió-tag:** EB Garamond small caps — római számok (I. II. III. IV.) — nem mono, nem fancy.

### Scale (fluid clamp)

| Token | Min → Max | Use |
|---|---|---|
| `--fs-hero` | `clamp(2.5rem, 9vw, 5.5rem)` | Hero tagline (display weight 600) |
| `--fs-h1` | `clamp(1.875rem, 5.5vw, 3rem)` | Szekció-cím |
| `--fs-h2` | `clamp(1.375rem, 4vw, 2rem)` | Sub-szekció |
| `--fs-h3` | `clamp(1.125rem, 2.8vw, 1.375rem)` | Kis fejléc |
| `--fs-body` | `clamp(1rem, 2.4vw, 1.125rem)` | Body |
| `--fs-meta` | `clamp(0.8125rem, 1.8vw, 0.9375rem)` | Metadata, side-note |

Line height: body 1.6, heading 1.15.
Letter spacing: hero -0.02em, body 0, all-caps meta +0.08em.

## Layout

**Strategy: rigorously-gridded "kézikönyv" — visible grid as voice**, NEM asymmetric. Egy kézikönyv strukturált — ez támogatja a sage / antropológiai voice-ot.

- Egy fő-oszlop, mobil-elsősorban. Max body szélesség: `min(92vw, 38rem)`.
- Bal margón **numbered side-marker** ("§ 01", "§ 02"...) — mint egy kézikönyv-fejezet-szám. Ez **manuál-érzetet** ad ami megkülönböztet az editorial-magazine-tól.
- Szekciók közt vékony `--rule` `<hr>`, NEM dekoratív gradient.
- Vertical rhythm: szekciók közt `clamp(4rem, 12vw, 7rem)`. **Generous, lélegzős.**
- Két termék prezentációja: mobile-en **stacked** (alul/felül), 768px+ tablet-en is még stacked. Csak 1024px+ desktop-on válik 2 oszlopra (de a one-pager mobil-elsősorban — desktop-on is jó, ha stack marad, csak nagyobb fehér margóval).

**SOHA:**
- Side-stripe border-eket (border-left: 4px solid orange) — abszolút ban.
- Identical card grid-eket (icon + heading + text repeated).
- Glassmorphism-et.
- Hero-metric template-et.
- Centered-stack-et generic icon-title-subtitle elrendezéssel.

## Imagery

Brand surface, **dev-tool kategória körüli** — ez az a brand-faj, ahol **zero imagery acceptable**, ha a voice tipográfia + szöveg + struktúra-elem (numbered sections, dimension chips) hordozza.

A jelen iterációban: **zero photographic imagery**. Helyette:
- Római számozás (I., II., III., IV.) a 4 dimenzióhoz.
- Vékony decorative rule-line-ok szekciók között.
- A két termék közti vizuális kontraszt: Tájoló-szekciónak halvány `--paper-deep` háttér, Műhely-szekciónak `--paper` háttér + ochre side-marker.

Ha v0.2-ben kell imagery: egy **egyetlen, decisive Unsplash photo** a hero alá vagy a workshop-szekcióba (pl. egy könyv-spread vagy egy üres térkép / iránytű). Most v0.1-ben kihagyjuk — a copy és a tipográfia hordozza a brand-érzetet.

## Motion

**Tech-minimal motion** — egy nyugodt fade-in az első nézettel a hero-n, ennyi.

- `prefers-reduced-motion: reduce` → minden motion off.
- Hero: 600ms ease-out-quart fade + 12px translateY a tagline-ra. Egyszer.
- Szekció-headers: scroll-triggered fade-in (IntersectionObserver) 400ms ease-out-quart. **Egyszer / szekció, nem repeat.**
- Hover állapotok: 180ms ease-out, csak `color` és `background-color`, NEM layout property.

## Components

**Hero:**
- Anyabrand kis label (felül, all-caps, ochre, +0.08em tracking)
- Tagline: hero font-size, display weight 600
- Sub-line: body+, ink-soft

**Numbered section ("§ 01" stb.):**
- Bal margón a §-jel + szám (EB Garamond italic, ink-soft)
- Section title h1 méretben
- Body szöveg

**Product card (Tájoló / Műhely):**
- Felül: római számozás (I. / II.) ochre színben + termékcsoport-tag ("Tájoló" / "Műhely") EB Garamond small caps
- Cím, sub-line
- Bullets — egyszerű unstyled list, vezérlőkötőjel ("—") helyett kis ochre négyzet
- CTA (lásd alább)

**Dimension chip:**
- Egysoros: római szám (I.), pötty a `--dim-X` színben, latin-görög név (Ethos/Logos/Pathos/Thelos), magyar kísérőszó (Felelősség / Értelem / Empátia / Vágyak)

**CTA (button):**
- Primary: ochre háttér, paper szöveg, no border, no radius (vagy 4px max). Padding 1rem 1.75rem. EB Garamond 500.
- Secondary: ink-soft text, vékony rule alá, NEM keret. "Hallgasd meg / Töltsd le" típusú low-commitment.

**Cross-sell footnote:**
- A két termék közt egy small block (`--paper-deep` háttér, ink), mely magyarázza "ez nem szekvenciális, ez két ösvény".
