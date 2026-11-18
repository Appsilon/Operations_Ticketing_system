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
]

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
            rows[int(cells[0])] = dict(verdict=verdict, note=clean(raw[len(verdict):].strip(" ()")),
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
                   "Agent count used on page", "Notes", "Source"], [30, 28, 26, 14, 10, 22, 14, 50, 50])
    names = {t[0]: t[1] for t in TOOLS}
    plan_row = {}
    for i, (key, product, plan, price, cur, bill, agents, notes, src) in enumerate(PRICING):
        r = 5 + i
        for c, v in enumerate([names[key], product, plan, price, cur, bill, agents, notes, src], 1):
            pr.cell(row=r, column=c, value=v)
        if isinstance(price, (int, float)):
            pr.cell(row=r, column=4).number_format = "#,##0.00"
        if PLAN_USED[key] == plan and key not in plan_row:
            plan_row[key] = r
    finish(pr)
    pr.freeze_panes = "A5"

    # ---------------- Overview (one card per tool) ----------------
    ov = wb.create_sheet("Overview", 0)
    ov["A1"] = "Helpdesk tool market review: 9 tools on all 59 requirements"
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
    rows += [("Products evaluated", "text", "products"), ("One tool for internal + external?", "text", "one_tool")]
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
             ("Billing", "price", "F"), ("Estimated monthly cost (price x agents)", "monthly", None),
             ("Estimated annual cost (monthly x 12)", "annual", None),
             ("Estimated monthly cost in EUR (ECB rate)", "eur", None), ("Within monthly budget?", "budget", None),
             ("Extra costs (one-time, add-ons)", "text", "extra"), ("Free trial", "text", "trial")]
    rows.append(("Summary", "section", None))
    rows += [("Main strengths", "text", "strengths"), ("Main gaps and risks", "text", "gaps"),
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
                cell.value = f'=IF(ISNUMBER({p}),{p}*$B$4,"Not public")'
                cell.number_format = "#,##0"
            elif kind == "annual":
                m = f"{ref}{rowno['Estimated monthly cost (price x agents)']}"
                cell.value = f'=IF(ISNUMBER({m}),{m}*12,"Not public")'
                cell.number_format = "#,##0"
            elif kind == "eur":
                m = f"{ref}{rowno['Estimated monthly cost (price x agents)']}"
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

    # ---------------- Method and sources ----------------
    ms = wb.create_sheet("Method and sources")
    ms["A1"] = "Method and sources"
    ms["A1"].font = TITLE
    header(ms, 3, ["Item", "Detail"], [34, 140])
    not_assessed = [t[1] for t in TOOLS if not assessed[t[0]]]
    items = [
        ("Requirements source", f"Google Sheet 'Helpdesk Tool requirements' ({REQ_SHEET_URL}), version modified 2026-11-13, read {CHECKED}. 59 requirements: 29 Must have, 30 Nice to have."),
        ("Scope", "Every tool checked on all 59 requirements: 16 knockout (K.O.) criteria first, then the other 43." + (f" Not assessed on the 43: {', '.join(not_assessed)}." if not_assessed else "")),
        ("K.O. criteria", "Rule A: Must have for at least 2 areas. Rule B: named as key or eliminating in the Notes tab. Rule C: #23, #27, #29 added by user decision. No tool is excluded (user decision)."),
        ("Verdict: Meets", "Every part of the requirement has direct evidence on an official vendor page."),
        ("Verdict: Partial", "Some parts have evidence; other parts are missing, limited, not documented or not verified."),
        ("Verdict: Does not meet", "Evidence that the feature is absent."),
        ("Verdict: Unknown", "No direct evidence found. An inference is not evidence. Unknown does not mean the feature is missing."),
        ("Integrations", "Meets = native or official integration (by the vendor or the other product's maker). Partial = only via a third-party app, Zapier/Make or a custom build on the API."),
        ("#21 Claude integration", "Meets = vendor-provided MCP server or a documented native way to connect an external AI agent. Partial = public REST API only."),
        ("#26 rule", "Meets = ISO 27001 and SOC 2 confirmed. NIS2-specific documents were not found publicly for any vendor (ServiceNow names them behind an NDA portal)."),
        ("#29 rule", "Meets = official statement that requesters are free or unlimited. Partial = a requester-side role needs a paid seat. Unknown = no explicit statement."),
        ("Area weighting", "User decision: Platform and IT requirements weigh more (People and Finance use Aboard today; IT has no tool). Operations weight not decided."),
        ("Budget", "Budget is not known (Overview B5 is left empty). Costs are estimated as price per agent x agents (B4, the user's assumption of 11). Tiered prices were read at 11 agents."),
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
