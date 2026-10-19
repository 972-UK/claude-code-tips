"""Rebuild office/dashboard/data/data.js from the office files.
Run: python3 scripts/refresh_dashboard.py  (or scripts/refresh-dashboard.sh / .ps1)
data.js is loaded by index.html with a <script> tag so the dashboard works offline from file://.
"""
import csv, json, re, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "office" / "dashboard" / "data"
TODAY = datetime.date.today()
DATE_RE = re.compile(r"(\d{2})/(\d{2})/(\d{4})")


def parse_date(s):
    m = DATE_RE.search(s or "")
    if not m:
        return None
    try:
        return datetime.date(int(m[3]), int(m[2]), int(m[1]))
    except ValueError:
        return None


def md_table(text):
    """Return dict of first two columns from a markdown table."""
    out = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and not set(cells[0]) <= set("-: "):
            out[cells[0]] = cells[1]
    return out


def money(s):
    m = re.search(r"£\s?([\d,]+(?:\.\d+)?)", s or "")
    return float(m[1].replace(",", "")) if m else 0.0


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


agents = json.loads(read(D / "agents.json") or "[]")
for a in agents:
    md = read(ROOT / ".claude" / "agents" / f"{a['id']}.md")
    m = re.search(r"^model:\s*(\S+)", md, re.M)
    a["model"] = m[1] if m else ""
    m = re.search(r"## Expertise\n(.*?)(?:\n## |\Z)", md, re.S)
    a["skills"] = m[1].strip().split(" You are highly skilled")[0] if m else ""
    m = re.search(r"^description:\s*(.+)$", md, re.M)
    a["description"] = m[1].strip() if m else ""
    a["briefings"] = [l[2:] for l in read(ROOT / "knowledge" / "briefings" / f"{a['id']}.md").splitlines() if l.startswith("- ")][:5]

with open(ROOT / "leads" / "pipeline.csv", newline="", encoding="utf-8") as f:
    leads = list(csv.DictReader(f))

clients = []
for prof in sorted((ROOT / "clients").glob("*/01-client-profile.md")):
    if prof.parent.name == "_TEMPLATE":
        continue
    t = md_table(read(prof))
    rating = "unrated"
    aml = read(prof.parent / "02-aml-due-diligence.md")
    m = re.search(r"^Rating:\s*(low|medium|high)\s*$", aml, re.M | re.I)
    if m:
        rating = m[1].lower()
    clients.append({
        "folder": prof.parent.name,
        "name": t.get("Client name", prof.parent.name),
        "package": t.get("Package", ""),
        "fee": money(t.get("Monthly fee", "")),
        "status": t.get("Status", ""),
        "nextDeadline": t.get("Next deadline", ""),
        "risk": rating,
    })

invoices = []
inv = ROOT / "finance" / "ledgerpeak-books" / "invoices.csv"
if inv.exists():
    with open(inv, newline="", encoding="utf-8") as f:
        invoices = list(csv.DictReader(f))
overdue = [i for i in invoices if not i.get("paid_date") and (parse_date(i.get("due_date")) or TODAY) < TODAY]

deadlines = []
for line in read(ROOT / "compliance" / "deadlines.md").splitlines():
    if line.startswith("- ") and "|" in line:
        parts = [p.strip() for p in line[2:].split("|")]
        d = parse_date(parts[0])
        if d:
            deadlines.append({"date": parts[0], "days": (d - TODAY).days, "item": parts[1] if len(parts) > 1 else "",
                              "who": parts[2] if len(parts) > 2 else "", "owner": parts[3] if len(parts) > 3 else ""})
deadlines.sort(key=lambda x: x["days"])

units = []
for line in read(ROOT / "academy" / "progress.md").splitlines():
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) >= 5 and cells[0] in ("2", "3", "4"):
        units.append({"level": cells[0], "unit": cells[1], "status": cells[2], "score": cells[3], "weak": cells[4]})

checklist = []
for line in read(ROOT / "office" / "policies" / "pre-launch-legal-checklist.md").splitlines():
    m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*\[(.)\]", line)
    if m:
        checklist.append({"item": m[2], "done": m[3].lower() == "x"})

log = [l for l in read(ROOT / "office" / "work-log.md").splitlines() if DATE_RE.match(l)]

paying = [c for c in clients if c["status"].lower().startswith("active")]
passed = sum(1 for u in units if u["status"].lower() == "passed")
data = {
    "generated": TODAY.strftime("%d/%m/%Y"),
    "kpi": {
        "payingClients": len(paying),
        "mrr": sum(c["fee"] for c in paying),
        "leadsInPipeline": sum(1 for l in leads if l["status"] not in ("won", "lost")),
        "overdueInvoices": len(overdue),
        "aatProgress": f"{passed}/{len(units)} units",
        "complianceDone": f"{sum(c['done'] for c in checklist)}/{len(checklist)}",
    },
    "agents": agents, "leads": leads, "clients": clients,
    "deadlines": [d for d in deadlines if -7 <= d["days"] <= 30],
    "tasks": [l for l in read(ROOT / "office" / "tasks" / "active.md").splitlines() if l.startswith("T-")],
    "updates": [l[2:] for l in read(ROOT / "knowledge" / "updates.md").splitlines() if l.startswith("- ")][:8],
    "units": units, "checklist": checklist, "log": log[-25:][::-1],
}
(D / "data.js").write_text("window.LP_DATA = " + json.dumps(data, indent=1, ensure_ascii=False) + ";\n", encoding="utf-8")
print(f"Dashboard data refreshed {data['generated']}: {len(clients)} clients, {len(leads)} leads, {len(deadlines)} deadlines")
