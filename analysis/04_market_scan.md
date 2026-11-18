# Extended market scan – method

1. Status: method agreed with the user on 2026-11-18, written down before any result was seen.
2. Why: the first 9 products came from the brief, the requirements sheet (Notes #15) and the reviewer's general knowledge, without a systematic scan or written selection criteria.

## Step 1 – Long list

1. Goal: about 20–30 product names that could plausibly serve internal requests and external client support in one tool.
2. Sources for names only: category and comparison pages (for example G2, Capterra, Gartner Peer Insights, vendor-neutral lists) found with web search, plus the reviewer's earlier unverified suggestions. These secondary sources are used only to find names, never for verdicts.
3. Every name is recorded with where it was found.
4. Products already assessed (Halo, Freshservice, Freshdesk, Atlassian Service Collection, Zendesk, Zoho Desk, TOPdesk, HubSpot Service Hub, ServiceNow) are not screened again.

## Step 2 – Quick filter (official vendor pages only)

| Q | Question | Linked requirement |
|---|---|---|
| Q1 | Does one product handle both internal employee requests and external client support (for example ESM and customer service, or an MSP/PSA mode)? | Brief; Notes #11 |
| Q2 | Does the vendor hold ISO 27001 or SOC 2? | #26; Notes #13 |
| Q3 | Can customer data be hosted in the EU? | #27 |
| Q4 | Is there a Slack integration? | #23 |

1. Answers: Yes / Partial / No / Unknown, each with a verbatim quote and the URL. No evidence = Unknown.
2. Pass rule: no "No" on Q1, Q2 or Q3. Q4 is recorded but does not eliminate, because all 9 products assessed so far got Partial on #23.
3. Unknown on Q1–Q3 does not eliminate; the product passes with a flag.
4. A product that fails is listed with the reason, not dropped silently.

## Step 3 – Full assessment

1. Products that pass step 2 get the same full assessment as the first 9: 16 K.O. criteria and the other 43 requirements, same verdict rules (`analysis/01_ko_criteria.md`).
2. Results are added to the repo and to a new version of the review workbook (no Google Sheets connector, so the Sheet cannot be edited in place).

## Step 1 result – Long list (35 names, built 2026-11-18)

Names only; where each was found. Sources are secondary (web search result pages, mostly vendor blogs and directories) and are not evidence for any verdict.

| # | Product | Group | Found in |
|---|---|---|---|
| 1 | BMC Helix ITSM | A Enterprise ITSM/ESM | Web search "enterprise service management … 2026" (InvGate and CloudNuro roundups); Gartner Peer Insights vendor page |
| 2 | Ivanti Neurons for ITSM | A | Harmony.io ESM 2026 roundup; G2 "Ivanti ITSM alternatives" page |
| 3 | OpenText Service Management | A | Gartner Peer Insights vendor page (IT Service Management Platforms) |
| 4 | SymphonyAI (Summit) | A | Gartner Peer Insights vendor page |
| 5 | IFS assyst | A | Gartner Peer Insights vendor page |
| 6 | Microsoft System Center Service Manager | A | Gartner Peer Insights vendor page |
| 7 | ManageEngine ServiceDesk Plus (incl. MSP edition) | B Mid-market ITSM/ESM | ChannelInsider MSP 2026 roundup; Gartner Peer Insights; InvGate roundup |
| 8 | InvGate Service Management | B | Gartner Peer Insights (product page) |
| 9 | SysAid | B | G2 ITSM alternatives page |
| 10 | Xurrent (formerly 4me) | B | Xurrent blog result in web search; reviewer's earlier suggestion |
| 11 | EasyVista (EV Service Manager) | B | Gartner Peer Insights vendor page |
| 12 | Zammad | C European / open source | europeanpurpose.com; EU-alternatives search |
| 13 | OTRS | C | europeanpurpose.com |
| 14 | Znuny | C | Reviewer's earlier suggestion (not found in search) |
| 15 | GLPI | C | Reviewer's earlier suggestion (not found in search) |
| 16 | Proactivanet | C | Gartner Peer Insights vendor page |
| 17 | HelpSpot | D Classic help desk | HelpSpot EU cloud page in search |
| 18 | Hesk | D | Hesk EU-hosted page in search |
| 19 | HelpSpace | D | eualternative.eu |
| 20 | Deskpro | D | Reviewer's earlier suggestion (not found in search) |
| 21 | Intercom | D | Intercom "best help desk software" page in search |
| 22 | Crisp | D | europeanpurpose.com listing |
| 23 | Userlike | D | europeanpurpose.com listing |
| 24 | Pylon | E Slack-native | Slack-native roundups (eesel, Unthread) |
| 25 | Plain | E | Plain blog "best support tools Slack/MS Teams" |
| 26 | Thena | E | Slack-native roundups |
| 27 | Unthread | E | Unthread blog |
| 28 | ClearFeed | E | ClearFeed blog |
| 29 | Suptask | E | Suptask blog; eesel |
| 30 | Siit | F Internal AI / MSP-PSA | Reviewer's earlier suggestion (not found in search) |
| 31 | Atomicwork | F | Reviewer's earlier suggestion (not found in search) |
| 32 | ConnectWise PSA | F | InvGate MSP roundup |
| 33 | Atera | F | Atera blog (MSP help desk roundup) |
| 34 | NinjaOne | F | MSP roundups |
| 35 | SuperOps | F | SuperOps blog |
