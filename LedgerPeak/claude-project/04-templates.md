# Templates (client folder and office)

The engagement letter is a Word file in the Claude Code version; its headings are: scope, fees, your responsibilities, our responsibilities, anti-money laundering, data protection, termination, complaints, limitation of liability, signatures.


---

<!-- file: clients/_TEMPLATE/01-client-profile.md -->

# Client profile: {{CLIENT_NAME}}

> Guide: fill in at onboarding (sophie-bennett). Leave unknowns as [to confirm]. No ID, NI or bank numbers here.

Created: {{DATE}}

| Field | Detail |
|---|---|
| Client name | {{CLIENT_NAME}} |
| Business type | sole trader / landlord / partnership / limited company |
| Trade | |
| Main contact | |
| Email | |
| Phone | |
| Address (business) | |
| Year end | DD/MM |
| VAT status | not registered / registered (scheme: standard / flat rate / cash) |
| VAT quarter ends | |
| MTD for Income Tax status | not in scope / in scope from DD/MM/YYYY / signed up |
| Qualifying income band | under £30,000 / £30,000 to £50,000 / over £50,000 |
| Software | Xero / QuickBooks / FreeAgent / spreadsheet / other |
| Package | Starter £95 / MTD Ready £165 / Business £325 / Catch-up |
| Monthly fee | £ |
| Start date | DD/MM/YYYY |
| Risk rating | see 02-aml-due-diligence.md |
| Next deadline | DD/MM/YYYY (what) |
| Status | onboarding / active / paused / left |



---

<!-- file: clients/_TEMPLATE/02-aml-due-diligence.md -->

# AML customer due diligence: {{CLIENT_NAME}}

> Guide: complete before any work starts. Record that checks were done and where evidence is kept. NEVER record passport, driving licence, NI, bank or card numbers. Write "ID checked, see paper/secure file".

Date started: {{DATE}}   Completed by: sophie-bennett (draft)   Approved by Parth: [ ] DD/MM/YYYY

## 1. Identity
| Check | Done | Date | Evidence location / note |
|---|---|---|---|
| Photo ID seen (original or certified/electronic) | [ ] | | ID checked, see paper/secure file |
| Proof of address (dated within 3 months) | [ ] | | |
| Face-to-face or video meeting | [ ] | | |
| Companies House check (if company) | [ ] | | |
| Beneficial owners over 25% identified (if company) | [ ] | | |
| Sanctions list search (GOV.UK UK sanctions list) | [ ] | | |
| PEP check | [ ] | | |
| Adverse media search | [ ] | | |

## 2. Business and funds
- Nature of business:
- Expected turnover band:
- Source of funds / wealth:
- Cash intensive? yes / no
- Reason for engaging LedgerPeak:

## 3. Risk rating
Rating: low / medium / high

| Factor | Present? | Note |
|---|---|---|
| Cash-intensive business | | |
| High-risk sector or country links | | |
| Complex ownership | | |
| Non-face-to-face only | | |
| PEP or close associate | | |
| Reluctance to provide information | | |

Reasons for rating:

Enhanced due diligence needed? yes / no (why)

## 4. Review
Next review date: high 6 months / medium 12 months / low 24 months -> DD/MM/YYYY



---

<!-- file: clients/_TEMPLATE/04-onboarding-checklist.md -->

# Onboarding checklist: {{CLIENT_NAME}}

> Guide: tick as you go. Do not start bookkeeping until items 1 to 4 are done.

| # | Item | Done | Date | Note |
|---|---|---|---|---|
| 1 | AML due diligence complete and approved | [ ] | | |
| 2 | Engagement letter signed by client and Parth | [ ] | | |
| 3 | Client added to risk register | [ ] | | |
| 4 | First invoice / direct debit set up | [ ] | | |
| 5 | Software access granted (user invite, not shared password) | [ ] | | |
| 6 | Bank feed connected or statements received | [ ] | | |
| 7 | Prior records requested (last return, TB, VAT returns) | [ ] | | |
| 8 | Authorisation to act with HMRC (agent services account / 64-8 equivalent) | [ ] | | |
| 9 | VAT and MTD status confirmed | [ ] | | |
| 10 | Deadlines added to compliance/deadlines.md | [ ] | | |
| 11 | Welcome pack sent (after Parth approves) | [ ] | | |



---

<!-- file: clients/_TEMPLATE/05-monthly-close-checklist.md -->

# Monthly close checklist: {{CLIENT_NAME}}   Month: MM/YYYY

> Guide: leo-hartley works through this; james-whitfield writes the summary; Parth approves.

| # | Step | Owner | Done |
|---|---|---|---|
| 1 | Import bank transactions | leo | [ ] |
| 2 | Categorise every transaction (workings in journal.md) | leo | [ ] |
| 3 | Reconcile bank to statement closing balance | leo | [ ] |
| 4 | Clear or query suspense items | leo | [ ] |
| 5 | Post accruals / prepayments if Business package | leo | [ ] |
| 6 | Trial balance: debits = credits | leo | [ ] |
| 7 | Queries listed in 06-queries-to-client.md | leo | [ ] |
| 8 | Monthly summary written | arjun | [ ] |
| 9 | Parth review and approval (12-review-log.md) | Parth | [ ] |



---

<!-- file: clients/_TEMPLATE/06-queries-to-client.md -->

# Queries to client: {{CLIENT_NAME}}

> Guide: one row per query. Parth sends; nobody else contacts the client.

| # | Date raised | Transaction (date, amount, description) | Question | Answer | Resolved |
|---|---|---|---|---|---|



---

<!-- file: clients/_TEMPLATE/07-monthly-summary-template.md -->

# Monthly summary: {{CLIENT_NAME}}   Month: MM/YYYY

> Guide: one page, plain English, no jargon. Draft by james-whitfield; Parth approves before sending.

| | This month | Last month | Change |
|---|---|---|---|
| Income | £ | £ | £ |
| Costs | £ | £ | £ |
| Profit | £ | £ | £ |
| Cash in bank at month end | £ | £ | £ |

## What changed
-
## Things to watch
1.
2.
3.
## Questions for you
-



---

<!-- file: clients/_TEMPLATE/08-vat-return-workings.md -->

# VAT return workings: {{CLIENT_NAME}}   Period: DD/MM/YYYY to DD/MM/YYYY

> Guide: james-whitfield fills each box with the transactions behind it. Parth files; nobody else submits.

VAT scheme:          Source of rates checked: GOV.UK "VAT rates" page, date checked:

| Box | Description | Amount | Workings |
|---|---|---|---|
| 1 | VAT due on sales and other outputs | £ | |
| 2 | VAT due on acquisitions from EU (NI only) | £ | |
| 3 | Total VAT due (box 1 + box 2) | £ | |
| 4 | VAT reclaimed on purchases and other inputs | £ | |
| 5 | Net VAT to pay or reclaim (difference between box 3 and box 4) | £ | |
| 6 | Total value of sales excluding VAT | £ | |
| 7 | Total value of purchases excluding VAT | £ | |
| 8 | Supplies of goods to EU excluding VAT (NI only) | £ | |
| 9 | Acquisitions of goods from EU excluding VAT (NI only) | £ | |

## Check before filing
- [ ] Every month in the period reconciled to bank statement
- [ ] Suspense cleared
- [ ] VAT rate checked on a sample of 10 transactions
- [ ] Figures agree to trial balance VAT control account
- [ ] Parth approved in 12-review-log.md



---

<!-- file: clients/_TEMPLATE/09-mtd-quarterly-update.md -->

# MTD for Income Tax quarterly update: {{CLIENT_NAME}}

> Guide: james-whitfield prepares. Confirm the quarterly period and deadline on GOV.UK and write the source and date checked. Parth submits through compatible software.

Tax year:          Quarter: 1 / 2 / 3 / 4      Period: DD/MM/YYYY to DD/MM/YYYY
Deadline (source, date checked):

## Self-employment
| Category | This quarter | Year to date |
|---|---|---|
| Turnover | £ | £ |
| Other income | £ | £ |
| Cost of goods | £ | £ |
| Staff costs | £ | £ |
| Travel | £ | £ |
| Premises | £ | £ |
| Admin / office | £ | £ |
| Professional fees | £ | £ |
| Other expenses | £ | £ |

## UK property (if any)
| Category | This quarter | Year to date |
|---|---|---|
| Rents received | £ | £ |
| Repairs and maintenance | £ | £ |
| Finance costs (restricted) | £ | £ |
| Other expenses | £ | £ |

## Check before filing
- [ ] Records digital and reconciled
- [ ] Categories mapped consistently with last quarter
- [ ] Parth approved



---

<!-- file: clients/_TEMPLATE/10-year-end-pack.md -->

# Year-end pack: {{CLIENT_NAME}}   Year ended DD/MM/YYYY

> Guide: collect everything needed to finalise the year. Final accounts or tax return preparation beyond bookkeeping may need a qualified accountant; flag it.

| Item | Received | Note |
|---|---|---|
| All bank statements to year end | [ ] | |
| Final bank reconciliation | [ ] | |
| Sales invoices / takings records | [ ] | |
| Purchase invoices and receipts | [ ] | |
| Fixed asset additions and disposals | [ ] | |
| Stock count at year end | [ ] | |
| Debtors and creditors lists | [ ] | |
| Loans and finance statements | [ ] | |
| Use of home / vehicle split (sole traders) | [ ] | |
| Drawings | [ ] | |
| Trial balance | [ ] | |



---

<!-- file: clients/_TEMPLATE/11-invoices-and-payments.md -->

# LedgerPeak invoices and payments: {{CLIENT_NAME}}

> Guide: emily-brooks keeps this up to date. No bank details here.

| Invoice no | Date | Description | Amount | Due date | Paid date | Status |
|---|---|---|---|---|---|---|



---

<!-- file: clients/_TEMPLATE/12-review-log.md -->

# Review log: {{CLIENT_NAME}}

> Guide: Parth's approvals and edits. Agents add "requested" rows; only Parth fills "Approved". After any edit, log the lesson in memory/style-lessons.md.

| Date | Document | Requested by | Parth's decision | Edits made | Lesson logged |
|---|---|---|---|---|---|



---

<!-- file: office/templates/chart-of-accounts.md -->

# Chart of accounts (simple small business)

| Code | Account | Type | Normal balance |
|---|---|---|---|
| 1200 | Bank current account | Asset | Debit |
| 1100 | Trade debtors | Asset | Debit |
| 0030 | Equipment | Asset | Debit |
| 2100 | Trade creditors | Liability | Credit |
| 2200 | VAT control | Liability | Credit |
| 3000 | Capital | Equity | Credit |
| 3050 | Drawings | Equity | Debit |
| 4000 | Sales | Income | Credit |
| 4900 | Other income | Income | Credit |
| 5000 | Purchases / cost of sales | Expense | Debit |
| 7000 | Wages | Expense | Debit |
| 7100 | Rent | Expense | Debit |
| 7200 | Utilities | Expense | Debit |
| 7400 | Travel and motor | Expense | Debit |
| 7500 | Telephone and internet | Expense | Debit |
| 7600 | Professional fees | Expense | Debit |
| 7700 | Software and subscriptions | Expense | Debit |
| 7900 | Bank charges | Expense | Debit |
| 8000 | Advertising | Expense | Debit |
| 8200 | Insurance | Expense | Debit |
| 9999 | Suspense | Temporary | either (must be cleared) |

Memory aid DEAD CLIC: Debits are Expenses, Assets, Drawings; Credits are Liabilities, Income, Capital.



---

<!-- file: office/templates/invoice.md -->

# INVOICE LP-YYYY-NNN

LedgerPeak, Harrow, North West London
Date: DD/MM/YYYY      Due: DD/MM/YYYY (14 days)
To: [client]

| Description | Amount |
|---|---|
| [Package] bookkeeping, [month] | £ |
| Total | £ |

Payment: bank details as on the official invoice. Reference: LP-YYYY-NNN.
LedgerPeak is not VAT registered. [Update if registered.]



---

<!-- file: office/templates/proposal.md -->

# Proposal for [business name]

Prepared by LedgerPeak, bookkeeper, Harrow. Date: DD/MM/YYYY

## What you told us
-
## What we will do
-
## Recommended package
| Package | Monthly | Includes |
|---|---|---|
| Starter | £95 | Bank reconciliation, categorisation, monthly summary |
| MTD Ready | £165 | Starter plus MTD for Income Tax quarterly update preparation |
| Business | £325 | MTD Ready plus VAT returns, credit control support, monthly call |
| Catch-up | from £250 one-off | Bringing old records up to date |

Prices are starting prices and will be confirmed after we see your records.
## Next steps
1. Short call  2. ID checks (required by law)  3. Engagement letter  4. Start



---

<!-- file: office/templates/welcome-email.md -->

Subject: Welcome to LedgerPeak

Hi [first name],

Thank you for choosing LedgerPeak. To get started, please send:
1. [records list]
2. Access to [software] (an invite to my email, please do not share passwords)

I will be in touch by [date].

Kind regards,
Parth Prajapati
LedgerPeak, bookkeeper, Harrow
