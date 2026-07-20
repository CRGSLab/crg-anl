# Pilot 001 Report Template

**Artifact:** Pilot 001 Report Template  
**Version:** 0.1.0  
**Status:** Draft — template with guidance for each section  
**Canonical:** Yes — all Pilot 001 reports follow this structure  

**Purpose:** This template guides the production of the Pilot 001 final report. It is designed to be filled in progressively as data accumulates, not written all at once. Each section includes guidance on content, sources, and quality criteria.

**Known Limitations:**
- This is a template, not a completed report
- Section lengths are estimates; actual length will vary with findings
- Some sections may not apply if the corresponding data was not collected

---

# Pilot 001: Quantic Longitudinal Researcher-as-Subject Pilot — Final Report

**Report ID:** pilot_001_report  
**Version:** [Draft / Review / Final]  
**Date:** [Completion date]  
**Principal Investigator:** [Researcher Name]  
**Study Period:** [Start date] to [End date]  

---

## Executive Summary

**Guidance:** Write this section last. It should be understandable to someone who has not read any other CRG-ANL documentation. Maximum 500 words.

**Required content:**
- What was studied and why (2-3 sentences)
- Methodology in brief (researcher-as-subject, N sessions, duration)
- Key findings (3-5 bullet points, evidence-backed)
- Main limitations (1-2 sentences)
- Implications for the CRG-ANL research program (2-3 sentences)

**Quality criteria:**
- [ ] Someone unfamiliar with the project can understand the core findings
- [ ] Every claim is backed by evidence cited in the report
- [ ] Limitations are acknowledged honestly
- [ ] Claims are proportionate to evidence (no overgeneralization)

---

## 1. Introduction

### 1.1 Background

**Guidance:** Contextualize Pilot 001 within the broader CRG-ANL Research Program. Reference `01_science/research_program.md`.

**Content:**
- What is Constitutional Runtime Governance? (2-3 sentences)
- Why does it matter for AI-native education? (2-3 sentences)
- What is the Quantic MS in AI Engineering as an experimental environment? (2-3 sentences)

### 1.2 Pilot Objectives

**Guidance:** List the specific objectives of Pilot 001. These should map to the success criteria defined in `README.md`.

**Content:**
1. Generate first empirical evidence about CRG in a real AI-native educational environment
2. Validate the observation schema and benchmark taxonomy against actual events
3. Refine construct definitions based on observed phenomena
4. Establish feasibility and validity of researcher-as-subject methodology
5. Produce preliminary benchmark scores for Quantic platform

### 1.3 Research Questions

**Guidance:** List the P0 research questions addressed. Copy from `README.md`.

| ID | Question |
|----|----------|
| RQ-C2.1 | What patterns of AI instructional behavior most reliably predict cognitive overload, confusion, and emotional distress? |
| RQ-C2.2 | How effectively do current AI-native educational systems detect and respond to cognitive safety threats in real time? |
| RQ-C3.1 | What is the rate and distribution of instructional integrity failures across the six dimensions? |
| RQ-C3.2 | How does instructional integrity vary by topic domain? |
| RQ-C4.1 | To what extent does an adaptive AI tutoring system preserve or erode learner agency? |
| RQ-C6.1 | What percentage of instructional transitions preserve all three properties of Transition Integrity? |
| RQ-C11.1 | Can the researcher-as-subject methodology produce internally valid, reproducible evidence? |

---

## 2. Methodology

### 2.1 Research Design

**Guidance:** Describe the researcher-as-subject design. Reference `01_science/study_protocol.md`.

**Content:**
- Design type: Longitudinal N-of-1 researcher-as-subject
- Duration: [X] months
- Sessions: [N] complete sessions
- Setting: Quantic School of Business and Technology, MS in AI Engineering

### 2.2 Participant

**Guidance:** Describe the researcher-as-subject. Maintain appropriate anonymity.

**Content:**
- Role: Graduate student in MS AI Engineering program
- Professional background: [high-level description]
- Prior knowledge: [relevant experience with AI/ML]
- Motivation for participation: [brief]

### 2.3 Instruments

**Guidance:** Describe all measurement instruments used. Reference `01_science/measures_and_instruments.md`.

| Instrument | Purpose | Administration | Data Source |
|-----------|---------|---------------|-------------|
| NASA-TLX | Cognitive workload | Post-session | Self-report |
| Subjective Scales (14 items) | SX dimensions | Post-session | Self-report |
| Structured Research Notes | Qualitative insights | Post-session | Self-report |
| Observation Coding Form | Event classification | Post-session | Coded observations |
| Micro-Pulse Ratings | In-the-moment states | During session | Embedded in observations |
| Pre-Session Baseline | Context and goals | Pre-session | Self-report |

### 2.4 Data Collection Protocol

**Guidance:** Summarize the session protocol. Reference `protocol.md` and `runbook.md`.

**Content:**
- 4-phase session structure (pre / during / post / micro-pulse)
- Trigger rules for observation logging
- File naming and storage conventions
- Quality control procedures

### 2.5 Analysis Approach

**Guidance:** Summarize the analysis plan. Reference `01_science/analysis_plan.md`.

**Content:**
- Qualitative analysis (coding approach, codebook version)
- Quantitative analysis (descriptive stats, benchmark calculations)
- Triangulation strategy
- Validity threat mitigation

---

## 3. Descriptive Statistics

### 3.1 Session Coverage

**Guidance:** Provide comprehensive session-level statistics.

| Metric | Value |
|--------|-------|
| Total sessions attempted | N |
| Complete sessions (all phases) | N |
| Incomplete sessions | N (list reasons) |
| Total session time | XX hours |
| Mean session duration | XX minutes (SD = X) |
| Date range | YYYY-MM-DD to YYYY-MM-DD |
| Sessions per week (mean) | X (SD = X) |

### 3.2 Observation Summary

**Guidance:** Provide comprehensive observation-level statistics.

| Metric | Value |
|--------|-------|
| Total coded observations | N |
| Observations per session (mean) | X (SD = X) |
| Observations by construct (table) | See below |
| Observations by severity (table) | See below |
| Screenshot evidence linked | N (X% of observations) |

**Observations by construct:**

| Construct | Count | % of Total | Mean Severity |
|-----------|-------|-----------|--------------|
| Cognitive Safety (C2) | N | X% | X.X |
| Instructional Integrity (C3) | N | X% | X.X |
| Learner Agency (C4) | N | X% | X.X |
| Human–AI Shared Responsibility (C5) | N | X% | X.X |
| Transition Integrity (C6) | N | X% | X.X |
| Runtime Intervention (C7) | N | X% | X.X |
| Constitutional Runtime Governance (C1) | N | X% | X.X |

**Observations by severity:**

| Severity | Count | % | Description |
|----------|-------|---|-------------|
| 1 — Informational | N | X% | Notable but not problematic |
| 2 — Minor | N | X% | Slight friction, easily resolved |
| 3 — Moderate | N | X% | Significant issue, required adaptation |
| 4 — Major | N | X% | Serious problem, session impact |
| 5 — Critical | N | X% | Session-threatening or safety-relevant |

### 3.3 Data Quality

**Guidance:** Assess completeness, consistency, and reliability of the dataset.

| Quality Metric | Target | Actual | Assessment |
|---------------|--------|--------|------------|
| Protocol fidelity | > 90% | X% | [met / not met] |
| Complete session data | 100% | X% | [met / not met] |
| All observations coded | 100% | X% | [met / not met] |
| Screenshots linked (where applicable) | > 80% | X% | [met / not met] |
| Post-session forms complete | 100% | X% | [met / not met] |
| NASA-TLX completion | 100% | X% | [met / not met] |

---

## 4. Benchmark Results

### 4.1 Primary Dimension Scores

**Guidance:** Present benchmark scores for each primary dimension. Show evolution over time if applicable.

| Primary Dimension | Mean Score | SD | Range | Interpretation |
|------------------|------------|-----|-------|---------------|
| Cognitive Safety (C2) | X.XX | X.XX | X.XX — X.XX | [brief] |
| Instructional Integrity (C3) | X.XX | X.XX | X.XX — X.XX | [brief] |
| Learner Agency (C4) | X.XX | X.XX | X.XX — X.XX | [brief] |
| Human–AI Shared Responsibility (C5) | X.XX | X.XX | X.XX — X.XX | [brief] |
| Transition Integrity (C6) | X.XX | X.XX | X.XX — X.XX | [brief] |
| **Overall Governance (C1)** | **X.XX** | **X.XX** | **X.XX — X.XX** | **[brief]** |

**Score interpretation guide:**
- 0.80–1.00: Excellent — minimal issues, strong governance
- 0.60–0.79: Good — occasional issues, generally adequate
- 0.40–0.59: Fair — regular issues, governance gaps evident
- 0.20–0.39: Poor — frequent issues, significant governance failures
- 0.00–0.19: Critical — systemic failures, immediate attention needed

### 4.2 Longitudinal Trends

**Guidance:** If sufficient data exists, show how scores evolved over time.

**Include:**
- Time-series plot of primary dimension scores (if possible to generate)
- Notable events that may explain score changes
- Trends by course phase or topic domain

### 4.3 Sub-Dimension Breakdown

**Guidance:** Provide detailed breakdown for dimensions with sufficient observations.

[Table or narrative for each primary dimension with sub-dimension scores]

---

## 5. Construct Validation

### 5.1 Evidence for Construct Validity

**Guidance:** For each construct, present evidence that the operationalization captured the intended phenomenon.

| Construct | Supporting Evidence | Contradictory Evidence | Assessment |
|-----------|-------------------|----------------------|------------|
| Cognitive Safety (C2) | [Examples from observations] | [Any gaps or anomalies] | [valid / needs refinement / unclear] |
| Instructional Integrity (C3) | [Examples] | [Gaps] | [Assessment] |
| Learner Agency (C4) | [Examples] | [Gaps] | [Assessment] |
| Human–AI Shared Responsibility (C5) | [Examples] | [Gaps] | [Assessment] |
| Transition Integrity (C6) | [Examples] | [Gaps] | [Assessment] |

### 5.2 Construct Refinements Proposed

**Guidance:** Based on empirical experience, propose any changes to construct definitions, relationships, or operationalizations.

| Construct | Proposed Change | Rationale | Confidence |
|-----------|----------------|-----------|------------|
| [C#] | [Description] | [Evidence] | [high / medium / low] |

---

## 6. Taxonomy Assessment

### 6.1 Coverage Analysis

**Guidance:** Report the taxonomy stress test results.

| Metric | Target | Actual |
|--------|--------|--------|
| Coverage rate | ≥ 90% | X% |
| Ambiguous observations | < 10% | X% |
| Uncodable observations | < 5% | X% |

### 6.2 Discriminability Analysis

**Guidance:** Assess whether the taxonomy can distinguish between different types of events.

| Test | Result |
|------|--------|
| Severity distribution | [description] |
| Construct separation | [can events be unambiguously assigned?] |
| Redundancy check | [observations mapping to > 3 dimensions] |

### 6.3 Proposed Taxonomy Revisions

**Guidance:** Document any proposed changes to the benchmark taxonomy.

| Proposal | Type | Rationale | Priority |
|----------|------|-----------|----------|
| [Description] | [add / modify / remove / merge] | [Evidence] | [high / medium / low] |

---

## 7. Mechanism → Student Experience Links

### 7.1 Qualitative Analysis

**Guidance:** Present narrative findings about how CRG mechanisms shaped student experience.

**Content:**
- Critical incident analyses (2-3 detailed examples)
- Pattern descriptions (recurring themes)
- Surprising findings (unexpected patterns)

### 7.2 Quantitative Plausibility Checks

**Guidance:** If sufficient data exists, test mechanism → SX state relationships.

| Hypothesized Link | Evidence | Assessment |
|------------------|----------|------------|
| Instructional Integrity → Clarity | [Data] | [supported / not supported / inconclusive] |
| Cognitive Safety → Affect | [Data] | [Assessment] |
| Transition Integrity → Momentum | [Data] | [Assessment] |
| Learner Agency → Control | [Data] | [Assessment] |

---

## 8. Methodology Assessment

### 8.1 Feasibility

**Guidance:** Assess whether the researcher-as-subject methodology was feasible to execute.

| Aspect | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Time burden | < 30% of learning time | X% | [acceptable / excessive] |
| Protocol adherence | > 90% | X% | [achievable / needs simplification] |
| Data quality | Complete and usable | [Assessment] | [sufficient / insufficient] |
| Researcher well-being | No adverse effects | [Assessment] | [maintained / concerns] |

### 8.2 Validity Threats

**Guidance:** Assess validity threats that materialized during the pilot.

| Threat Category | Threat | Severity | Mitigation Effectiveness |
|----------------|--------|----------|------------------------|
| Internal validity | [Specific threat] | [high / medium / low] | [effective / partial / ineffective] |
| External validity | [Specific threat] | [Severity] | [Effectiveness] |
| Construct validity | [Specific threat] | [Severity] | [Effectiveness] |
| Researcher-as-subject | [Specific threat] | [Severity] | [Effectiveness] |

### 8.3 Recommendations for Future Studies

**Guidance:** Based on lessons learned, recommend changes for Pilot 002 or cohort studies.

| Recommendation | Priority | Rationale |
|---------------|----------|-----------|
| [Description] | [high / medium / low] | [Evidence from pilot] |

---

## 9. Limitations

**Guidance:** Comprehensive, honest acknowledgment of limitations.

**Required content:**
- Single-subject design (N = 1)
- Researcher expertise bias
- Platform specificity (Quantic only)
- Self-report bias
- Hawthorne effect
- Duration limitations
- Any additional limitations encountered

**Quality criteria:**
- [ ] All major limitations are acknowledged
- [ ] Impact of each limitation on findings is discussed
- [ ] Limitations are proportionate (neither overstated nor understated)

---

## 10. Conclusions and Implications

### 10.1 Summary of Findings

**Guidance:** 3-5 key takeaways, each backed by evidence.

### 10.2 Implications for CRG-ANL Research Program

**Guidance:** How do these findings inform the broader research program?

- Construct refinements needed
- Taxonomy revisions indicated
- Methodology adjustments for future pilots
- Research questions that emerged

### 10.3 Implications for AI-Native Education

**Guidance:** What do these findings mean for platforms like Quantic?

- Practical recommendations
- Governance gaps identified
- Areas for platform improvement

---

## Appendices

### Appendix A: Codebook Version

**Codebook version used:** [version]  
**Location:** `05_experiments/codebook.md`  
**Key changes during pilot:** [summary]

### Appendix B: Instrument Versions

| Instrument | Version | Changes During Pilot |
|-----------|---------|---------------------|
| NASA-TLX | Standard | None |
| Subjective Scales | v0.1 | [Any changes] |
| Observation Schema | v0.1 | [Any changes] |

### Appendix C: Decision Log Summary

**Reference:** `07_project_operations/decision_log.md`

**Key decisions during Pilot 001:**

| ADR | Decision | Impact |
|-----|----------|--------|
| ADR-00N | [Summary] | [Impact on pilot] |

### Appendix D: Exemplar Observations

**Guidance:** Include 3-5 fully anonymized, representative observations that illustrate key findings.

[Observations with all fields, lightly edited for clarity]

### Appendix E: Data Availability

**Guidance:** Describe what data is available and under what conditions.

- Observation dataset: [location, format, access]
- Session logs: [location, format, access]
- Post-session forms: [location, format, access]
- Analysis scripts: [location, format, access]

---

## Report Checklist

Before marking this report complete:

- [ ] Executive summary written and reviewed
- [ ] All sections have content (no empty placeholders)
- [ ] All tables are populated with actual data
- [ ] All claims are backed by evidence
- [ ] Limitations are honestly acknowledged
- [ ] Claims are proportionate to evidence
- [ ] Cross-references to other artifacts are accurate
- [ ] Decision log references are current
- [ ] Codebook version is recorded
- [ ] Data availability statement is included
- [ ] Report reviewed for internal consistency
- [ ] Known limitations section is honest and complete
