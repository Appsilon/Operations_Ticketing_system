# Market scan filter – group A
Checked: 2026-11-18

## Summary
| Product | Q1 | Q2 | Q3 | Q4 | Result | Reason | Deployment | Starting price |
|---|---|---|---|---|---|---|---|---|
| BMC Helix ITSM | Partial | Yes | Yes | Yes | Pass | Q1: external client support needs a second product, BMC Helix Customer Service Management. Vendor is now HelixOps, Inc. (bmc.com redirects to helixops.ai) | SaaS confirmed; on-premises not confirmed on pages checked | Not public ("Request Pricing") |
| Ivanti Neurons for ITSM | Partial | Yes | Partial | Yes | Pass | Q1: "Customer Service Management" appears only as a plan line item, with no description. Q3: EU only confirmed through self-hosting | Both (cloud, on-premises, hybrid) | Not public |
| OpenText Service Management | Unknown | Partial | Partial | Yes | Pass (flag) | Q1: no vendor statement on external client support found. Q3: EU-only hosting requires the purchased "EU Managed Service", or self-hosting | Both (SaaS, on-premises, own cloud) | Not public |
| SymphonyAI Summit (now SummitAI) | Unknown | Yes | Unknown | Unknown | Pass (flag) | Q1: pages describe employee/IT support only, with no external-client statement. Q3: no EU region stated. Product moved to SummitAI, an independent company | SaaS confirmed; on-premises not confirmed | Not public |
| IFS assyst | Unknown | Unknown | Unknown | Unknown | Pass (flag) | All IFS pages blocked (Vercel Security Checkpoint, HTTP 429). User needs to supply the page content | Unknown (blocked) | Unknown (blocked) |
| Microsoft System Center Service Manager | No | Partial | Partial | Unknown | Fail | Q1: vendor scopes the product to "your organization's IT service management", with no external client support | Self-hosted only | System Center 2025 Standard MSRP $1,455 (suite licence, 16-core 2-processor server) |

## BMC Helix ITSM
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | ITSM: "BMC Helix ITSM enables you to create world-class, omni-channel service experiences for your users". External customers are handled by a separate product: "BMC Helix Customer Service Management … Revolutionize customer service with enterprise-grade agentic AI to deliver customer service excellence and 360-degree customer intelligence." | https://www.bmc.com/it-solutions/bmc-helix-itsm.html ; https://www.helixops.ai/products/bmc-helix-customer-service-management.html |
| Q2 | Yes | "ISO 27001:2022 International standard used by BMC Helix to effectively establish, implement, maintain, and continually improve its information security management system (ISMS). Download: ISO 27001:2022 BMC Helix". The page also lists SOC 2. Caveat on the trust center: "Certification scope and applicability may vary by service and region." | https://www.helixops.ai/about/trust-center/compliance.html ; https://www.helixops.ai/about/trust-center.html |
| Q3 | Yes | "Service Location European Union Amsterdam, Netherlands BMC Helix Client Management BMC Helix ITSM …" and "Service Location European Union Frankfurt, Germany BMC Helix ITSM" | https://docs.helixops.ai/xwiki/bin/view/Helix-Common-Services/Other/BMC-Helix-Subscriber-Information/helixsubscriber/Operations/Data-centers-and-architecture/Service-locations/ |
| Q4 | Yes | Both are vendor add-ons. Chatbot channel: "You can use Slack as a communication channel in BMC Helix Virtual Agent chatbot applications." Ticket notifications: "Automatically generate posts in Slack when an incident is created or updated in BMC Helix ITSM. … Requires a BMC Helix iPaaS Jitterbit subscription" | https://www.helixops.ai/marketplace/bmc-helix/slack-integration-for-bmc-helix-virtual-agent.html ; https://www.helixops.ai/marketplace/bmc-helix/post-incident-work-notes-in-slack.html |

## Ivanti Neurons for ITSM
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | Internal use: "Transform the employee experience across the entire organization". External: the plan table lists "Customer Service Management ✓ ✓" for Ivanti ITSM and ITSM Premium. No description of this module was found on the pages checked | https://www.ivanti.com/products/ivanti-neurons-itsm ; https://www.ivanti.com/service-management |
| Q2 | Yes | "We conform to the most stringent compliance frameworks. Certifications Service Organization Control 2 (SOC2) ISO/IEC …" | https://www.ivanti.com/resources/security-compliance |
| Q3 | Partial | Self-hosting: "Deploy in the cloud, on-premises, or through a hybrid setup for maximum flexibility." Vendor-hosted EU region for ITSM not confirmed: the subprocessor list shows "Australia, Canada, Germany, Ireland, Japan, Singapore, United Kingdom, United States Microsoft Azure services including providing infrastructure and data hosting", but the rendered text does not link that row to a product | https://www.ivanti.com/products/ivanti-neurons-itsm ; https://www.ivanti.com/company/legal/ivanti-subprocessors |
| Q4 | Yes | Listing published by Ivanti; requires the Neurons iPaaS add-on: "Ivanti Neurons iPaaS pre-built recipe for integrating Neurons for ITSM with Slack." | https://marketplace.ivanti.com/xchange/64b5b48e2ee9d6e08c3e6724/solution/664367c67e306ab10d4512c1 |

## OpenText Service Management
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Unknown | Only internal use is documented: "A single, user-friendly service portal or mobile app gives employees easy access to both IT and non-IT services." No statement on support for external clients was found on the product page, the product overview or the service description | https://www.opentext.com/media/product-overview/opentext-service-management-po-en.pdf ; https://www.opentext.com/products/service-management |
| Q2 | Yes | "OpenText maintains an Information Security Management System designed to comply with recognized industry standards such as ISO/IEC 27001 and undergoes periodic audits, including SOC 2 Type II assessments for applicable services." Whether Service Management is one of the "applicable services" is not stated | https://www.opentext.com/en/media/documentation/technical-and-organizational-measures-documentation-en.pdf |
| Q3 | Partial | "Customers who purchased the EU Managed Service will have their OTSM/OTAM Tenant deployed within a dedicated EU Managed infrastructure located within the EU" (service description, July 2026). Self-hosting: "runs on premises, in the cloud (with AWS, Microsoft Azure, or Google Cloud), or as SaaS in the OpenText public cloud." The Express plan lists "Multi-region data residency" but does not name the regions | https://www.opentext.com/media/documentation/opentext-service-management-and-asset-management-service-description-documentation-en.pdf ; https://www.opentext.com/media/product-overview/opentext-service-management-po-en.pdf |
| Q4 | Yes | "Below are popular out-of-the-box integrations. … Slack" | https://www.opentext.com/products/service-management |

## SymphonyAI Summit (now SummitAI)
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Unknown | Pages describe employee support only: "Available 24/7 wherever your employees work" and "Agentic AI for Employee Services". No statement on support for external clients was found. Status: "SymphonyAI's Enterprise IT business, including its IT service management (ITSM) … is now SummitAI, an independent company." | https://summitai.com/itsm/it-service-management ; https://summitai.com/itsm/agentic-ai ; https://www.symphonyai.com/retail-cpg/apex-platform |
| Q2 | Yes | "Our commitment to security is evidenced through third-party compliance, certifications and reports across our products, such as ISO/IEC 27001, ISO/IEC 277001, SOC2, CSA STAR" | https://summitai.com/security-trust/ |
| Q3 | Unknown | The page says only "SummitAI Managed Cloud Platform (Hosting Center for SummitAI Customer SAAS instances)", plus generic Microsoft Azure text. No EU region and no self-hosting option are stated | https://summitai.com/security-trust/ |
| Q4 | Unknown | Integration Hub says only "Integration with 100+ tools". Slack is not named on the integration, ITSM or platform pages checked | https://summitai.com/itsm/integration-hub |

## IFS assyst
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Unknown | Blocked: "Failed to verify your browser Code 21 Vercel Security Checkpoint" (HTTP 429, retried several times) | https://www.ifs.com/assyst ; https://assyst.ifs.com/ ; https://www.ifs.com/en/products/esm |
| Q2 | Unknown | Blocked: "Vercel Security Checkpoint" (HTTP 429) on the trust center and on the ISO certificate PDF | https://www.ifs.com/en/about/trust-center ; https://IFSworld.com/-/media10/project/ifs/ifs/assets/trust-center/iso_27001_2022_ifs_is_725861_exp_2026_10_17.pdf |
| Q3 | Unknown | Blocked (same checkpoint) | https://www.ifs.com/en/about/trust-center |
| Q4 | Unknown | Blocked (same checkpoint) | https://assyst.ifs.com/ |

## Microsoft System Center Service Manager
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | No | "provides an integrated platform for automating and adapting your organization's IT service management best practices" and "manage service desk functions for your organization's computer infrastructure" | https://learn.microsoft.com/en-us/system-center/scsm/service-manager?view=sc-sm-2025 |
| Q2 | Yes | "Microsoft's achievement of ISO/IEC 27001 certification points up its commitment …". Scope is "Microsoft in-scope cloud platforms and services". System Center is not in that list, and Service Manager is self-hosted | https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001 |
| Q3 | Partial | Self-hosting only: "The scenarios range from a simple, one-computer scenario to a four-computer scenario that is designed to support production-type environments." | https://learn.microsoft.com/en-us/system-center/scsm/deploy-sm?view=sc-sm-2025 |
| Q4 | Unknown | No Slack integration found in the Service Manager documentation pages checked | https://learn.microsoft.com/en-us/system-center/scsm/ |

## Reviewer check (2026-11-18)
1. Corrected Q2 from "Yes" to "Partial" in the summary for OpenText (SOC 2 covers "applicable services" without naming Service Management) and Microsoft System Center Service Manager (ISO 27001 covers Microsoft cloud services; System Center is not listed). Results unchanged: OpenText Pass (flag) because Q1 is Unknown; Microsoft Fail on Q1.
2. Q4 Yes for BMC and Ivanti relies on the vendors' own paid integration add-ons (BMC Helix iPaaS / Virtual Agent, Ivanti Neurons iPaaS); the cost is not included.
3. IFS assyst passes with a flag only because every IFS page was blocked (Vercel Security Checkpoint, HTTP 429). Its content would have to be provided by the user.
