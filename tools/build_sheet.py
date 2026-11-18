"""Build the market-review workbook (.xlsx) for upload to Google Sheets.

Usage:
    python3 tools/build_sheet.py <requirements.xlsx> <output.xlsx>

<requirements.xlsx> is an .xlsx export of the Google Sheet "Helpdesk Tool requirements"
(used only for the area priorities of the 16 K.O. criteria).

K.O. verdicts, evidence and vendor questions are parsed from analysis/ko_screen/*.md.
Pricing and other aspects are curated below from the same files; every entry names its file.
"""
import re
import sys
from pathlib import Path

import openpyxl
from openpyxl.comments import Comment
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
SCREENS = ROOT / "analysis" / "ko_screen"
REPO_URL = "https://github.com/Appsilon/Operations_Ticketing_system/blob/claude/affectionate-hypatia-c52l7j/"
REQ_SHEET_URL = "https://docs.google.com/spreadsheets/d/1ye7vTaVol6DFoRnUrXtx_ibS4FN5z_aJzppNDzCQIEM/edit"
CHECKED = "2026-11-18"
KO = [1, 3, 4, 5, 6, 9, 10, 12, 13, 15, 16, 17, 23, 26, 27, 29]
KO_RULE = {1: "A+B", 3: "A", 4: "A", 5: "A", 6: "A", 9: "A+B", 10: "B", 12: "A+B", 13: "A+B",
           15: "B", 16: "A", 17: "B", 23: "C", 26: "B", 27: "C", 29: "C"}
AREAS = ["Platform", "Operations", "IT", "People", "Finance"]
VERDICTS = ["Meets", "Partial", "Does not meet", "Unknown"]
NAMES = {}  # requirement names, filled from the requirements sheet

# key, display name, screen file, table section filter, vendor name for questions
TOOLS = [
    ("halo", "Halo (HaloITSM / HaloPSA)", "halo.md", "HaloITSM", "Halo"),
    ("freshservice", "Freshservice", "freshworks.md", "Freshservice", "Freshworks"),
    ("atlassian", "Atlassian Service Collection (JSM + CSM)", "atlassian.md", None, "Atlassian"),
    ("zendesk", "Zendesk Customer Service Suite", "zendesk.md", None, "Zendesk"),
    ("zoho", "Zoho Desk", "zoho-desk.md", None, "Zoho"),
    ("topdesk", "TOPdesk", "topdesk.md", None, "TOPdesk"),
    ("freshdesk", "Freshdesk", "freshworks.md", "Freshdesk", "Freshworks"),
    ("hubspot", "HubSpot Service Hub", "hubspot.md", None, "HubSpot"),
    ("servicenow", "ServiceNow (ITSM + CSM)", "servicenow.md", None, "ServiceNow"),
]

# Pricing rows: tool key, product, plan, price per agent/month (number or text), currency, billing,
# agent count used on the page, notes, source URL. Curated from analysis/ko_screen/<file>.
PRICING = [
    ("halo", "Halo", "Single plan", 69, "GBP", "Annual", "Any (calculator default 10)", "Required onboarding package at a bespoke price. AI included. Monthly billing possible, price not shown.", "https://www.usehalo.com/pricing"),
    ("freshservice", "Freshservice", "Starter", 19, "USD", "Annual (29 monthly)", "", "No SLA management or service catalog.", "https://www.freshworks.com/freshservice/pricing/"),
    ("freshservice", "Freshservice", "Growth", 49, "USD", "Annual (59 monthly)", "", "Lowest plan meeting the most K.O. criteria.", "https://www.freshworks.com/freshservice/pricing/"),
    ("freshservice", "Freshservice", "Pro", 99, "USD", "Annual (119 monthly)", "", "Business Agent add-on available (49 USD) for HR, Finance and other teams.", "https://www.freshworks.com/freshservice/pricing/"),
    ("freshservice", "Freshservice", "Enterprise", "Not public", "", "", "", "Adds audit logs.", "https://www.freshworks.com/freshservice/pricing/"),
    ("freshservice", "Freshworks add-on", "Freddy AI Copilot", 29, "USD", "Annual (35 monthly)", "", "Applies to Freshservice and Freshdesk.", "https://www.freshworks.com/freshservice/pricing/"),
    ("atlassian", "Atlassian Service Collection", "Free", 0, "USD", "", "Up to 3 agents", "No audit log, no data residency.", "https://www.atlassian.com/software/jira/service-management/pricing"),
    ("atlassian", "Atlassian Service Collection", "Standard", 26.90, "USD", "Monthly", "11", "Annual tier 11-15 agents: 4,050 USD per year. Approvals may need Premium.", "https://www.atlassian.com/software/jira/service-management/pricing"),
    ("atlassian", "Atlassian Service Collection", "Premium", 61.60, "USD", "Monthly", "11", "Annual tier 11-15 agents: 9,200 USD per year.", "https://www.atlassian.com/software/jira/service-management/pricing"),
    ("atlassian", "Atlassian Service Collection", "Enterprise", "Not public", "", "Annual only", "201+", "Contact sales.", "https://www.atlassian.com/software/jira/service-management/pricing"),
    ("zendesk", "Zendesk Customer Service", "Support Team", 19, "USD", "Annual", "", "Email and ticketing only.", "https://www.zendesk.com/pricing/"),
    ("zendesk", "Zendesk Customer Service", "Suite Team", 55, "USD", "Annual", "", "", "https://www.zendesk.com/pricing/"),
    ("zendesk", "Zendesk Customer Service", "Suite Professional", 115, "USD", "Annual", "", "EU data center add-on free from this plan. Full desk separation (#13) needs Enterprise.", "https://www.zendesk.com/pricing/"),
    ("zendesk", "Zendesk Customer Service", "Suite Enterprise", "Not public", "", "", "", "Talk to Sales. Private groups (#13).", "https://www.zendesk.com/pricing/"),
    ("zendesk", "Zendesk add-on", "Copilot", 50, "USD", "Annual", "", "", "https://www.zendesk.com/pricing/"),
    ("zoho", "Zoho Desk", "Professional", 23, "USD", "Annual (35 monthly)", "", "Approvals, departments.", "https://www.zoho.com/desk/pricing.html"),
    ("zoho", "Zoho Desk", "Enterprise", 40, "USD", "Annual (50 monthly)", "", "Audit log, data sharing, multi layout. 50 free light agents.", "https://www.zoho.com/desk/pricing.html"),
    ("zoho", "Zoho Desk add-on", "Light agent", 6, "USD", "Monthly", "", "Standard and Professional.", "https://www.zoho.com/desk/pricing-comparison.html"),
    ("topdesk", "TOPdesk", "Essential", 71, "EUR", "Not stated", "11", "No SLA management, no multi-level approval. Excl. tax.", "https://www.topdesk.com/en/pricing/?pa=11&pv=eur"),
    ("topdesk", "TOPdesk", "Engaged", 101, "EUR", "Not stated", "11", "86 EUR at 30 agents. Excl. tax.", "https://www.topdesk.com/en/pricing/?pa=11&pv=eur"),
    ("topdesk", "TOPdesk", "Excellent", 143, "EUR", "Not stated", "11", "Excl. tax.", "https://www.topdesk.com/en/pricing/?pa=11&pv=eur"),
    ("freshdesk", "Freshdesk", "Growth", 19, "USD", "Annual (23 monthly)", "", "No SLA reminders.", "https://www.freshworks.com/freshdesk/pricing/"),
    ("freshdesk", "Freshdesk", "Pro", 55, "USD", "Annual (66 monthly)", "", "Lowest plan meeting the most K.O. criteria.", "https://www.freshworks.com/freshdesk/pricing/"),
    ("freshdesk", "Freshdesk", "Enterprise", 89, "USD", "Annual (107 monthly)", "", "Adds audit log.", "https://www.freshworks.com/freshdesk/pricing/"),
    ("hubspot", "HubSpot Service Hub", "Professional (Service Seat)", 100, "USD", "Unclear (page shows 90 / 100)", "", "One-time onboarding 1,500 USD. Core Seat prices depend on hubs already owned.", "https://legal.hubspot.com/hubspot-product-and-services-catalog"),
    ("hubspot", "HubSpot Service Hub", "Enterprise (Service Seat)", 150, "USD", "Talk to Sales", "", "One-time onboarding 3,500 USD.", "https://legal.hubspot.com/hubspot-product-and-services-catalog"),
    ("servicenow", "ServiceNow ITSM", "Foundation / Advanced / Prime", "Not public", "", "", "", "Get Custom Quote.", "https://www.servicenow.com/products/itsm/pricing.html"),
    ("servicenow", "ServiceNow CSM", "CSM Advanced / second package", "Not public", "", "", "", "Get Custom Quote.", "https://www.servicenow.com/au/products/customer-service-management/pricing.html"),
]
PLAN_USED = {"halo": "Single plan", "freshservice": "Growth", "atlassian": "Standard", "zendesk": "Suite Professional",
             "zoho": "Enterprise", "topdesk": "Engaged", "freshdesk": "Pro", "hubspot": "Professional (Service Seat)",
             "servicenow": "Foundation / Advanced / Prime"}

# Other aspects, curated from analysis/ko_screen/<file>.
ASPECTS = {
    "halo": dict(
        products="HaloITSM and HaloPSA: one platform, one licence, one price.",
        one_tool="Yes per vendor: one licence for every department. Open: one instance for internal desks and client support together.",
        a10="Meets. Sequential steps; user's manager (needs Azure AD / AD) and head of department.",
        a17="Partial. Per-ticket audit log, but admins can redact entries (redactions are logged).",
        a23="Partial. Slash commands for agents only; other employees use the chatbot.",
        a26="Meets. ISO 27001:2022, ISO 27701, SOC 2 Type 2 (on request). NIS2 not mentioned.",
        a27="Partial. EU AWS hosting incl. backups, AI in the EU; but the GDPR page also says EU data is 'based out of the UK'.",
        a29="Meets. End users, customers and approvers are free.",
        ai="Included, no add-on.",
        extra="Required onboarding package, bespoke price.",
        trial="Yes, 30 days, all features, no card.",
        strengths="Most K.O. criteria met (13/16). Approvals, SLA warnings and per-client restriction documented. One price incl. AI.",
        gaps="Audit log can be redacted by admins. Slack only for agents. Conflicting EU/UK data statement. Onboarding price unknown."),
    "freshservice": dict(
        products="Freshservice (ITSM with business-team workspaces).",
        one_tool="Internal: yes. External B2B clients in an ESM-mode account: not documented (key question). Fallback: Freshservice + Freshdesk.",
        a10="Meets (Growth). Reporting manager, then department head; non-agents approve by email.",
        a17="Partial. Audit log on Enterprise only, admin changes, 6-month retention.",
        a23="Partial. ServiceBot for requesters; no help-channel or /support intake documented.",
        a26="Meets. ISO 27001:2022, ISO 27701, SOC 2 Type 2 (on request). NIS2 not mentioned.",
        a27="Partial. EU region and backups; data may be 'shifted'; US backup mail provider; EU country not named.",
        a29="Meets. Requesters unlimited; approvers need no agent licence.",
        ai="Freddy AI Copilot 29 USD (annual).",
        extra="Business Agent add-on 49 USD may be needed for People, Finance and Operations agents (not verified on Growth).",
        trial="Yes, 14 days, no card, max 100 requesters.",
        strengths="12/16 met. Internal side covered: approvals, workspaces per team, restricted groups.",
        gaps="Serving external clients in the same account is not documented. No @mentions documented."),
    "atlassian": dict(
        products="Jira Service Management + Customer Service Management in one Service Collection licence.",
        one_tool="Yes. JSM handles external clients by email without a portal; JSM and CSM share one licence.",
        a10="Meets. Approval steps on any workflow status; Premium may be needed (sources conflict).",
        a17="Partial. Work item history and site audit log from Standard; no immutability statement.",
        a23="Partial. Request channels with two-way sync; no private requester ticket or /support documented.",
        a26="Meets. ISO 27001:2022, SOC 2, GDPR. CSM not listed in ISO scope. NIS2 not listed.",
        a27="Partial. EU pinning from Standard incl. backups; customer accounts, logs and AI processing not covered.",
        a29="Meets. Customers and approvers need no licence.",
        ai="Rovo credits included; CSM AI agent 1 USD per resolution.",
        extra="SSO needs a separate Atlassian Guard subscription below Enterprise.",
        trial="Yes, 14 days (up to 30); Free plan for 3 agents.",
        strengths="11/16 met. One licence for internal and external. Free plan for 3 agents.",
        gaps="Approvals may need Premium. Per-client separation needs security levels plus automation. AI processing location not stated."),
    "zendesk": dict(
        products="Zendesk Customer Service Suite (Employee Service is internal-only by contract).",
        one_tool="Yes with Customer Service Suite only. Full desk/client separation needs Enterprise, and all agents must be on the same plan.",
        a10="Partial. A sequential chain needs separate approval requests; plan unclear (Growth, Professional or Enterprise).",
        a17="Meets. Ticket audits are a read-only history.",
        a23="Partial. /zendesk creates tickets; Slack DM channel is 1:1 and thread replies do not reach Zendesk.",
        a26="Meets. ISO 27001:2022, SOC 2 Type II (NDA), ISO 27017/27018/27701/42001. NIS2 not mentioned.",
        a27="Partial. EU data center add-on free from Professional (must be activated); AI processing location not found.",
        a29="Unknown. No explicit statement that end users are free; approvers can be end users.",
        ai="Copilot 50 USD (annual); AI agents billed per automated resolution.",
        extra="Enterprise price not published.",
        trial="Yes, 14 days (Suite Professional).",
        strengths="Only tool with a documented read-only audit history. ISO 27001/27017/27018/27701/42001 and SOC 2.",
        gaps="Full desk/client separation only on Enterprise (no public price). Approval plan unclear. Employee Service cannot serve clients."),
    "zoho": dict(
        products="Zoho Desk (Zoho ServiceDesk Plus is a separate internal product, not evaluated).",
        one_tool="Vendor positions Desk for internal and external use via departments. Internal approvals are weak.",
        a10="Partial. Single approval request to agents; no sequential chain documented; approvers must be agents.",
        a17="Partial. Audit log on Enterprise, does not cover tickets.",
        a23="Partial. Agent-facing Slack app; no requester intake.",
        a26="Meets. ISO 27001 (valid to 2028), SOC 2 Type 2, ISO 27701/27017/27018. NIS2 not mentioned.",
        a27="Partial. EU data centers Amsterdam/Dublin; backup location not stated; pre-built AI agents only in US/IN.",
        a29="Partial. No requester fee listed; approvers need an agent seat; light agents 6 USD.",
        ai="No separate AI add-on; BYOK on lower plans.",
        extra="Department add-on on Enterprise.",
        trial="Yes, 15 days, any paid plan, no card.",
        strengths="Departments per team. EU data centers (Amsterdam, Dublin). 15-day trial on any plan.",
        gaps="Approvals and audit log weak for Operations needs. Per-client separation only via departments."),
    "topdesk": dict(
        products="TOPdesk SaaS (Essential / Engaged / Excellent).",
        one_tool="Yes per docs (external support for service providers); clients modelled as branches, no B2B customer object.",
        a10="Partial. Multi-level approval on Engaged, documented only in Change Management.",
        a17="Partial. Audit trail tracks 'nearly all fields'; no immutability statement.",
        a23="Partial. No native Slack app (Zapier or partners); native Microsoft Teams app.",
        a26="Meets. SOC 2; ISO 27001 announced on the official community (certificate not seen). NIS2 not mentioned.",
        a27="Partial. EU hosting EU1-EU6 incl. backups; AI processing location only in a customer-only policy.",
        a29="Meets. End users unlimited; approvers act as persons (free).",
        ai="Bundled by plan.",
        extra="Billing frequency and contract term not stated.",
        trial="Yes, 30 days, no card (plan not stated).",
        strengths="SaaS managed from the EU, EU hosting, prices in EUR. Unlimited end users.",
        gaps="No native Slack. Approvals only in Change Management. Notifications must be built per event."),
    "freshdesk": dict(
        products="Freshdesk (customer service).",
        one_tool="No. No ticket approvals, so the internal side fails.",
        a10="Does not meet. The only approval workflow is for knowledge-base articles.",
        a17="Partial. Audit log on Enterprise covers admin modules, not tickets.",
        a23="Partial. Slack app for team channels; requester replies become private notes; 250-character limit.",
        a26="Meets. Same Freshworks certifications as Freshservice. NIS2 not mentioned.",
        a27="Partial. Same caveats as Freshservice.",
        a29="Unknown. No explicit statement that contacts are free.",
        ai="Freddy AI Copilot 29 USD (annual).",
        extra="",
        trial="Yes, 14 days (Enterprise plan).",
        strengths="External support covered: email, group-based access, SLA policies.",
        gaps="No ticket approvals. SLA reminders only 5 min to 4 h before a breach."),
    "hubspot": dict(
        products="HubSpot Service Hub (HubSpot already used for sales and marketing).",
        one_tool="No vendor evidence for internal employee requests. No ticket approvals.",
        a10="Does not meet. Approvals exist for quotes, content, exports and deals, not tickets.",
        a17="Partial. Audit log from Professional; no immutability statement; 30-day view.",
        a23="Partial. Tickets from Slack messages; no private requester chat.",
        a26="Partial. 'HubSpot itself is not currently ISO 27001 certified' (only AWS). SOC 2.",
        a27="Partial. EU data center (Germany); usage data goes to the US; existing account location unknown.",
        a29="Unknown. Seats are per user; no statement that contacts are never billed.",
        ai="HubSpot Credits; Customer Agent 50 credits per resolved conversation.",
        extra="One-time onboarding 1,500 USD (Professional).",
        trial="No official Service Hub trial found.",
        strengths="HubSpot is already used for sales and marketing (user information).",
        gaps="No ticket approvals. No own ISO 27001. Separation by team, not by client."),
    "servicenow": dict(
        products="ServiceNow ITSM and CSM: two packages on one platform.",
        one_tool="Two licensed products (ITSM internal, CSM external). One instance for both not verified.",
        a10="Unknown. Feature documentation not accessible.",
        a17="Unknown. Feature documentation not accessible.",
        a23="Unknown. Feature documentation not accessible.",
        a26="Meets. ISO 27001 since 2012, SOC 2 Type 2; the only vendor with a NIS2 white paper and FAQ (NDA portal).",
        a27="Partial. SPP EU opt-in: EU hosting, EU support, AI providers in the EU; Otto, Moveworks and EmployeeWorks parts excluded; support system in the US.",
        a29="Unknown. Not in the pages available.",
        ai="Included in packages; no separate price shown.",
        extra="Prices not public (custom quote).",
        trial="None on the pricing pages.",
        strengths="Most detailed EU residency commitment (SPP EU). Only vendor with NIS2-specific documents.",
        gaps="11/16 Unknown (no docs access). No public price or trial. Two products needed."),
}

HDR_FILL = PatternFill("solid", fgColor="1F3864")
HDR_FONT = Font(name="Arial", size=10, bold=True, color="FFFFFF")
BASE = Font(name="Arial", size=10)
BOLD = Font(name="Arial", size=10, bold=True)
TITLE = Font(name="Arial", size=14, bold=True)
INPUT_FONT = Font(name="Arial", size=10, color="0000FF")
INPUT_FILL = PatternFill("solid", fgColor="FFFF00")
WRAP = Alignment(wrap_text=True, vertical="top")
FILLS = {"Meets": "D9EAD3", "Partial": "FFF2CC", "Does not meet": "F4CCCC", "Unknown": "EFEFEF"}


def clean(text):
    text = text.replace("**", "").strip()
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1 (\2)", text)
    return text.replace("`", "")


def parse_screen(fname, section_filter):
    rows, sec = {}, None
    for line in (SCREENS / fname).read_text().splitlines():
        if line.startswith("## "):
            sec = line
        m = re.match(r"^\|\s*(\d+)\s*\|", line)
        if m and sec and "K.O." in sec and (section_filter is None or section_filter in sec):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            raw = cells[2].replace("*", "").strip()
            verdict = next(v for v in VERDICTS if raw.startswith(v))
            note = raw[len(verdict):].strip()
            rows[int(cells[0])] = dict(req=clean(cells[1]), verdict=verdict, note=clean(note),
                                       plan=clean(cells[3]), evidence=clean(cells[4]), source=clean(cells[5]))
    assert sorted(rows) == KO, f"{fname} {section_filter}: {sorted(rows)}"
    return rows


def parse_questions(fname):
    out, inside = [], False
    for line in (SCREENS / fname).read_text().splitlines():
        if line.startswith("## "):
            inside = line.startswith("## Could not verify")
            continue
        m = re.match(r"^(\d+)\.\s+(.*)", line)
        if inside and m:
            out.append(clean(m.group(2)))
    return out


def read_priorities(req_path):
    ws = openpyxl.load_workbook(req_path, data_only=True)["Requirements"]
    pr = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] is not None and int(r[0]) in KO:
            pr[int(r[0])] = [r[i] if r[i] else "—" for i in range(4, 9)]
            NAMES[int(r[0])] = r[2]
    return pr


def header(ws, row, labels, widths=None):
    for i, lab in enumerate(labels, 1):
        c = ws.cell(row=row, column=i, value=lab)
        c.font, c.fill, c.alignment = HDR_FONT, HDR_FILL, Alignment(wrap_text=True, vertical="center")
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w


def style_body(ws, first_row, last_row, ncols):
    for r in range(first_row, last_row + 1):
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            if cell.font == Font() or not cell.font.bold:
                cell.font = Font(name="Arial", size=10, bold=cell.font.bold, color=cell.font.color)
            cell.alignment = WRAP


def verdict_colors(ws, rng):
    for v, color in FILLS.items():
        ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{v}"'],
                                                      fill=PatternFill("solid", fgColor=color)))


def main(req_path, out_path):
    screens = {k: parse_screen(f, s) for k, _, f, s, _ in TOOLS}
    prio = read_priorities(req_path)
    wb = openpyxl.Workbook()

    # ---------- K.O. matrix ----------
    mx = wb.active
    mx.title = "KO matrix"
    mx["A1"] = "Knockout (K.O.) criteria: verdict per tool"
    mx["A1"].font = TITLE
    mx["A2"] = (f"Checked {CHECKED}. Lowest plan meeting the most criteria. Area columns show the priority "
                "each area gave in the requirements sheet. Evidence for every cell is on the Evidence tab.")
    labels = ["No.", "Requirement", "K.O. rule"] + AREAS + [t[1] for t in TOOLS]
    header(mx, 4, labels, [6, 38, 9] + [12] * 5 + [18] * len(TOOLS))
    first = 5
    for i, n in enumerate(KO):
        r = first + i
        mx.cell(row=r, column=1, value=n)
        mx.cell(row=r, column=2, value=NAMES[n])
        mx.cell(row=r, column=3, value=KO_RULE[n])
        for j, p in enumerate(prio[n]):
            mx.cell(row=r, column=4 + j, value=p)
        for j, t in enumerate(TOOLS):
            mx.cell(row=r, column=9 + j, value=screens[t[0]][n]["verdict"])
    last = first + len(KO) - 1
    style_body(mx, first, last, 8 + len(TOOLS))
    tc0, tcn = get_column_letter(9), get_column_letter(8 + len(TOOLS))
    verdict_colors(mx, f"{tc0}{first}:{tcn}{last}")
    cnt0 = last + 2
    for k, v in enumerate(VERDICTS):
        r = cnt0 + k
        mx.cell(row=r, column=2, value=f"{v} (count)").font = BOLD
        for j in range(len(TOOLS)):
            col = get_column_letter(9 + j)
            mx.cell(row=r, column=9 + j, value=f'=COUNTIF({col}${first}:{col}${last},"{v}")').font = BASE
    mx.freeze_panes = "C5"

    # ---------- Pricing ----------
    pr = wb.create_sheet("Pricing")
    pr["A1"] = f"Prices as displayed on {CHECKED} (not converted between currencies)"
    pr["A1"].font = TITLE
    pr["A2"] = ("Prices were read from the official pricing pages from a non-EU location, so currencies differ. "
                "Tiered prices were read at 11 agents where the page has a calculator.")
    header(pr, 4, ["Tool", "Product", "Plan", "Price per agent / month", "Currency", "Billing",
                   "Agent count used on page", "Notes", "Source"], [30, 28, 26, 14, 10, 22, 14, 50, 50])
    plan_row = {}
    names = {t[0]: t[1] for t in TOOLS}
    for i, (key, product, plan, price, cur, bill, agents, notes, src) in enumerate(PRICING):
        r = 5 + i
        vals = [names[key], product, plan, price, cur, bill, agents, notes, src]
        for c, v in enumerate(vals, 1):
            pr.cell(row=r, column=c, value=v)
        if isinstance(price, (int, float)):
            pr.cell(row=r, column=4).number_format = "#,##0.00"
        if PLAN_USED[key] == plan and key not in plan_row:
            plan_row[key] = r
    style_body(pr, 5, 4 + len(PRICING), 9)
    pr.freeze_panes = "A5"

    # ---------- Overview ----------
    ov = wb.create_sheet("Overview", 0)
    ov["A1"] = "Helpdesk tool market review: K.O. screen of 9 tools"
    ov["A1"].font = TITLE
    ov["A2"] = (f"Checked {CHECKED}. 16 of the 59 requirements were assessed (the K.O. criteria); the other 43 "
                "are not assessed yet. No tool is excluded. Unknown means no evidence was found, not that a feature is missing.")
    ov["A3"] = "Agents (user's assumption, used for the cost estimate)"
    ov["A3"].font = BOLD
    ov["C3"] = 11
    ov["C3"].font, ov["C3"].fill = INPUT_FONT, INPUT_FILL
    ov["C3"].comment = Comment("Source: user-provided assumption (Platform about 6, Finance 1, People 2, IT 1, "
                               "Operations 1), 2026-11-18. Blue on yellow = input you can change.", "review")
    ov["D3"] = "Blue text on yellow = input you can change."
    cols = ["Tool", "Products evaluated", "One tool for internal + external?", "Meets", "Partial", "Does not meet",
            "Unknown", "Platform Musts met", "IT Musts met", "Operations Musts met", "People Musts met",
            "Finance Musts met", "Plan used", "Price per agent / month", "Currency", "Billing",
            "Estimated monthly cost (price x agents)", "Extra costs", "Free trial", "Main strengths",
            "Main gaps and risks", "Details"]
    header(ov, 6, cols, [30, 34, 40, 9, 9, 10, 10, 11, 11, 11, 11, 11, 20, 12, 9, 18, 16, 34, 26, 44, 44, 40])
    ov["G5"] = "Musts among the 16 K.O. criteria:"
    ov["G5"].font = BOLD
    area_col = {"Platform": "D", "Operations": "E", "IT": "F", "People": "G", "Finance": "H"}
    ov_area = ["Platform", "IT", "Operations", "People", "Finance"]  # Platform and IT first (user weighting)
    for j, a in enumerate(ov_area):
        c = 8 + j
        ov.cell(row=5, column=c, value=f"=COUNTIF('KO matrix'!${area_col[a]}${first}:${area_col[a]}${last},\"Must have\")").font = BOLD
    for i, t in enumerate(TOOLS):
        r = 7 + i
        key, name, fname = t[0], t[1], t[2]
        mcol = get_column_letter(9 + i)
        asp = ASPECTS[key]
        ov.cell(row=r, column=1, value=name).font = BOLD
        ov.cell(row=r, column=2, value=asp["products"])
        ov.cell(row=r, column=3, value=asp["one_tool"])
        for k, v in enumerate(VERDICTS):
            ov.cell(row=r, column=4 + k, value=f"=COUNTIF('KO matrix'!{mcol}${first}:{mcol}${last},\"{v}\")")
        for j, a in enumerate(ov_area):
            ac = area_col[a]
            ov.cell(row=r, column=8 + j, value=(f"=COUNTIFS('KO matrix'!${ac}${first}:${ac}${last},\"Must have\","
                                                f"'KO matrix'!{mcol}${first}:{mcol}${last},\"Meets\")"))
        prow = plan_row[key]
        for c, pc in ((13, "C"), (14, "D"), (15, "E"), (16, "F")):
            ov.cell(row=r, column=c, value=f'=IF(ISBLANK(Pricing!{pc}{prow}),"",Pricing!{pc}{prow})')
        ov.cell(row=r, column=14).number_format = "#,##0.00"
        ov.cell(row=r, column=17, value=f'=IF(ISNUMBER(N{r}),N{r}*$C$3,"Not public")').number_format = "#,##0"
        ov.cell(row=r, column=18, value=asp["extra"])
        ov.cell(row=r, column=19, value=asp["trial"])
        ov.cell(row=r, column=20, value=asp["strengths"])
        ov.cell(row=r, column=21, value=asp["gaps"])
        ov.cell(row=r, column=22, value=REPO_URL + "analysis/ko_screen/" + fname)
    style_body(ov, 7, 6 + len(TOOLS), len(cols))
    ov["Q6"].comment = Comment("Price per agent x agents (C3), in the currency shown. Currencies differ and are "
                               "not converted. Tiered prices were read at 11 agents.", "review")
    ov.freeze_panes = "B7"

    # ---------- Other aspects ----------
    oa = wb.create_sheet("Other aspects")
    oa["A1"] = "Other aspects considered (details behind the key K.O. criteria)"
    oa["A1"].font = TITLE
    header(oa, 3, ["Tool", "One tool for internal + external?", "#10 Approvals", "#17 Audit log", "#23 Slack",
                   "#26 Certifications and NIS2", "#27 Data in the EU", "#29 Requester and approver licences",
                   "AI", "Extra costs", "Free trial"], [30] + [40] * 10)
    for i, t in enumerate(TOOLS):
        a = ASPECTS[t[0]]
        vals = [t[1], a["one_tool"], a["a10"], a["a17"], a["a23"], a["a26"], a["a27"], a["a29"], a["ai"],
                a["extra"], a["trial"]]
        for c, v in enumerate(vals, 1):
            oa.cell(row=4 + i, column=c, value=v)
    style_body(oa, 4, 3 + len(TOOLS), 11)
    for i in range(len(TOOLS)):
        oa.cell(row=4 + i, column=1).font = BOLD
    oa.freeze_panes = "B4"

    # ---------- Evidence ----------
    ev = wb.create_sheet("Evidence")
    ev["A1"] = "Evidence per tool and criterion (verbatim quotes from official vendor pages)"
    ev["A1"].font = TITLE
    header(ev, 3, ["Tool", "No.", "Requirement", "Verdict", "Reviewer note", "Lowest plan", "Evidence", "Source"],
           [28, 6, 30, 13, 30, 24, 80, 60])
    r = 4
    for t in TOOLS:
        for n in KO:
            d = screens[t[0]][n]
            for c, v in enumerate([t[1], n, NAMES[n], d["verdict"], d["note"], d["plan"], d["evidence"], d["source"]], 1):
                ev.cell(row=r, column=c, value=v)
            r += 1
    style_body(ev, 4, r - 1, 8)
    verdict_colors(ev, f"D4:D{r - 1}")
    ev.freeze_panes = "A4"
    ev.auto_filter.ref = f"A3:H{r - 1}"

    # ---------- Vendor questions ----------
    vq = wb.create_sheet("Vendor questions")
    vq["A1"] = "Open questions for vendors (from Partial and Unknown verdicts)"
    vq["A1"].font = TITLE
    header(vq, 3, ["Vendor", "No.", "Question"], [16, 6, 120])
    r, seen = 4, set()
    for t in TOOLS:
        if t[2] in seen:
            continue
        seen.add(t[2])
        for k, q in enumerate(parse_questions(t[2]), 1):
            for c, v in enumerate([t[4], k, q], 1):
                vq.cell(row=r, column=c, value=v)
            r += 1
    style_body(vq, 4, r - 1, 3)
    vq.freeze_panes = "A4"
    vq.auto_filter.ref = f"A3:C{r - 1}"

    # ---------- Method and sources ----------
    ms = wb.create_sheet("Method and sources")
    ms["A1"] = "Method and sources"
    ms["A1"].font = TITLE
    header(ms, 3, ["Item", "Detail"], [34, 140])
    items = [
        ("Requirements source", f"Google Sheet 'Helpdesk Tool requirements' ({REQ_SHEET_URL}), version modified 2026-11-13, read {CHECKED}. 59 requirements: 29 Must have, 30 Nice to have."),
        ("Scope of this review", "Step 1 only: the 16 knockout (K.O.) criteria. The remaining 43 requirements are not assessed yet."),
        ("K.O. rule A", "Requirement is 'Must have' for at least 2 areas."),
        ("K.O. rule B", "Notes tab, column 'Impact on tool choice', names the requirement as key or eliminating."),
        ("K.O. rule C", "#23, #27 and #29 added by user decision on 2026-11-18."),
        ("Verdict: Meets", "Every part of the requirement has direct evidence on an official vendor page."),
        ("Verdict: Partial", "Some parts have evidence; other parts are missing, not documented or not verified."),
        ("Verdict: Does not meet", "Evidence that the feature is absent."),
        ("Verdict: Unknown", "No direct evidence found. An inference is not evidence. Unknown does not mean the feature is missing."),
        ("#26 rule", "Meets = ISO 27001 and SOC 2 confirmed on an official vendor page. NIS2-specific documents were not found publicly for any vendor (ServiceNow names them behind an NDA portal)."),
        ("#29 rule", "Meets = official statement that requesters are free or unlimited. Partial = a requester-side role (e.g. approvers) needs a paid seat. Unknown = no explicit statement."),
        ("Area weighting", "User decision: Platform and IT requirements weigh more (People and Finance use Aboard today; IT has no tool). Operations weight not decided. Overview lists Platform and IT first."),
        ("Agent count", "About 11 agents is the user's assumption, not data. Used only for the cost estimate (Overview C3)."),
        ("Budget", "Not known and not set in this review. Prices are recorded as displayed."),
        ("Sources", "Official vendor pages (pricing, help centres, documentation, trust and compliance pages), read with a headless browser on 2026-11-18. No secondary sources were used for any verdict."),
        ("ServiceNow", "servicenow.com blocks automated browsing. Pricing, compliance and EU pages were provided by the user as PDF prints. Feature documentation could not be read, so 11 criteria are Unknown."),
        ("Halo", "HaloITSM and HaloPSA are one platform with one licence; the HaloITSM evidence is shown."),
        ("Prices", "Read from a non-EU location, so prices show in USD or GBP; EUR prices were not shown except for TOPdesk. Currencies are not converted."),
        ("Reviewer checks", "Key quotes were re-checked on the vendor pages for every tool. Verdicts that rested on inference or were inconsistent across vendors were corrected; each correction is in the Reviewer note column of the Evidence tab."),
        ("Detailed files", REPO_URL + "analysis/ (one file per vendor, criteria, summary)."),
    ]
    for i, (k, v) in enumerate(items):
        ms.cell(row=4 + i, column=1, value=k)
        ms.cell(row=4 + i, column=2, value=v)
    style_body(ms, 4, 3 + len(items), 2)
    for i in range(len(items)):
        ms.cell(row=4 + i, column=1).font = BOLD

    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if cell.font.name != "Arial":
                    cell.font = Font(name="Arial", size=cell.font.size or 10, bold=cell.font.bold, color=cell.font.color)
    wb.save(out_path)
    print("saved", out_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
