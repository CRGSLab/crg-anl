# Pilot 001: Session Runbook

**Artifact:** Pilot 001 Operational Runbook  
**Version:** 0.1.0  
**Status:** Draft — ready for first session  
**Canonical:** Yes — operational companion to the session protocol  

**Purpose:** This is a just-in-time reference document. Print it, keep it open during sessions, or consult it on a second screen. It answers: "What do I do right now?"

**Known Limitations:**
- Timing estimates are approximate; actual times will vary
- File paths assume standard repository structure

---

## Quick Start: Before Every Session

```
1. Open this runbook (keep accessible during session)
2. Open your session log template
3. Open the Quantic platform
4. Check: Are you in condition to observe? (Not exhausted, not rushed)
5. Note the start time
6. Begin Phase 1: Pre-Session
```

---

## Phase 1: Pre-Session (4 minutes)

### Step 1.1 — Create Baseline File (30 seconds)

**Action:** Create a new markdown file.

**Command template:**
```bash
# From repo root, or create manually
touch 03_evidence/observations/baselines/baseline_$(date +%Y-%m-%d).md
```

**Or manually:** Copy the template below into a new file.

**Filename:** `baseline_YYYY-MM-DD.md`
**Location:** `03_evidence/observations/baselines/`

### Step 1.2 — Fill Baseline Template (3 minutes)

Copy and complete this template:

```markdown
# Pre-Session Baseline — YYYY-MM-DD

## Environment
- **Device:** [mobile / tablet / desktop]
- **Location:** [home / commute / work / other]
- **Distraction level:** [1-5]
- **Time available:** [XX minutes]
- **Network:** [stable / intermittent / poor]

## Baseline State (1-7 scale)
- **Energy:** ___
- **Stress:** ___
- **Prior knowledge (today's topic):** ___
- **Motivation:** ___

## Goals (1-3 specific objectives)
1. ___
2. ___
3. ___

## Session Start
- **Planned start time:** HH:MM
- **Actual start time:** HH:MM
```

### Step 1.3 — Start Session Log (30 seconds)

Create the session log file that you will use for real-time notes.

**Filename:** `session_log_YYYY-MM-DD_HHMM.md`
**Location:** `03_evidence/observations/session_logs/`

**Initial content:**
```markdown
# Session Log — YYYY-MM-DD

## Start: HH:MM
## Device: [from baseline]
## Location: [from baseline]
## Goals: [from baseline]

---

```

**✓ Phase 1 Complete — Begin learning session**

---

## Phase 2: During Session (Real-Time)

### Decision Tree: Should I Log This?

```
Did one of these happen?
├── Confusion lasting > 60 seconds? ────────────────→ LOG IT (T1)
├── Transition between lesson/quiz/project? ────────→ LOG IT (T2)
├── AI tutor gave explanation/hint/feedback? ───────→ LOG IT (T3)
├── Assessment or quiz interaction? ────────────────→ LOG IT (T4)
├── Notable frustration/anxiety/confidence? ────────→ LOG IT (T5)
├── Overwhelmed / distressed / safety concern? ─────→ LOG IT (T6) + SAFETY:
├── Sought help (AI or human)? ─────────────────────→ LOG IT (T7)
└── Completed major milestone? ─────────────────────→ LOG IT (T8)

Does it feel significant even if none above? ────────→ LOG IT (judgment call)
```

### Logging Format (Real-Time)

For each event, append to the session log:

```markdown
### Event N — HH:MM

**What happened:**
[2-3 sentences describing the event]

**Context:**
[What were you trying to do? Where in the course?]

**System response:**
[What did the AI/platform do?]

**My reaction:**
[How did you feel? What did you think?]

**Trigger:** [T1-T8 or "judgment call"]
**Screenshot:** [Y/N — if Y, note description for filename]
**Micro-pulse:** [to be filled after event]
```

### Screenshot Capture (As Needed)

**When to capture:**
- Incorrect or confusing explanations
- UI states that contribute to confusion
- Error messages or system failures
- Transition screens
- Assessment ambiguity

**When NOT to capture:**
- Personal information (name, email, payment)
- Other students' data or profiles
- Anything that would identify you outside the research context

**Filename format:** `screenshot_NNN_brief_description.png`
**Storage:** Create date directory first:
```bash
mkdir -p 03_evidence/observations/screenshots/YYYY-MM-DD/
```

### Safety Monitoring (Continuous)

**Self-check every 10-15 minutes:**
- Am I still able to process content? (If no → possible overload)
- Am I feeling increasingly anxious or frustrated? (If yes → note it)
- Is my physical comfort okay? (Headache, eye strain, posture)

**If safety concern arises:**
1. Pause immediately
2. In session log: Add `SAFETY: [description]` 
3. Decide:
   - **Continue** (mild, can manage)
   - **Modify** (reduce pace, skip difficult section, take break)
   - **Terminate** (severe — session ends, proceed to Phase 3)
4. Document decision and reasoning

---

## Phase 3: Post-Session (15 minutes)

**⚠️ Do not delay. Complete immediately after session ends.**

### Step 3.1 — Record End Time (10 seconds)

In session log, add:
```markdown
## End: HH:MM
## Total duration: XX minutes
## Session complete: [Y/N — if N, note why]
```

### Step 3.2 — Complete Post-Session Form (12 minutes)

Create post-session file:
**Filename:** `post_session_YYYY-MM-DD.md`
**Location:** `03_evidence/observations/post_sessions/`

Use the full template from `01_science/measures_and_instruments.md` Section 2, or the condensed version below:

```markdown
# Post-Session — YYYY-MM-DD

## NASA-TLX (0-100)
| Dimension | Rating |
|-----------|--------|
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

### Top confusion moments
1. ___
2. ___
3. ___

### Momentum vs friction
Flow: ___
Stuck: ___

### Support effectiveness
Helped: ___
Missing: ___

### Safety moments
___

### Surprises
___

## Observations to Code
- [ ] Event 1
- [ ] Event 2
- [ ] Event 3
- [ ] ...
Total: N observations
```

### Step 3.3 — Create Observation YAML Files (4 minutes each)

For each event in your session log, create a coded observation.

**Command:**
```bash
# Create observation file
touch 03_evidence/observations/coded/obs_YYYYMMDD_NNN_<construct>.yaml
```

**Filename pattern:** `obs_YYYYMMDD_NNN_<construct>.yaml`

Where:
- `YYYYMMDD` = session date
- `NNN` = sequential number (001, 002, ...)
- `<construct>` = primary construct (c1_crg, c2_cog_safety, c3_inst_integrity, c4_agency, c5_shared_resp, c6_transition, c10_governance_window)

**Example:** `obs_20260115_003_c2_cog_safety.yaml`

**Required fields (from observation_schema.yaml):**
- `observation_id`
- `study`, `session_id`
- `timestamp`
- `observer` (researcher identity)
- `context`: course, lesson, device, environment
- `observation_type`
- `description`
- `constructs_involved`
- `severity`
- `observer_confidence` (1-5)
- `privacy`: contains_pii, consent_basis, retention_class
- `supporting_evidence` (screenshot references)

**Micro-pulse fields (if captured):**
- `sx_micro_pulse.clarity` (1-5)
- `sx_micro_pulse.cognitive_load` (1-5)
- `sx_micro_pulse.affect` (1-5)
- `sx_micro_pulse.perceived_control` (1-5)
- `sx_micro_pulse.trust` (1-5)

See `02_engineering/schemas/observation_schema.yaml` for complete field specifications.

---

## Post-Session: Weekly Tasks (Every Sunday)

If this is your last session of the week:

### Weekly Review Checklist

- [ ] **Completeness check:** All sessions this week have baseline + log + post-session + coded observations
- [ ] **Preliminary benchmarks:** Apply rough severity-weighted scoring to week's observations
- [ ] **Research memo:** Write weekly memo
- [ ] **Decision log:** Document any protocol changes or edge cases

### Weekly Memo Template

**Filename:** `memo_week_NN_YYYY-MM-DD.md`
**Location:** `03_evidence/memoes/weekly/`

```markdown
# Weekly Memo — Week NN (YYYY-MM-DD to YYYY-MM-DD)

## Sessions This Week
- N sessions
- Total observations: N
- Total duration: XX minutes

## Patterns Observed
[Emerging themes, recurring issues, positive surprises]

## Protocol Issues
[Any problems with the protocol, timing, instruments]

## Construct Reflections
[Do the constructs still fit? Any gaps?]

## Taxonomy Stress
[Any observations that were hard to code?]

## Next Week Focus
[What to pay attention to]

## Decisions
[Any changes made or needed]
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Forgot to log an event | Log it retrospectively in post-session; mark as "retrospective" with estimated timestamp |
| Session interrupted | End session; record actual duration; note interruption cause; proceed to Phase 3 |
| Too many events to code | Prioritize T1 (confusion) and T6 (safety) events; code others when time permits |
| Can't determine construct | Use "uncertain" tag; flag in weekly memo; consider inductive coding |
| Screenshot missed opportunity | Note in log what you would have captured; verbal description in observation YAML |
| Too tired for post-session | Take a short break (10-15 min); if still too tired, complete within 2 hours before memory degrades |
| Quantic platform changes | Document changes in session log; assess impact on comparability; flag in weekly memo |

---

## File Locations Quick Reference

| Artifact | Location | Naming Convention |
|----------|----------|-------------------|
| Pre-session baseline | `03_evidence/observations/baselines/` | `baseline_YYYY-MM-DD.md` |
| Session log | `03_evidence/observations/session_logs/` | `session_log_YYYY-MM-DD_HHMM.md` |
| Screenshots | `03_evidence/observations/screenshots/YYYY-MM-DD/` | `screenshot_NNN_description.png` |
| Post-session form | `03_evidence/observations/post_sessions/` | `post_session_YYYY-MM-DD.md` |
| Coded observations | `03_evidence/observations/coded/` | `obs_YYYYMMDD_NNN_<construct>.yaml` |
| Weekly memos | `03_evidence/memoes/weekly/` | `memo_week_NN_YYYY-MM-DD.md` |
| Monthly reports | `05_experiments/pilot_001/monthly_reports/` | `monthly_report_NN_YYYY-MM.md` |
| Decision log | `07_project_operations/decision_log.md` | Append ADR format |

---

## Timing Summary

| Phase | Target Time | Acceptable Range |
|-------|-------------|-----------------|
| Pre-session | 4 minutes | 3-6 minutes |
| During session | Variable | 20-60 minutes |
| Post-session | 15 minutes | 12-20 minutes |
| Micro-pulse (per event) | 15 seconds | 10-30 seconds |
| Observation coding (per event) | 4 minutes | 3-5 minutes |
| **Total overhead per session** | **~20 minutes** | **15-30 minutes** |

Target: Keep research overhead under 30% of learning time (e.g., 20 min overhead for 60 min session).
