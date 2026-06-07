---
title: "Indikatív TÓL-IG email draft — Raab / Patent Csoport K8s (2026-05-28)"
date: 2026-05-28
status: draft
description: "Email-ready indicative from-to (tól-ig) figure for Ács Gusztáv to forward to the end client (Patent Csoport / SP Vagyonkezelő) for their directors budget meeting. Derived from the CPS price list + the 2026-05-28 discovery call scope (Phase 1 = on-prem dev+prod cluster on existing VMware, hybrid later). Numbers indicative; Szántó Zoltán should sanity-check build days before send. Human-sent by Becze (confirmation-gate)."
practice_or_lead: raab-computer-k8s
audience: "Raab Computer (Ács Gusztáv) → Patent Csoport / SP Vagyonkezelő leadership"
language: hu
pricing_status: indicative-sent-pending-szanto-sizing-and-friday-scoping
send_status: sent-2026-05-28
id: d28249c2-0730-4e50-ba05-1528dffca221
index_schema_version: 1
---

# Indikatív TÓL-IG email draft

> **Internal note (not part of the email):** numbers derived from the CPS price list + the existing quote draft, adapted to the 2026-05-28 call (no new HW, Phase 1 = on-prem dev+prod on existing VMware, hybrid later). **SENT by Becze 2026-05-28 in a modified form:** build range widened to **20 000 – 45 000 EUR**, the dev-phase business-hours support row was **dropped (not quoted)**, and the post-go-live 7/24 line widened to **6 000 – 10 000 EUR/hó**. The table below reflects the AS-SENT version. Build engineer-days still to be confirmed with Szántó Zoltán; figures to be narrowed after the Friday meeting + dev-team CICD session.

---

**Tárgy:** Indikatív tájékoztató — Kubernetes platform (fejlesztési fázis)

Kedves Gusztáv!

Köszönöm a mai egyeztetést. Ahogy ígértem, küldök egy indikatív, tól-ig tájékoztatót, amit a vezetőség felé be tudtok terjeszteni a büdzsé-tervezéshez. Fontos: ezek nagyságrendi számok egy kiindulási alaphoz. A pontos, fix-scope ajánlat a pénteki egyeztetés és a fejlesztői csapattal tartott technikai kör után készül.

**Amit a mai beszélgetés alapján az 1. fázis alatt értünk:**

- Egy on-prem Kubernetes platform kiépítése a meglévő VMware környezetben (a fejlesztési fázishoz nincs új hardver-igény): először a fejlesztői cluster, majd vele párhuzamosan a production cluster.
- A kért képességek: terhelés-alapú automatikus skálázás, service discovery, service mesh (hitelesítés és jogosultságkezelés), állapot-monitorozás és önjavítás riasztással, observability (monitoring, logging, alert), CI/CD pipeline-ok, valamint a ~100 microservice egységes onboardingjának kerete.
- A hibrid/felhős kiterjesztést a tervezés végig nyitva tartja, de az egy későbbi, külön fázis.
- Az éles indulás után jön a 7/24 felügyelet és a rendelkezésre állási szerződés.

**Indikatív tól-ig (nettó EUR; HUF-ban is számlázható):**

| Tétel | Jelleg | Indikatív tól-ig |
|---|---|---|
| 1. Platform kiépítés (fejlesztői + production cluster) | egyszeri | **kb. 20 000 – 45 000 EUR** |
| 2. Éles indulás utáni 7/24 üzemeltetés (készenléttel) | havi | **kb. 6 000 – 10 000 EUR / hó** |

A tartomány szándékosan tág, mert a pontos ráfordítás a részletes felmérés után dől el (a ~100 service tényleges profilja, a meglévő observability mértéke, a hibrid igény üteme). A pénteki kör és a fejlesztői csapattal tartott technikai egyeztetés után ezt jelentősen tudjuk szűkíteni.

**Feltételezések:** az alkalmazás-kódot a fejlesztői csapat szállítja; a hardver-/felhő-erőforrás (a meglévő VMware, később a felhőszolgáltató) a megrendelő oldalán áll rendelkezésre; a CPS a platformot, az onboarding keretet és az üzemeltetést adja. A Sonrisa ISO/IEC 27001:2022 tanúsítvánnyal rendelkezik.

**Referencia:** a CPS éles tapasztalattal rendelkezik production-grade Kubernetes/OpenShift platform kiépítésében és üzemeltetésében, többek között egy több millió háztartást kiszolgáló energiaszektorbeli platformon (negyedévesről kétheti release-ütemre, nulla állásidővel).

Ha bármiben pontosítás kell a vezetőségi kör előtt, szólj nyugodtan. Pénteken egyeztetünk a részletekről.

Üdvözlettel,
Becze Szabolcs
Sonrisa Technologies — Cloud Platform Services (CPS)
