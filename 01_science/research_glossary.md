# Research Glossary

**Artifact:** Research Glossary  
**Version:** 0.1.0  
**Status:** Foundation complete — subject to expansion  
**Canonical:** Yes — standardizes terminology across all workstreams  

---

## How to Use This Glossary

This glossary defines all standardized terminology used in the CRG-ANL Research Program.
Terms are organized alphabetically.
Each entry includes: the term, its canonical definition, the construct it relates to (if applicable), and cross-references to related terms.

When contributing to the research program, use these definitions consistently.
When introducing a new term, add it to this glossary with a definition, construct linkage, and cross-references.

---

## A

**Adaptive Learning**  
An instructional approach in which an AI system adjusts content, difficulty, pacing, or path based on real-time assessment of learner performance and state.
In CRG-ANL, adaptive learning is evaluated for its impact on Cognitive Safety and Learner Agency — excessive or opaque adaptivity can erode safety and agency.
*See also:* Learner Agency, Scaffolding Integrity

**Agency Erosion**  
The progressive reduction of a learner's capacity to set, pursue, and revise their own learning goals, strategies, and standards due to AI system design patterns.
Agency erosion is a key concern in CRG-ANL and is measured through the Learner Agency benchmark dimension.
*Related construct:* C4 Learner Agency
*See also:* Auto-advance, Opaque Adaptivity

**Assessment Integrity**  
The sub-dimension of Instructional Integrity concerned with the validity, accuracy, consistency, and appropriate difficulty of assessments.
*Related construct:* C3 Instructional Integrity
*See also:* Content Validity, Distractor Quality

**Auto-advance**  
A design pattern in which the AI system automatically progresses the learner to the next lesson, topic, or difficulty level without explicit learner consent.
Auto-advance is a common agency erosion pattern.
*See also:* Agency Erosion, Learner Agency

## B

**Benchmark**  
A standardized measurement instrument for evaluating a specific dimension of Constitutional Runtime Governance.
In CRG-ANL, benchmarks are organized hierarchically in the benchmark taxonomy.
*Related construct:* C10 Governance Benchmark
*See also:* Benchmark Taxonomy, Severity Classification

**Benchmark Taxonomy**  
The hierarchical evaluation framework that organizes all CRG-ANL benchmarks into five primary dimensions, 22 sub-dimensions, and associated indicators.
Defined in `01_science/benchmark_taxonomy.md`.
*Related construct:* C10 Governance Benchmark

## C

**Candidate Intervention**  
A proposed Runtime Intervention that could address a observed governance violation, cognitive safety risk, or instructional integrity failure.
Candidate interventions are recorded in observation YAML files for future development.
*Related construct:* C7 Runtime Intervention
*See also:* Observation Schema

**Cascading Failure**  
A sequence of instructional integrity failures in which an initial failure (seed failure) produces subsequent failures in related instructional events (e.g., an incorrect explanation leads to an assessment based on that error, which leads to feedback reinforcing the error).
*Related construct:* C3 Instructional Integrity
*See also:* Failure Propagation, Seed Failure

**Cognitive Continuity**  
One of the three properties of Transition Integrity: the preservation of the learner's working memory representation of the current topic during a transition between instructional states.
*Related construct:* C6 Transition Integrity
*See also:* Epistemic Orientation, Agency Preservation

**Cognitive Load**  
The total amount of mental effort being used in working memory during learning.
Distinguished into intrinsic load (inherent to the material), extraneous load (caused by poor instructional design), and germane load (productive effort toward learning).
*See also:* Cognitive Overload, Cognitive Safety

**Cognitive Overload**  
A state in which the total cognitive demand of an instructional interaction exceeds the learner's working memory capacity, producing performance degradation, confusion, or distress.
One of the five sub-dimensions of Cognitive Safety.
*Related construct:* C2 Cognitive Safety
*See also:* Cognitive Load, NASA-TLX

**Cognitive Safety**  
The protection of a learner's cognitive resources from harm caused by AI-mediated instructional design.
One of the five primary dimensions of the benchmark taxonomy and a foundational construct of CRG-ANL.
*Related construct:* C2 Cognitive Safety
*See also:* Cognitive Overload, Emotional Safety, Attention Threats, Metacognitive Failure

**Constitutional Runtime Governance (CRG)**  
A governance model in which principled behavioral constraints (a "constitution") are applied to AI instructional agents dynamically during runtime, governing every instructional action in real time.
The foundational theoretical construct of the CRG-ANL Research Program.
*Related construct:* C1 Constitutional Runtime Governance
*See also:* Runtime Governance, Governance Benchmark, Persistent Runtime Governance Window

**Content Validity**  
The extent to which an assessment measures the learning objectives it claims to measure.
A component of Assessment Integrity.
*See also:* Assessment Integrity, Instructional Integrity

## D

**Decision Log**  
A record of all architectural and methodological decisions affecting the research program, maintained in ADR (Architecture Decision Record) format.
Located in `07_project_operations/decision_log.md`.
*See also:* Project Operations

## E

**Emotional Safety**  
One of the five sub-dimensions of Cognitive Safety: the absence of anxiety, frustration, demotivation, or distress caused by instructional design.
*Related construct:* C2 Cognitive Safety
*See also:* Cognitive Safety, Frustration

**Epistemic Humility**  
The principle that AI systems should clearly distinguish between established facts, informed inferences, and speculation, and should acknowledge the limits of their knowledge.
A core principle of Constitutional Runtime Governance.
*Related construct:* C1 Constitutional Runtime Governance
*See also:* Epistemic Orientation, Epistemic Reliability

**Epistemic Orientation**  
One of the three properties of Transition Integrity: the learner's understanding of how a new instructional state relates to what they just learned.
*Related construct:* C6 Transition Integrity
*See also:* Cognitive Continuity, Agency Preservation

**Epistemic Reliability**  
The extent to which an AI system provides accurate, verifiable information and appropriately expresses uncertainty.
Related to but distinct from Instructional Integrity — epistemic reliability concerns knowledge accuracy, while instructional integrity concerns pedagogical soundness.
*See also:* Epistemic Humility, Hallucination

**Evidence**  
In CRG-ANL, evidence refers to structured observations, measurements, and artifacts collected during research sessions that support or refute claims about Constitutional Runtime Governance, Cognitive Safety, Instructional Integrity, or related constructs.
Deposited in `03_evidence/`.

## F

**Failure Propagation**  
The process by which an instructional integrity failure spreads to subsequent instructional events, creating a cascade of errors.
*See also:* Cascading Failure, Seed Failure

**Feedback Integrity**  
The sub-dimension of Instructional Integrity concerned with the accuracy, specificity, actionability, and alignment of feedback provided to learners.
*Related construct:* C3 Instructional Integrity

**Field Notes**  
Qualitative observations recorded by the researcher during or after research sessions, providing context, interpretation, and analytical insight.
Deposited in `03_evidence/field_notes/`.

## G

**Governance Benchmark**  
A reproducible, standardized measurement instrument for evaluating CRG adherence.
*Related construct:* C10 Governance Benchmark
*See also:* Benchmark, Benchmark Taxonomy

**Governance Gap**  
An interval within the Persistent Runtime Governance Window during which Constitutional Runtime Governance constraints are not applied to instructional actions.
Governance gaps are critical vulnerabilities in AI-native educational systems.
*Related construct:* C9 Persistent Runtime Governance Window
*See also:* Persistent Runtime Governance Window, Transition Integrity

**Governance Violation**  
An instructional action that violates one or more constitutional constraints defined by the CRG framework.
Governance violations trigger Runtime Interventions.
*Related construct:* C1 Constitutional Runtime Governance
*See also:* Runtime Intervention, Severity Classification

**Germane Load**  
The component of cognitive load that represents productive cognitive effort directed toward schema construction and learning.
Germane load should be maximized; extraneous load should be minimized.
*See also:* Cognitive Load, Cognitive Overload

## H

**Hallucination**  
An AI-generated statement that is factually incorrect, fabricated, or unsupported by evidence, presented as if it were true.
Hallucinations are a primary source of Instructional Integrity failures.
*See also:* Instructional Integrity, Epistemic Reliability

**Human–AI Shared Responsibility**  
The negotiated distribution of cognitive, epistemic, and instructional labor between human learner and AI system.
One of the five primary dimensions of the benchmark taxonomy.
*Related construct:* C5 Human–AI Shared Responsibility
*See also:* Learner Agency, Responsibility Distribution

## I

**Instructional Integrity**  
The property of an AI-native educational system whereby its instructional actions are accurate, coherent, consistent, and aligned with stated learning objectives.
One of the five primary dimensions of the benchmark taxonomy.
*Related construct:* C3 Instructional Integrity
*See also:* Assessment Integrity, Scaffolding Integrity, Navigation Integrity, Transition Integrity, Feedback Integrity, Accessibility Integrity

**Instructional Integrity Dimension**  
One of the six sub-dimensions of Instructional Integrity: Assessment, Scaffolding, Navigation, Transition, Feedback, or Accessibility.
Used in the observation schema to classify integrity-related observations.

## L

**Learner Agency**  
The capacity of a learner to set, pursue, and revise their own learning goals, strategies, and evaluative standards.
One of the five primary dimensions of the benchmark taxonomy.
*Related construct:* C4 Learner Agency
*See also:* Agency Erosion, Goal-Setting, Self-Assessment

**Learner Cockpit**  
A persistent, learner-visible interface element that displays real-time information about the AI system's state, confidence, limitations, and governance status.
*Related construct:* C8 Learner Cockpit
*See also:* Transparency, Situation Awareness

## M

**Metacognitive Failure**  
One of the five sub-dimensions of Cognitive Safety: AI actions that impair the learner's ability to monitor their own understanding, such as providing complete solutions before learner attempts or failing to prompt self-assessment.
*Related construct:* C2 Cognitive Safety

## N

**NASA-TLX**  
The NASA Task Load Index: a standardized subjective workload assessment tool measuring mental demand, physical demand, temporal demand, performance, effort, and frustration on 0-100 scales.
Used in CRG-ANL as a primary measure of cognitive load and emotional state.
*See also:* Cognitive Load, Cognitive Overload

**Navigation Integrity**  
The sub-dimension of Instructional Integrity concerned with the coherence and logical progression of content sequencing.
*Related construct:* C3 Instructional Integrity

## O

**Observation**  
A structured record of a single instructional event, coded using the observation schema and deposited as a YAML file.
The fundamental unit of evidence in CRG-ANL.
*See also:* Observation Schema, Evidence

**Observation Schema**  
The canonical specification for recording observations, defining fields such as observation_id, study, course, lesson, timestamp, observation_type, runtime_trigger, instructional_integrity_dimension, cognitive_safety_impact, human_agency, shared_responsibility, severity, evidence_references, research_memo, candidate_intervention, and future_benchmark_mapping.
Defined in `02_engineering/schemas/observation_schema.yaml`.

**Opaque Adaptivity**  
A design pattern in which the AI system makes adaptive decisions (difficulty changes, path selections) without explaining what was changed, why, or how the learner can influence future decisions.
Opaque adaptivity erodes Learner Agency and Human–AI Shared Responsibility.
*See also:* Agency Erosion, Learner Agency, Human–AI Shared Responsibility

## P

**Persistent Runtime Governance Window (PRGW)**  
The continuous temporal scope within which Constitutional Runtime Governance operates, from session initiation through all instructional transitions to session conclusion.
*Related construct:* C9 Persistent Runtime Governance Window
*See also:* Governance Gap, Constitutional Runtime Governance

**Pilot Study**  
A preliminary research study designed to test methodology, refine constructs, and generate initial evidence.
CRG-ANL conducts pilot studies within the `05_experiments/` workstream.
*See also:* Pilot 001, Pilot 002

**Pilot 001**  
The inaugural CRG-ANL pilot study: a longitudinal researcher-as-subject study of the Quantic MS in AI Engineering.
Located in `05_experiments/pilot_001/`.

## R

**Researcher-as-Subject**  
A methodological framework in which the researcher studies their own learning experience using structured observation, validated instruments, and rigorous analytical protocols.
*Related construct:* C11 Researcher-as-Subject
*See also:* Study Protocol, N-of-1

**Responsibility Distribution**  
The allocation of cognitive, epistemic, and instructional labor between human learner and AI system at a given moment.
Measured as part of the Human–AI Shared Responsibility benchmark dimension.
*Related construct:* C5 Human–AI Shared Responsibility

**Runtime Governance**  
The application of governance constraints during real-time instructional interactions, as opposed to static pre-deployment filters or post-hoc audits.
*See also:* Constitutional Runtime Governance, Persistent Runtime Governance Window

**Runtime Intervention**  
An action triggered in real time by the detection of a governance violation, cognitive safety risk, or instructional integrity failure.
*Related construct:* C7 Runtime Intervention
*See also:* Governance Violation, Candidate Intervention

**Runtime Trigger**  
The specific event or condition that causes an observation to be recorded in the observation schema.
Examples: "AI generated explanation containing factual error" or "Difficulty adjusted without learner notification."

## S

**Scaffolding Integrity**  
The sub-dimension of Instructional Integrity concerned with the correctness, completeness, clarity, and pedagogical coherence of scaffolding content.
*Related construct:* C3 Instructional Integrity
*See also:* Correctness, Completeness, Clarity, Pedagogical Coherence

**Seed Failure**  
The initial instructional integrity failure in a cascading failure sequence.
*See also:* Cascading Failure, Failure Propagation

**Self-Assessment**  
One of the four components of Learner Agency: the learner's capacity to evaluate their own understanding against their own or external standards.
*Related construct:* C4 Learner Agency

**Severity Classification**  
The framework for classifying the severity of governance violations and integrity failures on a 1-5 scale (1 = minor, 5 = critical).
Defined in the benchmark taxonomy.
*See also:* Benchmark Taxonomy, Governance Violation

**Shared Responsibility**  
*See:* Human–AI Shared Responsibility

## T

**Transition**  
A change between instructional states: lessons, topics, difficulty levels, modalities, or phases.
Transitions are critical vulnerability points for governance failures.
*See also:* Transition Integrity, Governance Gap

**Transition Integrity**  
The preservation of cognitive continuity, epistemic orientation, and learner agency during transitions between instructional states.
One of the five primary dimensions of the benchmark taxonomy and one of the six sub-dimensions of Instructional Integrity.
*Related constructs:* C6 Transition Integrity, C3 Instructional Integrity
*See also:* Cognitive Continuity, Epistemic Orientation, Agency Preservation

## W

**Workstream**  
One of the seven top-level organizational units of the CRG-ANL repository: science, engineering, evidence, literature, experiments, publications, or project_operations.
Each workstream has a distinct scientific function and defined relationships to other workstreams.
