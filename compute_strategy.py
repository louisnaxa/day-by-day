"""
compute_strategy.py — PRODUCT layer (strategist)

Applies FRAMEWORK.md rules to a client profile and produces a per-client
strategy, stored as strategy/<client_id>.json.

Safety constraints are enforced HERE. The coach (BRIEF-13) receives only the
output of this step and can execute freely — the plan is safe by construction.
"""

import json
from pathlib import Path

# FRAMEWORK.md §3.2
RATE_CAP_PERCENT = 0.01  # 1% of current body weight per week

# FRAMEWORK.md §1 — phase focus descriptions
PHASE_FOCUS = {
    1: "Assessment: collect baseline, verify safety, set realistic target, identify 2-3 keystone habits.",
    2: "Habit-building: build 2-3 keystone habits (meals, movement, hydration). No strict caloric targets yet.",
    3: "Active loss: moderate energy deficit calibrated to rate cap. Emphasize protein and satiety.",
    4: "Stabilization: gradually reduce deficit to zero. Reinforce habits; introduce self-regulation.",
    5: "Autonomy: coaching fades to periodic check-ins. Client sets their own micro-goals.",
}


def bmi(weight_kg, height_cm):
    return round(weight_kg / (height_cm / 100) ** 2, 1)


def compute_strategy(profile):
    """
    Given a client profile dict, return a strategy dict.
    Status is one of: "active", "maintenance", "refer".
    """
    client_id = profile["id"]
    current_bmi = bmi(profile["current_weight_kg"], profile["height_cm"])
    target_bmi  = bmi(profile["target_weight_kg"],  profile["height_cm"])

    # ── FRAMEWORK.md §3.4 — referral triggers ────────────────────────────────
    if profile["age"] < 18:
        return {
            "client_id": client_id,
            "status": "refer",
            "reason": "Client is under 18 — refer to a pediatric specialist.",
        }
    desired = profile.get("desired_weekly_loss_kg")
    if desired is not None:
        hard_cap = round(profile["current_weight_kg"] * RATE_CAP_PERCENT * 1.5, 2)
        if desired > hard_cap:
            return {
                "client_id": client_id,
                "status": "refer",
                "reason": (
                    f"Requested rate {desired} kg/week exceeds 1.5× the safe cap "
                    f"({hard_cap} kg/week for {profile['current_weight_kg']} kg). "
                    f"Refer to a dietitian before proceeding."
                ),
            }
    if current_bmi < 18.5:
        return {
            "client_id": client_id,
            "status": "refer",
            "reason": f"Current BMI {current_bmi} is underweight (< 18.5). Refer to a GP or dietitian.",
        }
    if target_bmi < 18.5:
        return {
            "client_id": client_id,
            "status": "refer",
            "reason": f"Target weight yields BMI {target_bmi} (< 18.5). Target must be revised. Refer.",
        }

    # ── FRAMEWORK.md §3.1 — healthy-BMI floor ────────────────────────────────
    if current_bmi < 25.0:
        return {
            "client_id": client_id,
            "status": "maintenance",
            "current_bmi": current_bmi,
            "note": f"BMI {current_bmi} is already in the healthy range. Redirect to maintenance/health goals.",
        }

    # ── Active weight-loss strategy ───────────────────────────────────────────

    # Rate cap: 1% of current body weight (FRAMEWORK.md §3.2)
    weekly_rate_cap_kg = round(profile["current_weight_kg"] * RATE_CAP_PERCENT, 2)

    # Age-bracket adaptation (FRAMEWORK.md §2)
    age = profile["age"]
    if age < 36:
        age_note = None
    elif age < 56:
        age_note = "Age 36–55: include resistance training to preserve muscle alongside fat loss."
    else:
        age_note = "Age 56+: slower pace; muscle retention and bone density take priority over rate."

    phase = profile["current_phase"]

    return {
        "client_id": client_id,
        "status": "active",
        "current_bmi": current_bmi,
        "target_bmi": target_bmi,
        "current_weight_kg": profile["current_weight_kg"],
        "target_weight_kg": profile["target_weight_kg"],
        "kg_to_lose": round(profile["current_weight_kg"] - profile["target_weight_kg"], 1),
        "weekly_rate_cap_kg": weekly_rate_cap_kg,
        "current_phase": phase,
        "phase_focus": PHASE_FOCUS[phase],
        "lifestyle": profile["lifestyle"],
        "readiness": profile["readiness"],
        "autonomy_level": profile["autonomy_level"],
        "constraints": profile["constraints"],
        "age_note": age_note,
    }


if __name__ == "__main__":
    Path("strategy").mkdir(exist_ok=True)
    clients = json.load(open("coach.json"))
    for profile in clients:
        strategy = compute_strategy(profile)
        path = f"strategy/{profile['id']}.json"
        with open(path, "w") as f:
            json.dump(strategy, f, indent=2, ensure_ascii=False)
        print(f"\n── {profile['id']} ──")
        print(json.dumps(strategy, indent=2, ensure_ascii=False))
