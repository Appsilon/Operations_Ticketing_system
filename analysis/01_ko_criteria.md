# Knockout (K.O.) criteria

1. Status: **accepted on 2026-11-18** (16 criteria).
2. Source: Google Sheet “Helpdesk Tool requirements”, tabs Requirements, Notes and Legend. File version modifiedTime 2026-11-13 13:07 UTC, checked 2026-11-18.
3. K.O. criterion = a tool that does not meet it drops out of the detailed comparison.

## Method (sheet data only)

1. Precondition: one tool for internal requests and external client support (brief; Notes #11 “One tool for internal needs (IT, operations) and external ones (client support)”).
2. Rule A: the requirement is “Must have” for at least 2 areas (columns Platform / Operations / IT / People / Finance).
3. Rule B: Notes, column “Impact on tool choice”, names the requirement as key or eliminating (“has to”, “key”, “are out”, “remain the must”).
4. Rule C (user decision, 2026-11-18): #23, #27 and #29 are added as K.O.
5. K.O. = A + B + C. Other “Must have” requirements are scored, not eliminating.

## The 16 criteria

| # | Requirement | Rule | Basis in the sheet |
|---|---|---|---|
| 1 | Email-based ticket handling | A + B | Must: Platform, Operations. Notes #1: “Email handling has to be very good.” Notes #9: “The value has to come from our side, with no requirements placed on clients.” |
| 3 | Autoresponder | A | Must: Platform, People |
| 4 | Automatic notifications to the requester | A | Must: Platform, Operations, IT, People |
| 5 | Private notes (internal comments) | A | Must: Platform, Operations, People |
| 6 | Team collaboration on a ticket | A | Must: Platform, People |
| 9 | Configurable forms per ticket type or group | A + B | Must: Operations, People. Notes #20: “Configurable forms remain the must.” |
| 10 | Multi-step approval workflows | B | Notes #11: “The audit log and approval flows are key.” |
| 12 | Requesters see only their own tickets | A + B | Must: Operations, IT, People. Notes #16: “The tool has to support several permission models.” |
| 13 | Access separated by team desk, project or client | A + B | Must: Platform, IT, People. Notes #16 (as above) |
| 15 | SLA/SLO policies with breach warnings | B | Notes #6: “The tool has to handle several levels of targets and warnings.” |
| 16 | Dashboards and reports | A | Must: Platform, Operations |
| 17 | Audit log of changes | B | Notes #11: “The audit log and approval flows are key.” |
| 23 | Two-way Slack integration (intake and updates) | C | Must: IT. Notes #25: “Two-way Slack integration (must for IT)” |
| 26 | Mature vendor compliant with ISO 27001, NIS2 and GDPR | B | Notes #13: “Immature vendors without certifications are out.” |
| 27 | Data stored in the EU | C | Must: Operations |
| 29 | Only agents are paid seats | C | Must: Operations |

## Flag rule for #23, #27, #29

1. A tool that fails only #23, #27 or #29 but meets the other 13 criteria is **not dropped silently**.
2. It gets the flag “Fails only rule C criteria” and goes on to the full check of all 59 requirements.

## Verdict rules (applied to every screen)

1. Meets: every part of the requirement has direct evidence on an official vendor page.
2. Partial: some parts have evidence; other parts are missing, not documented or not verified.
3. Does not meet: evidence that the feature is absent.
4. Unknown: no direct evidence. An inference is not evidence.
5. #26: Meets = ISO 27001 and SOC 2 confirmed on an official vendor page. NIS2-specific supply-chain documentation was not found on public pages for any vendor; only ServiceNow names a NIS2 white paper and FAQ, behind an NDA portal. NIS2 is therefore an open question for every vendor and does not change the verdict.
6. Generally available only: a feature in beta, early access or "on request" gets Partial, not Meets (applied to the 43 non-K.O. requirements on 2026-11-18).
7. #29: Meets = an official statement that requesters / end users are free or unlimited. Partial = confirmed that a requester-side role (for example approvers) needs a paid seat. Unknown = no explicit statement.

## Observations

1. Rule A alone does not separate tools: 8 of its 9 requirements are rated “Standard” in the sheet, #9 “Standard (higher plans)”. That rating is preliminary (Legend: “to be verified during trials”).
2. Expected differentiators: #10, #15, #17, #23, #26, #27, #29, and the price plan in which each feature is available.
3. Sheet inconsistency (sheet owner to resolve): Notes #16 says “Operations needs isolation per ticket (for example HR cases)”, while #40 “Per-ticket visibility for agents too” (HR example) is “Nice to have” for Operations.

## How K.O. is used

1. Step 1: every candidate is checked against the 16 K.O. criteria only.
2. Step 2: all 59 requirements are checked only for candidates that pass step 1 or carry the flag above.
