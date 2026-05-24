---
name: Fókuszpont 2026 — Brainstorm State
type: think-engine-session
created: 2026-05-18
status: active
related_project: ../01_PROJECT_STATE.md
session_topic: 2-3 db 30 mp-es Fókuszpont reel forgatókönyv-fejlesztés
id: 3554f333-6b23-4a19-bcdd-cbcafd6d7e7e
index_schema_version: 1
---

# Brainstorm State — Fókuszpont 2026 Rövidvideók

## Goal

2-3 db 30 másodperces reel forgatókönyvének kidolgozása a 2026-os Fókuszpont imaesthez. Két alap-funkció kristályosodott ki:
- **Reel #1 — Vertikális** (Isten ↔ ember) — drámai, filozófiai, kontemplatív
- **Reel #2 — Horizontális** (fiatal ↔ fiatal) — könnyed, közösségi, „gyere velünk"
- Reel #3 — opcionális (TBD)

## Team

| AI | Role | Transport | Model / URL |
|----|------|-----------|-------------|
| Claude (this session) | Strategist + Synthesizer | local | claude-opus-4-7 |
| ChatGPT (prior session) | Dramaturgia / Reel-tanácsadó | Browser (history import) | [chat](https://chatgpt.com/c/6a0b380a-28c4-8385-99e4-63dd8bafd7f7) |
| Claude API | Forgatókönyv-író (planned) | API | claude-opus-4-7 |
| GPT-5 (API) | Validator (planned) | API | gpt-5 |

**Transzport döntés:** A ChatGPT chat egyszer beimportálva → onnantól minden további elemzés API-n keresztül (Part 2.5 elv).

**API kulcsok státusza:** ANTHROPIC ✓ · OPENAI ✓ · PPLX missing (nem szükséges).

## Source Material (imported)

### A felhasználó által hozott assets (külső)
- **2024 és 2025 tavalyi reel szövegek** — ✅ bekerültek `02_Areas/Fókuszpont/2024/Video script.md` és `02_Areas/Fókuszpont/2025/Video scrip.md` alá. Időzítés: SRT még nincs, csak szövegszintű prototípus.
- **2024-es Fókuszpont videófelvételek** — bevágható anyag (monstrancia, fény, felemelt tekintetek, csend, könnyek, térdelő emberek, worship, gyónás, kezek, fiatal arcok)
- **Vágó** — házon belül, dramaturgiailag erős
- **Pap (Tamás Barna atya)** — hiteles, békés hangú, ideális narrátor

### Vault-anyag
- [[../../02_Areas/Navigátor Podcast/Synthesis/Podcast/EP27 - Tamás Barna atya]] — EP27 szintézis: Fókuszpont mint imaest Székelyudvarhelyen, eukarisztia-központúság, „Istennek a legszebb, a legjobb jár", éves sorozat javaslat. Korábbi közönség (EP27): 100% nő, 51% 65+, 56% RO, FB-driven.

## ChatGPT konzultáció — kinyert kulcsmegállapítások

**Forrás:** https://chatgpt.com/c/6a0b380a-28c4-8385-99e4-63dd8bafd7f7
**Cím:** „Fókuszpont esemény leírása"
**Importálva:** 2026-05-18

### Alapelvek (ChatGPT validációja)
- **Nem promóvideó, hanem lelki diagnózis** — ez az alap-pozicionálás.
- **Dramaturgiai szerkezet:** fiatalok adják az érzelmi valóságot, a pap az irányt és értelmezést.
- **Figyelem-teológia** keret — a mai ember legnagyobb harca nem az ateizmus, hanem a szétszórtság. Ez az üzenet aktualitása.
- **„Nem csak egyházi reel"** — jó executionnel országosan is működhet.

### Reel #1 (vertikális) — dramaturgiai váz

**Szerepe:** „valami itt igaz" → megállít, nem meghív.

**Ív (30 mp):**

| Szakasz | Idő | Tartalom |
|---------|-----|----------|
| Szétesett figyelem | 0-10 mp | Kérdések, gyorsabb vágások, nyugtalanság, zaj. Pl. „Miért aggódsz?" / „Mit keresel?" / „Mire figyelsz?" |
| Felismerés | 10-20 mp | Lassulás, csend, mélység. „Amit nézel, az formál." / „És ha egész nap a félelmeidet nézed… akkor a félelem fog formálni." |
| Meghívás / válasz | 20-30 mp | Tavalyi Fókuszpont felvételek (monstrancia, közösség, fény). „Van egy pont, ahol minden tekintet Jézusra szegeződik." → FÓKUSZPONT / dátum / helyszín |

### 4-5 kérdés sweet spot (sorrend = lépcsőfok)

| # | Kérdés | Réteg |
|---|--------|-------|
| 1 | „Miért aggódsz?" | külső állapot — univerzális |
| 2 | „Mit keresel?" | belső hiány |
| 3 | „Mire figyelsz egész nap?" | fókusz |
| 4 | „Mi tölti meg a szívedet?" | identitás |
| 5 | „Kire nézel?" / „Mi történne, ha végre Jézusra szegeznéd a tekinteted?" | spirituális fordulat |

**Dramaturgia:** ne legyen mind kérdés — szúrjunk be kijelentéseket („Egész nap nézünk valamit." / „És amit nézünk… az formál minket."). A kijelentések megállítják a ritmust, súlyt és filozófiai mélységet adnak. Pure kérdés-narratíva „interrogációvá" válik.

### Stilisztikai döntések (Reel #1)
- **Pap hangja:** majdnem suttogó bizonyosság, ne prédikáció. Lehet végig **offscreen**, csak a végén látszik — filmesebb, belső monológ hatás.
- **Fiatalok:** ne színészkedjenek, hanem felismerhető állapotok (telefonbámulás, körömrágás, notification, magányos tömeg, plafonbámulás éjszaka, kapkodás, szétesett figyelem, túl sok inger).
- **Vágási ritmus:** első 10 mp gyors / zaklatott, középső lassul, utolsó 10 mp csendes / fényes.
- **Csend érték.** 1 másodperc jól időzített csend > 3 gyors vágás. „Túl sok minden beszél egyszerre" — ez maga az üzenet.
- **„Jézus a fókuszpont"** mondat: NE túl korán. Hadd épüljön. Előbb érezze az igazságot, mint magyarázza.
- **Vége NE eseményplakát legyen.** Ne: feszültség → dátum. Hanem: feszültség → felismerés → meghívás → DÁTUM.

### Reel #2 (horizontális) — váz

- **Energia:** könnyed, fiatalos, közösségi
- **Üzenet:** „gyere velünk", „én is ott akarok lenni"
- **Hang:** fiatalok hívnak meg fiatalokat, spontán, beszélt nyelv
- **Példa:** „Szeretnél találkozni Jézussal? Gyere egy vagány eseményre."
- **NEM** filozofál, NEM kontemplatív — behúz a közösségbe

### Reel #1 vs #2 — funkció-megosztás

| | Reel #1 | Reel #2 |
|---|---------|---------|
| Tengely | Vertikális (Isten↔ember) | Horizontális (fiatal↔fiatal) |
| Hangulat | Kontemplatív | Közösségi |
| Üzenet | „miért vagy szétesve?" | „gyere velünk" |
| Funkció | Megállít | Behúz |
| Hangerő | Csendes, lassuló | Energikus, gyors |

## Open Questions

- [ ] **Mennyi kérdés végül?** ChatGPT-vel 4-5 a sweet spot — de melyik 4-5? A fenti lépcsős sorozatból mi marad ki?
- [ ] **Mikor van a 2026-os Fókuszpont esemény?** (forgatási dátum)
- [ ] **Reel #3** — kell? Mi lenne a funkciója? (Post-event recap? Vendég-testimony? Behind-the-scenes?)
- [ ] **Tavalyi szöveg** — mi volt a 2024/2025 reel szövege és időzítése? (Szabolcs hozza)
- [ ] **Forgatási helyszínek** — fiatal-shotok hol? (utca / iskola / otthon / kávézó?)
- [ ] **Casting** — melyik fiatalok? Mennyi arc?
- [ ] **Zene / hangdesign** — milyen worship track / score? Ki keresi?
- [ ] **Csatorna-mix** — Instagram Reels + YouTube Shorts + Facebook (EP27 közönsége FB-driven volt!) — vertikális 9:16 az alap-format

## Next Steps

1. ✅ **Tavalyi szöveg** beimportálása — kész
2. ✅ **Reel #1 forgatókönyv v1** — kész (Opus + GPT-5 párhuzamos draft + szintézis):
   - `scripts/Reel-1_vertikalis_v1A_Opus.md` — Opus draft
   - `scripts/Reel-1_vertikalis_v1B_GPT5.md` — GPT-5 draft
   - `scripts/Reel-1_vertikalis_v1_FINAL.md` — **szintézis Szabolcs finomítására**
   - `scripts/Reel-1_vertikalis_v1_FINAL_voiceover.md` — plotter változat papnak
3. ✅ **Reel #2 forgatókönyv v1** — kész: `scripts/Reel-2_horizontalis_v1.md`
4. ⏳ **Szabolcs finomítás** — visszajelzés / cherry-pick a két AI verzióból
5. ⏳ **Kreatív brief** (`brief.md`) véglegesítése — Barna atyával egyeztetve
6. ⏳ **Casting + helyszín-recce** — fiatalok kiválasztása Reel #2-höz

## Raw Notes — ChatGPT teljes szövege

A teljes 3-fordulós ChatGPT konzultáció szövege megőrizve referenciaként (a fenti összegzésnél részletesebb, idézhető).

<details>
<summary>ChatGPT — 1. válasz (alapelvek)</summary>

> Szerintem ez működhet. Sőt, szerintem pont azért működhet, mert nem „promóvideóként" gondolkodsz róla, hanem lelki diagnózisként. És nagyon jó döntés az autoritás figura is. Nem azért, mert „pap kell a videóba", hanem mert: a fiatalok adják az érzelmi valóságot, a pap adja az irányt és az értelmezést.
>
> Ami szerintem különösen erős az ötletben: a kérdések nem támadnak. Nem prédikálnak. Hanem leállítják az embert egy pillanatra.
>
> Veszélyek:
> 1. ne legyen túl „színjátszós" — pillanatokat mutassatok, nem színészkedést (telefon, körömrágás, notification, magányos tömeg, plafonbámulás, kapkodás)
> 2. pap hangja legyen nyugodt, majdnem suttogó bizonyosság
> 3. vágások ritmusa: első fél gyorsabb, „Mire szegeződik a tekinteted?"-nél lelassul
> 4. NE eseményplakát legyen a vége: feszültség → felismerés → meghívás, és csak UTÁNA dátum
>
> Ez nem keresztény marketing, hanem figyelem-teológia. A mai ember legnagyobb harca a szétszórtság. Jó executionnel országosan is működhetne.

</details>

<details>
<summary>Szabolcs — 1. kérdés (kibontás)</summary>

> Jó, még pár részletet kihozzátennék. 30 másodperc kell legyen. Amint beérek a munkahelyemre, kikeresem a tavalyi reel szövegét és időzítését. Szerencsére tavalyi alkalomból szép videófelvételek születtek, ezt fel tudjuk használni. Jó vágónk van. Forgatókönyvet kell előkészítenünk. Az első nyugodtan lehet drámaibb, filozófiaibb, erőteljesebb. A második inkább fiatalos, könnyedebb — fiatalok hívnak meg fiatalokat. „Gyere egy vagány eseményre, ha szeretnél találkozni Jézussal".

</details>

<details>
<summary>ChatGPT — 2. válasz (vertikális/horizontális keret)</summary>

> Ez tudatos kampány-struktúra, nem csak két reel. Az első reel nem meghív — megállít. A második nem filozofál — behúz.
>
> Első reel: „valami itt igaz". Második: „én is ott akarok lenni".
>
> Tavalyi felvételek bevágása óriási előny — a végén megmutatható, hogy „ilyen az, amikor több száz ember tényleg ugyanoda néz" (monstrancia, fény, felemelt tekintetek, csend, könnyek, térdelő emberek, worship, gyónás, kezek, fiatal arcok).
>
> Dramaturgiai ív:
> - 0-10 mp: szétesett figyelem („Miért aggódsz?" / „Mit keresel?" / „Mire figyelsz?")
> - 10-20 mp: felismerés („Amit nézel, az formál." / „És ha egész nap a félelmeidet nézed…")
> - 20-30 mp: meghívás — tavalyi képek, monstrancia, „Van egy pont, ahol minden tekintet Jézusra szegeződik." → FÓKUSZPONT / dátum / helyszín
>
> Reel #1 vertikális (Isten↔ember), kontemplatív, „miért vagy szétesve?"
> Reel #2 horizontális (fiatal↔fiatal), közösségi, „gyere velünk"
>
> Pap akár végig offscreen az elsőben — csak hang, és csak a végén látjuk őt. Misztikusabb, filmesebb, belső monológ-hatás.
>
> Ne féljetek a csendtől. 1 mp jól időzített csend > 3 gyors vágás.

</details>

<details>
<summary>Szabolcs — 2. kérdés (kérdések száma)</summary>

> Először vertikálisat dolgozzuk ki. Hamarosan jelentkezem a tavalyi sablonnal. Konkrét forgatókönyv kell, és a papnak külön változat ahol csak a szöveg jelenik meg, szünetek kiemelve. Pap nagyon hiteles, békés hangú — beleillik.
>
> 4-5 kérdés érzésre a sweet spot. 2 túl kevés, 6 túl sok.

</details>

<details>
<summary>ChatGPT — 3. válasz (4-5 kérdés dramaturgia)</summary>

> 4-5 kérdés a sweet spot. 2 kérdés: nincs ritmus / fokozás / belső utazás. 6-7: túl gyors, intellektuális, érzelmi súly veszik.
>
> A LEGfontosabb döntés nem a kérdések száma, hanem a SORRENDJÜK. Nem információk — lépcsőfokok. Ne kezdj Jézusos kérdéssel — előbb emberi szinten szólítsd meg.
>
> Ív: nyugtalanság → keresés → szétesett figyelem → felismerés → meghívás/fókusz.
>
> Példa-sorozat:
> 1. „Miért aggódsz?" → univerzális
> 2. „Mit keresel?" → belső hiány
> 3. „Mire figyelsz egész nap?" → fókusz
> 4. „Mi tölti meg a szívedet?" → identitás
> 5. „Mi történne, ha végre Jézusra szegeznéd a tekinteted?" → átfordulás
>
> Ne legyen mind kérdés — szúrj be kijelentéseket („Egész nap nézünk valamit." / „És amit nézünk… az formál minket."). Tisztán kérdésekből álló narratíva „interrogációvá" válik.
>
> Legerősebb kérdések RÖVIDEK. Nem „Mi az, ami miatt sokszor úgy érzed, hogy elvesztél a mindennapokban?" — hanem „Mit keresel?". Üt. Hagy helyet a nézőnek.
>
> Szünetek hossza kritikus: kérdés után 1-2 mp lélegzés. Ez ad súlyt a képeknek.
>
> Kérdések egyre személyesebbek. Ne filozófiai előadás, hanem mintha valaki tényleg az ember lelkébe nézne.
>
> Ez már majdnem lelki zarándoklat 30 másodpercben.

</details>
