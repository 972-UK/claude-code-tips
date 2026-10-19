# LedgerPeak Office

Your bookkeeping firm as a folder. Eleven AI staff in six departments live in `.claude/agents/`, and you give them work with slash commands in Claude Code. They prepare drafts only. Nothing is sent to anyone until you approve it.

## Your team

| Department | Person | What they do |
|---|---|---|
| Leadership | Grace Whitmore, Operations Manager | Takes any task, plans it, gives each part to the right department, checks quality, hands you one result |
| Leadership | Ava Sterling, Chief of Staff | Morning brief, deadlines, tracker |
| Growth | Henry Collins, Sales | Leads, outreach emails, proposals |
| Growth | Charlotte Quinn, Marketing | Posts, Google Business Profile, reviews |
| Client Services | Sophie Bennett, Onboarding & AML | New clients, ID and risk checks, engagement letters |
| Client Services | Emily Brooks, Credit Control | Invoices, chasers |
| Bookkeeping & Reporting | Leo Hartley, Senior Bookkeeper | Books, reconciliations, month-end close |
| Bookkeeping & Reporting | James Whitfield, Reporting Analyst | Summaries, VAT, MTD |
| Legal & Compliance | Victor Hale | Legal questions, policies, when to see a solicitor |
| Innovation & Learning Lab | Theo Ashford, Head of Innovation | Finds what's new in the world, learns new skills, teaches the whole team simply |
| Innovation & Learning Lab | Iris Bell, AAT Tutor | Teaches you AAT |

## Give the office any task

Type `/task` and say what you want, for example `/task onboard a new plumber client and prepare their first MTD update`. Grace plans it, each department does its part, Grace checks it, and you get one summary to approve.

Keeping the team up to date: `/learn` (Theo checks what has changed) and `/teach <skill>` (Theo teaches everyone). Every agent reads its own file in `knowledge/briefings/` before each task, so what Theo teaches sticks.

## Watch them work

Open `office/dashboard/index.html` and stay on **Live office**. When you give a task in Claude Code, the person doing each step lights up at their desk. They type, their screen scrolls, and a speech bubble shows what they're doing. A green tick appears when they finish. The page updates itself every 3 seconds. This works through the hooks in `.claude/settings.json`, which call `scripts/office_hook.py`. Press **Watch a demo task** to see a full task play out without running anything.

On Windows, if `python3` isn't recognised, change `python3` to `python` in `.claude/settings.json`.

## How to start tomorrow morning

1. Open a terminal in this `LedgerPeak` folder and type `claude`.
2. Open `office/dashboard/index.html` beside it so you can watch the team.
3. Type `/morning`. Ava gives you today's priorities, deadlines in the next 14 days, leads to chase and tonight's study task.
4. Try the DEMO client end to end with `/close-month demo-harrow-hill-cafe`. Leo does the books with workings, James writes the summary, then it stops for your approval. Read `clients/demo-harrow-hill-cafe/README-DEMO.md` first to see the traps it should catch.
5. Spend 30 minutes on `/study`. Iris teaches one AAT topic and marks five questions.
6. Before you take a real client, work through `office/policies/pre-launch-legal-checklist.md`. Item 1 is reading your employment contract.
7. At the end of the evening, type `/log`.

## Commands

| Command | Who | What it does |
|---|---|---|
| `/morning` | Ava | Morning brief |
| `/new-client <name>` | Sophie | Client folder, AML checks, risk rating, engagement letter, welcome email draft |
| `/close-month <client>` | Leo then James | Books, reconciliation, summary, then stops for your approval |
| `/vat <client>` | James | VAT boxes 1 to 9 with workings and a check-before-filing list |
| `/mtd <client>` | James | MTD quarterly figures with workings |
| `/chase` | Emily | Aged debtors and chaser drafts |
| `/outreach <trade> <area>` | Henry | Lead list plan and three PECR-aware emails |
| `/post` | Charlotte | This week's posts and a Google Business update |
| `/legal <question>` | Victor | GOV.UK-sourced answer, and when you need a solicitor |
| `/study` | Iris | Tonight's AAT lesson and quiz |
| `/mock <unit>` | Iris | Timed mock, e.g. `/mock introduction-to-bookkeeping` |
| `/log` | any | Adds today's work to the work log |
| `/task <anything>` | Grace and the departments | Any task, planned, delegated, checked |
| `/learn [topic]` | Theo | What's new in the world, recorded and taught to the team |
| `/teach <skill>` | Theo | Teaches the team a new skill with a playbook |

## Scripts

- New client by hand: `scripts/new-client.sh "Client Name"` (Mac/Linux) or `.\scripts\new-client.ps1 "Client Name"` (Windows).
- Refresh the dashboard: `scripts/refresh-dashboard.sh` or `.\scripts\refresh-dashboard.ps1`, then reload the page. This needs Python 3.
- Check the office still works: `python3 scripts/self_test.py`.

## Where to edit things yourself

- Agents' desk status on the dashboard: `office/dashboard/data/agents.json`
- Leads: `leads/pipeline.csv` (status: lead, contacted, call booked, proposal, won, lost)
- Deadlines: `compliance/deadlines.md` (one line each: `DD/MM/YYYY | item | who | owner`)
- AAT results: `academy/progress.md`
- Compliance ticks: change `[ ]` to `[x]` in `office/policies/pre-launch-legal-checklist.md`

## Watching your staff work (Pixel Agents)

Pixel Agents shows every Claude Code session and subagent as a pixel character at a desk. When Leo is reconciling, you will see him typing.

- VS Code: install "Pixel Agents" from the VS Code Marketplace, open the Pixel Agents panel, click **+ Agent**, and pick this `LedgerPeak` folder.
- Without VS Code: run `npx pixel-agents` in a terminal and open the address it prints. Needs Node.js 20 or later.

Subagents (Ava, Leo and the rest) appear as extra characters while a command is running.

## Before you go live

- Every policy in `office/policies/` is marked DRAFT. Have a solicitor check them.
- Figures marked "verify" (ICO fee, HMRC AML fees, filing deadlines) came from secondary sources checked on 19/10/2026. Confirm them on GOV.UK.
- The AAT unit list came from secondary sources checked on 19/10/2026. Confirm it on aat.org.uk before you book exams.
- Delete the DEMO client and DEMO leads once you have real ones.
