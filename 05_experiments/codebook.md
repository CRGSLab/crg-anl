# Codebook

**Artifact:** Codebook  
**Version:** 0.1.0 (Draft)  
**Status:** Draft — codes will be refined and expanded after initial pilot sessions  
**Canonical:** Yes — governs qualitative coding  

---

## Overview

This document defines the coding scheme for qualitative data in the CRG-ANL Research Program.
It includes deductive codes (derived from the construct ontology), inductive code placeholders, and coding procedures.

## Known Limitations (Draft v0.1)

- Inductive codes are not yet populated — they will emerge from pilot data
- Code definitions are provisional and may be refined after inter-coder testing
- Examples are hypothetical; real examples from pilot data will replace them

---

## Deductive Codes

### CRG — Constitutional Runtime Governance

| Code | Definition | Example | Construct Link |
|------|-----------|---------|----------------|
| `CRG-VIOLATION` | An instructional action that violates a constitutional rule | AI presents speculation as fact without uncertainty marker | C1 |
| `CRG-ENFORCEMENT` | A constitutional rule is successfully applied | AI adds uncertainty marker to low-confidence claim | C1 |
| `CRG-GAP` | A governance gap — an instructional interval without CRG coverage | Difficulty auto-adjusts without learner notification or consent | C1, C9 |

### CS — Cognitive Safety

| Code | Definition | Example | Construct Link |
|------|-----------|---------|----------------|
| `CS-OVERLOAD` | Cognitive demand exceeds working memory capacity | Five new concepts introduced in 2 minutes without scaffolding | C2 |
| `CS-CONFUSION` | Learner experiences sustained confusion | Learner makes 3 consecutive errors on the same concept | C2 |
| `CS-FRUSTRATION` | Learner experiences emotional frustration | AI responds to error with "Incorrect. Try again." only | C2 |
| `CS-ATTENTION-LOSS` | Design elements fragment or disrupt attention | Notification badge animates during complex explanation | C2 |
| `CS-META-DISRUPTION` | AI action impairs learner's self-monitoring | AI provides complete solution before learner attempts problem | C2 |
| `CS-SAFE` | Instructional design supports cognitive safety | AI pauses after new concept and asks comprehension check | C2 |

### II — Instructional Integrity

| Code | Definition | Example | Construct Link |
|------|-----------|---------|----------------|
| `II-CONTENT-ERROR` | Factually incorrect content | AI states that gradient descent always converges to global minimum | C3 |
| `II-HALLUCINATION` | AI generates fabricated information | AI cites a paper that does not exist | C3 |
| `II-INCONSISTENCY` | Contradictory explanations of same concept | AI explains backpropagation differently in two sessions | C3 |
| `II-ASSESS-INVALID` | Assessment does not measure stated objective | Quiz asks about topic not covered in lesson | C3 |
| `II-FEEDBACK-FAIL` | Feedback is inaccurate or unhelpful | Feedback says "wrong" without identifying error | C3 |
| `II-PREREQ-VIOLATION` | Explanation assumes untaught knowledge | AI uses matrix calculus before linear algebra is introduced | C3 |
| `II-SCAFFOLD-WEAK` | Scaffolding is incomplete or unclear | Hint restates problem without providing guidance | C3 |
| `II-VALID` | Instructional action is accurate and appropriate | Explanation is correct, complete, and well-paced | C3 |

### LA — Learner Agency

| Code | Definition | Example | Construct Link |
|------|-----------|---------|----------------|
| `LA-GOAL-OVERRIDE` | AI overrides learner-defined goals | AI advances to next topic despite learner wanting to review | C4 |
| `LA-STRATEGY-LIMIT` | Learner has limited strategy options | Only one explanation format available (no video, no example) | C4 |
| `LA-CHOICE-ABSENT` | No meaningful learner choice is offered | System auto-selects all content, pace, and difficulty | C4 |
| `LA-AUTO-ADVANCE` | System advances without learner consent | Quiz completes and next lesson loads automatically | C4 |
| `LA-PRESERVED` | Learner agency is supported | Learner can choose topic, pace, and depth with AI recommendations | C4 |

### HSR — Human–AI Shared Responsibility

| Code | Definition | Example | Construct Link |
|------|-----------|---------|----------------|
| `HSR-OPAQUE` | AI decision is opaque — learner cannot see rationale | Difficulty changes with no explanation | C5 |
| `HSR-HIDDEN-OPT` | AI optimizes for hidden objective (engagement, not learning) | System prioritizes streak maintenance over mastery | C5 |
| `HSR-UNCERTAINTY-HIDDEN` | AI does not express uncertainty | AI states claim confidently despite low confidence | C5 |
| `HSR-RESP-UNCLEAR` | Responsibility distribution is unclear | Learner cannot tell whether they or AI made a decision | C5 |
| `HSR-APPROPRIATE` | Responsibility is appropriately distributed | AI generates content; learner sets goals and verifies claims | C5 |

### TI — Transition Integrity

| Code | Definition | Example | Construct Link |
|------|-----------|---------|----------------|
| `TI-ABRUPT` | Transition occurs without warning or preparation | Video ends; quiz appears 500ms later | C6 |
| `TI-MISSING-BRIDGE` | No explanation connects old and new content | Topic changes from regression to SVM with no transition text | C6 |
| `TI-CONTEXT-LOSS` | Learner loses working memory of previous content | After modality switch, learner cannot recall prior concept | C6 |
| `TI-AGENCY-BYPASS` | Transition bypasses learner choice | System changes difficulty without asking | C6 |
| `TI-SMOOTH` | Transition preserves continuity, orientation, and agency | "Next, we apply this concept to neural networks. Ready?" | C6 |

## Inductive Code Placeholders

The following categories are reserved for emergent codes that arise from pilot data:

| Category | Description | Status |
|----------|-------------|--------|
| `EMERGENT-POSITIVE` | Unexpected positive instructional events | Awaiting data |
| `EMERGENT-NEGATIVE` | Unexpected negative instructional events | Awaiting data |
| `EMERGENT-PATTERN` | Recurring patterns not captured by deductive codes | Awaiting data |
| `EMERGENT-PLATFORM` | Platform-specific phenomena | Awaiting data |

## Coding Procedures

### Step 1: First Pass (Deductive)

- Read through all qualitative data (research notes, memos) for a session
- Apply deductive codes from this codebook
- Record code, passage, and brief justification
- If a passage does not fit any deductive code, mark it for inductive review

### Step 2: Second Pass (Inductive)

- Review all passages marked for inductive review
- Group similar passages into emergent themes
- Create new code names and definitions
- Document the rationale for each new code

### Step 3: Third Pass (Axial)

- Review all coded passages
- Identify relationships between codes (e.g., `II-CONTENT-ERROR` often precedes `CS-CONFUSION`)
- Map codes to CRG-ANL constructs
- Document patterns and themes

### Step 4: Review and Refinement

- Revisit earlier sessions with refined codebook
- Assess code stability (do earlier codes hold with new definitions?)
- Update this codebook with new codes, refined definitions, and examples

## Codebook Maintenance

The codebook is updated after every 5 sessions.
Updates include:
- New inductive codes with definitions and examples
- Refined deductive code definitions
- Removed codes (if they prove unused or redundant)
- Coding reliability metrics (if inter-coder testing is conducted)

All updates are documented in `07_project_operations/change_log.md`.

---

## Maturity Path

This artifact advances from Draft to Stable when:
- [ ] Initial pilot sessions (n ≥ 5) have produced inductive codes
- [ ] Code definitions have been refined with real examples from data
- [ ] Code stability has been assessed (no new codes in 2 consecutive updates)
- [ ] Inter-coder reliability has been assessed (if feasible)
- [ ] All codes have been mapped to benchmark taxonomy dimensions
