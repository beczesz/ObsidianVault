---
title: Navigátor Podcast — Marketing Engine
date: 2026-05-26
author: Becze Szabolcs
status: active
description: A Navigátor Podcast marketing motor fájlja — brand-hang, célközönség, csatorna-mix, KPI-célok, kadencia és kiadványszabályok. Az összes Navigátor marketing-kampány és publikáció közös kontextus-rétege; Presto draft/prepare módban ezt olvassa brand-tone-ért.
version: 0.1.0
id: e7658561-719e-455a-82fa-d49f7f8c32b4
index_schema_version: 1
bdos_index: true
---

# Navigátor Podcast — Marketing Engine

> **Mentális modell:** ez a fájl a Presto brand-kontextus forrása. Minden publikáció-draftnál a `draft` és `prepare` módok innen olvassák a hang-útmutatót és a közönségprofilt. NE töröld, NE rövidítsd le a brand-tone szekciót — az a legértékesebb rész.

---

## 1. Area azonosítás

| Mező | Érték |
|---|---|
| **Area** | Navigátor Podcast |
| **Hely a vaultban** | `02_Areas/Navigátor Podcast/` |
| **Felelős** | Becze Szabolcs |
| **Státusz** | Aktív — magas érettségű tartalom-motor |
| **Engine verzió** | v0.1.0 (2026-05-26) |

---

## 2. Misszió és brand-pozíció

**A Navigátor Podcast misszió-mondata (az Alkotmányból):**
> Mélyreható párbeszédekkel térképet és alapelveket keresni egy változó világban — vendégekkel együtt.

**Pozíció:** A magyar vállalkozói / önfejlesztési podcast tér mély-interjú szegmensének vezető hangja. NEM news, NEM edutainment, NEM life-coaching — hanem **komoly, alázatos keresés**.

**Versenyelőny:** 5700+ feliratkozó, 5.7M megtekintési perc, 39 Gold Standard szintézis, és egy közönség, amely 17-20 percet néz egy 60-120 perces epizódból. Ez az átlagos megtartás iparági mérce szerint kivételes.

---

## 3. Célközönség

**Demográfia (YouTube Analytics-ből, 2026-04 baseline):**
- **89.6% 35+ évesek**, legnagyobb szegmens 45-54 (33.3%)
- **53.1% nő**, 46.9% férfi
- **81.8% magyar nyelvterület:** HU 61.7%, RO (Erdély) 15.8%, SK + RS + AT
- Erdély a második legnagyobb közönség — tudatosan kezelendő szegmens

**Téma-affinitás (top-performer pattern-ekből):**
- TOP 1: pszichológia / belső élet (nárcizmus, vércukor, fáradtság, fegyelem)
- TOP 2: hosszú formátumú (60-120 perces) mélybeszélgetések
- Az erdélyi szegmens: közéleti és helyi-kulturális témák iránt különösen fogékony

**Mit NEM akar a közönség:**
- Promotált, "marketing-szagú" tartalom
- Rövid, felszínes formátumok amelyek nem illeszkednek a mélység-ígérethez
- Clickbait és engagement-farming

---

## 4. Brand-hang (Tone of Voice)

**Alap hangvétel:** mély, alázatos, kereső. A host téved nyilvánosan — és ez erény.

**4 hangzásszabály:**

1. **Éberség-jelenlét:** minden poszt egy konkrét pillanatban él. Nem általános igazságok, hanem valós megfigyelések.
2. **Harmadik út:** nem fekete-fehér állítások. A kérdés mindig: "és mi más is lehetséges?"
3. **Bátorság + alázat kettőse:** merem kimondani, amit látok — de nem tudom a végső választ.
4. **Integritás:** amit mondunk, azt tesszük. Ami kiment, az mögött állunk.

**Formátum-irányelvek:**

| Platform | Hang | Hossz | Tiltott |
|---|---|---|---|
| YouTube | podcast-host-authoritative, HU | leírás: max 5000 ch | clickbait cím, megtévesztő thumbnail |
| Facebook | közösségi, meleg, HU | rövid poszt + link | kampány-szagú CTA |
| Patreon | bizalmas, zárt körnek szóló, HU | szabadon | „exclusive" zsargon, nyomásos FOMO |

**Ami sosem működik (tiltott minták):**
- "Ne maradj le!" / FOMO-alapú CTA
- Emoji-dömping
- "Hallgasd most!" / erőltetett azonnaliság
- Statisztika-hányás kontextus nélkül ("354.000 megtekintés!")
- Vendég vagy téma "eladása" — a tartalom maga adja el magát

---

## 5. Csatorna-mix

| Csatorna | Szerepe | Priorítás | Megjegyzés |
|---|---|---|---|
| **YouTube** | Elsődleges tartalom-felület. Minden epizód itt jelenik meg teljes hosszában. | P1 | Analytics API él, Data API 0-quota. Írás: Chrome MCP. |
| **Facebook** | Külső traffic-forrás (7.9% YouTube-forgalom). Közösség-kapcsolattartás. | P2 | Vault-ban nincs dokumentált FB-stratégia — első teendő. |
| **Patreon** | Monetizáció-felület, nem tartalom-felület. 2026-os kampányterv létezik. | P3 | Szabad/fizetős határvonal még nem tisztázott nyilvánosan. |
| Spotify | Szóba jöhet — nincs vizsgálva | P4 — halasztott | `Spotify_Master_Plan.md` létezik de nincs értékelve. |
| Shorts (YT) | Discovery-tölcsér. Meglévő 17.8% traffic onnan érkezik. | P2 | Alulelméleti — egységes stratégia hiányzik. |

---

## 6. KPI-célok (2026 — baseline)

> **Megjegyzés:** ezek induló placholder-célok a Marketing Engine v0.1-hez. Az első mérési ciklus (30 nap) után felülvizsgálandók Presto `measure` módban.

| Metrika | Jelenlegi állapot | 90 napos cél | Mérési forrás |
|---|---|---|---|
| YouTube feliratkozók | ~5,780 | +150 (net) | YouTube Analytics |
| 28 napos megtekintés | ~8,872 | +15% | YouTube Analytics |
| Átlagos megtartás | 20:19 | Tartani / javítani | YouTube Analytics |
| Facebook external traffic % | 7.9% (YT forrás) | +2pp | YouTube Analytics traffic_sources |
| Patreon tagok | Ismeretlen | Baseline mérés | Patreon API / manuális |

---

## 7. Kadencia

| Csatorna | Frekvencia | Megjegyzés |
|---|---|---|
| YouTube epizód | ~2 hetente | Jelenlegi ritmus — ne gyorsíts mesterségesen |
| Facebook poszt | Epizódonként 1-2 poszt | Minimum: minden epizód launch napján 1 |
| Patreon update | Havi 1 | Ha kampány aktív |

**Epizód-launch workflow (javasolt minimum):**
1. YouTube: cím + leírás + thumbnail + idókódok + pinned comment
2. Facebook: rövid, személyes poszt + link (NEM sablonos)
3. Patreon: értesítés ha relevant

---

## 8. Kockázatok és védőkorlátok

> **Legfontosabb kockázat:** **hangváltás.** A közönség egy specifikus tónusba fektetett bizalmat (mély, alázatos, kereső). Bármely marketing-akció, amely "promotált" érzetet kelt, gyorsabban veszít feliratkozókat, mint amennyit nyerhet.

**Védelmi szabályok:**
- Minden Facebook poszt megfelel-e az "ezt Szabolcs tényleg így mondaná?" tesztnek?
- Minden YouTube cím tükrözi-e a tényleges tartalmat? (nincs expectation gap)
- Minden új csatorna-kísérlet "maradj egy epizódon belül" elvén induljon — mielőtt rendszerré tesszük

---

## 9. Kapcsolódó fájlok

| Fájl | Szerepe |
|---|---|
| `Marketing/Pipeline.md` | 6-stage kanban — aktív kampányok és publikációk |
| `Marketing/Dashboard.md` | Heti KPI tracker |
| `Marketing/Campaigns/` | Kampány-szintű CAMPAIGN.md fájlok |
| `Marketing/Publications/` | Egyedi publikációk (presto.publication.v2 schema) |
| `Marketing/Channels/` | Meglévő csatorna-dokumentáció (STRATEGIC_PREP forrás) |
| `STRATEGIC_PREP_2026-05-24.md` | Teljes jelenlét-értékelés — olvasd el mielőtt kampányt tervezel |
| `A Navigátor Podcast Alkotmánya.md` | Brand alapdokumentum — misszió, értékek |
| `Synthesis/szintézis.md` | 1035 soros cross-epizód megfigyelések |

---

## Iteration history

- 2026-05-26 10:00 — v0.1.0 — initial scaffold by Presto (plan mode, Navigátor case-study focus)
