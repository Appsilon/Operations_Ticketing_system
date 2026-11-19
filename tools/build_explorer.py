"""Build the interactive decision page (Artifact) from the evidence files.

Usage:
    python3 tools/build_explorer.py <requirements.xlsx> <out_dir>

Writes <out_dir>/index.html (summary data inline, page from tools/explorer_template.html) and
<out_dir>/evidence.json (verdict notes, evidence quotes, sources and vendor questions, loaded on demand).
Data comes from analysis/ko_screen, analysis/full_screen, analysis/market_scan, analysis/01_ko_criteria.md,
analysis/05_recommendation.md and the curated pricing and aspects in tools/build_full_sheet.py.
Nothing is typed in by hand here except short display names and two caveat texts.
"""
import json
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_full_sheet as B  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "explorer_template.html"
CODE = {"Meets": "M", "Partial": "P", "Does not meet": "X", "Unknown": "U"}
SHORT = {"halo": "Halo", "freshservice": "Freshservice", "atlassian": "Atlassian", "zendesk": "Zendesk",
         "zoho": "Zoho Desk", "topdesk": "TOPdesk", "freshdesk": "Freshdesk", "hubspot": "HubSpot",
         "servicenow": "ServiceNow", "unthread": "Unthread", "deskpro": "Deskpro", "suptask": "Suptask",
         "helpspot": "HelpSpot", "zammad": "Zammad", "otrs": "OTRS", "ninjaone": "NinjaOne"}
CAVEAT = {
    "servicenow": "servicenow.com blocks automated browsers, so this assessment rests on PDFs of vendor pages "
                  "supplied by the user. Most verdicts are Unknown: the low score shows missing evidence, not proven gaps.",
    "helpspot": "Priced in agent tiers. The estimate uses the 15-agent tier; above 15 agents the tier is not modelled.",
}
MAX_TIER = {"helpspot": 15}  # agents covered by the tier used for the estimate; above that the price is not known
TIERED = {"atlassian": "Atlassian prices are tiered; the per-agent price was read at 11 agents.",
          "topdesk": "TOPdesk prices are tiered; the per-agent price was read at 11 agents.",
          "helpspot": CAVEAT["helpspot"]}


def md(text):
    """Keep markdown links and bold for the page renderer; drop code ticks."""
    return (text or "").replace("`", "").strip()


def parse_rows(path, section_kw, section_filter, expected):
    rows, sec = {}, None
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            sec = line
        m = re.match(r"^\|\s*(\d+)\s*\|", line)
        if m and sec and section_kw in sec and (section_filter is None or section_filter in sec):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            raw = cells[2].replace("*", "").strip()
            verdict = next(v for v in B.VERDICTS if raw.startswith(v))
            note = raw[len(verdict):].strip()
            if note.startswith("(") and note.endswith(")"):
                note = note[1:-1]
            rows[int(cells[0])] = dict(v=CODE[verdict], n=md(note.lstrip(" .:;-")), p=md(cells[3]),
                                       e=md(cells[4]), s=md(cells[5]))
    assert sorted(rows) == sorted(expected), f"{path.name}: got {sorted(rows)}"
    return rows


def section_items(path, prefix):
    out, inside = [], False
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            inside = line.startswith(prefix)
            continue
        m = re.match(r"^\d+\.\s+(.*)", line)
        if inside and m:
            out.append(md(m.group(1)))
    return out


def read_requirements(path):
    ws = openpyxl.load_workbook(path, data_only=True)["Requirements"]
    rows = list(ws.iter_rows(values_only=True))
    areas = [str(rows[0][i]) for i in range(4, 9)]  # e.g. "Platform (Dawid)", as in the sheet header
    reqs = []
    for r in rows[1:]:
        if r[0] is None:
            continue
        reqs.append(dict(no=int(r[0]), group=r[1], name=r[2], desc=r[3] or "",
                         areas=[{"Must have": "M", "Nice to have": "N"}.get(r[i], "") for i in range(4, 9)],
                         prio="M" if r[9] == "Must have" else "N", market=r[10] or "", comment=r[11] or ""))
    return areas, reqs


def read_legend(path):
    ws = openpyxl.load_workbook(path, data_only=True)["Legend"]
    out = {}
    for a, b in ws.iter_rows(max_col=2, values_only=True):
        if a in ("Last updated", "Platform", "Operations", "IT", "People", "Finance"):
            out[a] = str(b)
    return out


def ko_rules():
    out = {}
    for line in (ROOT / "analysis" / "01_ko_criteria.md").read_text().splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|(.*)\|\s*$", line)
        if m and int(m.group(1)) in B.KO:
            out[int(m.group(1))] = dict(rule=m.group(3).strip(), basis=md(m.group(4)))
    assert sorted(out) == sorted(B.KO), sorted(out)
    return out


def scan_groups():
    out = {}
    for line in (ROOT / "analysis" / "04_market_scan.md").read_text().splitlines():
        m = re.match(r"^\|\s*\d+\s*\|[^|]*\|\s*([A-F]) ([^|]+?)\s*\|", line)
        if m:
            out[m.group(1)] = m.group(2)
    assert sorted(out) == list("ABCDEF"), out
    return out


def market_scan():
    rows = []
    for g in "ABCDEF":
        inside = False
        for line in (ROOT / "analysis" / "market_scan" / f"filter_{g}.md").read_text().splitlines():
            if line.startswith("## "):
                inside = line.startswith("## Summary")
                continue
            if inside and line.startswith("| ") and not line.startswith(("| Product", "|---")):
                c = [x.strip() for x in line.strip().strip("|").split("|")]
                rows.append(dict(group=g, product=md(c[0]), q=c[1:5], result=md(c[5]), reason=md(c[6]),
                                 deploy=md(c[7]) if len(c) > 7 else "", price=md(c[8]) if len(c) > 8 else ""))
    return rows


def recommendation():
    p = ROOT / "analysis" / "05_recommendation.md"
    top = []
    for item in section_items(p, "## Recommended for the focus groups"):
        m = re.match(r"\*\*(.+?)\*\*\s*[–-]\s*(.*)", item)
        why, _, confirm = m.group(2).partition("To confirm first:")
        top.append(dict(name=m.group(1), why=why.strip(), confirm=confirm.strip()))
    return dict(top=top,
                pilot=section_items(p, "## Client pilot"),
                reserve=section_items(p, "## Reserve candidate"),
                gaps=section_items(p, "## Must haves none of the top 3"),
                method=section_items(p, "## Method"))


def main(req_path, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    areas, reqs = read_requirements(req_path)
    allnos = [r["no"] for r in reqs]
    rest = [n for n in allnos if n not in B.KO]
    rules = ko_rules()
    for r in reqs:
        r["ko"] = rules.get(r["no"])

    plan_row = {}
    for (key, product, plan, price, cur, bill, agents, notes, src) in B.PRICING:
        if B.PLAN_USED[key] == plan and key not in plan_row:
            num = isinstance(price, (int, float))
            plan_row[key] = dict(product=product, plan=plan, price=price if num else None,
                                 priceText="" if num else str(price), currency=cur, billing=bill,
                                 agentsNote=agents, notes=notes, source=src,
                                 minAgents=B.MIN_BILLED.get((key, plan), 0), maxAgents=MAX_TIER.get(key),
                                 tiered=TIERED.get(key, ""))
    other_plans = {}
    for (key, product, plan, price, cur, bill, agents, notes, src) in B.PRICING:
        if plan != B.PLAN_USED[key]:
            other_plans.setdefault(key, []).append(dict(product=product, plan=plan, price=price, currency=cur,
                                                         billing=bill, notes=notes, source=src))

    tools, evidence, n_sourced = [], {}, 0
    for key, name, kof, kos, fullf, fulls, vendor in B.TOOLS:
        d = parse_rows(B.KO_DIR / kof, "K.O.", kos, B.KO)
        d.update(parse_rows(B.FULL_DIR / fullf, "Full screen", fulls, rest))
        n_sourced += sum(1 for n in allnos if d[n]["v"] != "U")  # Meets / Partial / Does not meet: quote + source
        a, s = B.ASPECTS[key], B.FULL_SUMMARY[key]
        qs = section_items(B.KO_DIR / kof, "## Could not verify")
        if kof == "freshworks.md":  # one file for Freshservice and Freshdesk: keep this product's questions
            other = "Freshdesk" if key == "freshservice" else "Freshservice"
            qs = [q for q in qs if not (other in q and name not in q)]
        qs += [q for q in section_items(B.FULL_DIR / fullf, "## Could not verify") if q not in qs]
        checks = section_items(B.KO_DIR / kof, "## Reviewer check") + section_items(B.FULL_DIR / fullf, "## Reviewer check")
        tools.append(dict(
            key=key, name=name, short=SHORT[key], vendor=vendor,
            origin="scan" if key in B.SCAN_KEYS else "initial",
            products=a["products"], oneTool=a["one_tool"], ai=a["ai"], extra=a["extra"], trial=a["trial"],
            strengths=s[0], gaps=s[1], pricing=plan_row[key], otherPlans=other_plans.get(key, []),
            caveat=CAVEAT.get(key, ""),
            v="".join(d[n]["v"] for n in allnos),
            files=["analysis/ko_screen/" + kof, "analysis/full_screen/" + fullf],
        ))
        evidence[key] = dict(cells={str(n): {k: d[n][k] for k in "npes"} for n in allnos},
                             questions=qs, checks=checks)

    scan = market_scan()
    data = dict(
        meta=dict(checked="18–19 Nov 2026", built="19 Nov 2026", reqVersion=read_legend(req_path).get("Last updated", ""),
                  reqModified="13 Nov 2026", reqSheetUrl=B.REQ_SHEET_URL,
                  workbookUrl="https://docs.google.com/spreadsheets/d/18ER6Wh3bzfAFiQ_nCeuNp9sDBi17iPAj8_Oq1dqwLMI/edit",
                  repoUrl=B.REPO_URL, usdPerEur=B.USD_PER_EUR, gbpPerEur=B.GBP_PER_EUR, ecbUrl=B.ECB_URL,
                  ecbDate="18 Nov 2026", agents=11, verdicts=len(allnos) * len(tools), sourced=n_sourced,
                  koRules=section_items(ROOT / "analysis" / "01_ko_criteria.md", "## Method"),
                  verdictRules=section_items(ROOT / "analysis" / "01_ko_criteria.md", "## Verdict rules")),
        areas=areas, sources=read_legend(req_path), reqs=reqs, tools=tools, rec=recommendation(), scan=scan, scanGroups=scan_groups(),
        recKeys=["halo", "freshservice", "atlassian"], reserveKey="unthread",
    )
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text().replace("/*__DATA__*/null", payload)
    (out / "index.html").write_text(html)
    (out / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False))
    print(f"wrote {out/'index.html'} ({len(html)//1024} KB), {out/'evidence.json'} "
          f"({(out/'evidence.json').stat().st_size//1024} KB); {len(tools)} tools x {len(allnos)} requirements, "
          f"{n_sourced} verdicts backed by a quote and source; market scan rows: {len(scan)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
