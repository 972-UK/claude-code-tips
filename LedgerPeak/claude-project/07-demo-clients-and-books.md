# DEMO clients and LedgerPeak's own books (fictional, for practice)




---

<!-- file: clients/demo-harrow-hill-cafe/README-DEMO.md -->

# DEMO client: Harrow Hill Café

Everything in this folder is fictional and marked DEMO. Use it to test the office end to end:

1. `/close-month demo-harrow-hill-cafe` : Leo categorises `bank/2026-09-bank.csv`, reconciles to the closing balance £5,445.50, posts double entry; James writes the summary; then it stops for your approval.
2. `/vat demo-harrow-hill-cafe` : quarter to 30/09/2026. Only September data exists, so James should flag July and August as missing (a good test of rule 2).
3. `/chase` : invoice LP-2026-002 is overdue.

Deliberate test points in the bank file:
- "Unknown transfer in REF 77812" £300 should become a query, not a guess.
- "Owner transfer to personal account" £500 is drawings.
- Rent: the landlord has not opted to tax, so no VAT to reclaim.
- Wages, rent, bank charges and card fees carry no VAT.
- Catering invoice HHC-031 £240 includes £40 VAT.



---

<!-- file: clients/demo-harrow-hill-cafe/01-client-profile.md -->

**DEMO, fictional data for testing.**

# Client profile: DEMO Harrow Hill Café

> Guide: fill in at onboarding (sophie-bennett). Leave unknowns as [to confirm]. No ID, NI or bank numbers here.

Created: 19/10/2026

| Field | Detail |
|---|---|
| Client name | DEMO Harrow Hill Café |
| Business type | sole trader (DEMO) |
| Trade | Café and small catering orders |
| Main contact | DEMO Sam Example |
| Email | demo@example.com |
| Phone | DEMO 020 0000 0000 |
| Address (business) | DEMO, Harrow on the Hill (fictional) |
| Year end | 05/04 |
| VAT status | registered (scheme: standard) |
| VAT quarter ends | 31/12, 31/03, 30/06, 30/09 |
| MTD for Income Tax status | in scope from 06/04/2026 (DEMO assumption) |
| Qualifying income band | over £50,000 |
| Software | spreadsheet (DEMO) |
| Package | Business £325 |
| Monthly fee | £325 |
| Start date | 01/09/2026 |
| Risk rating | medium (see 02-aml-due-diligence.md) |
| Next deadline | 07/11/2026 (VAT return Q/E 30/09/2026, verify) |
| Status | active (DEMO) |



---

<!-- file: clients/demo-harrow-hill-cafe/bank/2026-09-bank.csv -->

date,description,amount
01/09/2026,Opening balance 31/08/2026 per statement (memo line; cash book agreed at 31/08),3850.00
01/09/2026,DEMO card takings settlement,612.40
02/09/2026,DEMO Bean Supply Co - coffee beans inv BS-2214,-540.00
03/09/2026,DEMO card takings settlement,588.10
04/09/2026,Rent - DEMO Hill Properties (commercial; landlord not opted to tax),-1200.00
05/09/2026,Cash takings banked,420.00
08/09/2026,DEMO card takings settlement,701.25
09/09/2026,DEMO Dairy Fresh - milk,-186.00
10/09/2026,Pinner Office Ltd (DEMO) - catering inv HHC-031,240.00
11/09/2026,DEMO Energy Ltd electricity DD,-264.00
12/09/2026,Cash takings banked,515.00
15/09/2026,DEMO card takings settlement,690.30
16/09/2026,Staff wages DEMO,-1450.00
17/09/2026,DEMO Packaging Ltd - cups and lids,-216.00
18/09/2026,Owner transfer to personal account,-500.00
19/09/2026,Cash takings banked,480.00
22/09/2026,DEMO card takings settlement,655.80
23/09/2026,Card machine fees,-38.45
24/09/2026,DEMO Phone & Broadband DD,-48.00
25/09/2026,Unknown transfer in REF 77812,300.00
26/09/2026,Cash takings banked,460.00
29/09/2026,DEMO card takings settlement,712.60
30/09/2026,LedgerPeak bookkeeping LP-2026-001,-325.00
30/09/2026,Bank charges,-12.50
30/09/2026,Closing balance per statement 5445.50 (memo line; not a transaction),



---

<!-- file: finance/ledgerpeak-books/journal.md -->

# Journal with workings (DEMO)

| Date | Debit | Credit | Amount | Plain English |
|---|---|---|---|---|
| 01/09/2026 | 1200 Bank | 3000 Capital | £1,000.00 | Money in from owner. Bank up (debit), capital up (credit). |
| 01/09/2026 | 1100 Trade debtors | 4000 Sales | £325.00 | Invoice LP-2026-001 raised. Customer owes us (asset up, debit); we earned income (credit). |
| 03/09/2026 | 7700 Software | 1200 Bank | £30.00 | Expense up (debit); bank down (credit). |
| 05/09/2026 | 7600 Professional fees | 1200 Bank | £52.00 | Expense up (debit); bank down (credit). |
| 10/09/2026 | 8200 Insurance | 1200 Bank | £180.00 | Expense up (debit); bank down (credit). Annual policy: at year end, think about prepayments (Level 3 topic). |
| 30/09/2026 | 1200 Bank | 1100 Trade debtors | £325.00 | Customer paid. Bank up (debit); debtor cleared (credit). |
| 01/10/2026 | 1100 Trade debtors | 4000 Sales | £325.00 | Invoice LP-2026-002 raised. |

LedgerPeak is not VAT registered (DEMO assumption; check the VAT registration threshold on GOV.UK as turnover grows).



---

<!-- file: finance/ledgerpeak-books/trial-balance.md -->

# Trial balance at 01/10/2026 (DEMO)

| Account | Debit | Credit |
|---|---|---|
| 1200 Bank (1,000 - 30 - 52 - 180 + 325) | £1,063.00 | |
| 1100 Trade debtors (325 - 325 + 325) | £325.00 | |
| 3000 Capital | | £1,000.00 |
| 4000 Sales (325 + 325) | | £650.00 |
| 7700 Software and subscriptions | £30.00 | |
| 7600 Professional fees | £52.00 | |
| 8200 Insurance | £180.00 | |
| Total | £1,650.00 | £1,650.00 |

Debits equal credits. Profit so far: £650 - £262 = £388.
