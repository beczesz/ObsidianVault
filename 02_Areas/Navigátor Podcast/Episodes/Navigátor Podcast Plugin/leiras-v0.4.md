---
description: YouTube leírás és hashtagek generálása SRT fájlból (v0.4 — top-performer szerkezet: EP14 78K-os referencia alapján bővítve)
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: 68dbb5ee-32a1-45e8-a874-b5b6a7d3aebc
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.

## Kontextus betöltés

1. Olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/SKILL.md` fájlt
2. Olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/references/csatorna-intelligencia.md` fájlt

Különösen a „Leírás és SEO" és a „A sorozat-hatás" szekciókra figyelj.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal.
2. Olvasd be az SRT fájlt a Read tool-lal.
3. Kérdezd meg a felhasználót az AskUserQuestion tool-lal:
   - **A vendég neve**
   - **Az epizód száma** (pl. EP43)
   - **Van-e korábbi epizód ezzel a vendéggel?** (Ha igen, melyik EP szám + URL?)
   - **Van-e tematikusan kapcsolódó korábbi epizód?** (Ha igen, melyik EP szám + URL?)

## Feladat: YouTube leírás és hashtagek

Készíts SEO-optimalizált, KÉSZRE FORMÁZOTT leírást, amely tartalmazza az összes
top-performer elemet. Referencia: EP14 „A rejtett nárcizmus jelei" (78K views,
csatorna #1 organic performer).

### Teljes szerkezet — KÖTELEZŐ sorrend

#### 1. HOOK (1 sor — a „Több" gomb előtt látszik)

Erős kérdés vagy provokatív állítás. Idézet formátum is elfogadható.
Legalább 1 kereshető kulcsszót tartalmazzon (pl. „nárcizmus", „kiégés", „gyász"
— nem költői, hanem konkrét).

Példa: `„Nem veled van a baj" — de hogyan ismerd fel, hogy nárcisztikus kapcsolatban élsz?`

#### 2. RÖVID KONTEXTUS (1 paragrafus, 2-3 mondat)

Vendég bemutatása + központi problémafelvetés. Kulcsszavakkal.

Példa:
`Bencze Edit pasztorálpszichológussal feltárjuk a rejtett (covert) nárcizmus
jeleit, a manipulációs technikákat (gaslighting, love bombing, breadcrumbing),
a munkahelyi nárcizmust és a kiút útjait.`

#### 3. EBBEN AZ EPIZÓDBAN — 5-7 bullet pont (ÚJ! KÖTELEZŐ)

Konkrét, kereshető altémák. Mindegyik egy egész gondolat, kérdés vagy provokatív
állítás. A YouTube AI ezeket szemantikus kulcsszóként használja a Suggested
Videos algoritmusban.

Példa:
```
Ebben az epizódban:
• Nyílt vs. rejtett (covert) nárcizmus — melyik a veszélyesebb?
• Gaslighting, love bombing, breadcrumbing — a manipuláció eszköztára
• A „hideg empátia": pontosan érzékeli, mit érzel — és felhasználja
• Munkahelyi nárcizmus és a repülő majmok
• Szürke szikla technika és mikor kell kilépni
```

#### 4. CROSS-REFERENCIA (ha van korábbi/kapcsolódó EP)

A sorozat-hatás kihasználása — az end-screen CTR egyetlen bizonyított növelője
(EP28 minta: 1.4% CTR).

```
Folytatás — EP[##]: [Cím] →
https://youtu.be/[ID]
```

Vagy ha több kapcsolódó:
```
🔗 Kapcsolódó epizódok:
EP14 — A nárcizmus rejtett arcai | Bencze Edit: https://youtu.be/[ID]
EP28 — Nárcisztikus kapcsolatokból kiút | Bencze Edit: https://youtu.be/[ID]
```

#### 5. IDŐKÓDOK (KÖTELEZŐ! — 0:00-tól)

⚠️ **Ez aktiválja a YouTube Chapters UI-t** — közvetlen retention-növelő.

Szabályok:
- **Az első timestamp KÖTELEZŐ 0:00**, különben a Chapters nem aktiválódik
- 10-12 időkód javasolt
- Formátum: `[M:SS]` vagy `[MM:SS]` vagy `[H:MM:SS]` — szóköz nélkül a cím
- Nincs bullet point, nyers szöveg új sorokban

Példa:
```
Időkódok:
0:00 Bevezető — személyes érintettség
0:10 Nyílt vs. rejtett nárcizmus — a spektrum
0:25 Manipulációs technikák: gaslighting, love bombing, breadcrumbing
0:50 Hideg empátia és az alapelvek instrumentalizálása
1:10 Munkahelyi nárcizmus és a repülő majmok
```

#### 6. SOCIAL MEDIA BLOKK (ÚJ! KÖTELEZŐ)

Elválasztó `---` után. Formátum:

```
---
Facebook: https://web.facebook.com/navigatorpodcast
Instagram: https://www.instagram.com/anavigatorpodcast/
TikTok: https://www.tiktok.com/@navigatorpodcast
Spotify: https://podcasters.spotify.com/pod/show/navigtor-podcast
```

#### 7. KRÉDIT + TÁMOGATÓK (ÚJ! KÖTELEZŐ)

```
A podcastet gyártotta: Szabó Sámuel / Samwork Studios
Támogatóink: Média Műhely, Eötvös-udvar, ExarLabs, Vekker Kávéközösség
Média Műhely: https://web.facebook.com/mediamuhely0
Vekker Kávéközösség: https://web.facebook.com/vekkerkavekozosseg
```

#### 8. HASHTAGEK (8-11 db)

Elválasztó `---` után. Vegyítsd:
- **2 állandó (kötelező):** `#NavigátorPodcast`, `#MagyarPodcast`
- **2-3 fő téma:** szélesebb keresési volumen (pl. `#Nárcizmus`, `#Pszichológia`)
- **3-5 specifikus altéma:** keskeny, magas-intent (pl. `#RejtettNárcizmus`,
  `#CovertNárcizmus`, `#Gaslighting`, `#LoveBombing`, `#NárcisztikusKapcsolat`)
- **1 vendégnévhez kötött:** (pl. `#BenczeEdit`) — különösen fontos visszatérő
  vendégeknél (sorozat-hatás)

### Stílus

- Olvasmányos, tagolt, motiváló
- Rövid bekezdések — mobilon olvasható
- Kulcsszavak az első 2 sorban (SEO!)
- Idézetek `„…"` típusú magyar idézőjelek között

### SEO ellenőrzőlista (v0.4 — bővített)

A leírás leadása előtt ellenőrizd:
- [ ] **Hook tartalmaz kereshető kulcsszót?** (első 2 sor)
- [ ] **„Ebben az epizódban:" blokk 5-7 bullet pontot tartalmaz?**
- [ ] **Cross-referencia szerepel** (ha van releváns korábbi EP)?
- [ ] **Időkódok 0:00-tól indulnak**, 10-12 db, helyes formátum?
- [ ] **Social media linkek mind a 4 platformhoz** (FB, IG, TikTok, Spotify)?
- [ ] **Krédit + Támogatók blokk megvan**?
- [ ] **Hashtagek 8-11 db**, tartalmazza a 2 állandót + vendég nevét?
- [ ] **Mobil olvashatóság** (rövid bekezdések, üres sorok blokkok között)?

### Példa végeredmény (referencia: EP14 — top performer, 78K views)

```
„Nem veled van a baj" — de hogyan ismerd fel, hogy nárcisztikus kapcsolatban élsz?

Bencze Edit pasztorálpszichológussal feltárjuk a rejtett (covert) nárcizmus
jeleit, a manipulációs technikákat (gaslighting, love bombing, breadcrumbing),
a munkahelyi nárcizmust és a kiút útjait.

Ebben az epizódban:
• Nyílt vs. rejtett (covert) nárcizmus — melyik a veszélyesebb?
• Gaslighting, love bombing, breadcrumbing — a manipuláció eszköztára
• A „hideg empátia": pontosan érzékeli, mit érzel — és felhasználja
• Munkahelyi nárcizmus és a repülő majmok
• Szürke szikla technika és mikor kell kilépni

Folytatás — EP28: Hogyan erősödjünk meg nárcisztikus kapcsolatokban →
https://youtu.be/tJNbiLjg5ks

Időkódok:
0:00 Bevezető — személyes érintettség
0:10 Nyílt vs. rejtett nárcizmus — a spektrum
0:25 Manipulációs technikák: gaslighting, love bombing, breadcrumbing
0:50 Hideg empátia és az alapelvek instrumentalizálása
1:10 Munkahelyi nárcizmus és a repülő majmok
1:35 Szülő-gyerek dinamika, anyai nárcizmus
1:50 Maradni vagy menni? A házastársi dilemma
2:00 Megoldási utak: szürke szikla, szakember, önképzés

---
Facebook: https://web.facebook.com/navigatorpodcast
Instagram: https://www.instagram.com/anavigatorpodcast/
TikTok: https://www.tiktok.com/@navigatorpodcast
Spotify: https://podcasters.spotify.com/pod/show/navigtor-podcast

A podcastet gyártotta: Szabó Sámuel / Samwork Studios
Támogatóink: Média Műhely, Eötvös-udvar, ExarLabs, Vekker Kávéközösség
Média Műhely: https://web.facebook.com/mediamuhely0
Vekker Kávéközösség: https://web.facebook.com/vekkerkavekozosseg

---
#NavigátorPodcast #MagyarPodcast #Nárcizmus #RejtettNárcizmus #CovertNárcizmus
#Gaslighting #LoveBombing #NárcisztikusKapcsolat #BenczeEdit #Pszichológia
#NárcizmusJelei
```

## Változások v0.3 → v0.4

Az EP14 (78K views, csatorna #1 performer) teljes szerkezetének leképezése:
1. **ÚJ:** „Ebben az epizódban:" 5-7 bullet pont — szemantikus SEO + scannability
2. **ÚJ:** Időkódok 0:00-tól → aktiválja a YouTube Chapters UI-t (retention!)
3. **ÚJ:** Social media blokk (FB, IG, TikTok, Spotify)
4. **ÚJ:** Krédit + Támogatók blokk (Samwork Studios, Média Műhely, Eötvös-udvar,
   ExarLabs, Vekker Kávéközösség)
5. **BŐVÍTVE:** Hashtagek 8-11 db (volt 5-8), kötelezően vendégnévvel
