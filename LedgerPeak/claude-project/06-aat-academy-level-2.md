# AAT Level 2 academy (practice material)




---

<!-- file: academy/README.md -->

# LedgerPeak Academy (AAT)

Practice material written for Parth. It is not official AAT material. Always check the current specification on aat.org.uk.

## Unit list and source
Level 2 Certificate in Accounting (Q2022 specification): four mandatory units, 255 guided learning hours, 340 hours total qualification time. Three unit assessments plus a synoptic assessment for The Business Environment. Unit assessment pass mark 70%.
Sources: learnsignal.com "AAT Level 2 Syllabus: Every Unit Explained" (states it was checked against AAT's Q2022 specification) and college course pages (Central College Nottingham, New College). Checked 19/10/2026. I could not reach aat.org.uk directly in this search, so confirm the unit list there before booking exams.

| Level | Folder | Unit |
|---|---|---|
| 2 | level-2/introduction-to-bookkeeping | Introduction to Bookkeeping |
| 2 | level-2/principles-of-bookkeeping-controls | Principles of Bookkeeping Controls |
| 2 | level-2/principles-of-costing | Principles of Costing |
| 2 | level-2/the-business-environment | The Business Environment (synoptic) |
| 3 | level-3/ | Built by iris-bell after Level 2 is under way; she will check the current Level 3 unit list on aat.org.uk first |
| 4 | level-4/ | As above for Level 4 |

## Each unit folder has
- `study-guide.md`: plain-English guide
- `worked-examples.md`: three worked examples from a small UK business
- `practice-questions.md`: 20 questions, answers at the bottom
- `mock.md`: a timed mock for `/mock`
- LedgerPeak task link at the end of the study guide

Run `/study` for tonight's topic and `/mock <unit folder>` for a timed test.



---

<!-- file: academy/progress.md -->

# AAT progress

Updated by iris-bell after every /study and /mock. Edit by hand if you sit a real exam.

## Units
| Level | Unit | Status | Score | Weak topics |
|---|---|---|---|---|
| 2 | Introduction to Bookkeeping | not started | - | - |
| 2 | Principles of Bookkeeping Controls | not started | - | - |
| 2 | Principles of Costing | not started | - | - |
| 2 | The Business Environment | not started | - | - |

Status values: not started, studying, mock passed, booked, passed.

## Study sessions
| Date | Topic | Score | Notes |
|---|---|---|---|



---

<!-- file: academy/level-2/introduction-to-bookkeeping/practice-questions.md -->

# Introduction to Bookkeeping: 20 practice questions

Try them all before scrolling to the answers.

1. Which document does a seller issue to reduce the amount a customer owes?
2. Name the book of prime entry for credit sales.
3. Net £350, VAT 20%. What is the VAT and gross?
4. Gross £144 including VAT at 20%. What is the VAT?
5. List price £800, trade discount 15%, VAT 20%. Calculate net, VAT and gross.
6. Owner pays £5,000 of personal savings into the business bank. Double entry?
7. Business buys a laptop for £900 cash (ignore VAT). Double entry?
8. Is the laptop capital or revenue expenditure?
9. Owner takes £300 from the business bank for personal use. Double entry?
10. Pay rent £650 by bank. Double entry?
11. What does DEAD CLIC stand for?
12. A customer pays £240 owed. Double entry in general ledger?
13. Which ledger holds one account per supplier?
14. Petty cash float £150; vouchers total £63.40. How much is the top-up?
15. Debit side total £2,400, credit side total £1,750. What is the balance c/d and on which side is it written?
16. What is a remittance advice?
17. Sales returns of £120 gross (£100 net, £20 VAT) from a credit customer. General ledger entries?
18. Which document lists all transactions with a customer and the balance owed?
19. Does a trial balance that agrees prove there are no errors? Give one reason.
20. Purchase of van fuel £60 by debit card. Capital or revenue, and double entry?

---

## Answers

1. A credit note.
2. Sales daybook.
3. VAT £70, gross £420.
4. £144 x 1/6 = £24.
5. Discount £120, net £680, VAT £136, gross £816.
6. Dr Bank £5,000; Cr Capital £5,000.
7. Dr Office equipment £900; Cr Bank £900.
8. Capital expenditure.
9. Dr Drawings £300; Cr Bank £300.
10. Dr Rent £650; Cr Bank £650.
11. Debits: Expenses, Assets, Drawings. Credits: Liabilities, Income, Capital.
12. Dr Bank £240; Cr Sales ledger control £240.
13. Purchases (payables) ledger.
14. £63.40.
15. £650 written on the credit side as balance c/d; it is brought down as a debit balance b/d.
16. A document sent by a customer with a payment saying which invoices are being paid.
17. Dr Sales returns £100; Dr VAT control £20; Cr Sales ledger control £120.
18. Statement of account.
19. No. For example, an error of omission (transaction not recorded at all) does not affect agreement.
20. Revenue. Dr Motor expenses £60; Cr Bank £60.



---

<!-- file: academy/level-2/introduction-to-bookkeeping/study-guide.md -->

# Introduction to Bookkeeping: study guide

Practice material, not official AAT content. Check the current unit specification on aat.org.uk.

## What this unit is about
Recording the day-to-day money of a business correctly: invoices, credit notes, receipts and payments, into books of prime entry, then into ledgers using double entry.

## Key ideas
1. **Documents**: sales invoice (we sell on credit), credit note (we reduce an invoice), receipt, remittance advice, purchase order, goods received note, statement of account.
2. **Books of prime entry** (daybooks): sales daybook, sales returns daybook, purchases daybook, purchases returns daybook, cash book, petty cash book, journal. Transactions go here first, then the totals are posted to the ledgers.
3. **Ledgers**: general ledger (all the accounts), sales ledger (one account per customer, also called receivables ledger), purchases ledger (one per supplier, payables ledger).
4. **Double entry**: every transaction has a debit and an equal credit. Memory aid DEAD CLIC: Debit Expenses, Assets, Drawings; Credit Liabilities, Income, Capital. An increase goes on the normal-balance side.
5. **VAT on invoices**: net + VAT = gross. At 20% standard rate, VAT = net x 20%, and VAT from a gross figure = gross x 1/6 (check current rates on GOV.UK "VAT rates"). Trade discount is taken off before VAT. Prompt payment discount: check the current AAT treatment in the specification.
6. **Cash book**: can be both a book of prime entry and part of the ledger. Receipts side (debit) and payments side (credit) with analysis columns.
7. **Petty cash**: imprest system. Top up the float to the fixed amount with the total spent.
8. **Balancing off accounts**: total both sides, put the difference as "balance c/d" on the smaller side, bring it down as "balance b/d" on the other side.
9. **Trial balance**: list of all balances; debits should equal credits.
10. **Capital vs revenue**: capital spend buys long-term assets (a van); revenue spend is running costs (fuel).

## LedgerPeak task that uses this skill
Run `/close-month demo-harrow-hill-cafe`. Leo's `journal.md` shows the double entry for every DEMO café transaction; check three of them yourself before reading his answer.



---

<!-- file: academy/level-2/introduction-to-bookkeeping/worked-examples.md -->

# Introduction to Bookkeeping: worked examples

All businesses are DEMO and fictional.

## Example 1: credit sale with VAT (DEMO Harrow Hill Café catering order)
The café invoices Pinner Office Ltd for a catering platter: net £200, VAT 20%.
- VAT = £200 x 20% = £40. Gross = £240.
- Sales daybook: customer Pinner Office Ltd, net £200, VAT £40, total £240.
- Posting totals to general ledger: Dr Sales ledger control £240; Cr Sales £200; Cr VAT control £40.
- Sales ledger: Dr Pinner Office Ltd £240.
Why: the customer owes us (asset up, debit); sales income up (credit); we owe HMRC the VAT (liability up, credit).

## Example 2: credit purchase with trade discount
The café buys coffee beans list price £500, 10% trade discount, VAT 20%.
- Trade discount £50, net £450, VAT £90, gross £540.
- Dr Purchases £450; Dr VAT control £90; Cr Purchases ledger control £540. Purchases ledger: Cr Supplier £540.

## Example 3: petty cash imprest
Float £100. Spent in the week: milk £12.50, cleaning £18.00, postage £9.50 = £40.00.
- Petty cash book analysis: Purchases £12.50, Cleaning £18.00, Postage £9.50.
- Top-up from bank: Dr Petty cash £40; Cr Bank £40. Float back to £100.



---

<!-- file: academy/level-2/principles-of-bookkeeping-controls/practice-questions.md -->

# Principles of Bookkeeping Controls: 20 practice questions

Try them all before scrolling to the answers.

1. Name an error that does not affect the trial balance where an entry is posted to the wrong account of the same type.
2. A van purchase debited to Motor expenses. Which error?
3. £54 recorded as £45 in both accounts. Which error?
4. Debit and credit entries posted the wrong way round. Which error?
5. Cash book £1,000 debit; bank shows bank charges of £20 not in cash book. Updated cash book balance?
6. Statement £2,300, unpresented cheques £400, outstanding lodgements £150. Adjusted balance?
7. What goes into a suspense account?
8. Write off a £600 debt plus £120 VAT (relief available). Journal?
9. SLCA £8,500; customer list £8,350. Give one possible cause.
10. What is a standing order?
11. Direct debit vs standing order: who controls the amount?
12. Which payment method gives same-day high-value guaranteed transfer?
13. VAT control: output VAT £3,200, input VAT £1,900. Owed to or by HMRC, how much?
14. Transposition: £1,890 posted as £1,980 on one side only. TB difference?
15. Why must journals have a narrative?
16. Opening capital journal: bank £3,000, equipment £2,000, loan £1,000. Capital?
17. Debit side of TB is £100 short. Which side is the suspense entry?
18. Name two errors that DO cause a trial balance difference.
19. A BACS receipt of £500 appears on the statement only. What do you do?
20. What is an outstanding lodgement?

---

## Answers

1. Error of commission.
2. Error of principle.
3. Error of original entry (both sides wrong by the same amount).
4. Reversal of entries.
5. £980.
6. £2,300 - £400 + £150 = £2,050.
7. A trial balance difference (or an unknown posting) until the error is found and corrected.
8. Dr Irrecoverable debts £600; Dr VAT control £120; Cr SLCA £720.
9. For example a £150 credit note posted to the customer account but omitted from the daybook, or a customer balance missed from the list.
10. A fixed regular payment set up by the payer at their bank.
11. Direct debit: the payee (recipient) collects the amount. Standing order: the payer sets a fixed amount.
12. CHAPS.
13. Owed to HMRC £1,300.
14. £90 (always divisible by 9).
15. To explain and authorise the entry for audit trail purposes.
16. Dr Bank £3,000, Dr Equipment £2,000; Cr Loan £1,000, Cr Capital £4,000.
17. Debit suspense £100.
18. Single-sided entry; entries of different amounts; balance omitted from the TB; casting error on one side (any two).
19. Enter it in the cash book: Dr Bank £500; Cr SLCA (or the right income account) £500.
20. Money paid into the bank and recorded in the cash book that has not yet appeared on the bank statement.



---

<!-- file: academy/level-2/principles-of-bookkeeping-controls/study-guide.md -->

# Principles of Bookkeeping Controls: study guide

Practice material, not official AAT content. Check the current unit specification on aat.org.uk.

## What this unit is about
Checking the books are right: bank reconciliations, control account reconciliations, the journal, errors and the suspense account, and payment methods.

## Key ideas
1. **Payment methods**: cash, cheque, debit card, credit card, BACS, Faster Payments, standing order, direct debit, CHAPS. Know their speed and cost in general terms.
2. **Bank reconciliation**: compare cash book to bank statement. Update the cash book first for items only on the statement (bank charges, direct debits, BACS receipts). Then reconcile: statement balance - unpresented payments + outstanding lodgements = adjusted cash book balance.
3. **Control accounts**: sales ledger control account (SLCA) and purchases ledger control account (PLCA) hold totals; the total of individual ledger balances should agree.
4. **VAT control account**: output VAT credit, input VAT debit; balance owed to or from HMRC.
5. **The journal**: for non-routine entries such as corrections, opening entries, irrecoverable debts. Each entry has a narrative.
6. **Errors not shown by the trial balance**: omission, commission, principle, original entry, reversal of entries, compensating.
7. **Errors shown by the trial balance**: one-sided entry, unequal amounts, transposition on one side, balance missed. Difference goes to a suspense account until corrected.
8. **Irrecoverable debts**: Dr Irrecoverable debts expense, Dr VAT control (if relief applies), Cr SLCA.

## LedgerPeak task that uses this skill
Open `clients/demo-harrow-hill-cafe/months/2026-09/bank-rec.md` after running `/close-month demo-harrow-hill-cafe` and redo the reconciliation yourself before reading it.



---

<!-- file: academy/level-2/principles-of-bookkeeping-controls/worked-examples.md -->

# Principles of Bookkeeping Controls: worked examples

All businesses are DEMO and fictional.

## Example 1: bank reconciliation (DEMO café, 30/09/2026)
Cash book balance £4,210 debit. Bank statement £4,580. Bank charges £15 not in cash book. Cheque to supplier £385 not yet presented. Card takings £0 outstanding.
- Update cash book: £4,210 - £15 = £4,195.
- Reconcile: statement £4,580 - unpresented £385 = £4,195. Agrees.
Journal for charges: Dr Bank charges £15; Cr Bank £15.

## Example 2: suspense account
Trial balance debits £50,120, credits £49,880. Difference £240 to suspense (credit side, because credits are short): Cr Suspense £240.
Found: a sales invoice of £240 posted to Dr SLCA but no credit entries. Correction: Dr Suspense £240; Cr Sales £200; Cr VAT control £40. Suspense cleared.

## Example 3: purchases ledger control reconciliation
PLCA balance £6,300. List of supplier balances totals £6,120. Investigation: a supplier credit note £180 recorded in the supplier account but omitted from the purchases returns daybook. Correct PLCA: Dr PLCA £180 (with Cr Purchases returns £150, Cr VAT £30). PLCA becomes £6,120. Agrees.



---

<!-- file: academy/level-2/principles-of-costing/practice-questions.md -->

# Principles of Costing: 20 practice questions

Try them all before scrolling to the answers.

1. Classify rent of the café premises by behaviour.
2. Classify ingredients per meal by behaviour.
3. Phone bill with £20 line rental plus 5p per minute. Behaviour?
4. Costs 1,000 units £6,000; 3,000 units £10,000. Variable cost per unit (high-low)?
5. Using Q4, what is the fixed cost?
6. Selling price £10, variable cost £6, fixed costs £8,000. Break-even units?
7. Budgeted overheads £24,000; budgeted labour hours 6,000. OAR?
8. Budget £5,000, actual £5,400 for materials. Variance?
9. Budget sales £12,000, actual £13,200. Variance and %?
10. Under FIFO, in times of rising prices, is closing inventory valued higher or lower than AVCO?
11. Name the three elements of cost.
12. Is a supervisor's salary in a factory direct or indirect labour?
13. Worker paid £12/hour, overtime at time and a half. Works 40 + 5 overtime hours. Gross pay and overtime premium?
14. Piecework £0.50 per unit; 900 units. Pay?
15. What is a profit centre?
16. A cost that rises by fixed steps at certain activity levels is called?
17. Opening 5 units at £10; buy 5 at £12; issue 6. AVCO cost of issue?
18. Same data, FIFO cost of issue?
19. Why does a business compare actual with budget?
20. Total cost £9,000 for 3,000 units. Cost per unit?

---

## Answers

1. Fixed.
2. Variable.
3. Semi-variable.
4. (£10,000 - £6,000)/2,000 = £2.
5. £10,000 - (3,000 x £2) = £4,000.
6. Contribution £4; £8,000/£4 = 2,000 units.
7. £4 per labour hour.
8. £400 adverse.
9. £1,200 favourable, 10%.
10. Higher (closing stock is at the latest, higher prices).
11. Materials, labour, overheads.
12. Indirect labour.
13. Basic 45 x £12 = £540; premium 5 x £6 = £30; gross £570.
14. £450.
15. A part of the business responsible for both costs and revenues.
16. Stepped fixed cost.
17. Average £11; 6 x £11 = £66.
18. 5 x £10 + 1 x £12 = £62.
19. To control costs, spot problems early and take action.
20. £3.



---

<!-- file: academy/level-2/principles-of-costing/study-guide.md -->

# Principles of Costing: study guide

Practice material, not official AAT content. Check the current unit specification on aat.org.uk.

## What this unit is about
Working out what things cost, how costs behave, and comparing actual results with budget.

## Key ideas
1. **Cost classification**: by element (materials, labour, overheads), by nature (direct, indirect), by function (production, admin, selling).
2. **Cost behaviour**: fixed (rent), variable (ingredients per cup), semi-variable (phone: line rental plus calls), stepped (one extra staff member per 200 covers).
3. **High-low method**: variable cost per unit = (cost at high - cost at low) / (units high - units low); fixed = total - variable.
4. **Inventory valuation**: FIFO (first in, first out), AVCO (weighted average). Know their effect on cost of issues and closing stock.
5. **Labour**: time rate, overtime premium, piecework, bonus.
6. **Cost centres, profit centres, investment centres.**
7. **Overhead absorption**: overhead absorption rate = budgeted overheads / budgeted activity (machine hours or labour hours).
8. **Cost per unit and simple break-even**: contribution per unit = selling price - variable cost; break-even units = fixed costs / contribution per unit.
9. **Variances**: actual vs budget; favourable (F) or adverse (A). Simple percentage variance = variance / budget x 100.

## LedgerPeak task that uses this skill
Work out LedgerPeak's own cost per client hour from `finance/ledgerpeak-books/` (software subscriptions, insurance, AML fee) and compare it with the Starter £95 package. Iris can mark it with `/study`.



---

<!-- file: academy/level-2/principles-of-costing/worked-examples.md -->

# Principles of Costing: worked examples

All businesses are DEMO and fictional.

## Example 1: cost behaviour (DEMO café coffee)
Each cup uses beans £0.18, milk £0.10, cup £0.07 = £0.35 variable. Rent £1,200/month is fixed. Selling 4,000 cups: variable £1,400, fixed £1,200, total £2,600, cost per cup £0.65.

## Example 2: high-low
Electricity: July 3,000 cups £520; September 5,000 cups £680.
Variable = (£680 - £520) / (5,000 - 3,000) = £0.08 per cup. Fixed = £680 - (5,000 x £0.08) = £280.

## Example 3: FIFO vs AVCO
01/09 buy 10 bags beans at £20; 15/09 buy 10 at £23; 20/09 issue 12 bags.
FIFO issue = 10 x £20 + 2 x £23 = £246; closing 8 x £23 = £184.
AVCO: average (£200 + £230)/20 = £21.50; issue 12 x £21.50 = £258; closing 8 x £21.50 = £172.



---

<!-- file: academy/level-2/the-business-environment/practice-questions.md -->

# The Business Environment: 20 practice questions

Try them all before scrolling to the answers.

1. Which business form gives the owner unlimited liability and no separate legal entity?
2. Name the five AAT fundamental ethical principles.
3. A client offers Parth a gift to ignore missing receipts. Which principle is threatened?
4. What is 'tipping off'?
5. Who should staff report a money laundering suspicion to?
6. Name the four essential elements of a contract mentioned in this unit.
7. Give two UK GDPR principles.
8. If demand rises and supply stays the same, what usually happens to price?
9. What does inflation mean?
10. Give two features of useful information.
11. Name two external stakeholders of a café.
12. Is an invitation to treat (e.g. price label) an offer?
13. What are the three parts of sustainability often called the triple bottom line?
14. Why might a bookkeeper decline work outside their competence?
15. Name one advantage of a limited company over a sole trader.
16. What should you do with personal data you no longer need?
17. How can higher interest rates affect a small business?
18. What is the role of the finance function in one sentence?
19. A partnership without an agreement: how are profits normally shared?
20. Give one example of a sustainable practice for LedgerPeak.

---

## Answers

1. Sole trader.
2. Integrity, objectivity, professional competence and due care, confidentiality, professional behaviour.
3. Integrity (and objectivity).
4. Telling someone they are or may be the subject of a money laundering report or investigation.
5. The firm's nominated officer (MLRO).
6. Offer, acceptance, consideration, intention to create legal relations.
7. Any two of: lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; accountability.
8. Price rises.
9. A general rise in prices over time, reducing the purchasing power of money.
10. Any two of accurate, complete, timely, relevant, understandable, cost-effective.
11. For example customers, suppliers, HMRC, lenders, local community.
12. No. It invites customers to make an offer.
13. People (social), planet (environmental), profit (economic).
14. Professional competence and due care.
15. Limited liability (or separate legal entity / easier to raise capital).
16. Delete it securely in line with the retention schedule (storage limitation).
17. Higher borrowing costs and possibly lower customer spending.
18. To record, report and control the organisation's financial information to support decisions and meet legal duties.
19. Equally (Partnership Act 1890 default; verify with current guidance).
20. For example paperless records, reducing travel with video meetings.



---

<!-- file: academy/level-2/the-business-environment/study-guide.md -->

# The Business Environment: study guide

Practice material, not official AAT content. Check the current unit specification on aat.org.uk.

## What this unit is about
The world the business and the bookkeeper work in: legal forms of business, the economy, ethics, sustainability, contract basics, data protection, and communication. It is assessed in a synoptic assessment that also draws on the other three units.

## Key ideas
1. **Business types**: sole trader (unlimited liability), partnership (unlimited, unless LLP), limited company (limited liability, separate legal entity), charities, public sector.
2. **Stakeholders**: owners, employees, customers, suppliers, lenders, HMRC, community.
3. **The finance function**: its role, links with other departments, and the importance of timely, accurate information.
4. **Economy**: supply and demand, inflation, interest rates, the Bank of England, how these affect small businesses.
5. **Contract law basics**: offer, acceptance, consideration, intention to create legal relations.
6. **Ethics**: AAT Code of Professional Ethics principles: integrity, objectivity, professional competence and due care, confidentiality, professional behaviour.
7. **Money laundering**: what it is, reporting suspicion to the nominated officer, tipping off.
8. **Data protection**: UK GDPR principles, e.g. lawfulness, purpose limitation, data minimisation, accuracy, storage limitation, security.
9. **Sustainability**: social, environmental and economic responsibility.
10. **Communication and information**: features of useful information (accurate, complete, timely, relevant, understandable).

## LedgerPeak task that uses this skill
Read `office/policies/aml-policy-and-firm-risk-assessment.md` and `uk-gdpr-privacy-notice.md`, then explain to Iris which ethical principle and which UK GDPR principle each of rules 1, 3 and 6 in `CLAUDE.md` protects.



---

<!-- file: academy/level-2/the-business-environment/worked-examples.md -->

# The Business Environment: worked examples

All businesses are DEMO and fictional.

## Example 1: choosing a business form
A Harrow electrician earning £60,000 asks sole trader vs limited company. Sole trader: simple, unlimited personal liability, profits taxed as personal income. Limited company: liability limited to shares, more admin (Companies House filings), separate legal entity. A bookkeeper explains the features; the tax choice is advice for a qualified accountant.

## Example 2: ethics
A friend asks Parth what a DEMO client earns. Principle: confidentiality. Answer: decline; information is used only for the purpose given.

## Example 3: interest rates
The Bank of England raises base rate. Effect on the DEMO café: overdraft and loan costs rise; customers may spend less; a bookkeeper would flag higher finance costs in the monthly summary.
