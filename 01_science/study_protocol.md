# Study Protocol

**Artifact:** Study Protocol  
**Version:** 0.1.0  
**Status:** Foundation complete — subject to refinement after initial pilot sessions  
**Canonical:** Yes — governs all data collection activity  

---

## Protocol Overview

This document specifies the researcher-as-subject protocol for the Quantic longitudinal case study (Pilot 001).
It defines procedures for session preparation, data collection, observation coding, benchmark application, and evidence deposition.

The protocol is designed to:
- Maximize the validity and reliability of researcher-as-subject observations
- Minimize researcher burden while capturing rich, structured evidence
- Ensure reproducibility of the observation and analysis process
- Protect researcher well-being during data collection

---

## Study Design

### Design Type

Single-subject (N-of-1) longitudinal design with structured observation.
The researcher is both investigator and subject.

### Study Duration

Full duration of the Quantic MS in Artificial Intelligence Engineering program, estimated at 12-18 months.

### Session Structure

A "session" is defined as one contiguous learning period within the Quantic platform, from login to logout.
Sessions may include multiple lessons, assessments, or interactions.

### Data Collection Frequency

| Data Type | Frequency | Method |
|-----------|----------|--------|
| Structured observation | Every session | Observation schema (see below) |
| NASA-TLX | Every session | Post-session rating |
| Subjective scales | Every session | Post-session rating |
| Screenshot documentation | As needed | Capture of significant events |
| Researcher notes | Every session | Free-form structured notes |
| Platform artifacts | Every session | Export or transcription of content |

---

## Pre-Session Procedures

### 1. Environment Preparation (2 minutes)

- [ ] Ensure quiet, distraction-minimized environment
- [ ] Silence notifications on all devices
- [ ] Open observation recording template
- [ ] Verify platform version and note any updates
- [ ] Record session metadata (date, time, device, environment)

### 2. Baseline State Assessment (1 minute)

Record the following on a 1-7 scale:

| Measure | Scale | Record |
|---------|-------|--------|
| Current energy level | 1 (exhausted) — 7 (energized) | |
| Current stress level | 1 (relaxed) — 7 (stressed) | |
| Prior knowledge of today's topic | 1 (none) — 7 (expert) | |
| Motivation for today's session | 1 (reluctant) — 7 (eager) | |

Record any external factors that may affect the session (poor sleep, time pressure, interruptions expected).

### 3. Goal Setting (1 minute)

Record the learner-defined goal for the session:
- What do I want to learn today?
- To what depth?
- How will I know if I've succeeded?

---

## During-Session Procedures

### 1. Event Logging

During the session, record all significant instructional events using the observation schema.
An "event" is any instructional action by the AI system or any significant learner action.

For each event, record:
- Timestamp
- Event type (from taxonomy)
- Brief description
- Initial severity assessment (1-5)

Event types to log:
- New concept introduction
- Scaffolding provision (explanation, hint, worked example)
- Assessment item presentation
- Feedback provision
- Difficulty adjustment
- Topic transition
- Modality transition
- AI error or questionable output
- Learner confusion or struggle
- Learner request for clarification
- Break or pause

### 2. Real-Time Cognitive Safety Monitoring

Throughout the session, self-monitor and note:
- Moments of confusion ("I don't understand this")
- Moments of overload ("This is too much at once")
- Moments of frustration ("This is annoying/unhelpful")
- Moments of attention loss ("I got distracted")
- Moments of metacognitive awareness ("I need to check if I understand")

These notes will be expanded in the post-session structured notes.

### 3. Screenshot Protocol

Capture screenshots of:
- AI outputs that contain errors, hallucinations, or questionable claims
- Transitions (before and after)
- Difficulty adjustments (with context)
- Unusual or unexpected AI behavior
- Interface elements that may affect attention or cognitive load

Screenshots are deposited in `03_evidence/screenshots/` with descriptive filenames.

---

## Post-Session Procedures

### 1. NASA-TLX Assessment (3 minutes)

Rate each dimension on a 0-100 scale:

| Dimension | Description | Score |
|-----------|-------------|-------|
| Mental Demand | How mentally demanding was the session? | 0-100 |
| Physical Demand | How physically demanding was the session? | 0-100 |
| Temporal Demand | How rushed or hurried was the pace? | 0-100 |
| Performance | How successful were you at learning? | 0-100 (0 = perfect) |
| Effort | How hard did you have to work? | 0-100 |
| Frustration | How frustrated, irritated, or annoyed were you? | 0-100 |

Overall NASA-TLX score = average of six dimensions.

### 2. Subjective Scales (2 minutes)

Rate each item on a 1-7 scale (1 = strongly disagree, 7 = strongly agree):

| Item | Scale |
|------|-------|
| I felt in control of my learning during this session. | 1-7 |
| I understood why the AI made the decisions it made. | 1-7 |
| I trusted the information the AI provided. | 1-7 |
| The AI was transparent about its limitations. | 1-7 |
| I felt safe to make mistakes during this session. | 1-7 |
| The pace of the session was appropriate for me. | 1-7 |
| The difficulty level was appropriate for me. | 1-7 |
| I felt the AI understood my learning needs. | 1-7 |
| I would recommend this learning experience to others. | 1-7 |
| I feel I learned something valuable in this session. | 1-7 |

### 3. Structured Research Notes (5 minutes)

Answer the following prompts in free-form text:

**Cognitive Safety:**
- Did you experience any moments of confusion, overload, or frustration?
- If so, when, and how did the system respond?
- Did you feel emotionally safe throughout the session?

**Instructional Integrity:**
- Did the AI make any errors, provide incorrect information, or give inconsistent explanations?
- Were assessments fair and aligned with what was taught?
- Was feedback helpful and accurate?

**Learner Agency:**
- Did you feel in control of your learning path, pace, and depth?
- Could you override AI decisions when you wanted to?
- Did the system support your learning goals?

**Human–AI Shared Responsibility:**
- Did you know what the AI was doing and why?
- Did you feel like a partner or a passenger?
- Were AI limitations made clear?

**Transition Integrity:**
- Were transitions between lessons, topics, or activities smooth and clear?
- Did you understand how new content related to previous content?
- Were you aware when transitions were happening?

**Notable Events:**
- What was the most significant event in this session?
- What worked well?
- What would you change?

### 4. Observation Schema Coding (5 minutes)

Transfer event logs into the canonical observation schema format (YAML).
Each observation receives:

```yaml
observation_id: "OBS-[SESSION]-[NNN]"
study: "pilot_001"
course: "[course_code]"
lesson: "[lesson_id]"
timestamp: "YYYY-MM-DDTHH:MM:SSZ"
observation_type: "[from taxonomy]"
runtime_trigger: "[what triggered the observation]"
instructional_integrity_dimension: "[if applicable]"
cognitive_safety_impact: "[none | minor | moderate | severe]"
human_agency: "[preserved | eroded | restored]"
shared_responsibility: "[appropriate | skewed | unclear]"
severity: 1-5
evidence_references: ["screenshot_001", "interaction_log"]
research_memo: "[analytical note]"
candidate_intervention: "[what intervention would address this]"
future_benchmark_mapping: "[which benchmark dimension this maps to]"
```

### 5. Data Deposition

Deposit all session artifacts in the appropriate evidence directories:

| Artifact | Destination | Naming Convention |
|----------|-------------|-------------------|
| Observation YAML | `03_evidence/observations/` | `OBS-[SESSION]-[NNN].yaml` |
| Screenshots | `03_evidence/screenshots/` | `[SESSION]_[description]_[NNN].png` |
| Research notes | `03_evidence/field_notes/` | `[DATE]_session_[NNN]_notes.md` |
| NASA-TLX | `03_evidence/observations/` | Embedded in observation YAML |
| Subjective scales | `03_evidence/observations/` | Embedded in observation YAML |
| Platform artifacts | `03_evidence/coded_events/` | `[SESSION]_[type]_[NNN].md` |

---

## Weekly Procedures

### 1. Evidence Review (15 minutes)

- Review completeness of all session observations
- Verify all observations are coded in canonical schema format
- Check for missing screenshots, notes, or ratings
- Identify any observations requiring re-coding or additional analysis

### 2. Preliminary Benchmark Application (30 minutes)

- Apply relevant benchmark dimensions to the week's observations
- Generate preliminary scores and severity classifications
- Document any benchmark dimensions that require refinement

### 3. Research Memo (15 minutes)

- Write a brief memo summarizing the week's findings
- Note any patterns, anomalies, or unexpected observations
- Identify questions that require deeper analysis

### 4. Decision Documentation

- If any protocol changes are needed, document in `07_project_operations/decision_log.md`
- If any construct definitions require refinement, document in `01_science/`

---

## Monthly Procedures

### 1. Comprehensive Benchmark Run (2 hours)

- Apply the full benchmark taxonomy to all observations from the month
- Generate primary dimension scores and overall governance score
- Produce severity distribution analysis
- Identify high-frequency failure modes

### 2. Longitudinal Trend Analysis (1 hour)

- Plot benchmark scores over time
- Identify trends, patterns, and change points
- Correlate benchmark scores with subjective ratings
- Assess cognitive safety trajectory

### 3. Protocol Fidelity Audit (30 minutes)

- Assess compliance with the study protocol
- Calculate observation completeness rate
- Identify protocol deviations and their causes
- Refine protocol if needed

### 4. Bias Audit (30 minutes)

- Review researcher notes for confirmation bias indicators
- Assess whether prior expectations influenced observation coding
- Check for Hawthorne effect (has being observed changed behavior?)
- Document bias mitigation effectiveness

### 5. Monthly Report (1 hour)

- Generate a structured monthly report including:
  - Session count and duration statistics
  - Benchmark scores and trends
  - Key findings and patterns
  - Protocol issues and refinements
  - Plans for the coming month

Deposit report in `05_experiments/pilot_001/monthly_reports/`.

---

## Bias Mitigation Protocol

### Known Biases

| Bias | Description | Mitigation Strategy |
|------|-------------|---------------------|
| **Confirmation bias** | Tendency to notice evidence supporting prior expectations | Document all expectations before data collection; require evidence for all claims; seek disconfirming evidence |
| **Hawthorne effect** | Changed behavior due to being observed | Normalize observation through repeated practice; compare early vs. late sessions for adaptation effects |
| **Recall bias** | Inaccurate memory of past sessions | Record observations immediately after sessions; use structured templates; avoid relying on memory |
| **Expectation effects** | Preconceptions about platform performance | Document all prior expectations; use blinded coding where possible; adversarial review |
| **Selection bias** | Selective attention to certain types of events | Use structured observation schema; code all events that meet criteria; avoid selective recording |
| **Anchoring bias** | Over-reliance on first impressions | Reassess severity ratings with fresh perspective; use inter-rater reliability checks |

### Bias Mitigation Procedures

1. **Expectation documentation:** Before each course phase, document expected findings. Reference during analysis.
2. **Structured observation:** Use the observation schema for all events. Do not rely on unstructured impressions.
3. **Adversarial review:** Periodically review observations as if arguing against the researcher's conclusions.
4. **Triangulation:** Compare subjective ratings with objective indicators (timing, error rates, screenshot evidence).
5. **Negative case analysis:** Actively seek observations that contradict emerging patterns.

---

## Ethical Considerations

### Researcher Well-being

- If a session causes significant frustration or distress, the researcher may pause and resume later
- There is no obligation to complete a session that feels harmful to cognitive well-being
- Regular self-checks: Is the research affecting learning quality? If so, adjust protocol or take a break
- The researcher may discontinue the study at any time without penalty

### Data Ethics

- All data pertains to the researcher's own learning experience only
- No data about other students or platform users is collected
- Platform terms of service are respected
- Findings are reported constructively; criticism is directed at design patterns, not individuals or institutions
- De-identification: Any personally identifying information is removed from version-controlled files

### Publication Ethics

- All findings are reported honestly, including negative results and null findings
- Limitations are disclosed transparently
- Methodological weaknesses are acknowledged
- Claims are proportionate to evidence

---

## Protocol Version Control

This protocol follows semantic versioning:

- **Major (X.0.0):** Fundamental changes to study design, observation schema, or data collection procedures
- **Minor (x.Y.0):** Additions of new measures, procedures, or analysis methods
- **Patch (x.y.Z):** Clarifications, corrections, or refinements of existing procedures

All changes are documented in `07_project_operations/decision_log.md` with rationale and impact assessment.

Current version: **0.1.0** (foundation protocol)
