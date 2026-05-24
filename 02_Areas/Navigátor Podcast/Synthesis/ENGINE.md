---
version: 0.2
date: 2026-04-06
type: engine
purpose: "Reusable guide for any Claude session to produce deep episode syntheses"
id: be97ac3d-ddb4-45d0-9c1d-a0378f265d1d
index_schema_version: 1
---

# Navigátor Podcast — Epizód-elemzés Engine

> **Mi ez?** Egy motorja a csatorna auditnak. Ha új session-ben dolgozol, olvasd el ezt ELŐSZÖR.
> Ez a dokumentum elmagyarázza, hogyan kell egy epizódot mélyen elemezni, milyen eszközökkel,
> milyen sorrendben, és milyen minőségben.

---

## 0. Kontextus betöltés (minden session elején)

Mielőtt bármit csinálnál, olvasd be ezeket:

```
1. CLAUDE.md                          -> csatorna identitás, értékek, formátumok
2. Synthesis/ENGINE.md                -> ez a fájl (hogyan dolgozzunk)
3. Synthesis/szintézis.md             -> eddigi általános megfigyelések
4. Synthesis/plan.md                  -> tracking mátrix (melyik epizód kész)
5. Synthesis/Podcast/EP27 - Tamás Barna atya.md  -> KÉSZ (17,978 bytes, RERUN Gold Standard)
6. Synthesis/Podcast/EP14 - Bencze Edit.md  -> KÉSZ (19,763 bytes, #1 videó, RERUN Gold Standard)
7. Synthesis/Podcast/EP36 - Both Richárd.md  -> KÉSZ (18,170 bytes, RERUN Gold Standard)
8. Synthesis/Podcast/EP37 - Kiégés.md  -> KÉSZ (15,049 bytes, #3 videó)
9. Synthesis/Podcast/EP29 - Dr. Lőrinczi Kincső.md  -> KÉSZ (16,636 bytes, #2 videó)
10. Synthesis/Podcast/EP28 - Bencze Edit.md  -> KÉSZ (17,123 bytes, RERUN Gold Standard)
11. Synthesis/Podcast/EP17 - ChatGPT.md  -> KÉSZ (20,791 bytes, #3 videó)
12. Synthesis/Podcast/EP31 - Simon Károly & Kolumbán Sándor.md  -> KÉSZ (24,280 bytes, AI-klaszter #3)
13. Synthesis/Podcast/EP06 - Szakács-Paál István.md  -> KÉSZ (24,056 bytes, Governance Gold Standard)
14. Synthesis/Podcast/EP18 - Lázár Csilla & Szilágyi-Balázs Brigitta.md  -> KÉSZ (23,143 bytes, AI/Digitális klaszter #4)
15. Synthesis/Podcast/EP12 - Pálfi Kinga.md  -> KÉSZ (25,699 bytes, Identitás-Önazonosság klaszter: EP07→EP12→EP14)
```

**Állapot felmérés:** Nézd meg melyik epizódok vannak kész (>4000 bytes = deep, <3000 = placeholder).

---

## 1. Epizód kiválasztása

### Prioritási sorrend
1. **Legtöbb megtekintéssel rendelkező placeholder-ök** — ezekből tanulunk a legtöbbet
2. **Tematikus csoportok** — ha egyszerre csinálsz többet, egy témakörből (pl. pszichológia epizódok egymás után) = hatékonyabb cross-referencia
3. **Felhasználó kérése** — ha Szabolcs megmond egy konkrét epizódot

### Aktuális állapot (2026-04-06)

| Státusz | Darab | Megjegyzés |
|---------|-------|------------|
| Benchmark kész | 0 | (EP27 upgraded to Gold Standard) |
| Deep kész (Podcast) | 18 | EP06, EP07, EP12, EP14, EP17, EP18, EP19, EP21, EP27, EP28, EP29, EP30, EP31, EP35, EP36, EP37, EP41 |
| Deep kész (Sorozat) | 16 | 7Sz EP1-EP8, KAW 1-5, Közösség EP01-EP03 |
| Placeholder / Nincs | ~18 | EP01-EP05, EP08-EP13, EP15-EP16, EP20-EP26, EP32-EP34, EP38-EP40, EP42-EP46 |

### Mappastruktúra (2026-04-06)

```
Synthesis/
├── ENGINE.md              <- ez a fájl
├── szintézis.md           <- cross-episode megfigyelések
├── plan.md                <- tracking mátrix
├── Csatorna Audit Terv v0.3.md
├── Podcast/               <- kész fő epizód szintézisek (36 db)
│   ├── EP27 - Tamás Barna atya.md  (17,978 B, RERUN Gold Standard)
│   └── EP28 - Bencze Edit.md  (16,915 B)
│   └── EP17 - ChatGPT.md  (20,791 B)
│   └── ... (36 epizód összesen)
└── Series/                <- sorozat szintézisek (16 db, KÉSZ)
    ├── 7Szokas EP1-EP8    (8 fájl, ~50,372 B)
    ├── KAW 1-5            (5 fájl, ~30,425 B)
    └── Kozosseg EP01-EP03 (3 fájl, ~17,127 B)
```

---

## 2. Checklist — egy epizód teljes elemzése

### FÁZIS A: SRT olvasás (~15-20 perc)

```
A.1  [ ] SRT fájl megkeresése
       Hely: Downloads--Navigátor/srt/
       FIGYELEM: NFD/NFC encoding — használj Python os.listdir()-t
       Keresés: grep a fájlnévben az epizód számra (EP XX) vagy vendég nevére

A.2  [ ] SRT feldolgozás szöveggé
       Python script:
         - re.split(r'\n\n+', content.strip()) -> blokkok
         - Időbélyeg: r'(\d{2}:\d{2}:\d{2})'
         - Szöveges sorok: filter(nem szám, nem '-->')
         - 5 percenként időbélyeg marker beillesztése
       Output: /sessions/.../EPXX_full_transcript.txt

A.3  [ ] Teljes átirat elolvasása
       NE ugorj át részeket! Olvasd el az EGÉSZET.
       Közben jegyzetelj fejben:
         - Főbb témablokkok + időkódok
         - Legütősebb idézetek / gondolatok
         - Szabolcs saját hozzájárulásai (ez FONTOS — nem csak kérdez)
         - Potenciális cold open / hook anyagok
         - Kontroverzális vagy meglepő kijelentések
```

### FÁZIS B: YouTube Studio analytics (~5-10 perc)

```
B.1  [ ] YouTube Studio megnyitása Chrome MCP-vel
       Tab: studio.youtube.com/channel/.../videos/upload
       Keresés: a videó címére vagy EP számra a felső search bar-ban

B.2  [ ] Overview tab
       Rögzítendő adatok:
         - Views (összesen)
         - Watch time (hours)
         - Subscribers gained
         - Average view duration
         - Average percentage viewed
         - Retention görbe leírása (hol esik, van-e spike)
         - "X% still watching at 0:30" — ez KULCS adat

B.3  [ ] Reach tab
       Rögzítendő:
         - Impressions
         - CTR (click-through rate)
         - Views from impressions
         - Traffic sources breakdown (External, Browse, Suggested, Search, Direct)
         - External sites részletezés (Facebook, Google, WhatsApp stb.)
         - YouTube search terms (milyen kulcsszavakkal találják)
         - Bell notification stats

B.4  [ ] Engagement tab
       - Watch time + trend
       - Likes vs dislikes %
       - Hype points

B.5  [ ] Audience tab
       - Device breakdown (mobile, computer, TV, tablet)
       - Age and gender breakdown
       - Top geographies
       - Subscriber vs non-subscriber watch time
       - Top subtitle languages

B.6  [ ] Comments tab
       - Szűrő eltávolítása ("Unresponded" filter -> töröld az X-szel)
       - MINDEN komment elolvasása és jegyzetelése
       - Van-e válasz a hosztól? (engagement quality)
```

### FÁZIS C: Szintézis megírása (~15-20 perc)

```
C.1  [ ] YAML header kitöltése
       Mezők: version, date, type, episode, guest, topic, duration, published, views, status

C.2  [ ] Alapadatok tábla
       Vendég, megjelenés, hossz, megtekintések, watch time, feliratkozók, likes, kommentek, téma

C.3  [ ] YouTube Studio Analytics szekció
       Alszekciók: Elérés, Forgalmi források, Megtartás, Közönség, Kommentek
       Minden adat táblázatban, értékeléssel

C.4  [ ] Tartalmi összefoglaló
       - A beszélgetés íve (2-3 mondat overview)
       - Főbb témablokkok (időkódokkal, 4-8 blokk)
       - Minden blokkban: téma, kulcspontok, idézetek, Szabolcs hozzájárulása

C.5  [ ] Teljesítmény elemzés
       - "Miért nem lett nézettebb?" VAGY "Miért lett kiemelkedő?"
       - Számozott okok, adatokkal alátámasztva
       - "Ami mégis működik" szekció (pozitív)

C.6  [ ] YouTube metadata minőség
       - Cím elemzés (formátum-megfelelés, hook erőssége)
       - Thumbnail értékelés
       - Javaslatok (alternatív cím, thumbnail szöveg)

C.7  [ ] Tanulságok a csatorna számára
       - Amit tanulhatunk (3-5 pont)
       - Fejlesztési lehetőségek (3-5 pont, konkrét)
       - Shorts potenciál (2-3 konkrét ötlet)
```

### FÁZIS D: Szintézis.md frissítése

```
D.1  [ ] Nyisd meg a szintézis.md-t
D.2  [ ] Ha az új epizód bármilyen ÁLTALÁNOS mintát erősít vagy cáfol -> jegyezd be
       Példák:
         - Új közönség-adat ami módosítja a demográfiai képet
         - Téma-nézettség korreláció megerősítése
         - Új hook/intro minta felfedezése
         - Traffic source minta (melyik témánál honnan jön a forgalom)
D.3  [ ] YAML header episodes_analyzed listájához add hozzá az új epizódot
D.4  [ ] Nézettségi rangsor frissítése ha szükséges
```

### FÁZIS E: Plan.md frissítése

```
E.1  [ ] Az epizód sorát állítsd KÉSZ-re a tracking mátrixban
E.2  [ ] Dátum frissítése
```

---

## 3. Minőségi kritériumok

### Minimum követelmények (nem placeholder)

| Kritérium | Elvárás |
|-----------|---------|
| Fájlméret | >4000 bytes (tipikusan 7000-16000) |
| YAML header | Minden mező kitöltve |
| YT Studio adatok | Valós adatok, nem becsült |
| Tartalmi összefoglaló | Időkódos témablokkok, nem generic leírás |
| Szabolcs gondolatai | Külön kiemelve, ha voltak |
| Miért lett/nem lett nézettebb | Adatokon alapuló elemzés |
| Konkrét javaslatok | Alternatív cím, thumbnail, Shorts ötletek |

### Placeholder felismerése (ami NEM elfogadható)

Ezek a jellemzők jelzik, hogy az epizód NINCS rendesen feldolgozva:
- Fájlméret <3000 bytes
- Generic kifejezések: "Kulcsfogalmak tisztázása", "Elméleti keretrendszer", "Gyakorlati alkalmazás"
- Nincs konkrét idézet a beszélgetésből
- Nincs YouTube Studio adat (views, CTR, retention)
- A témablokkok általánosak, nem specifikusak az epizódra

---

## 4. Eszközök és technikák

### SRT feldolgozás (Python)

```python
import re, os

def parse_srt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.split(r'\n\n+', content.strip())
    result = []
    current_time = None

    for block in blocks:
        lines = block.strip().split('\n')
        for line in lines:
            ts_match = re.search(r'(\d{2}):(\d{2}):(\d{2})', line)
            if ts_match and '-->' in line:
                h = int(ts_match.group(1))
                m = int(ts_match.group(2))
                s = int(ts_match.group(3))
                current_time = h * 3600 + m * 60 + s
            elif not re.match(r'^\d+$', line.strip()) and '-->' not in line and line.strip():
                result.append((current_time, line.strip()))

    # 5 perces blokkokba rendezés
    output = []
    last_marker = -1
    for time_sec, text in result:
        if time_sec is not None:
            marker = (time_sec // 300) * 300
            if marker > last_marker:
                h = marker // 3600
                m = (marker % 3600) // 60
                s = marker % 60
                output.append(f"\n\n=== [{h:02d}:{m:02d}:{s:02d}] ===\n")
                last_marker = marker
        output.append(f" {text}")

    return ''.join(output)
```

### NFD/NFC könyvtár kezelés

```python
import os
base = '/sessions/awesome-youthful-archimedes/mnt'

def find_nfd_dir(name_fragment):
    candidates = []
    for d in os.listdir(base):
        if name_fragment in d:
            full = os.path.join(base, d)
            if os.path.isdir(full):
                candidates.append((full, len(os.listdir(full))))
    if candidates:
        return max(candidates, key=lambda x: x[1])[0]
    return None

# Használat:
synthesis_dir = os.path.join(find_nfd_dir('Navig'), 'Synthesis')
srt_dir = os.path.join(find_nfd_dir('Download'), 'srt')
```

**FONTOS:** A session working directory (/sessions/...) változik session-ként!
Az `mnt/` alatti könyvtárak maradnak, de a `base` path mindig más lesz.
A session elején mindig nézd meg: `ls /sessions/*/mnt/`

### YouTube Studio navigáció (Chrome MCP)

```
1. tabs_context_mcp (createIfEmpty: true)
2. navigate -> studio.youtube.com
3. Keresés: felső search bar-ba a videó címe/EP száma
4. A találatra hover -> analytics ikon kattintás
5. Tabonként screenshot + adatok kinyerése:
   Overview -> Reach -> Engagement -> Audience -> Comments (bal oldali menü)
```

### SRT fájl megtalálása

```python
srt_dir = find_nfd_dir('Download') + '/srt'
ep_num = '27'  # keresett epizód

# Először EP szám alapján
for f in os.listdir(srt_dir):
    if f'EP {ep_num}' in f or f'EP{ep_num}' in f:
        print(os.path.join(srt_dir, f))
        break

# Ha nincs EP szám a fájlnévben, vendég neve alapján
for f in os.listdir(srt_dir):
    if 'Barna' in f or 'barna' in f.lower():
        print(os.path.join(srt_dir, f))
```

---

## 5. Batch feldolgozás stratégia

### NE csinálj párhuzamos agent-eket a szintézisekhez!

Az előző kísérlet bebizonyította: a párhuzamos agent-ek placeholder-eket gyártanak.
Egy session = egy epizód, MÉLYEN. Ha gyorsítani kell:

### Ajánlott sorrend (egy session-ben max 2-3 epizód)

1. **Először:** SRT-ket feldolgozni szövegfájlokká (ez batch-elhető, mert mechanikus)
2. **Utána:** Egyenként olvasni és szintetizálni (NEM batch-elhető)
3. **Közben:** YouTube Studio adatokat epizódonként kigyűjteni

### Hatékonysági tipp

Ha egy session-ben több epizódot csinálsz:
- A YouTube Studio-t ne zárd be — tab-ban tartsd nyitva
- A szintézis.md-t a session végén frissítsd (ne epizódonként)
- Az SRT parse-olást egyszer lefuttathatod batch-ben az összes hiányzóra

---

## 6. Szintézis sablon

Az alábbi a minimális sablon. A valódi szintézis MINDIG ennél bővebb, mert a tartalom epizódonként más.

```markdown
---
version: 0.2
date: YYYY-MM-DD
type: episode-synthesis
episode: EPXX
guest: "Vendég Neve"
topic: "Rövid téma leírás"
duration: "~X:XX:XX"
published: YYYY-MM-DD
views: XXXX
status: complete
---

# EPXX — Vendég Neve: Téma

## Alapadatok
(tábla: vendég, megjelenés, hossz, megtekintések, watch time, stb.)

## YouTube Studio Analytics
### Elérés (Reach)
### Forgalmi források
### Megtartás (Retention)
### Közönség (Audience)
### Kommentek

## Tartalmi összefoglaló
### A beszélgetés íve
### Főbb témablokkok
(időkódos, részletes, idézetekkel)

## Teljesítmény elemzés
### Miért lett / nem lett nézettebb?
### Ami működik

## YouTube metadata minőség
### Cím elemzés
### Thumbnail
### Javaslatok

## Tanulságok a csatorna számára
### Amit tanulhatunk
### Fejlesztési lehetőségek
```

---

## 7. Referencia minőségi szintek

| Szint | Bytes | Jellemzők | Példa |
|-------|-------|-----------|-------|
| Placeholder | <3000 | Generic szöveg, nincs YT adat | EP01-EP13 (mind) |
| Félkész | 3000-5000 | Van tartalom, de hiányos analytics | EP36 |
| Deep | 5000-8000 | Teljes tartalom + analytics | (következő cél) |
| Benchmark | >10000 | Mindent tartalmaz + mély elemzés | EP17 (20,791 bytes) |

**Cél:** Minden epizód legalább Deep szintű legyen. A benchmark nem követelmény, de komplex epizódoknál természetesen hosszabb lesz a szintézis.

---

## 8. Gyakori hibák (amiket kerülni kell)

1. **NE használj párhuzamos agent-eket szintézishez** — placeholder-eket gyártanak
2. **NE becsüld a nézettséget** — MINDIG YouTube Studio-ból vedd (a korábbi adatok TÉVESEK voltak)
3. **NE hagyd ki Szabolcs gondolatait** — a podcast értéke nem csak a vendégben van
4. **NE írj generic témablokkokat** — "Kulcsfogalmak tisztázása" nem elfogadható
5. **NE felejtsd el a szintézis.md frissítését** — ez a cross-episode intelligence
6. **NE próbálj egyszerre 10 epizódot csinálni** — 2-3 max egy session-ben, MÉLYEN
7. **NE hagyj megválaszolatlan kommentet** — jelezd ha van, Szabolcs válaszolhat

---

## 9. Multi-AI Workflow (ha elérhető)

A Think Agent Orchestrator v0.5 szerint:

| Szerepkör | Ki | Feladata |
|-----------|-----|---------|
| Stratéga | ChatGPT | Átfogó csatornastratégia, tartalmi irányok, versenytárs-elemzés |
| Kutató | Perplexity | Téma-háttér, trendek, kulcsszó-kutatás, versenytárs benchmark |
| Végrehajtó | Claude | SRT olvasás, YT Studio analytics, szintézis írás, fájlkezelés |
| Döntéshozó | Szabolcs | Jóváhagyás, prioritizálás, stratégiai döntések |

**ChatGPT thread:** https://chatgpt.com/g/g-p-675d8f1c97b48191b81ff4164cf7d789-navigator-podcast/c/69d32854-a780-8396-afd4-6787cd2c917b
**Perplexity thread:** https://www.perplexity.ai/search/az-asszisztenemmel-futtaok-egy-_hvbVRtDQEKMrXqJ9lh5Fg

Ha a session-ben van Chrome MCP, érdemes a ChatGPT/Perplexity thread-eket is megnyitni és kontextust kérni tőlük.

---

## 10. Navigátor Plugin skill-ök integrálása

A szintézis elkészítése után (vagy közben) a Navigátor Podcast plugin skill-jeit is érdemes lefuttatni az SRT-n.
Ezek a `/commands` a Cowork felületen elérhetők:

| Skill | Mit csinál | Mikor használd |
|-------|-----------|----------------|
| `/hook` | Cold Open / Hook javaslatok | Szintézis C.4 fázisban — hasonlítsd össze a jelenlegi intro-val |
| `/cim` | YouTube cím javaslatok | Szintézis C.6 fázisban — összevetheted a jelenlegi címmel |
| `/thumbnail` | Thumbnail szöveg javaslatok | Szintézis C.6 fázisban |
| `/leiras` | YouTube leírás + hashtagek | Ha a jelenlegi leírás hiányos |
| `/idokod` | Időkódok (timestamps) | Ha a videóhoz nincs időkód |
| `/navigator-metadata` | Mindent egyben | Ha a teljes metaadatot újra akarod generálni |

### Használati javaslat

A szintézis FÁZIS C.6 (YouTube metadata minőség) részeként:
1. Futtasd le a `/cim` és `/thumbnail` skill-t az SRT-re
2. Hasonlítsd össze az AI javaslatokat a jelenlegi címmel/thumbnaillal
3. Ha az AI javaslat jobb, tedd be a szintézisbe mint "Alternatív cím javaslat"
4. Ez kétirányú: a szintézis tartalmi ismerete segít jobb javaslatokat adni, mint ha vakon futtatnád

**FONTOS:** A skill-ök a navigator-context skill-t használják háttérként. Ha a session elején betöltöd a kontextust (0. pont), a skill-ök jobb eredményt adnak.

---

## 11. SRT fájlnév → EP szám mapping

### Korai epizódok (EP01-EP13) — nincs EP szám a fájlnévben!

A podcast első epizódjainál a fájlnév sorszámot tartalmaz (1., 2., 3...) de NEM EP számot.
Az offset: **EP szám = SRT sorszám + 1** (mert EP01 a Bevezető, EP02 az első vendéges).

| EP | SRT fájlnév (prefix) | Vendég |
|----|---------------------|--------|
| EP01 | `20240526 - Navigátor Podcast` | Bevezető (nincs vendég) |
| EP02 | `20240604 - 1. Vinczellér Árpád` | Vinczellér Árpád |
| EP03 | `20240618 - 2. Lukácsi Kata` | Lukácsi Kata |
| EP04 | `20240702 - 3. Nagy Lajos` | Nagy Lajos |
| EP05 | `20240716 - 4. Kirmájer Erika, Szabó Réka` | Kirmájer Erika, Szabó Réka |
| EP06 | `20240730 - 5. Szakács-Paál István` | Szakács-Paál István |
| EP07 | `20240813 - 6. Bencze Edit` | Bencze Edit |
| EP08 | `20240827 - 7. Széles Ferenc` | Széles Ferenc |
| EP09 | `20240910 - 8. Dr. Kurtus Aranka` | Dr. Kurtus Aranka |
| EP10 | `20240926 - 9. Dr. Simon Károly` | Dr. Simon Károly |
| EP11 | `20241008 - 10. Elekes István` | Elekes István |
| EP12 | `20241022 - 11. Pálfi Kinga` | Pálfi Kinga |
| EP13 | `20241105 - 12. Bándi Domokos` | Bándi Domokos |

**Megjegyzés:** Az SRT-k közt van egy `13. Józsa Levente` (2024.11.19) is, ami nem szerepel a Synthesis mappában — valószínű kimaradt az EP számozásból. Ellenőrizd YouTube Studio-ban!

### EP14-tól — EP szám a fájlnévben

EP14-től a fájlnévben benne van az EP szám, pl.:
`20241203 - A nárcizmus rejtett arcai ｜ Bencze Edit ｜ EP14.hu.srt`

Keresés: `f'EP {ep_num}' in filename or f'EP{ep_num}' in filename`

### Sorozatok (NEM epizód-szintézisek)

| Sorozat | SRT fájlnév minta | Synthesis mappa neve |
|---------|-------------------|---------------------|
| 7 Szokás (Covey) | `7 Szokás EP1`, `7 Szokás EP2`... | `7Szokás EP1 - Bevezető.md` stb. |
| KAW (Betenbough) | `fejezet – Bevezetés a Királyságba` stb. | `KAW 1 - Spirituális alapok.md` stb. |
| Közösség | `Navigátor Közösség ｜ EP 01` stb. | `Közösség EP01 - Növekedés.md` stb. |

**FIGYELEM:** A sorozat EP számok ÜTKÖZNEK a főepizód EP számokkal! Pl. a `7 Szokás EP1` és a `Közösség EP 01` NEM ugyanaz mint a fő `EP01`. Mindig nézd a teljes fájlnevet!

### Keresési Python snippet

```python
def find_srt(ep_num, srt_dir):
    """EP szám alapján megkeresi az SRT fájlt."""
    ep_num = int(ep_num)

    for f in os.listdir(srt_dir):
        # Először próbáljuk EP számmal
        if f'EP {ep_num}' in f or f'EP{ep_num}' in f:
            # De ne sorozatot találjunk!
            if '7 Szokás' not in f and 'Közösség' not in f:
                return os.path.join(srt_dir, f)

    # Korai epizódok: SRT sorszám = EP szám - 1
    if ep_num <= 13:
        srt_num = ep_num - 1
        prefix = f'{srt_num}.'
        for f in os.listdir(srt_dir):
            if f'. ' in f:
                parts = f.split(' - ', 1)
                if len(parts) > 1 and parts[1].startswith(f'{srt_num}.'):
                    return os.path.join(srt_dir, f)

    return None  # Nem találtuk - kézi keresés kell
```

---

## 12. Sorozat-epizódok kezelése

A Navigátor Podcast három sorozatot tartalmaz, amelyek más logikával működnek mint a vendéges epizódok:

### 7 Szokás (Stephen Covey könyv feldolgozás)

- **8 epizód** (EP1-EP8), Szabolcs szólója (nincs vendég)
- A szintézis sablon egyszerűsödik: nincs vendég, nincs "vendég hozzájárulása"
- **Helyette:** Szabolcs értelmezése, személyes példái, hogyan alkalmazza
- **YouTube metadata:** más logika — a könyv a hook, nem a vendég
- **Összehasonlítási szempont:** hogyan teljesítenek a szóló epizódok a vendégesekhez képest?

### KAW (Kingdom At Work / Betenbough Módszer)

- **5 fejezet**, könyvfeldolgozás, valószínűleg szóló
- Spirituális vezetés, munkateológia — niche téma
- A szintézis sablonban a "Tanulságok" szekció az eredeti könyv vs. Szabolcs értelmezése legyen

### Közösség sorozat

- **3 epizód** (EP01-EP03), valószínűleg szóló vagy belső közösségi
- Növekedés, 80/20, Bizalom — üzleti/szervezeti témák
- Ezek a Navigátor identitás „vállalkozói" oldalát képviselik

### Sablon-módosítások sorozatoknál

```
Szóló (nincs vendég):
  - Alapadatok: "Vendég" sor helyett "Formátum: szóló / könyvfeldolgozás"
  - Tartalmi összefoglaló: Szabolcs gondolatmenete, nem interjú-dinamika
  - Tanulságok: eredeti forrás (könyv) vs. Szabolcs értelmezése

Sorozat-elem:
  - Hivatkozás a sorozat többi elemére
  - Hol áll a sorozat ívében? (bevezető, csúcspont, zárás)
  - A sorozat összessége hogyan teljesít?
```

---

## 13. Session-folytonosság protokoll

### Probléma
Egy mély szintézis ~15-20 perc és sok token. Egy session-ben 2-3 epizódnál többre nem futja. A következő session-nek tudnia kell hol tartottunk.

### Átadási módszer

**A session végén MINDIG frissítsd:**

1. **plan.md** — melyik epizód kész, melyik nincs
2. **szintézis.md** — YAML header `episodes_analyzed` lista
3. **ENGINE.md 1. szekció** — "Aktuális állapot" tábla frissítése

**Ha a session közben fogy el a kontextus:**

A Cowork automatikusan generál egy session summary-t. De ezen felül a szintézis.md-be írd be:

```markdown
## Session log
- 2026-04-06: EP27 benchmark kész, ENGINE.md létrehozva
- 2026-04-06: EP14 RERUN Gold Standard (19,763 B), EP27 RERUN Gold Standard (17,978 B), EP36 RERUN Gold Standard (18,170 B), EP28 RERUN Gold Standard (17,123 B)
- [DÁTUM]: [EPXX, EPYY kész, EPZZ félbe maradt — B.3 fázisnál tartottunk]
```

### Új session indítása

```
1. Olvasd be a 0. szekció fájljait
2. Nézd meg a plan.md-t — mi van kész, mi nincs
3. Nézd meg a szintézis.md session log-ját — volt-e félbeszakadt munka
4. Ha volt félbe maradt: fejezd be azt először
5. Ha nem: válaszd a következő prioritásos epizódot (1. szekció)
```

---

## 14. YouTube videó ID-k

Ha egyszer kigyűjtjük, a következő session-nek nem kell keresnie a Studio-ban.

### Ismert videó ID-k

| EP | YouTube ID | Cím (rövidítve) |
|----|-----------|-----------------|
| EP27 | `RY14eU8NPU0` | Fókuszpont, Ferenc pápa... |
| EP19 | `DeGjg1EM7Qw` | A házasság szentsége, szeretet mint szolgálat |
| EP21 | `ymSgaBRwN4k` | Indul az Audit? Szakács-Paál István |
| EP30 | `S8JeFX3V07k` | Jövő Iskolája: AI, tanárok, diákok |
| EP31 | `h2i9WNsdWrc` | Az AI csak 80%-ra elég? Simon Károly & Kolumbán S. |
| EP06 | `1hbim8vN9gQ` | Milyen legyen a polgármester? Szakács-Paál István |
| EP12 | `0fAIJ99yur0` | A stílus nem pénz kérdése, Pálfi Kinga |
| EP13 | `CEBAnmXFlr8` | A Podcast az Új Mainstream, Józsa Levente |
| EP32 | `SlSRu1yE6ws` | Nem vagyunk összeszerelő üzem, Dr. Palkovics László |
| EP18 | `JhquTzM8dfU` | Digitális intelligencia: Az új kulcskompetencia |
| EP15 | `KYR2-VI3U3M` | Mit hoz a MI a mindennapjainkba, Szabó W. Péter |
| EP16 | `CR54gv3Ax8s` | Az erő ami Izraelből árad, Erőss Gáspár |
| EP33 | `s8C6QyRpJhA` | A langyos víz a legnagyobb veszély, Dr. Charaf Hassan |
| EP34 | `vS0SK2x1NQI` | A kudarc a legerosebb tanitomester, Suket Csaba |
| EP02 | `q7Q5aUY0w50` | A kávé összeköt, Vinczellér Árpád |
| EP03 | `1FmIRZ9kkVg` | A Hamm története, Nagy Lajos |
| EP05 | `J9175griS7c` | Képezzük a jövő vezetőit, Kirmájer Erika & Szabó Réka |
| EP08 | `j_GotIYqXKs` | Az élet tragédiájának közelében, Dr. Kurtus Aranka |
| EP09 | `Bzm2Ddxeni4` | Készüljünk az információs korszakra, Dr. Simon Károly |
| EP11 | `wVLydj4eUFg` | Hit és vezetés, Elekes István |
| EP20 | `34K4pwugxLc` | Játékból Szenvedély, Gábor Attila |
| EP22 | `yc50GxmlMNg` | Hangszerjavítás vagy művészet?, Tódor Botond |
| EP23 | `XrvpAIs4I3U` | A szavakon túl, Hátszegi Zsolt |
| EP24 | `X3Rhtpal5tA` | A valóság színpadra állítva, Faragó Zénó & Fodor Alain Leonard |
| EP25 | `-CBBMeGz6bI` | Versben élni, Albert Orsolya |
| EP26 | `yhUxLJO5OWY` | Életfonal — Daganatos betegség, Balázs Anna & Zoltáni Kinga |
| EP38 | `o4xWWp5qZDM` | Örökbefogadás — Ez a te családod, Gál Ildikó |
| EP35 | `X1EF52Eez4o` | Már nem elég olcsóbbnak lenni, Lang Máté |

**TODO:** A többi epizód ID-ját ki kell gyűjteni a YouTube Studio Content oldaláról.
Módszer: Content tab -> hover egy videóra -> a "watch on YouTube" ikon URL-jéből kiolvasható a videó ID.
Vagy: Advanced mode -> Export -> CSV-ben benne van minden ID.

### Gyors hozzáférés ha van ID

```
Analytics: studio.youtube.com/video/{ID}/analytics/tab-overview/period-default
Comments: studio.youtube.com/video/{ID}/comments
Details:  studio.youtube.com/video/{ID}/edit
```

---

*Utolsó frissítés: 2026-04-06 v3.4 | EP34 Gold Standard kész (Vallalkozas-Kudarc-Innovacio klaszter: EP34->EP35->EP31->EP32->EP11), 36 deep. Elozo: v3.3 EP25 Gold Standard kész, 35 deep*
