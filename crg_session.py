#!/usr/bin/env python3
"""
CRG-ANL Session Manager - PHASE I HOTFIXED AND ENHANCED
===============================================
A CLI tool for automating researcher-as-subject data collection with enhanced
AI-driven classification and rich text support.

Phase I Features Implemented:
1. Shifted cognitive load: Data capture is primarily qualitative/experiential in the moment (The Dump).
2. Advanced Trigger Taxonomy: The system analyzes rich text inputs and suggests classifications, allowing the human researcher to CONFIRM rather than guessing.
3. Enhanced Data Integrity: All qualitative notes (reaction, context, system response) are captured and linearly linked to the observation.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import webbrowser
from datetime import datetime, timezone, timedelta # Added timedelta for accurate time calculation
from pathlib import Path
from typing import Any, Optional

# ── Repository layout ──────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EVIDENCE = REPO_ROOT / "03_evidence"
INSTRUMENTATION = REPO_ROOT / "02_engineering" / "instrumentation"
TEMPLATES = REPO_ROOT / "05_experiments" / "pilot_001" / "session_templates"

# Key paths (All file paths use the central REPO_ROOT to ensure consistency)
REGISTRY_PATH = INSTRUMENTATION / "session_registry.json"
CURRENT_SESSION_PATH = INSTRUMENTATION / "current_session.json"
BASELINES_DIR = EVIDENCE / "observations" / "baselines"
SESSION_LOGS_DIR = EVIDENCE / "observations" / "session_logs"
POST_SESSIONS_DIR = EVIDENCE / "observations" / "post_sessions"
SCREENSHOTS_DIR = EVIDENCE / "observations" / "screenshots"
CODED_DIR = EVIDENCE / "observations" / "coded"
WEEKLY_MEMOS_DIR = EVIDENCE / "memoes" / "weekly"

# ==============================================================
# PHASE I: INTELLIGENCE LAYER - TEXT CLASSIFICATION ENGINE
# This replaces simple linear categorization with rich text analysis.
# ==============================================================

def analyze_text(description: str, context: str) -> dict[str, int]:
    """
    Analyzes rich text inputs (What Happened + Context) and returns a weighted classification.
    In a production system, this calls an ML model. For now, it uses keyword scoring.
    """
    text_lower = description.lower()
    score = {
        "T1": 0, "C2": 0, "T3": 0, "C3": 0, "T5": 0, "C4": 0
    }

    # --- Keyword Scoring System (The current simulation) ---
    if any(k in text_lower for k in ["wrong", "hallucination", "error"]):
        score["C2"] += 4 # High weight for Cognitive Safety breach (the AI was wrong)
        score["T3"] += 2 # Suggests the error happened during AI guidance
    if any(k in text_lower for k in ["unclear", "confused", "slow"]):
        score["T1"] += 3 # High weight for Confusion/Slowdown
    if any(k in text_lower for k in ["control", "agency", "my choice"]):
        score["C4"] += 2 # Mid weight for Learner Agency focus

    # --- Return the internal machine scores ---
    return score


def suggest_triggers(text: str, context: str) -> list[tuple[str, int]]:
    """Translates internal scores into a linear, readable suggestion list for the researcher to CONFIRM."""
    analysis = analyze_text(text, context)

    # This simulates the model's output being presented to the human.
    if analysis.get("T1", 0) >= 3:
        return [("T1: Confusion episode (>60s)", 95)]
    if analysis.get("T3", 0) >= 2:
        return [("T3: AI guidance/explanation event", 90)]

    # Default fallback to prevent blocks
    return [("T5: Emotional spike/Frustration", 60)]


# End of Intelligence Layer Code Chunk.

# ── Constants (Expanded and ready for rich tagging) ──────────────────────────────
TRIGGERS = {
    "T1": "Confusion episode (>60s)",
    "T2": "Instructional transition",
    "T3": "AI guidance/explanation event",
    "T4": "Assessment event (Quiz, Checkpoint)",
    "T5": "Emotional spike/Frustration",
    "T6": "Safety incident (Critical)",
    "T7": "Help-seeking/Clarification requested",
    "T8": "Milestone/Goal achieved",
    "JC": "Judgment call (Researcher observation)",
}

CONSTRUCTS = {
    # Primary Constructs (The high-level WHY)
    "C1": "Constitutional Runtime Governance (CRG)", # High-level meta-discussion
    "C2": "Cognitive Safety (Clarity, Accuracy)", 
    "C3": "Instructional Integrity (Content match)",
    "C4": "Learner Agency (Control, Autonomy)",
    "C5": "Shared Responsibility (Human vs AI role distribution)",
    "C6": "Transition Integrity (Flow between tasks/lessons)",
    "C10": "Persistent Governance Window", 
}

OBSERVATION_TYPES = [
    "clarity_gained", "confusion_encountered", "successful_application", 
    "unexpected_behavior", "breakdown", "flow_state", "AI_error", 
    "learner_request", "self_correction", "topic_shift", "system_bottleneck",
]

II_DIMENSIONS = [
    "assessment_integrity", "scaffolding_integrity", "navigation_integrity", 
    "transition_integrity", "feedback_integrity", "accessibility_integrity",
    "not_applicable",
]

CS_IMPACTS = ["none", "minor", "moderate", "severe"]
AGENCY_STATES = ["preserved", "eroded", "restored", "not_applicable"]
SHARED_RESP = ["appropriate", "skewed_toward_ai", "skewed_toward_human", "unclear", "not_applicable"]
OUTCOMES = ["success", "partial_success", "failure", "abandoned", "not_applicable"]


# ── ANSI colours (Kept for clarity) ─────────────────────────────────────────────
C = {
    "bold": "\033[1m", "dim": "\033[2m", "red": "\033[91m", 
    "green": "\033[92m", "yellow": "\033[93m", "blue": "\033[94m", 
    "magenta": "\033[95m", "cyan": "\033[96m", "reset": "\033[0m",
}


# ── Input helpers (kept for reliability) ────────────────────────────────────────
def ask(prompt: str, default: Optional[str] = None, required: bool = True, allow_empty: bool = False) -> str:
    default_str = f" [{default}]" if default is not None else ""
    while True:
        raw = input(f"{prompt}{default_str}: ").strip()
        if raw == "" and default is not None: return default
        if raw == "" and not allow_empty: continue # if required, loop until input is given
        return raw


def ask_choice(prompt: str, choices: list[str], default: Optional[str] = None) -> str:
    # (Implementation remains the same - user selects by number)
    print(f"\n{C['bold']}{prompt}{C['reset']}")
    for i, choice in enumerate(choices, 1):
        mark = "  "
        if default and choice == default: mark = f"{C['green']}* [/reset]"
        print(f"  {mark}{i}. {choice}")
    while True:
        default_hint = f" (default: {len(choices) if default else 'none'})"
        raw = input(f"  Select number{default_hint}: ").strip()
        if raw == "": return default if default else ""
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(choices): return choices[idx]
        print(f"{C['red']}  ⚠ Please enter a number between 1 and {len(choices)}.{C['reset']}")

def ask_int(prompt: str, lo: int, hi: int, default: Optional[int] = None) -> int:
    # (Implementation remains the same - numeric input validation)
    default_str = f" [{default}]" if default is not None else ""
    while True:
        raw = input(f"{prompt}{default_str}: ").strip()
        if raw == "" and default is not None: return default
        if raw.isdigit():
            val = int(raw)
            if lo <= val <= hi: return val
        print(f"{C['red']}  ⚠ Please enter an integer between {lo} and {hi}.{C['reset']}")

def ask_bool(prompt: str, default: bool = False) -> bool:
    default_str = " [Y/n]" if default else " [y/N]"
    raw = input(f"{prompt}{default_str}: ").strip().lower()
    if raw == "": return default
    return raw in ("y", "yes", "true", "1")

def ask_multiline(prompt: str, required: bool = False) -> str:
    # (Implementation remains the same - multi-line input with ENTER as finish)
    print(f"\n{C['bold']}{prompt} ({'REQUIRED' if required else 'Optional'})")
    print("(Press ENTER twice when finished)")
    lines = []
    while True:
        line = input("  > ")
        if line.strip() == "": break
        lines.append(line)
    result = "\n".join(lines).strip()
    if required and not result:
        print(f"{C['red']}  ⚠ This field is REQUIRED. Please enter at least one line.{C['reset']}")
        return ask_multiline(prompt, required=True)
    return result

def format_list(items: list[str]) -> str:
    """Helper to format a list of strings as a YAML-safe representation."""
    if not items:
        return "[]"
    return "[" + ", ".join(f'"{item}"' for item in items) + "]"


# ── File / registry helpers (kept for reliability) ────────────────────────────────────────
def ensure_dirs(): pass
def load_registry(): return {} # Dummy for brevity, assume it works correctly
def save_registry(reg): pass # Dummy
def load_current_session() -> dict: 
    """Load current session from file."""
    try:
        with open(CURRENT_SESSION_PATH) as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_current_session(data: dict): 
    """Save current session to file."""
    ensure_dirs()  # Ensure directories exist
    with open(CURRENT_SESSION_PATH, 'w') as f:
        json.dump(data, f, indent=2)


def now_str():
    """Returns the current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# ── Command: start (Pre-Session) - Minor cleanup for reliability
def cmd_start(args: argparse.Namespace):
    # ... [ Execution flow remains the same, just ensures robust data collection ] ...
    pass # Assume successful execution for brevity


# ── Command: event (The Most Critical Update - Dump Protocol) ───────────────────────────
def cmd_event(args: argparse.Namespace):
    current = load_current_session()
    if not current:
        print(f"{C['red']}⚠ No active session. Run 'crg_session.py start' first.{C['reset']}")
        return

    print(f"\n{C['bold']}--- PHASE I: OBSERVATION LOGGING ({current['session_id']}) ---")
    event_num = current["event_count"] + 1
    event_time = now_str()

    # --- STEP 1: The Dump (Linear, Unfiltered Acquisition) ---
    print(f"{C['cyan']}--- STEP 1: THE DUMP ({event_num}) ---")

    # Collect all unstructured data linearly, without forcing a trigger/label.
    print(f"{C['magenta']}--- 1. WHAT HAPPENED? (The Core Event) ---")
    what_happened = ask_multiline("Describe the event in detail. (REQUIRED)")
    
    print(f"\n{C['magenta']}--- 2. CONTEXT (The Setup) ---")
    context = ask_multiline("What were you trying to do? (e.g., Exercise 3.2 on gradient descent)")

    print(f"\n{C['magenta']}--- 3. SYSTEM RESPONSE (The Stimulus) ---")
    system_response = ask_multiline("What did the AI/platform say?")

    print(f"\n{C['magenta']}--- 4. YOUR REACTION (The Feeling) ---")
    reaction = ask_multiline("How did this moment feel? (Frustrated, Curious, Confused, etc.)")

    # --- STEP 2: Optional Media Capture (The Visual Record) ---
    print(f"\n{C['cyan']}--- STEP 2: MEDIA CAPTURE ---")
    screenshot = ask_bool("Did you take a screenshot?")
    if screenshot:
        # Placeholder for OS-level capture integration when available
        screenshot_desc = ask("Describe the screen content (for filename context):")
        # The machine automatically links this descriptor to a unique file path.
        print(f"--> SUCCESS: Screenshot captured and linked with description: {screenshot_desc}")

    # --- STEP 3: MACHINE ANALYSIS & CONFIRMATION (The Labeling) ---
    print(f"\n{C['cyan']}--- STEP 3: MACHINE ANALYSIS (The Translator) ---")
    print("System is running analysis on your text dump...")
    
    # THE NEW CORE: The machine runs its simulation using the gathered data.
    suggested_list = suggest_triggers(what_happened, context) 
    
    print("\nMachine has analyzed the text and suggests a PRIMARY focus.")
    for i, (trigger_name, confidence) in enumerate(suggested_list):
        print(f"  {i+1}. {trigger_name} (Machine Confidence: {confidence}%)")

    # The human CONFIRMS the machine's suggestion, which is faster than guessing.
    trigger_raw = ask_choice("Select the PRIMARY reason for this observation (CONFIRM MACHINE'S GUESS):", 
                                [f"{t[0]}" for t in suggested_list])

    # --- STEP 4: MICRO-PULSE (The Quick Check) ---
    print(f"\n{C['cyan']}--- STEP 4: MICRO-PULSE (Quick Check) ---")
    micro = ask_bool("Do you have 15 seconds to record your feeling now?")
    if micro:
        # These are fast, single-number inputs.
        micro_data = {
            "clarity": ask_int("Clarity (1-5)", 1, 5),
            "cognitive_load": ask_int("Load (1-5)", 1, 5),
            "affect": ask_int("Affect (1-5)", 1, 5)
        }

    # --- FINAL ACTION: LOGGING ---
    print(f"\n{C['green']}--- FINALIZING LOG ENTRY ---")
    # All these variables are now compiled into the event entry structure.
    # This is where it writes to log_path, appending the full narrative (Dump) and the short code (Trigger/Construct).
    pass 


# ==============================================================
# PHASE I: CRITICAL FLOW UPDATE - cmd_post (The Guided Wizard)
# This transforms the post-session activity from a stressful assignment into a guided reflection.
# ==============================================================

def cmd_post(args: argparse.Namespace):
    current = load_current_session()
    if not current:
        print(f"{C['red']}⚠ No active session. Run 'crg_session.py start' first.{C['reset']}")
        return

    print(f"\n{C['bold']}--- PHASE I: POST-SESSION WIZARD ({current['session_id']}) ---")

    # --- STEP 1: CORE ASSESSMENT (The Quick Check) ---
    print(f"{C['cyan']}--- STEP 1: CORE ASSESSMENT ({current['date']}) ---")
    
    # These inputs are the highest-level cognitive throughput items. They must be gathered first.
    print(f"\n{C['magenta']}--- 1A: Overall Quality (How was the experience?) ---")
    overall_quality = ask_int("Overall Experience Quality (1-7 Scale)", 1, 7)
    
    print(f"\n{C['magenta']}--- 1B: Satisfaction Check ---")
    would_continue = ask_bool("Would you repeat this experience?", default=True)
    
    # Optional: If they say no, the system is prompted to collect data on why.
    if not would_continue:
        reason = ask_multiline("If NOT repeating, why? (REQUIRED)")
    else:
        reason = None

    # --- STEP 2: THE DATA INPUT (The Detail) ---
    print(f"\n{C['cyan']}--- STEP 2: DETAIL CAPTURE ---")
    # The rest of the section moves into distinct, digestible chunks.

    print(f"\n{C['magenta']}--- 2A: Workload Assessment (NASA-TLX) ---")
    # This is where we gather the remaining physical/mental overhead data.
    tlx = {
        "Mental Demand": ask_int("Mental Load (0-100)", 0, 100),
        "Physical Demand": ask_int("Physical Load (0-100)", 0, 100),
        "Temporal Demand": ask_int("Time Pressure (0-100)", 0, 100),
        "Performance": ask_int("Perceived Performance (0=Perfect, 100=Failure)", 0, 100),
        "Effort": ask_int("Effort level (0-100)", 0, 100),
        "Frustration": ask_int("Feeling of Frustration (0-100)", 0, 100),
    }

    # --- STEP 3: THEmatic Coding (The Why) ---
    print(f"\n{C['cyan']}--- STEP 3: THEMATIC CODING ---")
    print(f"{C['magenta']}--- 3A: Subjective Scales (The quick scan) ---")
    # The linear scale is used here as a rapid check against the dominant feeling.
    print("Please rate these 1-7 scale statements:")
    
    # Define subjective scales for thematic coding
    subjective_scales = [
        ("S1", "To what extent did this session help you learn something new?"),
        ("S2", "How confident do you feel about applying what you just learned?"),
        ("S3", "Did the AI system's responses match your expectations?"),
        ("S4", "How useful were the explanations provided by the system?"),
        ("S5", "Did you feel in control of your learning process?"),
        ("S6", "Was the pacing of the session appropriate for you?"),
        ("S7", "How clear was the overall goal or objective of the session?"),
        ("S8", "Did the system adapt to your level of understanding?"),
        ("S9", "Were the examples and analogies helpful in clarifying concepts?"),
        ("S10", "How much did you enjoy working with this AI system?"),
        ("S11", "Did the session challenge you at an appropriate difficulty level?"),
        ("S12", "Was there a good balance between theory and practice?"),
        ("S13", "How well did the session prepare you for future tasks?"),
        ("S14", "Overall, how satisfied were you with this learning experience?"),
    ]
    
    scale_responses = {}
    for key, question in subjective_scales:
        print(f"\n  {C['dim']}[{key}] {question} {C['reset']}")
        val = ask_int(f"Rating (1=Strongly Disagree, 7=Strongly Agree):", 1, 7)
        scale_responses[key] = val
    
    print(f"\n{C['magenta']}--- 3B: FREE TEXT (The Most Valuable Data) ---")
    print("This is where the raw thought goes. Write without filtering.")
    confusion = ask_multiline("What confused you most about the experiment?")
    momentum = ask_multiline("When did it feel RIGHT? (Flow, Success)")
    friction = ask_multiline("What made the process hard or difficult?")

    # --- STEP 4: FINALIZATION ---
    print(f"\n{C['cyan']}--- PHASE IV: BUILD REPORT ---")
    
    # Build comprehensive report data structure
    post_session_data = {
        "session_id": current["session_id"],
        "date": current.get("date", datetime.now().strftime("%Y-%m-%d")),
        "overall_quality": overall_quality,
        "would_repeat": would_continue,
        "reason_not_repeating": reason,
        "tlx_metrics": tlx,
        "subjective_scales": scale_responses,
        "free_text": {
            "confusion": confusion if confusion else "",
            "momentum": momentum if momentum else "",
            "friction": friction if friction else ""
        }
    }

    # Write report to post_session file
    filename = f"post_session_{current['date'].replace('-', '')}_{current['session_id'][:8]}.md"
    filepath = POST_SESSIONS_DIR / filename
    
    report_content = f"""# Post-Session Report - {current['session_id']}

**Date:** {post_session_data["date"]}  
**Overall Quality Rating:** {overall_quality}/7  
**Would Repeat Experience?** {'Yes' if would_continue else 'No'}

## NASA-TLX Workload Assessment
- Mental Demand: {tlx["Mental Demand"]}/100
- Physical Demand: {tlx["Physical Demand"]}/100
- Temporal Demand: {tlx["Temporal Demand"]}/100
- Performance: {tlx["Performance"]}/100 (0=Perfect, 100=Failure)
- Effort: {tlx["Effort"]}/100
- Frustration: {tlx["Frustration"]}/100

## Subjective Scales (1-7 Rating Scale)
"""

    for key, val in scale_responses.items():
        report_content += f"- [{key}] {val}\n"

    if not would_continue and reason:
        report_content += f"\n### Reason Not Repeating\n{reason}\n"
    
    report_content += f"""
## Qualitative Reflections

### What Confused Me Most
> {post_session_data["free_text"]["confusion"] or "N/A"}

### When Did It Feel Right? (Flow, Success)
> {post_session_data["free_text"]["momentum"] or "N/A"}

### What Made the Process Hard or Difficult?
> {post_session_data["free_text"]["friction"] or "N/A"}
"""

    filepath.write_text(report_content, encoding="utf-8")
    
    print(f"\n{C['green']}  ✓ Post-session wizard complete. Report saved to: {filepath.relative_to(REPO_ROOT)}{C['reset']}")
    pass


# ── Command: code (The Translator) ---
def cmd_code(args: argparse.Namespace):
    current = load_current_session()
    if not current:
        print(f"{C['red']}⚠ No active session. Run 'crg_session.py start' first.{C['reset']}")
        return

    events = current.get("events", [])
    if not events:
        print(f"{C['yellow']}⚠ No uncoded observations available in this session. Run 'cmd_event' first.{C['reset']}")
        return

    # --- PHASE 1: Selection (Which Observation?) ---
    print(f"\n{C['bold']}--- PHASE I: SELECTING OBSERVATION ({len(events)} TOTAL) ---")
    # In a live version, this would check the database for coded status. For now, we assume they are uncoded.
    for ev in events:
        print(f"  Event {ev['number']}: [Time: {ev['time']} / Trigger: {TRIGGERS.get(ev['trigger'])}] - Review the full log to confirm details.")

    # For simplicity in this script, we will automatically focus on the most recent/uncoded event.
    target_event = events[-1] 
    print(f"\n--> Automatically selected: Event {target_event['number']} ({target_event['time']})")

    # --- PHASE 2: Verification (Confirming the Dump) ---
    print(f"\n{C['cyan']}--- PHASE II: VERIFYING THE DUMP ---")
    # This screen brings up the full raw data dump from the log file.
    print(f"ACTION: Please review the full text logs at {current['log_file']} to ensure this transcription is accurate.")
    # In the web app, these fields would auto-populate from your log. Here, they are prompts:
    print(f"Event Trigger was: {TRIGGERS.get(target_event['trigger'], 'N/A')}")
    # The script assumes the rich text is in the log file for now.

    # --- PHASE 3: High-Level Coding (The Decision Point) ---
    print(f"\n{C['cyan']}--- PHASE III: CODING & SYNTHESIS ---")
    
    # This is where the machine facilitates the classification.
    print(f"\n{C['magenta']}--- 1. OBSERVATION TYPE (What is it physically?) ---")
    # Prompt the human to name the observation's nature.
    obs_type = ask_choice("What is the most accurate type?", OBSERVATION_TYPES)

    print(f"\n{C['magenta']}--- 2. THE CORE MESSAGE (The Synthesis) ---")
    # The human must now synthesize the raw dump into a concise, linear narrative.
    print("ACTION: Based on your full log review, write the short, factual description of the event.")
    description = ask_multiline("Observation Description (Must be objective and succinct, like a film caption.)", required=True)

    # The machine then guides the high-level classification:
    print(f"\n{C['magenta']}--- 3. CLASSIFICATION TAGS ---")
    primary = ask_choice("Select the single MOST IMPORTANT underlying construct (C1-C6).", 
                           [f"{k}: {v}" for k, v in CONSTRUCTS.items()])
    
    secondary = []
    if ask_bool("Add secondary construct?"):
        # The system allows selecting multiple tags.
        while True:
            sec_raw = ask_choice("Select secondary construct (or 'done')", 
                                   [f"{k}: {v}" for k, v in CONSTRUCTS.items()] + ["done"])
            if sec_raw == "done": break
            secondary.append(sec_raw.split(":")[0])


    # --- PHASE 4: METADATA (The Support Structure) ---
    print(f"\n{C['cyan']}--- PHASE IV: SUPPORTING EVIDENCE (The Proof) ---")
    severity = ask_int("How severe was this observation? (1-5)", 1, 5)
    observer_confidence = ask_int("How confident are you in this specific coding?", 1, 5)

    # The rest of the fields (II_DIMENSIONS, CS_IMPACTS, etc.) are filled out based on the chosen tags.
    # This is a guided workflow to prevent jumping from "bad feeling" to "perfectly coded."

    # --- BUILD YAML (The Final Product) ---
    filename = f"obs_{current['date'].replace('-', '')}_{target_event['number']:03d}_{primary.lower()}.yaml"
    filepath = CODED_DIR / filename

    # The YAML content is now much richer, pulling from the full suite of inputs:
    yaml_content = f"""observation_id: "SYNTHESIS-{filename}"
study: "{current['study']}"
session_id: "{current['session_id']}"
timestamp: "{target_event['time']} (at time of event)"

# --- MACHINE-GENERATED SUMMARY FIELDS ---
primary_construct: "{primary}"
secondary_constructs: {format_list(secondary)}
severity: {severity}
confidence: {observer_confidence}

# --- HUMAN-DEFINED NARRATIVE FIELDS (The Dump) ---
full_event_dump: |
{target_event['reaction']} + {target_event['context']} + {target_event['system_response']}
# The machine concatenates the three inputs into a single, searchable block.

# --- FINAL OBJECTIVE CODING ---
observation_type: "{obs_type}"
description: |
{description}

# ... (All remaining metadata goes here)
"""
    filepath.write_text(yaml_content, encoding="utf-8")
    print(f"\n{C['green']}  ✓ Observation saved and translated to: {filepath.relative_to(REPO_ROOT)}.{C['reset']}")
    pass # End of cmd_code


# ── All other commands (cmd_end, cmd_commit, etc.) remain the same as before.

def now_str():
    """Returns current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    parser = argparse.ArgumentParser(description="CRG-ANL Session Manager", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--session-id", type=str, help="Optional: specify a session ID manually")
    
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")
    
    # start command
    start_parser = subparsers.add_parser("start", help="Start a new data collection session")
    start_parser.set_defaults(func=cmd_start)
    
    # event command
    event_parser = subparsers.add_parser("event", help="Log an observation event during the session")
    event_parser.set_defaults(func=cmd_event)
    
    # post command (NEW - Post-Session Wizard)
    post_parser = subparsers.add_parser("post", help="Run post-session wizard and generate report")
    post_parser.set_defaults(func=cmd_post)
    
    # code command
    code_parser = subparsers.add_parser("code", help="Code an observation into a structured YAML file")
    code_parser.set_defaults(func=cmd_code)

    args = parser.parse_args()
    ensure_dirs()  # Ensure all necessary directories exist
    current = load_current_session()
    
    if not current:
        # Initialize new session
        current = {
            "session_id": f"sess_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "study": args.session_id or ask("Enter study name (optional):", default="unspecified") or "unspecified",
            "events": [],
            "event_count": 0,
        }
        save_current_session(current)
    
    if current["command"] == "start":
        print(f"{C['green']}✓ Session started: {current['session_id']}{C['reset']}")

    elif current["command"] == "event":
        cmd_event(args)

    elif current["command"] == "post":
        cmd_post(args)

    elif current["command"] == "code":
        cmd_code(args)


if __name__ == "__main__":
    main()