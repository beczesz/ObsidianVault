---
title: Merkantil Teams chat — full transcript (2026-04-27 to 2026-05-27)
date: 2026-05-27
author: pasted by Becze Szabolcs
status: archive
description: Verbatim copy of the internal Sonrisa Teams chat 'Merkantil' that has tracked the engagement from 2026-04-27 (chat opened by Szacsúri László) through 2026-05-27 (Becze Szabolcs added for CPS infra pricing). Pasted into the vault for searchability and historical context. Participants Sonrisa-side; Merkantil contact is "Gábor".
tags: [merkantil, teams-transcript, internal-archive, lang-hu, lang-en]
extracted: 2026-05-27
chat_name: "Merkantil"
participants_sonrisa: ["Szacsúri László", "Gergely Baján", "Komlósi Dávid", "Miklós Nándor", "Bán József", "Gergely Dombi", "Becze Szabolcs"]
participants_merkantil: ["Gábor (last name TBD), +36 70 394 1260"]
id: cad4c795-6f85-4844-9ce4-530ab92710db
index_schema_version: 1
---

# Merkantil — Teams chat transcript

> **Forrás:** Sonrisa belső Teams chat, "Merkantil" csoport. Megnyitva 2026-04-27-én Szacsúri László által. Becze Szabolcs (CPS) hozzáadva 2026-05-27-én az AID infrastruktúra árazás miatt. A teljes történet alább, kronológiai sorrendben. Felhasznált rövidítések: SzL = Szacsúri László, GB = Gergely Baján, KD = Komlósi Dávid, MN = Miklós Nándor, BJ = Bán József, GD = Gergely Dombi, BSz = Becze Szabolcs.

## 2026-04-27 (Hétfő) — Kezdeti egyeztetés a csütörtöki demóról

**SzL → csoport (14:54):** chat létrehozva, hozzáadva: Gergely Dombi és 4 további. Csoport átnevezve "Merkantil"-ra.

> SzL: hali!
> SzL: csütörtök délután 12:35-14:00, ki tud jönni?
> GB: hello! én max online, szabin leszek csütörtökön. csak személyes?
> SzL: demózzuk az email rútert, meg az ai érzékenyítési programot összerakjuk együtt
> GB: ah i see
> SzL: lehet online vagy hibrid is
> KD (idézve SzL-t): mit kell azt demózni? egy 20sec-es n8n workflow 😄 gif-be befér
> SzL: oké, elmagyarázod, hogy működik
> GB: csak barokk körmondatokkal
> KD: valszeg jobban jár mindenki ha nem én beszélek 🙂 szerintem Bán József elvállalja ugye? de a demo kész, amit múlt héten elküldtem az használható?
> SzL: nekem tetszik, de hogy használható-e, azt mondja meg a merkantil
> BJ (idézve KD-t): sure, sima ügy, előtte beszéljük majd át, hogy mit is mutatok
> MN: nézzük meg esetleg előtte a demót? nekem csütörtökön pont akkor van a fiam ballagása, így én kihagyom

## 2026-04-28 (Kedd) — Belső demó-átnézés

> BJ → MN: küldtem erre egy invite-ot holnap 11:30-ra, de az mégse lesz jó egy másik ügyfeles meeting miatt. helyette 10:00-10:30 között látok még rá némi esélyt. nektek az milyen?
> GD: Nekem sajnos nem jó, de majd elmesélitek hogy milyen volt 🙂

## 2026-05-04 (Hétfő) — Két párhuzamos ajánlat indítása

> SzL (13:32): halihó
> SzL (13:35): akkor a héten kellene küldjünk 2 ajánlat:
> 1. az Email router workflow és a n8n a Merkantilban már futó KodeSage instance mellé telepítése + ruleset kialakítása az általuk megosztott emailek és szabályok alapján
> 2. a saját 20+ fejlesztőjüknek nyújtott beginner szintű AI kurzus és workshopok ütemterve és erőforrásbecslése
> BJ (13:59): sziasztok! Igen. Az email routinghoz én megpróbálom összeszedni, hogy én milyen feladatokat látok, illetve tervezek adni egy 1-2 oldalas leírást, hogy akkor mit értünk a feladat alatt. Ha megvan, bedobom majd ide reviewra. Ahhoz a ponthoz ez jó így? Szükség van még valamire?
> SzL: tök elég, köszi Joe!
> SzL (16:08): Gergely, az RSM-es non-prod AI package-et át tudjuk alakítani a második ajánlattá?
> GB: A GenAI workshopra gondolsz?
> SzL: aha
> GB: persze, de azért az elég lightweight
> SzL: össze kell mesterkélni a sonrisa academys curriculummal, és kiszitálni belőle az advanced részeket
> GB: és az melyik? Sonrisa_AI_Strategy_Manifesto_v0.1.pptx ez?
> SzL: jajj dehogy 🙂
> GB: na, akkor segíts ki
> MN (16:19): árazni mikor kell?
> SzL (16:19): [link: Agentic AI Enablement Hub] a héten ki kellene menjen mindkettő, szóval mielőbb
> SzL (16:21): Gergely ez ugye egy self learning guide, viszont témánként csinálnánk hozzá egy előadást vagy workshopot. azt kell beárazni igazából
> GB: ok, ahogy nézem és ahogy megértettem az 1-2-3 és esetleg még a 4. pontok lehetnek érdekesek
> SzL: igen
> GB: nem ígérem hogy ma, de holnap fogok vele foglalkozni

## 2026-05-05 (Kedd) — Első ajánlat-draft + árazás javaslat

> GB (15:51): hello. összegyűjtögettem az eddigi anyagokat, kicsit promptolgattam, aztán meg letisztáztam meg itt-ott átdolgoztam az anyagot és született belőle egy ilyen: **Sonrisa_AI_Enablement_Ajanlat_Merkantil.docx**
> GB: alig-alig merkantil specifikus, úgyhogy akár máshova is használható
> GB (15:57): ami az árazást illeti, ehhez mit szóltok (az RSM árazásából kiindulva):
> - Alap ws sorozat: **3500 EUR**
> - Fejlesztői/haladó: **2500 EUR**
> - Kettő együtt: **5000 EUR**
> - Ha párhuzamosan lenne több kis csoport, akkor:
>   - 2 csoport esetén: + 2000 EUR az alap
>   - 2 csoport esetén: + 1500 EUR a haladó
> - Follow up alkalom a képzés után: **400 EUR/óra**
> - Konkrét merkantil use-case közös kidolgozása: egyedi árazás
> BJ (17:46): Sziasztok! Én itt járok, ezeket mesterkéltem eddig össze:
> 1. Lett egy rövid összefoglalója annak mit is értünk a feladat alatt, mit oldunk meg vele és hogyan.
> 2. Összeszedtem milyen taskok merülhetnek fel, itt igyekeztem minél több mindent beletenni - becslés még nincs.
> Itt eléritek őket: Intelligens email router - proposal

## 2026-05-11 (Hétfő) — Sync hívás

> SzL (11:54): halihó. gyors sync?
> GB: én meg egy másikban
> SzL: mikor jó?
> GB: 11:15
> SzL: hehe, pont akkor kezdődik nekem egy másik. kora délután?
> BJ (12:02): yettel előtt vagy után is jó, 3-ig
> SzL: akkor inkább előtte
> BJ: akkor 13:00 - 13:30?
> SzL: aha
> GB (12:46): az nekem is ok
> GB (14:58): most valószínűleg én keresem rossz helyen, de itt a megosztott file-ok között nem látom Bán József a cuccost, merre van?
> BJ: itt [idézi a 2026-05-05 saját üzenetét]
> GB: ja, sorry, ez megvolt, azt hittem van még egy becslős táblázat is
> BJ: van, a markdown fájl elején. azt másoltam át a doksi végére, csak kiszedtem a MD-eket
> GB: ahha, oksa, köszi

## 2026-05-13 (Szerda) — Ajánlat-csomag végleges és kiküldés

> SzL (9:48): halihó. megyek be a céghez, 10 körül tudunk beszélni?
> GB: Hello. Nekem 10:15-ig van Misivel egy callom, de utána jó vagyok
> BJ (9:53): Sziasztok! Majd pingeljetek itt ha kezdünk, és kiugrom egy másik hívásból.
> GB (11:49): **merkantil_ai_enablement_proposal.docx** [megosztva sales > General]
> GB (11:52): **merkantil_ai_enablement_proposal.docx** [újra megosztva]
> SzL (15:16): módosítgattam. valaki egy final peer review?
> GB: én most épp egy callban, utána ránézek
> SzL: okok, köszi
> SzL (15:21): Nándor te is belepillantassz azért pls?
> SzL (15:22): belinkelnéd a műszaki ajánlat József pls?
> BJ (15:24): **exec_summary_merkantil_intelligent_email_rounting.docx** [megosztva reseachtalk > General]
> GB: belepillantottam, sztem oké

## 2026-05-15 (Péntek) — Hétfői meeting tisztázása

> GB (16:35): sziasztok! lehet, hogy lemaradtam, a hétfői merkantil megbeszélés az online is lehet? vagy személyes?
> GB (17:44): mondjuk az nekem már biztos, hogy csak online tudok, mert a yettelben van jelenés

## 2026-05-18 (Hétfő) — Beteg gyerek, MN személyesen, Gábor elérhetősége

> SzL (9:49): sziasztok. begöthösödött a kisebbik, az anyja meg még külföldön. személyesen én sem tudok jönni, de behívok.
> BJ (10:01): Jön valaki személyesen rajtam kívül? 🙂
> SzL: Nándi menne
> MN (10:15): Igen, én megyek. Előtte beszéljünk azért 🙂
> GB: Nandi, te oszotsz? Vagy cleware és merkantil is cél ma?
> MN: Mindkettő. 4-kor végzünk és rohanok át yettel
> BJ (15:38): Miklós Nándor, oda jössz majd?
> BJ (15:56): Szacsúri László, el tudod küldeni **Gábor telefonszámát**?
> SzL (16:00): **+36703941260** [bocs]
> SzL (16:08): Gergely Baján, mondjuk hogy gyakorlati workshopba hozhatnak témát
> GB (16:12): sorry, csak közben Miki hívott
> GB (16:52): én a yettelben leszek délelőtt, nekem legkorábban sajnos aznap csak f4 körül lenne jó

## 2026-05-21 (Csütörtök) — Ajánlat módosítás: email router árát feljebb, training mellé érv

> GB (11:41): sziasztok Everyone! módosítottam ebben a doksiban, egyrészt írtam egy magyarázatot, hogy miért lett drágább az email routing megoldás (ezt mindenképp nézzétek meg pls), másrészt tettem egy kiegészítő mondatot az AI enablement training fejlesztőknek fejezetbe, hogy a workshopokat konkrét problémák megoldása köré építenénk. [merkantil_ai_enablement_proposal.docx]
> GB (11:41): amit nem módosítottam: a training árak, ez igazából mindegy honnan nézzük, jelenleg egy 5 alkalmas ws-t áraz be. mindegy mi a tartalma.
> GB (11:41): kérlek nézzétek meg, most úton leszek, ezért módosítani nem fogom tudni, de ha kell tudunk róla gyorsan egyeztetni
> GB (12:28): Miklós Nándor módosítottam a training részt is, csak elbizonytalanodtam, hogy jól emlékeztem-e a keretre, úgyhogy ezt mindenképp csekkold pls. **50 óra/hó keret**, ami lehívható trainingre, tanácsadásra, szakértői feladatokra. **20% kedvezmény**.
> BJ (13:08): Megnéztem részemről rendben.
> SzL (14:08): ez a 2 órási meeting nekem nincs ám a kalendáriumban
> SzL (14:28): lehetne?
> MN (14:33): Bszki nem küldtünk inviteot… csak egy note volt nálam.
> SzL (14:33): jeeeez

## 2026-05-23 (Szombat) — Bán József előkészíti a további igényeket

> BJ (23:16): Sziasztok! Nem beszéltük meg mit is szeretnénk még pontosan Gábornak küldeni kedden, de összemesterkéltem egy kiindulási alapot a további igényekről: **02-megvalositasi-vazlatok.md** [megosztva reseachtalk > General]

## 2026-05-25 (Hétfő) — AID infra kérdés merül fel, KodeSage út kizárva

> MN (14:16): Köszi szépen, este fogok vele foglalkozni. Kedd reggel kereslek titeket. Azt kellene kitalálni, hogy milyen környezetben tud futni a sonrisa Aid náluk. **Kb mennyibe kerülne ez nekik?**
> BJ (19:40): elméleti lehetőség, hogy a kodesage alatt futó LLM modellt használják ahhoz is. mi is próbálkoztunk hasonlóval házon belül. de nem jött be, mert a kodesage magának menedzseli a modelljeit, ha jön egy új kodesage verzió, változhat a modell alatta. amihez így mindig alkalmazkodni kell.

## 2026-05-26 (Kedd) — Időpont csúszik

> GB: Nekem nem jó a mai időpont

## 2026-05-27 (Szerda) — CPS becsatlakozik: ÁRAZÁST KELL KIKÜLDENI MA

> MN (8:26): Tegnapi callban azt ígértem, hogy kiküldöm a sonrisa aid soksit egy számmal, hogy mennyi effort ezt náluk telepíteni. Ki tudja ezt nekem megmondani? **CPS?**
> BJ (9:27): A szükséges infra kialakítást szerintem igen, **Szabi tudná beárazni**. Hasonló stack kéne nekik, mint amit nálunk is összerakott a CPS csapat. Beszéljünk egyet közösen?
> MN (10:02): Igen. Ki kellene küldenem egy számot.
> BJ (10:11): oks, már keresem Szabit
> **BJ → Becze Szabolcs hozzáadva a chathez** (megosztva a teljes történet)
> BSz (10:24): Sziasztok, most szólt Joe
> BSz (10:24): ha sürgős azonnal nekiláthatunk, ha nem akkor mit szólnál olyan dél körül?
> BSz (10:25): + kellene idő Ceclan Sanyi is, hogy az effortokat meg tudjuk határozni pontosabban
> BSz (10:25): Jó neked 12:00-kor?
> MN (10:32): Igen, de ne később, mert muszáj kiküldenem egy számot
> BSz (10:33): Miklós Nándor te is akarsz jönni erre a meetingre? vagy csak Bán József elég?
> MN (10:42): mindenképpen megyek, mert nekem kell kiküldeni az offert
> BSz (10:54): ok meghívtam mindenkit
> MN (11:10): a call végére meg kell állapodnunk a számokban. tehát nem lesz idő 1-2 napra elvonulni és visszajönni valamivel
> BSz (11:11): Megpróbálok felkészülni előtte akkor, látom volt előzménye a beszélgetésnek

> **Out of office:** Komlósi Dávid és Szacsúri László OOO 2026-05-27.

---

**Becze Szabolcs jegyzet (2026-05-27 ~11:30):** ezt a transcript-et a vault-ba mentettem, hogy a teljes történet kereshetően meglegyen. A kulcs információk a NOTES.md-be összegezve.
