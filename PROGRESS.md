# PROGRESS.md — Progress log schema

Each client has an append-only log at `progress/<client_id>.json`.
The file is a JSON array. New entries are appended; old entries are NEVER modified.

## Entry fields

| Field | Type | Values / format | Purpose |
|-------|------|-----------------|---------|
| `date` | string | `"YYYY-MM-DD"` | When the entry was recorded |
| `weight_kg` | float | kilograms | Current measured weight |
| `adherence` | string | `"low"` / `"medium"` / `"high"` | How well the client followed their plan this period |
| `phase` | integer | 1–5 | Framework phase the client was in at this entry |
| `note` | string or null | free text | Optional context (anything worth recording) |

## Invariants
- Entries are ordered by `date` ascending.
- No entry is ever deleted or modified — the full trajectory is the data.
- `phase` is the phase active at the time of recording (not recomputed retroactively).

## How to add an entry
```
python3 log_progress.py <client_id> <weight_kg> <adherence> [note]
```
Examples:
```
python3 log_progress.py louis 84.2 high "Bonne semaine, objectifs respectés."
python3 log_progress.py sophie 91.5 medium
```

## Why this structure matters for Phase 2
The progress log is the dynamic half of the dataset (profile is the static half).
Phase 2's statistical analysis will join profiles + progress logs to compute:
- Success rates per profile segment (BMI class, lifestyle, readiness)
- Correlation between adherence patterns and outcome
- Friction points: where/when clients stall or drop off
Consistent types and clean fields here set the ceiling for every insight Phase 2 can produce.
