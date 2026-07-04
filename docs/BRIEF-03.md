# Task Brief — Day 3: The notification sends itself

## Status
- BRIEF-01: DONE — notification fired ✓
- BRIEF-02: DONE — repo live at louisnaxa/day-by-day ✓

## Objective (the ONLY objective)
Every morning at a fixed time, my phone gets the notification automatically —
no human running anything. This is done with a scheduled GitHub Action.
When the notification arrives without me touching the computer, this task is DONE.

## Definition of done
- [ ] A workflow file exists at `.github/workflows/notify.yml`
- [ ] It runs `notify.py` on a daily schedule (pick a time, e.g. 08:00 Paris)
- [ ] I triggered it once manually from the GitHub Actions tab to verify it works
      (don't wait until tomorrow to find out it's broken)
- [ ] The message is updated to something like "Day N. Ship something small."

## What I'll need from you (Claude Code)
1. Explain in 3 sentences what GitHub Actions is before writing anything
2. Write the workflow file, then walk me through it line by line —
   `on:`, `schedule:`, `cron:`, `jobs:`, `steps:` — one sentence each
3. Explain cron syntax with my chosen time as the example
4. Show me where the Actions tab is on GitHub and how to trigger a manual run
5. **I type the git commands for the final commit and push myself.**
   Guide me; do not run them for me. This is non-negotiable today.

## Constraints
- **NO** secrets management yet (the ntfy topic can stay in the code for now —
  note it as a future improvement, that's a fine lesson for a later brief)
- **NO** refactoring notify.py beyond changing the message text
- **NO** multiple workflows, no matrix builds, no fancy YAML
- One workflow file, ~15 lines. If it's longer, it's doing too much.

## Why this task matters (for context, not scope)
This workflow file IS CI/CD in miniature: code that runs automatically on a
trigger, on GitHub's machines, not mine. Every pipeline I build later is this
same idea with more steps. Also: cron schedules and YAML are everywhere.

## At the end of the session
Update docs/LOG.md and commit — but today I type those commands.

## Next (do not start today)
Day 4 direction, to be decided: either move the topic name to a GitHub secret
(security lesson), or make the message dynamic (e.g. include the day count).
Small either way.
