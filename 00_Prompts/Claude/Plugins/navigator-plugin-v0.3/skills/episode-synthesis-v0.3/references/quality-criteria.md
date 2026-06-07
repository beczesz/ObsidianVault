---
title: "Szintézis Minőségi Kritériumok és Sablon"
date: 2026-04-21
author: Becze Szabolcs
status: active
description: "Szintézis minőségi szabvány és sablon podcastokat feldolgozó tudásvault számára. Tartalmazza a minőségi szinteket (Placeholder, Deep, Benchmark, Gold Standard), minimum követelményeket, placeholder-azonosítást és kitölthető sablonokat vendég epizódokhoz és sorozat-részekhez YouTube analitikával és tartalmi elemzéssel."
description_source: auto
description_hash: f71953bbcac9a547
id: 1746c9f7-1d4d-479c-9f62-d52c4a94632c
index_schema_version: 1
bdos_index: true
---
# Szintézis Minőségi Kritériumok és Sablon

## Minőségi szintek

| Szint | Bytes | Jellemzők |
|-------|-------|-----------|
| Placeholder | <3000 | Generic szöveg, nincs YT adat — NEM ELFOGADHATÓ |
| Deep | 4000-10000 | Teljes tartalom + analytics — MINIMUM |
| Benchmark | 10000-15000 | Mindent tartalmaz + mély elemzés |
| Gold Standard | >15000 | Teljes cross-referencia, klaszter-elemzés, konkrét javaslatok |

## Minimum követelmények (nem placeholder)

| Kritérium | Elvárás |
|-----------|---------|
| Fájlméret | >4000 bytes |
| YAML header | Minden mező kitöltve |
| YT Studio adatok | Valós adatok, nem becsült |
| Tartalmi összefoglaló | Időkódos témablokkok, nem generic leírás |
| Szabolcs gondolatai | Külön kiemelve, ha voltak |
| Miért lett/nem lett nézettebb | Adatokon alapuló elemzés |
| Konkrét javaslatok | Alternatív cím, thumbnail, Shorts ötletek |

## Placeholder felismerése (NEM elfogadható jelek)

- Fájlméret <3000 bytes
- Generic kifejezések: "Kulcsfogalmak tisztázása", "Elméleti keretrendszer"
- Nincs konkrét idézet a beszélgetésből
- Nincs YouTube Studio adat
- A témablokkok általánosak, nem specifikusak

---

## Szintézis sablon — Vendéges podcast epizód

```markdown
---
version: 0.3
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

| Mező | Érték |
|------|-------|
| Vendég | Név, foglalkozás |
| Megjelenés | YYYY-MM-DD |
| Hossz | ~X:XX:XX |
| Megtekintések | XXXX |
| Watch Time | XXX.X óra |
| Feliratkozók | +/- XX |
| Likes | XX |
| Kommentek | XX |
| Téma | ... |

## YouTube Studio Analytics

### Elérés (Reach)
(Impressions, CTR, traffic sources breakdown)

### Forgalmi források
(External, Browse, Suggested, Search — százalékokkal)

### Megtartás (Retention)
(AVD, AVD%, "X% still watching at 0:30", retention görbe leírása)

### Közönség (Audience)
(Device, age, gender, geography, subscriber vs non-subscriber)

### Kommentek
(Minden komment rövid összefoglalója, van-e válasz a hosztól?)

## Tartalmi összefoglaló

### A beszélgetés íve
(2-3 mondat overall)

### Főbb témablokkok
(4-8 blokk, mindegyikben: időkód, téma, kulcspontok, idézetek, Szabolcs hozzájárulása)

## Teljesítmény elemzés

### Miért lett / nem lett nézettebb?
(Számozott okok, adatokkal)

### Ami működik
(Pozitív aspektusok)

## YouTube metadata minőség

### Cím elemzés
(Formátum-megfelelés, hook erőssége)

### Thumbnail
(Értékelés)

### Javaslatok
(Alternatív cím, thumbnail, leírás javaslat)

## Tanulságok a csatorna számára

### Amit tanulhatunk
(3-5 pont)

### Fejlesztési lehetőségek
(3-5 pont, konkrét)

### Shorts potenciál
(2-3 konkrét ötlet)
```

## Szintézis sablon — Sorozat-epizód (szóló)

A sorozat-epizódoknál (7 Szokás, KAW, Közösség) a sablon egyszerűsödik:
- Nincs vendég → „Formátum: szóló / könyvfeldolgozás"
- Nincs interjú-dinamika → Szabolcs gondolatmenete
- Van sorozat-kontextus → Hivatkozás a sorozat többi elemére
- Van eredeti forrás → Könyv/eredeti vs. Szabolcs értelmezése

```markdown
---
title: "Sorozat EP# – Téma"
series: "Sorozat neve"
episode: #
youtube_id: "..."
duration: "MM:SS"
views: XXX
watch_hours: XX.X
subscribers_gained: +/-X
avd: "M:SS"
avd_percent: "XX.X%"
synthesis_version: "Gold Standard v3.4"
date_created: "YYYY-MM-DD"
---

# Sorozat EP# – Téma

## Epizód-ív
(A rész helye a sorozat ívében, fő mondanivaló)

## Kulcstémák és gondolati blokkok
(3-6 blokk, mindegyik mély elemzéssel)

## Kulcsidézetek
(3-5 releváns idézet)

## Kereszthivatkozások
(Kapcsolódó podcast-epizódok és más sorozat-elemek)

## Analitikai megjegyzések
(AVD%, megtekintés, stratégiai tanulság)
```
