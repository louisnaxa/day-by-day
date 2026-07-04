# FRAMEWORK.md — General Strategic Framework for Healthy Weight Loss

## Purpose and scope

This is a PRODUCT-layer artifact. It defines the universal principles of healthy
weight loss from which all per-client strategies are derived (BRIEF-11). It does
not describe any specific client's plan, and it does not describe coach behavior.

**Architecture reminder:**
- PRODUCT (strategist): applies this framework to a client profile to compute a
  safe, customized strategy. Safety constraints live here.
- COACH (executor): executes the strategy it is handed. It never sets goals or
  invents strategy. It can only operate within a plan that is already safe.

---

## 1. Phases of a healthy weight-loss journey

Progress through phases is driven by client data and outcomes, not calendar alone.

### Phase 1 — Assessment
**Goal:** Establish a clear, safe, realistic picture of where the client is and
what is possible for them.
**Typical duration:** 1–2 weeks.
**Strategy emphasis:**
- Collect baseline: current weight, height (BMI), age, lifestyle, constraints.
- Check against all safety constraints before proceeding (see Section 3).
- Set a realistic target weight/BMI and timeline, applying the rate-of-loss formula.
- Identify 2–3 keystone habits to introduce — not a full diet overhaul.

### Phase 2 — Habit building
**Goal:** Establish the behavioral foundation that makes sustained loss possible.
**Typical duration:** 3–6 weeks.
**Strategy emphasis:**
- Focus on 2–3 keystone habits (e.g. regular meals, daily movement, hydration).
- No strict caloric targets yet; directional guidance only.
- Build consistency and confidence before adding restriction.
- Tone: encouraging, low-pressure. Celebrate showing up, not scale results.

### Phase 3 — Active loss
**Goal:** Steady, sustainable weight reduction within safe-rate bounds.
**Typical duration:** Variable; continues while the client has a loss target above
current weight and is progressing.
**Strategy emphasis:**
- Apply a moderate energy deficit calibrated to the rate-of-loss formula (Section 3.2).
- Emphasize protein, satiety, and food quality over precise calorie counting.
- Regular check-in rhythm (weekly weight); adjust if deviation from target is significant.
- Tone: steady and practical. Focus on process and habits, not the scale number.

### Phase 4 — Stabilization
**Goal:** Transition from active loss to maintenance without rebound.
**Typical duration:** 4–8 weeks after reaching target weight.
**Strategy emphasis:**
- Gradually reduce energy deficit to zero.
- Reinforce and maintain the habits built in Phase 2.
- Introduce flexibility and self-regulation: the client learns to manage without
  a precise plan.
- Tone: autonomy-building. The client is taking over.

### Phase 5 — Autonomy
**Goal:** The client no longer needs active coaching and self-regulates.
**Typical duration:** Ongoing; coaching intensity fades to periodic check-ins.
**Strategy emphasis:**
- Periodic check-ins replace daily or frequent coaching.
- Client sets their own micro-goals; coach provides light accountability.
- Exit condition: client is confident, stable at healthy weight, and not dependent
  on the coach. This is the definition of success.

---

## 2. Tailoring principles

These are the rules BRIEF-11 applies when computing a per-client strategy from
this framework and a specific profile. They are stated as general principles here;
the actual computation is in BRIEF-11.

### Starting BMI
| BMI range      | Guidance |
|----------------|----------|
| < 18.5         | SAFETY BLOCK: do not compute a weight-loss strategy. Issue referral. |
| 18.5–24.9      | Client is at a healthy weight. Redirect to maintenance or health goals, not loss. |
| 25–29.9        | Weight loss is appropriate. Standard framework applies; emphasize habits. |
| 30–34.9        | Weight loss is a health priority. Slightly more structured approach; consider suggesting medical involvement. |
| ≥ 35           | Flag for professional co-management. Proceed only if client states medical clearance. |

### Age
- **Under 18:** Out of scope — refer to a pediatric specialist.
- **18–35:** Standard approach.
- **36–55:** Prioritize muscle retention alongside fat loss; include resistance training emphasis.
- **56+:** Slower pace. Bone density and muscle retention are primary concerns; weight loss is a secondary, slower goal.

### Constraints and injuries
- Joint or mobility constraints: remove impact-based movement recommendations;
  substitute low-impact alternatives.
- Metabolic conditions (diabetes, thyroid disorders, etc.): flag for medical
  co-management; do not prescribe a caloric deficit without stated medical clearance.

### Lifestyle and readiness
- **Sedentary baseline:** Extend Phase 2; movement habits before dietary changes.
- **High readiness** (motivated, consistent, informed): can shorten Phase 2;
  more structured targets are appropriate earlier.
- **Low readiness or prior failed attempts:** Extend Phase 2 significantly; one
  habit at a time; reduce goal size and timeline ambition.

---

## 3. Safety constraints (strategy layer — non-negotiable)

These constraints are enforced at strategy-computation time (BRIEF-11). A plan
that violates any of them must not be issued. The coach never needs to enforce
these independently — the plan it receives is safe by construction.

### 3.1 Healthy-BMI floor

A weight-loss strategy is NEVER computed for a client whose current or projected
BMI falls at or below 18.5. Such clients are redirected to maintenance or health
goals. The computation step checks BMI against this floor before anything else.

### 3.2 Rate-of-loss formula

**Rule:** the plan must not target loss exceeding **1% of the client's current
body weight per week.**

Examples:
- 90 kg client → cap at 0.90 kg/week
- 65 kg client → cap at 0.65 kg/week

**Absolute ceiling:** regardless of the formula result, the plan never targets
more than **1.0 kg/week** of loss.

The formula result is a **maximum**, not a target. The strategy should aim for
0.5–0.75%/week for sustainability; 1%/week is the hard upper bound.

### 3.3 No rigid numeric obsession

The framework does not produce plans built around exact daily calorie or gram
targets as the primary guidance. Directional habits ("increase protein at each
meal", "reduce refined carbs at dinner") are preferred. Exact numeric targets are
only appropriate in specific, professional contexts.

*Rationale: rigid numeric tracking is associated with disordered-eating risk in a
subset of users. The product avoids creating this vector.*

### 3.4 Referral triggers

When any of the following is present, the strategy-computation step outputs
**REFER** instead of a plan:

- BMI < 18.5
- Known eating disorder history
- Client requests a loss rate more than 50% above the formula cap (> 1.5%/week)
- Client describes behaviors consistent with disordered eating (multi-day
  deliberate fasting, purging, food-guilt affecting daily function)
- Metabolic or endocrine condition without stated medical clearance
- Client is under 18

Referral messages must be warm, non-alarmist, and specific: name the appropriate
professional (GP, dietitian, or specialist) based on the trigger.

### 3.5 Autonomy principle

Every phase and every strategy choice should shift agency progressively toward the
client. A plan that maximizes dependency on the coach is a failure mode. The Phase
5 exit condition — client self-regulates without coaching — is the explicit success
definition. Strategy choices that trade client capability for short-term compliance
are inconsistent with this framework.
