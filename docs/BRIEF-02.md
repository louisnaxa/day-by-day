# Task Brief — Day 2: Put the project on GitHub

## Status
- Day 1 (BRIEF-01): DONE — notification fired ✓

## Objective (the ONLY objective)
The Day 1 script lives in a GitHub repository, with a minimal README.
When I can open github.com and see my code there, this task is DONE.

## Definition of done
- [ ] A GitHub repo exists (name suggestion: `notify` or `day-by-day`)
- [ ] It contains `notify.py`, a `README.md`, and a `docs/` folder with BRIEF-01 and BRIEF-02
- [ ] README is ~5 lines max: what it does, how to run it
- [ ] I made the commit and push myself (Claude Code guides, I type the git commands)

## Repo structure (final state)
```
notify/
├── notify.py
├── README.md
└── docs/
    ├── BRIEF-01.md   (Day 1 — done)
    └── BRIEF-02.md   (this file)
```

## What I'll need from you (Claude Code)
1. Check if git is installed and configured; help me set it up if not
2. Walk me through: init → add → commit → create GitHub repo → push
3. Explain each git command in ONE sentence as we go — I'm learning the tool
4. Make me type the git commands myself instead of running them for me

## Constraints
- **NO** CI/CD yet (that's Day 3, when scheduling arrives)
- **NO** branch strategy, no .gitignore debates, no license discussion
- **NO** refactoring notify.py — it works, don't touch it
- One commit is enough. "Initial commit" is a fine message.

## Convention going forward (project hygiene)
- One brief per task: BRIEF-03, BRIEF-04… all in `docs/`
- Completed briefs are never edited — they are the track record
- Each brief starts with the status of the previous one

## Tomorrow (do not start today)
Day 3: the notification sends itself daily at a fixed time (scheduled GitHub Action = first contact with CI/CD).
