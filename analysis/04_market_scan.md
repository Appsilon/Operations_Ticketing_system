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
