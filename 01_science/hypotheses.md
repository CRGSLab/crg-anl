# Hypotheses

**Artifact:** Hypotheses  
**Version:** 0.1.0  
**Status:** Foundation complete — awaiting preregistration before data analysis  
**Canonical:** Yes — governs confirmatory analysis  

---

## Overview

This document contains the testable hypotheses of the CRG-ANL Research Program.
Each hypothesis is linked to a research question, includes operational definitions for all variables, specifies the planned analytical approach, and indicates whether it will be preregistered.

Hypotheses are organized by construct.
Post-hoc hypotheses (exploratory) will be clearly labeled and analyzed separately from preregistered (confirmatory) hypotheses.

---

## Hypothesis Format

Each hypothesis uses the following structure:

```yaml
id: "H-[CONSTRUCT]-[NUMBER]"
research_question: "RQ-[CONSTRUCT]-[NUMBER]"
statement: "Formal hypothesis statement"
type: "directional" | "non-directional" | "null"
phase: "1" | "2" | "3"
preregistered: false | true
preregistration_date: "YYYY-MM-DD" | null
status: "planned" | "preregistered" | "testing" | "confirmed" | "rejected" | "inconclusive"
operationalization:
  independent_variable: "How the IV is measured"
  dependent_variable: "How the DV is measured"
  controls: "What variables are controlled"
planned_analysis: "Statistical or analytical method"
expected_effect_size: "Cohen's d or equivalent"
power_analysis: "Required sample size for 80% power at alpha=0.05"
```

---

## Cognitive Safety Hypotheses

### H-CS-1: Cognitive Overload Prediction

**Research Question:** RQ-C2.1  
**Statement:** Cognitive overload episodes in AI-native learning sessions are predicted by the density of new concept introductions (rate > 2 concepts per minute), the absence of worked examples or scaffolding after new concept introduction, and high interaction frequency (> 6 AI exchanges per minute).  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Independent variables: Concept introduction rate (concepts/minute), scaffolding presence (binary per concept), interaction frequency (exchanges/minute)
- Dependent variable: Cognitive overload (operationalized as NASA-TLX mental demand > 70 AND self-reported confusion rating >= 5/7)
- Controls: Prior knowledge of topic, session duration, time of day  
**Planned Analysis:** Multiple logistic regression with concept rate, scaffolding presence, and interaction frequency as predictors; overload as binary outcome  
**Expected Effect Size:** Cohen's d = 0.6 (medium)  
**Power Analysis:** n = 45 sessions required for 80% power  
**Construct → Measurable Proxy → Expected Direction:** Cognitive Safety (C2) → NASA-TLX mental demand > 70 + confusion rating ≥ 5/7 → Higher concept density and absent scaffolding predict higher overload probability (positive association)  
**Data That Will Adjudicate:** Post-session NASA-TLX ratings, self-reported confusion ratings, coded observation logs documenting concept introduction rate and scaffolding presence per session

### H-CS-2: Confusion Detection Gap

**Research Question:** RQ-C2.2  
**Statement:** AI-native educational systems detect fewer than 40% of learner confusion episodes when the learner does not explicitly signal confusion (e.g., by typing "I don't understand" or requesting clarification).  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Confusion episode: Period where learner makes >= 2 consecutive errors OR requests clarification OR self-reports confusion >= 5/7
- Detection: System provides targeted support (hint, explanation, difficulty adjustment) within 30 seconds of confusion onset
- Explicit signal: Learner uses confusion-indicating language  
**Planned Analysis:** Sensitivity analysis comparing detection rates with/without explicit signals; binomial proportion test  
**Expected Effect Size:** Large difference in detection rates (detected with signals: 70%, without: 30%)  
**Power Analysis:** n = 30 confusion episodes required  
**Construct → Measurable Proxy → Expected Direction:** Cognitive Safety (C2) → System detection of confusion episodes (targeted support within 30s) → Detection rate is higher when learner explicitly signals confusion (> 70%) than when they do not (< 40%)  
**Data That Will Adjudicate:** Coded observation logs tracking confusion episode onset timestamps and system response timestamps, stratified by whether confusion was explicitly signaled

### H-CS-3: Integrity-Safety Relationship

**Research Question:** RQ-C2.3  
**Statement:** Instructional integrity failures (scaffolding errors, incorrect content, inconsistent explanations) produce measurable cognitive safety decrements within the same session, with the magnitude of the safety decrement proportional to the severity of the integrity failure.  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Integrity failure severity: Coded on 1-5 scale (1 = minor wording issue, 5 = fundamental conceptual error)
- Cognitive safety decrement: Change in NASA-TLX mental demand and frustration from pre-failure to post-failure measurement  
**Planned Analysis:** Within-subject analysis of covariance (ANCOVA) with failure severity as predictor and safety change as outcome  
**Expected Effect Size:** Cohen's d = 0.5 (medium)  
**Power Analysis:** n = 25 integrity failure events required  
**Construct → Measurable Proxy → Expected Direction:** Instructional Integrity (C3) → Coded failure severity (1–5 scale) AND Cognitive Safety (C2) → Change in NASA-TLX mental demand and frustration from pre- to post-failure → Higher severity failures produce larger safety decrements (positive association)  
**Data That Will Adjudicate:** Coded observation logs with severity ratings for each integrity failure event, paired NASA-TLX ratings collected before and after each failure event

---

## Instructional Integrity Hypotheses

### H-II-1: Hallucination Rate

**Research Question:** RQ-C3.1  
**Statement:** AI-generated scaffolding content contains factually incorrect statements (hallucinations) in 8-15% of generated explanations, with higher rates for advanced topics and lower rates for foundational concepts.  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Hallucination: Factually incorrect statement presented as true (verified against authoritative sources)
- Scaffolding content: All AI-generated explanatory text, worked examples, and hints
- Topic level: Foundational (appears in standard curricula) vs. Advanced (specialized, emerging)  
**Planned Analysis:** Proportion estimation with confidence intervals; chi-square comparison of foundational vs. advanced  
**Expected Effect Size:** 8% foundational, 15% advanced  
**Power Analysis:** n = 200 explanations required for 5% precision at 95% CI  
**Construct → Measurable Proxy → Expected Direction:** Instructional Integrity (C3) → Factually incorrect statements in AI-generated scaffolding (verified against authoritative sources) → Advanced topics produce higher hallucination rates than foundational topics  
**Data That Will Adjudicate:** Coded observation logs classifying scaffolding content as accurate or hallucinated, with topic-level classification (foundational vs. advanced)

### H-II-2: Inconsistency Rate

**Research Question:** RQ-C3.2  
**Statement:** AI-generated explanations of the same concept are inconsistent across different sessions in 20-30% of cases, with inconsistencies ranging from minor wording differences to contradictory explanations.  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Inconsistency: Any difference in explanation content between two sessions covering the same concept
- Severity: Minor (wording), Moderate (different emphasis), Major (contradictory)  
**Planned Analysis:** Content comparison across sessions; inter-rater reliability for severity coding  
**Expected Effect Size:** 25% inconsistency rate  
**Power Analysis:** n = 15 concepts x 2 sessions = 30 comparisons  
**Construct → Measurable Proxy → Expected Direction:** Instructional Integrity (C3) → Content differences between explanations of the same concept across sessions → 20–30% of concept explanations show inconsistency (minor to major)  
**Data That Will Adjudicate:** Paired explanation transcripts from different sessions covering the same concept, coded for consistency by independent review against a rubric

### H-II-3: Failure Propagation

**Research Question:** RQ-C3.4  
**Statement:** A single instructional integrity failure (e.g., an incorrect explanation) produces cascading failures in subsequent instructional events (assessments based on the error, feedback that reinforces the error) in 40-60% of cases.  
**Type:** Directional  
**Phase:** 2  
**Operationalization:**
- Seed failure: Initial integrity failure in scaffolding/content
- Cascading failure: Subsequent assessment, feedback, or navigation that incorporates or reinforces the seed failure  
**Planned Analysis:** Event sequence analysis; proportion of seed failures that produce >= 1 cascading failure  
**Expected Effect Size:** 50% propagation rate  
**Power Analysis:** n = 30 seed failure events required  
**Construct → Measurable Proxy → Expected Direction:** Instructional Integrity (C3) → Number of subsequent instructional events that incorporate or reinforce an initial integrity failure → 40–60% of seed failures produce at least one cascading failure  
**Data That Will Adjudicate:** Event sequence coding from observation logs, tracking each seed failure forward through subsequent assessments, feedback events, and scaffolding to identify propagated errors

---

## Learner Agency Hypotheses

### H-LA-1: Agency Erosion Patterns

**Research Question:** RQ-C4.1  
**Statement:** Adaptive AI tutoring systems systematically erode learner agency across all four components (goal-setting, strategy selection, self-assessment, revision), with the greatest erosion in strategy selection (where AI makes pacing and path decisions) and the least erosion in goal-setting (where learner-defined goals are still possible).  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Agency component scores: Self-report scales (1-7) for each of the four components
- Erosion: Deviation from maximum possible agency (7) on each component  
**Planned Analysis:** Repeated measures ANOVA with agency component as within-subject factor  
**Expected Effect Size:** Strategy selection: mean = 3.5/7; Goal-setting: mean = 5.0/7  
**Power Analysis:** n = 20 sessions for repeated measures design  
**Construct → Measurable Proxy → Expected Direction:** Learner Agency (C4) → Self-reported agency component scores (1–7) across goal-setting, strategy selection, self-assessment, revision → Strategy selection shows the greatest erosion (lowest score); goal-setting shows the least  
**Data That Will Adjudicate:** Post-session subjective agency scales (10 items, 1–7), with 4 items mapping to the 4 agency components, aggregated across all sessions

### H-LA-2: Cockpit Agency Effect

**Research Question:** RQ-C4.4  
**Statement:** The presence of a Learner Cockpit that displays AI state, confidence, and governance status increases perceived learner agency by 15-25% compared to sessions without cockpit visibility.  
**Type:** Directional  
**Phase:** 2  
**Operationalization:**
- Learner Cockpit presence: Simulated via structured observation protocol (researcher documents what information would be in a cockpit)
- Perceived agency: Self-report scale (1-7)  
**Planned Analysis:** Within-subject comparison of sessions with/without cockpit documentation  
**Expected Effect Size:** Cohen's d = 0.5  
**Power Analysis:** n = 34 paired sessions required  
**Construct → Measurable Proxy → Expected Direction:** Learner Agency (C4) → Self-reported perceived control (1–7 scale) → Sessions with documented cockpit information produce 15–25% higher perceived agency scores than sessions without  
**Data That Will Adjudicate:** Post-session perceived agency ratings, with sessions categorized by whether the researcher documented cockpit-equivalent information during the session

---

## Transition Integrity Hypotheses

### H-TI-1: Transition Failure Rate

**Research Question:** RQ-C6.1  
**Statement:** Fewer than 50% of instructional transitions in an AI-native educational system preserve all three properties of Transition Integrity (cognitive continuity, epistemic orientation, learner agency).  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Transition: Any change between lessons, topics, difficulty levels, modalities, or phases
- Integrity preservation: All three properties maintained (coded via observation schema)  
**Planned Analysis:** Proportion estimation with confidence intervals  
**Expected Effect Size:** 35% full integrity preservation  
**Power Analysis:** n = 50 transitions required  
**Construct → Measurable Proxy → Expected Direction:** Transition Integrity (C6) → Proportion of transitions preserving all three properties (cognitive continuity, epistemic orientation, learner agency) → Fewer than 50% of transitions preserve all three properties  
**Data That Will Adjudicate:** Coded observation logs of all transition events, with each transition rated on the three integrity properties (preserved / not preserved)

### H-TI-2: Transition Type Vulnerability

**Research Question:** RQ-C6.2  
**Statement:** Modality transitions (e.g., video to quiz, text to interactive) have the lowest transition integrity scores, while topic transitions within the same modality have the highest.  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Transition types: Modality, topic, difficulty, phase
- Integrity score: Average of three property scores (continuity, orientation, agency) on 1-5 scale  
**Planned Analysis:** One-way ANOVA with transition type as factor  
**Expected Effect Size:** Eta-squared = 0.15 (medium)  
**Power Analysis:** n = 15 transitions per type (60 total)  
**Construct → Measurable Proxy → Expected Direction:** Transition Integrity (C6) → Average integrity score (1–5) by transition type → Modality transitions have the lowest scores; topic transitions within the same modality have the highest  
**Data That Will Adjudicate:** Coded transition observations stratified by transition type (modality, topic, difficulty, phase), with integrity scores averaged within each type

---

## Human–AI Shared Responsibility Hypotheses

### H-HSR-1: Default Distribution Skew

**Research Question:** RQ-C5.1  
**Statement:** The default distribution of instructional responsibility in an adaptive AI tutoring system is skewed 70-30 toward the AI (AI: 70%, Human: 30%), with the AI controlling content generation, difficulty adjustment, assessment design, and feedback timing, while the human retains only response selection and basic navigation.  
**Type:** Directional  
**Phase:** 1  
**Operationalization:**
- Responsibility coding: Each instructional action coded as AI-controlled, human-controlled, or shared
- Distribution: Percentage of actions in each category  
**Planned Analysis:** Descriptive statistics; proportion confidence intervals  
**Expected Effect Size:** AI: 70%, Human: 25%, Shared: 5%  
**Power Analysis:** n = 10 sessions with full action coding  
**Construct → Measurable Proxy → Expected Direction:** Human–AI Shared Responsibility (C5) → Proportion of instructional actions coded as AI-controlled, human-controlled, or shared → AI controls ~70% of instructional actions; human retains ~25%; shared ~5%  
**Data That Will Adjudicate:** Coded observation logs with each instructional action classified by responsibility (AI / human / shared), aggregated across sessions

---

## Preregistration Protocol

All P0 and P1 hypotheses will be preregistered on the Open Science Framework (OSF) before data analysis begins.
Preregistration includes:

1. Hypothesis statement and directional prediction
2. Operational definitions of all variables
3. Planned analytical approach
4. Decision rules for confirmation/rejection
5. Expected effect size and power analysis

Post-hoc hypotheses (exploratory analyses) will be:
- Clearly labeled as exploratory in all reports
- Analyzed with appropriate multiple comparison corrections
- Reported separately from confirmatory results
- Used to generate new preregistered hypotheses for subsequent studies

## Hypothesis Status Tracking

| Hypothesis | Phase | Preregistered | Status |
|-----------|-------|--------------|--------|
| H-CS-1 | 1 | Planned | Planned |
| H-CS-2 | 1 | Planned | Planned |
| H-CS-3 | 1 | Planned | Planned |
| H-II-1 | 1 | Planned | Planned |
| H-II-2 | 1 | Planned | Planned |
| H-II-3 | 2 | Planned | Planned |
| H-LA-1 | 1 | Planned | Planned |
| H-LA-2 | 2 | Planned | Planned |
| H-TI-1 | 1 | Planned | Planned |
| H-TI-2 | 1 | Planned | Planned |
| H-HSR-1 | 1 | Planned | Planned |
