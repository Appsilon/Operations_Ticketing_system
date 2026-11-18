# K.O. screen – summary

1. Status: step 1 (K.O. screen) done for all 8 vendors (9 products). ServiceNow is based on pages the user provided as PDF; its feature documentation could not be read, so 11 of its criteria are Unknown.
2. Checked: 2026-11-18. Criteria and verdict rules: `analysis/01_ko_criteria.md`. Evidence, quotes and sources: `analysis/ko_screen/<vendor>.md`.
3. Legend: ✅ Meets · 🟡 Partial · ❌ Does not meet · ❓ Unknown.
4. Columns are sorted by number of ✅. A count is not a ranking: one 🟡 on a key criterion can matter more than several ✅.

## Matrix (lowest plan meeting the most criteria)

| # | Requirement | Rule | Halo | Freshservice | Atlassian SC | Zendesk CS | Zoho Desk | TOPdesk | Freshdesk | HubSpot SH | ServiceNow |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Email-based ticket handling | A+B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❓ |
| 3 | Autoresponder | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❓ |
| 4 | Automatic notifications to requester | A | ✅ | ✅ | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❓ |
| 5 | Private notes | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❓ |
| 6 | Team collaboration on a ticket | A | ✅ | 🟡 | 🟡 | 🟡 | ✅ | 🟡 | ✅ | ✅ | ❓ |
| 9 | Configurable forms per type/group | A+B | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ✅ | ✅ | 🟡 |
| 10 | Multi-step approval workflows | B | ✅ | ✅ | ✅ | 🟡 | 🟡 | 🟡 | ❌ | ❌ | ❓ |
| 12 | Requesters see only own tickets | A+B | ✅ | ✅ | ✅ | ✅ | ✅ | ❓ | ❓ | ✅ | ❓ |
| 13 | Access separated by desk / client | A+B | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | 🟡 | ❓ |
| 15 | SLA/SLO with breach warnings | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | 🟡 |
| 16 | Dashboards and reports | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| 17 | Audit log of changes | B | 🟡 | 🟡 | 🟡 | ✅ | 🟡 | 🟡 | 🟡 | 🟡 | ❓ |
| 23 | Two-way Slack integration | C | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❓ |
| 26 | Mature vendor: ISO 27001 / NIS2 / GDPR | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ |
| 27 | Data stored in the EU | C | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 |
| 29 | Only agents are paid seats | C | ✅ | ✅ | ✅ | ❓ | 🟡 | ✅ | ❓ | ❓ | ❓ |
| | **Meets** | | 13 | 12 | 11 | 9 | 9 | 9 | 8 | 8 | 1 |
| | **Partial** | | 3 | 4 | 5 | 6 | 7 | 6 | 5 | 6 | 4 |
| | **Does not meet** | | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| | **Unknown** | | 0 | 0 | 0 | 1 | 0 | 1 | 2 | 1 | 11 |

## Plan, price and trial (as displayed on 2026-11-18)

Prices are shown as displayed (currency and billing differ, so they are not directly comparable). "11 agents" is the user's assumption, not data.

| Product | Plan used in the matrix | Price per agent / month | Billing | Free trial | Source |
|---|---|---|---|---|---|
| Halo | Single plan (no tiers) | £69 | Annual; required onboarding package at bespoke cost | 30 days, all features | `ko_screen/halo.md` |
| Freshservice | Growth | $49 / $59 | Annual / monthly | 14 days (max 100 requesters) | `ko_screen/freshworks.md` |
| Atlassian Service Collection | Standard (approvals may need Premium) | Standard $26.90, Premium $61.60 (at 11 agents) | Monthly | 14 days (extendable to 30); Free plan for 3 agents | `ko_screen/atlassian.md` |
| Zendesk Customer Service Suite | Professional; #13 ✅ only on Enterprise | Professional $115; Enterprise not published | Annual | 14 days (Suite Professional) | `ko_screen/zendesk.md` |
| Zoho Desk | Enterprise | $40 / $50 | Annual / monthly | 15 days | `ko_screen/zoho-desk.md` |
| TOPdesk | Engaged | €101 (at 11 agents) | Not stated | 30 days | `ko_screen/topdesk.md` |
| Freshdesk | Pro | $55 / $66 | Annual / monthly | 14 days (Enterprise plan) | `ko_screen/freshworks.md` |
| HubSpot Service Hub | Professional | $100 per Service Seat + $1,500 one-time onboarding | Not clear from page text | No official Service Hub trial found | `ko_screen/hubspot.md` |
| ServiceNow (ITSM + CSM) | ITSM Foundation / Advanced / Prime; CSM | Not public (custom quote) | – | None on the pricing pages | `ko_screen/servicenow.md` |

## One tool for internal + external?

1. Halo: yes per vendor ("same platform and the same licence" for every department). Open: whether one instance runs internal desks and client support together.
2. Freshservice: internal side yes. External B2B clients in an ESM-mode account are not documented; key question for Freshworks.
3. Atlassian: yes. JSM handles external clients by email; JSM and CSM share one licence.
4. Zendesk: yes, with Customer Service Suite only. Employee Service is internal-only by contract.
5. Zoho Desk: vendor positions it for both; internal approvals are weak (#10 🟡).
6. TOPdesk: yes per docs (external support for service providers); no dedicated B2B customer object.
7. Freshdesk: no; internal side fails on approvals (#10 ❌).
8. HubSpot Service Hub: no vendor evidence for internal use; approvals fail (#10 ❌).
9. ServiceNow: two products (ITSM internal, CSM external) on one platform; one instance for both not verified.

## Market-wide findings

1. #23 Two-way Slack: 🟡 for all 8 products with evidence (ServiceNow ❓). None documents a private requester–agent ticket from Slack with two-way sync.
2. #27 Data in the EU: 🟡 for all 9. ServiceNow has the most detailed commitment (SPP EU, opt-in) but excludes Otto, Moveworks and EmployeeWorks components. Typical gaps: AI processing location, sub-processors outside the EU, unclear statements.
3. #17 Audit log: ✅ only for Zendesk ("Audits are a read-only history of all updates to a ticket"). Others do not state that entries cannot be edited.
4. #26: NIS2-specific documentation was not found publicly for any vendor. Only ServiceNow names a NIS2 white paper and FAQ, behind an NDA portal.

## Decision (user, 2026-11-18)

1. No tool is excluded. All 9 products are listed with what they meet and what they do not.
2. Google Sheet with all tools, prices and other aspects: [Helpdesk tool market review (K.O. screen)](https://docs.google.com/spreadsheets/d/1wQezDjJLfttVSxtOb3TP2wDXY0pGRWu62XZcrPSCqp0/edit), generated by `tools/build_sheet.py` (copy in `output/helpdesk_tool_market_review.xlsx`).
