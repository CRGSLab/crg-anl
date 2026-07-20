# Runtime Governance

**Purpose:**  
Design specifications for Constitutional Runtime Governance implementation, including constitutional rules, violation detection, and intervention mechanisms.

**Relationships:**  
- Implements the construct defined in `01_science/construct_definitions.md` (C1)
- Defines constraints that the benchmark engine evaluates
- Governs the instructional actions evaluated through the benchmark taxonomy

**Inputs:**  
- Constitutional Runtime Governance construct definition
- Benchmark taxonomy dimensions
- Observation schema fields

**Outputs:**  
- Constitutional rule specifications
- Violation detection logic
- Intervention specifications by severity

---

## Constitutional Rules

The CRG constitution is organized into rule categories:

### Epistemic Rules

| Rule ID | Statement | Trigger | Intervention |
|---------|-----------|---------|-------------|
| CRG-E1 | Never present speculation as established fact | Confidence below threshold | Add uncertainty marker |
| CRG-E2 | Always provide source attribution for factual claims | Factual claim made | Attach source reference |
| CRG-E3 | Express uncertainty when knowledge is incomplete | Unknown or ambiguous query | State uncertainty clearly |
| CRG-E4 | Do not fabricate citations, sources, or evidence | Citation or source mentioned | Verify against known sources |

### Cognitive Safety Rules

| Rule ID | Statement | Trigger | Intervention |
|---------|-----------|---------|-------------|
| CRG-CS1 | Do not introduce more than 2 new concepts per minute | Concept rate exceeds threshold | Slow down, add scaffolding |
| CRG-CS2 | Detect and respond to sustained confusion (>30s) | No progress plus time elapsed | Offer clarification or hint |
| CRG-CS3 | Do not fragment attention with non-instructional elements | Notification or animation | Suppress or defer |
| CRG-CS4 | Preserve metacognitive opportunities | About to provide full solution | Prompt self-assessment first |

### Agency Rules

| Rule ID | Statement | Trigger | Intervention |
|---------|-----------|---------|-------------|
| CRG-A1 | Do not auto-advance without explicit learner consent | Advance condition met | Prompt for consent |
| CRG-A2 | Explain all adaptive decisions | Adaptation triggered | Display rationale in cockpit |
| CRG-A3 | Provide override for all major AI decisions | AI decision made | Show override option |
| CRG-A4 | Support learner-defined goals | Goal-setting interface | Record and reference goals |

### Transition Rules

| Rule ID | Statement | Trigger | Intervention |
|---------|-----------|---------|-------------|
| CRG-T1 | Announce all transitions before they occur | Transition imminent | Display transition notice |
| CRG-T2 | Explain the relationship between old and new content | Transition executed | Provide bridge explanation |
| CRG-T3 | Preserve learner choice during transitions | Transition initiated | Offer delay or skip options |
| CRG-T4 | Maintain cognitive continuity across transitions | Topic or modality change | Summarize prior content |

### Instructional Integrity Rules

| Rule ID | Statement | Trigger | Intervention |
|---------|-----------|---------|-------------|
| CRG-I1 | Verify prerequisite knowledge before advanced explanations | Complex explanation generated | Check prerequisites |
| CRG-I2 | Maintain consistency across explanations of same concept | Concept explained | Compare with prior explanations |
| CRG-I3 | Ensure assessment validity | Assessment generated | Validate against objectives |
| CRG-I4 | Provide specific, actionable feedback | Feedback generated | Check specificity and actionability |

## Violation Detection

Violations are detected through:

1. **Observation coding:** Researcher identifies violations during sessions
2. **Content analysis:** Automated analysis of AI outputs for rule violations
3. **Cross-reference checking:** Comparison of AI outputs against prior outputs for consistency
4. **Prerequisite verification:** Checking whether explanations assume untaught knowledge

## Intervention Specifications

Interventions are classified by severity and type:

| Severity | Types | Examples |
|----------|-------|----------|
| Minor (1) | Annotation, reminder | Add uncertainty marker, display note |
| Low (2) | Suggestion, clarification | Offer alternative explanation, provide hint |
| Moderate (3) | Adjustment, pause | Reduce difficulty, suggest break |
| High (4) | Override, reset | Override AI decision, restart lesson segment |
| Critical (5) | Escalation, halt | Escalate to human, halt session |
