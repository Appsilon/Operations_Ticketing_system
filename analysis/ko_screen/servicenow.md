# ServiceNow – K.O. screen
1. Products evaluated: ServiceNow **ITSM** (packages Foundation / Advanced / Prime) and **CSM** (Customer Service Management; "CSM Advanced" plus a second package whose name is not visible in the capture), both on the ServiceNow AI Platform.
2. Checked: 2026-11-18. Sources are official ServiceNow pages captured as PDF by the user on 2026-11-18 (servicenow.com blocks automated browsing):
   1. `Servicenow1.pdf`: https://www.servicenow.com/products/itsm/pricing.html (printed 11/18/26, 3:28 PM)
   2. `Servicenow2.pdf`: https://www.servicenow.com/au/products/customer-service-management/pricing.html (printed 11/18/26, 3:29 PM)
   3. `Servicenow3.pdf`: https://www.servicenow.com/company/trust/compliance.html (printed 11/18/26, 3:35 PM)
   4. `wp-spp_european_union.pdf`: white paper "ServiceNow Protected Platform for the European Union (SPP EU)", dated September 3, 2026, version "SPP for the EU_v4.3"
3. Summary: Meets 1 / Partial 4 / Does not meet 0 / Unknown 11 (of 16). **The 11 Unknowns mean "no evidence in the pages available", not "missing feature".** Feature documentation could not be read (see "Access").

## Single tool for internal + external?
1. ITSM (internal IT) and CSM (external customers) are **separate packages with separate pricing pages** on one platform. So ServiceNow is two licensed products, not one.
2. Whether both run in one instance, and whether ITSM alone can serve external clients, is not documented in the pages available.
3. The ITSM grid lists "ServiceNow EmployeeWorks" in all packages; its scope (for example HR or Finance requests) is not described in the pages available.

## K.O. criteria
| # | Requirement | Verdict | Lowest plan | Evidence (verbatim, short) | Source |
|---|---|---|---|---|---|
| 1 | Email-based ticket handling | Unknown | – | Not documented in the pages available. (The white paper mentions "inbound emails to customers' instances" only in a data-scope context.) | White paper p. 6 |
| 3 | Autoresponder | Unknown | – | Not documented in the pages available. | – |
| 4 | Automatic notifications to requester | Unknown | – | Not documented in the pages available. | – |
| 5 | Private notes | Unknown | – | Not documented in the pages available. | – |
| 6 | Team collaboration on a ticket | Unknown | – | Not documented in the pages available. | – |
| 9 | Configurable forms per type/group | Partial | ITSM Foundation; CSM (both packages) | ITSM grid: "Request Management" in all packages. CSM grid: "Service Catalogue" in both packages. **Missing:** field types, required fields and forms per ticket type are not described. | Servicenow1.pdf p. 4; Servicenow2.pdf p. 4 |
| 10 | Multi-step approval workflows | Unknown | – | Grids list "Workflow Automation" only; approvals are not named. | Servicenow1.pdf p. 4; Servicenow2.pdf p. 4 |
| 12 | Requesters see only own tickets | Unknown | – | CSM grid lists "Customer and Partner Portals"; visibility rules are not described. | Servicenow2.pdf p. 3 |
| 13 | Access separated by desk / client | Unknown | – | CSM grid lists "Business Organisation Modelling"; visibility rules are not described. | Servicenow2.pdf p. 3 |
| 15 | SLA/SLO with breach warnings | Partial | CSM (both packages); not listed in the ITSM grid | CSM grid: "Service Level Management". **Missing:** targets per priority and warnings before a breach are not described. | Servicenow2.pdf p. 4 |
| 16 | Dashboards and reports | Partial | CSM (both packages); ITSM Advanced ("Platform Analytics Advanced") | CSM grid: "Reports and Dashboards", "Platform Analytics". **Missing:** queue view and response/resolution metrics are not described. | Servicenow2.pdf p. 4; Servicenow1.pdf p. 5 |
| 17 | Audit log of changes | Unknown | – | Not documented in the pages available. | – |
| 23 | Two-way Slack integration | Unknown | – | Not documented in the pages available. | – |
| 26 | Mature vendor: ISO 27001 / NIS2 / GDPR | Meets | Vendor level | Compliance page lists "ISO/IEC 27001:2022", "ISO/IEC 27017:2015", "ISO/IEC 27018:2019", "ISO/IEC 27701:2019", "ISO/IEC 42001", C5, "CSA STAR Level 2", "EU Cloud CoC", "GDPR compliance". White paper: "ServiceNow has been an ISO 27001-certified organization since 2012"; "The ServiceNow AI Platform also holds SOC 2 Type 2". **NIS2:** a "NIS2 white paper" and "NIS2 FAQ" exist, but "These links require access to the ServiceNow CORE Compliance Portal" (under NDA). This is the only vendor with NIS2-specific documents found. | Servicenow3.pdf p. 2–5; white paper p. 2, 10 |
| 27 | Data stored in the EU | Partial | SPP EU (opt-in, contract amendment) | "Customer data is hosted in EU-based sites." "ServiceNow provides routine support for SPP EU customers from within the EU." "Commercial ServiceNow-integrated third-party model providers are hosted in the EU". "Backups of production instances are made in both sites in a pair". **Missing:** SPP EU is opt-in ("Customers can choose to opt in"); "Veza, ServiceNow Otto, built on Moveworks, and … Moveworks-powered components of EmployeeWorks cannot currently be covered under SPP EU", while the ITSM grid includes "ServiceNow Otto for ITSM Foundation", "Moveworks Core" and "ServiceNow EmployeeWorks"; "the ServiceNow Support itself remains hosted outside the EU (in the US)"; "systems generated data … is not in scope". Whether SPP EU costs extra is not stated. | White paper p. 5–7, 9; Servicenow1.pdf p. 1, 4 |
| 29 | Only agents are paid seats | Unknown | – | Not documented in the pages available. | – |

## Pricing (as displayed on 2026-11-18)
| Product | Plan | Price per agent / month | Billing | Currency | Notes | Source |
|---|---|---|---|---|---|---|
| ITSM | Foundation / Advanced / Prime | Not public | – | – | "Get Custom Quote" | Servicenow1.pdf p. 1 |
| CSM | CSM Advanced / second package | Not public | – | – | "Get Custom Quote" | Servicenow2.pdf p. 1 |

1. AI: the grids include AI features in the packages ("ServiceNow Otto", "AI Agents for Customer Service", "Predictive Intelligence"); no separate AI price is shown. CSM: "All packages include unlimited Virtual Agent conversations."
2. Licences for requesters and approvers (#29): not documented in the pages available.

## Free trial
No trial is offered on the pricing pages ("Get Custom Quote", "Schedule Demo"). No official trial information was found. Secondary sources disagree, so they are not used.

## Access
1. `servicenow.com` blocks headless browsing ("Access Denied").
2. `servicenow.com/docs` loads, but its text is hidden behind a cookie-consent banner. Accepting the banner on the user's behalf was blocked by this session's safety settings, so the documentation was not read.
3. To close the Unknowns, the docs pages for #1, #3–#6, #10, #12, #13, #17, #23 and #29 have to be provided as PDF or text, or ServiceNow has to answer the questions below.

## Could not verify
1. Single tool: can one instance run internal desks (IT, People, Finance, Operations) and external client support (Platform) together? Is CSM required for external B2B clients, or can ITSM / EmployeeWorks serve them?
2. #1, #3, #4, #5, #6: email-to-ticket with full history, autoresponder, requester notifications (including each approval step), private work notes, @mentions and tasks: in which packages?
3. #10: multi-step approvals (requester's manager, then department head) with recorded decisions: in which package?
4. #12, #13: requester sees only own tickets; separation per team desk and per client (for example domain separation): in which package?
5. #15, #16: SLA targets per priority with warnings before a breach; standard queue and response/resolution reports: in ITSM Foundation?
6. #17: are audit records immutable, including owner changes and approvals?
7. #23: native two-way Slack intake with a private requester–agent ticket?
8. #27: does SPP EU cost extra? Which ITSM/CSM features fall outside SPP EU (Otto, Moveworks, EmployeeWorks)?
9. #29: are requesters and approvers free?
10. Pricing: indicative price per agent for about 11 agents (assumption), and is there a trial or sandbox?
