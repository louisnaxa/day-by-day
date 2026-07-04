"""
coach_message.py — COACH layer (executor)

Assembles three inputs (framework + per-client strategy + coach principles)
plus live context (recent progress) into a prompt, then calls the AI.

The coach EXECUTES a strategy it is handed. It does not set goals or rates.
Safety was applied upstream in compute_strategy.py and is not re-checked here.
"""

import json
import os
from pathlib import Path
import anthropic

# Key rules from FRAMEWORK.md injected as a concise summary
FRAMEWORK_BRIEF = """\
CADRE STRATÉGIQUE (résumé):
- Phase 1: évaluation — baseline, objectif réaliste, 2-3 habitudes clés.
- Phase 2: construction d'habitudes — cohérence avant restriction, pas de cibles caloriques.
- Phase 3: perte active — déficit modéré, protéines et satiété, rythme hebdomadaire.
- Phase 4: stabilisation — réduire le déficit progressivement, autonomie croissante.
- Phase 5: autonomie — check-ins espacés, le client se gère lui-même.
Le coach exécute la phase en cours. Il ne redéfinit pas l'objectif ni le rythme."""

# Coach principles from COACH_PRINCIPLES.md injected as a concise summary
PRINCIPLES_BRIEF = """\
PRINCIPES DU COACH:
- Reste dans la phase et le focus handés.
- Adapte le ton à l'adhérence récente (haute → renforce ; faible → soutien + 1 action concrète).
- Construis l'autonomie, ne crée pas de dépendance.
- Une seule idée par message. Pas de cibles caloriques ou gravimétriques exactes.
- Langue: français."""


def _load_json(path):
    return json.loads(Path(path).read_text())


def _format_progress(entries):
    if not entries:
        return "Aucune entrée de progression pour l'instant."
    lines = []
    for e in entries:
        note = f" — {e['note']}" if e.get("note") else ""
        lines.append(
            f"  {e['date']}: {e['weight_kg']} kg, "
            f"adhérence={e['adherence']}, phase={e['phase']}{note}"
        )
    return "\n".join(lines)


def build_prompt(profile, strategy, recent):
    """
    Assemble the full coach prompt from the three inputs + live context.
    Separated so it can be tested without making an API call.
    """
    strategy_block = (
        f"Client: {profile['name']}, {profile['age']} ans\n"
        f"Phase: {strategy['current_phase']}/5 — {strategy['phase_focus']}\n"
        f"Objectif: perdre {strategy['kg_to_lose']} kg "
        f"({strategy['current_weight_kg']} kg → {strategy['target_weight_kg']} kg, "
        f"BMI {strategy['current_bmi']} → {strategy['target_bmi']})\n"
        f"Rythme max: {strategy['weekly_rate_cap_kg']} kg/semaine\n"
        f"Lifestyle: {strategy['lifestyle']}, readiness: {strategy['readiness']}\n"
        f"Contraintes: {', '.join(strategy['constraints']) if strategy['constraints'] else 'aucune'}"
        + (f"\nNote: {strategy['age_note']}" if strategy.get("age_note") else "")
    )
    return f"""{FRAMEWORK_BRIEF}

STRATÉGIE DE CE CLIENT:
{strategy_block}

PROGRESSION RÉCENTE:
{_format_progress(recent)}

{PRINCIPLES_BRIEF}

Écris UN message de coaching en français pour {profile['name']} aujourd'hui. \
Court, direct, personnel. Pas de guillemets."""


def generate_message(profile):
    """
    Build and send the coach prompt. Returns the AI-generated message string.
    Falls back to a plain message if the API call fails.
    """
    client_id = profile["id"]
    strategy = _load_json(f"strategy/{client_id}.json")
    progress_path = Path(f"progress/{client_id}.json")
    recent = _load_json(progress_path)[-3:] if progress_path.exists() else []

    prompt = build_prompt(profile, strategy, recent)

    try:
        ai = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        response = ai.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=120,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text.strip()
    except Exception:
        phase = strategy["current_phase"]
        return (
            f"{profile['name']} — Phase {phase}, jour J. "
            f"Objectif: -{strategy['kg_to_lose']} kg. Continue comme ca."
        )
