# Pilot 001: Session Protocol

**Artifact:** Pilot 001 Session Protocol  
**Version:** 0.1.0  
**Status:** Draft — ready for first session  
**Canonical:** Yes — governs all Pilot 001 data collection sessions  

**Known Limitations:**
- Protocol has not been field-tested; timing estimates are approximate
- Trigger rules may need refinement based on actual event frequency
- Micro-pulse instrument has not been validated for sensitivity

---

## 1. Purpose

This document defines the step-by-step operational protocol for each data collection session in Pilot 001. It is designed to be used *during* sessions as a checklist and reference, not just read beforehand.

For the pilot overview, research questions, and success criteria, see `README.md` in this directory.

---

## 2. Sampling Unit

**Sampling unit:** A single "study session" — defined as a contiguous block of learning activity on the Quantic platform, bounded by intentional start and end points.

**Session eligibility criteria:**
- Minimum duration: 10 minutes (shorter sessions may be logged but flagged)
- Must involve active learning (not just login/logout)
- Researcher must be in condition to observe and record (not exhausted, distracted, or impaired)

---

## 3. Trigger Rules: When to Log an Observation

An observation record must be created whenever **any** of the following events occur:

| Trigger | Description | Priority |
|---------|-------------|----------|
| **T1: Confusion episode** | Confusion or "stuck" state lasting > 60 seconds | Required |
| **T2: Instructional transition** | Transition between lesson → quiz → project → review | Required |
| **T3: AI guidance event** | AI tutor provides explanation, hint, feedback, or direction | Required |
| **T4: Assessment event** | Any quiz, exam, or evaluative interaction, especially ambiguous items | Required |
| **T5: Emotional spike** | Notable frustration, anxiety, surprise, or confidence moment | Required |
| **T6: Safety incident** | Cognitive overload, emotional distress, or integrity failure | Required + immediate notation |
| **T7: Help-seeking** | Request for support (AI or human) and the response received | Optional but encouraged |
| **T8: Milestone** | Completion of significant unit, achievement, or progress marker | Optional |

**Researcher's judgment:** If an event feels significant but doesn't match a trigger above, log it anyway and note the ambiguity.

---

## 4. Session Phases

Each session follows a standardized 4-phase structure:

```
┌─────────────────────────────────────────────────────────────────────┐
│  PHASE 1: PRE-SESSION (4 minutes)                                   │
│  ├── Environment setup                                              │
│  ├── Baseline state assessment                                      │
│  └── Goal setting (1-3 learning objectives)                         │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 2: DURING SESSION (variable, typically 20-60 minutes)        │
│  ├── Real-time event logging                                        │
│  ├── Screenshot capture (as needed)                                 │
│  └── Cognitive safety self-monitoring                               │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 3: POST-SESSION (15 minutes)                                 │
│  ├── NASA-TLX (6 dimensions)                                        │
│  ├── Subjective scales (14 items)                                   │
│  ├── Structured research notes                                      │
│  └── Observation YAML coding                                        │
├─────────────────────────────────────────────────────────────────────┤
│  PHASE 4: MICRO-PULSE (15 seconds per triggered event)              │
│  └── In-the-moment ratings (clarity, load, affect, control, trust)  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. Phase 1: Pre-Session Protocol (4 minutes)

### 5.1 Environment Setup (1 minute)

Check and record:
- [ ] Device being used (mobile / tablet / desktop)
- [ ] Location type (home / commute / work / other)
- [ ] Distraction level (1-5: isolated → highly distracting)
- [ ] Time available for session (minutes)
- [ ] Network stability (stable / intermittent / poor)

### 5.2 Baseline State Assessment (2 minutes)

Rate on 1-7 scale:

| Dimension | Scale | Record |
|-----------|-------|--------|
| Energy level | 1 = exhausted, 7 = highly energized | ___ |
| Stress level | 1 = completely calm, 7 = highly stressed | ___ |
| Prior knowledge (today's topic) | 1 = completely new, 7 = expert | ___ |
| Motivation | 1 = unwilling, 7 = highly motivated | ___ |

### 5.3 Goal Setting (1 minute)

Define 1-3 specific learning objectives for this session:

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

**File:** Save as `baseline_YYYY-MM-DD.md` in `03_evidence/observations/baselines/`

---

## 6. Phase 2: During-Session Protocol (Real-Time)

### 6.1 Event Logging

Maintain a real-time session log. Format:

```markdown
# Session Log: YYYY-MM-DD

## Start: HH:MM
## Device: [mobile/tablet/desktop]
## Location: [home/commute/work/other]

### Event 1 — HH:MM
[Free-form description of what happened]
[Context: what were you trying to do?]
[System response (if any)]
[Your reaction/feeling]
Trigger: [T1-T8 or "judgment call"]

### Event 2 — HH:MM
...

## End: HH:MM
## Total duration: XX minutes
## Observations to code: N
```

### 6.2 Screenshot Protocol

Capture screenshots for events where visual evidence would strengthen the observation:

- **Always capture:** Incorrect explanations, confusing UI states, error messages
- **Capture when possible:** Transition screens, AI guidance responses, assessment items
- **Never capture:** Personal information, payment details, other students' data

**Naming:** `screenshot_NNN_description.png`
**Storage:** `03_evidence/observations/screenshots/YYYY-MM-DD/`

### 6.3 Safety Monitoring

Throughout the session, self-monitor for:
- Overwhelming cognitive load (can't process content)
- Emotional distress (anxiety, frustration, hopelessness)
- Physical symptoms (headache, eye strain, fatigue)

If any of these reach moderate severity (5/7 or higher):
1. Pause the session
2. Note the incident in the log with `SAFETY:` prefix
3. Decide whether to continue, modify, or terminate
4. If terminating, this is a complete session — proceed to Phase 3

---

## 7. Phase 3: Post-Session Protocol (15 minutes)

Complete the post-session instrument. Do not delay — complete immediately after session ends.

### 7.1 NASA-TLX (3 minutes)

Rate each dimension 0-100:

| Dimension | Description | Your Rating |
|-----------|-------------|-------------|
| Mental Demand | How mentally demanding was the session? | ___ |
| Physical Demand | How physically demanding was the session? | ___ |
| Temporal Demand | How hurried or rushed did you feel? | ___ |
| Performance | How successful were you in accomplishing goals? (0 = perfect, 100 = failure) | ___ |
| Effort | How hard did you have to work? | ___ |
| Frustration | How frustrated did you feel? | ___ |

**Optional:** Overall weighted workload score (if time permits)

### 7.2 Subjective Scales (3 minutes)

Rate each item 1-7:

| # | Item | Scale | Rating |
|---|------|-------|--------|
| S1 | "I knew what I was supposed to be learning" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S2 | "The content was at the right difficulty level" | 1 = far too easy, 7 = far too hard (4 = just right) | ___ |
| S3 | "I felt overwhelmed during this session" | 1 = not at all, 7 = extremely | ___ |
| S4 | "I trust the AI tutor's explanations" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S5 | "I had control over my learning path" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S6 | "I felt anxious or stressed during learning" | 1 = not at all, 7 = extremely | ___ |
| S7 | "The feedback I received was helpful" | 1 = not at all helpful, 7 = extremely helpful | ___ |
| S8 | "I felt confident in my understanding" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S9 | "Transitions between activities were smooth" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S10 | "I understood why the system made suggestions" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S11 | "I felt safe making mistakes" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S12 | "The session felt like a good use of my time" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S13 | "I would recommend this learning experience" | 1 = strongly disagree, 7 = strongly agree | ___ |
| S14 | "I felt a sense of progress" | 1 = strongly disagree, 7 = strongly agree | ___ |

### 7.3 Structured Research Notes (5 minutes)

Free-form responses:

**Top confusion moments (if any):**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

**Momentum vs. friction:**
- Where did you feel "in flow"? _______________________________________________
- Where did you get stuck or slowed down? _______________________________________________

**Support effectiveness:**
- What support (AI/human/system) helped most? _______________________________________________
- What support was missing or unhelpful? _______________________________________________

**Safety moments:**
- Any anxiety, frustration, or pressure moments? _______________________________________________

**Surprises:**
- Anything unexpected (positive or negative)? _______________________________________________

### 7.4 Observation YAML Coding (4 minutes per observation)

For each triggered event from the session log, create an observation YAML file following the schema in `02_engineering/schemas/observation_schema.yaml`.

**File naming:** `obs_YYYYMMDD_NNN_<construct>.yaml`
**Location:** `03_evidence/observations/coded/`

---

## 8. Phase 4: Micro-Pulse Protocol (15 seconds)

When a trigger event occurs **during** the session, capture micro-pulse ratings:

| Dimension | Question | Scale |
|-----------|----------|-------|
| Clarity | "Right now, I know what to do next" | 1-5 |
| Cognitive Load | "Right now, this feels mentally heavy" | 1-5 |
| Affect | "Right now, I feel frustrated [or confident]" | 1-5 |
| Control | "Right now, I have control over how to proceed" | 1-5 |
| Trust | "Right now, I trust the guidance I'm receiving" | 1-5 |

**When to capture:** Immediately after a trigger event, before continuing
**Where to record:** Embedded in the observation YAML as `sx_micro_pulse` fields
**Burden target:** < 15 seconds total, < 30 seconds after event

---

## 9. Session Completion Checklist

Before considering a session "complete":

- [ ] Pre-session baseline recorded and saved
- [ ] Session log created with all events noted
- [ ] Screenshots captured and properly named
- [ ] Post-session form complete (NASA-TLX + scales + notes)
- [ ] All triggered events coded as observation YAML files
- [ ] Micro-pulse ratings captured for all applicable events
- [ ] Weekly memo updated (if this is the last session of the week)

---

## 10. Protocol Fidelity

**Target:** > 90% of sessions have complete data (all checklist items)

**Tracking:** Record protocol fidelity per session:
- Which phases were completed
- Which items were skipped and why
- Time taken for each phase
- Any protocol deviations

**Audit:** Monthly review of protocol fidelity with plan for improvement.
