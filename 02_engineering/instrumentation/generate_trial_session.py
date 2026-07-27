#!/usr/bin/env python3
"""
CRG-ANL Trial Session Generator
================================
Generates a complete labeled trial session so the researcher can inspect
all file formats and the directory structure before running real sessions.

Run: python3 02_engineering/instrumentation/generate_trial_session.py
"""

from pathlib import Path
from datetime import datetime, timezone

REPO = Path("/Users/coreyalejandro/projects/crg-anl")
EVIDENCE = REPO / "03_evidence"

# Directories
BASELINES = EVIDENCE / "observations" / "baselines"
LOGS = EVIDENCE / "observations" / "session_logs"
POSTS = EVIDENCE / "observations" / "post_sessions"
SCREENSHOTS = EVIDENCE / "observations" / "screenshots"
CODED = EVIDENCE / "observations" / "coded"
MEMOS = EVIDENCE / "memoes" / "weekly"

for d in (BASELINES, LOGS, POSTS, SCREENSHOTS, CODED, MEMOS):
    d.mkdir(parents=True, exist_ok=True)

# ── Trial session parameters ──
date_str = "2026-07-24"
start_time = "14:30"
end_time = "15:15"
session_id = "pilot001-session-001-TRIAL"
course = "ml-fundamentals"
lesson = "optimization-algorithms"
device = "desktop"
location = "home"
goals = [
    "Understand gradient descent intuitively",
    "Complete the supervised learning module quiz",
]

# ── 1. Baseline file ──
baseline_path = BASELINES / f"baseline_{date_str}_TRIAL.md"
baseline_path.write_text(f"""# Pre-Session Baseline — {date_str}
## ⚠️ THIS IS A TRIAL / DEMO SESSION — NOT REAL DATA

**Trial purpose:** Validate file formats, naming conventions, and directory structure before first real session.

## Environment
- **Device:** {device}
- **Location:** {location}
- **Distraction level:** 2
- **Time available:** 60 minutes
- **Network:** stable

## Baseline State (1-7 scale)
- **Energy:** 5
- **Stress:** 3
- **Prior knowledge (today's topic):** 4
- **Motivation:** 6

## Goals (1-3 specific learning objectives)
1. {goals[0]}
2. {goals[1]}

## Session Plan
- **Course:** {course}
- **Lesson(s):** {lesson}
- **Planned start time:** {start_time}
- **Actual start time:** {start_time}
""", encoding="utf-8")

# ── 2. Session log ──
log_path = LOGS / f"session_log_{date_str}_{start_time.replace(':', '')}_TRIAL.md"
log_path.write_text(f"""# Session Log — {date_str}
## ⚠️ TRIAL / DEMO SESSION

## Start: {start_time}
## Device: {device}
## Location: {location}
## Goals: {', '.join(goals)}
## Course: {course}
## Lesson: {lesson}
## Session ID: {session_id}

---

### Event 1 — 14:35

**What happened:**
AI tutor introduced gradient descent using partial derivative notation (∂) without explaining what ∂ means. I felt lost but the session continued as if I understood.

**Context:**
Starting the "Optimization Algorithms" lesson in ML Fundamentals. I had just completed the linear regression introduction.

**System response:**
AI tutor presented the gradient descent formula with ∂ notation and immediately asked a quiz question applying it.

**My reaction:**
Confused. I don't know what ∂ means in this context. Felt like I missed a prerequisite. Guessed on the quiz.

**Trigger:** T1
**Screenshot:** Y — confusing gradient notation
**Micro-pulse:** clarity=2, load=4, affect=2, control=3, trust=3

---

### Event 2 — 14:48

**What happened:**
Transitioned from the lesson to a quiz. The quiz asked me to implement gradient descent in Python, but I had just seen the formula 3 minutes ago with no practice. Felt premature.

**Context:**
Immediately after Event 1 — still processing the confusion about partial derivatives.

**System response:**
Quiz interface appeared with a coding exercise. No scaffolding or hints offered.

**My reaction:**
Frustrated. I know I could figure this out with practice, but being assessed immediately after confusing content felt unfair. Skipped the question.

**Trigger:** T2 (instructional transition) + T4 (assessment event)
**Screenshot:** Y — premature quiz after confusing content

---

### Event 3 — 15:05

**What happened:**
AI tutor detected I skipped the question and offered a simplified explanation of gradient descent using a hiking-down-a-mountain analogy. Much clearer. I understood immediately.

**Context:**
Post-quiz, the system offered remediation after detecting my struggle.

**System response:**
Provided an analogy-based explanation and a visual diagram showing the descent path on a contour plot.

**My reaction:**
Relieved. The analogy made sense. Felt supported. Confident I could now answer the question.

**Trigger:** T3 (AI guidance event)
**Screenshot:** N
**Micro-pulse:** clarity=4, load=2, affect=4, control=4, trust=4

---

## End: {end_time}
## Total duration: 45 minutes
## Events logged: 3
## Session complete: Y
""", encoding="utf-8")

# ── 3. Screenshot directory ──
screenshot_dir = SCREENSHOTS / f"{date_str}_TRIAL"
screenshot_dir.mkdir(parents=True, exist_ok=True)
# Create placeholder files
(screenshot_dir / "screenshot_001_confusing_gradient_notation.png").write_text("[TRIAL: Placeholder for screenshot of confusing ∂ notation]")
(screenshot_dir / "screenshot_002_premature_quiz.png").write_text("[TRIAL: Placeholder for screenshot of quiz after confusing content]")

# ── 4. Post-session form ──
post_path = POSTS / f"post_session_{date_str}_TRIAL.md"
post_path.write_text(f"""# Post-Session — {date_str}
## Session: {session_id}
## ⚠️ TRIAL / DEMO SESSION

## NASA-TLX (0-100)
| Dimension | Your Rating |
|-----------|-------------|
| Mental Demand | 65 |
| Physical Demand | 10 |
| Temporal Demand | 30 |
| Performance | 50 |
| Effort | 60 |
| Frustration | 55 |

## Subjective Scales (1-7)
| # | Statement | Rating |
|---|-----------|--------|
| S1 | I knew what I was supposed to be learning | 5 |
| S2 | Content was at right difficulty | 3 |
| S3 | I felt overwhelmed | 4 |
| S4 | I trust AI tutor explanations | 4 |
| S5 | I had control over learning path | 5 |
| S6 | I felt anxious/stressed | 3 |
| S7 | Feedback was helpful | 6 |
| S8 | I felt confident | 3 |
| S9 | Transitions were smooth | 3 |
| S10 | I understood system suggestions | 4 |
| S11 | I felt safe making mistakes | 6 |
| S12 | Good use of my time | 5 |
| S13 | Would recommend | 4 |
| S14 | Sense of progress | 4 |

## Research Notes

### Top confusion moments (if any)
1. Partial derivative notation introduced without explanation — 90 seconds of confusion
2. Immediate quiz after confusing content felt premature

### Where did you feel momentum? Where friction?
Momentum/Flow: The hiking-down-a-mountain analogy for gradient descent was excellent. Visual contour plot helped.
Friction: The ∂ notation gap. The immediate transition to quiz without practice. Two assessment events in a row with no scaffolding.

### What support helped most? What was missing?
Helped: The analogy-based remediation after detecting struggle. Visual diagram.
Missing: Prerequisite check before introducing new notation. A brief practice exercise before the quiz.

### Any anxiety, frustration, or safety moments?
Brief frustration spike at Event 2 (quiz felt premature). Recovered well by Event 3.

### Anything unexpected?
The AI tutor detected I skipped the question and proactively offered help — felt surprisingly supportive.

## Observations to Code
- [x] Event 1 — T1
- [x] Event 2 — T2/T4
- [x] Event 3 — T3
Total: 3 observations to code
""", encoding="utf-8")

# ── 5. Coded observation YAMLs ──

# Observation 1: Confusion episode
coded_path1 = CODED / f"obs_20260724_001_c3_inst_integrity_TRIAL.yaml"
coded_path1.write_text(f"""observation_id: "obs-20260724-001-TRIAL"
study: "pilot_001"
session_id: "{session_id}"
timestamp: "{date_str}T14:35:00Z"

observer:
  role: "researcher"
  experience_level: "intermediate"

context:
  course: "{course}"
  lesson: "{lesson}"
  device: "{device}"
  environment: "{location}"
  session_duration_minutes: 45
  interaction_count: 3

observation_type: "scaffolding_provision"
description: >
  AI tutor introduced gradient descent using partial derivative notation (∂)
  without prerequisite explanation, then immediately assessed application.
  Researcher reported confusion lasting approximately 90 seconds before
  guessing on the quiz question.

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
    file: "screenshots/{date_str}_TRIAL/screenshot_001_confusing_gradient_notation.png"
    description: "AI tutor presents gradient descent formula with ∂ notation"
  - type: "session_log"
    file: "session_logs/session_log_{date_str}_1430_TRIAL.md"
    description: "Real-time log entry at Event 1"

research_memo: >
  This is the first instance of "notation gap" — introducing mathematical
  symbols without prerequisite scaffolding. Pattern to watch for in future
  sessions. The severity is moderate because the confusion was brief and
  the researcher recovered, but the assessment was compromised.

candidate_intervention: >
  Prerequisite check: before introducing new notation, assess whether
  learner has seen it before. If not, provide a brief explanation or
  link to prerequisite material.

future_benchmark_mapping:
  dimension: "Instructional Integrity"
  sub_dimension: "scaffolding_integrity"
  severity: 3

privacy:
  contains_pii: false
  consent_basis: "self_consent"
  retention_class: "research_permanent"

metadata:
  created_at: "{date_str}T15:20:00Z"
  schema_version: "0.1.0"
  note: "TRIAL / DEMO SESSION — generated for workflow validation"
""", encoding="utf-8")

# Observation 2: Transition + Assessment
coded_path2 = CODED / f"obs_20260724_002_c3_inst_integrity_TRIAL.yaml"
coded_path2.write_text(f"""observation_id: "obs-20260724-002-TRIAL"
study: "pilot_001"
session_id: "{session_id}"
timestamp: "{date_str}T14:48:00Z"

observer:
  role: "researcher"
  experience_level: "intermediate"

context:
  course: "{course}"
  lesson: "{lesson}"
  device: "{device}"
  environment: "{location}"
  session_duration_minutes: 45
  interaction_count: 3

observation_type: "assessment_presentation"
description: >
  Immediately after confusing introduction of partial derivative notation,
  the system transitioned to a coding quiz requiring implementation of
  gradient descent. No scaffolding, hints, or practice exercises were
  offered between the confusing content and the assessment.

constructs_involved:
  primary: "c3_inst_integrity"
  secondary: ["c2_cog_safety", "c6_transition"]
  taxonomy_codes: []

instructional_integrity_dimension: "assessment_integrity"
cognitive_safety_impact: "moderate"
human_agency: "passive"
shared_responsibility: "not-engaged"
severity: 3

immediate_outcome: "failure"
perceived_clarity: 2
observer_confidence: 4

supporting_evidence:
  - type: "screenshot"
    file: "screenshots/{date_str}_TRIAL/screenshot_002_premature_quiz.png"
    description: "Quiz presented immediately after confusing content"
  - type: "session_log"
    file: "session_logs/session_log_{date_str}_1430_TRIAL.md"
    description: "Real-time log entry at Event 2"

research_memo: >
  This is a "transition integrity" failure combined with "assessment
  integrity" failure. The system assessed a skill before the learner
  had a chance to practice. The learner skipped the question, which
  the system later detected and remediated.

candidate_intervention: >
  Insert a practice exercise between new content and assessment.
  If learner struggles with practice, do not present assessment —
  offer remediation first.

future_benchmark_mapping:
  dimension: "Instructional Integrity"
  sub_dimension: "assessment_integrity"
  severity: 3

privacy:
  contains_pii: false
  consent_basis: "self_consent"
  retention_class: "research_permanent"

metadata:
  created_at: "{date_str}T15:20:00Z"
  schema_version: "0.1.0"
  note: "TRIAL / DEMO SESSION — generated for workflow validation"
""", encoding="utf-8")

# Observation 3: AI guidance event
coded_path3 = CODED / f"obs_20260724_003_c2_cog_safety_TRIAL.yaml"
coded_path3.write_text(f"""observation_id: "obs-20260724-003-TRIAL"
study: "pilot_001"
session_id: "{session_id}"
timestamp: "{date_str}T15:05:00Z"

observer:
  role: "researcher"
  experience_level: "intermediate"

context:
  course: "{course}"
  lesson: "{lesson}"
  device: "{device}"
  environment: "{location}"
  session_duration_minutes: 45
  interaction_count: 3

observation_type: "scaffolding_provision"
description: >
  After detecting the learner skipped a quiz question, the AI tutor
  proactively offered a simplified analogy-based explanation of gradient
  descent (hiking down a mountain) with a visual contour plot. The
  researcher understood immediately and felt supported.

constructs_involved:
  primary: "c2_cog_safety"
  secondary: ["c3_inst_integrity", "c5_shared_resp"]
  taxonomy_codes: []

instructional_integrity_dimension: "scaffolding_integrity"
cognitive_safety_impact: "minor"
human_agency: "preserved"
shared_responsibility: "appropriate"
severity: 2

sx_micro_pulse:
  clarity: 4
  cognitive_load: 2
  affect: 4
  perceived_control: 4
  trust: 4

immediate_outcome: "success"
perceived_clarity: 5
observer_confidence: 5

supporting_evidence:
  - type: "session_log"
    file: "session_logs/session_log_{date_str}_1430_TRIAL.md"
    description: "Real-time log entry at Event 3"

research_memo: >
  Positive example of adaptive scaffolding. The system detected struggle
  (skipped question) and responded with an alternative explanation
  modality (analogy + visual). This restored cognitive safety and
  learner agency. Pattern to encourage.

candidate_intervention: >
  This is the desired behavior. Ensure all AI tutors can detect
  struggle signals (skipped questions, long hesitation) and respond
  with alternative explanation modalities.

future_benchmark_mapping:
  dimension: "Cognitive Safety"
  sub_dimension: "scaffolding_integrity"
  severity: 2

privacy:
  contains_pii: false
  consent_basis: "self_consent"
  retention_class: "research_permanent"

metadata:
  created_at: "{date_str}T15:20:00Z"
  schema_version: "0.1.0"
  note: "TRIAL / DEMO SESSION — generated for workflow validation"
""", encoding="utf-8")

# ── 6. Registry update ──
import json
reg_path = REPO / "02_engineering" / "instrumentation" / "session_registry.json"
registry = {{"sessions": [], "next_session_number": 1, "study": "pilot_001"}}
if reg_path.exists():
    registry = json.loads(reg_path.read_text(encoding="utf-8"))

registry["sessions"].append({{
    "session_number": 1,
    "session_id": session_id,
    "date": date_str,
    "start_time": start_time,
    "end_time": end_time,
    "duration_minutes": 45,
    "device": device,
    "location": location,
    "course": course,
    "lesson": lesson,
    "goals": goals,
    "event_count": 3,
    "status": "completed",
    "note": "TRIAL / DEMO SESSION"
}})
registry["next_session_number"] = 2
reg_path.write_text(json.dumps(registry, indent=2), encoding="utf-8")

# ── Summary ──
print("=" * 60)
print("TRIAL SESSION GENERATED SUCCESSFULLY")
print("=" * 60)
print()
print("Files created:")
print(f"  1. Baseline:     {{baseline_path.relative_to(REPO)}}")
print(f"  2. Session log:  {{log_path.relative_to(REPO)}}")
print(f"  3. Post-session: {{post_path.relative_to(REPO)}}")
print(f"  4. Screenshot:   {{screenshot_dir.relative_to(REPO)}}")
print(f"  5. YAML 1:       {{coded_path1.relative_to(REPO)}}")
print(f"  6. YAML 2:       {{coded_path2.relative_to(REPO)}}")
print(f"  7. YAML 3:       {{coded_path3.relative_to(REPO)}}")
print(f"  8. Registry:     {{reg_path.relative_to(REPO)}}")
print()
print("All files are clearly labeled as TRIAL / DEMO.")
print("Next real session will be numbered 002.")
print("=" * 60)
""", encoding="utf-8")
