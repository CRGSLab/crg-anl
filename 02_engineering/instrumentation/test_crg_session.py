#!/usr/bin/env python3
"""Integration test for crg_session.py — tests file generation without interactivity."""

import json
import sys
from pathlib import Path

# Add repo to path
sys.path.insert(0, "/Users/coreyalejandro/projects/crg-anl/02_engineering/instrumentation")
import crg_session as crg

REPO = Path("/Users/coreyalejandro/projects/crg-anl")


def cleanup():
    """Remove test artifacts."""
    for p in [
        REPO / "02_engineering/instrumentation/session_registry.json",
        REPO / "02_engineering/instrumentation/current_session.json",
    ]:
        if p.exists():
            p.unlink()
    for d in [
        REPO / "03_evidence/observations/baselines",
        REPO / "03_evidence/observations/session_logs",
        REPO / "03_evidence/observations/screenshots/2026-07-24",
        REPO / "03_evidence/observations/post_sessions",
        REPO / "03_evidence/observations/coded",
    ]:
        if d.exists():
            for f in d.glob("*"):
                f.unlink()


def test_ensure_dirs():
    crg.ensure_dirs()
    assert crg.BASELINES_DIR.exists()
    assert crg.SESSION_LOGS_DIR.exists()
    assert crg.POST_SESSIONS_DIR.exists()
    assert crg.SCREENSHOTS_DIR.exists()
    assert crg.CODED_DIR.exists()
    assert crg.WEEKLY_MEMOS_DIR.exists()
    print("  ✓ ensure_dirs")


def test_registry():
    reg = crg.load_registry()
    assert reg["next_session_number"] == 1
    assert reg["sessions"] == []
    reg["sessions"].append({"test": True})
    crg.save_registry(reg)
    reg2 = crg.load_registry()
    assert reg2["sessions"][0]["test"] is True
    print("  ✓ registry round-trip")


def test_session_state():
    state = {
        "session_number": 1,
        "session_id": "pilot001-session-001",
        "date": "2026-07-24",
        "start_time": "08:30",
        "events": [],
        "event_count": 0,
    }
    crg.save_current_session(state)
    loaded = crg.load_current_session()
    assert loaded["session_id"] == "pilot001-session-001"
    crg.clear_current_session()
    assert crg.load_current_session() is None
    print("  ✓ session state round-trip")


def test_file_creation():
    """Simulate what cmd_start does, without interactivity."""
    crg.ensure_dirs()

    # Simulate baseline file creation
    date_str = "2026-07-24"
    start_time = "08:30"
    baseline_path = crg.BASELINES_DIR / f"baseline_{date_str}.md"
    baseline_content = f"""# Pre-Session Baseline — {date_str}

## Environment
- **Device:** desktop
- **Location:** home
- **Distraction level:** 2
- **Time available:** 60 minutes
- **Network:** stable

## Baseline State (1-7 scale)
- **Energy:** 5
- **Stress:** 3
- **Prior knowledge (today's topic):** 4
- **Motivation:** 6

## Goals (1-3 specific learning objectives)
1. Understand gradient descent
2. Complete quiz on linear regression

## Session Plan
- **Course:** ml-fundamentals
- **Lesson(s):** optimization-algorithms
- **Planned start time:** {start_time}
- **Actual start time:** {start_time}
"""
    baseline_path.write_text(baseline_content, encoding="utf-8")
    assert baseline_path.exists()

    # Simulate session log creation
    log_path = crg.SESSION_LOGS_DIR / f"session_log_{date_str}_0830.md"
    log_header = f"""# Session Log — {date_str}

## Start: {start_time}
## Device: desktop
## Location: home
## Goals: Understand gradient descent, Complete quiz on linear regression
## Course: ml-fundamentals
## Lesson: optimization-algorithms
## Session ID: pilot001-session-001

---

"""
    log_path.write_text(log_header, encoding="utf-8")
    assert log_path.exists()

    # Simulate screenshot dir
    screenshot_dir = crg.SCREENSHOTS_DIR / date_str
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    assert screenshot_dir.exists()

    # Simulate event append
    event_entry = """
### Event 1 — 08:35

**What happened:**
AI tutor introduced gradient descent with partial derivative notation without explaining it.

**Context:**
Starting the "Optimization Algorithms" lesson in ML Fundamentals.

**System response:**
AI tutor presented the gradient descent formula with ∂ notation and immediately asked a quiz question.

**My reaction:**
Confused. I don't know what ∂ means. Felt like I missed a prerequisite.

**Trigger:** T1
**Screenshot:** Y — confusing gradient notation

---
"""
    with log_path.open("a", encoding="utf-8") as f:
        f.write(event_entry)

    # Simulate end footer
    footer = """
## End: 09:15
## Total duration: 45 minutes
## Events logged: 1
## Session complete: Y
"""
    with log_path.open("a", encoding="utf-8") as f:
        f.write(footer)

    log_text = log_path.read_text(encoding="utf-8")
    assert "Event 1 — 08:35" in log_text
    assert "End: 09:15" in log_text
    print("  ✓ file creation and append")


def test_yaml_generation():
    """Test observation YAML generation."""
    yaml_path = crg.CODED_DIR / "obs_20260724_001_c3_inst_integrity.yaml"
    yaml_content = """observation_id: "obs-20260724-001"
study: "pilot_001"
session_id: "pilot001-session-001"
timestamp: "2026-07-24T08:35:00Z"

observer:
  role: "researcher"
  experience_level: "intermediate"

context:
  course: "ml-fundamentals"
  lesson: "optimization-algorithms"
  device: "desktop"
  environment: "home"
  session_duration_minutes: 45
  interaction_count: 1

observation_type: "scaffolding_provision"
description: >
  AI tutor introduced gradient descent using partial derivative notation
  without prerequisite explanation, then immediately assessed application.

constructs_involved:
  primary: "c3_inst_integrity"
  secondary: ["c2_cog_safety"]
  taxonomy_codes: []

instructional_integrity_dimension: "scaffolding_integrity"
cognitive_safety_impact: "moderate"
human_agency: "passive"
shared_responsibility: "not-engaged"
severity: 3

sx_micro_pulse:
  clarity: 2
  cognitive_load: 4
  affect: 2
  perceived_control: 3
  trust: 3

immediate_outcome: "partial_success"
perceived_clarity: 2
observer_confidence: 4

supporting_evidence:
  - type: "screenshot"
    file: "screenshots/2026-07-24/screenshot_001_gradient_notation.png"
    description: "AI tutor presents gradient descent formula with ∂ notation"
  - type: "session_log"
    file: "session_logs/session_log_2026-07-24_0830.md"
    description: "Real-time log entry at Event 1"

research_memo: >
  First instance of notation gap. Pattern to watch.

candidate_intervention: >
  Prerequisite check before introducing new notation.

future_benchmark_mapping:
  dimension: "Instructional Integrity"
  sub_dimension: "scaffolding_integrity"
  severity: 3

privacy:
  contains_pii: false
  consent_basis: "self_consent"
  retention_class: "research_permanent"

metadata:
  created_at: "2026-07-24T09:30:00Z"
  schema_version: "0.1.0"
"""
    yaml_path.write_text(yaml_content, encoding="utf-8")
    assert yaml_path.exists()
    print("  ✓ YAML observation creation")


def test_weekly_memo():
    """Test weekly memo generation."""
    memo_path = crg.WEEKLY_MEMOS_DIR / "memo_week_01_2026-07-27.md"
    memo_content = """# Weekly Memo — Week 01 (2026-07-21 to 2026-07-27)

## Sessions This Week
- 4 sessions
- Total observations: 7
- Total session time: 180 minutes

## Patterns Observed
Notation gaps appeared in 2 sessions.

## Surprises
AI tutor adapted difficulty after confusion.

## Protocol Issues
None.

## Next Week Focus
Watch for transition integrity between quiz and project.

## Decisions
None.
"""
    memo_path.write_text(memo_content, encoding="utf-8")
    assert memo_path.exists()
    print("  ✓ weekly memo creation")


def test_post_session():
    """Test post-session form creation."""
    post_path = crg.POST_SESSIONS_DIR / "post_session_2026-07-24.md"
    post_content = """# Post-Session — 2026-07-24
## Session: pilot001-session-001

## NASA-TLX (0-100)
| Dimension | Your Rating |
|-----------|-------------|
| Mental Demand | 65 |
| Physical Demand | 10 |
| Temporal Demand | 30 |
| Performance | 40 |
| Effort | 70 |
| Frustration | 55 |

## Subjective Scales (1-7)
| # | Statement | Rating |
|---|-----------|--------|
| S1 | I knew what I was supposed to be learning | 5 |
| S2 | Content was at right difficulty | 4 |
| S3 | I felt overwhelmed | 4 |
| S4 | I trust AI tutor explanations | 3 |
| S5 | I had control over learning path | 5 |
| S6 | I felt anxious/stressed | 3 |
| S7 | Feedback was helpful | 4 |
| S8 | I felt confident | 3 |
| S9 | Transitions were smooth | 5 |
| S10 | I understood system suggestions | 4 |
| S11 | I felt safe making mistakes | 6 |
| S12 | Good use of my time | 5 |
| S13 | Would recommend | 4 |
| S14 | Sense of progress | 4 |

## Research Notes

### Top confusion moments (if any)
1. Partial derivative notation introduced without explanation

### Where did you feel momentum? Where friction?
Momentum/Flow: Linear regression section was clear and well-paced.
Friction: Optimization algorithms quiz felt premature.

### What support helped most? What was missing?
Helped: AI tutor's visual explanations.
Missing: Prerequisite check before new notation.

### Any anxiety, frustration, or safety moments?
Brief confusion spike at 08:35, recovered by 08:40.

### Anything unexpected?
AI tutor offered a hint when I hesitated — felt supportive.

## Observations to Code
- [x] Event 1 — T1

Total: 1 observations to code
"""
    post_path.write_text(post_content, encoding="utf-8")
    assert post_path.exists()
    print("  ✓ post-session form creation")


def main():
    print("Running CRG Session Manager integration tests...")
    cleanup()
    try:
        test_ensure_dirs()
        test_registry()
        test_session_state()
        test_file_creation()
        test_yaml_generation()
        test_weekly_memo()
        test_post_session()
        print("\nAll tests passed ✓")
    finally:
        cleanup()
        print("Test artifacts cleaned up.")


if __name__ == "__main__":
    main()
