---
title: "F1: Tanítsd be az AI-t a strukturált rendszeredre"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "Az F1 modul bemutatja, hogyan írjuk le a Regio meglévő, strukturált projekt-felépítését egymásba ágyazott CLAUDE.md szabálykönyvekben, hogy az AI (Cowork) értse és kövesse a belső sztenderdet. A meglévő rendet nem bolygatjuk, párhuzamosan bővítjük. Ez a workshop első tapasztalata és a közös setup: a CLAUDE.md innen él tovább F6-ig."
id: 3c7a1e58-9d24-4b60-8f13-6a2e0c9d5b41
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, claude-md, struktura]
---
# F1: Tanítsd be az AI-t a strukturált rendszeredre
**Időkeret:** 25 perc · **Fázis a workshopban:** 1/6 (a workshop első tapasztalata és közös setup)

## Narratív összefoglaló

**F1 = az AI megérti a rendszeredet. F2 = az AI megjegyzi a feladatokat. F3-F6 = az AI dolgozik benne.**

Csütörtök reggel. A Napsugár projekt fut, a gépeden ott a Regio strukturált rendszere: `Napsugar_projekt/`, benne a teljes projekt-dosszié (Cerere de finantare, Editabil, Dosare de achizitii, Monitorizare). Ez a rend erősség: bárki fél óra alatt átveszi. De az AI még nem ismeri.

Az eredeti Haladó itt káoszt rendezett. Nálatok fordított a helyzet: **nem rendet rakunk (az megvan), hanem a meglévő rendet írjuk le az AI-nak** úgy, hogy értse és kövesse. Ez a `CLAUDE.md`: az AI hosszútávú memóriája és szabálykönyve, amit minden új session elején elsőként elolvas.

## A kulcs-belátás

A ChatGPT-ben minden beszélgetés tiszta lap: minden alkalommal újra el kell magyaráznod, kik vagytok, hogy néz ki egy projekt, mi a Verdana 9 szabály. A Cowork-ben a **CLAUDE.md egyszer leírja, és onnantól minden session automatikusan tudja**. Ez a különbség a tranzakció és a folyamat között, és ez a strukturált rendszer igazi ereje: pont azért taníthatóan leírható, mert tudatosan sztenderd.

## Tanulási célok

1. **Cowork alapok**, mi a plugin, hogyan fut a háttérben a lokális fájlrendszeren, hogyan köti össze a OneDrive / SharePoint közös struktúrával.
2. **Mi a markdown fájl**, miért ez az AI anyanyelve, miért jobb, mint egy Word-doksi a szabályokhoz.
3. **CLAUDE.md mint szabálykönyv**, a belső sztenderd (elnevezés, mappa-logika, formátum) átültetése markdownba.
4. **Kalandkönyv-navigáció**, egymásba ágyazott CLAUDE.md-k: gyökér → projekt → almappa, mindegyik plusz kontextust ad.
5. **Párhuzamos, nem-romboló bővítés**, a markdown réteg a meglévő struktúra mellé kerül, azt nem módosítja.

## A feladatok

| # | Feladat | Típus | Idő |
|---|---|---|---|
| **1.1** | A gyökér-CLAUDE.md: írd le a Regio sztenderdjét | 🎤 DEMO + mindenki saját gépén | ~12p |
| **1.2** | Kalandkönyv: projekt-szintű CLAUDE.md a Napsugárra | ⏸ STÁCIÓ (mikro) | ~6p |

A `Napsugar_projekt/`-ben már ott van egy kész CLAUDE.md (gyökér + projekt), hogy legyen megoldókulcs. A feladat során az AI-val **magad állítod elő** ugyanezt a saját sztenderdedből, és összeveted.

## Otthoni bónusz feladatok

| # | Bónusz | Output |
|---|--------|--------|
| 1.3 | `Feladat_1.3_Bonusz_Belso_sztenderd.md` | A valós belső „internet sztendard" → CLAUDE.md |
| 1.4 | `Feladat_1.4_Bonusz_Uj_projekt_scaffold.md` | Új projekt-mappa legyártása a sztenderd szerint |
| 1.5 | `Feladat_1.5_Bonusz_Lektor_szabalyok.md` | Sztenderd-ellenőrző szabálylista (a jövőbeli lektor-agent magja) |

## Delivery design

| Fázis | Ki | Mit | Idő |
|-------|-----|------|-----|
| Bevezetés | Oktató | Cowork megnyitása, a `Napsugar_projekt/` felfedezése, mi a markdown / CLAUDE.md | ~4p |
| **HANDS-ON** | Mindenki (saját gépen) | A gyökér-CLAUDE.md előállítása prompttal + átolvasás | ~10p |
| Mikro-stáció | Mindenki | Projekt-szintű CLAUDE.md a Napsugárra | ~6p |
| Átkötés F2-be | Oktató | „A rendszer megvan. De honnan tudja az AI, mi a mai teendő?" | ~2p |

**Hands-on arány:** ~65%.

## Átmenet F2-be

*„A struktúra megvan, az AI tudja hogy néz ki egy projekt. De a napi munkában nem a mappák a kérdés, hanem: mi a mai teendő? Épp most volt egy belső egyeztetés a Napsugárról, tele feladattal. Ki fogja ezeket nyomon követni?"*

## Asset-ek

- `Napsugar_projekt/CLAUDE.md`, a kész gyökér-szabálykönyv (megoldókulcs).
- `Napsugar_projekt/Projects/THR_Napsugar_Tejuzem/CLAUDE.md`, a kész projekt-szintű szabálykönyv.
- `Feladat_1.1` és `Feladat_1.2`, a fő feladatok, copy-paste prompttal.

**Verzió:** 1.0 (Regio adaptáció)
