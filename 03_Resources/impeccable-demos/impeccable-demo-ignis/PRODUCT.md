# PRODUCT.md — Ignis Academy / online tanulóközpont (demó)

> Tanuló-demó. A brand valódi (a vault Ignis anyagából), a landing oldal és a képek
> illusztrációk. Készült `/ui-ux-pro-max` + `/impeccable` + Librarian bemutatására.
> Forrás: 02_Areas/Ignis/AI Course HBC/Pozicionalas/{DESIGN, brand-brief, PRODUCT, MESSAGING}.md
> és 02_Areas/Ignis Academy/{CLAUDE, BMC}.md

## Register

**brand** — a dizájn maga a meggyőzés. Egy 35-55 éves KKV-vezetőnek azt kell éreznie:
"végre valaki nem egy újabb trendet üvölt rám", hanem nyugalmat és tisztaságot kínál.

## Product Purpose

Az **Ignis Academy** online tanulóközpont bemutatkozó oldala. AI-vezérelt, ember-központú
készségfejlesztő platform + két képzési formátum. Cél: (1) nyugodt, anti-hype belépés,
(2) a 4 emberi dimenzió (Ethos/Logos/Pathos/Thelos) keret bemutatása mint védjegy,
(3) a képzések/platform átláthatóvá tétele, (4) bizalom, (5) alacsony küszöbű kapcsolat.

## Users

35-55 éves magyar/erdélyi KKV-vezetők, középvezetők, tudásmunkás-alkotók. Kipróbálták a
ChatGPT-t, de elvesztek a hype-ban. NEM AI power-userek, NEM fejlesztők. Nyugalmat,
elvi tisztaságot és gyakorlatba ültethető tudást keresnek, nem "10 lépés" trükköket.

## Brand & Tone (a vault brand-brief + PRODUCT.md alapján)

- **Archetípus:** Sage (bölcs), antropológiai keretre építve. Aaker: competence + sincerity.
- **Hang:** vízszintes (peer-level, "te"), tömör, gyakorló. Székely tárgyilagosság. Anti-hype.
- **Érzelmi cél:** nyugalom és tisztaság, nem izgalom-túladagolás.
- **Tagline (primary):** „Ne harcolj az AI ellen. Légy emberibb tőle."
- **Tézis:** Az AI az eszköz; arra való, hogy emberibbé válj, nem hogy 10x produktívabb.

## Visual system (a vault DESIGN.md-ből — OKLCH)

- **Esztétika:** „1968-as agronómiai zsebkönyv borítója" — meleg field-guide / kézikönyv. Világos téma.
- **Szín-stratégia: Committed** — meleg **okker** (`oklch(0.68 0.135 75)`) a felület 25-35%-án.
- Tokenek: paper `0.97 0.008 85`, paper-deep `0.94 0.012 85`, ink `0.22 0.008 60`,
  ink-soft `0.42 0.010 60`, rule `0.82 0.008 75`, ochre `0.68 0.135 75`, ochre-deep `0.52 0.130 65`.
- 4 dimenzió-akcent: Ethos agyagvörös `0.50 0.115 30`, Logos pala-kék `0.43 0.060 240`,
  Pathos terra `0.62 0.130 50`, Thelos fenyőzöld `0.36 0.055 160`.
- **Tipó:** EB Garamond (display, magyar ékezetek, 500-700) + Atkinson Hyperlegible (törzs, accessibility-first).
- Dimenzió-tagek: EB Garamond kiskapitális, római számok (I. II. III. IV.).
- **Fotó-kezelés (a v0.1 "no photo" felülírása a felhasználó kérésére):** minden kép egységes
  meleg duotón/okker filterrel, hogy "nyomtatott kézikönyv-tábla" hatású legyen, ne stock.

## Anti-references (a vault PRODUCT.md-ből — szigorúan kerülni)

- AI-guru landing: neon gradient, „10x produktivitás", rakéta-emoji.
- Vendor Copilot: céges kék gradient.
- Klim-stílusú editorial-tipográfiai minimalizmus (a 2026-os AI-startup default csapda).
- Stripe-szerű steril SaaS-hűvösség.
- Magyarított corporate: Calibri + business stock fotó.
- (ui-ux-pro-max „education" reflexe: gyerek-clay, Baloo/Comic Neue, teal+narancs — NEM ez.)

## Scope (demó)

`index.html` + `styles.css` + `main.js`, statikus. Képek: hotlinkelt Unsplash, okker duotónnal.
Szekciók: header → hero (tagline + csendes kép) → tézis/manifesztó → 4 dimenzió (védjegy) →
képzések (Tájoló, Műhely, Platform) → hogyan működik → kiknek (és kiknek nem) → oktató/about →
idézet → CTA/kapcsolat → footer (EU-grant hitelesség). Nyelv: magyar. Reszponzív, akadálymentes.
