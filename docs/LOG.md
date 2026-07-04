# Project log — one line per completed task

2026-07-04 — BRIEF-01 — done — Push notification fired on phone via ntfy.sh (notify.py, 11 lines)
2026-07-04 — BRIEF-02 — done — Repo created on GitHub at louisnaxa/day-by-day, initial commit pushed
2026-07-04 — BRIEF-03 — done — Daily GitHub Actions workflow live, notification fires automatically at 08:00 Paris
2026-07-04 — BRIEF-04 — done — notify.py reads message content from coach.json instead of hardcoded string
2026-07-04 — BRIEF-05 — done — coach.json is a list of 2 people, notify.py loops and sends one notification per person
2026-07-04 — BRIEF-06 — done — build_message() generates text from goal_type fields; two people get visibly different messages
2026-07-04 — BRIEF-07 — done — build_message() calls Anthropic API; AI writes a distinct coaching line per person in French
2026-07-04 — BRIEF-08 — done — NOTIFY secret wired into workflow; scheduled Action generates AI messages automatically
2026-07-04 — BRIEF-09 — done — FRAMEWORK.md written: 5 phases, tailoring principles, safety constraints with rate-of-loss formula
2026-07-04 — BRIEF-08 — done — ANTHROPIC_API_KEY added as GitHub secret; workflow installs anthropic and passes key to notify.py
