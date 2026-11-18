# Market scan filter – group D
Checked: 2026-11-18

## Summary
| Product | Q1 | Q2 | Q3 | Q4 | Result | Reason | Deployment | Starting price |
|---|---|---|---|---|---|---|---|---|
| HelpSpot | Yes | Partial | Yes | Partial | Pass | SOC 2 "in progress"; only AWS hosting is certified. Slack only via Zapier | Both (US Cloud, EU Cloud, self-hosted) | $2,199/year for 10 agents ($18.33/agent/month), sold annually (calculator default; tiers from 3 agents, price for 3 not shown) |
| Hesk (Hesk Cloud) | Partial | Unknown | Yes | No | Pass (flag) | Q2 Unknown: no ISO 27001/SOC 2 statement found. Internal use mentioned only briefly with limits. No integrations (Slack) | Both (free self-hosted, Hesk Cloud) | Self-hosted: free download. Hesk Cloud: $299/year (10 agents) |
| HelpSpace | No | Partial | Yes | Yes | Fail | Q1: vendor describes the product as client/customer service software; no internal employee use found | SaaS (no self-hosted option found) | $12/user/month (Starter, from 2 users, Annual/Monthly toggle, excl. VAT) |
| Deskpro | Yes | Yes | Yes | Yes | Pass | All four documented | Both (Deskpro Cloud, Deskpro Private self-hosted) | $39/agent/month (Team, min 5 agents; billing period not stated) |
| Intercom | Partial | Yes | Partial | Yes | Pass | Internal IT use documented with stated limits ("not a traditional ITSM platform"). EU hosting only for new workspaces on Advanced/Expert plans, on contract | SaaS (no self-hosted option found) | $29/seat/month Essential, USD (page structured data); EU hosting needs Advanced ($99/seat/month) or Expert; Fin AI Agent $0.99 per outcome |
| Crisp | Partial | No | Yes | Yes | Fail | Q2: vendor states no SOC 2 audit; ISO 27001 only "committed to aligning" (no certificate claimed) | SaaS (no self-hosted option found) | Free plan (2 seats); Mini $45/month per workspace (4 seats) |
| Userlike (now Lime Connect) | No | Yes | Yes | Yes | Fail | Q1: vendor scopes product to customer communication (sales and support); no internal employee use found | SaaS (hosted in Germany) | Free 0 €/month (1 seat); Pro from 87 €/month (min 3 seats), excl. VAT |

## HelpSpot
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Yes | "Whether you're supporting employees or customers, HelpSpot adapts to your unique workflow INTERNAL SUPPORT IT Service Desk … HR Service Desk … CUSTOMER SUPPORT B2B Customer Support" | https://www.helpspot.com/ |
| Q2 | Partial | "Our SOC 2 work is in progress. We have not completed our SOC 2 examination. The AWS reports described below apply to our hosting infrastructure, not to a completed HelpSpot examination." | https://www.helpspot.com/security (page "Last updated: September 29, 2026") |
| Q3 | Yes | "Hosted on dedicated servers in AWS Frankfurt with full GDPR compliance at no extra cost. All data stays in the EU at all times." Self-hosted also offered. | https://www.helpspot.com/hosting/eu-cloud |
| Q4 | Partial | "Zapier 5,000+ app connections with zero code. Slack, Teams, Salesforce, Google Sheets, and thousands more." | https://www.helpspot.com/platform/developer |

## Hesk (Hesk Cloud)
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | "Internal IT or operations desk Hesk covers many straightforward internal desks. Zendesk Employee Service may be better when asset management, service catalog, approvals …" Customer use: "Look closely at Hesk when support is mainly handled through email and web tickets." | https://www.hesk.com/compare/zendesk-vs-hesk.php; https://www.hesk.com/compare/ |
| Q2 | Unknown | No ISO 27001 or SOC 2 statement found. Pages checked: Hesk Cloud, EU hosting page ("GDPR-compliant provider"), subprocessor list (Linode/Akamai, AWS). | https://www.hesk.com/eu-hosted-help-desk.php; https://www.hesk.com/knowledgebase/?article=106 |
| Q3 | Yes | "Frankfurt, Germany Choose the EU region when starting Hesk Cloud. Tickets and attachments hosted in the EU" | https://www.hesk.com/eu-hosted-help-desk.php |
| Q4 | No | "Unfortunately no, HESK doesn't integrate directly with other software. HESK was developed to be a stand-alone help desk application." | https://www.hesk.com/knowledgebase/index.php?article=38 |

## HelpSpace
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | No | "HelpSpace is a comprehensive client service solution both you and your clients will cherish!"; "an intuitive help desk solution that organizes customer inquiries". No internal employee use case found on pages checked. | https://helpspace.com/security; https://helpspace.com/ |
| Q2 | Partial | "ISO 27001 The data centers are ISO 27001 certified" | https://helpspace.com/security |
| Q3 | Yes | "All data in HelpSpace is hosted exclusively in data centers within the European Union." | https://helpspace.com/security |
| Q4 | Yes | "Slack Get instant alerts for new customer messages and stay up to date in one place." | https://helpspace.com/integrations |

## Deskpro
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Yes | "Every customer or employee request becomes a ticket your team can route, track, and report on." Solutions: "B2B customer support HR support Internal operations IT help desk" | https://www.deskpro.com/cloud-based-help-desk; https://www.deskpro.com/ |
| Q2 | Yes | "Compliance certifications and regulations ISO 27001 … SOC 2 Type II" | https://www.deskpro.com/security |
| Q3 | Yes | "Deskpro offers deployment of Cloud accounts onto data centers located in either the US, EU or UK. Customers can choose which region they wish to exclusively host their data in, as standard." | https://www.deskpro.com/security |
| Q4 | Yes | "Submit support requests directly from Slack with a simple command." | https://www.deskpro.com/product/slack |

## Intercom
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | "Intercom was built for customer-facing support, but the same principles apply to internal IT help desks" … "Intercom is not a traditional ITSM platform. It does not include asset management, CMDB, or change management modules." | https://www.intercom.com/learning-center/what-is-it-help-desk (dated September 25, 2026) |
| Q2 | Yes | "Intercom and Fin hold SOC 2 Type II and HIPAA compliance along with ISO 27001, ISO 27018, ISO 27701, and ISO 42001 certification" | https://www.intercom.com/security |
| Q3 | Partial | "Regional Data Hosting is only available to new workspaces on the Advanced and Expert plans and is not available through the Early Stage program." "Our EU data center is located in … eu-west-1 AWS Region (Dublin, Ireland)." | https://www.intercom.com/help/en/articles/6124430-regional-data-hosting |
| Q4 | Yes | "For organizations using Slack internally, Fin operates directly inside Slack channels as a support agent." | https://www.intercom.com/learning-center/what-is-it-help-desk |

## Crisp
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | Product: "The one complete suite for AI-first customer support". Internal use only as a knowledge base: "Empower employee knowledge with a private help center". No internal request handling found. | https://crisp.chat/en/; https://crisp.chat/en/knowledge/internal-knowledge-base/ |
| Q2 | No | "Crisp hasn't been over any SOC2 audit"; "Crisp is committed to aligning with ISO 27001 standards" (no certification claimed) | https://help.crisp.chat/en/article/crisp-compliance-status-with-soc2-1xet2vz/; https://help.crisp.chat/en/article/crisp-compliance-with-iso-27001-10e05uc/ (updated 28/10/2026) |
| Q3 | Yes | "Messaging servers are hosted in … The Netherlands Plugin servers are hosted in … Germany" | https://docs.crisp.chat/guides/others/security-practices/ |
| Q4 | Yes | "Slack Reply to incoming messages from Slack" | https://crisp.chat/en/integrations/ |

## Userlike (now Lime Connect)
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | No | Page title: "AI customer communication for sales & support – Lime Connect (ex Userlike)"; "Automate customer service end-to-end with AI agents across chat, email, WhatsApp and more." No internal employee use case found. | https://www.userlike.com/en/ |
| Q2 | Yes | "Lime Connect is ISO27001 certified, ensuring enterprise-grade information security, risk mitigation and data protection at every level." | https://www.userlike.com/en/ |
| Q3 | Yes | "All chat data is securely stored on servers within Germany." | https://connect.lime-technologies.com/en/products/data-privacy/ |
| Q4 | Yes | "Subscribe to a set of events for which you receive Lime Connect notifications in a dedicated Slack channel." | https://connect.lime-technologies.com/en/integrations/ |

## Reviewer check (2026-11-18)
1. Re-checked: Deskpro security page lists "ISO 27001" and "SOC 2 Type II" under compliance certifications (https://www.deskpro.com/security).
2. Re-checked: "Crisp hasn't been over any SOC2 audit" (Crisp help centre), so Q2 = No and the Fail stands.
3. HelpSpace and Userlike Q1 = No rests on the vendors' own scoping of the product to client/customer communication (rule 2 of the method). Neither vendor says internal use is impossible. The same rule was applied to Pylon, Plain and Thena in group E.
