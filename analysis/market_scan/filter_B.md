# Market scan filter – group B
Checked: 2026-11-18

## Summary
| Product | Q1 | Q2 | Q3 | Q4 | Result | Reason | Deployment | Starting price |
|---|---|---|---|---|---|---|---|---|
| ManageEngine ServiceDesk Plus (incl. MSP edition) | Partial | Yes | Yes | Yes | Pass | External clients are served by a separate edition, ServiceDesk Plus MSP. ServiceDesk Plus itself documents IT and ESM use. | Both (cloud and on-premises) | Cloud Standard: from US$13 per technician per month. The page has a monthly/yearly toggle, and which one the shown price uses was not confirmed. |
| InvGate Service Management | Partial | Yes | Partial | Yes | Pass | External-customer use is mentioned in one sentence only. Data residency options and on-premise hosting are listed for Enterprise only, and no EU region is named. | Both (on-premise in Enterprise only) | Starter $1,499 per year fixed (5 agents). Pro $500 per agent per year (from $2,500 per year). |
| SysAid | Unknown | Yes | Yes | Partial | Pass (flag) | The official pages checked describe only employee (internal) service. No use for external clients was found. | SaaS (no self-hosted option seen on the pages checked) | Page title: "From $89 per Agent per Month". The page shows Professional at $59 per agent per month for 70 agents, billed annually. |
| Xurrent (formerly 4me) | Partial | Yes | Yes | Yes | Pass | ESM (internal) and MSP (multi-client) run on the same platform but are sold as separate license plans (Corporate IT vs MSP). | SaaS | Not public |
| EasyVista (EV Service Manager) | Unknown | Partial | Yes | Yes | Pass (flag) | No external-client support was found on the pages checked. The French ESM page was blocked (403). SOC 2 is named only on a marketing page. The SaaS documentation attributes ISO 27001 and SOC 2 to the hosting providers. | Both (SaaS and on-premises) | Not public |

## ManageEngine ServiceDesk Plus (incl. MSP edition)
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | Internal: "combines IT service management, IT asset management, and CMDB with enterprise service management capabilities for departments including HR, facilities, and finance". External needs the separate MSP edition: "ServiceDesk Plus MSP is a unified platform designed for MSPs" and "Multi-tenancy for personalized service delivery to customers". | https://www.manageengine.com/products/service-desk/ ; https://www.manageengine.com/products/service-desk-msp/ |
| Q2 | Yes | "ManageEngine has earned ISO/IEC 27001 certification ... Applicable to: All cloud services and on-premise products of ManageEngine." "ManageEngine is SOC 2 Type II compliant." | https://www.manageengine.com/compliance.html |
| Q3 | Yes | "EUROPE Amsterdam Amsterdam, Netherlands Facility role: Primary datacenter" and "EUROPE Dublin Dublin, Ireland Facility role: Secondary datacenter". Also: "Available both on-premises and in the cloud". | https://www.manageengine.com/know-your-datacenter.html ; https://www.manageengine.com/products/service-desk/ |
| Q4 | Yes | "Slack Availability: Natively and in the Marketplace Carry out service desk operations within Slack". Release notes, ServiceDesk Plus Cloud, 2026-07-31: "Slack integration is now available for all data centers, except the UAE, INEC, and CN data centers." On-premises Slack support is not stated. | https://www.manageengine.com/products/service-desk/integrations/ ; https://www.manageengine.com/products/service-desk/cloud/whats-new.html |

## InvGate Service Management
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | Internal: "extend them to other teams, such as Human Resources, Legal, Facilities and Finance". External is mentioned only briefly: "Meeting employees and customers where they already are is key to building a support experience that actually works." No external-client setup is described. | https://invgate.com/solutions/esm ; https://invgate.com/service-management/product-tour/omnichannel-support |
| Q2 | Yes | "InvGate is certified under ISO 27001:2022" and "SOC 2 Type II Security Controls". | https://invgate.com/security |
| Q3 | Partial | Enterprise only. "Data residency options Special services and data hosting for country-specific requirements. Not included Not included Available". "On-premise deployment Host and manage the platform entirely within your own infrastructure ... Not included Not included Available". No EU region is named. trust.invgate.com returned no readable text. | https://invgate.com/pricing?p=serviceManagement |
| Q4 | Yes | "InvGate Service Management now integrates natively with Slack." | https://invgate.com/integrations/slack |

## SysAid
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Unknown | Internal: "One platform runs service for every department — IT, HR, Finance, Facilities, Legal, and beyond." and "Employees have one place to ask for help." No external-client use was found. https://www.sysaid.com/service-center now shows the homepage. | https://www.sysaid.com/enterprise-service-management ; https://www.sysaid.com/ |
| Q2 | Yes | "SysAid Cloud is under an ISO 27001-certified ISMS, with ISO 27017 and 27018 certification, annual SOC 2 Type II examination". | https://www.sysaid.com/support/sysaid-documentation/data-security (page title "Trust Center - SysAid") |
| Q3 | Yes | "if you are located in the European Union, your data will be stored in an AWS data center in the EU." | https://www.sysaid.com/support/sysaid-documentation/data-storage-location |
| Q4 | Partial | Slack is listed only through embedded Workato, a third-party integration platform: "SLACK Connect SysAid with Slack Via our embedded Workato offering". Pre-built AI agents for Slack are also listed, for example: "SLACK – ITSM CASE EXTRACTION AGENT ... creating service records in SysAid". | https://www.sysaid.com/service-management/integrations |

## Xurrent (formerly 4me)
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | Internal: "Xurrent Enterprise Service Management (ESM) unifies IT, HR, Facilities, Finance, and more". External: "Multi-Tenant Client Management Securely manage multiple client environments from a single platform". The two are separate license plans: "Corporate IT License Plans MSP License Plans". | https://www.xurrent.com/use-cases/enterprise-service-management ; https://www.xurrent.com/solutions/managed-service-providers ; https://www.xurrent.com/pricing/it-service-management |
| Q2 | Yes | "Our ISO 27001 and ISO 27018 certifications confirm..." and "Customers can request Xurrent's latest SOC 2 Type 2 report". | https://www.xurrent.com/security |
| Q3 | Yes | "All customer data uploaded to the Xurrent services is always stored within the region selected by the customer, for example the European Economic Area (EEA)." | https://www.xurrent.com/security |
| Q4 | Yes | "A new native Slack Connector brings Slack into Xurrent iPaaS as a first-class integration". | https://www.xurrent.com/product-updates/xurrent-itsm-july-2026-product-updates |

## EasyVista (EV Service Manager)
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Unknown | Internal: "HR SELF-SERVICE FOR EMPLOYEE SUPPORT Empower employees to find answers to common HR questions". The product page scopes EV Service Manager to "IT service operations". No external-client ticketing was found. The French ESM page was blocked (NinjaFirewall 403). | https://www.easyvista.com/products/self-service-software/ ; https://www.easyvista.com/products/it-service-management-software/ ; blocked: https://www.easyvista.com/fr/solution-de-gestion-des-services-entreprise |
| Q2 | Partial (reviewer correction: was "Yes"; the marketing page and the SaaS documentation disagree on whether EasyVista or only its hosting providers hold SOC 2 / ISO 27001) | The marketing page says: "through our certifications and services. EasyVista's Standard of Security SSAE18 SOC2 GDPR & ISO 27018". The documentation attributes ISO 27001 and SOC 2 to the hosting providers only: "hosted by providers meeting the following standards: Tiers 3+ or 4. ISO 27001, SOC2 certifications." No ISO 27001 certificate of EasyVista itself was found. | https://info.easyvista.com/security-data-sheet ; https://docs.easyvista.com/docs/white-paper-service-manager-saas |
| Q3 | Yes | "hosting services of an EU customer will be located in EU". | https://www.easyvista.com/about/sub-contractors/ |
| Q4 | Yes | "SLACK Connect EasyVista with Slack to deliver IT service notifications, updates, and collaboration workflows directly into Slack channels." Creating requests from Slack is not stated. | https://www.easyvista.com/platform/platform-integrations/ |

## Reviewer check (2026-11-18)
1. Corrected EasyVista Q2 from "Yes" to "Partial": the marketing page lists "SSAE18 SOC2" among "our certifications", but the SaaS documentation attributes ISO 27001 and SOC 2 to the hosting providers. The result stays "Pass (flag)" because Q1 is Unknown.
2. SysAid and EasyVista pass only with a flag: support for external clients was not documented (Q1 Unknown). This is the first question to settle in the full assessment.
