# ServiceNow (ITSM + CSM) – full screen (requirements outside the K.O. set)
1. Products evaluated: ServiceNow ITSM (Foundation / Advanced / Prime) and CSM (CSM Advanced and a second package whose name is not visible in the capture).
2. Checked: 2026-11-18. Sources: the user's PDF captures of https://www.servicenow.com/products/itsm/pricing.html (`Servicenow1.pdf`), https://www.servicenow.com/au/products/customer-service-management/pricing.html (`Servicenow2.pdf`), https://www.servicenow.com/company/trust/compliance.html (`Servicenow3.pdf`), the SPP EU white paper (`wp-spp_european_union.pdf`, 2026-09-03), and https://zapier.com/apps/servicenow/integrations (fetched 2026-11-18). Feature documentation on servicenow.com/docs could not be read (cookie banner; accepting it on the user's behalf was blocked by this session's safety settings).
3. Summary: Meets 1 / Partial 12 / Does not meet 0 / Unknown 30 (of 43). Must have (13 of the 43): Meets 0 / Partial 5 / Does not meet 0 / Unknown 8. **Partial here mostly means "listed by name in the pricing grids, behaviour not described". Unknown means no evidence in the pages available, not a missing feature.**

## Full screen
| # | Requirement | Verdict | Lowest plan | Evidence (verbatim, short) | Source |
|---|---|---|---|---|---|
| 2 | Shared inbox with a separate address per client | Unknown | – | Not in the pages available. | – |
| 7 | Assigning and reassigning the owner | Partial | CSM (both packages) | CSM grid: "Advanced Work Assignment". Missing: manual reassignment and its logging are not described. | Servicenow2.pdf p. 3 |
| 8 | Custom statuses per process | Unknown | – | Not in the pages available. | – |
| 11 | Linked tickets and sub-tickets across teams | Unknown | – | ITSM grid lists "Universal Request" (Foundation) and "Universal Request Pro" (Advanced, Prime); what they do is not described. | Servicenow1.pdf p. 5 |
| 14 | Built-in automation | Partial | ITSM Foundation; CSM | Grids: "Workflow Automation" in all packages. Missing: if/then rule capabilities are not described. | Servicenow1.pdf p. 4; Servicenow2.pdf p. 4 |
| 18 | AI-suggested solutions | Partial | ITSM Foundation; CSM | ITSM: "ServiceNow Otto for ITSM", "Predictive Intelligence", "AI Search". CSM: "AI-Powered Recommendations". Included in the packages, no separate price shown. Missing: use of past tickets and knowledge bases is not described. | Servicenow1.pdf p. 3–5; Servicenow2.pdf p. 3 |
| 19 | AI categorization and routing | Partial | CSM (both packages) | CSM grid: "Intelligent Case Triage and Routing". Listed by name only; behaviour not described. Included in the packages. | Servicenow2.pdf p. 3 |
| 20 | Building a knowledge base from resolved cases | Partial | ITSM Foundation; CSM | Grids: "Knowledge Management"; CSM: "Conversational Summarisation and Wrap-Up". Missing: AI-written articles from resolved cases are not described. | Servicenow1.pdf p. 4; Servicenow2.pdf p. 3–4 |
| 21 | Claude integration | Unknown | – | Not in the pages available. (The white paper says "Commercial ServiceNow-integrated third-party model providers are hosted in the EU", which is about ServiceNow's own AI, not connecting an external agent.) | White paper p. 5 |
| 22 | Notion as a knowledge base | Unknown | – | Not in the pages available. | – |
| 24 | Public API, webhooks and app marketplace | Unknown | – | Grids list "Application Development", "App Engine Starter" and "Workflow Data Fabric"; API, webhooks and a marketplace are not described. | Servicenow1.pdf p. 4–5 |
| 25 | SSO and 2FA | Unknown | – | Not in the pages available for customer agents. (Multi-factor checks in the white paper apply to ServiceNow personnel.) | White paper p. 8 |
| 28 | Data retention with automatic deletion | Unknown | – | Not in the pages available. (The white paper describes backup retention only.) | White paper p. 10 |
| 30 | Support chat or AI assistant | Partial | ITSM Foundation; CSM | ITSM: "Virtual Agent". CSM: "Chat"; "All packages include unlimited Virtual Agent conversations." Missing: answering from the knowledge base, pointing to forms, status checks and ticket creation are not described. | Servicenow1.pdf p. 1, 5; Servicenow2.pdf p. 2, 4 |
| 31 | Single entry point with a service catalog | Partial | ITSM Foundation; CSM | ITSM: "Request Management", "ServiceNow EmployeeWorks". CSM: "Service Catalogue". Missing: linking requests handled in other systems is not described. | Servicenow1.pdf p. 4; Servicenow2.pdf p. 4 |
| 32 | Branded support space per client | Partial | CSM (both packages) | CSM grid: "Customer and Partner Portals". Missing: a separate branded space per client is not described. | Servicenow2.pdf p. 3 |
| 33 | 24/7 on-call alerting | Partial | ITSM Advanced | ITSM grid: "On-Call Management" (Advanced, Prime); "Now Mobile" in all packages. Missing: push or SMS alerting is not described. | Servicenow1.pdf p. 2, 4 |
| 34 | Watchers and temporary participants | Unknown | – | Not in the pages available. | – |
| 35 | Structured links to other systems | Unknown | – | Not in the pages available. | – |
| 36 | Dependent (dynamic) fields | Unknown | – | Not in the pages available. | – |
| 37 | No-code form builder for business teams | Unknown | – | Grids list "Application Development" and "App Engine Starter"; whether business teams can build forms without technical help is not described. | Servicenow1.pdf p. 5 |
| 38 | Forms visible only to selected groups | Unknown | – | Not in the pages available. | – |
| 39 | Checklists and process templates | Partial | CSM (both packages) | CSM grid: "Case Management and Playbooks". Missing: checklists with owners and due dates are not described. | Servicenow2.pdf p. 1, 3 |
| 40 | Per-ticket visibility for agents too | Unknown | – | Not in the pages available. | – |
| 41 | Bulk ticket creation from a CSV file | Unknown | – | Not in the pages available. | – |
| 42 | Scheduled and recurring tickets | Unknown | – | Not in the pages available. | – |
| 43 | Sending ticket data to registers on close | Unknown | – | Not in the pages available. | – |
| 44 | Automatic tickets from monitoring | Unknown | – | Not in the pages available. | – |
| 45 | Filtering and reporting by requester, period and amount | Partial | CSM (both packages); ITSM Advanced | CSM: "Reports and Dashboards", "Platform Analytics". ITSM: "Platform Analytics Advanced" (Advanced, Prime). Missing: filtering by custom fields such as amounts is not described. | Servicenow2.pdf p. 4; Servicenow1.pdf p. 5 |
| 46 | Time tracking on tickets | Unknown | – | Not in the pages available. | – |
| 47 | Reminders and alerts for waiting tickets | Unknown | – | Not in the pages available. | – |
| 48 | Request history per person | Unknown | – | Not in the pages available. | – |
| 49 | Company structure sync | Unknown | – | Not in the pages available. (CSM "Business Organisation Modelling" is listed; its scope is not described.) | Servicenow2.pdf p. 3 |
| 50 | Zapier | Meets | – | Zapier lists an official "ServiceNow Integrations" app, marked "Premium" (a paid Zapier plan is needed for premium apps). | https://zapier.com/apps/servicenow/integrations |
| 51 | Outline | Unknown | – | Not in the pages available. | – |
| 52 | HubSpot | Unknown | – | Not in the pages available. https://ecosystem.hubspot.com/marketplace/apps/servicenow did not show a ServiceNow listing. | – |
| 53 | Productive | Unknown | – | Not in the pages available. | – |
| 54 | Clients' ticketing tools (for example ServiceNow) | Unknown | – | Not in the pages available. (CSM lists "Partner and Outsourced Provider Management"; its scope is not described.) | Servicenow2.pdf p. 3 |
| 55 | Calendar integration | Unknown | – | Not in the pages available. (CSM "Appointment and Schedule Management" concerns customer appointments; team calendars are not described.) | Servicenow2.pdf p. 3 |
| 56 | Aboard (HR system) | Unknown | – | Not in the pages available. | – |
| 57 | Handling data subject requests | Unknown | – | Not in the pages available. | – |
| 58 | Choosing the data region per client | Unknown | – | Not in the pages available. (SPP EU is opted into "at the account level"; other regions are not described.) | White paper p. 5 |
| 59 | Boards and queue views | Partial | CSM (both packages) | CSM grid: "Workspaces", "CSM Configurable Workspace". Missing: boards and team queue views are not described. | Servicenow2.pdf p. 3–4 |

## Add-on costs found
1. No ServiceNow prices are public ("Get Custom Quote"); AI features are listed inside the packages with no separate price.
2. Zapier: ServiceNow is a "Premium" app on Zapier (needs a paid Zapier plan). Source: https://zapier.com/apps/servicenow/integrations.

## Could not verify
1. #2, #8: separate support email per client; custom statuses per process: in which package?
2. #11: can a request create linked tasks or tickets in other teams' desks (Universal Request)? In Foundation?
3. #21, #24: is there an MCP server or a documented way to connect an external LLM agent? Public REST API, webhooks and the app store: included in all packages?
4. #22, #51, #52, #53, #56: official integrations with Notion, Outline, HubSpot, Productive and Aboard?
5. #25: SSO with Google Workspace and 2FA for agents: included?
6. #28, #57: retention policies with automatic deletion; data subject requests (deletion and export of a person's data)?
7. #34–#38, #40–#42: watchers, structured links, dependent fields, no-code forms for business teams, forms per group, per-ticket visibility, bulk CSV creation, scheduled tickets: in which package?
8. #44, #54: automatic tickets from monitoring of client-hosted systems; receiving tickets from clients' own ServiceNow instances?
9. #46–#48, #55: time tracking, waiting-ticket reminders, request history per person, calendar integration?
10. #58: can one customer hold instances in several regions (EU, US, India) for different clients?
