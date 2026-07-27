# Quick Start: Automated Session Workflow

**This is your operational entry point.** If you are reading this, you are about to become both researcher and research subject. The `crg` CLI tool automates file creation, naming, cross-referencing, and validation — so you can focus on observing.

**Time to first observation:** ~15 minutes (2 min automated setup + learning session + 10 min guided post-session)

---

## ONE-TIME: Add the Tool to Your Path (2 minutes)

### Option A: Alias (recommended)

Add to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
alias crg='python3 /path/to/crg-anl/02_engineering/instrumentation/crg_session.py'
```

> **Tip:** The path above is absolute. If you move the repo, update the alias.

### Option B: Direct Path

```bash
cd /path/to/crg-anl
python3 02_engineering/instrumentation/crg_session.py <command>
```

### Verify It Works

```bash
crg status
```

You should see the CRG-ANL status header with zero sessions.

---

## BEFORE EVERY SESSION: One Command

```bash
crg start
```

That's it. The tool will:

1. **Prompt you** for baseline data (device, location, energy, stress, goals, etc.)
2. **Auto-fill** smart defaults from your last session
3. **Validate** every rating is in range
4. **Create** the baseline file with correct naming
5. **Create** the session log with header pre-filled from baseline
6. **Create** the dated screenshot directory
7. **Track** session number automatically
8. **Offer** to open Quantic in your browser

> **No copy-paste. No filename math. No template hunting.**

---

## DURING SESSION: Log Events in Seconds

When something happens, run:

```bash
crg event
```

The tool will:
1. Ask which trigger fired (T1–T8 or judgment call)
2. Offer **quick mode** (just timestamp + trigger) or **full mode** (full description now)
3. Ask if you took a screenshot
4. Optionally capture micro-pulse ratings
5. **Append** the event to your session log
6. **Track** event count for post-session

> **Quick mode** is designed for minimal interruption. Fill in details later during post-session.

---

## AFTER SESSION: Guided Post-Session

### Step 1: End the session

```bash
crg end
```

Auto-computes duration and appends the footer to your log.

### Step 2: Complete instruments

```bash
crg post
```

An interactive wizard walks you through:
- NASA-TLX (validated 0–100)
- 14 subjective scales (validated 1–7)
- Research notes (momentum, friction, surprises)
- Auto-generates the observations-to-code checklist from your events

### Step 3: Code observations

```bash
crg code
```

For each uncoded event, the wizard guides you through:
- Observation type (from canonical enum)
- Construct selection (primary + secondary)
- Dimensional coding (II dimension, CS impact, agency, shared responsibility)
- Severity, confidence, outcome
- Micro-pulse (if not captured during session)
- Research memo and candidate intervention

The tool **auto-fills** session context (course, lesson, device, timestamps) and **links** supporting evidence.

### Step 4: Commit

```bash
crg commit
```

Auto-generates a descriptive commit message with session ID, event count, observation count, and screenshot count.

---

## COMPLETE WORKFLOW EXAMPLE

```bash
# === PRE-SESSION ===
crg start
#   ↳ Answer prompts (2 min)
#   ↳ Baseline + session log + screenshot dir created automatically
#   ↳ Quantic opens in browser

# === DURING SESSION ===
# ... studying on Quantic ...
crg event
#   ↳ Select trigger, quick log (15 sec)
# ... more studying ...
crg event
#   ↳ Another event (15 sec)

# === POST-SESSION ===
crg end        # 5 sec
crg post       # NASA-TLX + scales + notes (8 min)
crg code       # Observation YAML wizard (3 min each)
crg code       # Second observation
crg commit     # Git commit (10 sec)
```

**Total overhead: ~12 minutes** (down from ~20 minutes manual)

**Data quality: Higher** — validation prevents out-of-range ratings, cross-references are auto-linked, filenames are always correct.

---

## WEEKLY REVIEW

```bash
crg week
```

Auto-counts sessions, observations, and duration for the current week. You fill in:
- Patterns observed
- Surprises
- Protocol issues
- Construct reflections
- Next week focus

---

## CHEAT SHEET

| Task | Command |
|------|---------|
| Start session | `crg start` |
| Log event | `crg event` |
| End session | `crg end` |
| Post-session form | `crg post` |
| Code observation | `crg code` |
| Git commit | `crg commit` |
| Weekly memo | `crg week` |
| Check status | `crg status` |
| Open Quantic | `crg open` |

---

## WHAT CHANGED FROM THE OLD WORKFLOW?

| Before (manual) | After (automated) |
|---|---|
| Copy-paste templates into new files | `crg start` creates everything |
| Manually compute filenames with dates | Auto-generated, always correct |
| No input validation | Every rating validated against scale |
| Cross-reference baseline → log by hand | Auto-copied into log header |
| Remember session number | Auto-tracked in registry |
| Type full event log during session | Quick mode: 15 seconds |
| Post-session form from scratch | Interactive wizard with validation |
| YAML coded by hand from template | Guided construct selection |
| Git commit message composed manually | Auto-generated with counts |
| Weekly counting by hand | Auto-aggregated from registry |

---

## FILE LOCATIONS (UNCHANGED)

| What | Where | Example Filename |
|------|-------|-----------------|
| Pre-session baseline | `03_evidence/observations/baselines/` | `baseline_2026-07-24.md` |
| Session log | `03_evidence/observations/session_logs/` | `session_log_2026-07-24_0830.md` |
| Screenshots | `03_evidence/observations/screenshots/YYYY-MM-DD/` | `screenshot_001_gradient_notation.png` |
| Post-session form | `03_evidence/observations/post_sessions/` | `post_session_2026-07-24.md` |
| Coded observations | `03_evidence/observations/coded/` | `obs_20260724_001_c2_cog_safety.yaml` |
| Weekly memos | `03_evidence/memoes/weekly/` | `memo_week_01_2026-07-27.md` |
| Session registry | `02_engineering/instrumentation/` | `session_registry.json` |

---

## TROUBLESHOOTING

| Problem | What To Do |
|---------|-----------|
| `crg` command not found | Check your alias/path. Try `python3 02_engineering/instrumentation/crg_session.py` instead. |
| Forgot to log an event | `crg event` → select trigger → full mode → fill retrospectively. Mark "retrospective" in description. |
| Session got interrupted | `crg end` → record actual duration → note interruption in post-session. |
| Too many events to code | `crg code` prioritizes uncoded events. Code T1/T6 first; others can wait. |
| Can't determine construct | Use `c1_crg` (general governance). Flag in weekly memo. |
| Screenshot missed | Describe in log. Use words in YAML description. |
| Too tired for post-session | Take 10 min break. Complete within 2 hours. Run `crg post` when ready. |
| Quantic looks different today | Note in log. Keep going. Assess comparability in weekly memo. |

---

## IF SOMETHING GOES WRONG WITH THE TOOL

The tool never deletes files. If it crashes or behaves unexpectedly:

1. Check `crg status` to see what state it thinks you're in
2. Files are always in `03_evidence/observations/` — you can edit them manually
3. The registry is at `02_engineering/instrumentation/session_registry.json` — it's plain JSON
4. File a bug in `07_project_operations/decision_log.md` using the ADR template

---

## NEXT STEPS

1. **Set up the alias** (2 min)
2. **Run `crg status`** to verify
3. **Run `crg start`** for your first automated session
4. **After 5 sessions** — Review `05_experiments/codebook.md` and refine coding
5. **After Month 1** — Generate your first monthly report

---

*The Quantic curriculum is the experimental environment. The true object of study is a new generation of AI-native educational systems and how they can be systematically evaluated, governed, and improved for learners with diverse cognitive profiles.*
