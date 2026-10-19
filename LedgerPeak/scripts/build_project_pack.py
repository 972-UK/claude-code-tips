"""Rebuild the claude-project/ knowledge files from the office folder.
Run: python3 scripts/build_project_pack.py
01-PROJECT-INSTRUCTIONS.md, 09-first-30-evenings.md and SETUP.md are written by hand and left alone.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "claude-project"
TEAM = ("grace-whitmore ava-sterling eleanor-price henry-collins charlotte-quinn amelia-hart sophie-bennett leo-hartley "
        "james-whitfield daniel-foster edward-lancaster emily-brooks harriet-ellis victor-hale william-hayes theo-ashford iris-bell").split()


def bundle(name, title, files, intro=""):
    parts = [f"# {title}\n", intro]
    for f in files:
        p = ROOT / f
        if p.exists():
            parts.append(f"\n\n---\n\n<!-- file: {f} -->\n\n" + p.read_text(encoding="utf-8"))
    (OUT / name).write_text("\n".join(parts), encoding="utf-8")
    print(f"{name}: {sum(len(x) for x in parts) // 1000}k characters")


def files_in(folder, pattern="*.md"):
    return sorted(str(p.relative_to(ROOT)) for p in (ROOT / folder).glob(pattern))


bundle("02-company-rules-and-facts.md", "LedgerPeak: company rules, facts and latest updates",
       ["CLAUDE.md", "knowledge/updates.md", "office/templates/chart-of-accounts.md", "office/quality/review-checklist.md"])
bundle("03-the-team.md", "LedgerPeak: job descriptions for all seventeen staff",
       [f".claude/agents/{a}.md" for a in TEAM],
       "In a claude.ai Project the staff do not run as separate programs. Claude takes each role in turn using these job descriptions. "
       "File paths refer to the Claude Code version of the office; in the Project, produce the same documents in the conversation.")
bundle("04-templates.md", "Templates: client file and office",
       files_in("clients/_TEMPLATE") + files_in("office/templates"),
       "The engagement letter is a Word file in the Claude Code version. Its sections: scope, fees, your responsibilities, our responsibilities, "
       "anti-money laundering, data protection, termination, complaints, limitation of liability, signatures.")
bundle("05-policies-and-compliance.md", "Policies (drafts for solicitor review), registers and deadlines",
       files_in("office/policies") + ["compliance/deadlines.md", "compliance/registers/risk-register.md"])
bundle("06-aat-academy-level-2.md", "AAT Level 2 academy (practice material)",
       ["academy/README.md", "academy/progress.md"] + [f for f in sorted(str(p.relative_to(ROOT)) for p in (ROOT / "academy/level-2").rglob("*.md")) if not f.endswith("mock.md")])
bundle("07-demo-clients-and-books.md", "DEMO clients and LedgerPeak's own books (fictional, for practice)",
       ["clients/demo-harrow-hill-cafe/README-DEMO.md", "clients/demo-harrow-hill-cafe/01-client-profile.md",
        "clients/demo-harrow-hill-cafe/bank/2026-09-bank.csv", "finance/ledgerpeak-books/journal.md", "finance/ledgerpeak-books/trial-balance.md"])
bundle("08-roadmap-and-finance-plan.md", "Road to launch and the finance plan",
       ["office/roadmap.md", "finance/budget.md", "finance/cashflow-forecast.md", "leads/pipeline.csv"])
