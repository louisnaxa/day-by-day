# PROFILE.md — Client profile schema

Each client record in `coach.json` must conform to this schema.
Field names and allowed values are fixed — no free text where a category works.

## Fields

| Field | Type | Values / format | Maps to |
|-------|------|-----------------|---------|
| `id` | string | unique, e.g. `"louis"` | identifier |
| `name` | string | display name | — |
| `age` | integer | years | age-bracket tailoring |
| `height_cm` | integer | centimetres | BMI computation |
| `current_weight_kg` | float | kilograms | BMI, rate-of-loss cap |
| `target_weight_kg` | float | kilograms | goal, BMI floor check |
| `lifestyle` | string | `"sedentary"` / `"moderate"` / `"active"` | habit-building duration |
| `readiness` | string | `"low"` / `"medium"` / `"high"` | phase-2 pacing |
| `constraints` | array of strings | e.g. `["knee pain"]`, or `[]` | movement adaptation |
| `current_phase` | integer | 1–5 (framework phases) | strategy focus |
| `autonomy_level` | string | `"low"` / `"medium"` / `"high"` | coaching intensity |
| `start_date` | string | `"YYYY-MM-DD"` | days-in-program computation |

## Notes
- BMI is always computed from `height_cm` + `current_weight_kg`; it is never stored.
- `target_weight_kg` must yield a healthy BMI (≥ 18.5) — the strategy-computation
  step (BRIEF-11) verifies this before issuing a plan.
- `constraints` is an array so multiple constraints are representable cleanly.
- `current_phase` and `autonomy_level` are updated as the client progresses;
  they are the living state of the coaching relationship.
