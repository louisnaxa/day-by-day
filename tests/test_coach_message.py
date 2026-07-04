"""
Tests for coach_message.py — that the coach actually uses the strategy and
progress data, not generic filler.
"""

from coach_message import build_prompt


def _strategy():
    return {
        "client_id": "test",
        "status": "active",
        "current_bmi": 26.8,
        "target_bmi": 24.6,
        "current_weight_kg": 85.0,
        "target_weight_kg": 78.0,
        "kg_to_lose": 7.0,
        "weekly_rate_cap_kg": 0.85,
        "current_phase": 2,
        "phase_focus": "Habit-building: build 2-3 keystone habits.",
        "lifestyle": "moderate",
        "readiness": "high",
        "autonomy_level": "low",
        "constraints": [],
        "age_note": None,
    }


def _profile():
    return {
        "id": "test",
        "name": "TestClient",
        "age": 30,
        "height_cm": 178,
        "current_weight_kg": 85.0,
        "target_weight_kg": 78.0,
        "lifestyle": "moderate",
        "readiness": "high",
        "constraints": [],
        "current_phase": 2,
        "autonomy_level": "low",
        "start_date": "2026-01-01",
        "desired_weekly_loss_kg": None,
    }


def _recent_progress():
    return [
        {"date": "2026-07-01", "weight_kg": 85.5, "adherence": "high", "phase": 2, "note": "Bonne semaine."},
        {"date": "2026-07-04", "weight_kg": 85.0, "adherence": "medium", "phase": 2, "note": None},
    ]


# ── Test 6: Prompt contains strategy values and recent progress ───────────────

def test_prompt_contains_phase_focus():
    """The phase focus from the strategy must appear in the prompt."""
    prompt = build_prompt(_profile(), _strategy(), _recent_progress())
    assert "Habit-building" in prompt


def test_prompt_contains_rate_cap():
    """The weekly rate cap must appear in the prompt."""
    prompt = build_prompt(_profile(), _strategy(), _recent_progress())
    assert "0.85" in prompt


def test_prompt_contains_kg_to_lose():
    """The kg_to_lose value must appear in the prompt."""
    prompt = build_prompt(_profile(), _strategy(), _recent_progress())
    assert "7.0" in prompt


def test_prompt_contains_recent_progress():
    """Recent progress entries must appear in the prompt."""
    prompt = build_prompt(_profile(), _strategy(), _recent_progress())
    assert "85.5" in prompt   # weight from first entry
    assert "high" in prompt   # adherence from first entry


def test_prompt_contains_client_name():
    """Client name must appear in the prompt."""
    prompt = build_prompt(_profile(), _strategy(), _recent_progress())
    assert "TestClient" in prompt


def test_prompt_with_no_progress_still_builds():
    """An empty progress list must not crash the prompt builder."""
    prompt = build_prompt(_profile(), _strategy(), [])
    assert "TestClient" in prompt
    assert "0.85" in prompt
