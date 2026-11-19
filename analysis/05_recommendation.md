# Recommendation: 3 tools for the focus groups

1. Date: 2026-11-19. Basis: 16 tools assessed on all 59 requirements (`analysis/ko_screen/`, `analysis/full_screen/`), requirements sheet version modified 2026-11-13.
2. Workbook with all details: [Helpdesk tool market review (16 tools, all 59 requirements)](https://docs.google.com/spreadsheets/d/18ER6Wh3bzfAFiQ_nCeuNp9sDBi17iPAj8_Oq1dqwLMI/edit).
3. The choice of which tools to test is the team's decision; this is the review's recommendation.

## Method

1. Order agreed with the user: (1) no "Does not meet" on a K.O. criterion, (2) Must haves of Platform and IT met (user decision: these areas weigh more), (3) Must haves of Operations met.
2. Platform or IT Must haves: 19 requirements (#1, #2, #3, #4, #5, #6, #11, #12, #13, #15, #16, #18, #19, #20, #21, #22, #23, #24, #25). Operations Must haves: 14.
3. Operations weight is not decided, so the ranking was also checked with Operations equal to Platform and IT (28 requirements) and with all 29 Must haves equal. The top 3 is the same in all three cases.
4. Counts are of "Meets" only; "Partial" and "Unknown" are not counted as met.

## Ranking (top of 16)

| Rank | Tool | K.O. fail | Platform/IT Musts met (of 19) | Operations Musts met (of 14) | All Musts met (of 29) | Platform + IT + Ops met (of 28) | Est. EUR per month (11 agents) |
|---|---|---|---|---|---|---|---|
| 1 | Halo (HaloITSM / HaloPSA) | none | 16 | 11 | 23 | 22 | ~911 + onboarding (bespoke) |
| 2 | Freshservice | none | 15 | 11 | 21 | 21 | ~491 (+ Copilot $29/agent for AI) |
| 3 | Atlassian Service Collection | none | 14 | 10 | 21 | 20 | ~270 (Standard; approvals may need Premium) |
| 4 | Unthread | none | 13 | 7 | 17 | 16 | ~853 |
| 5 | Zendesk Customer Service Suite | none | 12 | 9 | 18 | 17 | ~1,153 |

Tools with a K.O. "Does not meet" (all on #10 approvals): Freshdesk, HubSpot Service Hub, Zammad. ServiceNow could not be assessed in substance (feature documentation not accessible). Full ranking of all 16 in the workbook.

## Recommended for the focus groups

1. **Halo** – Meets the most Must haves (23 of 29), including 13 of 15 Platform and 5 of 6 IT, on one platform and one licence for internal desks and client support, with AI and free requesters and approvers included. To confirm first: EU hosting (its GDPR page says both "EU" and "based out of the UK") and the onboarding price.
2. **Freshservice** – Strongest on the internal side (approvals, workspaces per team, restricted groups) with 21 Musts met and a generally available MCP server for Claude. To confirm first: Freshworks must state that external B2B clients can be requesters in an ESM-mode account; otherwise it becomes a two-product setup (Freshservice + Freshdesk).
3. **Atlassian Service Collection (JSM + CSM)** – 21 Musts met, external clients by email documented, one licence for JSM and CSM, and the lowest estimated cost of the three. To confirm first: whether approvals need Premium, and the cost of Atlassian Guard for SSO.

## Client pilot (optional, Notes #10: two tools on two clients)

1. If two tools are piloted with clients, Halo and Atlassian are the two whose external client support is documented (Platform Musts met: 13 and 11 of 15).
2. Freshservice fits the pilot only after Freshworks confirms external clients in an ESM-mode account.

## Reserve candidate

1. **Unthread** – one of only two tools (with Suptask) that fully meet #23 two-way Slack, which IT rated Must (Notes #25: do not change how people ask for help). Weak points: EU data residency only on Enterprise (US by default), no ISO 27001, few IT Musts met.

## Must haves none of the top 3 meets in full

1. #17 audit log that cannot be edited (Partial for all three).
2. #20 AI knowledge base linked to Notion/Outline, #22 Notion as a knowledge base.
3. #23 two-way private Slack, #27 all data including AI processing in the EU, #28 retention with automatic deletion.
4. These are questions for all three vendors before or during the focus groups (Vendor questions tab of the workbook).
