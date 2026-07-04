# Task Brief — Day 8: API key in GitHub Actions

## Roadmap position
Step 5b of 6 (ROADMAP.md): completing "AI generates the message from the data."
The local run works. This makes the scheduled Action work too.

## Status
- BRIEF-01..07: DONE — AI writes coaching messages locally ✓

## Objective (the ONLY objective)
Add ANTHROPIC_API_KEY as a GitHub secret and pass it to the workflow so the
daily scheduled run generates AI messages, not the fallback. When the Action
runs and produces AI-written notifications, this task is DONE.

## Definition of done
- [ ] ANTHROPIC_API_KEY added as a GitHub Actions secret (never in code)
- [ ] notify.yml installs the anthropic package and passes the secret as an env var
- [ ] Workflow triggered manually confirms AI messages fire
- [ ] Commit pushed

## End of session
Update LOG.md, commit.
