---
title: "Meeting transcript — Raab Computer / Patent Csoport K8s discovery (2026-05-28)"
date: 2026-05-28
status: archive
description: "Digest + verbatim of the 2026-05-28 09:28 discovery call (23 min) on the Kubernetes platform for end client Patent Csoport (SP Vagyonkezelő). Participants: Ács Gusztáv (Raab Computer), Szántó Zoltán (Sonrisa CPS tech lead), Becze Szabolcs (CPS). Becze-side audio is noise-corrupted and disregarded. Clarifies: greenfield dev-cluster-first phasing on existing VMware, hybrid-cloud as future roadmap, mission-critical Tell-system replacement, 6 PM same-day indicative number for the end client's directors budget meeting."
tags: [raab-computer, patent-csoport, meeting-transcript, kubernetes, discovery, lang-hu, archive]
participants_sonrisa: ["Szántó Zoltán (tech lead)", "Becze Szabolcs (CPS lead)"]
participants_partner: ["Ács Gusztáv (Raab Computer)"]
end_client: "Patent Csoport / SP Vagyonkezelő Kft. (securitypatent.hu)"
meeting_datetime: "2026-05-28 09:28 CEST"
duration: "22m 58s"
source_file: "C:\\Users\\EvoComputers\\Downloads\\Kuberenetes projekt.docx"
id: 1935f1f1-bc1c-47fa-953a-06f5e7b5d498
index_schema_version: 1
---

# Raab / Patent Csoport — K8s discovery call (2026-05-28)

> **Note on quality:** this is a Teams meeting recording transcript. **Becze Szabolcs's audio was noise-corrupted** (background bleed), so his transcribed lines are largely garbled and have been disregarded. The reliable content is from **Ács Gusztáv** (Raab) and **Szántó Zoltán** (CPS). Raw verbatim preserved at the bottom + in the source .docx.

## Participants

- **Ács Gusztáv** — Raab Computer Kft. (partner channel)
- **Szántó Zoltán** — Sonrisa CPS, technical lead (cloud-native), drove the technical discovery
- **Becze Szabolcs** — CPS lead (audio corrupted, disregarded)

## Key content (digest)

### End client: Patent Csoport / SP Vagyonkezelő Kft.

- Legal entity name surfaced in call: **SP Vagyonkezelő Kft.** (brand "Patent Csoport", domain securitypatent.hu; formerly ran under the "Patent" name, kept the domain).
- Security / property-protection **holding** in Győr: multiple Hungarian owners, several business lines / companies, must keep balance between group companies.
- Guards major regional firms (Gusztáv named **Audi Győr** among others). High-stakes sector: visibility = a problem ("if you end up in the newspaper, big trouble").
- ~20,000 own clients, AND they provide **outsourced dispatch service ("bérdiszpécser") to OTHER security firms** → alarm/dispatch volume can grow very dynamically. **This elasticity need is the core reason they want Kubernetes.**
- Financially healthy ("they guard the most prominent companies in the region") but **NOT unlimited budget** (Gusztáv's explicit comparison: "not as unlimited as MVM").
- **Buyer psychology:** trust-driven. Once they commit to a process they follow through; getting them to commit is the critical step. Value-aware ("if something has value, it has a price"). Hectic on price-sensitivity, varies.

### Raab Computer (the partner / channel)

- 27 years in business. IT infrastructure / system management for ~25 companies; handles up-to-the-application-layer (infra + sysadmin), software teams build apps on top.
- Patent's IT partner for **15-16 years**, does their procurement, built their current infra. Deep trust.
- Sonrisa would deliver **under Raab's "trust umbrella"** (Raab fronts and recommends Sonrisa; local presence in Győr is a value point for the client). Gusztáv: "I recommend you."

### Existing infrastructure at the end client

- **Dell servers + Dell storage**, VMware (vSphere) hypervisor, shared **SSD storage** (fast), **memory headroom available**.
- **~21-22 VMs** running, split across: development / serving (production) / internal / one "special" purpose.
- The **K8s cluster can be hosted on the existing VMware environment**; resources are allocatable. → **No new hardware needed for the dev phase.**

### The project (greenfield)

- Replacing an **old mission-critical system called "Tell"** that registers security-device events and feeds them to the dispatch service.
- **Trigger for the rewrite:** the system's support person **died**, leaving them without proper support → they are bringing development in-house and rebuilding the system.
- **Mission-critical:** continuous operation, **cannot miss alarm signals** (a missed signal = service failure). Eventually needs 7/24 ops + availability SLA. (Raab already gives the client a 1-hour desktop-support SLA today.)
- **Why Kubernetes:** elastic scale for unpredictable dispatch volume, easier rollouts (test/canary then production), automated health-checks / self-healing / auto-restart + alerting.
- **~100 microservices / pods** order of magnitude (confirmed).
- They have NOT pre-decided test envs / structure — they **expect Sonrisa to bring the package and recommendation** ("big playground", come with ideas). Szántó flagged a follow-up meeting with their **dev team about CICD pipelines** and dev-phase structure.

### Phasing (clarified — differs from the email reading)

- **Phase 1: build an on-prem DEV cluster first**, then start the **production cluster** in parallel, on the existing VMware infra. Observability (logging/monitoring/health-check/alerting) included from the start.
- **Hybrid / public-cloud is a FUTURE roadmap item, NOT Phase 1.** Design must keep hybrid extension possible. They already have components at external providers (e.g. a **customer portal** where clients log in to see their alarms / billing / documents — currently hosted at a third party they want to migrate away from later).
- → The earlier "multi-DC is the big day-1 cost driver" assumption is **overstated**: Phase 1 is a single-site on-prem dev cluster on existing VMware. Multi-DC/hybrid is a later phase.

### Commercial / timing

- **URGENT: indicative "tól-ig" (from-to) number by 18:00 TODAY 2026-05-28.** Reason: the end client's **IT director** needs a ballpark for the **directors' meeting / budget planning happening today**. Not committed numbers — an order-of-magnitude baseline so they can slot the first step into budget planning.
- **Becze's stated pricing approach:** a from-to range with a large uncertainty factor (could be a **50-100% spread**), priced to **safely cover scope (not underpriced)**, narrowed after proper scoping. Will NOT undercut to win ("I'll give the price that safely covers it; if they find it too much, we trim later").
- **Friday 2026-05-29:** first real discussion meeting.
- **Next step:** meeting with the end client's **dev team** (CICD pipelines, dev-phase structure).
- **Becze's 2-thread plan:** (1) immediate skicc/number today; (2) the broader strategic potential around the project — **bring in the Sonrisa sales director** for a longer-term conversation, ~2 weeks out (Becze is going on vacation, back "the week after next").
- Becze to send a **summary email to his superiors** today.

## Notable verbatim (Gusztáv)

> "Most fog elindulni, tehát zöld mezőbe megyünk bele." (greenfield, starting now)

> "Jelenleg egy Tell nevű rendszert használnak. Ennek az átírása fog elkezdődni... ennek a szoftvernek a támogatói oldaláról sajnos egy sajnálatos haláleset okán azt érzik, hogy nincs meg a megfelelő segítségük, és ezért próbálnak saját berkeken belül fejleszteni."

> "Bérdiszpécser szolgálatot is vállalnak... nagyon dinamikusan növekedhet a darabszám, és ezért gondolkodtak el a Kubernetes klaszteren."

> "Annyira korlátlan anyagi háttér biztos nincs, mint az MVM-nél." (on budget)

> "Az SP Vagyonkezelő egyébként így hívják ezt a céget... egy elég tőkeerős cég."

> "A ti bizalmi ernyőtök alá fogunk kerülni" / "Én ajánlak benneteket." (Raab fronting Sonrisa)

---

## Raw verbatim transcript (preserved)

> Becze-side lines are noise-corrupted; read for record only.

```
Kuberenetes projekt-20260528_122811-Meeting Recording — May 28, 2026, 9:28AM — 22m 58s

Szántó Zoltán 0:03 — Hogy milyen már meglévő infrastruktúrátok van, vagy a kliensnek... milyen infra van már?
Ács Gusztáv 0:27 — A cégünk a Raab Computer Kft., idén 27. éve áll fenn, folyamatosan rendszerfelügyelettel foglalkozunk. Az alkalmazás réteggel nem (OSI szerint mindent támogatunk az alkalmazásokig, azokat a szoftveres csapatok építik rá). ~25 cégnek tartjuk a rendszerfelügyeletét. Ez a cég [a végfelhasználó] a nagyobbak közé tartozik, vagyonvédelmi cég, nagy ügyfélkörrel, fontos nekik a rendelkezésre állás (desktopra is 1 órás SLA-nk van). Már ügyfelünk.
Ács Gusztáv 1:25 — 15-16 éve folyamatosan náluk vagyunk, a bizalom megvan, a beszerzéseket is nálunk csinálják, az infrastruktúrát is mi építettük ki. Jelenleg: Dell rendszer, Dell storage, 3 szerver kapcsolódik rá, VMware-es megoldás, virtuális szerverek, ~21-22 szerver üzemel (fejlesztés / kiszolgálás / belső / egy különleges célra). VMware környezetbe lehetne elhelyezni a clustert, erőforrás van (memória, SSD tárhely gyors).
Szántó Zoltán 2:48 — VMware-ben futó környezet / hipervizor tisztázása.
Ács Gusztáv 3:07-3:43 — Hipervizor a készülékeken, közös storage. Lokális on-prem megoldást kellene 1. körben, van egy fejlesztői csapatuk. Egy régi szoftver kiváltó verzióját fejlesztenék ebben a környezetben, később itt üzemeltetnék; itt jönne a 7/24 felügyelet + rendelkezésre állási szerződés. Kritikus: biztonsági eszközök bejegyzéseit a diszpécserszolgálat felé feladó szoftverrendszer. Jelenleg "Tell" nevű rendszert használnak, ennek átírása indul. Bérdiszpécser szolgálat miatt dinamikusan nőhet a darabszám → ezért Kubernetes (skálázás, frissítések könnyebb bejátszása, automatizált health-check).
Szántó Zoltán 5:30 — Fejlesztés alatt álló projekt?
Ács Gusztáv 5:33-5:59 — Most indul, zöld mező. Dev fázisban még nem jön a nagy terhelés, de ott akarják kezdeni. Tudomásom szerint mástól nem kértek ajánlatot, hozzánk ragaszkodnak, helyben vagyunk.
Szántó Zoltán 6:30 — 1. körben egy fejlesztői clustert építünk, párhuzamosan a production clustert; observability, logging, monitoring, health-check, alert mellé.
Ács Gusztáv 7:00-8:14 — Igen. Hibrid cloud elvárás: 1. körben on-prem, de a hibrid kiterjesztés lehetőségét fenn kell tartani. Vannak külön szolgáltatóknál lévő komponenseik (pl. ügyfélportál, ahol az ügyfelek bejelentkeznek: riasztások, számlázás, dokumentáció), ez most egy harmadik szolgáltatónál van, onnan költöznének. Ár-érték arányban keresik a legjobb felhő/erőforrás szolgáltatót.
Ács Gusztáv 8:14-9:41 — A koncepció képlékeny. 1. lépés: on-prem fejlesztői környezet ebben a filozófiában. Bármi egyéb igény külön projekt. Most csak erre tudunk mondani valamit. Igazgatói értekezlet most zajlik, az informatikai igazgató kért egy indikatív számot a büdzsé-tervezéshez az 1. lépcsőre.
Ács Gusztáv 10:03 — Élesben nem lehet hibázni, folyamatosan megy, nincs kimaradó jelzés, mert akkor vége a szolgáltatásnak.
Szántó Zoltán 10:29-10:55 — On-prem erőforrás nem probléma; 1. körben dev cluster + observability, majd production; úgy tervezni, hogy külsős felhőszolgáltatóval hibrid rendszerbe hozható legyen.
Ács Gusztáv 11:02-11:29 — Pontosan ez a kérés. Hogy a production a végén ide vagy felhőbe kerül, az erőforrásoktól függ. Szép projekt, reméljük elindul.
Szántó Zoltán 11:54 — Lesznek-e tesztkörnyezetek, stb.?
Ács Gusztáv 12:13-12:17 — Ezt még nem tárgyalták ki velünk részletesen; az ötletet, a javaslatot várják tőletek (van tapasztalatotok a fejlesztési fázisok felépítésében). Ez van az e-mailben is.
Szántó Zoltán 12:37-13:47 — Jó lenne kb. mit futtatnak a ~100 podban; van-e meglévő observability vagy zero-ról építünk. Egy meeting a fejlesztői csapattal (CICD pipeline-ok, automatizált telepítés). Ez a következő lépés.
Ács Gusztáv 13:52 — Egy meeting a csapattal mindenképp.
Becze 13:55 (értelmezett) — Gusztáv azt mondtad, ma kellene egy számot/tervet lássanak.
Ács Gusztáv 14:00-14:52 — Tól-ig kell mondani most. Az igazgatóság felé kell felterjeszteni, nem sarokszám, hanem nagyságrend, baseline a büdzsé-tervezéshez. Nem várják, hogy telibe találd a hibahatárt.
Becze 15:12 (értelmezett) — Lesz egy olló / bizonytalansági faktor, később szűkítjük.
Ács Gusztáv 15:14-15:57 — Tól-ig határ elég. Ha a tulajdonosi kör + igazgatóság rábólint, indulnak. Most van az igazgatói napjuk, ezért kérték a plusz segítséget; pénteken lesz az 1. beszélgetésünk.
Becze 16:16 (értelmezett) — 2 szálra bontom: (1) mihamarabb egy skicc ma; (2) a projekt körüli potenciál, ehhez behívnám a sales igazgatót, hosszabb távú stratégiai dolog, ~2 hét múlva (szabadságról visszatérve). Kérdés a kliens mentalitásáról.
Becze 16:41-17:10 (értelmezett) — Kétféle kliens: (a) MVM-típus, 100%-ban működnie kell, deadline tartandó, a pénz másodlagos (több mozgásteret ad); (b) ár a legfontosabb. Melyik ez?
Ács Gusztáv 17:16-18:38 — Hektikus. Magyar tulajdonosi kör, holding, sok tulajdonos, cégek közti balansz. Anyagilag jó helyzetben (a legprominensebb cégeket őrzik, pl. Audi Győr). Megnézik mennyi az annyi, de ha elindultak egy folyamatban, végigmennek. Nem korlátlan, mint az MVM. SP Vagyonkezelő a cég neve, tőkeerős.
Ács Gusztáv 18:58-19:26 — Rá szoktuk őket beszélni a jobb megoldásra, bizalmon múlik; 16-17 év alatt nem volt incidens, megvan a bizalom.
Becze 19:35 (értelmezett) — A ti bizalmi ernyőtök alá kerülünk; azt az árat adom, amivel biztosan fedezem a scope-ot, nem megyek ár alá; ha sok, faragunk.
Ács Gusztáv 19:35-20:15 — Ajánlak benneteket. Ha van értéke, van ára; ők is szolgáltatnak, tudják. Olyan cégeket védenek mint az Audi Győrben.
Becze 20:35 (értelmezett) — Küldd el a honlapjukat, utánanézek; összesítő e-mailt írok a fölötteseimnek.
Ács Gusztáv 20:47-21:31 — Beírom a chatbe. Régen "Patent" néven futottak, megtartották a domaint, most "Patent Csoport", a holding szerkezetre utal; itt találjátok a dolgaikat. [securitypatent.hu]
Becze 21:35 (értelmezett) — Köszönjük, elvonulunk, délután 6-ig küldünk valamit.
Ács Gusztáv 21:44 — Köszönöm. Jeleztem feléjük, hogy ma kapnak információt; a közvetlen kontakt kell majd a pontos megfogalmazáshoz.
Becze 22:23 (értelmezett) — Lesz egy szórás (akár 50-100%), benne a kétely; ha oké, megyünk tovább, és pontosítjuk.
Ács Gusztáv 22:41 — Ennyi információból lehetetlen pontosan belőni; később pontosítható.
[Zárás, elköszönés.]
```
