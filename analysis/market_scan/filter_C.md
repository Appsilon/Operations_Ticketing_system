# Market scan filter – group C
Checked: 2026-11-18

## Summary
| Product | Q1 | Q2 | Q3 | Q4 | Result | Reason | Deployment | Starting price |
|---|---|---|---|---|---|---|---|---|
| Zammad | Yes | Yes | Yes | Partial | Pass | No "No" on Q1–Q3. Q4: Slack notifications only via generic webhook | Both (hosted in Germany; self-hosted open source) | €7/agent/month (Starter v2, hosted, max 5 agents, excl. VAT; billing period of the shown price not confirmed) |
| OTRS | Yes | Partial | Yes | Unknown | Pass | No "No" on Q1–Q3. Q2 Partial: OTRS states it holds no ISO 27001 or SOC 2; only its data-centre operators are certified | Both (on-premise; managed/cloud) | Not public ("Get a quote") |
| Znuny | Partial | Yes | Partial | Unknown | Pass | No "No" on Q1–Q3. Q1 Partial: external client support only briefly described. Q3 Partial: EU only proven via self-hosting; vendor-hosted location not stated | Both (self-hosted open source; hosted by Znuny) | Software free (open source); hosting from $799/month (Silver, paid annually, no per-user pricing) + 1,595 EUR one-time setup fee |
| GLPI (GLPI Network / Teclib) | Yes | No | Yes | Unknown | Fail | Q2 No: Teclib states it has only started preparing for ISO/IEC 27001 (audit scheduled 2027); no SOC 2 mentioned | Both (GLPI Network Cloud; self-hosted open source) | €19/user/month excl. VAT (GLPI Network Public Cloud) |
| Proactivanet | Unknown | Yes | Yes | Yes | Pass (flag) | Q1 Unknown: only internal use (IT, HR, Finance, General Services) found; no external client support use documented | Both (SaaS on AWS; On Premises) | Not public |

## Zammad
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Yes | Internal: "Zammad for IT Service Desk" … "Zammad gives your IT team structure, clarity, and full visibility" … customer story "ø 200 Internal Customers". External: "How Nextcloud Scales Customer Support with Zammad" | https://zammad.com/en/solutions/zammad-at-the-it-service-desk ; https://zammad.com/en/pricing |
| Q2 | Yes | "Berlin, June 18, 2026 – Zammad GmbH has been awarded ISO/IEC 27001:2022 certification." | https://zammad.com/en/company/press/zammad-gmbh-achieves-iso-iec-27001-2022-certification |
| Q3 | Yes | "With all Hosted rates, only data centres in Germany are used." Also: "secure and powerful on our servers in German data centers" (hosted); self-hosted option on pricing page | https://support.zammad.com/help/en-us/2-regular-subscriptions-hosted/108-where-is-my-data-and-how-is-it-protected ; https://zammad.com/en/pricing |
| Q4 | Partial | "Follow the steps below to configure a webhook for receiving Zammad notifications in a Slack channel." (uses Slack's "Incoming WebHooks" app; no Slack entry in the admin docs integrations list) | https://admin-docs.zammad.org/en/latest/manage/webhook/examples/slack-notifications.html ; https://admin-docs.zammad.org/en/latest/system/integrations/index.html |

## OTRS
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Yes | "Both external and internal customers are quickly and continuously informed about the status of their request." Solutions list: "Choose the solution that fits your use case or combine them on one platform." (Help Desk, Customer Service & Support, IT Service Management, Office Management, HR Management) | https://otrs.com/otrs-software-solutions/otrs/ ; https://otrs.com/otrs-software-solutions/customer-service-support/ |
| Q2 | Partial | "OTRS currently does not maintain ISO 27001 or SOC 2 certification." and "The respective datacenter operators maintain independent certifications and controls" (managed hosting: "Highest Infrastructure Standards: ISO 27001") | https://otrs.com/trust-center/ (text in the Compliance & Governance and Infrastructure tabs) ; https://otrs.com/otrs-software-solutions/otrs/otrs-on-premise-managed/ |
| Q3 | Yes | "By default, data is stored on servers in Germany (on request in USA or Canada) according to the latest GDPR standards." On-premise also offered | https://otrs.com/otrs-software-solutions/otrs/otrs-on-premise-managed/ |
| Q4 | Unknown | No Slack entry found in the integrations catalogue (pages 1–3) | https://otrs.com/integrations/ ; https://otrs.com/integrations/2/ ; https://otrs.com/integrations/3/ |

## Znuny
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | "Znuny is a flexible, open-source ITSM and service enterprise management tool". External use only briefly: "Your customers don’t communicate through a single channel — and your service desk shouldn’t either." Channels include "Customer self-service portal" | https://www.znuny.com/en/product ; https://www.znuny.com/en/product/features/channels |
| Q2 | Yes | "We are proud to have achieved SOC 2 certification since 2024 and ISO/IEC 27001:2022 certification since January 2025." | https://www.znuny.com/en/trust-compliance |
| Q3 | Partial | "Run Znuny on your server or have it hosted by us." Hosting page states only "Certified data centers"; no data-centre location found for vendor hosting | https://www.znuny.com/en/product ; https://www.znuny.com/en/services/hosting |
| Q4 | Unknown | No Slack entry found on add-ons or channels pages; channels page: "More channels like messenger, text messages can be added with add-ons." | https://www.znuny.com/en/product/add-ons ; https://www.znuny.com/en/product/features/channels |

## GLPI (GLPI Network / Teclib)
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Yes | Internal: "Align Your IT Services with ITIL Best Practices". MSP mode: "An outsourcing provider can also use it to manage its clients' information systems, thanks to entities." … "each client's access can be limited to its own data." | https://www.glpi-project.org/en/helpdesk-software/ ; https://www.glpi-project.org/en/it-outsourcing/ |
| Q2 | No | "Teclib’ has started preparing for ISO/IEC 27001:2022 certification." … "The certification audit is scheduled for 2027." SOC 2 not mentioned on security policy or pricing pages | https://www.glpi-project.org/en/teclib-iso-27001-certification/ ; https://www.glpi-project.org/en/security-policy/ |
| Q3 | Yes | "The computer server hosting company, OVH. These servers are hosted in Europe (France)." Pricing: "Hosting providers: OVHCloud (primary data) · Acronis France/Strasbourg (system backups) · Scaleway France/Paris (archiving)" | https://www.glpi-project.org/en/security-policy/ ; https://www.glpi-project.org/en/pricing/ |
| Q4 | Unknown | No Slack entry found on integrations page; only "Webhook (Plugin Collaborative Tools) Keep an eye on GLPI events and be warned in real time" | https://www.glpi-project.org/en/integration/ |

## Proactivanet
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Unknown | Internal only: "modernization of processes in the areas of IT Services, HR, Finance and General Services" (customer story teaser). Positioned as "IT Service Management Software (ITSM)"; no external client support use found on ITSM or Service Desk pages | https://www.proactivanet.com/en/ ; https://www.proactivanet.com/en/it-service-management-itsm/ ; https://www.proactivanet.com/en/service-desk/ |
| Q2 | Yes | "Proactivanet is certified in ISO 9001, ISO 20000, ISO 27001 and ISO 27017" | https://www.proactivanet.com/en/official-certifications/ |
| Q3 | Yes | (ES, general terms) "El Proveedor garantiza que los datos personales del Cliente serán alojados dentro de la Unión Europea" (SaaS runs on "Servicios de Infraestructura Cloud Computing – AWS"; On Premises also offered) | https://www.proactivanet.com/condiciones-generales-de-contratacion/ |
| Q4 | Yes | "Integration with MS Teams, Telegram, Whatsapp and Slack." | https://www.proactivanet.com/en/service-desk/ |

## Reviewer check (2026-11-18)
1. Re-checked: "Zammad GmbH has been awarded ISO/IEC 27001:2022 certification" (Zammad press release, 2026-06-18).
2. Re-checked: Teclib "started preparing for ISO/IEC 27001:2022 certification" and "The certification audit is scheduled for 2027", so GLPI Q2 = No and the Fail stands.
3. otrs.com and proactivanet.com showed a "One moment, please..." check that cleared by waiting, with no clicking or spoofing. This is not treated as circumventing a block.
4. OTRS passes with Q2 Partial: its trust centre says it "currently does not maintain ISO 27001 or SOC 2 certification" (only data-centre operators are certified). That is likely to fail K.O. #26 in the full assessment (Notes #13: "Immature vendors without certifications are out").
