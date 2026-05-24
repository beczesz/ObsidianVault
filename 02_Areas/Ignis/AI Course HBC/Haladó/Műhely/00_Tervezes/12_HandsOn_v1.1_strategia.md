# 🎯 Hands-on átdolgozási stratégia (v1.1)

> **Forrás:** Dry-run jelentés + pontozás (2026-05-12)
> **Cél:** A hands-on érték 6,5 → 8,5+ átlagra emelése
> **Időkeret:** A 4 órás összes idő VÁLTOZATLAN — átcsoportosítással
> **Tananyag-érintettség:** Feladat_X.X.md fájlok módosítása + oktatói segédlet v1.1

---

## A diagnózis 1 mondatban

A workshop **dramaturgiailag erős (9,0)**, **technikailag mély (Cowork-spec 8,3)**, **üzletileg releváns (8,5)** — de **a tényleges tanuló-aktivitás a felében sem éri el a 30%-ot**, az ígért 70/20/10 inkább **80/15/5**. **A javítás nem új tananyag — átrendezés.**

---

## A 4 idő-átrendezés (a foundation)

A jelenlegi időterv **F3-F4-F5 csúszás-tűrése 0**. Az új beosztás:

| Fázis | Jelenlegi | Új | Különbség |
|---|---|---|---|
| Bevezető | 30 p | **22 p** | −8 p (TransOffice-bemutatás 22→12 perc) |
| F1 | 25 p | **25 p** | — |
| F2 | 25 p | **25 p** | — |
| Szünet 1 | 15 p | **15 p** | — |
| F3 | 30 p | **35 p** | +5 p (csapatmunka kell idő) |
| F4 | 35 p | **42 p** | +7 p (3 sub-flow → 3 csoport) |
| Szünet 2 | 10 p | **10 p** | — |
| F5 | 35 p | **40 p** | +5 p (identitás-élmény) |
| F6 | 25 p | **18 p** | −7 p (a vizuális csúcs nem igényel 25p) |
| Zárás | 10 p | **13 p** | +3 p (anonim "1 mondat") |
| **Össze** | **240 p** | **240 p** | **0 (4 óra)** |

**Hatás:** F3-F4-F5 légzőhelyhez jut. F6 időben fókuszáltabb. Bevezető tempósabb (és kevésbé fárasztó az új info miatt).

---

## P0 — KRITIKUS (3 fő hands-on átdolgozás)

### P0.1 — F1: Közös CLAUDE.md HANDS-ON (5 perc)
**Most:** Az oktató generálja egyedül 4 percben → tanulók nézik.
**Helyette:** 3 fős csoportokra osztás. Mindegyik csoport diktálja a Cowork-nek "ki vagyok, mit csinálok a TransOffice-nél, mit kell tudnod rólam" — saját CLAUDE.md-t generálnak. Aztán **összehasonlítják** mit dobott más-más csoport.
**Hatás:** 6 → 8.5 hands-on. Az "én ezt csináltam" érzés azonnali.
**Implementáció:** `Feladat_1.2.md` átírása + Prompt Library A.2 frissítése.

### P0.2 — F4: 3 sub-flow → 3 csoport (12 perc dolgoz, 8 perc bemutatás)
**Most:** Mind a 3 sub-flow demo (Legal/Pénzügy/CEO) → 35 perc → 5/15 hands-on.
**Helyette:** 25 fős csoport → 3 darab 8 fős kiscsoport, mindegyik egy sub-flow-t kap:
- A-csoport: Legal sub-flow (bérleti szerződés deep-check, Béla bácsi felfedezés)
- B-csoport: Pénzügy sub-flow (Mihaela Excel + EBITDA)
- C-csoport: CEO sub-flow (5-slide PPTX)

12 perc dolgozás, aztán 3 × 2,5 perces bemutatás a teljes csoportnak.
**Hatás:** 5 → 8.5 hands-on. Mindenki valamilyen output-tulajdonos.
**Implementáció:** F4-es 3 Feladat_4.X.md teljes átírása, oktatói segédlet F4 szekciója újra.

### P0.3 — F5: "Spot the error" → "Identitás-élmény" (10 perc)
**Most:** A Cowork tölti ki a formot, a tanulók 2 hibát keresnek → frusztrációs HANDS-ON.
**Helyette:** Mindenki a saját CUI-ját, saját cégnevét, saját címét írja be a CSV-be → nézik hogyan **változik a Plan de afaceri minden említése** (a Cowork újragenerálja). **A workshop egyetlen pillanata ahol mindenki a saját életét látja**.
**Hatás:** 6 → 9 hands-on. Pszichológiailag a legerősebb pillanat.
**Implementáció:** `Feladat_5.3.md` átírása, MySMIS form-mockup CSV-import bővítése, oktatói segédlet F5.3 szekciója.

---

## P1 — FONTOS (3 további csoportmunka)

### P1.1 — F3: 12 kritérium → 3 csapatra (10 perc verseny)
**Most:** Oktató kihúzza a 12 kritériumot → 5 perc HANDS-ON ("kérdezz 1 kritériumot").
**Helyette:** 3 csapatra osztás (5-5-5 fő), mindegyik 4 kritériumot kap, **versenyhelyzet**: ki tudja gyorsabban kiértékelni? Aztán egyesítjük.
**Hatás:** 6 → 8 hands-on. Versenyenergia + outputot termel.
**Implementáció:** `Feladat_3.1.md` második fele, oktatói segédlet F3.1 szekciója.

### P1.2 — F2: Saját TODO írás + összehasonlítás (8 perc)
**Most:** Cowork-kel meeting → 18 TODO → HANDS-ON "új session, kérdezz".
**Helyette:** Mielőtt a Cowork dolgozik, **mindenki ír kézzel 3 TODO-t** a meeting-ből. Aztán a Cowork futtatja → összehasonlítják. "Ah, ezt is megfogalmazta!" / "Ezt én is kiszúrtam!" → **kalibrálás-élmény**.
**Hatás:** 7 → 8.5 hands-on.
**Implementáció:** `Feladat_2.1.md` előbukkanó-szekció.

### P1.3 — F6: 2 alap + 1 közös HANDS-ON (8 perc)
**Most:** 3 variánst az oktató demózik → 8 perc HANDS-ON (mindenki saját).
**Helyette:** 2 alapváltozat oktatótól (Modern + Erdélyi), **a 3. (Klasszikus) közösen** — az oktató magyarázza a brief-et ("konzervatív B2B, intézményi ügyfelek"), a csoport diktálja a Cowork-nek élőben. Aztán **mindenki saját** F6.2 (4-5 perc).
**Hatás:** 9 → 9.5 hands-on. A "Modern+Erdélyi" elég vizuális csúcs, a "Klasszikus" születése csoportmunka.
**Implementáció:** `Feladat_6.1.md` átírása, oktatói segédlet F6 szekciója.

---

## P2 — KÍVÁNATOS (3 finomítás)

### P2.1 — Bevezető: bemutatkozás újra (5 perc → 5 perc, de pozitív)
**Most:** "Hány %-ban használod az AI-t?" → "nullások" megszégyenülhetnek.
**Helyette:** "1 dolog amit ma várok az AI-tól" — pozitív, nem hierarchikus.
**Hatás:** Hangulat 7 → 8.5.

### P2.2 — Zárás: "1 mondat" lehet anonim/Mentimeter (3 perc)
**Most:** Körkérdés szóban (kínos a csendes embereknek).
**Helyette:** Mentimeter live (vagy nyomtatott cetli a falra). Mindenki ír valamit, akkor is ha nem szólal meg.
**Hatás:** Bevonás 70% → 95%.

### P2.3 — F4: Béla bácsi felfedezés "kérdezz vissza"
**Most:** "Itt egy fontos dolog. A Cowork megtalálta..."
**Helyette:** "Mit gondoltok, miért emelte ki a Cowork pont ezt a 41. mondatot?" → a résztvevő ráébred.
**Hatás:** WOW 10 → 10 (megtartva), de tudásszikra megnő.

---

## P3 — NICE-TO-HAVE (2 átláthatósági fejlesztés)

### P3.1 — Becsületes átláthatóság a bevezetőben
**Most:** Nem említi explicit hogy a Béla bácsi-válasz és a Mihaela-Excel előre meg van rendezve.
**Helyette:** Bevezetőben: "A workshop 5 nap valódi munkát tömörít 4 órába — egyes válaszok és emailek a film miatt fiktívek, de a Cowork-képességek mind valódiak."
**Hatás:** Realizmus 7 → 8. Bizalom-növelés.

### P3.2 — F4: CEO PPT élő-vs-előre kérdés rendezése
**Most:** Élőben generálja, néha hibázik.
**Helyette:** Az oktató választhat: élő generálás (kockázatos) VAGY előre legenerált PPT bemutatása + 1 slide élő-módosítás (biztonságos).
**Hatás:** Tempó stabil, ha élesben generálási lassúság van.

---

## Időszimuláció — új arányok

| Fázis | DEMO | HANDS-ON | Beszélgetés | Aktivitás % |
|---|:---:|:---:|:---:|:---:|
| Bevezető 22p | 16p | 4p | 2p | **18%** |
| F1 25p | 14p | 8p | 3p | **32%** |
| F2 25p | 13p | 10p | 2p | **40%** |
| F3 35p | 18p | 14p | 3p | **40%** |
| F4 42p | 16p | 22p | 4p | **52%** |
| F5 40p | 22p | 14p | 4p | **35%** |
| F6 18p | 10p | 6p | 2p | **33%** |
| Zárás 13p | 3p | 9p | 1p | **70%** |
| **Össze** | **112p (47%)** | **87p (36%)** | **21p (9%)** | **átlag 40%** |

Hasonlítva az ígért 70/20/10 (de valódi 80/15/5) arányhoz: az új terv **DEMO 47% + HANDS-ON 36% + Beszélgetés 9% + szünet 8%**.

**A hands-on átlag 6,5 → 8,5+ pont.**

---

## Implementációs prioritás (mit csináljunk most)

| # | Csomag | Idő-becslés | Várt impact | Sorrend |
|---|---|---|---|---|
| 1 | **P0.1 — F1 közös CLAUDE.md** | 30 perc | Hands-on 6→8.5 | **1.** |
| 2 | **P0.2 — F4 3 csoport** | 60 perc (3 Feladat-fájl) | Hands-on 5→8.5 | **2.** |
| 3 | **P0.3 — F5 identitás-élmény** | 45 perc | Hands-on 6→9 | **3.** |
| 4 | P1.1 — F3 verseny | 25 perc | Hands-on 6→8 | 4. |
| 5 | P1.2 — F2 saját TODO | 20 perc | Hands-on 7→8.5 | 5. |
| 6 | P1.3 — F6 közös 3. variáns | 20 perc | Hands-on 9→9.5 | 6. |
| 7 | P2.1 — Bevezető újrahangolás | 15 perc | Hangulat | 7. |
| 8 | P2.2 — Zárás anonim | 10 perc | Bevonás | 8. |
| 9 | P2.3 — F4 Béla bácsi kérdés | 5 perc | Tudásszikra | 9. |
| 10 | **Oktatói segédlet v1.1** | 60 perc | Lefedi mind | **VÉGÉRE** |
| 11 | P3.1 — Átláthatóság | 5 perc | Bizalom | post-v1.1 |
| 12 | P3.2 — F4 PPT opcionalitás | 10 perc | Stabilitás | post-v1.1 |

**Össze idő mind a P0-P2-re: ~5 óra fejlesztés** (egyszeri, nem ismétlődő).

---

## Mit kérdezzek a user-től, mielőtt indulunk

1. **Mindent (P0+P1+P2) átdolgozzunk?** Vagy csak P0?
2. **Időtervet (a 22→42→40→18 perces fázisok) elfogadod-e?** Mert ha nem, az alapszerkezet kérdéses.
3. **Akarsz-e v1.1 jelölést az oktatói segédleten** (új verzió-tag), vagy csak inline frissítést a v1.0-ban?

---

**Készítette:** Claude (a dry-run jelentés alapján)
**Dátum:** 2026-05-12
**Forrás:** TransOfficeCopy/_DryRun_jelentés/jelentes.md + pontozas.md
