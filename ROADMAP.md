# ROADMAP v2 — from delivery engine to data-driven coaching

## The real vision (owner's words, distilled)
An AI coach that guides each client toward a healthy BMI by following a
strategic weight-loss FRAMEWORK, tailored per client profile. The AI improvises
WITHIN the framework's guardrails — free in tone and specifics, bounded in
strategy. Over time, STATISTICAL ANALYSIS of accumulated client data identifies
what drives success and where clients hit friction, and that insight is fed back
to refine the framework and techniques. Goal for the client: healthy, effective
weight loss AND growing autonomy.

(Note: "machine learning" is explicitly OUT of scope — possibly forever. The
analytical goal is statistics/analytics: success rates, friction points,
outcome comparisons across profiles. Interpretable, small-data-friendly, and
the right tool for this product.)

## The key sequencing truth
The statistical "success-factor" analysis is DATA-GATED. It cannot happen before
real clients generate real outcome data over time. Therefore:
- Phase 1 builds the framework + the data-collection loop.
- Running Phase 1 with clients GENERATES the data.
- Phase 2 (the analysis) becomes possible only once that data exists.
Building Phase 1 correctly IS how Phase 2 becomes possible. Statistics is even
MORE sensitive to clean data than ML would be — so the data structures designed
in Phase 1 set the ceiling for every insight Phase 2 can ever produce.

---

## PHASE 0 — Delivery engine ✅ DONE (BRIEF-01..08)
Scheduled, per-person, secret-handled, automated message delivery.
Necessary plumbing. Demonstrates no product value on its own (correctly noted).

## PHASE 1 — Framework + strategy + coach = the REAL MVP

### Two scopes (owner's architecture — keep them separate)
- PRODUCT (strategist): sets profile + objective, computes the profile-
  customized strategy. SAFETY lives here. The plan it outputs is safe by
  construction.
- COACH (executor): a tool that EXECUTES a handed strategy in real time —
  delivers needed info, remembers motivations, helps with strategy questions,
  keeps the client progressing. Does NOT set goals or invent strategy.

Reached when the product hands the coach a safe per-client strategy and the
coach executes it with live context — AND that coaching demonstrably beats a
generic message. The MVP may DISPROVE its value hypothesis; that is valid.

- BRIEF-09 — GENERAL strategic framework (universal principles + SAFETY
  constraints as strategy-layer rules). Product layer. Design work. ✅ DONE
- BRIEF-10 — Client PROFILE + OBJECTIVE (product sets the client up). ✅ DONE
- BRIEF-11 — Product COMPUTES the profile-customized strategy from framework +
  profile + objective. SAFETY APPLIED HERE. Output = a safe per-client plan. ✅ DONE
- BRIEF-12 — PROGRESS LOG: the client's changing state over time, append-only.
  The data loop that feeds Phase 2; also live context for the coach.
- BRIEF-13 — The AI COACH: inject (framework + customized strategy + coaching
  principles) + live context, and EXECUTE. Includes the value test vs template.
  This is the MVP-value moment.
- BRIEF-14 — (likely) tests + CI, once logic can fail quietly.

## PHASE 2 — Statistical analysis of outcomes (DATA-GATED, do not start early)
Only meaningful after Phase 1 has collected clean, structured outcome data
across multiple clients over time.
- Aggregate profiles + progress logs into an analysis-ready dataset.
- Compute success rates; compare outcomes across profile segments; identify
  friction points (where/when clients stall or drop off).
- Feed findings back into the framework and techniques (close the loop).
- This is STATISTICS/ANALYTICS, not machine learning. Interpretable and
  small-data-friendly. It is LAST, not first.

## CROSS-CUTTING (ongoing)
- SAFETY: healthy-BMI floor, safe rate-of-loss cap, referral triggers, avoid
  rigid numeric prescriptions that could fuel disordered patterns. Encoded in
  the framework from BRIEF-09 onward. Non-negotiable.
- Eventually: a real interface + signup for non-technical clients (deferred
  until the value hypothesis is proven).

## RULE
Each brief advances one step at the smallest size that still moves it. Aligned
first, small second. Phase 2 analysis does not get a brief until its data exists.
