"""Build the LedgerPeak HQ page (3D office) from the office files.

Run: python3 scripts/build_hq.py [artifact-output-path]
Writes office/dashboard/hq.html for local use (goes live with Claude Code through data/live.js).
If a path is given, also writes a version without the document wrapper for publishing as a claude.ai artifact.
"""
import datetime, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASH = ROOT / "office" / "dashboard"


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


subprocess.run([sys.executable, str(ROOT / "scripts" / "refresh_dashboard.py")], check=True, capture_output=True)
base = json.loads(read(DASH / "data" / "data.js").split("=", 1)[1].rstrip().rstrip(";"))

claude = read(ROOT / "CLAUDE.md")
duty = {m[0]: m[1] for m in re.findall(r"^\| [^|]+ \| ([a-z-]+) \| [^|]+ \| [a-z]+ \| ([^|]+?) \|$", claude, re.M)}
agents = []
for a in base["agents"]:
    a = dict(a)
    a["duty"] = duty.get(a["id"], "")
    agents.append(a)

rules = []
for m in re.finditer(r"^\d+\. (.+)$", claude.split("## Rules every agent must follow")[1].split("##")[0], re.M):
    first = re.split(r"(?<=\.) ", m[1])[0].replace("`", "")
    rules.append(first)

roadmap = []
for block in read(ROOT / "office" / "roadmap.md").split("\n## ")[1:]:
    title = block.splitlines()[0].strip()
    items = []
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and re.match(r"\d+\.\d+$", cells[0]):
            done = "[x]" in cells[-1].lower()
            target = cells[3] if len(cells) == 5 else ""
            items.append({"id": cells[0], "text": cells[1], "owner": cells[2], "target": target, "done": done})
    roadmap.append({"title": title.split("(")[0].strip(), "items": items})

lessons = []
for p in sorted((ROOT / "knowledge" / "briefings").glob("*.md")):
    for line in read(p).splitlines():
        m = re.match(r"- (\d{2}/\d{2}/\d{4}) \| (.+)", line)
        if m and not any(l["text"] == m[2] for l in lessons):
            lessons.append({"date": m[1], "text": m[2]})

aat_passed = sum(1 for u in base["units"] if u["status"].lower() == "passed")
demo = sum(1 for p in (ROOT / "clients").glob("demo-*") if p.is_dir())
data = {
    "agents": agents, "rules": rules, "roadmap": roadmap, "lessons": lessons[:6],
    "log": base["log"], "kpi": {"leads": base["kpi"]["leadsInPipeline"]},
    "demoClients": demo, "aatPassed": aat_passed,
    "built": datetime.date.today().strftime("%d/%m/%Y"),
}
page = read(DASH / "hq.template.html").replace("/*LP:DATA*/", "window.LP_HQ = " + json.dumps(data, ensure_ascii=False) + ";")

local = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
         '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n'
         + page.replace('<script src="https://cdnjs', '<script src="data/live.js" onerror="this.remove()"></script>\n<script src="https://cdnjs', 1)
         + "\n</body>\n</html>\n")
(DASH / "hq.html").write_text(local, encoding="utf-8")
print("wrote office/dashboard/hq.html")
if len(sys.argv) > 1:
    Path(sys.argv[1]).write_text(page, encoding="utf-8")
    print("wrote", sys.argv[1])
