"""Build the full market-review workbook: every tool on all 59 requirements.

Usage:
    python3 tools/build_full_sheet.py <requirements.xlsx> <output.xlsx>

Verdicts come from analysis/ko_screen/*.md (16 K.O. criteria) and analysis/full_screen/*.md
(the other 43). A tool without a full-screen file gets "Not assessed" for those 43.
Pricing and other aspects are reused from tools/build_sheet.py.
"""
import re
import sys
from pathlib import Path

import openpyxl
from openpyxl.comments import Comment
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.formula import ArrayFormula

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_sheet import ASPECTS, KO, PLAN_USED, PRICING, REPO_URL, REQ_SHEET_URL, clean  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
KO_DIR, FULL_DIR = ROOT / "analysis" / "ko_screen", ROOT / "analysis" / "full_screen"
CHECKED = "2026-11-18"
VERDICTS = ["Meets", "Partial", "Does not meet", "Unknown"]
NA = "Not assessed"
# ECB euro foreign exchange reference rates, 2026-11-18
ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
USD_PER_EUR, GBP_PER_EUR = 1.0968, 0.83290

# key, display name, K.O. file, K.O. section filter, full-screen file, full section filter, vendor
TOOLS = [
    ("halo", "Halo (HaloITSM / HaloPSA)", "halo.md", "HaloITSM", "halo.md", None, "Halo"),
    ("freshservice", "Freshservice", "freshworks.md", "Freshservice", "freshservice.md", None, "Freshworks"),
    ("atlassian", "Atlassian Service Collection (JSM + CSM)", "atlassian.md", None, "atlassian.md", None, "Atlassian"),
    ("zendesk", "Zendesk Customer Service Suite", "zendesk.md", None, "zendesk.md", None, "Zendesk"),
    ("zoho", "Zoho Desk", "zoho-desk.md", None, "zoho-desk.md", None, "Zoho"),
    ("topdesk", "TOPdesk", "topdesk.md", None, "topdesk.md", None, "TOPdesk"),
    ("freshdesk", "Freshdesk", "freshworks.md", "Freshdesk", "freshdesk.md", None, "Freshworks"),
    ("hubspot", "HubSpot Service Hub", "hubspot.md", None, "hubspot.md", None, "HubSpot"),
    ("servicenow", "ServiceNow (ITSM + CSM)", "servicenow.md", None, "servicenow.md", None, "ServiceNow"),
    # extended market scan (analysis/04_market_scan.md), products with Q1 = Yes
    ("unthread", "Unthread", "unthread.md", None, "unthread.md", None, "Unthread"),
    ("deskpro", "Deskpro", "deskpro.md", None, "deskpro.md", None, "Deskpro"),
    ("suptask", "Suptask", "suptask.md", None, "suptask.md", None, "Suptask"),
    ("helpspot", "HelpSpot", "helpspot.md", None, "helpspot.md", None, "HelpSpot"),
    ("zammad", "Zammad", "zammad.md", None, "zammad.md", None, "Zammad"),
    ("otrs", "OTRS", "otrs.md", None, "otrs.md", None, "OTRS"),
    ("ninjaone", "NinjaOne Ticketing", "ninjaone.md", None, "ninjaone.md", None, "NinjaOne"),
]
SCAN_KEYS = {"unthread", "deskpro", "suptask", "helpspot", "zammad", "otrs", "ninjaone"}

# Strengths and gaps across all 59 requirements (counts are in the Overview formulas, not repeated here).
FULL_SUMMARY = {
    "halo": ("Most Must haves met, incl. most Platform and IT Musts. One plan and price with AI included; MCP server for Claude; approvals, SLA warnings, sub-tickets and per-client restriction documented.",
             "Not fully met Musts: #17 audit log (admins can redact), #20, #22 Notion (no native integration found), #23 Slack (agents only), #27 conflicting EU/UK data statement, #28 retention (Unknown). Onboarding price unknown."),
    "freshservice": ("Internal side covered: approvals, workspaces per team, restricted groups. MCP server for Claude (generally available). SSO on all plans.",
                     "Serving external B2B clients in an ESM-mode account is not documented. Not fully met Musts: #6, #8, #17, #20, #22, #23, #27, #28. AI suggestions need the Copilot add-on (Pro and up)."),
    "atlassian": ("One licence for JSM and CSM; most Nice to haves met; MCP server covers JSM and can create and update work items.",
                  "Not fully met Musts: #4, #6, #17, #20, #22, #23, #27, #28. Approvals may need Premium; SSO needs paid Atlassian Guard below Enterprise; per-client separation needs security levels."),
    "zendesk": ("Only tool with a documented read-only audit history; ticket and attachment deletion schedules; many certifications.",
                "Not fully met Musts: #4, #6, #9, #10, #11, #20, #21 (Bridge in early access), #22, #23, #27, #29. Full desk/client separation only on Enterprise (no public price)."),
    "zoho": ("Departments per team; EU data centres; native AI at no extra charge.",
             "Not fully met Musts: #4, #10, #11, #13, #17, #18, #20, #21, #22, #23, #27, #28, #29. Approvals go only to agents; AI that reuses past resolutions only in US/IN data centres."),
    "topdesk": ("SaaS managed from the EU, prices in EUR, unlimited end users. Mail import per address, built-in automation, API and marketplace.",
                "Many Musts only partly met, incl. #10 approvals (Change Management only), #21 (MCP read-only, Excellent plan), #23 (no native Slack), #25 (Google SSO and 2FA not documented)."),
    "freshdesk": ("External support covered: email, SLA policies, group-based access. MCP server for Claude (generally available). SAML SSO on all plans.",
                  "No ticket approvals (#10). No recurring tickets (#42, per a still-published 2017 article). Not fully met Musts include #4, #8, #12, #15, #17, #20, #22, #23."),
    "hubspot": ("HubSpot is already used for sales and marketing (user information). MCP server and Claude connector can read and update tickets.",
                "No ticket approvals (#10). No own ISO 27001. Few IT Musts met. Not fully met Musts include #11, #13, #17, #18, #23, #24, #28."),
    "servicenow": ("Most detailed EU residency commitment (SPP EU); only vendor with NIS2-specific documents (NDA portal).",
                   "Feature documentation not accessible, so most requirements are Unknown. No public price or trial. ITSM and CSM are two products."),
}

# ---- Data for the 7 extended-scan products, curated from analysis/ko_screen/<key>.md and full_screen/<key>.md ----
EXTRA_PRICING = [
    ("unthread", "Unthread", "Pro", 85, "USD", "Not stated (same price on Annual and Monthly tabs)", "Min 5 seats", "Conversation limits apply. SSO needs Business; data residency and audit logs need Enterprise (prices not published).", "https://unthread.io/pricing"),
    ("unthread", "Unthread", "Business / Enterprise", "Not public", "", "", "", "Get in touch.", "https://unthread.io/pricing"),
    ("deskpro", "Deskpro Cloud", "Team", 39, "USD", "Not displayed (page source: annual)", "Min 5 agents", "No Deskpro AI, no Lite Agents.", "https://www.deskpro.com/pricing"),
    ("deskpro", "Deskpro Cloud", "Professional", 59, "USD", "Not displayed (page source: annual)", "Min 10 agents", "Deskpro AI, 50 Lite Agents.", "https://www.deskpro.com/pricing"),
    ("deskpro", "Deskpro Cloud", "Enterprise", 99, "USD", "Not displayed (page source: annual)", "Min 25 agents", "Global data centre (paid), sandbox.", "https://www.deskpro.com/pricing"),
    ("suptask", "Suptask", "Starter", 15, "USD", "Annual (18 monthly)", "", "Page shows $ without naming the currency. No email intake, no approvals, no SLA.", "https://www.suptask.com/pricing"),
    ("suptask", "Suptask", "Professional", 24, "USD", "Annual (29 monthly)", "", "Email, approvals, API, MCP (read-only).", "https://www.suptask.com/pricing"),
    ("suptask", "Suptask", "Growth", 38, "USD", "Annual (45 monthly)", "", "Approval sequences, SLA, SSO.", "https://www.suptask.com/pricing"),
    ("suptask", "Suptask", "Custom", "Not public", "", "", "", "Audit & Compliance, AI assistants, CRM/HRIS connectors.", "https://www.suptask.com/pricing"),
    ("helpspot", "HelpSpot", "Single plan (15-agent tier)", 17.78, "USD", "Annual only", "15 (tier needed for about 11 agents)", "US$3,199 per year for up to 15 agents; 10-agent tier US$2,199. Same price for US/EU cloud or self-hosted.", "https://www.helpspot.com/pricing"),
    ("zammad", "Zammad hosted", "Professional v2", 16, "EUR", "Annual (18 monthly)", "Max 35", "SLAs, ticket fields, AI optional. Excl. VAT.", "https://zammad.com/en/pricing/table"),
    ("zammad", "Zammad hosted", "Plus v2", 25, "EUR", "Annual (27 monthly)", "Unlimited", "Core Workflows, standard reporting. Excl. VAT.", "https://zammad.com/en/pricing/table"),
    ("otrs", "OTRS", "Starter / Advanced / Pro", "Not public", "", "Annual in advance, 1-year minimum (2024 terms)", "", "Get a quote. AI included in Advanced and Pro.", "https://otrs.com/how-to-buy/"),
    ("ninjaone", "NinjaOne platform", "Quote (per device)", "Not public", "", "Per device", "", "Per managed device: US$1.50 (10,000 endpoints) to US$3.75 (50 or fewer) per month; not per agent.", "https://www.ninjaone.com/pricing/"),
]
# Vendor minimums or tiers: the number of agents billed at least (used by the Overview cost estimate)
MIN_BILLED = {("unthread", "Pro"): 5, ("deskpro", "Team"): 5, ("deskpro", "Professional"): 10, ("deskpro", "Enterprise"): 25,
              ("helpspot", "Single plan (15-agent tier)"): 15}
EXTRA_PLAN_USED = {"unthread": "Pro", "deskpro": "Team", "suptask": "Growth", "helpspot": "Single plan (15-agent tier)",
                   "zammad": "Plus v2", "otrs": "Starter / Advanced / Pro", "ninjaone": "Quote (per device)"}
EXTRA_ASPECTS = {
    "unthread": dict(products="Unthread, Slack-native (Pro / Business / Enterprise).",
        one_tool="Yes: projects and portal can each be set to internal or external support. Inbound email is posted to an internal Slack channel, so it depends on Slack.",
        a10="Partial. An approval request is a DM to one approver; a manager-then-head chain needs custom automations.",
        a17="Partial. Audit log on Enterprise only (account events); the ticket audit trail does not show who made each change.",
        a23="Meets. Slack-native intake and replies.",
        a26="Partial. SOC 2 Type II; no ISO 27001 found.",
        a27="Partial. Data goes to the US by default; EU database instance only on Enterprise.",
        a29="Unknown. Priced per agent; no statement that requesters are free.",
        ai="No AI price listed; bring-your-own model on higher plans.",
        extra="Min 5 seats. SSO needs Business; data residency and audit logs need Enterprise (prices not published).",
        trial="Yes, 14 days (via a demo)."),
    "deskpro": dict(products="Deskpro Cloud (Team / Professional / Enterprise); self-hosted Deskpro Private exists.",
        one_tool="Yes per vendor; departments separate the desks.",
        a10="Partial. Approvals with templates and logging; chaining steps only in a 2019 post.",
        a17="Partial. Admin audit log and ticket history; agents can edit or delete messages.",
        a23="Partial. Deskpro's own Slack app; non-agents can open tickets from channels; DMs not supported.",
        a26="Meets. ISO 27001 and SOC 2 Type II on the security page.",
        a27="Partial. EU hosting by default; backup and AI region not stated; EU AI provider option from Professional.",
        a29="Meets. End users free and unlimited; approvers can be free CRM users.",
        ai="Deskpro AI from Professional (US$59); not in Team.",
        extra="Minimums: Team 5, Professional 10, Enterprise 25 agents. Implementation services paid (price not shown).",
        trial="Yes, 14 days, no card."),
    "suptask": dict(products="Suptask, Slack-native service desk (Starter / Professional / Growth / Custom).",
        one_tool="Yes per vendor: 'Service desk for internal teams and customer support'; email intake from Professional.",
        a10="Meets. Sequential approvals (manager field, then Head of Finance), recorded in the ticket (Growth).",
        a17="Partial. 'Audit & Compliance' only on Custom; no field-change log.",
        a23="Meets. Slack-native intake and updates.",
        a26="Partial. SOC 2 Type II; ISO 27001 only at AWS.",
        a27="Partial. AWS Ireland; backups and AI region not stated; ticket messages are also stored in the customer's Slack.",
        a29="Meets. Requesters unlimited at no cost; approvers need no seat.",
        ai="No separate AI price; AI assistants partly beta or Custom-only.",
        extra="Integrations from $20 per month each; Custom plan for CRM/HRIS connectors (price on request).",
        trial="Yes, 14 days on Growth, no card."),
    "helpspot": dict(products="HelpSpot (US or EU cloud, or self-hosted; one plan with all features).",
        one_tool="Yes per vendor (filter Q1 Yes).",
        a10="Unknown. No approval feature found in the manuals.",
        a17="Partial. Audit log can be switched off; entries kept up to 730 days.",
        a23="Partial. Slack only via Zapier or webhooks; nothing syncs back.",
        a26="Partial. Own SOC 2 'in progress'; ISO 27001 belongs to AWS.",
        a27="Partial. Hosting and backups in Frankfurt; AI processing region not stated.",
        a29="Meets. 'Customers never need licenses'.",
        ai="Included; no add-on.",
        extra="Tiered: about 11 agents need the 15-agent tier (US$3,199 per year). Zapier subscription needed for Slack.",
        trial="Yes, 21 days, no card; 90-day money-back guarantee."),
    "zammad": dict(products="Zammad (hosted SaaS in Germany; self-hosting possible).",
        one_tool="Yes per vendor (filter Q1 Yes).",
        a10="Does not meet. No native approvals; a closed GitHub PR says an approval engine 'may be' added in the future.",
        a17="Partial. Ticket history; no immutability statement; authors can delete their own articles within 10 minutes.",
        a23="Partial. One-way notifications to Slack via webhook only.",
        a26="Partial. ISO 27001 since 2026-06-18; no SOC 2.",
        a27="Partial. Hosting in Germany; Zammad AI hosted in the EU; backup location not stated.",
        a29="Unknown. Priced per agent; no explicit statement that customers are free.",
        ai="Zammad AI about EUR 0.03 per AI call (prepaid); Professional v2 and up.",
        extra="Self-hosted support plans EUR 2,999 / 5,999 / 9,999 per year.",
        trial="Yes, 30 days (Professional v2, 3 agents)."),
    "otrs": dict(products="OTRS (managed SaaS or on-premises; site footer: EasyVista-OTRS GmbH).",
        one_tool="Yes per vendor (filter Q1 Yes).",
        a10="Partial. Approvals are modelled in Process Management; routing to the requester's manager not documented.",
        a17="Partial. History logs who and when; no immutability statement; history can be anonymized.",
        a23="Partial. No Slack or Zapier app; only a custom build on the API (Advanced package).",
        a26="Partial. 'Currently does not maintain ISO 27001 or SOC 2 certification'; only data-centre operators are certified.",
        a27="Partial. Hosting in Germany by default, AI in the EU; backup location not stated; support sub-processors outside the EU.",
        a29="Unknown. Priced per licensed user; no statement on requesters.",
        ai="Included in Advanced and Pro; AI credits on Starter (price not public).",
        extra="No public prices; annual billing with a 1-year minimum (2024 terms).",
        trial="Yes, on request; length not stated."),
    "ninjaone": dict(products="NinjaOne Ticketing (module of the NinjaOne endpoint platform).",
        one_tool="Yes per vendor: 'Both' internal IT teams and MSPs serving clients; built around managed devices.",
        a10="Partial. Approvals (any/all, by email) logged on the ticket; ordered steps not documented.",
        a17="Partial. System activity log per ticket; comment editing on by default.",
        a23="Partial. Slack notifications only.",
        a26="Meets. ISO 27001 and SOC 2.",
        a27="Partial. EU instance exists; country, backups and AI region not stated.",
        a29="Unknown. No statement that requesters are free.",
        ai="Katana AI in early access; no price.",
        extra="Priced per managed device, quote only; not stated whether Ticketing can be bought without RMM.",
        trial="Yes, 14 days, no card."),
}
EXTRA_SUMMARY = {
    "unthread": ("One of two tools that fully meet two-way Slack (#23). MCP server with write tools. Most Platform Musts met among the extended-scan tools.",
                 "EU data residency only on Enterprise (US by default). No ISO 27001. SSO only on Business. Few IT Musts met."),
    "deskpro": ("ISO 27001 and SOC 2; EU hosting by default; requesters and approvers free; own Slack app; SSO and 2FA in every plan.",
                "No MCP server (#21 Partial). Approval chaining not in current docs. Many Musts only partly met (#4, #8, #11, #12, #13, #17, #18, #20, #22, #28)."),
    "suptask": ("One of two tools that fully meet two-way Slack (#23). Sequential approvals (#10). Requesters free. Hosted in Ireland.",
                "AI features beta or Custom-only; MCP read-only; Google SSO not documented; no ISO 27001; ticket messages partly stored in Slack."),
    "helpspot": ("One all-inclusive plan; MCP server with write tools (generally available); customers free; EU cloud in Frankfurt.",
                 "No own ISO 27001 or SOC 2 (SOC 2 in progress). No approvals found. No native Slack. No chat or AI assistant for requesters (#30)."),
    "zammad": ("ISO 27001, hosting in Germany, prices in EUR. One product for internal desks and customer support.",
               "No native approvals (#10). No SOC 2. Slack one-way only. Many Musts only partly met (#8, #11, #15, #16, #17, #21, #28)."),
    "otrs": ("Vendor MCP server with write tools; process management for workflows; EU hosting.",
             "No own ISO 27001 or SOC 2 (Notes #13). No public prices. No Slack app. No IT Musts fully met."),
    "ninjaone": ("Ticketing inside an endpoint-management platform; ISO 27001 and SOC 2; EU instance.",
                 "Priced per device, not per agent. AI in early access, no AI routing. No recurring tickets (#42). Few IT Musts met."),
}
ASPECTS = {**ASPECTS, **EXTRA_ASPECTS}
PLAN_USED = {**PLAN_USED, **EXTRA_PLAN_USED}
PRICING = PRICING + EXTRA_PRICING
FULL_SUMMARY.update(EXTRA_SUMMARY)

HDR_FILL, SEC_FILL = PatternFill("solid", fgColor="1F3864"), PatternFill("solid", fgColor="D9E1F2")
HDR_FONT = Font(name="Arial", size=10, bold=True, color="FFFFFF")
BASE, BOLD = Font(name="Arial", size=10), Font(name="Arial", size=10, bold=True)
TITLE = Font(name="Arial", size=14, bold=True)
INPUT_FONT, INPUT_FILL = Font(name="Arial", size=10, color="0000FF"), PatternFill("solid", fgColor="FFFF00")
WRAP = Alignment(wrap_text=True, vertical="top")
FILLS = {"Meets": "D9EAD3", "Partial": "FFF2CC", "Does not meet": "F4CCCC", "Unknown": "EFEFEF", NA: "FFFFFF"}


def parse_table(path, section_kw, section_filter, expected):
    rows, sec = {}, None
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            sec = line
        m = re.match(r"^\|\s*(\d+)\s*\|", line)
        if m and sec and section_kw in sec and (section_filter is None or section_filter in sec):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            raw = cells[2].replace("*", "").strip()
            verdict = next(v for v in VERDICTS if raw.startswith(v))
            note = raw[len(verdict):].strip()
            if note.startswith("(") and note.endswith(")"):
                note = note[1:-1]
            rows[int(cells[0])] = dict(verdict=verdict, note=clean(note.lstrip(" .:;-")),
                                       plan=clean(cells[3]), evidence=clean(cells[4]), source=clean(cells[5]))
    assert sorted(rows) == sorted(expected), f"{path.name}: got {sorted(rows)}"
    return rows


def parse_questions(path):
    out, inside = [], False
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            inside = line.startswith("## Could not verify")
            continue
        m = re.match(r"^(\d+)\.\s+(.*)", line)
        if inside and m:
            out.append(clean(m.group(2)))
    return out


def read_requirements(path):
    ws = openpyxl.load_workbook(path, data_only=True)["Requirements"]
    reqs = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] is None:
            continue
        reqs.append(dict(no=int(r[0]), area=r[1], name=r[2], prio=r[9],
                         areas=[r[i] if r[i] else "—" for i in range(4, 9)]))
    return reqs


def header(ws, row, labels, widths):
    for i, lab in enumerate(labels, 1):
        c = ws.cell(row=row, column=i, value=lab)
        c.font, c.fill, c.alignment = HDR_FONT, HDR_FILL, Alignment(wrap_text=True, vertical="center")
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def colors(ws, rng):
    for v, color in FILLS.items():
        if v != NA:
            ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{v}"'],
                                                          fill=PatternFill("solid", fgColor=color)))


def finish(ws):
    for row in ws.iter_rows():
        for cell in row:
            f = cell.font
            cell.font = Font(name="Arial", size=f.size or 10, bold=f.bold, color=f.color)
            if cell.alignment.wrap_text is not True and cell.row > 2:
                cell.alignment = WRAP


def main(req_path, out_path):
    reqs = read_requirements(req_path)
    allnos = [r["no"] for r in reqs]
    rest = [n for n in allnos if n not in KO]
    data, assessed = {}, {}
    for key, _, kof, kos, fullf, fulls, _ in TOOLS:
        d = parse_table(KO_DIR / kof, "K.O.", kos, KO)
        fp = FULL_DIR / fullf
        assessed[key] = fp.exists()
        if fp.exists():
            d.update(parse_table(fp, "Full screen", fulls, rest))
        else:
            for n in rest:
                d[n] = dict(verdict=NA, note="", plan="", evidence="", source="")
        data[key] = d

    wb = openpyxl.Workbook()
    nt = len(TOOLS)

    # ---------------- Matrix ----------------
    mx = wb.active
    mx.title = "Matrix"
    mx["A1"] = "All 59 requirements: verdict per tool"
    mx["A1"].font = TITLE
    mx["A2"] = (f"Checked {CHECKED}. Lowest plan meeting the most criteria. Area columns show the priority each area "
                "gave in the requirements sheet. Evidence for every cell is on the Evidence tab.")
    labels = ["No.", "Area", "Requirement", "Label", "Overall priority", "K.O. criterion",
              "Platform", "Operations", "IT", "People", "Finance"] + [t[1] for t in TOOLS]
    header(mx, 4, labels, [6, 18, 40, 8, 12, 10, 11, 11, 11, 11, 11] + [17] * nt)
    first, last = 5, 4 + len(reqs)
    for i, rq in enumerate(reqs):
        r = first + i
        vals = [rq["no"], rq["area"], rq["name"], f'="#"&A{r}&" "&C{r}', rq["prio"],
                "Yes" if rq["no"] in KO else "No"] + rq["areas"] + [data[t[0]][rq["no"]]["verdict"] for t in TOOLS]
        for c, v in enumerate(vals, 1):
            mx.cell(row=r, column=c, value=v)
    mx.column_dimensions["D"].hidden = False
    tool_col = {t[0]: get_column_letter(12 + j) for j, t in enumerate(TOOLS)}
    colors(mx, f"L{first}:{get_column_letter(11 + nt)}{last}")
    for k, v in enumerate(VERDICTS + [NA]):
        r = last + 2 + k
        mx.cell(row=r, column=3, value=f"{v} (count)").font = BOLD
        for t in TOOLS:
            c = tool_col[t[0]]
            mx[f"{c}{r}"] = f'=COUNTIF({c}${first}:{c}${last},"{v}")'
    finish(mx)
    mx.freeze_panes = "D5"
    mx.auto_filter.ref = f"A4:{get_column_letter(11 + nt)}{last}"

    # ---------------- Pricing ----------------
    pr = wb.create_sheet("Pricing")
    pr["A1"] = f"Prices as displayed on {CHECKED}"
    pr["A1"].font = TITLE
    pr["A2"] = ("Read from the official pricing pages from a non-EU location, so currencies differ. Tiered prices were "
                "read at 11 agents where the page has a calculator. Overview converts to EUR with ECB reference rates.")
    header(pr, 4, ["Tool", "Product", "Plan", "Price per agent / month", "Currency", "Billing",
                   "Agent count used on page", "Notes", "Source", "Minimum billed agents"], [30, 28, 26, 14, 10, 22, 14, 50, 50, 12])
    names = {t[0]: t[1] for t in TOOLS}
    plan_row = {}
    for i, (key, product, plan, price, cur, bill, agents, notes, src) in enumerate(PRICING):
        r = 5 + i
        for c, v in enumerate([names[key], product, plan, price, cur, bill, agents, notes, src], 1):
            pr.cell(row=r, column=c, value=v)
        if isinstance(price, (int, float)):
            pr.cell(row=r, column=4).number_format = "#,##0.00"
        if (key, plan) in MIN_BILLED:
            pr.cell(row=r, column=10, value=MIN_BILLED[(key, plan)])
        if PLAN_USED[key] == plan and key not in plan_row:
            plan_row[key] = r
    finish(pr)
    pr.freeze_panes = "A5"

    # ---------------- Overview (one card per tool) ----------------
    ov = wb.create_sheet("Overview", 0)
    ov["A1"] = f"Helpdesk tool market review: {len(TOOLS)} tools on all 59 requirements"
    ov["A1"].font = TITLE
    ov["A2"] = (f"Checked {CHECKED}. One column per tool. Unknown means no evidence was found, not that a feature is missing. "
                "Blue text on yellow = input you can change.")
    inputs = [
        (4, "Agents (user's assumption)", 11, "Source: user-provided assumption, 2026-11-18 (Platform about 6, Finance 1, People 2, IT 1, Operations 1)."),
        (5, "Monthly budget in EUR (not set yet)", None, "Enter a budget to fill the 'Within monthly budget?' row."),
        (6, "ECB reference rate: USD per 1 EUR", USD_PER_EUR, f"Source: ECB euro foreign exchange reference rates, 2026-11-18, {ECB_URL}"),
        (7, "ECB reference rate: GBP per 1 EUR", GBP_PER_EUR, f"Source: ECB euro foreign exchange reference rates, 2026-11-18, {ECB_URL}"),
    ]
    for r, lab, val, note in inputs:
        ov.cell(row=r, column=1, value=lab).font = BOLD
        c = ov.cell(row=r, column=2, value=val)
        c.font, c.fill = INPUT_FONT, INPUT_FILL
        c.comment = Comment(note, "review")
        ov.cell(row=r, column=3, value=note)
    header(ov, 9, ["Aspect"] + [t[1] for t in TOOLS], [36] + [40] * nt)
    M = "Matrix!"
    rng = lambda col: f"{M}${col}${first}:${col}${last}"  # noqa: E731
    trng = lambda col: f"{M}{col}${first}:{col}${last}"  # noqa: E731
    rows = []  # (label, kind, payload)
    rows += [("Products evaluated", "text", "products"), ("How it was selected", "origin", None),
             ("One tool for internal + external?", "text", "one_tool")]
    for prio, total_label in (("Must have", "Must have (29 requirements)"), ("Nice to have", "Nice to have (30 requirements)")):
        rows.append((total_label, "section", None))
        for v in VERDICTS + [NA]:
            rows.append((f"{v} (count)", "count", (prio, v)))
        for v in VERDICTS:
            rows.append((f"{v}: which", "list", (prio, v)))
    rows.append(("K.O. criteria not fully met", "kolist", None))
    rows.append(("Must have met per area (met of total)", "section", None))
    for a, col in (("Platform", "G"), ("IT", "I"), ("Operations", "H"), ("People", "J"), ("Finance", "K")):
        rows.append((a, "area", col))
    rows.append(("Budget", "section", None))
    rows += [("Plan used", "price", "C"), ("Price per agent / month", "price", "D"), ("Currency", "price", "E"),
             ("Billing", "price", "F"), ("Estimated monthly cost (price x agents, at least the vendor minimum)", "monthly", None),
             ("Estimated annual cost (monthly x 12)", "annual", None),
             ("Estimated monthly cost in EUR (ECB rate)", "eur", None), ("Within monthly budget?", "budget", None),
             ("Extra costs (one-time, add-ons)", "text", "extra"), ("Free trial", "text", "trial")]
    rows.append(("Summary", "section", None))
    rows += [("Main strengths", "summary", 0), ("Main gaps and risks", "summary", 1),
             ("Details", "links", None)]
    rowno = {}
    for i, (label, kind, payload) in enumerate(rows):
        r = 10 + i
        rowno[label] = r
        a = ov.cell(row=r, column=1, value=label)
        a.font = BOLD
        if kind == "section":
            for c in range(1, nt + 2):
                ov.cell(row=r, column=c).fill = SEC_FILL
            continue
        for j, t in enumerate(TOOLS):
            key, col = t[0], tool_col[t[0]]
            cell = ov.cell(row=r, column=2 + j)
            ref = f"{get_column_letter(2 + j)}"
            if kind == "text":
                cell.value = ASPECTS[key][payload]
            elif kind == "origin":
                cell.value = ("Extended market scan (quick filter, Q1 = Yes)" if key in SCAN_KEYS
                              else "Initial list (brief, requirements sheet Notes #15, reviewer's suggestions)")
            elif kind == "summary":
                cell.value = FULL_SUMMARY[key][payload]
            elif kind == "count":
                prio, v = payload
                cell.value = f'=COUNTIFS({rng("E")},"{prio}",{trng(col)},"{v}")'
            elif kind == "list":
                prio, v = payload
                f = f'=_xlfn.TEXTJOIN(CHAR(10),TRUE,IF(({rng("E")}="{prio}")*({trng(col)}="{v}"),{rng("D")},""))'
                cell.value = ArrayFormula(f"{ref}{r}", f)
            elif kind == "kolist":
                f = (f'=_xlfn.TEXTJOIN(CHAR(10),TRUE,IF(({rng("F")}="Yes")*({trng(col)}<>"Meets"),'
                     f'{rng("D")}&" ("&{trng(col)}&")",""))')
                cell.value = ArrayFormula(f"{ref}{r}", f)
            elif kind == "area":
                cell.value = (f'=IF(COUNTIF({rng(payload)},"Must have")=0,"No Must have requirements",'
                              f'COUNTIFS({rng(payload)},"Must have",{trng(col)},"Meets")&" of "&'
                              f'COUNTIF({rng(payload)},"Must have"))')
            elif kind == "price":
                prow = plan_row[key]
                cell.value = f'=IF(ISBLANK(Pricing!{payload}{prow}),"",Pricing!{payload}{prow})'
                if payload == "D":
                    cell.number_format = "#,##0.00"
            elif kind == "monthly":
                p = f"{ref}{rowno['Price per agent / month']}"
                mn = f"Pricing!J{plan_row[key]}"
                cell.value = f'=IF(ISNUMBER({p}),{p}*MAX($B$4,IF(ISNUMBER({mn}),{mn},0)),"Not public")'
                cell.number_format = "#,##0"
            elif kind == "annual":
                m = f"{ref}{rowno['Estimated monthly cost (price x agents, at least the vendor minimum)']}"
                cell.value = f'=IF(ISNUMBER({m}),{m}*12,"Not public")'
                cell.number_format = "#,##0"
            elif kind == "eur":
                m = f"{ref}{rowno['Estimated monthly cost (price x agents, at least the vendor minimum)']}"
                cur = f"{ref}{rowno['Currency']}"
                cell.value = (f'=IF(ISNUMBER({m}),IF({cur}="EUR",{m},IF({cur}="USD",{m}/$B$6,'
                              f'IF({cur}="GBP",{m}/$B$7,"No rate"))),"Not public")')
                cell.number_format = "#,##0"
            elif kind == "budget":
                e = f"{ref}{rowno['Estimated monthly cost in EUR (ECB rate)']}"
                cell.value = (f'=IF(ISBLANK($B$5),"Budget not set",IF(ISNUMBER({e}),'
                              f'IF({e}<=$B$5,"Yes","No"),"Not public"))')
            elif kind == "links":
                cell.value = (REPO_URL + "analysis/ko_screen/" + t[2] + "\n" +
                              (REPO_URL + "analysis/full_screen/" + t[4] if assessed[key] else "Full screen: not assessed"))
    finish(ov)
    for i in range(len(rows)):
        ov.cell(row=10 + i, column=1).font = BOLD
    ov.freeze_panes = "B10"

    # ---------------- Other aspects ----------------
    oa = wb.create_sheet("Other aspects")
    oa["A1"] = "Other aspects considered (details behind the key criteria)"
    oa["A1"].font = TITLE
    header(oa, 3, ["Tool", "One tool for internal + external?", "#10 Approvals", "#17 Audit log", "#23 Slack",
                   "#26 Certifications and NIS2", "#27 Data in the EU", "#29 Requester and approver licences",
                   "AI", "Extra costs", "Free trial"], [30] + [40] * 10)
    for i, t in enumerate(TOOLS):
        a = ASPECTS[t[0]]
        for c, v in enumerate([t[1], a["one_tool"], a["a10"], a["a17"], a["a23"], a["a26"], a["a27"], a["a29"],
                               a["ai"], a["extra"], a["trial"]], 1):
            oa.cell(row=4 + i, column=c, value=v)
    finish(oa)
    oa.freeze_panes = "B4"

    # ---------------- Evidence ----------------
    ev = wb.create_sheet("Evidence")
    ev["A1"] = "Evidence per tool and requirement (verbatim quotes from official vendor pages)"
    ev["A1"].font = TITLE
    header(ev, 3, ["Tool", "No.", "Requirement", "Overall priority", "K.O. criterion", "Verdict", "Reviewer note",
                   "Lowest plan", "Evidence", "Source"], [28, 6, 34, 12, 10, 13, 30, 24, 80, 60])
    r = 4
    for t in TOOLS:
        for rq in reqs:
            d = data[t[0]][rq["no"]]
            for c, v in enumerate([t[1], rq["no"], rq["name"], rq["prio"], "Yes" if rq["no"] in KO else "No",
                                   d["verdict"], d["note"], d["plan"], d["evidence"], d["source"]], 1):
                ev.cell(row=r, column=c, value=v)
            r += 1
    colors(ev, f"F4:F{r - 1}")
    finish(ev)
    ev.freeze_panes = "A4"
    ev.auto_filter.ref = f"A3:J{r - 1}"

    # ---------------- Vendor questions ----------------
    vq = wb.create_sheet("Vendor questions")
    vq["A1"] = "Open questions for vendors (from Partial and Unknown verdicts)"
    vq["A1"].font = TITLE
    header(vq, 3, ["Vendor", "Product", "Step", "No.", "Question"], [14, 30, 22, 6, 110])
    r, seen = 4, set()
    for key, name, kof, _, fullf, _, vendor in TOOLS:
        sources = []
        if ("ko", kof) not in seen:
            seen.add(("ko", kof))
            sources.append(("K.O. criteria", KO_DIR / kof, vendor if kof == "freshworks.md" else name))
        if assessed[key]:
            sources.append(("Other 43 requirements", FULL_DIR / fullf, name))
        for step, path, prod in sources:
            for k, q in enumerate(parse_questions(path), 1):
                for c, v in enumerate([vendor, prod, step, k, q], 1):
                    vq.cell(row=r, column=c, value=v)
                r += 1
    finish(vq)
    vq.freeze_panes = "A4"
    vq.auto_filter.ref = f"A3:E{r - 1}"

    # ---------------- Market scan (all names from the long list) ----------------
    msc = wb.create_sheet("Market scan")
    msc["A1"] = "Extended market scan: quick filter of 35 more names (official vendor pages, 2026-11-18)"
    msc["A1"].font = TITLE
    msc["A2"] = ("Q1 one product for internal + external use; Q2 own ISO 27001 or SOC 2; Q3 EU hosting possible; "
                 "Q4 Slack integration. Fail = a No on Q1, Q2 or Q3. Pass (flag) = Unknown on Q1, Q2 or Q3.")
    header(msc, 4, ["Group", "Product", "Q1", "Q2", "Q3", "Q4", "Filter result", "Reason", "Deployment",
                    "Starting price (as displayed)", "Next step"], [8, 34, 9, 9, 9, 9, 13, 60, 22, 40, 34])
    full_names = {t[1] for t in TOOLS}
    r = 5
    for g in "ABCDEF":
        fp = ROOT / "analysis" / "market_scan" / f"filter_{g}.md"
        if not fp.exists():
            continue
        inside = False
        for line in fp.read_text().splitlines():
            if line.startswith("## "):
                inside = line.startswith("## Summary")
                continue
            if inside and line.startswith("| ") and not line.startswith("| Product") and not line.startswith("|---"):
                c = [x.strip() for x in line.strip().strip("|").split("|")]
                prod = c[0]
                in_full = any(prod.split(" (")[0].split()[0] in n for n in full_names)
                nxt = ("Full assessment (see Overview)" if in_full else
                       ("Filter only (passed; not assessed further)" if c[5].startswith("Pass") else "Out (failed filter)"))
                for k, v in enumerate([g, prod] + c[1:5] + [c[5], clean(c[6]), c[7] if len(c) > 7 else "",
                                                             clean(c[8]) if len(c) > 8 else "", nxt], 1):
                    msc.cell(row=r, column=k, value=v)
                r += 1
    for v, color in (("Yes", "D9EAD3"), ("Partial", "FFF2CC"), ("No", "F4CCCC"), ("Unknown", "EFEFEF")):
        msc.conditional_formatting.add(f"C5:F{max(r - 1, 5)}", CellIsRule(operator="equal", formula=[f'"{v}"'],
                                                                          fill=PatternFill("solid", fgColor=color)))
    finish(msc)
    msc.freeze_panes = "C5"
    msc.auto_filter.ref = f"A4:K{max(r - 1, 5)}"

    # ---------------- Method and sources ----------------
    ms = wb.create_sheet("Method and sources")
    ms["A1"] = "Method and sources"
    ms["A1"].font = TITLE
    header(ms, 3, ["Item", "Detail"], [34, 140])
    not_assessed = [t[1] for t in TOOLS if not assessed[t[0]]]
    items = [
        ("Requirements source", f"Google Sheet 'Helpdesk Tool requirements' ({REQ_SHEET_URL}), version modified 2026-11-13, read {CHECKED}. 59 requirements: 29 Must have, 30 Nice to have."),
        ("Scope", "Every tool checked on all 59 requirements: 16 knockout (K.O.) criteria first, then the other 43." + (f" Not assessed on the 43: {', '.join(not_assessed)}." if not_assessed else "")),
        ("Tool selection", "9 tools from the initial list (brief, requirements sheet Notes #15, reviewer's suggestions), plus 7 from an extended market scan: 35 names found in category lists, filtered on official pages with 4 questions (one product for internal + external, own ISO 27001 or SOC 2, EU hosting, Slack). 24 passed, 11 failed; the 7 with Q1 = Yes got the full assessment (user decision). See the Market scan tab."),
        ("K.O. criteria", "Rule A: Must have for at least 2 areas. Rule B: named as key or eliminating in the Notes tab. Rule C: #23, #27, #29 added by user decision. No tool is excluded (user decision)."),
        ("Verdict: Meets", "Every part of the requirement has direct evidence on an official vendor page."),
        ("Verdict: Partial", "Some parts have evidence; other parts are missing, limited, not documented or not verified."),
        ("Verdict: Does not meet", "Evidence that the feature is absent."),
        ("Verdict: Unknown", "No direct evidence found. An inference is not evidence. Unknown does not mean the feature is missing."),
        ("Generally available only", "A feature in beta, early access or available on request gets Partial, not Meets."),
        ("Integrations", "Meets = native or official integration (by the vendor or the other product's maker). Partial = only via a third-party app, Zapier/Make or a custom build on the API."),
        ("#21 Claude integration", "Meets = vendor-provided MCP server or a documented native way to connect an external AI agent. Partial = public REST API only."),
        ("#26 rule", "Meets = ISO 27001 and SOC 2 confirmed. NIS2-specific documents were not found publicly for any vendor (ServiceNow names them behind an NDA portal)."),
        ("#29 rule", "Meets = official statement that requesters are free or unlimited. Partial = a requester-side role needs a paid seat. Unknown = no explicit statement."),
        ("Area weighting", "User decision: Platform and IT requirements weigh more (People and Finance use Aboard today; IT has no tool). Operations weight not decided."),
        ("Budget", "Budget is not known (Overview B5 is left empty). Costs are estimated as price per agent x the larger of agents (B4, the user's assumption of 11) and the vendor's minimum or tier (Pricing column J). Tiered prices were read at 11 agents. HelpSpot's tier is fixed at 15 agents; change it if B4 goes above 15."),
        ("Currency conversion", f"EUR estimates use ECB euro reference rates of 2026-11-18 (USD {USD_PER_EUR}, GBP {GBP_PER_EUR} per EUR), {ECB_URL}. Vendors' own EUR price lists may differ."),
        ("Sources", "Official vendor pages (pricing, help centres, documentation, developer docs, marketplaces, trust pages) and official integration pages of the other product, read with a headless browser on 2026-11-18."),
        ("ServiceNow", "servicenow.com blocks automated browsing. Pricing, compliance and EU pages were provided by the user as PDF prints; feature documentation could not be read, so many verdicts are Unknown."),
        ("Halo", "HaloITSM and HaloPSA are one platform with one licence; one column covers both."),
        ("Reviewer checks", "Key quotes were re-checked on vendor pages. Verdicts that rested on inference or were inconsistent across vendors were corrected; see the Reviewer note column on the Evidence tab."),
        ("Detailed files", REPO_URL + "analysis/"),
    ]
    for i, (k, v) in enumerate(items):
        ms.cell(row=4 + i, column=1, value=k).font = BOLD
        ms.cell(row=4 + i, column=2, value=v)
    finish(ms)
    for i in range(len(items)):
        ms.cell(row=4 + i, column=1).font = BOLD
    wb.save(out_path)
    print("saved", out_path, "| full screen present for:", [k for k, v in assessed.items() if v])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
