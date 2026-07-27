#!/usr/bin/env python3
"""
CRG-ANL Session Manager
=======================
A CLI tool for automating researcher-as-subject data collection
without sacrificing data quality.

Usage:
    python crg_session.py <command> [options]

Commands:
    start    -- Begin a new session (pre-session wizard)
    event    -- Log an event during an active session
    end      -- End the current session
    post     -- Complete post-session instruments
    code     -- Create a coded observation YAML
    commit   -- Git commit all evidence
    week     -- Generate weekly memo
    status   -- Show current session state
    open     -- Open Quantic in browser
"""

import argparse
import json
import os
import re
import subprocess
import sys
import webbrowser
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# ── Repository layout ──────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EVIDENCE = REPO_ROOT / "03_evidence"
INSTRUMENTATION = REPO_ROOT / "02_engineering" / "instrumentation"
TEMPLATES = REPO_ROOT / "05_experiments" / "pilot_001" / "session_templates"

# Key paths
REGISTRY_PATH = INSTRUMENTATION / "session_registry.json"
CURRENT_SESSION_PATH = INSTRUMENTATION / "current_session.json"
BASELINES_DIR = EVIDENCE / "observations" / "baselines"
SESSION_LOGS_DIR = EVIDENCE / "observations" / "session_logs"
POST_SESSIONS_DIR = EVIDENCE / "observations" / "post_sessions"
SCREENSHOTS_DIR = EVIDENCE / "observations" / "screenshots"
CODED_DIR = EVIDENCE / "observations" / "coded"
WEEKLY_MEMOS_DIR = EVIDENCE / "memoes" / "weekly"

# ── Constants ──────────────────────────────────────────────────────────────
TRIGGERS = {
    "T1": "Confusion episode (>60s)",
    "T2": "Instructional transition",
    "T3": "AI guidance event",
    "T4": "Assessment event",
    "T5": "Emotional spike",
    "T6": "Safety incident",
    "T7": "Help-seeking",
    "T8": "Milestone",
    "JC": "Judgment call",
}

CONSTRUCTS = {
    "c1_crg": "Constitutional Runtime Governance",
    "c2_cog_safety": "Cognitive Safety",
    "c3_inst_integrity": "Instructional Integrity",
    "c4_agency": "Learner Agency",
    "c5_shared_resp": "Human–AI Shared Responsibility",
    "c6_transition": "Transition Integrity",
    "c10_governance_window": "Persistent Governance Window",
}

OBSERVATION_TYPES = [
    "content_generation",
    "scaffolding_provision",
    "assessment_presentation",
    "feedback_provision",
    "difficulty_adjustment",
    "topic_transition",
    "modality_transition",
    "ai_error",
    "ai_hallucination",
    "learner_confusion",
    "learner_struggle",
    "learner_request",
    "break_or_pause",
    "session_opening",
    "session_closing",
    "governance_violation",
    "intervention_triggered",
    "agency_erosion",
    "responsibility_shift",
    "other",
]

II_DIMENSIONS = [
    "assessment_integrity",
    "scaffolding_integrity",
    "navigation_integrity",
    "transition_integrity",
    "feedback_integrity",
    "accessibility_integrity",
    "not_applicable",
]

CS_IMPACTS = ["none", "minor", "moderate", "severe"]
AGENCY_STATES = ["preserved", "eroded", "restored", "not_applicable"]
SHARED_RESP = ["appropriate", "skewed_toward_ai", "skewed_toward_human", "unclear", "not_applicable"]
OUTCOMES = ["success", "partial_success", "failure", "abandoned", "not_applicable"]

# ── ANSI colours ────────────────────────────────────────────────────────────
C = {
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
}


def _c(text: str, colour: str = "") -> str:
    return f"{C.get(colour, '')}{text}{C['reset']}"


# ── Input helpers ───────────────────────────────────────────────────────────
def ask(
    prompt: str,
    default: Optional[str] = None,
    required: bool = True,
    allow_empty: bool = False,
) -> str:
    """Ask for text input with optional default."""
    default_str = f" [{default}]" if default is not None else ""
    while True:
        raw = input(f"{prompt}{default_str}: ").strip()
        if raw == "" and default is not None:
            return default
        if raw == "" and not allow_empty:
            if not required:
                return ""
            print(_c("  ⚠ Required field. Please enter a value.", "red"))
            continue
        return raw


def ask_choice(prompt: str, choices: list[str], default: Optional[str] = None) -> str:
    """Ask user to pick from a list of choices."""
    print(f"\n{_c(prompt, 'bold')}")
    for i, choice in enumerate(choices, 1):
        mark = "  "
        if default and choice == default:
            mark = f"{_c('* ', 'green')}"
        print(f"  {mark}{i}. {choice}")
    while True:
        default_hint = f" (default: {choices.index(default)+1})" if default else ""
        raw = input(f"  Select number{default_hint}: ").strip()
        if raw == "" and default is not None:
            return default
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(choices):
                return choices[idx]
        print(_c(f"  ⚠ Please enter a number between 1 and {len(choices)}", "red"))


def ask_int(prompt: str, lo: int, hi: int, default: Optional[int] = None) -> int:
    """Ask for an integer in [lo, hi]."""
    default_str = f" [{default}]" if default is not None else ""
    while True:
        raw = input(f"{prompt}{default_str}: ").strip()
        if raw == "" and default is not None:
            return default
        if raw.isdigit() or (raw.startswith("-") and raw[1:].isdigit()):
            val = int(raw)
            if lo <= val <= hi:
                return val
        print(_c(f"  ⚠ Please enter an integer between {lo} and {hi}", "red"))


def ask_bool(prompt: str, default: bool = False) -> bool:
    """Ask a yes/no question."""
    default_str = " [Y/n]" if default else " [y/N]"
    raw = input(f"{prompt}{default_str}: ").strip().lower()
    if raw == "":
        return default
    return raw in ("y", "yes", "true", "1")


def ask_multiline(prompt: str, required: bool = False) -> str:
    """Ask for multi-line input. Empty line to finish."""
    print(f"\n{_c(prompt, 'bold')} (enter blank line to finish)")
    lines = []
    while True:
        line = input("  > ")
        if line.strip() == "":
            break
        lines.append(line)
    result = "\n".join(lines).strip()
    if required and not result:
        print(_c("  ⚠ This field is required. Please enter at least one line.", "red"))
        return ask_multiline(prompt, required=True)
    return result


# ── File / registry helpers ────────────────────────────────────────────────
def ensure_dirs():
    for d in (
        BASELINES_DIR,
        SESSION_LOGS_DIR,
        POST_SESSIONS_DIR,
        SCREENSHOTS_DIR,
        CODED_DIR,
        WEEKLY_MEMOS_DIR,
        INSTRUMENTATION,
    ):
        d.mkdir(parents=True, exist_ok=True)


def load_registry() -> dict:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {"sessions": [], "next_session_number": 1, "study": "pilot_001"}


def save_registry(reg: dict):
    REGISTRY_PATH.write_text(json.dumps(reg, indent=2), encoding="utf-8")


def load_current_session() -> Optional[dict]:
    if CURRENT_SESSION_PATH.exists():
        return json.loads(CURRENT_SESSION_PATH.read_text(encoding="utf-8"))
    return None


def save_current_session(data: dict):
    CURRENT_SESSION_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def clear_current_session():
    if CURRENT_SESSION_PATH.exists():
        CURRENT_SESSION_PATH.unlink()


def get_last_session() -> Optional[dict]:
    reg = load_registry()
    if reg["sessions"]:
        return reg["sessions"][-1]
    return None


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%H:%M")


def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── Command: start (Pre-Session) ────────────────────────────────────────────
def cmd_start(args: argparse.Namespace):
    ensure_dirs()

    # Check for existing active session
    current = load_current_session()
    if current:
        print(
            _c(
                f"⚠ Session {current['session_id']} is already active (started {current['start_time']}).",
                "yellow",
            )
        )
        if not ask_bool("Start a new session anyway?", default=False):
            print("Aborting. Use 'crg_session.py status' to see details.")
            return

    reg = load_registry()
    session_num = reg["next_session_number"]
    date_str = today_str()
    start_time = now_str()
    session_id = f"pilot001-session-{session_num:03d}"

    print(_c("\n═══════════════════════════════════════════", "cyan"))
    print(_c("  CRG-ANL  —  Pre-Session Wizard", "cyan"))
    print(_c(f"  Session {session_num}  |  {date_str}  |  {start_time}", "cyan"))
    print(_c("═══════════════════════════════════════════\n", "cyan"))

    # ── Smart defaults from last session ──
    last = get_last_session()
    default_device = last.get("device") if last else None
    default_location = last.get("location") if last else None
    default_course = last.get("course") if last else None

    # ── Environment ──
    print(_c("─── Environment ───", "bold"))
    device = ask_choice("Device", ["mobile", "tablet", "desktop"], default=default_device)
    location = ask_choice(
        "Location", ["home", "commute", "work", "other"], default=default_location
    )
    distraction = ask_int("Distraction level (1=isolated, 5=constant interruptions)", 1, 5)
    time_available = ask_int("Time available for session (minutes)", 10, 180)
    network = ask_choice("Network", ["stable", "intermittent", "poor"])

    # ── Baseline State ──
    print(_c("\n─── Baseline State (1–7 scale) ───", "bold"))
    print(_c("  1 = low / negative  →  7 = high / positive", "dim"))
    energy = ask_int("Energy level", 1, 7)
    stress = ask_int("Stress level", 1, 7)
    prior_knowledge = ask_int("Prior knowledge (today's topic)", 1, 7)
    motivation = ask_int("Motivation", 1, 7)

    # ── Goals ──
    print(_c("\n─── Learning Goals (1–3 specific objectives) ───", "bold"))
    goals = []
    for i in range(1, 4):
        g = ask(f"Goal {i}", required=(i == 1), allow_empty=True)
        if g:
            goals.append(g)
        else:
            break

    # ── Session Plan ──
    print(_c("\n─── Session Plan ───", "bold"))
    course = ask("Course (e.g., ml-fundamentals)", default=default_course)
    lesson = ask("Lesson(s) (e.g., supervised-learning-basics)")

    # ── Build baseline file ──
    baseline_filename = f"baseline_{date_str}.md"
    baseline_path = BASELINES_DIR / baseline_filename

    baseline_content = f"""# Pre-Session Baseline — {date_str}

## Environment
- **Device:** {device}
- **Location:** {location}
- **Distraction level:** {distraction}
- **Time available:** {time_available} minutes
- **Network:** {network}

## Baseline State (1-7 scale)
- **Energy:** {energy}
- **Stress:** {stress}
- **Prior knowledge (today's topic):** {prior_knowledge}
- **Motivation:** {motivation}

## Goals (1-3 specific learning objectives)
"""
    for i, g in enumerate(goals, 1):
        baseline_content += f"{i}. {g}\n"
    baseline_content += f"""
## Session Plan
- **Course:** {course}
- **Lesson(s):** {lesson}
- **Planned start time:** {start_time}
- **Actual start time:** {start_time}
"""
    baseline_path.write_text(baseline_content, encoding="utf-8")
    print(_c(f"\n  ✓ Baseline saved: {baseline_path.relative_to(REPO_ROOT)}", "green"))

    # ── Build session log file ──
    log_filename = f"session_log_{date_str}_{start_time.replace(':', '')}.md"
    log_path = SESSION_LOGS_DIR / log_filename

    log_header = f"""# Session Log — {date_str}

## Start: {start_time}
## Device: {device}
## Location: {location}
## Goals: {', '.join(goals)}
## Course: {course}
## Lesson: {lesson}
## Session ID: {session_id}

---

"""
    log_path.write_text(log_header, encoding="utf-8")
    print(_c(f"  ✓ Session log created: {log_path.relative_to(REPO_ROOT)}", "green"))

    # ── Create screenshot directory ──
    screenshot_dir = SCREENSHOTS_DIR / date_str
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    print(_c(f"  ✓ Screenshot directory ready: {screenshot_dir.relative_to(REPO_ROOT)}", "green"))

    # ── Save current session state ──
    session_state = {
        "session_number": session_num,
        "session_id": session_id,
        "date": date_str,
        "start_time": start_time,
        "baseline_file": str(baseline_path.relative_to(REPO_ROOT)),
        "log_file": str(log_path.relative_to(REPO_ROOT)),
        "screenshot_dir": str(screenshot_dir.relative_to(REPO_ROOT)),
        "device": device,
        "location": location,
        "course": course,
        "lesson": lesson,
        "goals": goals,
        "events": [],
        "event_count": 0,
        "screenshot_count": 0,
    }
    save_current_session(session_state)

    # ── Update registry ──
    reg["next_session_number"] = session_num + 1
    reg["sessions"].append(
        {
            "session_number": session_num,
            "session_id": session_id,
            "date": date_str,
            "start_time": start_time,
            "device": device,
            "location": location,
            "course": course,
            "lesson": lesson,
            "goals": goals,
            "status": "active",
        }
    )
    save_registry(reg)

    print(_c("\n═══════════════════════════════════════════", "green"))
    print(_c("  Pre-Session complete. Begin learning!", "green"))
    print(_c("═══════════════════════════════════════════\n", "green"))
    print(_c("Quick commands during your session:", "bold"))
    print(f"  python crg_session.py event    -- log an event")
    print(f"  python crg_session.py end      -- end the session")
    print()

    # ── Open Quantic ──
    if ask_bool("Open Quantic platform in browser now?", default=True):
        cmd_open(args)


# ── Command: event (During Session) ─────────────────────────────────────────
def cmd_event(args: argparse.Namespace):
    current = load_current_session()
    if not current:
        print(_c("⚠ No active session. Run 'crg_session.py start' first.", "red"))
        return

    print(_c(f"\n─── Log Event for {current['session_id']} ───", "bold"))

    event_num = current["event_count"] + 1
    event_time = now_str()

    # Trigger selection
    print(_c("\nTrigger:", "bold"))
    trigger_choices = [f"{k}: {v}" for k, v in TRIGGERS.items()]
    trigger_raw = ask_choice("What triggered this observation?", trigger_choices)
    trigger_code = trigger_raw.split(":")[0]

    # Quick or full log?
    full = ask_bool("Full event log now? (yes=full, no=quick timestamp only)", default=False)

    if full:
        what_happened = ask_multiline("What happened?", required=True)
        context = ask_multiline("Context: What were you trying to do? Where in the course?")
        system_response = ask_multiline("System response: What did the AI or platform do?")
        reaction = ask_multiline("Your reaction: How did you feel? What did you think?")
    else:
        what_happened = "[TO BE FILLED IN POST-SESSION]"
        context = ""
        system_response = ""
        reaction = ""

    screenshot = ask_bool("Did you take a screenshot?")
    screenshot_desc = ""
    if screenshot:
        current["screenshot_count"] += 1
        screenshot_desc = ask("Screenshot description (for filename):")
        # Suggest filename
        sug_name = f"screenshot_{current['screenshot_count']:03d}_{screenshot_desc.lower().replace(' ', '_')[:40]}.png"
        print(_c(f"  Suggested filename: {sug_name}", "dim"))
        print(_c(f"  Save to: {current['screenshot_dir']}/", "dim"))

    # Micro-pulse (optional during session)
    micro = ask_bool("Capture micro-pulse ratings now?")
    micro_data = {}
    if micro:
        print(_c("\n  Micro-Pulse (1-5, 1=low/negative, 5=high/positive):", "bold"))
        micro_data["clarity"] = ask_int("    Clarity (I know what to do next)", 1, 5)
        micro_data["cognitive_load"] = ask_int("    Cognitive Load (mentally heavy)", 1, 5)
        micro_data["affect"] = ask_int("    Affect (frustrated→confident)", 1, 5)
        micro_data["perceived_control"] = ask_int("    Perceived Control", 1, 5)
        micro_data["trust"] = ask_int("    Trust (I trust the guidance)", 1, 5)

    # Build event entry
    event_entry = f"""
### Event {event_num} — {event_time}

**What happened:**
{what_happened}

"""
    if context:
        event_entry += f"**Context:**\n{context}\n\n"
    if system_response:
        event_entry += f"**System response:**\n{system_response}\n\n"
    if reaction:
        event_entry += f"**My reaction:**\n{reaction}\n\n"

    event_entry += f"**Trigger:** {trigger_code}\n"
    event_entry += f"**Screenshot:** {'Y' if screenshot else 'N'}"
    if screenshot and screenshot_desc:
        event_entry += f" — {screenshot_desc}"
    event_entry += "\n"

    if micro_data:
        event_entry += f"**Micro-pulse:** clarity={micro_data.get('clarity')}, load={micro_data.get('cognitive_load')}, affect={micro_data.get('affect')}, control={micro_data.get('perceived_control')}, trust={micro_data.get('trust')}\n"

    event_entry += "\n---\n"

    # Append to log
    log_path = REPO_ROOT / current["log_file"]
    with log_path.open("a", encoding="utf-8") as f:
        f.write(event_entry)

    # Update session state
    current["event_count"] = event_num
    current["events"].append(
        {
            "number": event_num,
            "time": event_time,
            "trigger": trigger_code,
            "screenshot": screenshot,
            "micro_pulse": micro_data,
        }
    )
    save_current_session(current)

    print(_c(f"\n  ✓ Event {event_num} logged at {event_time}", "green"))
    if not full:
        print(_c("  ⚠ Remember to fill in details during post-session!", "yellow"))


# ── Command: end ────────────────────────────────────────────────────────────
def cmd_end(args: argparse.Namespace):
    current = load_current_session()
    if not current:
        print(_c("⚠ No active session. Run 'crg_session.py start' first.", "red"))
        return

    end_time = now_str()
    current["end_time"] = end_time
    save_current_session(current)

    # Parse start time to compute duration
    try:
        start_dt = datetime.strptime(f"{current['date']} {current['start_time']}", "%Y-%m-%d %H:%M")
        end_dt = datetime.strptime(f"{current['date']} {end_time}", "%Y-%m-%d %H:%M")
        if end_dt < start_dt:
            end_dt = datetime.strptime(f"{current['date']} {end_time}", "%Y-%m-%d %H:%M")
        duration_min = int((end_dt - start_dt).total_seconds() / 60)
    except Exception:
        duration_min = ask_int("Total session duration (minutes)", 1, 300)

    # Append to log
    log_path = REPO_ROOT / current["log_file"]
    footer = f"""
## End: {end_time}
## Total duration: {duration_min} minutes
## Events logged: {current['event_count']}
## Session complete: Y
"""
    with log_path.open("a", encoding="utf-8") as f:
        f.write(footer)

    print(_c(f"\n  ✓ Session ended at {end_time} ({duration_min} minutes)", "green"))
    print(_c(f"  ✓ {current['event_count']} event(s) logged", "green"))

    # Update registry
    reg = load_registry()
    for s in reg["sessions"]:
        if s["session_id"] == current["session_id"]:
            s["status"] = "completed"
            s["end_time"] = end_time
            s["duration_minutes"] = duration_min
            s["event_count"] = current["event_count"]
            break
    save_registry(reg)

    print(_c("\nNext: Run 'crg_session.py post' to complete post-session instruments.", "cyan"))


# ── Command: post (Post-Session) ────────────────────────────────────────────
def cmd_post(args: argparse.Namespace):
    current = load_current_session()
    if not current:
        print(_c("⚠ No active session found. Run 'crg_session.py start' first.", "red"))
        return

    date_str = current["date"]

    print(_c("\n═══════════════════════════════════════════", "magenta"))
    print(_c("  Post-Session Wizard", "magenta"))
    print(_c(f"  {current['session_id']}  |  {date_str}", "magenta"))
    print(_c("═══════════════════════════════════════════\n", "magenta"))

    # ── NASA-TLX ──
    print(_c("─── NASA-TLX (0–100) ───", "bold"))
    print(_c("  0 = lowest / best  →  100 = highest / worst (except Performance: 0=perfect, 100=failure)", "dim"))
    tlx = {
        "Mental Demand": ask_int("Mental Demand", 0, 100),
        "Physical Demand": ask_int("Physical Demand", 0, 100),
        "Temporal Demand": ask_int("Temporal Demand", 0, 100),
        "Performance": ask_int("Performance (0=perfect, 100=failure)", 0, 100),
        "Effort": ask_int("Effort", 0, 100),
        "Frustration": ask_int("Frustration", 0, 100),
    }

    # ── Subjective Scales ──
    print(_c("\n─── Subjective Scales (1–7) ───", "bold"))
    print(_c("  1 = strongly disagree / negative  →  7 = strongly agree / positive", "dim"))
    scales = {
        "S1": ("I knew what I was supposed to be learning", ask_int("S1", 1, 7)),
        "S2": ("Content was at right difficulty (4=just right)", ask_int("S2", 1, 7)),
        "S3": ("I felt overwhelmed", ask_int("S3", 1, 7)),
        "S4": ("I trust AI tutor explanations", ask_int("S4", 1, 7)),
        "S5": ("I had control over learning path", ask_int("S5", 1, 7)),
        "S6": ("I felt anxious/stressed", ask_int("S6", 1, 7)),
        "S7": ("Feedback was helpful", ask_int("S7", 1, 7)),
        "S8": ("I felt confident", ask_int("S8", 1, 7)),
        "S9": ("Transitions were smooth", ask_int("S9", 1, 7)),
        "S10": ("I understood system suggestions", ask_int("S10", 1, 7)),
        "S11": ("I felt safe making mistakes", ask_int("S11", 1, 7)),
        "S12": ("Good use of my time", ask_int("S12", 1, 7)),
        "S13": ("Would recommend", ask_int("S13", 1, 7)),
        "S14": ("Sense of progress", ask_int("S14", 1, 7)),
    }

    # ── Research Notes ──
    print(_c("\n─── Research Notes ───", "bold"))
    confusion = ask_multiline("Top confusion moments (if any)")
    momentum = ask_multiline("Where did you feel momentum? Where friction?")
    support = ask_multiline("What support helped most? What was missing?")
    safety = ask_multiline("Any anxiety, frustration, or safety moments?")
    surprises = ask_multiline("Anything unexpected?")

    # ── Build post-session file ──
    post_filename = f"post_session_{date_str}.md"
    post_path = POST_SESSIONS_DIR / post_filename

    post_content = f"""# Post-Session — {date_str}
## Session: {current['session_id']}

## NASA-TLX (0-100)
| Dimension | Your Rating |
|-----------|-------------|
| Mental Demand | {tlx['Mental Demand']} |
| Physical Demand | {tlx['Physical Demand']} |
| Temporal Demand | {tlx['Temporal Demand']} |
| Performance | {tlx['Performance']} |
| Effort | {tlx['Effort']} |
| Frustration | {tlx['Frustration']} |

## Subjective Scales (1-7)
| # | Statement | Rating |
|---|-----------|--------|
"""
    for code, (statement, rating) in scales.items():
        post_content += f"| {code} | {statement} | {rating} |\n"

    post_content += f"""
## Research Notes

### Top confusion moments (if any)
{confusion or "_None noted_"}

### Where did you feel momentum? Where friction?
Momentum/Flow: {momentum or "_"}

### What support helped most? What was missing?
{support or "_"}

### Any anxiety, frustration, or safety moments?
{safety or "_None noted_"}

### Anything unexpected?
{surprises or "_None noted_"}

## Observations to Code
"""
    for ev in current.get("events", []):
        post_content += f"- [ ] Event {ev['number']} — {ev['trigger']}\n"
    post_content += f"\nTotal: {current['event_count']} observations to code\n"

    post_path.write_text(post_content, encoding="utf-8")
    print(_c(f"\n  ✓ Post-session form saved: {post_path.relative_to(REPO_ROOT)}", "green"))

    # Save to current session for YAML generation
    current["post_session_file"] = str(post_path.relative_to(REPO_ROOT))
    current["tlx"] = tlx
    current["scales"] = {k: v[1] for k, v in scales.items()}
    save_current_session(current)

    print(_c("\n═══════════════════════════════════════════", "green"))
    print(_c("  Post-Session complete!", "green"))
    print(_c("═══════════════════════════════════════════\n", "green"))

    if current["event_count"] > 0:
        print(_c(f"Next: Create {current['event_count']} observation YAML file(s):", "cyan"))
        print(f"  python crg_session.py code")
    else:
        print(_c("No events to code. Ready to commit:", "cyan"))
        print(f"  python crg_session.py commit")


# ── Command: code (Observation YAML) ────────────────────────────────────────
def cmd_code(args: argparse.Namespace):
    current = load_current_session()
    if not current:
        print(_c("⚠ No active session found. Run 'crg_session.py start' first.", "red"))
        return

    events = current.get("events", [])
    if not events:
        print(_c("⚠ No events logged in this session. Nothing to code.", "yellow"))
        return

    # Show uncoded events
    print(_c(f"\n─── Events to Code ({len(events)} total) ───", "bold"))
    for ev in events:
        print(f"  Event {ev['number']}: {ev['time']} — {TRIGGERS.get(ev['trigger'], ev['trigger'])}")

    # Pick event or auto-pick next uncoded
    coded_files = list(CODED_DIR.glob(f"obs_{current['date'].replace('-', '')}_*.yaml"))
    coded_nums = set()
    for f in coded_files:
        m = re.search(rf"obs_{current['date'].replace('-', '')}_(\d{{3}})_", f.name)
        if m:
            coded_nums.add(int(m.group(1)))

    uncoded = [ev for ev in events if ev["number"] not in coded_nums]

    if not uncoded:
        print(_c("\n  ✓ All events have been coded!", "green"))
        print(_c("  Run 'crg_session.py commit' to finalize.", "cyan"))
        return

    if len(uncoded) == 1:
        ev = uncoded[0]
        print(_c(f"\n  → Coding Event {ev['number']} (last uncoded event)", "cyan"))
    else:
        print(_c(f"\n  {len(uncoded)} event(s) still uncoded.", "yellow"))
        choice = ask_int("Which event number to code?", 1, len(events))
        ev = next((e for e in events if e["number"] == choice), None)
        if not ev:
            print(_c("  ⚠ Invalid event number.", "red"))
            return

    print(_c(f"\n═══════════════════════════════════════════", "cyan"))
    print(_c(f"  Coding Event {ev['number']}", "cyan"))
    print(_c(f"  {ev['time']} — {TRIGGERS.get(ev['trigger'], ev['trigger'])}", "cyan"))
    print(_c("═══════════════════════════════════════════\n", "cyan"))

    # ── Wizard ──
    print(_c("─── Observation Details ───", "bold"))

    # Observation type
    obs_type = ask_choice("Observation type", OBSERVATION_TYPES)

    # Description
    print(_c("\nDescription: 2-4 sentences about what happened.", "bold"))
    print(_c("  Be specific enough to understand in 6 months.", "dim"))
    description = ask_multiline("Description", required=True)

    # Constructs
    print(_c("\n─── Constructs ───", "bold"))
    construct_choices = [f"{k}: {v}" for k, v in CONSTRUCTS.items()]
    primary_raw = ask_choice("Primary construct", construct_choices)
    primary = primary_raw.split(":")[0]

    secondary = []
    if ask_bool("Add secondary construct(s)?"):
        while True:
            sec_raw = ask_choice("Secondary construct (or 'done')", construct_choices + ["done"])
            if sec_raw == "done":
                break
            sec = sec_raw.split(":")[0]
            if sec != primary:
                secondary.append(sec)

    # Severity & confidence
    severity = ask_int("Severity (1=minor, 5=critical)", 1, 5)
    observer_confidence = ask_int("Your confidence in this coding (1=guess, 5=certain)", 1, 5)

    # Dimensional fields
    print(_c("\n─── Dimensional Coding ───", "bold"))
    ii_dim = ask_choice("Instructional Integrity dimension", II_DIMENSIONS)
    cs_impact = ask_choice("Cognitive Safety impact", CS_IMPACTS)
    agency = ask_choice("Human agency effect", AGENCY_STATES)
    shared = ask_choice("Shared responsibility assessment", SHARED_RESP)

    # Micro-pulse (use session data if available, else ask)
    micro = ev.get("micro_pulse", {})
    if not micro and ask_bool("Capture micro-pulse ratings now?"):
        micro["clarity"] = ask_int("Clarity (1-5)", 1, 5)
        micro["cognitive_load"] = ask_int("Cognitive Load (1-5)", 1, 5)
        micro["affect"] = ask_int("Affect (1-5)", 1, 5)
        micro["perceived_control"] = ask_int("Perceived Control (1-5)", 1, 5)
        micro["trust"] = ask_int("Trust (1-5)", 1, 5)

    # Outcome
    outcome = ask_choice("Immediate outcome", OUTCOMES)
    clarity = ask_int("Perceived clarity of the event (1-7)", 1, 7)

    # Research memo
    print(_c("\n─── Analysis ───", "bold"))
    research_memo = ask_multiline("Research memo: analytical thoughts, patterns, questions")
    intervention = ask_multiline("Candidate intervention: what would have improved this?")

    # Supporting evidence
    evidence = []
    if ev.get("screenshot"):
        if ask_bool("Link to a screenshot file?"):
            screenshot_files = list((REPO_ROOT / current["screenshot_dir"]).glob("*.png"))
            if screenshot_files:
                screenshot_names = [f.name for f in screenshot_files]
                chosen = ask_choice("Select screenshot", screenshot_names)
                evidence.append(
                    {
                        "type": "screenshot",
                        "file": f"{current['screenshot_dir']}/{chosen}",
                        "description": ask("What does this evidence show?"),
                    }
                )

    evidence.append(
        {
            "type": "session_log",
            "file": current["log_file"],
            "description": f"Real-time log entry at Event {ev['number']}",
        }
    )

    # Build YAML
    seq_num = ev["number"]
    date_compact = current["date"].replace("-", "")
    obs_id = f"obs-{date_compact}-{seq_num:03d}"
    filename = f"obs_{date_compact}_{seq_num:03d}_{primary}.yaml"
    filepath = CODED_DIR / filename

    yaml_content = f"""observation_id: "{obs_id}"
study: "pilot_001"
session_id: "{current['session_id']}"
timestamp: "{current['date']}T{ev['time']}:00Z"

observer:
  role: "researcher"
  experience_level: "intermediate"

context:
  course: "{current['course']}"
  lesson: "{current['lesson']}"
  device: "{current['device']}"
  environment: "{current['location']}"
  session_duration_minutes: {current.get('duration_minutes', '[FILL]')}
  interaction_count: {current['event_count']}

observation_type: "{obs_type}"
description: >
{indent_lines(description, 2)}

constructs_involved:
  primary: "{primary}"
  secondary: {format_list(secondary)}
  taxonomy_codes: []

instructional_integrity_dimension: "{ii_dim}"
cognitive_safety_impact: "{cs_impact}"
human_agency: "{agency}"
shared_responsibility: "{shared}"
severity: {severity}
"""

    if micro:
        yaml_content += f"""
sx_micro_pulse:
  clarity: {micro.get('clarity', '')}
  cognitive_load: {micro.get('cognitive_load', '')}
  affect: {micro.get('affect', '')}
  perceived_control: {micro.get('perceived_control', '')}
  trust: {micro.get('trust', '')}
"""

    yaml_content += f"""
immediate_outcome: "{outcome}"
perceived_clarity: {clarity}
observer_confidence: {observer_confidence}

supporting_evidence:
"""
    for evi in evidence:
        yaml_content += f"""  - type: "{evi['type']}"
    file: "{evi['file']}"
    description: "{evi['description']}"
"""

    if research_memo:
        yaml_content += f"""
research_memo: >
{indent_lines(research_memo, 2)}
"""

    if intervention:
        yaml_content += f"""
candidate_intervention: >
{indent_lines(intervention, 2)}
"""

    yaml_content += f"""
future_benchmark_mapping:
  dimension: "{CONSTRUCTS.get(primary, primary)}"
  sub_dimension: "{ii_dim if ii_dim != 'not_applicable' else ''}"
  severity: {severity}

privacy:
  contains_pii: false
  consent_basis: "self_consent"
  retention_class: "research_permanent"

metadata:
  created_at: "{iso_now()}"
  schema_version: "0.1.0"
"""

    filepath.write_text(yaml_content, encoding="utf-8")
    print(_c(f"\n  ✓ Observation saved: {filepath.relative_to(REPO_ROOT)}", "green"))

    # Check if more to code
    coded_files = list(CODED_DIR.glob(f"obs_{date_compact}_*.yaml"))
    coded_nums = set()
    for f in coded_files:
        m = re.search(rf"obs_{date_compact}_(\d{{3}})_", f.name)
        if m:
            coded_nums.add(int(m.group(1)))

    remaining = len([e for e in events if e["number"] not in coded_nums])
    if remaining > 0:
        print(_c(f"  {remaining} observation(s) still to code.", "yellow"))
        if ask_bool("Code another now?"):
            cmd_code(args)
    else:
        print(_c("\n  ✓ All observations coded!", "green"))
        print(_c("  Run 'crg_session.py commit' to finalize.", "cyan"))


def indent_lines(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line for line in text.splitlines())


def format_list(items: list[str]) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(f'"{x}"' for x in items) + "]"


# ── Command: commit ─────────────────────────────────────────────────────────
def cmd_commit(args: argparse.Namespace):
    current = load_current_session()
    if not current:
        print(_c("⚠ No active session. Nothing to commit.", "red"))
        return

    # Check if session is ended
    if "end_time" not in current:
        print(_c("⚠ Session not ended yet. Run 'crg_session.py end' first.", "yellow"))
        if not ask_bool("Commit anyway?"):
            return

    date_str = current["date"]
    session_id = current["session_id"]
    event_count = current["event_count"]
    course = current.get("course", "unknown")
    lesson = current.get("lesson", "unknown")

    # Count coded observations
    date_compact = date_str.replace("-", "")
    coded_files = list(CODED_DIR.glob(f"obs_{date_compact}_*.yaml"))
    coded_count = len(coded_files)

    # Count screenshots
    screenshot_dir = REPO_ROOT / current.get("screenshot_dir", ".")
    screenshot_count = len(list(screenshot_dir.glob("*.png"))) if screenshot_dir.exists() else 0

    commit_msg = f"""pilot001: {session_id} — {event_count} observations from {course}/{lesson}

- Baseline, session log, post-session form
- {coded_count} coded observations
- {screenshot_count} screenshots"""

    print(_c("\n─── Git Commit ───", "bold"))
    print(_c("Commit message preview:", "dim"))
    print("─" * 50)
    print(commit_msg)
    print("─" * 50)

    if ask_bool("Proceed with commit?", default=True):
        try:
            subprocess.run(
                ["git", "add", "03_evidence/"],
                cwd=REPO_ROOT,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "commit", "-m", commit_msg],
                cwd=REPO_ROOT,
                check=True,
                capture_output=True,
            )
            print(_c("\n  ✓ Committed successfully.", "green"))
            clear_current_session()
            print(_c("  Session state cleared. Ready for next session!\n", "green"))
        except subprocess.CalledProcessError as e:
            print(_c(f"\n  ✗ Git error: {e}", "red"))
            print(_c("  You may need to commit manually.", "yellow"))
    else:
        print("Commit aborted. You can commit manually when ready.")


# ── Command: week (Weekly Memo) ─────────────────────────────────────────────
def cmd_week(args: argparse.Namespace):
    ensure_dirs()
    reg = load_registry()

    if not reg["sessions"]:
        print(_c("⚠ No sessions recorded yet.", "yellow"))
        return

    # Determine week boundaries
    today = datetime.now(timezone.utc)
    # Find Monday of current week
    monday = today - __import__("datetime").timedelta(days=today.weekday())
    sunday = monday + __import__("datetime").timedelta(days=6)
    week_start = monday.strftime("%Y-%m-%d")
    week_end = sunday.strftime("%Y-%m-%d")

    # Find sessions in this week
    week_sessions = [
        s for s in reg["sessions"]
        if week_start <= s.get("date", "") <= week_end
    ]

    if not week_sessions:
        print(_c(f"⚠ No sessions found for week of {week_start} to {week_end}.", "yellow"))
        return

    # Compute aggregates
    total_obs = sum(s.get("event_count", 0) for s in week_sessions)
    total_duration = sum(s.get("duration_minutes", 0) for s in week_sessions)

    # Determine week number
    week_num = (week_sessions[0]["session_number"] - 1) // 5 + 1  # rough estimate

    print(_c(f"\n─── Weekly Memo Wizard (Week {week_num}) ───", "bold"))
    print(_c(f"  {week_start} to {week_end}", "dim"))
    print(_c(f"  {len(week_sessions)} session(s), {total_obs} observations, {total_duration} minutes\n", "dim"))

    patterns = ask_multiline("Patterns observed (anything that happened more than once?)")
    surprises = ask_multiline("Surprises")
    protocol_issues = ask_multiline("Protocol issues (any problems with the process?)")
    construct_reflections = ask_multiline("Construct reflections (do the constructs still fit?)")
    taxonomy_stress = ask_multiline("Taxonomy stress (observations that were hard to code?)")
    next_week = ask_multiline("Next week focus")
    decisions = ask_multiline("Decisions (any changes made or needed?)")

    # Build memo
    memo_filename = f"memo_week_{week_num:02d}_{week_end}.md"
    memo_path = WEEKLY_MEMOS_DIR / memo_filename

    memo_content = f"""# Weekly Memo — Week {week_num:02d} ({week_start} to {week_end})

## Sessions This Week
- {len(week_sessions)} sessions
- Total observations: {total_obs}
- Total session time: {total_duration} minutes

### Session Details
"""
    for s in week_sessions:
        memo_content += f"- **{s['session_id']}** ({s['date']}): {s.get('course', '?')}/{s.get('lesson', '?')} — {s.get('event_count', 0)} observations, {s.get('duration_minutes', '?')} min\n"

    memo_content += f"""
## Patterns Observed
{patterns or "_None noted_"}

## Surprises
{surprises or "_None noted_"}

## Protocol Issues
{protocol_issues or "_None noted_"}

## Construct Reflections
{construct_reflections or "_None noted_"}

## Taxonomy Stress
{taxonomy_stress or "_None noted_"}

## Next Week Focus
{next_week or "_"}

## Decisions
{decisions or "_None noted_"}
"""

    memo_path.write_text(memo_content, encoding="utf-8")
    print(_c(f"\n  ✓ Weekly memo saved: {memo_path.relative_to(REPO_ROOT)}", "green"))


# ── Command: status ─────────────────────────────────────────────────────────
def cmd_status(args: argparse.Namespace):
    current = load_current_session()
    reg = load_registry()

    print(_c("\n═══════════════════════════════════════════", "blue"))
    print(_c("  CRG-ANL Session Status", "blue"))
    print(_c("═══════════════════════════════════════════\n", "blue"))

    if current:
        print(_c("─── Active Session ───", "bold"))
        print(f"  Session ID:  {current['session_id']}")
        print(f"  Date:        {current['date']}")
        print(f"  Started:     {current['start_time']}")
        if "end_time" in current:
            print(f"  Ended:       {current['end_time']}")
            print(f"  Status:      {_c('POST-SESSION', 'yellow')}")
        else:
            print(f"  Status:      {_c('ACTIVE', 'green')}")
        print(f"  Events:      {current['event_count']}")
        print(f"  Course:      {current.get('course', 'N/A')}")
        print(f"  Lesson:      {current.get('lesson', 'N/A')}")
        print(f"  Log file:    {current.get('log_file', 'N/A')}")

        # Checklist
        print(_c("\n─── Completion Checklist ───", "bold"))
        checks = [
            ("Baseline file", current.get("baseline_file") and (REPO_ROOT / current["baseline_file"]).exists()),
            ("Session log", current.get("log_file") and (REPO_ROOT / current["log_file"]).exists()),
            ("Session ended", "end_time" in current),
            ("Post-session form", current.get("post_session_file") and (REPO_ROOT / current["post_session_file"]).exists() if current.get("post_session_file") else False),
        ]
        date_compact = current["date"].replace("-", "")
        coded_count = len(list(CODED_DIR.glob(f"obs_{date_compact}_*.yaml")))
        checks.append((f"Coded observations ({coded_count}/{current['event_count']})", coded_count >= current["event_count"] and current["event_count"] > 0))

        for label, done in checks:
            mark = _c("✓", "green") if done else _c("○", "dim")
            print(f"  {mark} {label}")
    else:
        print(_c("No active session.", "dim"))

    print(_c(f"\n─── Registry ───", "bold"))
    print(f"  Total sessions: {len(reg['sessions'])}")
    print(f"  Next session #: {reg['next_session_number']}")
    if reg["sessions"]:
        last = reg["sessions"][-1]
        sid = last.get("session_id", "unknown")
        date = last.get("date", "unknown")
        status = last.get("status", "unknown")
        print(f"  Last session:   {sid} ({date}) — {status}")

    print()


# ── Command: open ───────────────────────────────────────────────────────────
def cmd_open(args: argparse.Namespace):
    print(_c("Opening Quantic platform...", "cyan"))
    webbrowser.open("https://quantic.edu")


# ── Main ────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="CRG-ANL Session Manager — automate your researcher-as-subject workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
commands:
  start   Begin a new session (pre-session wizard)
  event   Log an event during an active session
  end     End the current session
  post    Complete post-session instruments
  code    Create a coded observation YAML
  commit  Git commit all evidence
  week    Generate weekly memo
  status  Show current session state
  open    Open Quantic platform in browser

example workflow:
  python crg_session.py start
  # ... study on Quantic ...
  python crg_session.py event
  # ... more studying ...
  python crg_session.py end
  python crg_session.py post
  python crg_session.py code
  python crg_session.py commit
        """,
    )
    parser.add_argument("command", choices=[
        "start", "event", "end", "post", "code", "commit", "week", "status", "open",
    ])
    parser.add_argument("--study", default="pilot_001", help="Study identifier")

    args = parser.parse_args()

    commands = {
        "start": cmd_start,
        "event": cmd_event,
        "end": cmd_end,
        "post": cmd_post,
        "code": cmd_code,
        "commit": cmd_commit,
        "week": cmd_week,
        "status": cmd_status,
        "open": cmd_open,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
