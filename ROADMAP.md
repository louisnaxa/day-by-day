# ROADMAP — from notifier to coaching app

The long-term target: an app that sends personalized, AI-generated diet-coaching
notifications to clients on a schedule, adapting over time.

That target is built from these capabilities, in dependency order. Each builds
directly on the previous one. No detours — if a proposed task isn't on this
list, question whether it belongs.

## The path
1. **Send a scheduled notification** — ✅ DONE (BRIEF-01 to 03)
   The spine: code runs automatically on a schedule and pushes to a phone.

2. **Message is data-driven, not hardcoded** — ← WE ARE HERE (BRIEF-04)
   The script reads the message content from a data file. This is the seed of
   "each client has their own info." Turns an alarm clock into something that
   *could* be personal.

3. **Store multiple people's data** — (upcoming)
   The data file holds several people, each with name + goal + plan. The script
   can pick one. This is the "clients" concept in its simplest form.

4. **Message is personalized from the data** — (upcoming)
   The message text is built from a person's fields (their name, their goal),
   not just copied. First real personalization.

5. **AI generates the message from the data** — (upcoming)
   Instead of a template, an AI call turns a person's data into a coaching
   message. This is the "IA coaching" core of the product.

6. **People can be added / sign up** — (upcoming)
   Real users get into the system. This is where it becomes an actual app with
   an interface, not a script.

## Rule
Each brief advances exactly one step on this path, at the smallest size that
still moves it forward. Aligned first, small second. If a task teaches a skill
but doesn't advance a step, it's optional polish — schedule it deliberately or
skip it, never let it masquerade as progress.

## Where the "later" ambitions go
The other apps, tokenization, astrophysics, politics — not on this roadmap on
purpose. This roadmap is one accomplishment: the coaching app. Finish it, then
the next accomplishment gets its own roadmap. One at a time.
