"""
value_test.py — Does the framework-aware coach beat a generic template?

Runs both approaches for each client and prints them side by side.
Run with ANTHROPIC_API_KEY set.
"""

import json
from pathlib import Path
from datetime import date
from coach_message import generate_message

def generic_template(profile):
    """The baseline: a flat, context-free message — what we had before BRIEF-09."""
    days = (date.today() - date.fromisoformat(profile["start_date"])).days + 1
    kg = round(profile["current_weight_kg"] - profile["target_weight_kg"], 1)
    return f"{profile['name']} — Jour {days}. Objectif: perdre {kg} kg. Continue comme ca."

def run():
    clients = json.loads(Path("coach.json").read_text())
    for profile in clients:
        print(f"\n{'═' * 60}")
        print(f"  CLIENT: {profile['name'].upper()}")
        print(f"{'═' * 60}")
        print(f"\n[TEMPLATE]\n{generic_template(profile)}")
        print(f"\n[COACH]\n{generate_message(profile)}")
        print()

if __name__ == "__main__":
    run()
