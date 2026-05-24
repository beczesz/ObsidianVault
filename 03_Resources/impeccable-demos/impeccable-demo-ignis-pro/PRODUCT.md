# PRODUCT.md — IGNIS professional / Elektromobilitás szakképzés (demó)

> Tanuló-demó, 4. variáns. A paletta a valódi logóból származtatva:
> 02_Areas/Ignis/Marketing/21 Alkalom - Előlap.png
> Készült `/ui-ux-pro-max` + `/impeccable` bemutatására. Képek: hotlinkelt Unsplash.

## Register

**brand** — energikus, magabiztos kurzus-landing. A látogatónak azt kell éreznie:
"ez komoly, gyakorlati, és lendületet ad a karrieremnek". Lendület és tűz, de nem hype-scam.

## Product Purpose

Az **IGNIS professional** intenzív **elektromobilitási szakképzés** bemutatkozó oldala:
**21 alkalmas** program (AFM Electromobil kontextus). Cél: (1) lendületes, bizalomkeltő
belépő, (2) a 21 alkalom tananyagának átlátható bemutatása, (3) gyakorlati kimenetek és
oklevél, (4) bizalom (oktatók, EU/AFM-támogatás), (5) jelentkezés.

## Users

Szakemberek és karrierváltók: autószerelők, villanyszerelők, technikusok, flottakezelők,
valamint pályakezdők, akik az elektromobilitásban látják a jövőt. Gyakorlatias, konkrét
tudást és elismert papírt akarnak, nem elméleti ködöt. Lendületet és magabiztosságot keresnek.

## Brand & Tone

- **Energikus, magabiztos, gyakorlatias.** "Lángra lobbantjuk a karriered." de földön járó.
- **Tűz mint metafora** (ignis = tűz): lendület, energia, átalakulás — nem agresszió.
- Magyar "te"/"ti" hang, tárgyilagos, konkrét. Anti-hype: számok és tananyag, nem jelszavak.

## Visual system (a LOGÓBÓL származtatva — OKLCH)

- **Téma: SÖTÉT** (mély navy). Indok: esti, fókuszált döntés egy karrierlépésről; a navy + tűz
  prémium-technikai, energikus érzetet ad — és tudatos eltérés az előző 3 világos oldaltól.
- **Szín-stratégia: Full palette / bold** — navy felület + tűz-akcentek.
- Logó-színek → tokenek:
  - navy háttér `#0E293E` → `oklch(0.255 0.045 248)` (page bg sötétebb: ~0.20)
  - piros (primary) `#CF2232` → `oklch(0.555 0.205 22)`
  - narancs (secondary) `#DB7722` / `#E96425` → `oklch(0.675 0.16 50)`
  - sárga (spark) `#FBF000` → `oklch(0.915 0.19 103)`
- **Signature device:** a logó láng-nyíl (chevron) + a **sárga→narancs→piros tűz-gradiens**,
  visszatérő motívumként: chevron-mark, hero highlight, a nagy „21", a tananyag-gerinc
  (progress spine), szekció-elválasztók, CTA gombok.
- **Tipó:** Sora (display, geometrikus, prémium, nagybetűs tracking a logó-echo miatt) + Inter (törzs).
- **Fotó-kezelés:** egységes **navy→tűz split-tone duotón** (grayscale + diagonális
  navy→narancs gradiens, mix-blend), hoverre természetes színre old + enyhe zoom.

## Anti-references (kerülni)

- ui-ux-pro-max „bootcamp" reflexe: gamer/esports (Russo One + Chakra Petch, neon zöld). NEM.
- Hype-scam kurzus-landing: „KERESS MILLIÓKAT", visszaszámláló-pánik, hamis szűkösség.
- Steril corporate kék SaaS. Stock kézfogás dísznek (ha kézfogás, akkor duotónnal, indokoltan).
- Gradient-szöveg, üveghatás dísznek, egyforma ikonos kártyarács.

## Scope (demó)

`index.html` + `styles.css` + `main.js`, statikus. Képek: hotlinkelt Unsplash, navy→tűz duotón.
Szekciók: header → hero (21 alkalom hook, EV-kép) → miért most (tűz-band) → tananyag
(21 alkalom, modulokba szervezve, gradiens-gerinc) → mit fogsz tudni → formátum → kinek →
oktatók/hitelesség → végzős idézet → jelentkezés (CTA) → footer. Nyelv: magyar.
Reszponzív, akadálymentes (sötét téma kontraszt-ellenőrzéssel).
