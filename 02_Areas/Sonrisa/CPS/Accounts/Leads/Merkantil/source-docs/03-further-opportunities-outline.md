---
title: Merkantil — Megvalósítási vázlatok (további igények)
date: 2026-05-23
author: Bán József
status: draft
description: HU draft outline of Merkantil's verbally-raised additional needs beyond the email router and training. Six workstreams: helpdesk automation, contract analysis, knowledge-base Q&A, credit decisioning, Olga support, AI-assisted SDLC. Drafted by Bán József 2026-05-23 as a kindling document for the Tuesday meeting with Gábor. Source: 02-megvalositasi-vazlatok.md.
tags: [merkantil, opportunities, outline, draft, lang-hu]
source_file: "C:\\Users\\EvoComputers\\Downloads\\02-megvalositasi-vazlatok.md"
extracted: 2026-05-27
id: eec25c61-a3c5-45e3-aeaa-a49b49b9346c
index_schema_version: 1
---

# Megvalósítási vázlatok — további igények

> Bán József készítette 2026-05-23 (szombat 23:16) a következő keddi Merkantil egyeztetés előkészítésére: "Nem beszéltük meg mit is szeretnénk még pontosan Gábornak küldeni kedden, de összemesterkéltem egy kiindulási alapot a további igényekről."

---

## 1. Helpdesk automatizálás

A Merkantil support csapata naponta nagyszámú, sok esetben ismétlődő jellegű belső és ügyfél megkeresést kezel: termékekkel kapcsolatos kérdések, folyamatleírások, használati útmutatók. Ezeket jelenleg munkatársak válaszolják meg manuálisan, ami jelentős kapacitást köt le, és a válaszadási idő is változó.

Az igény egy olyan automatizált megoldásra irányul, amely képes a beérkező kérdéseket megérteni és a meglévő tudásbázis alapján releváns választ adni — emberi beavatkozás nélkül, vagy csak a bizonytalanabb esetekben eszkalálva.

**Lehetséges megvalósítás:** Agentic workflow, amelynek működéséhez elengedhetetlen egy jól felépített tudásbázis — ez képezi az alapját annak, hogy az AI-ügynök releváns és megbízható válaszokat tudjon adni. Ennek forrása lehet a support csapat által ma is használt segédanyagok, oktatási dokumentumok, kézikönyvek, folyamatleírások, illetve bármilyen, jelenleg embereknek szánt belső dokumentáció. Amennyiben nem áll rendelkezésre megfelelő minőségű és lefedettségű dokumentáció, alternatív megközelítésként a korábbi bejelentésekre adott válaszokat AI segítségével feldolgozva lehet azonosítani visszatérő megoldási mintákat, majd ezeket kivonatolva dokumentálni a tipikus esetekre adható helyes válaszokat.

A tudásbázis tartalma több forrásból is táplálkozhat — Confluence, belső wiki, SharePoint-dokumentumok, e-mail archívum —, ezért valószínűleg érdemes RAG (Retrieval-Augmented Generation) megoldást alkalmazni, amely az elérhető forrásokból dinamikusan állítja össze a szükséges kontextust az AI-ügynök számára.

---

## 2. Szerződéselemzés és adatkinyerés

A Merkantil szerződéstára SharePoint-alapú, és nagy mennyiségű, változatos formátumú szerződést tartalmaz. Az üzleti igény kettős: egyrészt ad-hoc dokumentumokból gyors összefoglalók készítése, másrészt meghatározott adatmezők automatikus kinyerése — például szerződő fél neve, IKT szolgáltató-e az érintett, szerződés típusa, lejárati dátum.

Jelenleg ezeket a feladatokat manuálisan végzik, ami időigényes és hibalehetőséget hordoz, különösen nagy dokumentummennyiség esetén.

**Lehetséges megvalósítás:** A megoldás két irányból közelíthető meg, a prioritásoktól és a meglévő infrastruktúrától függően.

Az első és valószínűleg legreálisabb megközelítés egy RAG pipeline kiépítése — például **Sonrisa KnowledgeVault**, Azure OpenAI + AI Search, vagy Amazon Bedrock alapon. Ez az ad-hoc összefoglalókat és a strukturált mezőkinyerést egyaránt lefedi, a SharePoint-hoz kész konektor áll rendelkezésre, és az EU adatrezidencia-követelmények is teljesíthetők.

A második megközelítés egy egyedi extrakciós pipeline, amely akkor indokolt, ha az elsődleges cél a meghatározott mezők kinyerése és azok valamilyen downstream rendszerbe való betöltése — például szerződés-nyilvántartóba, vagy adattárházba. Ez a megközelítés determinisztikusabb és auditálhatóbb, de több fejlesztési befektetést igényelhet.

---

## 3. Tudástár és dokumentáció alapú Q&A

Több területen is felmerült az igény, hogy a meglévő belső dokumentáció alapján egy automatizált rendszer tudjon kérdésekre válaszolni. A DevOps csapat **Confluence-oldalak alapján** szeretne egy asszisztenst, amely fejlesztői és üzemeltetési kérdésekre válaszol; az üzleti terület pedig alkalmazásleírások alapján várna „hogyan működik" típusú válaszokat. Mindkét esetben **Teams-integrációt** is igényelnek.

**Lehetséges megvalósítás:** A megoldás magja egy RAG-alapú pipeline, amelyhez a Confluence-tartalmak integrációja is szükséges lehet. Első lépésként érdemes megvizsgálni, hogy a Merkantilnál már bevezetett **KodeSage** rendelkezik-e ilyen képességgel, vagy bővíthető-e erre. Amennyiben igen, ez a legkevesebb új infrastruktúrával járó út.

Alternatívaként szóba jön a **Sonrisa KnowledgeVault**, amely beépített RAG képességgel rendelkezik, és szükség esetén egyedi feladatra optimalizált célügynökkel bővíthető — abban az esetben, ha az általános célú chat ügynökök képességei nem lennének elegendők. A Teams-felület mindkét esetben megvalósítható Microsoft Bot Framework vagy Power Automate segítségével, a háttérben futó RAG pipeline-ra csatlakoztatva.

---

## 4. Hitelbírálat és döntéselőkészítés

A hitelbírálati folyamat jelenleg munkaigényes, több adatforrásból összegyűjtött információk manuális értékelését igényli. Az igény egy olyan rendszerre irányul, amely az ügylet adatai alapján — amelyeket vagy közvetlenül kap, vagy meglévő interface-eken keresztül kérdez le — képes bírálati anyagot készíteni, vagy legalább döntéselőkészítő összefoglalót generálni. Alacsonyabb összegű ügyleteknél akár önálló döntés is elvárás lehet.

**Lehetséges megvalósítás:** Agentic workflow, amelyben az agent az ügylet adatait összegyűjti, a definiált szempontrendszer alapján értékeli, és strukturált bírálati javaslatot állít elő. A megoldás megbízhatósága és auditálhatósága érdekében a döntési logika explicit szabályrendszerként kerül meghatározásra — hasonlóan az e-mail routing megoldásnál alkalmazott score-alapú megközelítéshez. Az automatikus döntés kezdetben alacsony összegű ügyletekre korlátozható, a többi esetben HITL (human-in-the-loop) felülvizsgálattal.

---

## 5. Olga support — hibakezelés és script generálás

Az Olga support csapat ismétlődő jellegű megkereséseket és hibabejelentéseket kezel, amelyekre jelenleg manuálisan reagálnak. Emellett felmerült az igény, hogy repetitív feladatokhoz — elsősorban korábbi hibák tapasztalatai alapján — automatikusan generáljon a rendszer SQL scripteket.

**Lehetséges megvalósítás:** A megkeresések megválaszolása helpdesk automatizálásként kezelhető (lásd 1. pont). Az SQL script generálás kiegészítő funkcióként integrálható: az agent a hibabejelentés kontextusa és a korábbi esetek alapján javaslatot tesz a szükséges adatbázis-műveletre, amelyet a szakértő felülvizsgál és jóváhagy. A pontos scope-ot érdemes az Olga csapattal közösen tisztázni.

---

## 6. Technikai feladatok — AI-assisted SDLC

A fejlesztői csapat több, egyenként konkrétnak tűnő igényt fogalmazott meg: unit tesztek generálása Java osztályokhoz, mock szolgáltatások request/response párjainak előállítása, illetve a Katalon tesztautomatizálási eszköz AI-alapú kódgenerálással való kiegészítése. Ezek az igények közös nevezőre hozhatók: a fejlesztési és tesztelési folyamat (SDLC) AI-eszközökkel való támogatásáról van szó.

**Lehetséges megvalósítás:** A leghatékonyabb megközelítés nem egyedi, feladatspecifikus eszközök bevezetése, hanem egy egységes AI-assisted fejlesztési keretrendszer kialakítása, amely a teljes SDLC-t lefedi — tervezéstől implementáción és code review-n át a tesztelésig. Ez egyszerre old meg több igényt, és fenntartható, bővíthető alapot ad a csapatnak.

Erre a célra a Sonrisa saját keretrendszere, az **AID** kínál kész megoldást: agent definíciók (pl: tervező, implementáló, debugger, reviewer), újrafelhasználható skill-ek és bevált munkafolyamatok, amelyek bármely AI coding eszközzel és IDE-vel működnek. A csomag tartalmaz képzési anyagot is — a Sonrisa belső **Agentic Coding 101** curriculumát —, amely segít a fejlesztőknek hatékonyan megismerni és beépíteni ezeket a módszereket a napi munkájukba. A Sonrisa több projekten alkalmazza ezt a megközelítést éles körülmények között, így a bevezetéshez saját tapasztalatra alapozott support is adható.

Banki környezetben nyilvános LLM nem jöhet szóba, ezért a megoldás helyi vagy privát infrastruktúrán futó modellre épül — a már telepített KodeSage erre alkalmas lehet. Az ajánlott eszköz a **kiloCode CLI**, amely bármely IDE mellé telepíthető, és helyi LLM endpointhoz konfigurálható.

> **CPS-relevancia (Becze Szabolcs jegyzet, 2026-05-27):** Pont a 6. pont (AID) infrastruktúrája kapcsán került be a CPS a meetingbe. Bán József és Miklós Nándor 2026-05-26-án jelezte, hogy a KodeSage alatti LLM újrahasznosítása NEM járható út (KodeSage maga menedzseli a modelljeit), ezért külön inference stack kell az AID-hez Merkantilnál. Mai 12:00 call: ezt árazzuk be.
