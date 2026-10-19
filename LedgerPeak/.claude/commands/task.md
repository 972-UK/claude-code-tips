---
description: Give the office any task. Grace plans it, each department does its part (watch them on the live office), Grace checks and hands back one result.
argument-hint: <what you want done>
---

Parth's task: $ARGUMENTS

1. PLAN: use the grace-whitmore subagent with "PLAN: <the task>". She returns numbered steps: step | agent-id | brief | depends on.
2. DO: run every step by calling the named subagent with its brief. Start all steps with no unmet dependency at the same time (parallel Agent calls), then the next wave. Do not do specialist work yourself.
3. CHECK: use the grace-whitmore subagent with "CHECK:" plus a summary of every step's output and file paths. If she sends a step back, re-run it once.
4. Give Parth Grace's final summary: what was done, by whom, files, and decisions he needs to make. Drafts only; nothing is sent. Log one line in office/work-log.md.
