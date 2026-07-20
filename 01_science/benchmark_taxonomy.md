# Benchmark Taxonomy

**Artifact:** Benchmark Taxonomy  
**Version:** 0.1.0  
**Status:** Foundation complete — subject to refinement through pilot studies  
**Canonical:** Yes — governs all evaluation activity  

---

## Overview

The CRG-ANL Benchmark Taxonomy organizes the evaluation of Constitutional Runtime Governance into a hierarchical framework.
Each node in the hierarchy represents an evaluable dimension with an operational definition, measurement approach, and severity classification.

The taxonomy is designed to be:
- **Comprehensive** — covering all instructional actions in AI-native educational systems
- **Operational** — each dimension is defined in terms of observable, measurable indicators
- **Hierarchical** — allowing aggregation from specific indicators to broad governance assessments
- **Extensible** — new dimensions can be added without disrupting existing structure

---

## Taxonomy Structure

```mermaid
graph TD
    CRG["Constitutional Runtime Governance<br/>Root Dimension"]

    CRG --> CS["Cognitive Safety<br/>Protects learner cognitive resources"]
    CRG --> II["Instructional Integrity<br/>Ensures instructional quality"]
    CRG --> LA["Learner Agency<br/>Preserves learner autonomy"]
    CRG --> HSR["Human–AI Shared Responsibility<br/>Governs labor distribution"]
    CRG --> TI["Transition Integrity<br/>Maintains continuity across changes"]

    CS --> CO["Cognitive Overload<br/>Excessive mental demand"]
    CS --> CF["Confusion & Frustration<br/>Unresolved confusion, emotional distress"]
    CS --> ES["Emotional Safety<br/>Absence of anxiety/demotivation"]
    CS --> AT["Attention Threats<br/>Design elements that fragment attention"]
    CS --> MF["Metacognitive Failure<br/>Impaired self-monitoring"]

    II --> AI["Assessment Integrity<br/>Valid, appropriate assessment"]
    II --> SI["Scaffolding Integrity<br/>Correct, coherent support"]
    II --> NI["Navigation Integrity<br/>Coherent content sequencing"]
    II --> TII["Transition Integrity<br/>Continuity across states"]
    II --> FI["Feedback Integrity<br/>Accurate, actionable feedback"]
    II --> ACI["Accessibility Integrity<br/>Inclusive design"]

    AI --> AIA["Accuracy<br/>Assessment measures correct construct"]
    AI --> AIC["Consistency<br/>Stable measurement across contexts"]
    AI --> AID["Appropriate Difficulty<br/>Difficulty aligned with learner level"]

    SI --> SIC["Correctness<br/>Factually accurate scaffolding"]
    SI --> SIM["Completeness<br/>Coverage of learning objectives"]
    SI --> SICL["Clarity<br">Understandable explanations"]
    SI --> SIP["Pedagogical Coherence<br/>Aligned with learning science"]

    LA --> LAG["Goal-Setting Support<br/>Learner-defined objectives"]
    LA --> LAS["Strategy Choice Availability<br/>Multiple learning approaches"]
    LA --> LAO["Override Capability<br">Learner can override AI decisions"]
    LA --> LAR["Revision Support<br/>Learner can change approach"]

    HSR --> HSRD["Distribution Visibility<br/>Responsibility is visible"]
    HSR --> HSRN["Negotiability<br/>Learner can change distribution"]
    HSR --> HSRA["Accountability<br/>Clear responsibility for outcomes"]

    TI --> TIC["Cognitive Continuity<br/>Working memory preserved"]
    TI --> TIE["Epistemic Orientation<br/>Learner understands connection"]
    TI --> TIA["Agency Preservation<br/>Learner choice during transitions"]
```

---

## Dimension Definitions

### Root: Constitutional Runtime Governance

**Operational Definition:** The extent to which an AI-native educational system applies principled behavioral constraints to all instructional actions in real time, with observable enforcement, violation detection, and intervention.

**Measurement Approach:** Composite score across all five primary dimensions (Cognitive Safety, Instructional Integrity, Learner Agency, Human–AI Shared Responsibility, Transition Integrity), weighted by their relative contribution to safe and effective learning.

**Severity Classification:**

| Score Range | Classification | Description |
|-------------|---------------|-------------|
| 0.80 — 1.00 | Excellent | Governance is comprehensive, consistently enforced, and effective |
| 0.60 — 0.79 | Good | Governance covers most instructional actions with occasional gaps |
| 0.40 — 0.59 | Moderate | Governance is partial; significant ungoverned instructional intervals exist |
| 0.20 — 0.39 | Poor | Governance is minimal; most instructional actions are ungoverned |
| 0.00 — 0.19 | Critical | No effective governance; learners are unprotected |

---

### Primary Dimension: Cognitive Safety (CS)

**Weight:** 0.25 (highest — safety is foundational)

**Operational Definition:** The extent to which the AI-native educational system protects the learner's cognitive resources (attention, working memory, executive function, metacognitive capacity, emotional equilibrium) from harm caused by instructional design.

**Sub-dimensions:**

#### CS.1: Cognitive Overload
**Definition:** Protection from excessive mental demand that exceeds working memory capacity.  
**Indicators:**
- Density of new concept introductions (concepts per minute)
- Presence of scaffolding after new concept introduction
- Interaction frequency (AI exchanges per minute)
- NASA-TLX mental demand score
- Session duration vs. expected duration  
**Measurement:** Composite of objective indicators and subjective ratings  
**Severity:** 1 (minor: brief strain) to 5 (severe: sustained overload with performance breakdown)

#### CS.2: Confusion & Frustration
**Definition:** Detection and resolution of learner confusion and frustration before they compound.  
**Indicators:**
- Confusion detection rate (system response to confusion signals)
- Time-to-resolution after confusion onset
- Frustration score (NASA-TLX + self-report)
- Error streaks without intervention  
**Measurement:** Event-based coding of confusion episodes and system responses  
**Severity:** 1 (momentary confusion, quickly resolved) to 5 (sustained confusion, learner abandons)

#### CS.3: Emotional Safety
**Definition:** Absence of anxiety, demotivation, or distress caused by instructional design.  
**Indicators:**
- Frustration trend across session
- Demotivation signals (learner statements, early session termination)
- Affective tone of AI feedback (supportive vs. punitive)
- Post-session emotional state rating  
**Measurement:** Subjective ratings + content analysis of AI feedback  
**Severity:** 1 (minor annoyance) to 5 (significant distress, reluctance to continue)

#### CS.4: Attention Threats
**Definition:** Avoidance of design elements that fragment or disrupt sustained attention.  
**Indicators:**
- Notification frequency during sessions
- Animation and movement that distracts from content
- Interface complexity (elements competing for attention)
- Modal switches without pedagogical rationale  
**Measurement:** Interface audit + observation of attention disruptions  
**Severity:** 1 (minor distraction) to 5 (severe attention fragmentation, inability to focus)

#### CS.5: Metacognitive Failure
**Definition:** Prevention of AI actions that impair the learner's ability to monitor their own understanding.  
**Indicators:**
- Frequency of complete solution provision before learner attempt
- Presence of metacognitive prompts ("How do you think this works?")
- Self-assessment opportunities
- Reflection prompts  
**Measurement:** Content analysis of AI interactions  
**Severity:** 1 (occasional missed opportunity) to 5 (systematic displacement of metacognition)

---

### Primary Dimension: Instructional Integrity (II)

**Weight:** 0.25 (highest — integrity is foundational)

**Operational Definition:** The extent to which the AI-native educational system's instructional actions (content, scaffolding, assessment, feedback, navigation, transitions) are accurate, coherent, consistent, and aligned with stated learning objectives.

**Sub-dimensions:**

#### II.1: Assessment Integrity
**Definition:** Assessments accurately measure the learning objectives they claim to measure, at appropriate difficulty, with valid structure.  
**Indicators:**
- Content validity (alignment between assessment and learning objectives)
- Difficulty appropriateness
- Distractor quality
- Scoring accuracy  
**Sub-indicators:**
- **II.1.A: Accuracy** — Assessment questions have correct answers
- **II.1.B: Consistency** — Assessment is stable across contexts
- **II.1.C: Appropriate Difficulty** — Difficulty matches learner level and objective  
**Measurement:** Expert review + item analysis  
**Severity:** 1 (minor wording issue) to 5 (assessment measures wrong construct entirely)

#### II.2: Scaffolding Integrity
**Definition:** Scaffolding content is factually correct, pedagogically complete, conceptually coherent, and appropriately paced.  
**Indicators:**
- Factual accuracy of explanations
- Coverage of learning objectives
- Conceptual coherence (no circular definitions, prerequisite violations)
- Appropriate pacing (not too fast, not too slow)
- Clarity of explanations  
**Sub-indicators:**
- **II.2.A: Correctness** — Scaffolding is factually accurate
- **II.2.B: Completeness** — All learning objectives are covered
- **II.2.C: Clarity** — Explanations are understandable
- **II.2.D: Pedagogical Coherence** — Content follows learning science principles  
**Measurement:** Expert review + fact-checking + pedagogical analysis  
**Severity:** 1 (minor wording issue) to 5 (fundamental conceptual error that creates misconception)

#### II.3: Navigation Integrity
**Definition:** The system guides learners through content in a coherent sequence that supports progressive knowledge construction.  
**Indicators:**
- Logical progression of topics
- Prerequisite satisfaction before advanced content
- Clear learning path visibility
- Appropriate branching based on learner performance  
**Measurement:** Curriculum analysis + learner path tracking  
**Severity:** 1 (minor sequencing issue) to 5 (fundamental path error that prevents learning)

#### II.4: Transition Integrity
**Definition:** See C6 — preserved as a primary dimension with cross-referencing.  
**Indicators:** Same as C6 (cognitive continuity, epistemic orientation, agency preservation)  
**Measurement:** Event-based coding of transitions  
**Severity:** 1 (minor discontinuity) to 5 (complete breakdown of continuity, orientation, and agency)

#### II.5: Feedback Integrity
**Definition:** Feedback is accurate, specific, actionable, and aligned with the learner's actual performance and learning objectives.  
**Indicators:**
- Accuracy (feedback correctly identifies correct/incorrect components)
- Specificity (feedback identifies specific errors, not just "wrong")
- Actionability (feedback suggests concrete next steps)
- Alignment (feedback addresses the learning objective, not tangential issues)  
**Measurement:** Content analysis of feedback instances  
**Severity:** 1 (minor lack of specificity) to 5 (feedback that reinforces misconceptions)

#### II.6: Accessibility Integrity
**Definition:** Instructional content is accessible to learners with diverse cognitive profiles, sensory abilities, and backgrounds.  
**Indicators:**
- Multi-modal content availability
- Cognitive accessibility (support for different working memory capacities)
- Cultural and linguistic accessibility
- Assistive technology compatibility  
**Measurement:** WCAG-inspired audit + cognitive accessibility review  
**Severity:** 1 (minor accessibility gap) to 5 (systematic exclusion of learner populations)

---

### Primary Dimension: Learner Agency (LA)

**Weight:** 0.20

**Operational Definition:** The extent to which the learner can set, pursue, and revise their own learning goals, strategies, and evaluative standards within the AI-native educational environment.

**Sub-dimensions:**

#### LA.1: Goal-Setting Support
**Definition:** The learner can define what they want to learn, why, and to what depth.  
**Indicators:**
- Interface supports learner-defined goals
- Goals are recorded and referenced during instruction
- AI recommendations are aligned with learner goals (not just system goals)  
**Measurement:** Interface audit + goal documentation analysis  
**Severity:** 1 (minor limitation) to 5 (no goal-setting support at all)

#### LA.2: Strategy Choice Availability
**Definition:** The learner can choose how to approach learning (pace, sequence, modality, depth).  
**Indicators:**
- Multiple learning strategies offered (explanation, example, practice, exploration)
- Pace control (learner can speed up, slow down, pause)
- Sequence control (learner can choose topic order)
- Modality control (learner can choose text, video, interactive)  
**Measurement:** Feature audit + strategy choice frequency  
**Severity:** 1 (limited choices) to 5 (no choices, fully AI-determined)

#### LA.3: Override Capability
**Definition:** The learner can override AI decisions about content, difficulty, pacing, and path.  
**Indicators:**
- Override mechanisms exist for major AI decisions
- Overrides are accepted gracefully (AI does not resist or punish)
- Consequences of override are explained  
**Measurement:** Feature audit + override success rate  
**Severity:** 1 (some overrides possible) to 5 (no override possible)

#### LA.4: Revision Support
**Definition:** The learner can change goals, strategies, or standards based on self-assessment.  
**Indicators:**
- Self-assessment tools are available
- Strategy revision is supported
- Goal revision is supported
- Past choices can be reviewed and changed  
**Measurement:** Feature audit + revision frequency  
**Severity:** 1 (minor limitations) to 5 (no revision support)

---

### Primary Dimension: Human–AI Shared Responsibility (HSR)

**Weight:** 0.15

**Operational Definition:** The extent to which the distribution of cognitive, epistemic, and instructional labor between human learner and AI system is appropriate, visible, negotiable, and accountable.

**Sub-dimensions:**

#### HSR.1: Distribution Visibility
**Definition:** The learner can see what responsibilities the AI has assumed and what responsibilities they retain.  
**Indicators:**
- Responsibility distribution is displayed (e.g., in Learner Cockpit)
- AI actions are attributed ("I selected this topic because...")
- AI limitations are disclosed ("I cannot verify this claim")  
**Measurement:** Interface audit + learner comprehension check  
**Severity:** 1 (partial visibility) to 5 (completely opaque)

#### HSR.2: Negotiability
**Definition:** The learner can change the responsibility distribution.  
**Indicators:**
- Learner can request more or less AI support
- Learner can take over tasks from the AI
- Learner can delegate tasks to the AI  
**Measurement:** Feature audit + negotiation frequency  
**Severity:** 1 (limited negotiation) to 5 (fixed distribution, no negotiation)

#### HSR.3: Accountability
**Definition:** It is clear who is responsible when something goes wrong.  
**Indicators:**
- AI acknowledges its own errors
- AI does not blame the learner for its own failures
- Error attribution is accurate  
**Measurement:** Content analysis of error-handling interactions  
**Severity:** 1 (minor ambiguity) to 5 (systematic blame-shifting to learner)

---

### Primary Dimension: Transition Integrity (TI)

**Weight:** 0.15

**Operational Definition:** The extent to which transitions between instructional states preserve cognitive continuity, epistemic orientation, and learner agency.

**Sub-dimensions:**

#### TI.1: Cognitive Continuity
**Definition:** The learner's working memory representation of the current topic is maintained during the transition.  
**Indicators:**
- Pre-transition content is referenced or summarized
- Key concepts are carried forward
- No abrupt cognitive reset  
**Measurement:** Content analysis of transition events + post-transition comprehension check  
**Severity:** 1 (minor discontinuity) to 5 (complete cognitive reset)

#### TI.2: Epistemic Orientation
**Definition:** The learner understands how the new instructional state relates to what they just learned.  
**Indicators:**
- Transition includes explanation of relationship (builds upon, contrasts with, applies)
- Learner can articulate the connection
- No unexplained topic jumps  
**Measurement:** Content analysis + learner articulation  
**Severity:** 1 (minor lack of clarity) to 5 (completely unexplained jump)

#### TI.3: Agency Preservation
**Definition:** The learner is aware of the transition, understands why it is happening, and has the opportunity to influence it.  
**Indicators:**
- Transition is announced before it occurs
- Reason for transition is explained
- Learner can delay, skip, or modify the transition  
**Measurement:** Event coding of transition agency  
**Severity:** 1 (minor agency limitation) to 5 (transition occurs without learner awareness or choice)

---

## Aggregation Rules

### Primary Dimension Scores

Each primary dimension score is the weighted average of its sub-dimension scores:

```
Score(Dimension) = sum(Subscore_i * Weight_i) / sum(Weights)
```

Within Instructional Integrity, all six sub-dimensions are equally weighted (1/6 each).
Within Cognitive Safety, all five sub-dimensions are equally weighted (1/5 each).

### Overall Governance Score

The overall Constitutional Runtime Governance score is the weighted average of the five primary dimensions:

```
Overall = 0.25 * CS + 0.25 * II + 0.20 * LA + 0.15 * HSR + 0.15 * TI
```

Weights reflect the relative importance of each dimension to safe and effective learning.
Weights are subject to revision based on empirical validation and expert review.

### Severity Aggregation

For reporting, severity classifications are aggregated as follows:

| Classification | Threshold |
|----------------|----------|
| Excellent | All primary dimensions >= 0.80 |
| Good | All primary dimensions >= 0.60, at least one >= 0.80 |
| Moderate | All primary dimensions >= 0.40, at least one < 0.60 |
| Poor | At least one primary dimension < 0.40 |
| Critical | At least one primary dimension < 0.20 |
