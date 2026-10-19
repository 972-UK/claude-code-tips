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
