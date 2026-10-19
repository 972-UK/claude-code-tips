"""One cheap self-test of the office. Run: python3 scripts/self_test.py"""
import re, subprocess, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
fails = []

def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)

for c in "morning new-client close-month vat mtd chase outreach post legal study mock log".split():
    check((ROOT / ".claude/commands" / f"{c}.md").exists(), f"command /{c}")

for a in "ava-sterling rohan-mehta maya-okafor leo-hartley nia-brooks arjun-patel zara-quinn victor-hale iris-bell".split():
    t = (ROOT / ".claude/agents" / f"{a}.md").read_text() if (ROOT / ".claude/agents" / f"{a}.md").exists() else ""
    fm = re.match(r"---\n(.*?)\n---\n", t, re.S)
    keys = dict(l.split(":", 1) for l in fm[1].splitlines() if ":" in l) if fm else {}
    ok = all(k in keys for k in ("name", "description", "tools", "model")) and keys.get("name", "").strip() == a \
        and keys.get("model", "").strip() in ("haiku", "sonnet", "opus")
    check(ok, f"agent {a} front matter")

for f in ["01-client-profile.md", "02-aml-due-diligence.md", "03-engagement-letter.docx", "04-onboarding-checklist.md",
          "05-monthly-close-checklist.md", "06-queries-to-client.md", "07-monthly-summary-template.md",
          "08-vat-return-workings.md", "09-mtd-quarterly-update.md", "10-year-end-pack.md",
          "11-invoices-and-payments.md", "12-review-log.md"]:
    check((ROOT / "clients/_TEMPLATE" / f).exists(), f"template {f}")

r = subprocess.run([sys.executable, str(ROOT / "scripts/refresh_dashboard.py")], capture_output=True, text=True)
check(r.returncode == 0 and (ROOT / "office/dashboard/data/data.js").exists(), "dashboard data refresh")

name = "Selftest Zoë Ltd"
dest = ROOT / "clients/selftest-zoe-ltd"
log = ROOT / "office/work-log.md"
before = log.read_text()
r = subprocess.run(["bash", str(ROOT / "scripts/new-client.sh"), name], capture_output=True, text=True)
ok = r.returncode == 0 and dest.exists() and name in (dest / "01-client-profile.md").read_text() \
    and "{{" not in (dest / "01-client-profile.md").read_text()
check(ok, "new-client.sh creates and fills a folder")
shutil.rmtree(dest, ignore_errors=True)
log.write_text(before)

bad = []
for p in ROOT.rglob("*.md"):
    if re.search(r"\b[A-CEGHJ-PR-TW-Z]{2}\d{6}[A-D]\b", p.read_text(errors="ignore")):
        bad.append(str(p))
check(not bad, "no NI-number-shaped strings in files " + ", ".join(bad))

print("\nAll checks passed." if not fails else f"\n{len(fails)} check(s) failed.")
sys.exit(1 if fails else 0)
