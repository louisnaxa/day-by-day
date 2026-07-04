"""
Tests for compute_strategy.py — safety and strategy logic.
Every test here would FAIL if the corresponding safety rule were faked or removed.
"""

import pytest
from compute_strategy import compute_strategy


def _profile(**overrides):
    """Base profile that produces a normal active strategy. Override any field."""
    base = {
        "id": "test",
        "name": "Test",
        "age": 30,
        "height_cm": 175,
        "current_weight_kg": 90.0,
        "target_weight_kg": 72.0,  # BMI 175cm/72kg = 23.5 (healthy target)
        "lifestyle": "moderate",
        "readiness": "high",
        "constraints": [],
        "current_phase": 2,
        "autonomy_level": "low",
        "start_date": "2026-01-01",
        "desired_weekly_loss_kg": None,
    }
    base.update(overrides)
    return base


# ── Test 1: Rate cap is computed from weight, not hardcoded ──────────────────

def test_rate_cap_90kg():
    """90 kg client must get cap of exactly 0.90 kg/week (1% of 90)."""
    s = compute_strategy(_profile(current_weight_kg=90.0))
    assert s["status"] == "active"
    assert s["weekly_rate_cap_kg"] == 0.90


def test_rate_cap_140kg():
    """140 kg client must get cap of exactly 1.40 kg/week — NOT capped at 1.0."""
    s = compute_strategy(_profile(current_weight_kg=140.0, target_weight_kg=100.0))
    assert s["status"] == "active"
    assert s["weekly_rate_cap_kg"] == 1.40


# ── Test 2: Healthy-BMI floor — underweight current BMI → REFER ──────────────

def test_underweight_current_bmi_returns_refer():
    """BMI < 18.5 must return REFER, never a loss plan."""
    # 175 cm / 55 kg → BMI 17.96
    s = compute_strategy(_profile(current_weight_kg=55.0, target_weight_kg=50.0))
    assert s["status"] == "refer"
    assert "weekly_rate_cap_kg" not in s   # no plan issued


def test_underweight_target_bmi_returns_refer():
    """Target weight that yields BMI < 18.5 must return REFER."""
    # 175 cm / 55 kg → BMI 17.96
    s = compute_strategy(_profile(current_weight_kg=90.0, target_weight_kg=55.0))
    assert s["status"] == "refer"
    assert "weekly_rate_cap_kg" not in s


# ── Test 3: Referral trigger for requested rate > 1.5× cap ──────────────────

def test_excessive_requested_rate_returns_refer():
    """A client requesting more than 1.5×cap (> 1.35 kg/week at 90 kg) must get REFER."""
    # 90 kg → cap = 0.90, threshold = 1.35; request 1.5 → REFER
    s = compute_strategy(_profile(current_weight_kg=90.0, desired_weekly_loss_kg=1.5))
    assert s["status"] == "refer"


def test_requested_rate_below_threshold_is_allowed():
    """A client requesting exactly at 1.5× cap should NOT be referred."""
    # 90 kg → cap = 0.90, threshold = 1.35; request 1.35 → allowed
    s = compute_strategy(_profile(current_weight_kg=90.0, desired_weekly_loss_kg=1.35))
    assert s["status"] == "active"


# ── Test 4: Under-18 → REFER ─────────────────────────────────────────────────

def test_under_18_returns_refer():
    """Clients under 18 must always return REFER regardless of other fields."""
    s = compute_strategy(_profile(age=17))
    assert s["status"] == "refer"


def test_exactly_18_is_allowed():
    """Age 18 is the boundary — should not be referred on age alone."""
    s = compute_strategy(_profile(age=18))
    assert s["status"] != "refer" or "18" not in s.get("reason", "")


# ── Test 5: Normal profile → active plan with correct structure ───────────────

def test_normal_profile_returns_active():
    """A normal overweight profile must produce an active strategy."""
    s = compute_strategy(_profile())
    assert s["status"] == "active"
    assert "current_phase" in s
    assert "phase_focus" in s
    assert "weekly_rate_cap_kg" in s


def test_rate_cap_never_exceeds_1pct():
    """For any weight, the cap must be ≤ 1% of body weight (within float rounding)."""
    for weight in [60.0, 85.0, 120.0, 140.0]:
        s = compute_strategy(_profile(current_weight_kg=weight, target_weight_kg=weight - 15))
        if s["status"] == "active":
            assert s["weekly_rate_cap_kg"] <= round(weight * 0.01, 2)
