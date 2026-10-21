# LedgerPeak

LedgerPeak is a bookkeeping practice for small businesses in Harrow and North West London, operated by Parth Prajapati with a team of seventeen AI specialists across twelve departments. The team prepares, reviews and drafts. Parth approves every deliverable before it leaves the firm.

**Current status: pre-registration.** The firm is in its build-and-test stage. Every workflow runs on DEMO clients, and the brand, systems, pricing and roadmap are prepared in full. When Parth registers, one setting in `CLAUDE.md` changes and the firm is ready to take clients.

## Organisation

| Department | Staff | Responsibilities |
|---|---|---|
| Executive Office | Parth Prajapati, Chief Executive | Direction, approvals, signing officer |
| | Grace Whitmore, Operations Manager | Receives every task, plans it, assigns departments, signs off |
| | Ava Sterling, Chief of Staff | Daily brief, calendar, roadmap tracking |
| Strategy & Business Development | Eleanor Price, Director of Strategy | Market research, competitors, pricing strategy, growth plan, roadmap |
| Sales & Marketing | Henry Collins, Head of Sales | Lead generation, outreach, discovery calls, proposals |
| | Charlotte Quinn, Marketing Manager | Brand, website copy, social posts, Google Business Profile |
| Client Experience | Amelia Hart, Client Relationship Manager | Client communication, check-ins, complaints, waiting list |
| Client Onboarding & AML | Sophie Bennett, Onboarding and AML Manager | Due diligence, risk rating, engagement letters |
| Bookkeeping & Accounts | Leo Hartley, Senior Bookkeeper | Transaction processing, double entry, reconciliations, month-end |
| | James Whitfield, Reporting Analyst | Management summaries, VAT returns, MTD quarterly updates |
| Tax & Payroll | Daniel Foster, Tax and Payroll Support Specialist | Self Assessment packs, CIS records, landlord schedules, payroll records |
| Finance & Credit Control | Edward Lancaster, Finance Director | The firm's budget, cash flow, margins and management accounts |
| | Emily Brooks, Credit Controller | Invoicing, aged debtors, payment reminders |
| Quality & Risk | Harriet Ellis, Head of Quality and Risk | Reviews every deliverable, maintains the risk register |
| Legal & Compliance | Victor Hale, Head of Legal and Compliance | AML, UK GDPR, contracts, policies, when to instruct a solicitor |
| Technology & Automation | William Hayes, Head of Technology | Software, bank feeds, data security, automation |
| Innovation & Learning | Theo Ashford, Head of Innovation | Monitors regulatory and industry change, briefs every department |
| | Iris Bell, AAT Tutor | AAT study programme, quizzes and mock assessments |

## How work flows

1. Parth assigns a task (`/task …`).
2. Grace Whitmore checks the firm's current mode, plans the work and assigns each step to the right department.
3. Departments complete their steps. Independent steps run in parallel.
4. Harriet Ellis reviews the output against the quality checklist.
5. Grace signs off and gives Parth one summary with the decisions required.
6. Parth approves. Nothing is sent or filed without that approval.

Theo Ashford keeps the firm current: `/learn` records what has changed, and `/teach` briefs each affected department. Every staff member reads their briefing before starting work.

## Starting each evening

1. Open a terminal in this folder and run `claude`.
2. Open `office/dashboard/hq.html` beside it to watch the office.
3. Run `/morning` for the daily brief, which leads with the next roadmap actions.
4. Choose one roadmap action and assign it with `/task`.
5. Spend 30 minutes on `/study`.
6. Close with `/log`.

## Commands

| Command | Department | Purpose |
|---|---|---|
| `/task <description>` | Operations | Any task, planned, assigned, reviewed and signed off |
| `/morning` | Executive Office | Daily brief |
| `/roadmap` | Executive Office, Strategy | Progress on the road to launch |
| `/strategy <topic>` | Strategy | Market, competitor, pricing or growth brief |
| `/outreach <trade> <area>` | Sales | Lead plan and compliant outreach drafts |
| `/post` | Marketing | The week's posts and a Google Business update |
| `/client-care <message>` | Client Experience | Client or waiting-list message drafts |
| `/new-client <name>` | Onboarding and AML | Client file, due diligence, engagement letter, welcome draft |
| `/practice <DEMO client>` | All departments | Full practice month on a DEMO client |
| `/close-month <client>` | Bookkeeping | Books, reconciliation, summary, then approval |
| `/vat <client>` | Bookkeeping | VAT return workings and pre-filing checks |
| `/mtd <client>` | Bookkeeping | MTD quarterly update workings |
| `/tax-pack <client>` | Tax and Payroll | Self Assessment or CIS preparation pack |
| `/finance [request]` | Finance | Budget, cash flow, margin checks |
| `/chase` | Credit Control | Aged debtors and payment reminders |
| `/review <file>` | Quality and Risk | Quality review with a pass or return decision |
| `/legal <question>` | Legal and Compliance | Sourced answer and when to instruct a solicitor |
| `/systems <request>` | Technology | Software, security and automation guidance |
| `/learn [topic]` | Innovation | What has changed, with briefings |
| `/teach <skill>` | Innovation | Teaches a new skill to the departments affected |
| `/study`, `/mock <unit>` | Innovation (AAT) | AAT lessons and timed mocks |
| `/log` | Any | Records the day's work |

## Pre-registration mode

While the mode is ON (see `CLAUDE.md`), the firm can build the brand, systems, pricing and policies; research the market; practise on DEMO clients; keep its own books; hold a consent-based waiting list; and support AAT study. It does not do bookkeeping, tax or payroll work for real people or businesses, take fees, collect identity documents, or advertise as open for business. Anti-money laundering supervision must be in place before bookkeeping services are provided. The steps are listed in `office/roadmap.md`, stage 4.

## The office view

- `office/dashboard/hq.html`: LedgerPeak HQ, the main office. An architect-style floor plan with every department in its own furnished room and each specialist at their desk, plus specialist screens, the road to launch, the skills library and the team directory with Grace's updates. It goes live while Claude Code runs. Rebuild it after changes with `python3 scripts/build_hq.py`.
- `office/dashboard/office.html`: the pixel-art office. It shows thirteen rooms and every staff member, with a Command Centre (live feed, task board, expertise, briefings, work log, team) and a staff roster. It updates live while Claude Code runs, through the hooks in `.claude/settings.json`.
- `office/dashboard/index.html`: the reports view, with KPIs, pipeline, clients, deadlines, academy and compliance.
- On Windows, if `python3` is not recognised, change it to `python` in `.claude/settings.json`.

## Claude Project

The `claude-project/` folder contains everything needed to run the firm from a Project on claude.ai, including from a phone. See `claude-project/SETUP.md`.

## Maintenance

- New client folder: `scripts/new-client.sh "Client Name"` (Mac/Linux) or `.\scripts\new-client.ps1 "Client Name"` (Windows).
- Refresh dashboard data: `scripts/refresh-dashboard.sh` or `.\scripts\refresh-dashboard.ps1`.
- Office health check: `python3 scripts/self_test.py`.

## Before going live

All policies in `office/policies/` are drafts for a solicitor to review. Fees and figures marked "verify" come from secondary sources checked on 19/10/2026 and must be confirmed on GOV.UK, the ICO website or the AAT website.
