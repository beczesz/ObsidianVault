# PRODUCT.md — OBLIQUE / Architecture Studio (fiktív demó)

> Tanuló-demó. A stúdió, a projektek, a díjak és a személyek mind kitaláltak.
> Készült az `/ui-ux-pro-max` (template/stílus választás) + `/impeccable` (craft) bemutatására.
> Valódi, jogtisztán hotlinkelt Unsplash építészfotók illusztrációként.

## Register

**brand** — galéria-szintű portfólió. A dizájn maga a termék: a stúdió ízlését és
igényességét bizonyítja, mielőtt egyetlen szót is elolvasnának.

## Product Purpose

Egy nemzetközi építészstúdió bemutatkozó/portfólió oldala. Egyetlen, hosszú,
mozgásvezérelt landing oldal. Célja: (1) azonnal éreztetni a kézművességet és a léptéket,
(2) bemutatni a válogatott munkákat szerkesztői ritmusban, (3) átadni a stúdió szemléletét
("Mass & Void"), (4) bizalmat építeni díjakkal/sajtóval, (5) egyszerű kapcsolatfelvétel.

## Users

- **Potenciális megbízók** (fejlesztők, intézmények, magántőkés ügyfelek): léptéket,
  megbízhatóságot és esztétikai szintet keresnek. Gyakran nagy képernyőn, este.
- **Szakmai közönség** (sajtó, díjbizottság, leendő munkatársak): a portfólió mélységét
  és a szemlélet eredetiségét nézik.

Amire szükségük van: nagy, jól megmutatott képek; gyors átfutás a projekteken; egy
emlékezetes szemléleti állítás; minimális, nem tolakodó navigáció.

## Brand & Tone

- **Csendes magabiztosság.** A munka beszél, nem a jelzők. Kevés szó, nagy levegő.
- **Anyagszerű, tárgyilagos.** Tömeg, fény, anyag, arány. Nem lifestyle-marketing.
- **Editorial, nem brosúra.** Úgy olvad össze szöveg és kép, mint egy építészeti magazinban.
- Szemléleti mottó: **"Mass, light, and the space between."**

## Strategic Principles

1. **A kép az úr.** A felület halk és meleg-semleges, hogy a fotók vigyék a színt és a drámát.
2. **Tömeg és üresség ritmusa.** Világos "vakolat" szekciók és teljes szélességű sötét
   ("mass") sávok váltakoznak — ez maga a fő kompozíciós eszköz.
3. **Kártya helyett szerkesztői elrendezés.** A projektek NEM egyforma kártyák rácsban,
   hanem aszimmetrikus, váltakozó méretű editorial blokkok.
4. **A mozgás cél, nem dísz.** Lassú, ease-out reveal és finom parallax — galéria-tempó,
   semmi pattogás. `prefers-reduced-motion` teljeskörűen tisztelve.

## Design decisions (ui-ux-pro-max alap → impeccable finomítás)

- **ui-ux-pro-max ajánlás:** Portfolio Grid pattern + Motion-Driven style + Archivo/Space Grotesk
  + "minimal fekete + arany" paletta.
- **impeccable korrekció:** a "fekete + arany építész" a kategória-reflex (AI-slop kockázat).
  Helyette: **meleg vakolat (plaster) + meleg majdnem-fekete tinta + egyetlen visszafogott
  terrakotta/agyag akcent** (a téglát/terrakottát idézi, anyagszerű). A Motion-Driven
  irányt és a Portfolio Grid struktúrát megtartjuk. Tipó: **Bricolage Grotesque** (display,
  karakteres, modern) + **Space Grotesk** (törzs/labelek, technikai, jó a projekt-specekhez).

## Anti-references (amit NEM akarunk)

- "Fekete háttér + arany szöveg" lézersugaras luxus-klisé.
- Egyforma ikon+cím+szöveg projektkártyák végtelen rácsban.
- Gradient-szöveg, üveghatás dísznek, hero-metrika sablon (nagy szám + kis label).
- Stock "öltönyös építész tervrajz fölött" hangulat. Túlírt marketinghang.

## Scope (demó)

`index.html` + `styles.css` + `main.js`, statikus, build nélkül. Képek: hotlinkelt Unsplash.
Szekciók: header → editorial hero (featured image, parallax) → Selected Works (aszimmetrikus,
~6 projekt) → teljes szélességű "mass" sáv → Approach (Mass & Void, számozott elvek) →
Studio (alapítók, meleg belső kép) → Recognition (díjak) → Contact (nagy CTA) → footer.
Nyelv: angol (nemzetközi galéria-hang). Reszponzív, akadálymentes, lazy-load + CLS-mentes képek.
