# Regule – Játékszabályok és Fejlesztési Terv

> Ez a fájl tartalmazza a román szótanuló játék specifikációját.
> Iteratívan fejlesztjük, lépésről lépésre.

---

## Jelenlegi verzió: v1.0

### Alapkoncepció
- A játék célja: a kislányom megtanulja a román szavakat
- Különleges szempont: **diszlexia-barát tervezés** (extra vizuális segítség, nagy betűk, kontrasztos színek, képközpontú megközelítés)
- A szavak forrása: `cuvinte.md` fájl (papír kártyákról lefényképezve bővítjük)

---

## v1 Specifikáció (aktuálisan kész)

### Kártya megjelenítés
- Mindig egy kártya jelenik meg egyszerre
- Jelenleg: csak a kép látható (emoji / illusztráció)
- A szó (román + magyar) egyelőre rejtve van

### Értékelő gombok (szülő értékel, nem a gyerek)
Három gomb a kártya alatt:

| Gomb | Jelentés | Következmény |
|------|----------|--------------|
| Tudja | Helyes válasz | A szót többé nem mutatja ebben a körben |
| Félig tudja | Részben helyes | A szó visszakerül randomra a pakli hátulsó felébe |
| Nem tudja | Helytelen | A szó visszakerül randomra a következő néhány kártya közé |

### Progress bar
- Látványos zöld sáv felül
- **Medve animáció:** a medve a képernyő bal oldalától indul és a barlangja felé halad jobbra
- Minden "Tudja" kártyával a medve előrelép
- Cél: medve elérje a barlangot = kör vége, ünneplés!

### Szókészlet (v1)
- Állatok, gyümölcsök, zöldségek, színek, számok, testrészek
- Képek: emoji alapú, jól felismerhető
- Forrás: `cuvinte.md`

---

## v2 Specifikáció (aktuálisan kész – 2026-03-29)

### Változás v1-hez képest
- Gombnyomásra (bármelyik: Tudja / Félig / Nem tudja) **nagyban megjelenik a román szó**
- Azonnal **felolvassa hangosan románul** (Web Speech API, `ro-RO` nyelv)
- A szó megjelenik egy animált overlay-en, majd a kártya továbblép
- Diszlexia-barát: nagy, kontrasztos betűk a feliratnál

## v3 Specifikáció (aktuálisan kész – 2026-03-29)

### Változás v2-höz képest
- A böngésző beépített TTS-e helyett **Google Translate TTS** adja a hangot (valódi román kiejtés)
- Tartalék: **ResponsiveVoice** (felhő alapú román hang) ha a Google Translate blokkolva van
- Végső tartalék: Web Speech API (mint v2-ben)
- A felhasználó látja melyik hang éppen aktív (kis badge)

## v4 Specifikáció (aktuálisan kész – 2026-03-29)

### Változás v3-hoz képest
- Minden emoji/kép felülvizsgálva: **a képnek magát a szót/cselekvést kell mutatnia**, nem egy kapcsolódó eszközt
- Pl.: `desenează` = rajzoló ember (🧑‍🎨), nem ceruza (✏️)
- Pl.: `învață` = könyvet olvasó gyerek (🧒📖), nem könyv (📚)
- Ahol szükséges, több emoji kombinációja adja a helyes képet
- Az összes 35 szó képe egyenként ellenőrizve és indokolt

### Emoji döntési szempontok
1. A kép önmagában érthetően mutatja a szó jelentését
2. Gyerek (5-8 éves) számára egyértelműen felismerhető
3. Diszlexia-barát: egyszerű, nem zsúfolt vizuális tartalom

## v5 Specifikáció (aktuálisan kész – 2026-03-29)

### Változás v4-hez képest
- Emoji helyett **valódi fotók** (Wikimedia Commons, CC-licencelt képek)
- Minden szóhoz az internetről keresett, tárgyhoz/cselekvéshez illő kép
- Kártya teljes felülete kép (`object-fit: cover`)
- Ha a kép nem töltődik be: automatikus emoji fallback
- Forrás: Wikipedia REST API thumbnails (upload.wikimedia.org)

### Kép forrásai (kategóriánként)
- Gyümölcsök / Zöldségek: Wikipedia botanical fotók
- Napszakok: napfelkelte, naplemente, ételek, alvás
- Tevékenységek: sport, tánc, énekkar, játszótér, festő, úszás, stb.

## Tervezett következő verziók

### v6 – Saját fényképes kártyák
- [ ] A papír kártyák saját fotóinak integrálása
- [ ] Admin felület a szavak és képek hozzáadásához
- [ ] OpenDyslexic betűtípus opció

### v3 – Fényképes kártyák
- [ ] Saját fényképek integrálása (papír kártyák fotói)
- [ ] Kép + emoji párosítás
- [ ] Egyszerű admin felület a szavak hozzáadásához

### v4 – Gamification
- [ ] Pontrendszer (csillagok, jutalmak)
- [ ] Több "barlang" = több szókategória
- [ ] Rekord követés (legjobb idő, legtöbb szó)
- [ ] Nap végi összefoglaló a szülőnek

### v5 – Kategória választó
- [ ] Szülő kiválaszthatja melyik kategóriát gyakorolja
- [ ] Nehézségi szint: Könnyű / Közepes / Nehéz

### v6 – Multiplayer / Verseny mód
- [ ] Két gyerek versenyezhet egymással
- [ ] Szülő vs. gyerek mód

---

## Diszlexia-barát tervezési elvek

1. **Nagy, kontrasztos betűk** – minimum 24px, sötét alapon világos VAGY világos alapon sötét
2. **Képközpontú** – mindig kép az elsődleges, szöveg másodlagos
3. **Egyszerű layout** – semmi zsúfolt, sok fehér tér
4. **Rövid szövegek** – szavanként, nem mondatokban
5. **Animáció = visszajelzés** – minden interakcióra látható, pozitív visszajelzés
6. **Hang** – a szó felolvasása segít a betű-hang kapcsolat kialakításában
7. **Nincs időnyomás** – a gyerek akkor megy tovább, amikor készen van

---

## Fájlstruktúra

```
Work/
  család/
    Tanulás/
      Román/
        cuvinte.md       ← szószedeta (bővíthető)
        regule.md        ← ez a fájl (játékszabályok + fejlesztési terv)
        jatek_v1.html    ← az aktuális játék
```

---

> **Fejlesztési mottó:** Lépésről lépésre, a kislányom tempójában.
