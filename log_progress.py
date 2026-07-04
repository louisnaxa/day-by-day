"""
log_progress.py — append a progress entry for a client (APPEND-ONLY).

Usage:
    python3 log_progress.py <client_id> <weight_kg> <adherence> [note]

adherence: low | medium | high
note:      optional free text (quote if it contains spaces)

Example:
    python3 log_progress.py louis 84.2 high "Bonne semaine."
    python3 log_progress.py sophie 91.5 medium
"""

import json
import sys
from datetime import date
from pathlib import Path

VALID_ADHERENCE = {"low", "medium", "high"}

def load_log(client_id):
    path = Path(f"progress/{client_id}.json")
    if path.exists():
        return json.loads(path.read_text())
    return []

def save_log(client_id, entries):
    Path("progress").mkdir(exist_ok=True)
    path = Path(f"progress/{client_id}.json")
    path.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n")

def load_profile(client_id):
    clients = json.loads(Path("coach.json").read_text())
    for c in clients:
        if c["id"] == client_id:
            return c
    return None

def append_entry(client_id, weight_kg, adherence, note=None):
    if adherence not in VALID_ADHERENCE:
        print(f"Error: adherence must be one of {VALID_ADHERENCE}")
        sys.exit(1)

    profile = load_profile(client_id)
    if profile is None:
        print(f"Error: no client with id '{client_id}' in coach.json")
        sys.exit(1)

    entry = {
        "date": date.today().isoformat(),
        "weight_kg": float(weight_kg),
        "adherence": adherence,
        "phase": profile["current_phase"],
        "note": note,
    }

    entries = load_log(client_id)
    entries.append(entry)
    save_log(client_id, entries)
    print(f"Entry added for {client_id}: {entry}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    client_id = sys.argv[1]
    weight_kg = sys.argv[2]
    adherence = sys.argv[3]
    note      = sys.argv[4] if len(sys.argv) > 4 else None
    append_entry(client_id, weight_kg, adherence, note)
