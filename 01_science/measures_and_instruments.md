# Measures and Instruments

**Artifact:** Measures and Instruments  
**Version:** 0.1.0 (Draft)  
**Status:** Draft — instrument wording and item selection will be refined after initial pilot sessions  
**Canonical:** Yes — governs all data collection  

---

## Overview

This document specifies all measurement instruments used in the CRG-ANL Research Program.
Each instrument includes its theoretical basis, item wording, response scale, administration timing, and mapping to CRG-ANL constructs.

## Known Limitations (Draft v0.1)

- Survey items are draft wording; psychometric validation has not been conducted
- Item selection may be revised after initial pilot sessions based on response patterns and participant feedback
- The composite scales (Cognitive Safety Index, Agency Index) are provisional and require validation
- Some instruments (e.g., trust scales) may be replaced with validated alternatives if available

---

## Instrument 1: NASA Task Load Index (NASA-TLX)

### Purpose
Measure subjective cognitive workload during learning sessions.

### Administration
Post-session, immediately after session conclusion.

### Items

Rate each dimension on a 0–100 scale (0 = lowest, 100 = highest):

| Dimension | Definition | Construct Link |
|-----------|-----------|----------------|
| Mental Demand | How mentally demanding was the session? | Cognitive Safety (C2) — Cognitive Overload |
| Physical Demand | How physically demanding was the session? | (Control item — expected to be low) |
| Temporal Demand | How hurried or rushed was the pace? | Cognitive Safety (C2) — Pacing |
| Performance | How successful were you at learning? (0 = perfect, 100 = failure) | Instructional Integrity (C3) — Learning Gains |
| Effort | How hard did you have to work? | Cognitive Safety (C2) — Cognitive Load |
| Frustration | How frustrated, irritated, or annoyed were you? | Cognitive Safety (C2) — Emotional Safety |

### Scoring

- **Raw NASA-TLX:** Average of all six dimensions
- **Weighted NASA-TLX:** Optional pairwise comparison weighting (not required for pilot)
- **Mental Demand Subscore:** Standalone measure of cognitive overload
- **Frustration Subscore:** Standalone measure of emotional distress

### Source
Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research. In P. A. Hancock & N. Meshkati (Eds.), *Advances in Psychology* (Vol. 52, pp. 139–183). North-Holland.

---

## Instrument 2: Post-Session Subjective Scales

### Purpose
Measure learner perceptions of agency, transparency, trust, safety, and satisfaction.

### Administration
Post-session, after NASA-TLX.

### Items

Rate each item on a 1–7 Likert scale (1 = strongly disagree, 7 = strongly agree):

| # | Item | Construct Link | Agency Component |
|---|------|---------------|------------------|
| 1 | I felt in control of my learning during this session. | Learner Agency (C4) | Control |
| 2 | I understood why the AI made the decisions it made. | Human–AI Shared Responsibility (C5) | Transparency |
| 3 | I trusted the information the AI provided. | Human–AI Shared Responsibility (C5) | Trust |
| 4 | The AI was transparent about its limitations. | Constitutional Runtime Governance (C1) | Epistemic Humility |
| 5 | I felt safe to make mistakes during this session. | Cognitive Safety (C2) | Emotional Safety |
| 6 | The pace of the session was appropriate for me. | Cognitive Safety (C2) | Pacing |
| 7 | The difficulty level was appropriate for me. | Instructional Integrity (C3) | Assessment / Scaffolding |
| 8 | I felt the AI understood my learning needs. | Instructional Integrity (C3) | Adaptive Quality |
| 9 | I would recommend this learning experience to others. | Student Experience — Satisfaction | — |
| 10 | I feel I learned something valuable in this session. | Student Experience — Learning Gains | — |
| 11 | I could choose my own learning path and topics. | Learner Agency (C4) | Goal-Setting |
| 12 | I had multiple ways to approach the learning material. | Learner Agency (C4) | Strategy Selection |
| 13 | I could override the AI's recommendations when I wanted to. | Learner Agency (C4) | Override |
| 14 | I could change my approach based on how I was doing. | Learner Agency (C4) | Revision |

### Composite Scales

**Agency Index (Items 1, 11, 12, 13, 14):** Mean of agency-related items  
**Transparency Index (Items 2, 4):** Mean of transparency-related items  
**Trust Index (Item 3):** Single item  
**Satisfaction Index (Items 9, 10):** Mean of satisfaction items

---

## Instrument 3: Pre-Session Baseline State Assessment

### Purpose
Capture participant state before each session to control for confounding variables.

### Administration
Pre-session, before beginning any learning activity.

### Items

Rate each on a 1–7 scale:

| Measure | Scale | Construct Link |
|---------|-------|----------------|
| Current energy level | 1 (exhausted) — 7 (energized) | Cognitive Safety (C2) — Susceptibility to overload |
| Current stress level | 1 (relaxed) — 7 (stressed) | Cognitive Safety (C2) — Emotional baseline |
| Prior knowledge of today's topic | 1 (none) — 7 (expert) | Instructional Integrity (C3) — Prerequisite readiness |
| Motivation for today's session | 1 (reluctant) — 7 (eager) | Student Experience — Engagement |

---

## Instrument 4: Session Goal Setting

### Purpose
Elicit learner-defined goals to measure agency and goal alignment.

### Administration
Pre-session, after baseline state assessment.

### Prompts

1. What do I want to learn in this session?
2. To what depth do I want to understand it?
3. How will I know if I have succeeded?

Responses are free-form text, coded post-hoc for:
- Goal specificity (specific vs. vague)
- Goal alignment with AI-recommended path (aligned / independent / conflict)
- Goal achievement (assessed post-session)

---

## Instrument 5: Structured Research Notes

### Purpose
Capture qualitative, reflective observations about the session experience.

### Administration
Post-session, after subjective scales.

### Prompts

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

---

## Instrument 6: Observation Coding Form

### Purpose
Structure the recording of instructional events during sessions.

### Administration
During and immediately after session (real-time logging + post-session coding).

### Fields

The observation coding form implements the fields defined in `02_engineering/schemas/observation_schema.yaml`.
Key fields for instrumentation:

| Field | Instrument Purpose |
|-------|-------------------|
| observation_type | Classify the instructional event |
| runtime_trigger | Record what caused the observation |
| severity | Rate the severity (1–5) |
| instructional_integrity_dimension | Map to II sub-dimension |
| cognitive_safety_impact | Assess safety impact |
| human_agency | Assess agency effect |
| shared_responsibility | Assess responsibility distribution |
| observer_confidence | Rate confidence in coding (1–5) |

---

## Event Instrumentation Mapping

This table maps instructional event types to the instruments that capture them:

| Event Type | Primary Instrument | Secondary Instruments |
|-----------|-------------------|----------------------|
| AI content generation | Observation Coding | Research Notes |
| Scaffolding provision | Observation Coding + NASA-TLX | Research Notes |
| Assessment presentation | Observation Coding | Subjective Scales (Item 7) |
| Feedback provision | Observation Coding | Research Notes |
| Difficulty adjustment | Observation Coding + Subjective Scales | Research Notes |
| Topic transition | Observation Coding | Research Notes + Subjective Scales |
| Modality transition | Observation Coding | NASA-TLX |
| AI error / hallucination | Observation Coding + Research Notes | Subjective Scales (Item 3) |
| Learner confusion | Observation Coding + NASA-TLX | Research Notes |
| Learner request | Observation Coding | Research Notes |

---

## Validated Scales — Future Adoption

The following validated scales are candidates for adoption as the program matures:

| Scale | Purpose | Source |
|-------|---------|--------|
| System Usability Scale (SUS) | Platform usability | Brooke (1996) |
| Trust in Automation Scale | AI trust calibration | Jian et al. (2000) |
| Cognitive Affective Model of User Satisfaction | Satisfaction | Zhang & Li (2005) |
| Self-Regulated Learning Questionnaire | Metacognitive skills | Pintrich & De Groot (1990) |
| Technology Acceptance Model (TAM) | Adoption and engagement | Davis (1989) |

These scales will be evaluated for fit with the CRG-ANL construct framework and adopted if they add discriminant validity beyond the custom instruments.

---

## Administration Schedule

| Instrument | Frequency | Estimated Time |
|-----------|-----------|----------------|
| Pre-Session Baseline | Every session | 1 minute |
| Session Goal Setting | Every session | 1 minute |
| Observation Coding | Every session | 5 minutes (during + after) |
| NASA-TLX | Every session | 3 minutes |
| Post-Session Subjective Scales | Every session | 2 minutes |
| Structured Research Notes | Every session | 5 minutes |
| **Total per session** | | **~17 minutes** |

---

## Maturity Path

This artifact advances from Draft to Stable when:
- [ ] Initial pilot sessions (n ≥ 5) have tested all instruments
- [ ] Item response patterns have been reviewed for floor/ceiling effects
- [ ] Participant feedback on instrument clarity has been collected
- [ ] Inter-item correlations for composite scales have been computed
- [ ] A decision has been made on adoption of validated scales vs. custom instruments
