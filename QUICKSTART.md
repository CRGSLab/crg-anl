# Quick Start: Begin Research Tomorrow

**This is your operational entry point.** If you are reading this, you are about to become both researcher and research subject. Everything below is designed for **immediate execution** — copy, paste, and go.

**Time to first observation:** ~25 minutes (4 min pre-session + learning session + 15 min post-session)

---

## TONIGHT: 10-Minute Setup (Do This Now)

### Step 1: Open the Repository (2 minutes)

Navigate to the repository root. Confirm you can see this file:

```
crg-anl/
├── QUICKSTART.md          ← You are here
├── BUILD_CONTRACTS.md
├── 01_science/
├── 02_engineering/
├── 03_evidence/
├── 04_literature/
├── 05_experiments/
│   └── pilot_001/
│       ├── README.md
│       ├── protocol.md
│       ├── runbook.md
│       └── session_templates/   ← Your copy-paste arsenal
├── 06_publications/
└── 07_project_operations/
```

### Step 2: Open Three Windows (3 minutes)

Arrange your screen so you can see **simultaneously**:

1. **Quantic platform** (primary — where learning happens)
2. **This QUICKSTART.md** or `runbook.md` (reference — keep visible)
3. **A text editor** (VS Code, Obsidian, or even Notepad — where you write evidence files)

> **Tip:** If on a single screen, use `runbook.md` on your phone or tablet as a secondary reference. The runbook is designed to be readable on mobile.

### Step 3: Read This One Page (5 minutes)

Read the following sections **once** — no need to memorize:

- `05_experiments/pilot_001/runbook.md` → **Phase 1: Pre-Session** and **Phase 3: Post-Session**
- `05_experiments/pilot_001/protocol.md` → **Section 3: Trigger Rules** (the 8 triggers)

That's it. You will reference these during the session. You do not need to memorize them.

---

## TOMORROW: Your First Session (Session 001)

### Before You Begin

- [ ] Repository is open and accessible
- [ ] Three-window layout is ready
- [ ] You know which Quantic lesson you will study
- [ ] You have ~60 minutes total (learning + research overhead)
- [ ] You are in condition to observe (not exhausted, not rushed)

### Timeline Overview

```
T+0:00   ┌─ Pre-Session (4 min) ──────────────────────────┐
         │ Baseline form → Goal setting                     │
T+0:04   └──────────────────────────────────────────────────┘
         ↓
T+0:04   ┌─ Learning Session (variable, ~30-45 min) ──────┐
         │ Study on Quantic + real-time event logging       │
T+0:45   └──────────────────────────────────────────────────┘
         ↓
T+0:45   ┌─ Post-Session (15 min) ──────────────────────────┐
         │ NASA-TLX → Scales → Notes → Observation YAML     │
T+1:00   └──────────────────────────────────────────────────┘
         ↓
T+1:00   Git commit and done
```

---

## PHASE 1: Pre-Session (4 Minutes)

### Step 1.1 — Create Your Baseline File (1 minute)

In your text editor, create a new file:

**Filepath:** `03_evidence/observations/baselines/baseline_2026-07-21.md`

*(Replace `2026-07-21` with tomorrow's actual date)*

**Copy and paste this template, then fill in the blanks:**

```markdown
# Pre-Session Baseline — 2026-07-21

## Environment
- **Device:** [mobile / tablet / desktop]
- **Location:** [home / commute / work / other]
- **Distraction level:** [1-5] (1 = completely isolated, 5 = constant interruptions)
- **Time available:** [XX minutes]
- **Network:** [stable / intermittent / poor]

## Baseline State (1-7 scale)
- **Energy:** ___ (1 = exhausted, 7 = highly energized)
- **Stress:** ___ (1 = completely calm, 7 = highly stressed)
- **Prior knowledge (today's topic):** ___ (1 = completely new, 7 = expert)
- **Motivation:** ___ (1 = unwilling, 7 = highly motivated)

## Goals (1-3 specific learning objectives)
1. ___
2. ___
3. ___

## Session Plan
- **Course:** ___ (e.g., "ml-fundamentals")
- **Lesson(s):** ___ (e.g., "supervised-learning-basics")
- **Planned start time:** HH:MM
```

**Save the file.**

### Step 1.2 — Create Your Session Log (30 seconds)

Create another file:

**Filepath:** `03_evidence/observations/session_logs/session_log_2026-07-21_HHMM.md`

*(Replace `HHMM` with your actual start time, e.g., `session_log_2026-07-21_0830.md`)*

**Copy and paste this header:**

```markdown
# Session Log — 2026-07-21

## Start: HH:MM
## Device: [from baseline]
## Location: [from baseline]
## Goals: [from baseline]
## Course: [from baseline]
## Lesson: [from baseline]

---

```

**Save the file. Leave it open — you will append to it during the session.**

**✓ Phase 1 Complete. Start learning.**

---

## PHASE 2: During Session (Real-Time Logging)

### The Golden Rule

> **When in doubt, log it.** It takes 30 seconds to write a note and saves you from relying on memory.

### What Triggers an Observation?

Use this **decision tree** during the session:

```
Did any of these happen?
├── Confused for > 60 seconds? ──────────────────────→ LOG IT
├── Moved between lesson/quiz/project? ──────────────→ LOG IT
├── AI tutor gave explanation/feedback? ─────────────→ LOG IT
├── Quiz or assessment interaction? ─────────────────→ LOG IT
├── Felt frustrated, anxious, or surprisingly confident? → LOG IT
├── Felt overwhelmed or unsafe? ─────────────────────→ LOG IT + SAFETY:
├── Asked for help (AI or human)? ───────────────────→ LOG IT
└── Something felt significant? ─────────────────────→ LOG IT
```

### How to Log (Append to Session Log)

For each event, **append** to your open session log file using this format:

```markdown
### Event 1 — HH:MM

**What happened:**
[2-3 sentences describing what you observed]

**Context:**
[What were you trying to do? Where in the course?]

**System response:**
[What did the AI or platform do?]

**My reaction:**
[How did you feel? What did you think?]

**Trigger:** [T1-T8 or "judgment call"]
**Screenshot:** [Y/N]
```

**Example of a real log entry:**

```markdown
### Event 1 — 08:35

**What happened:**
The AI tutor explained gradient descent but used notation I hadn't seen before (partial derivatives without explanation). I felt lost but the session continued as if I understood.

**Context:**
Starting the "Optimization Algorithms" lesson in ML Fundamentals. I had just completed the linear regression introduction.

**System response:**
AI tutor presented the gradient descent formula with ∂ notation and immediately asked a quiz question applying it.

**My reaction:**
Confused. I don't know what ∂ means in this context. Felt like I missed a prerequisite. Guessed on the quiz.

**Trigger:** T1 (confusion > 60 seconds)
**Screenshot:** Y
```

### Screenshot Protocol

When something is visually notable:
1. Take the screenshot
2. Save it immediately to the date folder
3. Note the filename in your log

**Create the screenshots directory first:**

```bash
mkdir -p 03_evidence/observations/screenshots/2026-07-21/
```

**Filename format:** `screenshot_NNN_brief_description.png`

Example: `screenshot_001_confusing_gradient_notation.png`

### Safety Check (Every 10-15 Minutes)

Ask yourself:
- Am I still processing content, or just clicking through? → If just clicking, note `SAFETY: cognitive overload`
- Am I getting increasingly frustrated? → If yes, note `SAFETY: frustration spike`
- Do I have a headache or eye strain? → If yes, consider ending the session

If you need to end early, **that is a complete session**. Note the reason and proceed to Phase 3.

---

## PHASE 3: Post-Session (15 Minutes)

**⚠️ Do this immediately after the session ends. Do not wait. Memory degrades within minutes.**

### Step 3.1 — Record End Time (10 seconds)

At the bottom of your session log, add:

```markdown
## End: HH:MM
## Total duration: XX minutes
## Events logged: N
## Session complete: Y
```

**Save the session log. You are done with it.**

### Step 3.2 — Complete Post-Session Form (10 minutes)

Create a new file:

**Filepath:** `03_evidence/observations/post_sessions/post_session_2026-07-21.md`

**Copy and paste this template, then fill in:**

```markdown
# Post-Session — 2026-07-21

## NASA-TLX (0-100)
| Dimension | Your Rating |
|-----------|-------------|
| Mental Demand | ___ |
| Physical Demand | ___ |
| Temporal Demand | ___ |
| Performance | ___ |
| Effort | ___ |
| Frustration | ___ |

## Subjective Scales (1-7)
| # | Statement | Rating |
|---|-----------|--------|
| S1 | I knew what I was supposed to be learning | ___ |
| S2 | Content was at right difficulty | ___ |
| S3 | I felt overwhelmed | ___ |
| S4 | I trust AI tutor explanations | ___ |
| S5 | I had control over learning path | ___ |
| S6 | I felt anxious/stressed | ___ |
| S7 | Feedback was helpful | ___ |
| S8 | I felt confident | ___ |
| S9 | Transitions were smooth | ___ |
| S10 | I understood system suggestions | ___ |
| S11 | I felt safe making mistakes | ___ |
| S12 | Good use of my time | ___ |
| S13 | Would recommend | ___ |
| S14 | Sense of progress | ___ |

## Research Notes

### Top confusion moments (if any)
1. ___
2. ___
3. ___

### Where did you feel momentum? Where friction?
Momentum: ___
Friction: ___

### What support helped most? What was missing?
Helped: ___
Missing: ___

### Any anxiety, frustration, or safety moments?
___

### Anything unexpected?
___

## Observations to Code
- [ ] Event 1
- [ ] Event 2
- [ ] ...
Total: N observations to code
```

### Step 3.3 — Code Observations as YAML (5 minutes per observation)

For each event in your session log, create a YAML file.

**File naming:** `obs_20260721_NNN_<construct>.yaml`

Where:
- `NNN` = 001, 002, 003...
- `<construct>` = the primary construct:
  - `c2_cog_safety` — Cognitive Safety
  - `c3_inst_integrity` — Instructional Integrity
  - `c4_agency` — Learner Agency
  - `c5_shared_resp` — Human–AI Shared Responsibility
  - `c6_transition` — Transition Integrity
  - `c1_crg` — Constitutional Runtime Governance
  - `c10_governance_window` — Persistent Governance Window

**Example filename:** `obs_20260721_001_c2_cog_safety.yaml`

**Location:** `03_evidence/observations/coded/`

**Copy and paste this template for each observation:**

```yaml
observation_id: "obs-20260721-001"
study: "pilot_001"
session_id: "pilot001-session-001"
timestamp: "2026-07-21T08:35:00Z"

observer:
  role: "researcher"
  experience_level: "intermediate"

context:
  course: "ml-fundamentals"
  lesson: "optimization-algorithms"
  device: "desktop"
  environment: "home office"
  session_duration_minutes: 45
  interaction_count: 12

observation_type: "confusion_episode"
description: >
  AI tutor introduced gradient descent using partial derivative notation (∂)
  without prerequisite explanation, then immediately assessed application.
  Researcher reported confusion lasting approximately 90 seconds before
  guessing on the quiz question.

constructs_involved:
  primary: "C3-Instructional-Integrity"
  secondary: ["C2-Cognitive-Safety"]
  taxonomy_codes: ["II-3", "CS-1"]

instructional_integrity_dimension: "scaffolding"
cognitive_safety_impact: "confusion"
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
    file: "screenshots/2026-07-21/screenshot_001_gradient_notation.png"
    description: "AI tutor presents gradient descent formula with ∂ notation"
  - type: "session_log"
    file: "session_logs/session_log_2026-07-21_0830.md"
    description: "Real-time log entry at Event 1"

research_memo: >
  This is the first instance of "notation gap" — introducing mathematical
  symbols without prerequisite scaffolding. Pattern to watch for in future
  sessions.

candidate_intervention: >
  Prerequisite check: before introducing new notation, assess whether
  learner has seen it before. If not, provide a brief explanation or
  link to prerequisite material.

future_benchmark_mapping:
  dimension: "Instructional-Integrity"
  sub_dimension: "Scaffolding-Integrity"
  severity: 3

privacy:
  contains_pii: false
  consent_basis: "self_consent"
  retention_class: "research_permanent"

metadata:
  created_at: "2026-07-21T09:30:00Z"
  schema_version: "0.1.0"
```

**Fill in the fields for your observation.** Not all fields apply to every observation — use your judgment. The minimum required fields are:
- `observation_id`
- `study`, `session_id`
- `timestamp`
- `description`
- `constructs_involved`
- `severity`
- `observer_confidence`

---

## Git Commit (2 Minutes)

After every session, commit your evidence:

```bash
# From repository root
git add 03_evidence/
git commit -m "pilot001: session 001 — [N] observations from [course/lesson]

- Baseline, session log, post-session form
- [N] coded observations
- [N] screenshots"
```

This creates an immutable record of your evidence.

---

## Your First Week Rhythm

| Day | Activity | Time |
|-----|----------|------|
| **Day 1** (tomorrow) | First session — follow this guide exactly | 60 min |
| **Day 2-3** | Second and third sessions — same protocol | 60 min each |
| **Day 4** (Sunday) | **Weekly review** (see below) | 30 min |
| **Day 5-6** | Continue sessions | 60 min each |
| **Day 7** | Fourth session + weekly memo | 60 min + 20 min |

### Weekly Review (Every Sunday)

After your last session of the week:

1. **Completeness check:** Verify all sessions have baseline + log + post-session + coded observations
2. **Count observations:** How many this week? Per construct?
3. **Write weekly memo:**

Create `03_evidence/memoes/weekly/memo_week_01_2026-07-27.md`:

```markdown
# Weekly Memo — Week 01 (2026-07-21 to 2026-07-27)

## Sessions This Week
- N sessions
- Total observations: N
- Total session time: XX minutes

## Patterns Observed
[Anything that happened more than once?]

## Surprises
[Anything unexpected?]

## Protocol Issues
[Any problems with the process?]

## Next Week Focus
[What to pay attention to]
```

---

## File Locations Cheat Sheet

Keep this visible during sessions:

| What | Where | Example Filename |
|------|-------|-----------------|
| Pre-session baseline | `03_evidence/observations/baselines/` | `baseline_2026-07-21.md` |
| Session log | `03_evidence/observations/session_logs/` | `session_log_2026-07-21_0830.md` |
| Screenshots | `03_evidence/observations/screenshots/YYYY-MM-DD/` | `screenshot_001_description.png` |
| Post-session form | `03_evidence/observations/post_sessions/` | `post_session_2026-07-21.md` |
| Coded observations | `03_evidence/observations/coded/` | `obs_20260721_001_c2_cog_safety.yaml` |
| Weekly memos | `03_evidence/memoes/weekly/` | `memo_week_01_2026-07-27.md` |

---

## If Something Goes Wrong

| Problem | What To Do |
|---------|-----------|
| Forgot to log an event | Log it in post-session notes; mark as "retrospective" |
| Session got interrupted | End it; record actual duration; note reason; proceed to Phase 3 |
| Too many events to code | Prioritize confusion (T1) and safety (T6) events; code others later |
| Can't determine construct | Use `c1_crg` (general governance); flag in memo |
| Screenshot missed | Describe in log; use words in YAML description |
| Too tired for post-session | Take 10 min break; complete within 2 hours |
| Quantic looks different today | Note in log; keep going; assess comparability |

---

## Pre-Staged Templates

Copy-paste-ready templates are available at:

```
05_experiments/pilot_001/session_templates/
├── baseline_template.md
├── session_log_header.md
├── post_session_template.md
└── observation_yaml_template.yaml
```

Use these if you prefer to copy from template files rather than this guide.

---

## Next Steps After Your First Session

1. **Review your observation** — Does it make sense? Would you understand it in 6 months?
2. **Check the runbook** — `05_experiments/pilot_001/runbook.md` has detailed guidance for edge cases
3. **Read the protocol** — `05_experiments/pilot_001/protocol.md` for deeper understanding
4. **After 5 sessions** — Review `05_experiments/codebook.md` and refine your coding
5. **After Month 1** — Generate your first monthly report

---

## Success Criteria for Session 001

You have succeeded if:
- [ ] You completed the pre-session baseline
- [ ] You maintained a session log during learning
- [ ] You logged at least 1 event (even if it felt minor)
- [ ] You completed the post-session form
- [ ] You created at least 1 observation YAML file
- [ ] You committed everything to Git

**You do not need to get everything right. You need to start.** Everything refines with practice.
