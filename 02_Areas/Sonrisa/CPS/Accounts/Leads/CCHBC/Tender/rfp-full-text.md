Cloud Platform Management - Requirements

Executive Summary

Coca-Cola HBC (CCHBC) is seeking a qualified and experienced service provider to manage, evolve, and optimize its Cloud environment through modern DevOps practices, automation, and business-aligned innovation. The goal is to establish a long-term managed services partnership that supports the full lifecycle cloud management, including deployment, operations, observability, financial governance, security, and continuous improvement, all aligned with CCHBC’s business continuity, compliance, and sustainability frameworks.
The scope of services includes not only standard cloud operations but also advanced capabilities such as:
Infrastructure-as-Code (IaC) and CI/CD pipeline management
24x7 operational support and incident management
Comprehensive observability using Dynatrace and Azure-native tooling
FinOps cost optimization and forecasting
Enablement of self-service and platform uplift for internal teams
Innovation delivery, including AIOps and Agentic AI pilots
CCHBC expects the selected vendor to operate with a high degree of technical maturity and accountability, demonstrated through clear SLA/SLO commitments, proactive reporting, and participation in crisis response (IMCR) processes. Additionally, vendors are not expected to provide standalone security services, but rather to operate all cloud services in adherence to CCHBC’s internal security guidelines and under the governance of the CCHBC Cyber teams.
The service model must be compatible with existing enterprise platforms such as ServiceNow, Dynatrace, and Azure DevOps, and must be future-ready for Google Cloud Platform (GCP) enablement. Additionally, vendors must support structured transition and exit processes, ensuring operational continuity and secure handover at both onboarding and offboarding stages.
These requirements represent a strategic opportunity for long-term partnership with CCHBC’s Digital Technology &amp; Platform Services (DTPS) team. Vendors are invited to respond with a comprehensive proposal that demonstrates technical depth, strategic alignment, and innovation capability, and that meets the specific evaluation criteria detailed herein.
Introduction

The objective is to identify a qualified service provider to manage, operate, and continuously evolve its Microsoft Azure-based cloud platform using DevOps methodologies and the Cloud Well-Architected Frameworks (WAF). The provider will be accountable for deploying, maintaining, and improving the cloud infrastructure and services with a strong emphasis on automation, observability, cost optimization, resilience, and security, all within the boundaries of CCHBC’s Business Continuity and Compliance frameworks.
This initiative directly supports CCHBC’s broader digital transformation goals by enabling a robust, scalable, and sustainable cloud foundation across multiple business and technology domains. The engagement will follow a fully managed service model, with the selected provider acting as a strategic extension of CCHBC’s internal Cloud Platform team.
While Microsoft Azure is the current primary platform and support for it is mandatory, the architecture and operational model must be future-ready for Google Cloud Platform (GCP) expansion where applicable.
The use of AI-driven tooling and practices is strongly preferred to accelerate incident resolution, optimize resources, and enforce intelligent governance. The provider is expected to recommend, integrate, and operate such tools across cloud operations, security, performance, and financial domains, including AIOps, FinOps, DevOps, and Observability Automation.
Scope of Work

The scope includes full lifecycle management of the CCHBC cloud ecosystem with a DevOps-centric approach. The selected provider will be responsible for designing, deploying, operating, and continuously improving the cloud infrastructure platform. This includes, but is not limited to, the following areas:
Infrastructure Provisioning &amp; Deployment

Utilize Infrastructure-as-Code (IaC) tools, primarily Terraform, Ansible, scripting (PowerShell, Bash), for the provisioning and management of cloud resources, with version control managed via Git.
Design, implement, maintain and operate deployment pipelines using Azure DevOps or GitHub Actions (ideal tool) to support the automated delivery of both infrastructure and applications.
Apply SDLC principles and support multi-environment configurations (e.g., Development, Testing, Pre-Production, Production), with clearly defined and automated promotion of workflows.
Ensure full alignment with the Cloud Well-Architected Framework principles and platform best practice, including reliability, security, performance efficiency, cost optimization, and operational excellence.
Manage both IaaS (e.g., Virtual Machines and Guest Oses, Windows, RedHat Linux and SUSE Linux for SAP, Storage Accounts, Cloud native Networking Services) and PaaS resources (e.g., App Services, SQL Databases and Managed Instances, Functions, APIM, and other cloud-native components).
Support the deployment and lifecycle management of containerized workloads, including services running on Azure Kubernetes Service (AKS) and compatible platforms such as Azure Container Instances (ACI) or Docker-based deployments.
Manage the full lifecycle of containers, including version upgrades, node pool scaling, integration with managed identity, and enforcing workload isolation and autoscaling policies across environments.
Platform Automation and Efficiency

Propose and implement new automation use cases that reduce manual effort, improve consistency, or accelerate change implementation.
Examples include: drift correction bots, automated tagging enforcement, backup policy validation, dynamic resource scheduling.
Continuously improve deployment processes through:
CI/CD pipeline enhancements (e.g., pipeline-as-code, reusable templates, dynamic approvals)
GitOps practices, automated testing, and artifact promotion workflows
Collaborate on platform-wide automation initiatives, such as centralized secret management, telemetry normalization, or policy compliance bots.
Implement “as-code” everything: RBAC-as-code, Policy-as-Code, Alerting-as-Code for unified deployment and auditability for green and brown field environments if needed 
Introduce drift detection dashboards for IaC vs. deployed state, with remediation suggestion scoring
As part of the DevOps enablement for application teams, the provider is expected to deliver and maintain a framework for containerized and code-based application deployments. This includes:
Providing deployment templates, reusable pipeline components, and best practice guidance
Enforcing governance rules and security scanning of Docker images using approved tools (e.g., Aqua, Trivy, Defender for DevOps)
Implementing auditing and runtime validation tooling for container workloads (e.g., image origin, vulnerability posture, policy adherence)
Supporting onboarding of development teams into secure, compliant deployment models aligned with CCHBC’s platform architecture and cloud controls
Operations &amp; Platform Support

The service provider will be responsible for the day-to-day operations and 24/7 support of CCHBC’s cloud platform and workloads. Responsibilities include proactive maintenance, incident handling, automation, and platform optimization, with a focus on reliability and operational excellence.
Provide 24x7 operational monitoring and support for all in-scope cloud services, ensuring platform availability and responsiveness according to defined SLAs/SLOs.
Execute routine operational tasks, including but not limited to:
Monitoring and alert management
Operating system and platform patching (Windows &amp; Linux)
Health checks, log reviews, and platform hygiene
Performance tuning and incident trend analysis
Capacity planning and growth forecasting
Proactive maintenance based on performance trends and trend data
Implement automated remediation mechanisms for known failure conditions, using scripting, cloud-native features (e.g., Logic Apps, Event Grid, Azure Automation), or workflow engines to minimize manual intervention.
Provide end-to-end incident, problem, and change management, integrated with CCHBC’s existing ServiceNow platform, including:
Incident prioritization and escalation paths
Root cause analysis and corrective action tracking
Close collaboration and direct communication with 3rd parties (Microsoft support, SUSE, SAP, etc.)
Change record creation, risk assessment, and implementation coordination
Coordinate with CCHBC’s incident response team to investigate, contain, and resolve incidents (including security). 
Support RCA documentation and regulatory notification workflows where applicable.
Participate in deployment readiness checks and go-live support, including rollback validation and post-deployment monitoring to ensure stability across environments.
Maintain and continuously improve a repository of operational runbooks and SOPs for routine issues, platform operations, and escalation triggers, in alignment with CCHBC governance.
Ensure cloud resource inventory is continuously updated and synchronized with CCHBC’s CMDB or asset management tooling to maintain configuration accuracy and traceability.
Maintain a vulnerability management process, including remediation SLAs based on CVSS score severity, integration with ticketing, and monthly vulnerability closure trend reporting.
Track and report on Cloud Security Posture KPIs, including Azure Advisor secure score trends.
Remediate the infrastructure and architecture related issues reported by Defender for Cloud.
Correlate observability signals (e.g., metrics, logs, traces) with incident workflows to accelerate triage, reduce noise, and support effective RCA documentation.
Monitor platform scalability thresholds with cost-efficiency insights (e.g., overprovisioned autoscaling groups, unused services) and propose corrective actions as part of monthly operational reviews.
Enforce hygiene and resource expiration policies in non-production environments to prevent orphaned services and support cost governance.
FinOps and Cost Optimization

The service provider will be responsible for supporting CCHBC’s cloud financial management goals by implementing FinOps principles and delivering actionable insights in a programmatic manner, that optimize cloud spending while enabling innovation and agility.
Enable cost visibility and accountability across CCHBC cloud environments by implementing:
Standardized resource tagging policies and enforcement for cost allocation by business unit, product, or cost center.
Budgeting and forecasting mechanisms using well-known 3rd-party FinOps tool (preferred) or Azure Cost Management.
Consumption breakdowns for infrastructure (IaaS), platforms (PaaS), and services (e.g., AKS, SQL, App Services).
Custom dashboards for CCH personas (Platform &amp; Product / Finance / Cloud).
Budget/Cost allocation logic for shared services (e.g., SAP infrastructure. monitoring, backup, DNS, network, etc) and internal showback simulations.
Handling of untagged and orphaned costs through backlog and governance escalation.
Highlight top cost drivers per group and provide alerts for budget exhaustion or anomalous spikes.
Trigger ownership escalation workflows when anomalies or budget overages persist beyond threshold.
Enable cost simulation tooling to compare consumption patterns, understand budget impact, and model future investment scenarios.
Deliver monthly chargeback dashboards showing cost per team/product/application, budget adherence, and forecast vs actual trends.
Perform continuous cost analysis and optimization, including:
Rightsizing computing and storage resources
Identification of unused or underutilized assets
Cleanup of orphaned and unused resources in a regular cadence
Continuously identify and implement pricing optimizations including Azure Hybrid Benefit, Reserved Instances, and usage-based adjustments
Workload scheduling and automation to reduce runtime costs for non-production systems. 
Track and report on realized vs. potential savings from applied optimization activities.
Provide weekly and monthly cost reporting including:
Total and per platform/product/application spend trends
Forecast vs. actual usage analysis
Identified optimization opportunities and recommended actions taken
Missed savings opportunities and cost spike root cause analysis
FinOps KPIs (e.g., coverage of tagged resources, utilization of reserved instances)
Establish a collaborative FinOps practice with CCHBC internal teams by:
Supporting platforms and product teams in understanding and managing their cloud spend
Contributing to the continuous improvement of internal cost governance policies
Aligning with internal budget cycles and investment governance processes
Provide tooling for cost simulation, pricing modeling, and forecasting scenarios
License Governance &amp; Hybrid Benefit Monitoring
Perform quarterly compliance reviews for Azure Hybrid Use Benefit (AHUB) across Windows Server, SQL Server, SUSE Linux, and Red Hat resources.
Provide recommendations and tracking on AHUB usage to maximize license entitlement and avoid missed savings.
Continuously monitor on-premises VMware environments running Windows/Linux and SQL Server to ensure proper license alignment with cloud workloads using AHUB.
Generate quarterly reporting on license compliance across hybrid environments, including risks, optimization actions, and savings potential.
Identify non-compliant deployments (e.g., cloud VMs missing AHUB flag despite eligible licenses) and propose corrective actions.
Track license overuse or underutilization and highlight expired/expiring Software Assurance or Subscription entitlements.
Include this information in the Quarterly Management Report, integrated with broader FinOps and cost governance insights.
Ensure cost insights and budget anomalies are integrated into ServiceNow or equivalent ITSM workflows where relevant, to trigger appropriate governance or approval flows.
Track GreenOps optimization focusing on emission-aware scheduling, energy-efficient workload placement, and reporting on the cost of idle carbon consumption.
Governance &amp; Agile Delivery

Maintain a structured quarterly backlog, documented using user stories with clear ownership, prioritization logic, and defined target delivery windows. 
Track all deliverables separately from SLA-driven activities, including scope, delivery date, and associated value metrics (e.g., efficiency, quality, resilience).
Work jointly with the CCHBC Cloud Governance and Automation teams to ensure that goals are aligned with the Cloud platform roadmap and transformation themes.
Performance will be reviewed during quarterly service governance with leadership-level visibility.
Conduct quarterly planning and review cycles, aligned with internal PI Planning and other Agile cadences, to ensure transparency, cross-team coordination, and outcome-based delivery across product lines.
Ensure backlog coverage includes multiple focus areas including platform &amp; operations automation, observability, FinOps, security, resilience, enablement, and innovation initiatives.
Proactively propose new backlog proposals based on operational telemetry, incident trends, optimization opportunities, or relevant industry practices.
Report value realization, for completed items, including time/cost savings, SLA improvements, or sustainability impact, where applicable.
Performance and progress will be reviewed during monthly service governance sessions, with visibility provided to relevant leadership stakeholders.
Enablement and Self-Service

Build self-service capabilities for internal product teams (e.g., environment provisioning portals, reusable pipeline libraries).
Implement ways to shift platform responsibilities left, empowering developers and analysts while maintaining governance and control.
Provide platform documentation, onboarding kits, and knowledge articles, as part of capability uplift.
Create automated deployment for default services with ServiceNow and IaC with rehardened templates.
Offer developer coaching sessions on platform tools, cost optimization, and cloud-native patterns.
Security &amp; Compliance

The service provider is expected to operate cloud workloads in full alignment with CCHBC’s internal security policies, standards, and approved tools. Security must be embedded across all lifecycle stages, not only as configuration, but as automated, auditable practices integrated into infrastructure and application delivery. Providers are not expected to define or operate security governance independently, but rather to implement and manage workloads in accordance with controls defined by CCHBC’s Cyber Security team.
Design and operate all services in accordance with CCHBC’s security policies, best practices, and the Cloud Well-Architected Framework – Security Pillar.
Enforce Zero Trust Architecture principles by validating identity, device, and network trust continuously before granting access to services.
Ensure integration with Entra ID for identity and access management, including:
Role-Based Access Control (RBAC) based on the least privilege principles
Conditional access policies and MFA enforcement
Integration with privileged access workflows and systems where applicable
Implement security practices in all infrastructure and pipeline components, including:
Secrets management (e.g., Key Vault integration)
Container image and code scanning in CI/CD pipelines (e.g., Sonar, Aqua, Defender for DevOps)
Drift detection and enforcement via Policy-as-Code
Utilize Microsoft Defender for Cloud to:
Continuously assess security posture and compliance across subscriptions
Evaluate recommendations and perform remediation actions
Act on threat alerts and trigger response workflows, where applicable and remediate the infrastructure and architecture related issues reported.
Maintain compliance adherence to relevant regulatory and industry standards (e.g., GDPR, ISO 27001, CCH internal audit frameworks) by:
SOC 2 Type 2 certification is required by the vendor, and to ensure that each year provides evidence from random systems to ensure that all of them are aligned with the security standards.
Enforcing Azure Policy assignments for governance at scale, following Cyber Security team’s guidelines
Utilize compliance score dashboards and remediate non-compliant resources
Supporting data collection and evidence reporting audit
Execute mitigation actions based on risk assessments and periodic security reviews performed by the Cyber Security team.
Ensure alignment with DevOps principles by adopting a shift-left approach that integrates security validation into every stage of the DevOps lifecycle.
Ensure that the vendor collaborates efficiently with other teams, including:
SOC Team – for security incidents and log onboarding to the SIEM.
EDR Management Team – to confirm that all relevant assets are onboarded to the EDR solution and to coordinate troubleshooting or exception management when needed.
Active Directory Team – to align on group policy management.
Network team - to ensure that the minimum connectivity is applied and not have broad communications allowed.
Backup team – to ensure that cloud workloads are covered by the resilient backup &amp; restore service 
Ensure access to sensitive environments is time-bound, justified, and properly logged and apply corrective actions provided by the quarterly privileged access reviews conducted by Cyber Security teams. 
Maintain adherence to data residency and handling requirements. Personnel with access to regulated workloads (e.g., personal data, financials) must operate within CCHBC-approved processing regions and comply with applicable data sovereignty laws.
Ensure all third-party access (vendor/contractor) is role-scoped, time-limited, and in line with CCHBC security protocols.
Observability

The service provider will be responsible for working along with CCHBC’s observability team to ensure comprehensive observability across the cloud estate, leverage existing and approved tools to deliver deep insights into system health, user experience, and service-level performance.
Utilize CCHBC’s existing Dynatrace observability platform as the primary monitoring tool for applications, infrastructure, and cloud services 24x7.
Ensure full instrumentation of services and infrastructure components across all environments.
Use dashboards for real-time visibility of application performance, infrastructure health, and business transactions.
Configure and manage synthetic monitors, real user monitoring, and custom metrics as required.
Design end-to-end telemetry (metrics, logs, and traces) and implement it using Dynatrace in combination with Azure-native monitoring tools, including:
Azure Monitor and Log Analytics
Application Insights (for supported PaaS workloads)
Diagnostic logs and activity logs
Define, track, and report on Service Level Objectives (SLOs) and error thresholds for mission-critical business and technical services.
Establish SLOs in accordance with the requirements provided by the CCHBC product and operations teams.
Ensure automated alerts are generated when error thresholds are at risk or SLOs are breached.
Ensure seamless integration of alerts and events into the ServiceNow incident management system, enabling seamless triage, escalation, and resolution tracking.
Provide continuous improvement insights based on observability insights, usage trends, and incident analysis.
Collaborate with internal teams to support integrated monitoring and event correlation for critical SaaS applications, that are not in direct scope, (e.g., Dynamics 365, SAP Commerce, etc.) but have dependencies that either impact the cloud infrastructure or are impacted by it.
In scope Cloud Infrastructure

The service provider will be responsible for managing and continuously evolving the following infrastructure components within the CCHBC Cloud ecosystem. These services span provisioning, automation, day-to-day operations, monitoring, backup orchestration, compliance enforcement, and optimization activities, in line with CCHBC governance policies.
Azure Management Groups and Subscriptions (except those explicitly delegated to other teams)
Azure IaaS Services: Virtual Machines (Windows/SUSE/Linux), Disks, Snapshots, Storage Accounts, and other IaaS resources
Windows Operating System routine patching and update management of supported cloud workloads
Linux Operating System administration and routine patching and update management of supported cloud workloads
Azure PaaS Services, including:
Azure App Services, Azure Functions, 
Azure SQL / MI (infrastructure-level only)
Azure Database for PostgreSQL (infrastructure-level only)
Azure Database for MySQL (infrastructure-level only)
Azure Kubernetes Service (AKS), other Containers
Azure API Management, Azure Key Vault, Event Grid, Service Bus
Dell Apex Cluster (Archiving solution for limited time)
Additional approved Azure PaaS offerings as adopted by CCHBC
The service provider is expected to support the onboarding and lifecycle management of new Cloud (Azure or other) services as they are formally adopted by CCHBC, ensuring phased enablement aligned with platform governance and architecture standards.
A recent high-level inventory is attached to this document. (Appendix 1)
Out of Scope Cloud Infrastructure

The following list outlines the infrastructure services that are considered out-of-scope for the Cloud Platform Managed Services engagement. This distinction is intended to provide clarity on the areas of ownership, operational responsibility, and tool usage expectations. 
Out-of-scope items are either managed by other CCHBC teams, governed under separate contracts, or are operated by other vendors, as part of the broader ecosystem.
Data &amp; Analytics Subscriptions (Microsoft Fabric, Synapse, ADF, Data Lake, etc.)
Azure Management Group &amp; Subscriptions managed by application development teams (CCHBC internal, Infosys, Proexes)
Azure Virtual Desktop (AVD) host pools, sessions and golden image configuration
Azure Arc enabled servers
On-Premises Lenovo HCI and server clusters
On-Premises VMware
On-premises Network
FortiGate appliances, hosted on Cloud or on-premises
FortiGate Firewall (including WAF) policy design &amp; rule management
Veeam Backup (on-premises VMWare)
Windows Operating System administration - While Windows OS administration (e.g., domain joins, OS-level policy tuning) is out of scope, the routine patching and update management of supported cloud workloads (e.g., Azure VMs running Windows OS) is within scope.
Microsoft SQL, PostgreSQL, MySQL and Databases (application-level) administration and tuning of database instances – While out of scope, the provisioning of Azure PaaS database infrastructure, the configuration (tiers, storage sizing, HA), backup and restore orchestration, policy enforcement, observability at the infrastructure level (availability, performance metrics), is within scope.
Microsoft Active Directory
DNS
DHCP
Group Policy
PKI and Certificate
Microsoft Entra ID
Entra Connect Sync
Conditional Access
Enterprise App Registration
Azure DNS
Microsoft Defender (use only, not manage)
Microsoft Sentinel (use only, not manage)
Dynatrace (use only, not manage)
Azure DevOps (use only, not manage)
ServiceNow (use only, not manage)
Cloud Team Structure

The Cloud Platform team operates as a cross-functional, agile organization designed to manage, evolve, and govern our cloud ecosystem across infrastructure, Automation, FinOps, and cloud engineering.
The provider will be expected to collaborate closely with our internal team, not only through service delivery interactions but also in planning, operations, and continuous improvement. Each role has clearly defined responsibilities, and the provider should align with our governance, standards, and delivery cadences. Agile ceremonies (e.g., PI Planning, Service Reviews) may involve joint participation to ensure transparency and prioritization alignment.
Short summary of Technical Roles

Platform Architect: Owns the overall architecture vision of the cloud platform. Defines architectural standards, oversees technical alignment of vendor-delivered solutions with CCHBC strategy, and ensures consistency across IaaS/PaaS, networking, and Well-Architecture Framework pillars.
Cloud Architect: Designs solutions, ensures technical governance and validates architecture for projects and other platform initiatives. Work closely with the providers to validate designs, conduct reviews, and evaluate adoption of new services or features.
Product Manager Cloud Governance: Accountable for shaping and evolving the governance model of the cloud platform (e.g., policies, guardrails, RBAC, tagging, etc.). Ensures vendor adherence to CCHBC governance principles and drives roadmap evolution through backlog, committed objectives and key results.
Cloud FinOps Leader: Leads cost visibility, forecasting, budgeting, and savings realization across the cloud estate. Collaborates with the provider to implement FinOps practices, monitor spending trends, and report cost optimization performance.
SRE: Acts as the engineering lead for operational excellence. Leads major incident response, root cause analysis (RCA), and ensures observability maturity. Will co-own critical KPIs (SLOs, MTTR) with the provider and lead performance and resiliency improvement actions.
Cloud Senior Engineers: Ensure continuity and quality of cloud operations through incident triage, monitoring alerts, change validation, and deployment readiness. These roles are the providers’ day-to-day counterparts on run-related topics.
Product Manager Cloud Automation: Manages the automation product backlog and delivery roadmap in collaboration with other CCHBC product managers. Works with provider engineers to prioritize new features, standardize reusable components, and scale self-service capabilities for developers and platform teams.
Technical Lead Cloud Automation: Provides hands-on technical leadership on IaC, pipelines, automation frameworks, and developer enablement tooling. This role will act as the primary technical counterpart for provider engineers working on automation backlog items.
Cloud Automation Engineers: Implement reusable IaC modules, CI/CD pipelines, policy automation, and platform scripts. Expected to work alongside provider DevOps engineers in a shared Git-based delivery model.
Technical Requirements

The service provider must demonstrate deep technical expertise and operational experience across the following technologies and platforms. The proposed service model must be based on automation, cloud-native tooling, and integration with existing enterprise systems.
Category
Requirement
Cloud Platform
Microsoft Azure (mandatory): Primary platform in scope for all services.
Google Cloud Platform (GCP): Future-ready architecture and support capabilities required, though not part of immediate scope.
Support multi-cloud deployments, including tooling abstraction (e.g., multi-cloud Terraform modules, centralized CI/CD for Azure/GCP).
Infrastructure as Code (IaC)
Primary tools: Terraform (strongly recommended).
IaC must be version-controlled (Git) and follow modular, reusable design patterns.
Must support parameterization, environment-specific configurations, and policy integration, including alerting and remediation scoring for IaC misalignment.
Must maintain alignment between deployed state and IaC source of truth via drift detection tools, with dashboards and remediation scoring.
Support “as-code” expansion to policies, RBAC, and alerting to enable full auditability and repeatability of cloud environments.
CI/CD Pipelines
Supported tooling: Azure DevOps, GitHub Actions, optionally GitLab CI/CD.
Pipeline templates must be reusable and modular to support cloud enablement and onboarding acceleration
CI/CD must integrate container image scanning, secrets validation, and infrastructure policy checks (e.g., with SonarQube, Aqua)
Pipelines must support:
Infrastructure deployments
Application deployments (containers and code)
Pre- and post-deployment validations
Secure integration with secrets, scanning tools, and change workflows
Containerization &amp; Orchestration
Azure Kubernetes Service (AKS): Must be fully supported.
Support for alternative runtimes: Azure Container Instances (ACI),Azure Container Apps,  Docker, and Helm-based deployments for kubernetes deployments.
Experience with private container registries and secure image pipelines.
Monitoring &amp; Observability
Dynatrace: Mandatory platform for full-stack observability, including infrastructure, applications, and end-user experience.
Must support correlation of metrics, logs, and traces to reduce alert fatigue and accelerate root cause analysis (RCA)
Include error budget policies and alerting thresholds for SLOs defined jointly with product teams
Azure-native monitoring tools (required as complement):
Azure Monitor
Log Analytics
Application Insights
IT Service Management (ITSM)
Seamless integration with ServiceNow (mandatory), including:
Incident, problem, and change management workflows
Automated ticket generation from monitoring and alerts
Approval processes tied to deployment activities
Cost &amp; Governance
Tooling and practices to support FinOps tagging, budgeting, forecasting, budget &amp; cost allocation logic
Preferred: Use of 3rd-party FinOps platforms (e.g., Apptio, Flexera, Turbonomic, other well-known)
Persona-specific FinOps dashboards (Platform &amp; Product / Finance / Cloud) that include trend analysis and optimization insights
Integration with Azure Cost Management APIs, and emission reporting where required
Security &amp; DevOps
Entra ID for identity and access control
Microsoft Defender for Cloud, Sentinel, and Azure Policy
Experience with SonarQube and Aqua Security tools for static code analysis (Preferred)
Ability to enforce security policies via IaC and CI/CD integration
Code and Automation
Scripting and automation using:
PowerShell
Ansible
Python
Bash
Azure CLI
Google CLI
Integration with Logic Apps, Azure Functions, or serverless workflows for orchestration
Sustainability &amp; GreenOps
Support Microsoft sustainability APIs, emission-aware scheduling features, and telemetry integration into reporting tools (e.g., Power BI, Dynatrace).
Service Levels (SLAs &amp; SLOs)

The service provider is expected to operate under a defined Service Level Agreement (SLA) and actively manage Service Level Objectives (SLOs) for key services and operational processes. These commitments will be tracked and reported monthly and reviewed as part of the continuous service improvement framework.
Core Operational SLAs

Metric
Target
Description
Incident response time (P0/P1)
≤ 15 minutes
Time from ticket creation to first meaningful response for critical incidents
Incident resolution time (P0) 
≤ 4 hours on 24/7 schedule
Time to resolve high-priority incidents or apply workaround
Incident resolution time (P1)
≤ 8 hours
For medium-priority issues affecting critical systems
Incident resolution time (P2)
≤ 16 hours
For medium-priority issues not affecting critical systems
Incident resolution time (P3)
≤ 32 hours
For low-priority issues not affecting critical systems
Change success rate
≥ 98%
% of changes implemented without causing incidents or rollbacks
Root cause identification
≤ 5 business days
Time to identify root cause, implement immediate preventive actions and define corrective actions to avoid recurrence after major incident
Availability &amp; Reliability SLOs

Service Area
SLO Target
Notes
Production workload availability
≥ 99.9% monthly
Measured at service level, excluding approved maintenance windows
Platform-level uptime (shared services)
≥ 99.95%
Includes shared CI/CD, identity, and observability components
Monitoring coverage (Dynatrace-monitored entities)
≥ 95% of all cloud services
All production workloads must be integrated into Dynatrace
Mean Time to Detect (MTTD)
≤ 5 minutes
From service impact to alert generation via observability tools
Mean Time to Resolve (MTTR)
≤ 3 hours (P0),≤ 6 hours (P1)
Includes diagnosis and restoration of service
SLO compliance (defined key services)
≥ 95%
Against pre-agreed SLO definitions and error thresholds
Financial &amp; Cost Optimization KPIs

The KPIs should support a proactive FinOps culture by ensuring not only resource level optimization but also forecast accuracy, stakeholder accountability, and automation coverage. These should be indicators to promote transparency, predictability, and collaborative ownership of cloud spend across CCHBC.
FinOps KPI
Target
% of tagged cloud resources
≥ 98%
% of reserved instance/savings plan utilization (eligible workloads)
≥ 85%
Cost optimization recommendations implemented with traceable savings (per month)
≥ 3 (with impact justification) ≥ 80% with validation in cost reports
Time to detect and escalate forecast overruns
≤ 24 hours
% of forecast variance (month-end vs actual)
≤ 10% for core services
% of cloud spend with owner accountability assigned
≥ 90% (via tagging)
Number of auto-deallocation or scale-down jobs executed
≥ 95% of scheduled jobs executed successfully
Chargeback coverage and reporting cadence
≥ 95% of spend reported monthly
≥ 90% of platforms/business units engaged in quarterly reviews
Reporting &amp; Transparency 

The service provider must implement a robust reporting framework that enables real-time visibility, monthly trend analysis, and strategic insights into the health, performance, and cost-efficiency of the cloud ecosystem.
Monthly Operational Reports

The provider shall deliver a structured monthly report that includes:
Category
Requirement
SLA &amp; SLO Compliance Summary
Overview of uptime and reliability per service
Summary of SLO breaches with with breach type and frequency
Error threshold usage per service (weekly/monthly trends)
Root cause analysis for critical incidents or missed objectives
Uptime % per key service with trendlines (per environment and platform tier)
Incident &amp; Problem Management Metrics
Volume of incidents (P0–P3), resolution time, and reopen rates
Mean Time to Detect (MTTD) and Mean Time to Resolve (MTTR)
Top recurring issues and associated problem management status
% auto-resolved incidents via automation (e.g., Logic Apps, Azure Functions)
Change Management Analysis
Number of changes raised and implemented
Change success/failure rates
CAB (Change Advisory Board) exceptions and emergency changes
Deployment &amp; Automation Metrics
Number of CI/CD pipeline runs (infrastructure, applications)
Deployment frequency and success rate
Lead time for changes from commit to production
Manual vs. automated deployments ratio
% of pipelines blocked due to policy
Security &amp; Compliance Posture
Defender for Cloud security score trends
Summary of non-compliant resources per Azure Policy assignments
High-risk findings from Defender, Sentinel, or vulnerability scans
Actions taken on identity/access violations or overprivileged roles
Policy coverage across core domains (identity, network, encryption, tagging) and enforcement rate
Observability &amp; Monitoring Insights
Dynatrace monitoring coverage (% of cloud workloads monitored)
Availability/performance degradation alerts and resolution paths
Custom dashboards and service health reports
RUM (Real User Monitoring) or synthetic check statistics (optional)
Continuous Improvement &amp; Governance Updates
Summary of automation improvements deployed
Lessons learned from incidents or platform optimizations
Backlog of improvement opportunities, prioritized by business value
Input for quarterly service reviews or PI Planning, if using Agile/SAFe
Estimated hours saved through automation (% reduction in manual effort)
Percentage of prioritized improvements delivered per quarter
Cost and FinOps Dashboarding

Weekly and Monthly FinOps reporting must reflect both realized savings and missed opportunities with actionable recommendations.
Category
Requirement
Monthly cloud cost overview
Actual vs. forecasted costs by subscription, application, product, platform
Top cost drivers and high-consumption anomalies
Optimization actions implemented, with monthly savings attribution (Ops-led or automated)
AI-flagged cost anomalies by subscription/product/team
Reserved Instance (RI) and Savings Plan utilization
RI/SP coverage trend and ROI performance
Upcoming expirations and renewal recommendations
Resource hygiene reporting
Underutilized or unattached resources (e.g., idle compute, orphaned IPs/disks)
Tagging coverage and compliance
Policy drift auto-remediation coverage
Governance audit scorecard (naming standards, backup, identity, encryption adherence)
Custom Dashboards
Platform/Product: Resource usage vs. budget, cost per environment, underutilized assets, app-level tagging  
 Cloud Engineering: Cost optimization backlog, automation-based savings, infrastructure scaling cost impact  
Finance: Forecast vs. actual per business unit, cost anomaly history, RI/SP utilization, investment ROI  
Security/Compliance: Cost of non-compliance (e.g., non-tagged or unencrypted resources), avoided penalties, compliance hygiene  
Product Owners: Cost per application by resource type, cost evolution by feature/release cycle
Forecasting &amp; Budget Governance
Multi-month rolling forecasts per product/platform/team  
Budget variance root cause analysis  
AI-based prediction of budget exhaustion risks (by team/product)  
Forecast accuracy scoring based on actual vs. forecast deviation (%)  
Monthly forecast adjustment logs and justifications
Application Modernization Opportunity Management
Backlog of open modernization actions  
Aging report of unaddressed savings opportunities  
Prioritization matrix by ROI, effort, and business impact  
Approval status of each action (pending, deferred, completed)  
Percentage of executed optimizations with validated cost savings
Chargeback / Showback &amp; Internal Accountability
Cost per team/product/application with owner linkage
Shared service allocation breakdown (DNS, monitoring, backups, etc.)
Custom pricing tiers for cost simulation and internal benchmarking
Showback vs. approved budget adherence report
Visual cost distribution heatmaps
Cloud Cost Behavior &amp; Trend Analytics
Application-level usage growth trends
Cost per environment trend (dev/test/prod)
Alerts on unexpected cost trajectory changes
Spend elasticity score (cost variance relative to usage/load change)
Comparative spend heatmaps (week-over-week or by region)
Forecasting Accuracy &amp; Rolling Estimate Monitoring
Monthly and rolling forecast vs. actual per subscription/team/product
Forecast variance thresholds (e.g., alerts for &gt;10% monthly deviation)
History of forecast adjustments and drivers (seasonality, launches, migrations)
Forecast confidence score per team/product (based on historical accuracy)
Forecast accuracy score (e.g., % deviation month-over-month)
Cost Accountability &amp; Cost Owner Traceability
% of resources with assigned cost center or owner (via tags or CMDB linkage)
Top 10 untagged spenders and remediation trend
Cost owner dashboard tracking spend vs. budget, resource sprawl, and unresolved optimizations
App/product-level unit economics (e.g., cost per active user, per transaction)
SaaS Licensing &amp; Subscription Cost Intelligence
Spend by licensing model (e.g., Pay-As-You-Go vs Reserved vs CSP)
RI/SP unused capacity breakdown per service
Utilization rate per licensed SKU (e.g., Premium Disk usage vs. allocation)
Missed opportunity alerts (e.g., not using Hybrid Benefit where applicable)
Cloud Sustainability / GreenOps Metrics
Estimated CO₂ emissions per resource type (based on Microsoft emissions model)
Carbon impact of idle resources (zero utilization compute/storage)  
% of resources on energy-optimized SKUs (e.g., Ampere-based ARM VMs)
Emissions saved via automation-based shutdowns
Real-Time Dashboards &amp; Shared Access

The provider is expected to offer:
Live dashboards for monitoring SLA/SLO performance, deployments, costs
Shared access to CI/CD pipeline status boards
Integration with Power BI or ServiceNow dashboards, if applicable
Persona-based dashboards (Ops Engineer, Platform Owner, Product Manager etc.)
Incident Management Crisis Response (IMCR)

The service provider is expected to fully support CCHBC’s IMCR (Incident Management Crisis Response) process, which governs the structured escalation, coordination, and resolution of major IT disruptions that pose a significant risk to business continuity.
IMCR participation is mandatory for all critical incidents that meet defined business impact thresholds, and the provider must ensure operational readiness, timely escalation, technical leadership, and communication alignment during such events. 
The service provider must have documented Standard Operating Procedures (SOPs) in place for IMCR participation. These SOPs must align with and adhere to CCHBC’s standards and escalation governance and must be shared during onboarding and updated as part of ongoing governance reviews.
Core requirements

Alignment with IMCR Framework: The provider must operate within and support the escalation flow defined in CCHBC’s IMCR process, including coordination with CCHBC Business Continuity leadership, Service Desk, Vendor Crisis Managers, and Country/Regional stakeholders.
IMCR Declaration and Triage:
Participate in initial impact assessment and contribute to IMCR declaration decision-making.
Emergency Team Mobilization:
Be available 24x7 to participate in IMCR emergency team calls, providing platform-specific updates, resolution plans, and technical recommendations.
Assign named Crisis Support Contacts with authority to act, troubleshoot, and communicate under pressure.
Crisis Communication &amp; Coordination:
Coordinate with ServiceNow and Service Desk for timely incident communication (initial notification, updates, resolution notice).
Resolution, Contingency &amp; Recovery:
Collaborate on technical resolution, business contingency activation, and potential DRP (Disaster Recovery Plan) execution.
Provide regular updates during emergency team calls, including workaround status, risk assessments, and ETR (Estimated Time to Recovery).
Service Disruption Reporting (SDR) and Prevention:
Contribute to post-crisis Service Disruption Reports (SDR), including technical RCA, timeline of events, and preventive recommendations.
Track, implement, and report on preventive and corrective actions resulting from IMCR reviews.
Crisis Tools and Escalation Integration:
Ensure incident and IMCR records are updated in ServiceNow, with references to relevant SD tickets.
Use agreed escalation paths (e.g., 24/7 Hotline, vendor-level Crisis Managers) to ensure responsiveness and traceability.
Deliverables &amp; Performance Expectations

Item
Frequency/Trigger
Description
IMCR Participation Log
Per IMCR
List of participants, timestamps, and actions contributed by provider
Emergency Call Attendance
Real-time
Named participants in all relevant crisis calls
Service Disruption Report Input
Post-IMCR
Root cause, mitigation, and technical chronology sections
IMCR Incident Escalation SLA
Immediate
Max response time to join call and provide status: &lt;15 minutes
Incident Prioritization

Priority Level
Definition
P0 – Crisis
Critical Global Business Impact
A complete outage or severe degradation of a business-critical cloud service, platform component, or infrastructure layer. Impacts multiple regions or services. No workaround is available. Requires immediate incident response, IMCR escalation, and full coordination across vendor, platform, and business continuity teams.
P1 – High 
Major Business Impact
Significant degradation or partial unavailability of a production workload or shared platform component. Affects business operations, SLAs, or key integrations. Workaround may exist but is not sustainable. Escalation required within defined SLA.
P2 – Medium Moderate Business Impact
Affects non-critical environments (e.g., dev, test) or limited functionality within a production workload. Workaround is available and business impact is contained. Requires timely resolution but not immediate escalation.
P3 – Low 
Minimal Business Impact 
No immediate impact on service availability or performance. Often relates to scheduled tasks, misconfigurations, or platform hygiene issues. Can be addressed during normal business hours or via planned changes.
Business Continuity and Disaster Recovery (BC/DR)

While backup and recovery tooling may be managed separately, the service provider is expected to support and enhance cloud-native DR capabilities as part of the operations scope. Responsibilities include:
Ensuring that mission-critical services have defined recovery objectives (RPO/RTO).
Supporting region-aware deployment architectures, failover testing, and DR runbook documentation.
Participating in DR exercises or simulations upon request.
Implement automated DR test executions with reporting into ServiceNow.
DRP scenarios must be codified via IaC or automated testable scripts, to assist in the verification of the recovery plans.
Ensure DR readiness metrics (replication health, RPO lag, app availability) are visible in Dynatrace or integrated Power BI dashboards
Use tagging, monitoring, and storage telemetry to detect when real life recovery potential deviates from defined RPO/RTO
Create templated reports after each DR simulation, documenting objectives, outcomes, gaps, remediation, and responsible teams
Tooling Responsibility and Licensing Clarification

The provider must operate within CCHBC’s approved cloud tooling ecosystem. Unless otherwise agreed:
CCHBC will maintain ownership and licensing of core platforms including Dynatrace, Azure DevOps, and ServiceNow.
The provider is responsible for maintaining operational configurations, dashboards, and integrations within these tools.
Any proposal to introduce third-party tooling must include licensing terms, cost model, and support requirements.
Tools versions must be maintained within vendor-supported ranges and align with CCHBC’s enterprise support lifecycle. Major version upgrades must go through CAB/change management
Transition &amp; Onboarding Expectations

The service provider must deliver a structured and time-bound transition plan that enables a seamless onboarding into the management of CCHBC’s cloud environment, with minimal disruption to existing services and in alignment with internal governance processes.
The provider is expected to support internal platform enablement by facilitating knowledge transfer, onboarding, and operational readiness for CCHBC’s cloud engineering teams. This includes reusable pipeline templates, self-service guardrails, and support during joint backlog or sprint planning activities.
Transition Timeline and Milestones

The full transition phase must be completed within 6 to 8 weeks from contract signature, unless otherwise agreed.
A detailed transition project plan shall be submitted within the first week, including:
Kickoff and stakeholder alignment
Environment discovery and documentation handover
Tooling integration (e.g., CI/CD, Dynatrace, ServiceNow)
Access and identity setup
Parallel run/knowledge transfer milestones
Go-live readiness review and formal service acceptance
Environment Discovery &amp; Knowledge Transfer

Conduct a structured environment assessment to baseline:
Existing Azure subscriptions, resource groups, policies, and tagging structures
Active workloads, IaC repositories, build pipelines
Monitoring integrations and observability coverage
Change and incident history (from ServiceNow or equivalent)
Review and absorb all relevant documentation (runbooks, diagrams, policies)
Shadow existing teams during the parallel run period and progressively take ownership based on service criticality
Integration with CCHBC Tooling and Processes

Ensure full integration and operational readiness across:
ServiceNow (for incidents, problems, changes, requests)
Dynatrace (monitoring, alerting, dashboards)
Azure DevOps / GitHub (pipelines, repos, workflows)
Power BI / reporting platforms for dashboards, if applicable
Implement RBAC roles and secure access controls aligned with internal security and audit requirements
Apply tagging and compliance policies from day one
Staffing and Communication

Assign a dedicated Transition Manager to oversee onboarding activities and act as the primary point of contact
Define the full delivery team, including DevOps engineers, cloud architects, automation technical lead, and support personnel
Key roles (e.g., Transition Manager, Service Delivery Manager, , Technical Coordinator) must be staffed by senior resources with a proven enterprise delivery background, ideally with relevant Cloud certifications (e.g.  Solutions Architect, DevOps Engineer, Cloud Network, Cloud Security)
Any role filled via a third-party subcontractor or external partner must be
Explicitly disclosed (company, role, duration, accountability)
Accompanied by a business justification (e.g., niche skillset, geographic requirement)
Covered by the same performance, confidentiality, and compliance commitments as primary vendor personnel
How performance will be managed
How communications and handovers will be handled
How escalation will be enforced across organizational boundaries
Provide escalation paths and define governance cadence (e.g., daily syncs during onboarding, weekly reviews after go-live)
CCHBC reserves the right to assign or involve CCH-selected partner resources in delivery oversight, onboarding, or operational coordination. The vendor is expected to accommodate these roles with full visibility, access, and participation in relevant processes and governance forums.
KPIs for Vendor Accountability

Time to replace or add a critical resource with equal or higher capability ≤ 5 business days
% of vendor resources holding Microsoft or equivalent cloud certifications ≥ 90%
Stakeholder satisfaction score for onboarding communication ≥ 85%
External resource transparency compliance score (quarterly audit) = 100%
Deliverables

The following deliverables must be provided during or at the end of the onboarding phase:
Transition and onboarding plan with sign-off from CCHBC
Updated architecture diagrams and environment inventory
Access control matrix and audit trail confirmation
SLA/SLO monitoring setup and dashboards
First full monthly operations report
Runbooks and operational procedures adapted to CCHBC environment
Identified early risks, technical debt, or improvement opportunities
Innovation Roadmap

In addition to day-to-day operations, the service provider is expected to actively contribute to the evolution of CCHBC’s cloud ecosystem by proposing and implementing innovations that improve efficiency, scalability, resilience, and internal enablement.
The provider must maintain a structured Innovation Roadmap as part of their service delivery, aligned with CCHBC’s platform objectives and reviewed quarterly. This roadmap should address three key dimensions:
AI-Driven Operations (AIOps) and Observability Enhancement

Leverage AI/ML-based features within existing tooling (e.g., Dynatrace, Azure Advisor, Defender for Cloud) to:
Predict or preemptively detect anomalies and performance regressions.
Recommend right-sizing or policy adjustments based on usage trends.
Correlate telemetry and reduce alert noise through intelligent event grouping.
Integrate with or propose AI-powered tools to enable smart forecasting (e.g., cost forecasting, resource saturation risks) and decision support for infrastructure scaling.
Use AI to analyze alert fatigue patterns, alert suppression rules, and silence anomalies Apply predictive modeling for:
Infra saturation (CPU/memory/storage)
RI/SP expiration and cost spike forecasting
Mean Time to Resolve (MTTR) projections based on incident metadata
Integrate Copilot-style assistants into the monitoring/observability UI for faster platform queries.
Agentic AI for Autonomous Remediation and RCA

In addition to embedded AIOps, the provider is expected to explore and propose Agentic AI solutions, where AI agents autonomously plan, execute, and learn from operational workflows across multiple systems.
These capabilities go beyond predictive alerts and focus on chained reasoning and action. Examples include:
AI agents that detect anomalies → perform root cause correlation → trigger validated remediation (e.g., scaling, tagging, shutdown).
Planning agents that dynamically update alert routing, thresholds, or compliance tagging based on observed behaviors.
Self-improving automation loops that adjust pipeline policies or deployment blockers based on rollout failure patterns.
Integration with ServiceNow, Dynatrace, and Azure-native automation to support autonomous multi-step execution.
Expected deliverables may include:
Quarterly proof-of-concept (PoC) pilots using Agentic AI frameworks
Measurable reduction in human intervention (e.g., % of repeat incidents auto-resolved)
Governance safeguards for override, explainability, and auditability of autonomous agents
CCHBC reserves the right to propose or mandate the use of specific AIOps tools or AI integration components in alignment with enterprise architecture, security, and enterprise tooling strategies.
Innovation Delivery &amp; Governance

Maintain a quarterly innovation backlog, reviewed during service governance meetings.
Track all innovation deliverables separately from standard SLA metrics.
Work jointly with CCHBC Cloud Architecture and Cloud Automation team to prioritize and align innovations with platform roadmap and transformation goals.
Use Quarterly Innovation OKRs, aligned with PI Planning themes, for delivery transparency
Offboarding and Exit Readiness

In the event of contract expiration, early termination, or transition to another provider, the selected vendor must execute a controlled and fully documented offboarding process to ensure continuity of operations, secure transfer of knowledge and assets, and protection of Coca-Cola HBC's intellectual property, data, and access controls.
The offboarding process must be initiated no later than 10 business days after formal notice of termination and completed within a maximum of 30 business days, unless otherwise agreed in writing.
Knowledge and Asset Transfer

The service provider must ensure complete and validated transfer of:
Infrastructure-as-Code (IaC) assets:
All Terraform/Bicep modules, environments, variables, and deployment state files
Version-controlled Git repositories, documentation and architectural diagrams on IaC structure
CI/CD Pipelines and Artifacts:
Full source of deployment pipelines (e.g., YAML files, scripts, templates)
Access to pipeline history, logs, and credential vault integrations
Runbooks and Operational Documentation:
Updated and CCHBC-specific operating procedures for all supported services
Troubleshooting playbooks and remediation workflows
Alert handling protocols and incident escalation paths
Monitoring and Observability Configurations:
Exported or shared configurations from Dynatrace and Azure Monitor
Dashboards, synthetic monitors, custom metric definitions
Alert routing logic and ServiceNow integration mappings
Configuration Baselines and State Reports:
Snapshot of active resource configurations at point of exit
Active Azure Policies, tag policies, cost controls, backup schedules
Open Items and Operational Continuity

Provide a handover of all open incidents, problems, and service requests, including:
Ticket summaries, latest status, affected stakeholders
Outstanding RCA actions or approvals
Transfer the service improvement backlog, including:
Known issues or technical debt
In-flight optimizations or automation work
Planned but unexecuted infrastructure changes
Identity and Access Revocation

Ensure the revocation of all vendor-related access rights, including:
Azure portal roles (subscriptions, resource groups, key vaults)
Git repositories, CI/CD tools, monitoring platforms, and documentation systems
Service accounts and API keys created or managed by the vendor
Provide a signed offboarding checklist confirming deprovisioning of all identities and the secure return or destruction of any CCHBC-issued credentials or devices.
Final Exit Deliverables

The provider must deliver the following no later than the agreed transition completion date:
Exit Summary Report including:
Inventory of all transferred assets
Overview of open actions and remaining risks
Recommendations for transition stabilization period
Verification of clean handovers (signed by both parties)
Post-transition support window (optional) if agreed in exit plan
Retention and IP Clauses

All infrastructure code, configurations, knowledge artifacts, and data generated under this engagement are the exclusive property of CCHBC.
The provider may not retain or reuse any templates, playbooks, or scripts developed during the engagement unless explicitly licensed or permitted by CCHBC in writing.
Post-Exit Support (Stabilization Period)

Upon request by CCHBC, the service provider shall make available key personnel for a limited post-exit support period of up to 15 business days following the completion of the handover. During this stabilization window:
The provider shall assist with clarifications, operational troubleshooting, and configuration walkthroughs related to services transferred.
Any issues directly caused by undocumented handover gaps must be remediated at no additional cost.
The provider must maintain read-only access (if required) during this period for investigation purposes, subject to approval.
The terms, scope, and personnel involved in the stabilization period will be mutually agreed prior to the transition completion.
Intellectual Property (IP) and Data Ownership

All deliverables produced under this engagement — including but not limited to code, automation scripts, deployment templates, dashboards, runbooks, documentation, and knowledge bases — shall be considered “work made for hire” and are the exclusive property of CCHBC.
The service provider shall not reuse, copy, retain, distribute, or commercialize any such assets unless explicitly licensed or authorized by CCHBC in writing.
All cloud data, metadata, logs, and backups accessed or managed during the engagement remain the sole property of CCHBC. No copies may be retained beyond contract termination.
Upon completion of offboarding, the provider shall confirm permanent deletion of any CCHBC data (production or non-production) held within its systems or personnel devices, and provide a formal data disposal declaration, if requested.
Appendix 1 – Azure Resource inventory (high-level)

Appendix 2 - Proposal Submission Guidelines and Evaluation Framework

To support a consistent and thorough evaluation process, vendors are requested to structure their proposal in alignment with the following format and content areas. Proposals should address both functional and non-functional requirements, operational capabilities, integration with CCHBC’s existing platforms, and innovation maturity.
Each section should be clearly labeled and concise, providing both narrative and supporting evidence (e.g., diagrams, reference cases, metrics, or dashboards).
Proposal Format

Executive Summary: Brief overview of your proposed approach, value proposition, and key differentiators.
Technical Solution &amp; Scope Coverage: Describe your solution’s architecture, coverage across all service domains and integration with CCHBC’s ecosystem.
Delivery Model &amp; Governance: Outline your operating model, 24x7 support capabilities, governance alignment, roles &amp; responsibilities, and collaboration with internal CCHBC teams.
Security &amp; Compliance: Summarize how your operating model will follow the CCHBC guidelines to enforce DevOps, privileged access control, policy-as-code, and support audits and compliance alignment.
FinOps &amp; Cost Optimization: Explain how you will provide FinOps services including tagging compliance, chargeback/showback, AHUB/license governance, cost forecasting, and GreenOps metrics.
Service Levels and Observability: Describe how you define, measure, and report on SLAs/SLOs. Explain your observability approach, telemetry coverage, and incident correlation capabilities.
Innovation &amp; Continuous Improvement: Describe how you will drive continuous improvement, innovation backlog delivery, automation scaling, AIOps/Agentic AI integration, and enablement of internal teams.
Transition &amp; Onboarding: Detail your approach to onboarding, knowledge transfer, risk mitigation, and handover preparation from any incumbent vendors.
Offboarding &amp; Exit Readiness: Describe how knowledge, documentation, and tooling will be transitioned back to CCHBC or to a new provider at the end of the engagement.
Platform Enablement &amp; Self-Service: Describe how your team will support onboarding, self-service provisioning, reusable pipeline delivery, and shift-left enablement.
Commercial Proposal: Provide a clear pricing structure including fixed and variable elements, cost breakdown by service component, and any licensing or tooling assumptions.
References and Case Studies: Include at least three (3) references from similar enterprise engagements, ideally in FMCG or regulated industries, highlighting delivery scope, outcomes, and tooling used.
Team Qualifications and Certifications: Provide an overview of your proposed delivery team’s qualifications, including:
Cloud certifications: Microsoft Azure (e.g., AZ-104, AZ-305, AZ-400), Google Cloud (e.g., Professional Cloud Architect or DevOps Engineer)
FinOps certifications: FinOps Certified Practitioner or equivalent
Security and compliance certifications (e.g. Microsoft SC-series) for roles involved in DevOps and governance
Vendors should also clarify if certifications are held by named team members or available through internal capability pools.
Proposal Submission and Clarifications

Vendors may request clarification or schedule a short Q&amp;A session prior to submission.
Shortlisted vendors may be invited for a technical presentation or deep-dive review.
Submissions should be delivered in PDF or editable Word format by email.

