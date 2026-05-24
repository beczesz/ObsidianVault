---
title: "További felismerések — mélyebb adatbányászat"
type: synthesis
project: Gergely István
created: 2026-05-21
tags: [synthesis, deep-dive, findings]
id: c4ac6cb4-1f50-4888-9faf-8ae4e44f9057
index_schema_version: 1
---

# További felismerések (2. kör mélyelemzés)

## 1. ✅ A csatornák összeállnak — GERDIT = teljes árbevétel
A három fájl 0,017%-os pontossággal egyezik (lásd [[05_GERDIT_szamlaregiszter]]):
**Adaos kasszás (4 928 463) + P2025 számlás (696 177) = 5 624 640 ≈ GERDIT 5 623 663.**
→ A teljes 2025-ös árbevétel **~5,62 M lei (áfa nélkül)**, ebből a **kasszás kiskereskedelem ~88%**,
a **számlás B2B ~12%**. A GERDIT nem beszerzés, hanem eladás.

## 2. Készlet-egészség (PTOT) — itt van a legtöbb akcióképes lelet
17 413 cikksorból:
- **267 sor negatív zárókészlettel** → leltár-/könyvelési hiba vagy nem rögzített bevételezés.
  Ezeket egyenként ki kell vizsgálni (negatív készlet fizikailag lehetetlen).
- **1 159 „holt" cikk**: van zárókészlete, de **egész évben 0 kiadás** → lekötött pénz a polcon,
  forgás nélkül. Pl. egyedi kozmetikum, prémium sör (BIRRA MORETTI, HEINEKEN SILVER), egyszer
  bevételezett, soha el nem adott tételek. **Kifuttatandó / akciózandó.**
- **1 022 teljesen mozdulatlan sor** (mind 0) → valószínűleg **duplikált vagy megszűnt cikktörzs**,
  törzsadat-tisztítás javasolt.

## 3. Mit ad el a bolt valójában (mennyiség, top mozgók)
A 6 egységen át legnagyobb darabszámú kiadás:
1. **TOJÁS (OUA CONS.CAT.L) — 228 790** db → messze a #1 forgási tétel
2. Csomagolózacskó (PUNGI AMBALAT) — 112 402 (működési tétel, nem árbevétel-fókusz)
3. Burgonya RO — 65 523 · 4. Bere Bucegi 0,5 — 64 731 · 5. Káposzta RO — 31 141
6. Damla cukorka — 29 188 · majd banán, 3in1 kávé, fehér kenyér, paradicsom, szilva
→ A **friss alapélelmiszer (tojás, burgonya, zöldség, kenyér, gyümölcs) + olcsó sör/cukorka/kávé**
a forgalmi gerinc. Mind a 6 egységben jelen vannak → **közös alapszortiment.**

## 4. Áfa-szerkezet (Adaos alapján)
A kasszás forgalom nagyjából **félbe oszlik** áfakulcs szerint:
- **~9% (élelmiszer): ~2,45 M lei** — zöldség, gyümölcs, kenyér, tej, hús, alapélelmiszer
- **~19–21% (általános): ~2,32 M lei** — sör, alkohol, üdítő, mosószer, kozmetikum, cigaretta, ipari
- A számolt kulcsok év átlagban ~20%-ot adnak a standard sávban → összhangban a romániai
  **áfa-emeléssel (19%→21%) 2025 közepén**; érdemes a kulcsváltás dátumát figyelembe venni a
  havi összevetéseknél.

## 5. Szezonalitás — két különböző minta
- **Számlás csatorna (P2025)**: erős nyári csúcs (jún–szept), mély novemberi gödör (27 e lei) →
  HoReCa/turizmus-vezérelt ([[02_ZGY_partnerek]]: panziók, catering).
- **Teljes árbevétel (GERDIT havi)**: simább, nyári csúccsal (júl 581 e), de **nincs novemberi
  összeomlás** (nov 405 e) → a kasszás kiskereskedelem stabilizálja az évet. A novemberi gödör
  tehát **kifejezetten a B2B számlás csatorna** jelensége, nem az egész cégé.

## Akció-javaslatok (adatból)
1. **Negatív készletek (267) kivizsgálása** — leltár/könyvelés pontosítás.
2. **Holt készlet (1 159 cikk) kifuttatása** — felszabaduló forgótőke.
3. **Cikktörzs tisztítása** (~1 022 mozdulatlan sor) — pontosabb riportok.
4. **Magas árrésű kategóriák súlyozása** (sör, bor, gyümölcs, állateledel; lásd [[03_Adaos_arres]]).
5. **B2B novemberi gödör okának feltárása** — szezonvég vagy elvesztett vevő?

Kapcsolódó: [[00_Attekintes]] · [[01_PTOT_keszletmozgas]] · [[03_Adaos_arres]] · [[05_GERDIT_szamlaregiszter]]
