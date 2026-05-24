Implementációs fázisok
Bevezetés
Az ügyfelek megfelelő támogatásához nélkülözhetetlen egy megbízható infrastruktúra, ami a különböző szolgáltatásaink megbízható alapját biztosítja. Ez nem csak a CPS csapat érdeke - megfelelő tervezéssel általános vállalati szintre hozható. 
Általános architektúra
Kubernetes alapú, menedzselt infrastruktúra, valamelyik cloudban.
Ütemezés
Phase 0: Cloud provider kiválasztása
A szóba jöhető Cloud Providerek: AWS, GCP, Azure, Oracle
A részletes analízist most nagyvonalúan félredobva az Oracle Cloud-ot javaslom: Egyfelől Oracle partnerek lettünk, hasznos lenne tapasztalatot szerznünk benne. Másfelől az Oracle Cloud elég nagyvonalú a belépő ügyfelekkel, a lenti infrastruktúrát gyakorlatilag ingyen kiépíthetjük és futtathatjuk, nincs trial időszak
Phase 1: Operations Foundation
Step 0: Infrastructure Provisioning
Cél: Infrastruktúra template-alapú létrehozása, IaC (Infrastructure as Code), ismételhetőség
Komponensek:
Terraform
Gitlab pipeline
Step 0.5: CD Tool
L. Phase 3/step 3 - én ide tenném, de erősen kapcsolódik a CICD folyamathoz, ami még nem elég érett itt.
Step 1: Monitoring, Alerting
Cél: Általános központi log, metrika és trace gyűjtő komponens kialakítása,
Komponensek:
Victoria(Logs/Metrics/trace) https://victoriametrics.com
Grafana https://grafana.com
Step 2: Environment Access, network security
Cél: Az adott környezet hatékony, biztonságos és kontrollált elérése (ssh, kubectl, app, db, etc.)
Komponensek:
Teleport
Step 3: Ticketing
Cél: Incidenskezelési folyamatok, ügyeleti rend, eszkalációs utak, runbook-ok és post-mortem gyakorlat sok ügyfélre skálázva. Ezen felül ügyfélkommunikációs csatornák, SLA, átláthatóság.
Komponensek:
Grafana Alertmanager
Keep (?) https://docs.keephq.dev/overview/introduction
Jira Cloud
Phase 2: Intelligence
Step 1: Autonomous AI agent 
Cél: Always-on AI agent kialakítása, ami folyamatosan figyel az alertekre, és reagál rájuk 
Komponensek:
Hermes (OpenClaw?) + vmelyik LLM (pl. MiniMax)
Alert Agent
Operator Agent
Step 2: Cost Management, Reporting
Cél: Erőforrás-felhasználás mérése és allokálása ügyfelenként, tagging, optimalizálási lehetőségek és költségjelentések.
Komponensek:
Opencost (?)
Finops Agent
Phase 3: CI/CD
Step 1: CI/CD folyamat kodifikálása
Cél: Build, test és deploy folyamatok felépítése, release stratégia, rollback lehetőségek és a pipeline-ok skálázhatósága sok ügyfélre.
Komponensek:
Step 2: CI eszköz
Komponensek:
Gitlab pipeline
Test Agent
Step 3: CD eszköz
Komponensek:
ArgoCD
Deploy Agent

