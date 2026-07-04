# CLAUDE.md — Project context (read this first, every session)

## What this project is
A deliberately incremental learning project. The owner is building technical
skills one small, finishable task at a time. Each task = one brief = roughly
one afternoon. The long-term direction (a coaching app, then more) is
irrelevant to any single session — only the current brief matters.

## How to know where we are
1. Read `docs/LOG.md` — one line per completed task, most recent last
2. Read the highest-numbered `docs/BRIEF-XX.md` — if not logged as done in
   LOG.md, it is the current task
3. Never assume progress that isn't written in these files

## Working rules (non-negotiable)
- Do ONLY what the current brief says. No "while we're at it" improvements.
- If the brief says the owner types the commands, guide — don't execute.
- Explain each new tool/command in one sentence. The owner is learning.
- Keep everything as small as the brief allows. Smaller is better.
- If something is out of scope, say so and note it for a future brief.

## At the end of every session
1. Append one line to `docs/LOG.md`:
   `YYYY-MM-DD — BRIEF-XX — done/partial — one-sentence result`
2. If partial, add a "## Where we stopped" section at the bottom of the
   current brief with exact next steps.
3. Commit everything. Uncommitted work is invisible to the next session.

## Conventions
- One brief per task: `docs/BRIEF-01.md`, `BRIEF-02.md`, ...
- Completed briefs are never edited (except a final status line)
- Repo structure stays flat and simple until a brief says otherwise
