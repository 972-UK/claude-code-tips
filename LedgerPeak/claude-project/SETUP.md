# Setting up the LedgerPeak Project on claude.ai

Time needed: about 10 minutes.

1. Open claude.ai, choose Projects, then Create project. Name it "LedgerPeak".
2. Open the project instructions and paste the full contents of `01-PROJECT-INSTRUCTIONS.md`.
3. Add files 02 to 09 from this folder to the project knowledge.
4. Turn on web search, so the team can check GOV.UK.
5. Start a new chat in the project and type: roadmap
6. Then follow `09-first-30-evenings.md`, one evening at a time.
7. Keep the office view pinned in your sidebar: https://claude.ai/artifact/CVkf7SPzwczqqRqb78Qbnj

Project or Claude Code?
- The Project is for conversation, drafts and planning from any device, with all rules and templates loaded. It does not edit files on your computer, so copy anything you want to keep into your LedgerPeak folder or a document.
- Claude Code works directly on the LedgerPeak folder: client files, books, the live office view and the dashboard. Use it at your laptop for DEMO practice runs you want saved.

Keeping the Project up to date: when the office changes (prices, staff, rules, roadmap progress), run `python3 scripts/build_project_pack.py` in Claude Code, then re-upload the changed files.
