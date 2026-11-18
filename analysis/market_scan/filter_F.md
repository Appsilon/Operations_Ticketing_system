# Market scan filter – group F
Checked: 2026-11-18

## Summary
| Product | Q1 | Q2 | Q3 | Q4 | Result | Reason | Deployment | Starting price |
|---|---|---|---|---|---|---|---|---|
| Siit | No | Yes | Yes | Yes | Fail | Q1: vendor scopes the product to internal employee requests ("all internal operations"); customer support is only an escalation target in other tools (Freshdesk, Intercom etc.) | SaaS (AWS, EU – Ireland) | $23 per admin per month, billed annually (Essentials) |
| Atomicwork | No | Yes | Yes | Yes | Fail | Reviewer correction: Q1 was Partial. The vendor scopes the product to ITSM/ESM and its own article says "If your job is external customer support, run Zendesk". | SaaS (US or EU hosting) | From $25,000 per year, billed annually (Professional, up to 250 end users) |
| ConnectWise PSA | Unknown | Yes | Unknown | Unknown | Pass (flag) | connectwise.com, docs.connectwise.com and marketplace.connectwise.com blocked; internal use and EU region not confirmed; SOC 2 seen only on the Cyber Security Management trust profile | SaaS; "on-site" also named on an undated university page | Unknown (pricing page blocked) |
| Atera | Unknown | Yes | Unknown | Unknown | Pass (flag) | atera.com and support.atera.com blocked (Cloudflare); trust center lists hosting subprocessors in "United States" only, no EU statement found | SaaS (multi-tenant, Azure) | Unknown (pricing page blocked) |
| NinjaOne (Ticketing) | Yes | Yes | Yes | Yes | Pass | Vendor FAQ: ticketing used by internal IT teams and by MSPs for client support; IT-focused; Slack is a notification channel only | SaaS (AWS, region chosen by customer) | Not public |
| SuperOps | Partial | Yes | Yes | Yes | Pass | Q1 Partial: internal service desk in the "for IT teams" plan; client support in the separate MSP PSA edition (separate pricing tabs) | SaaS (AWS, US or Europe chosen at sign-up) | Not public (quote, billed per endpoint per month) |

## Siit
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | No | "Can Siit be used for teams beyond IT? Yes, Siit supports all internal operations, including HR, Finance, Legal, Facilities, and more. Any team that handles employee requests in Slack or Teams can use Siit." Docs: "The Freshdesk integration is the right choice when customer support teams already manage their work in Freshdesk." | https://www.siit.io/pricing ; https://docs.siit.io/llms.txt |
| Q2 | Yes | "Soc 2 Type II Attested Independent auditor attestation covering Security, Availability and Confidentiality." | https://www.siit.io/pricing ; https://www.siit.io/security (trust.siit.io returned 403) |
| Q3 | Yes | "The Siit Platform is hosted by Amazon Web Services in the European Union (Ireland)." | https://www.siit.io/privacy-policy |
| Q4 | Yes | "Slack Bot Collect and respond to support requests directly in Slack." | https://www.siit.io/pricing |

## Atomicwork
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | No (reviewer correction: was "Partial") | "Atomicwork is the AI-native ITSM and ESM platform"; email from non-trusted domains: "Choose Add as Guest to keep external conversations going"; vendor article: "If your job is external customer support, run Zendesk, or at least put it on the shortlist." | https://www.atomicwork.com/ ; https://www.atomicwork.com/product-announcements ; https://www.atomicwork.com/atomicnotes/zendesk-is-not-an-itsm-tool |
| Q2 | Yes | "SOC 2 Type II SECURITY ISO 42001 AI MANAGEMENT ISO 27001 SECURITY" | https://www.atomicwork.com/security |
| Q3 | Yes | "Data can be hosted in the EU or the US." (pricing also lists "Custom data residency" under Business Plus) | https://www.atomicwork.com/security ; https://www.atomicwork.com/pricing |
| Q4 | Yes | "Integrate with Okta, Slack, Workday, GitHub, Salesforce, Microsoft Entra and 100+ other apps." | https://www.atomicwork.com/ |

## ConnectWise PSA
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Unknown | Product pages blocked (Cloudflare "Just a moment..."). Only accessible official page: "Keeping your data (and your clients' data) safe and secure is our top priority." Internal employee use not found. | https://www.connectwise.com/platform/psa (blocked) ; https://university.connectwise.com/content/landing/cloud/connectwise-cloud.html |
| Q2 | Yes | "Audits and Certifications ... SOC 2 1 Document"; listed file: "ConnectWise - Security Services - 2024 - SOC 2 Type II - Report - Final.pdf" (Cyber Security Management profile; PSA scope not shown) | https://trust.connectwise.com/ConnectWise_Cyber_Security_Management_Profile ; https://connectwise.com/company/trust/compliance (blocked) |
| Q3 | Unknown | "ConnectWise Clouds are hosted at regional facilities on four continents" (no EU region named; undated page); "we designed ConnectWise to be used on-site or accessed as a SAAS solution" | https://university.connectwise.com/content/landing/cloud/connectwise-cloud.html |
| Q4 | Unknown | Marketplace listings blocked (Cloudflare). | https://marketplace.connectwise.com/slack (blocked) ; https://marketplace.connectwise.com/thread (blocked) |

## Atera
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Unknown | Product and help-center pages blocked (Cloudflare "Attention Required!" / "Just a moment..."). No evidence found. | https://www.atera.com/ (blocked) ; https://support.atera.com/ (blocked) |
| Q2 | Yes | "Compliance ISO/IEC 42001:2023 ISO 27001:2022 ... SOC 2 Type II" | https://trust.atera.com/ |
| Q3 | Unknown | "Microsoft Corporation (Azure) • Cloud service provider, cloud hosting, AI services, and content delivery network United States" – no EU hosting statement found; hosting article and privacy policy blocked | https://trust.atera.com/subprocessors ; https://support.atera.com/hc/en-us/articles/205116768-Where-are-the-cloud-servers-placed (blocked) |
| Q4 | Unknown | Pages blocked; no evidence found. | https://www.atera.com/ (blocked) |

## NinjaOne (Ticketing)
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Yes | "Is NinjaOne Ticketing suitable for internal IT teams or MSPs? Both. Internal IT teams use it to move off email chains and shared inboxes, while MSPs use it to manage client support requests natively" | https://www.ninjaone.com/ticketing/ (FAQ) |
| Q2 | Yes | "FedRAMP Moderate Rev 5 SOC 2 GovRAMP ISO 27001 GDPR HIPAA" | https://www.ninjaone.com/pricing/ |
| Q3 | Yes | "Data is stored within AWS in the region you choose."; subprocessor: "Amazon Web Services Cloud Infrastructure/Hosting USA, Canada, Germany, Australia" | https://trustpage.ninjaone.com/controls/ ; https://trustpage.ninjaone.com/subprocessors/ |
| Q4 | Yes | "push these alerts to designated Slack channels, email addresses, phone numbers, or webhook applications" (notifications only) | https://www.ninjaone.com/docs/new-to-ninjaone/alerting-and-notifications/endpoint-notification-channels-alerts/ |

## SuperOps
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | "FOR IT TEAMS ... Built-in ticketing, service desk, and knowledge base"; MSP edition: "With PSA, RMM, and MDM in one platform, run your MSP" / "The full client lifecycle, on one platform" | https://superops.com/pricing ; https://superops.com/msp |
| Q2 | Yes | "with SOC II Type 2, GDPR, ISO 27001, and HIPAA compliance" | https://superops.com/security |
| Q3 | Yes | "The data hosting locations available at the time of sign-up are (i) United States (ii) Europe." | https://superops.com/data-hosting-policy |
| Q4 | Yes | "employees can raise support requests by sending a direct message to the SuperOps app in Slack" | https://support.superops.com/it/en/articles/14032595-integrating-slack-with-superops |

## Reviewer check (2026-11-18)
1. Corrected Atomicwork Q1 from "Partial" to "No" and the result from "Pass" to "Fail": the vendor describes "the AI-native ITSM and ESM platform" and its own article says "If your job is external customer support, run Zendesk, or at least put it on the shortlist". "Add as Guest" covers external conversations, not client support. Same rule as Siit here and Pylon, Plain and Thena in group E.
2. ConnectWise PSA and Atera pass only with a flag because their sites were blocked (Cloudflare/403); most answers are Unknown.
