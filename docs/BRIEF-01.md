# Task Brief — Day 1: Make my phone buzz

## Objective (the ONLY objective)
Send one push notification to my phone, triggered by a script I run manually.
When the notification appears on my phone, this task is DONE.

## Definition of done
- [ ] I run one command (e.g. `python notify.py`)
- [ ] Within seconds, a notification appears on my phone with a hardcoded message (e.g. "Day 1: it works.")

## Suggested approach (pick the simplest)
1. Use **ntfy.sh** (free, no account needed):
   - I install the ntfy app on my phone and subscribe to a topic
   - The script is a single HTTP POST to `https://ntfy.sh/<my-topic>`
2. Alternatives only if ntfy fails: Pushover, Telegram bot.

## Constraints — read carefully
- **Keep it under ~20 lines of code.** One file. No framework.
- **NO** app development (no iOS/Android project, no React Native, no Flutter)
- **NO** AI features, no user accounts, no database, no scheduling
- **NO** CI/CD, no Docker, no tests, no config files, no .env
- **NO** "while we're at it" improvements. If a step feels optional, skip it.
- Explain each step in one short sentence so I learn the stack minimally.

## What I'll need from you (Claude Code)
1. Tell me exactly what to install on my phone (1 app) and computer (if anything)
2. Write the script
3. Give me the single command to run it
4. If it errors, help me read the error and fix it. Errors are normal, not failure.

## Explicitly out of scope (do not mention, do not scaffold)
The diet-coaching app, personalization, clients, deployment, repo setup.
Those come AFTER this buzz. This brief covers today only.

## Tomorrow (do not start today)
Put this script in a GitHub repo with a 3-line README. That's a separate session.
