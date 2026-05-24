# Navigátor Podcast — Új Videó Publikálási Checklist

**Verzió:** 1.0 | **Dátum:** 2026-04-09
**Cél:** Minden új epizód ELEVE optimálisan induljon — ne utólag kelljen pótolni, amit az elején is meg lehetett volna csinálni.

---

## FÁZIS 0 — Felvétel előtt (EP előkészítés)

- [ ] Vendég kutatás + korábbi epizódok cross-referencia ellenőrzés
- [ ] Felkészülési kérdések elkészítése (`/meghivo` command)
- [ ] Meghívólevél elküldése a vendégnek
- [ ] Tematikus klaszter azonosítása — melyik playlistbe fog kerülni?
- [ ] Előzetes Cards-terv: mely korábbi epizódokra fogunk linkelni a videóból?

---

## FÁZIS 1 — Felvétel után, publikálás előtt

### 1.1 SRT feldolgozás és szintézis

- [ ] SRT fájl elkészítése / letöltése
- [ ] Szintézis futtatása (`/szintezis` command)
- [ ] Szintézis review: kulcsüzenetek, idézetek, témák ellenőrzése

### 1.2 Metadata generálás

- [ ] **Cím** generálás (`/cim` command)
  - Formátum: `„Erős állítás/Idézet" – Téma | Vendég neve | EP[szám]`
  - Max 55-60 karakter (mobilbarát)
  - Fő kulcsszó az első 3-5 szóban
  - Egyértelmű ígéret: mit kap a néző?
- [ ] **Thumbnail szöveg** generálás (`/thumbnail` command)
  - Max 3-4 szó
  - NE ismételje a címet, hanem egészítse ki
  - Provokatív, kérdő vagy tényközlő stílus
- [ ] **Leírás** generálás (`/leiras` command)
  - Hook (első 2 sor): erős kérdés vagy provokatív állítás
  - Kontextus: vendég + problémafelvetés
  - Összefoglaló: 3-4 mondat, kulcsszavakban gazdag
  - Hashtagek: #NavigátorPodcast #MagyarPodcast + 3-6 témaspecifikus
- [ ] **Időkódok** generálás (`/idokod` command)
  - 10-12 kulcspillanat
  - Az időkódok a leírásba kerülnek
- [ ] **Cold Open / Hook** generálás (`/hook` command)
  - A videó elejére kerülő "felvezetés" szövege

### 1.3 Thumbnail készítés

- [ ] Thumbnail elkészítése (arc + 3-4 szó + kontrasztos háttér)
- [ ] Mobilon ellenőrizve: olvasható-e kis méretben?
- [ ] A szöveg és a cím együtt "minitörténetet" mesél?

---

## FÁZIS 2 — Publikálás (YouTube Studio)

### 2.1 Feltöltés és alapbeállítások

- [ ] Videó feltöltés YouTube Studio-ba
- [ ] Cím beillesztése (a generált és jóváhagyott verzió)
- [ ] Leírás beillesztése (hook + kontextus + összefoglaló + időkódok + hashtagek)
- [ ] Thumbnail feltöltése
- [ ] Kategória: People & Blogs / Education (a témától függően)
- [ ] Nyelv: Magyar
- [ ] Tags hozzáadása (témaspecifikus + állandó: Navigátor Podcast, magyar podcast)

### 2.2 End Screen beállítás

- [ ] End Screen hozzáadása (utolsó 20 mp)
  - "Best for viewer" automatikus ajánlás VAGY tematikusan kapcsolódó videó
  - Feliratkozás gomb
- [ ] Ellenőrzés: megjelenik-e a preview-ban?

### 2.3 Cards beállítás

- [ ] Minimum 2-3 Card hozzáadása a videóhoz
  - Card #1: A retention-görbe esése ELŐTT (általában 20-30%-nál) → legrelevansabb korábbi epizód
  - Card #2: A videó közepén (50%) → tematikusan kapcsolódó epizód
  - Card #3 (opcionális): Második félidőben → playlist vagy másik releváns videó
- [ ] Cards célpontok a tematikus klaszterből kiválasztva
- [ ] Ellenőrzés: a kártyák a megfelelő időpontoknál jelennek meg?

### 2.4 Playlist

- [ ] Videó hozzáadva a megfelelő tematikus playlisthez:
  - 🧠 Pszichológia és mentális egészség
  - 🤖 AI és technológia
  - 💼 Vállalkozás és vezetés
  - ❤️ Egészség és életmód
  - 🎨 Kultúra és kreativitás
  - 🏠 Család és kapcsolatok
  - ☕ Személyes történetek
- [ ] Ha több playlistbe is illik → mindegyikbe hozzáadva

---

## FÁZIS 3 — Publikálás után (első 48 óra)

### 3.1 Pinned Comment

- [ ] Pinned Comment megírása és kitűzése. Tartalmazza:
  - Kérdés a nézőkhöz (engagement driver)
  - Cross-promote link a legrelevansabb korábbi epizódra
  - Rövid CTA (pl. "Ha tetszett, nézd meg az EP[X]-et is, ahol folytatjuk a témát → [link]")
- [ ] Példa formátum:
  ```
  Ha ez a beszélgetés megérintett, nézd meg az EP[X]-et is, ahol [rövid leírás] → [link]
  Ti mit gondoltok? [releváns kérdés] 👇
  ```

### 3.2 Community Tab poszt

- [ ] Publikálási poszt a Community Tab-on
  - Rövid teaser szöveg (ne a címet ismételd!)
  - Link a videóra
  - Kérdés vagy szavazás a témáról

### 3.3 Cross-linking visszafelé

- [ ] A KAPCSOLÓDÓ RÉGI videók frissítése:
  - Pinned Comment frissítés a régi videón (ha releváns): "Azóta megjelent a folytatás → [link]"
  - VAGY: Ha van régebbi videó ugyanazzal a vendéggel, ott is frissíteni a pinned commentet
- [ ] Leírás frissítés a régi videón: "Kapcsolódó: [új videó cím + link]" hozzáadása

---

## FÁZIS 4 — Első hét (optimalizálás)

### 4.1 Analytics ellenőrzés (48 óra után)

- [ ] CTR (Click-Through Rate) ellenőrzése — cél: >5%
  - Ha <3%: fontold meg a cím vagy thumbnail cseréjét
- [ ] Retention görbe ellenőrzése
  - Hol esik el a legtöbb néző? → következő videóknál ez alapján tervezz Cards pozíciót
- [ ] Traffic sources áttekintése — honnan jönnek a nézők?

### 4.2 A/B teszt (opcionális, ajánlott)

- [ ] YouTube A/B teszt indítása a címre (ha a CTR alacsony)
  - Max 3 variáns tesztelhető
- [ ] Thumbnail A/B teszt (ha elérhető)

### 4.3 Shorts tervezés

- [ ] 3-5 Shorts jelölt kiválasztása a szintézis/SRT alapján
  - Keress: erős idézeteket, meglepő állításokat, praktikus tippeket, érzelmi csúcspontokat
- [ ] Shorts ütemezése (heti 3-5 db a publikálás utáni hetekben)
  - Minden Short végén: "A teljes beszélgetés a leírásban" + link

---

## FÁZIS 5 — Tracking és dokumentáció

- [ ] `synthesis_map.md` frissítése az új epizóddal
- [ ] `plan.md` frissítése (ha releváns fázisokat érint)
- [ ] Szintézis fájl mentése a Synthesis mappába
- [ ] EP szám és videó ID rögzítése

---

## Gyors referencia — Állandó elemek

| Elem | Érték |
|------|-------|
| Állandó hashtagek | #NavigátorPodcast #MagyarPodcast |
| Cím formátum | „Idézet" – Téma \| Vendég \| EP[szám] |
| Cím max hossz | 55-60 karakter |
| Thumbnail max szavak | 3-4 |
| Időkódok száma | 10-12 |
| Cards minimum | 2-3 per videó |
| End Screen | Utolsó 20 mp, "Best for viewer" + Subscribe |
| Playlist | Min. 1 tematikus playlisthez hozzáadni |

---

## Megjegyzések

- **Data API v3** jelenleg nem működik (0 kvóta) → metadata frissítések YouTube Studio-n keresztül (Chrome MCP vagy manuálisan)
- **Analytics API** működik → CTR, retention, traffic source ellenőrzésre használható
- A `/cim`, `/leiras`, `/thumbnail`, `/hook`, `/idokod` parancsok SRT fájlból dolgoznak — a szintézis ELŐTT is futtathatók, de a szintézis utáni kontextussal pontosabb eredményt adnak
- Cards pozicionáláshoz a retention-görbe a legjobb útmutató — az első nagy esés ELŐTT tegyél card-ot
