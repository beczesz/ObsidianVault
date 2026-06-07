---
title: "Workshop Summary - 2026-03-24"
date: 2026-03-31
author: Becze Szabolcs
status: active
description: "A CPS csapat 2026-os operációs modelljét összefoglaló workshop (március 24.), amely a Sales, Delivery és Retention stratégiákat, az Unit modellt (TAM+csapattagok), kommunikációs elveket és support szinteket részletezi. Szabolcs csapata és az engineers számára készült átirat a meglévő klienskezelés és új lead-generálási folyamat dokumentációjából."
description_source: auto
description_hash: 35c4c7a230c401c7
id: fde05f6e-a7f4-4d24-84fe-0cdf56cdc492
index_schema_version: 1
bdos_index: true
---
# Workshop Summary - 2026-03-24

> Helyszín: Strada Luminisului (csapatépítő helyszín)
> Résztvevők: CPS csapat (Szabolcs + engineers)
> Forrás: Hangfelvétel-átirat

---

## 1. Stratégia - Gyors áttekintés

A workshop a CPS csapat teljes 2026-os működési modelljét járta körbe: Sales, Delivery, Retention. Szabolcs egy AI-asszisztált prezentációt mutatott be, amit a workshop alatt állított össze a meglévő dokumentációkból (Prényed, Business Model, etc.).

**Három nagy pillér:**
- **Sales** - saját pipeline építése, AI-alapú lead validáció
- **Delivery** - Unit modell operacionalizálása (TAM + Unit Members)
- **Retention** - reporting, kommunikáció, ügyfélmegtartás

---

## 2. Sales

### ICP és lead generálás

- **Célpont:** KKV-k, 10-200 fő, AWS/Azure infra, havi 3-30k EUR cloud költés
- **Trigger:** DevOps/Platform Engineer álláshirdetés = krízis = mi jövünk be csapatként
- **Pitch:** nem embert keresnek, hanem megoldást - mi olcsóbban, jobb lefedettséggel, senior+junior kombóval
- AI-alapú napi lead scanner fut, egyre több forrást fog aggregálni
- Cél: napi 5 validált lead, heti 25, amiből havi 2 új kliens - ez az ambíció

### Free Cost Optimization Report mint "wrench service"

- Ingyenes cost optimization report = ajtónyitó
- NDA + szerződés + credential hozzáférés szükséges hozzá = már van személyes kapcsolat
- Az Onrivának 5 email nem ment át, erre azonnal válaszolt
- Profil + tapasztalat + cross-sell lehetőség - ha nem lesz kliens, akkor is nyertünk

### Sales pipeline állapot

- Sonoriza sales pipeline eddig eltartja a csapatot, láthatóság van május végéig
- Szeptemberig nem leszünk veszteségesek
- Szabolcs hozza a saját pipeline-ját, Sonoriza pipeline-ja párhuzamosan fut

### Aktuális hot lead

- **Greenergy-Service Kft.** (energiaszektor, Budapest, score 11/15)
- AI azt javasolta: ne azonnal írjuk meg, mert az álláshirdetés friss, várjunk néhány napot
- Tervezett outreach: jövő hét eleje

---

## 3. Unit Modell

### Szerepkörök

**Technical Account Manager (TAM)**
- Egy személyben látja át az egész projektet
- Első kapcsolattartó a kliens felé
- Kommunikáció, eszkaláció, reporting felelős
- Felhatalmazott döntéshozó a projekten belül
- Nem lehet egyszerre mély fókuszban és "always available" - ez a feszültség tudatos, kommunikálni kell

**Unit Member**
- A TAM mögé beálló mérnök
- "Kovácsinas" szerepkör - tanul és pakol
- Junior-ok belépési pontja

**Sales Engineer**
- Külön funkció (jelenlegi SE-k: Zoli, Molnár Dani, István)
- Klienssel leül, angolul tárgyal, stressztoleráns
- A TAM és SE nem kell ugyanaz legyen minden projekten

### Azonosított Units (workshop döntés)

| Kliens | TAM | Unit tagok |
|---|---|---|
| Green Hill / SynLab | Molnár Dani (SE is egyben) | Marci, Zsolt |
| Onriva | KV (Kovács Attila?) - kimondandó | Márk, Boti |
| Colosseum Dental | Marci | Boti, Zoli |
| Diligentes | Ceclan Alexandru | TBD |
| SocialBud | Szabolcs (ritkán) | Marci, Dávid |
| Okfü | Tornai Zsolt | (önszerveződő) |
| Observer | István (projekt vezető) | fix price modell |

### Ramp-up folyamat

- Minden új kliensnél van 2-3 hetes ramp-up időszak
- Ezt explicit bele kell írni a szerződésbe (és különdíjazni, mint pl. Accenture csinálják)
- Ramp-up tartalmaz: monitoring setup, alerting, dokumentáció, quick ramp-up deck
- AI-assisted onboarding dokumentáció generálás - ne kelljen kézzel

---

## 4. Retention és Kommunikáció

### Reporting

- Havi riport minden kliensnek - ez: összefoglaló + dokumentáció + upsell lehetőség
- Marci eddig egyedül vitte - ezt AI-val kell megkönnyíteni
- Cowork Word plugin fejlesztés tervben: a riportot AI csinálja, mi csak az inputot adjuk
- Mark alázatosan és szorgalmasan "ástáss előre az utat" - ezt folytatni és optimalizálni

### Kommunikációs elvek

- **Kliens csendjében nem lehet megbízni** - ha nem mondja explicit, hogy minden OK, akkor valószínűleg nincs minden OK
- Pozitív visszajelzést ki kell erőszakolni
- Tanulság: Onriva, Ellen, Zonrisa mind csendben volt, aztán fekete leves jött
- Zonrisa 9 hónapon át csendben volt, mi nem reagáltunk elég proaktívan

### Napi jelenlét

- A kliensnek éreznie kell, hogy elérnek minket
- Nem kell azonnal megoldani, de "ott vagyunk, tudomásul vettük" visszajelzés kritikus
- Alert-rendszer / notifikáció szükséges, hogy valaki mindig vegye

### Eszkaláció szintjei

1. Csapaton belül
2. TAM eszkalál (email, Teams)
3. Szabolcshoz eszkaláció
4. Kliens döntéshozójához eszkaláció
5. Sonoriza fele (ha szükséges)

### Nemet mondás kultúrája

- Ha a kliens irreális igényeket támaszt (pl. Irina éjjel), és ez nem fér bele az SLA-ba: hivatkozni kell a szerződésre
- Ha 24/7-et akarnak, annak ára van (jelenlegi csomag: +€2.000/hó)
- "Vagy vesznek egy drágább csomagot, vagy nem vállaljuk" - ezt kell kommunikálni, nem lenyelni
- Példa: Irina panaszkodott reakcióidőre, Szabolcs megnyitotta a honlapot, ránézett az SLA táblázatra - pont az az opció hiányzott amit kért. Egyből elhallgatott.

---

## 5. Support Modell

### Normal Support (12h, munkanapokon)

- Időzónák eltolásával + korán kelő/késő fekvők kombinációjával 12h lefedhető
- Unit felelős a saját kliense normál supportjáért
- Ha valaki szabadnapon van, TAM felelős hogy valaki más beugorjon
- Ünnepnapok: normál support leáll - ha valaki ünnepi supportot akar, premium csomag kell

### 24/7 Support

- Külön szervezett dedikált csapat (5-7 fő)
- Külön projekt menedzser és schedule szükséges
- AI-alapú első szűrés: tiketek 98%-át az AI szűrje ki, csak kritikus esetben csörög telefon
- Ha egy kliensen hetente 5+ eszkaláció van: probléma, kivizsgálandó
- Rossz kliensek: 5x áron vagy kilépés

---

## 6. Eszközök

| Eszköz | Célra |
|---|---|
| **Jira** | Projekt és tiketing rendszer (már döntés) |
| **Power Automate** | Automatizálás (logic press irányba) |
| **Copilot Studio** | Power Automate flow-k "demokráciás" kezelése (HR-nek is kezelhető) |
| **Monitoring Stack** | Kiépítendő - Jira-n belül is lehet, vagy Grafana/Prometheus |
| **Financial Dashboard** | Projekt profitabilitás tracker (Szabolcs által épített, 1.5+ éve) |
| **Cowork (Claude)** | Riport generálás, case study, lead validáció, mindenhez |

### Monitoring csapat ötlet (Zoli)

- Legyen egy dedikált "monitoring csapat", akik minden új kliensnek beállítják a monitoringot
- Kevesebb context switch, fókuszált munkavégzés

---

## 7. Kommunikációs szabályok (Teams)

- Minden megbeszélés után induljon saját csatorna-szál (nem group chat)
- Ha valaki mégis rossz helyre ír, az első válasz: copy-paste a helyes csatornába + emlékeztető
- Fokuszon kívüli idő = nézze meg a chatjét és válaszoljon
- **2 órás reakcióidő elvárás** (belső, TAM szerepkörben)
- TAM szerepkörben: gyors reakció elvárt, ez a szerepkör természete
- Fókuszidő a "nem sürgős, de fontos" feladatokra való - nem a "mindenből kikapcsolok"

---

## 8. Pénzügyi kép és Csapat

### Projektek profitabilitása

| Projekt | Profit % | Megjegyzés |
|---|---|---|
| Onriva | 72% | Volt beteg projekt, most rendben |
| Jumeon (Kovács Attila) | 48% | Sárga tartomány, de stabil bevétel |
| SocialBud | Veszteséges (korán), utolsó 6+ hó nyereséges | Tanulságos projekt |
| Okfü | Egészséges | Unalmas, de megbízható bevétel - "ilyenből kell sok" |

### Célok 2026 végére

- 5-10 managed service kliens
- Csapat növekedése szükséges lesz, ha jön a pipeline
- Raymond Csirak: első hívás ha növekedünk

### Jövő (Szabolcs perspektívája)

- Ha 5 év múlva ugyanebben a pozícióban van, rosszul csinálta
- Célja: absztrakciósan felfelé haladni, a helyét Business Unit Lead tölti be
- Guildhead: Ceclan Alexandru (formalizálva, szerződéssel, szakszervezeti vezető + csapat képviselet)

---

## 9. AI és Produktivitás

- "Bal agyfélteke szteroid" analógia: AI az analitikus/adminisztratív feladatokat veszi át
- A csapatnak a "jobb agyféltekés" feladatokra kell fókuszálni: kreativitás, empátia, stratégia, kapcsolatok
- Szabolcs: minden nap van "beszarás élmény" az AI-jal - CPS-ben ez a norma lesz
- Cowork Claude integrációja (Jira, Word riport, lead validáció, case study generátor)
- Navigátor Podcast epizód: "Hogyan legyünk produktívabbak AI-jal" - ~1.5 hónapon belül megjelenik

---

## 10. TODO Lista (Workshop döntések alapján)

### Azonnali (1-2 héten belül)

- [ ] **Greenergy outreach draft** - soft angle, NIS2/24-7 pain, nem "replace your hire" - Szabolcs küldi jövő hét elején
- [ ] **Case study generátor bemutatása Nándinak** - az egész sales mappát be kell vonni (rengeteg anyag)
- [ ] **Onriva TAM kimondva** - ki lesz formálisan a TAM? (KV? Márk?) - megbeszélni a csapattal
- [ ] **Colosseum Dental - szállítási státusz** - hány nap az estimate, hol tartunk, mikor szólunk Csabának a május deadline előtt
- [ ] **Kommunikációs szabályok bevezetése Teamsben** - helyes csatorna használat, első figyelmeztetés protokoll

### Rövid távú (Q2 2026)

- [ ] **Ramp-up folyamat dokumentálása** - sablont csinálni a szerződésbe (external ramp-up + pricing)
- [ ] **Unit lista dokumentálása** - `00_Units_Concept.md` frissítése: kliens / TAM / tagok / felelősségi körök
- [ ] **Monitoring stack döntés** - Jira-n belül vagy külső tool? (Grafana/Prometheus? Azure Monitor?) - Zoli javasolta a dedikált monitoring csapat ötletet
- [ ] **Observer post-mortem** - mi ment félre, mit csinálunk másképp - felső vezetőknek is bemutatni, felelősség vállalással
- [ ] **Riport folyamat AI-ificálása** - Markkal + Bánfi Istvánnal újraálmodni, Cowork Word plugin kidolgozás
- [ ] **Jira board beállítás** - unit-onkénti boardok manuálisan hozzáadni (státuszok már készen)

### Közép-/hosszú táv

- [ ] **24/7 support csapat szervezés** - dedikált csapat, PM, schedule, AI első szűrő
- [ ] **Romania piac bővítés** - lead scanner kiterjesztése
- [ ] **Security csomag kidolgozása** - kell valaki aki mélyen beleássa magát, vagy felveszünk security szakembert
- [ ] **CPS Academy / Inference Farm service** - mint eladható csomag kidolgozása
- [ ] **Médiatartalmak** - ki akar angolul a stúdióban szerepelni? Zoli angolja jó volt megemlítve
- [ ] **Business Unit Lead szerepkör** - jövőbeli lépés, Szabolcs fokozatos kiszállása a napi operációból

---

## Kulcs-tanulságok (workshop hangulat)

> "Ezt nem lehet online megbeszélni" - Szabolcs

> "Az amatőr csapat tüzet old. A profi csapat tervez és haladékonyan, még akkor is, ha nem sürgős, de fontos."

> "Aki TAM, az válaszol. Ebben a pillanatban leveszi a sapkáját, nem TAM, hanem dolgozó - és akkor megengedheti, hogy ne válaszoljon azonnal."

> "A kliens csendjében nem lehet megbízni."

> "Valójában outsource-olod azt, amivel amúgy sem akarsz foglalkozni. Mi vagyunk a backstage crew."
