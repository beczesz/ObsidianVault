---
title: "Indikatív ajánlat - Kubernetes platform kiépítés és üzemeltetés (Raab Computer)"
date: 2026-05-28
status: draft
validity: 2026-06-30
description: "INDIKATÍV ajánlat-vázlat a Raab Computer partner-csatornán érkezett Kubernetes platform igényre. Sub-contractor pozíció (CPS beszállító Raab alá). OpenShift-alapú multi-DC architektúra, fázisolt engagement (Build + business-hours support + 7/24 support). Placeholder árazás, Ceclan effort-sizing véglegesíti. Péntek 2026-05-29 előtt küldendő draft."
practice_or_lead: raab-computer-k8s
audience: "Raab Computer (Ács Gusztáv) → end-client leadership"
language: hu
pricing_status: placeholder-pending-ceclan-sizing
id: 87c356cc-5be1-4fdd-bfc4-1c3a184adf40
index_schema_version: 1
---

# Indikatív ajánlat

## Kubernetes platform kiépítése és üzemeltetése

**Készítette:** Sonrisa Technologies, Cloud Platform Services (CPS)
**Címzett:** Raab Computer Kft. (Ács Gusztáv) - beszállítói (sub-contractor) ajánlat
**Dátum:** 2026-05-28
**Jelleg:** INDIKATÍV. Nem kötelező érvényű árajánlat. A végleges árazás a részletes felmérés (discovery) után, fix scope mellett készül.

> **Megjegyzés a számokról:** az alábbi árak indikatív tartományok, a CPS belső effort-becslése (Ceclan Sándor) véglegesíti őket. A multi-adatközpontos kiépítés a fő költség-driver, ennek pontos bound-olása a discovery feladata.

---

## 1. Vezetői összefoglaló

A Sonrisa CPS csapata vállalja egy **production-grade Kubernetes platform** kiépítését és hosszú távú üzemeltetését a leírt igények szerint. A megoldás OpenShift alapokon épül, és lefedi a kért képességeket: terhelés-alapú automatikus skálázás, service-szintű kommunikáció-szabályozás (hitelesítés és jogosultságkezelés), service discovery, állapot-monitorozás, önjavítás és riasztás, valamint a több adatközpontot átfogó (hybrid) működés.

Az együttműködést a kért fázisoláshoz igazítjuk:
- **Fázis 1 (fejlesztési szakasz, kb. 1-2 év):** a cluster kiépítése a cég környezetében, plusz munkaidős support.
- **Éles indulás után:** 7/24 üzemeltetés.

A CPS rendelkezik éles Kubernetes / OpenShift platform-tapasztalattal (referencia: 3M+ háztartást kiszolgáló energiaszektorbeli ügyfél OpenShift platformja, negyedévesről kétheti release-re, nulla állásidővel).

---

## 2. Az igény, ahogy megértettük

A megrendelő egy mikroszolgáltatás-alapú rendszert épít, amelynek a magja egy Kubernetes cluster. A platformmal szemben támasztott elvárások:

| # | Elvárás | Lefedettség |
|---|---|---|
| 1 | Node-ok és podok menedzselhetősége | OpenShift admin réteg + GitOps |
| 2 | Terhelés-alapú (lehetőleg automatikus) pod-skálázás | HPA + Cluster Autoscaler |
| 3 | Új podok hálózati regisztrálása, service discovery | OpenShift Service + DNS, mesh cross-cluster |
| 4 | Service-ek közti kommunikáció szabályozása (hitelesítés, jogosultság) | Service mesh (Istio): mTLS + AuthorizationPolicy |
| 5 | Node / pod / microservice állapot-monitorozás (health check) | Liveness / readiness probe + Prometheus |
| 6 | Önjavítás (újraindítás), sikertelenség esetén riasztás | K8s restart + Alertmanager riasztási lánc |
| 7 | Több adatközpontos / hybrid működés (céges hálózat + Vultr / más felhő) | Multi-cluster topológia + mesh föderáció + VPN/peering |
| 8 | Nagyságrendileg 100 pod / microservice | Namespace + mesh + onboarding keret |
| 9 | Kiépítés ÉS hosszú távú üzemeltetés | Fázisolt engagement (lent) |

---

## 3. Javasolt megoldás (architektúra)

**Cluster alap:** OpenShift (vagy egyenértékű enterprise Kubernetes), a CPS éles tapasztalata erre épül.

**Fő komponensek:**
- **Orchestration:** OpenShift cluster, GitOps-vezérelt (ArgoCD) deployment és konfiguráció.
- **Service mesh:** Istio. Ez adja a service-to-service hitelesítést (kölcsönös TLS) és a jogosultságkezelést (AuthorizationPolicy: pontosan melyik service melyikkel kommunikálhat).
- **Automatikus skálázás:** Horizontal Pod Autoscaler a terhelés-alapú pod-szaporításhoz, Cluster Autoscaler a node-szintű kapacitáshoz.
- **Service discovery:** beépített OpenShift Service + DNS, cluster-eken átnyúlóan a mesh föderációval.
- **Observability:** Prometheus (metrikák) + Grafana (vizualizáció) + központi log-gyűjtés. Minden node, pod és microservice állapota látható.
- **Önjavítás és riasztás:** liveness / readiness probe-ok az automatikus újraindításhoz, Alertmanager a riasztási lánchoz (e-mail / chat / on-call), ha az újraindítás nem oldja meg a problémát.
- **Multi-adatközpont / hybrid:** a robusztus minta a **multi-cluster föderáció**: a céges hálózatban és a felhőszolgáltatónál (Vultr vagy más) külön cluster fut, ezeket a service mesh köti össze biztonságos csatornán. Ez ellenállóbb, mint egyetlen, WAN-on szétfeszített cluster.

---

## 4. Engagement-modell és fázisok

### Fázis 1 - Build (a fejlesztési szakaszban, kb. 1-2 év eleje)

A cluster kiépítése a cég környezetében:
- Architektúra-design és discovery (DC-topológia, hálózat, kapacitás-terv)
- OpenShift cluster telepítés, multi-DC topológia, DC-k közti biztonságos hálózat
- Service mesh bevezetés (mTLS, kommunikáció-szabályozás)
- Autoscaling (HPA + Cluster Autoscaler) beállítás
- Observability stack (Prometheus + Grafana + log) + riasztási lánc
- Önjavítás (probe-ok) konfigurálás
- Microservice onboarding keret (a ~100 service egységes telepítéséhez)
- Dokumentáció, runbook-ok, tudásátadás

### Support - Fázis 1 (fejlesztési szakaszban, NEM 7/24)

Munkaidős managed support a fejlesztés alatt: incidenskezelés, változtatások, tanácsadás, platform-karbantartás.

### Support - éles indulás után (7/24)

Teljes 7/24 üzemeltetés készenléti ügyelettel, az éles rendszer SLA-jával.

---

## 5. Indikatív árazás

> Minden szám INDIKATÍV. A Ceclan-féle effort-sizing és a discovery véglegesíti.

| Tétel | Jelleg | Indikatív érték |
|---|---|---|
| **Fázis 1 - Build** | Egyszeri projekt (fix vagy keret) | **[Ceclan sizing: kb. 30-50 mérnök-nap]** indikatívan ~20.000-35.000 EUR egyszeri |
| **Support - Fázis 1 (munkaidős)** | Havi managed | Growth csomag bázison: **~4.000 EUR/hó** (a tényleges terheléstől függően Essential 2.000 EUR és Growth 4.000 EUR között) |
| **Support - éles után (7/24)** | Havi managed + készenlét | Scale 6.000 EUR/hó + 24/7 On-Call 2.000 EUR/hó = **~8.000 EUR/hó** |
| Opcionális add-on | havi | DevSecOps 700 EUR/hó, Solution Architect 1.000 EUR/hó (igény szerint) |

A számlázás EUR-ban vagy HUF-ban is lehetséges. A fenti a CPS beszállítói (sub-contractor) árazása Raab Computer felé; a végfelhasználó felé Raab határozza meg a saját feltételeit.

---

## 6. Feltételezések és kizárások

- A Build effort a discovery után pontosul. A fő bizonytalanság a **multi-adatközpontos topológia** mértéke (hány DC, hány cluster, milyen hálózati összeköttetés).
- Az árazás feltételezi, hogy a hardver / felhő-erőforrás (GPU nem szükséges, általános compute node-ok) a megrendelő, illetve a felhőszolgáltató (Vultr stb.) oldalán áll rendelkezésre; ez a CPS díján kívül esik.
- A ~100 microservice alkalmazás-kódját a megrendelő fejlesztői szállítják; a CPS a platformot és az onboarding keretet adja.
- A CPS ISO/IEC 27001:2022 tanúsítvánnyal rendelkezik. NIS2 tanúsítvánnyal NEM (NIS2-aware, de nem tanúsított).
- Végfelhasználó adatai (cégnév, méret, jelenlegi stack, DC-helyszínek) még tisztázandók; ezek pontosítják a Build scope-ot.

---

## 7. Minőségbiztosítás

A Sonrisa fejlesztési és üzemeltetési folyamatai az **ISO/IEC 27001:2022** tanúsítványra épülnek: dokumentált eljárások, verziókezelés, kódellenőrzés, automatikus és manuális tesztelés, változáskezelés, auditálhatóság.

---

## 8. Következő lépések

1. **Indikatív ajánlat** átadása Raab Computernek (péntek 2026-05-29 előtt).
2. **Pénteki megbeszélés** a részletek egyeztetésére.
3. **Discovery** (a végfelhasználóval): DC-topológia, kapacitás, jelenlegi stack, ütemezés.
4. **Végleges, fix-scope ajánlat** a discovery után.

---

*Sonrisa CPS - Cloud Platform Services. Kapcsolat: Becze Szabolcs.*
