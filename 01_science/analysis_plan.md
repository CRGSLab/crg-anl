# Analysis Plan

**Artifact:** Analysis Plan  
**Version:** 0.1.0 (Draft)  
**Status:** Draft — analytical procedures will be refined after initial data collection  
**Canonical:** Yes — governs all data analysis  

---

## Overview

This document specifies the analytical approach for the CRG-ANL Research Program.
It covers qualitative coding, quantitative analysis, and triangulation strategies for the researcher-as-subject longitudinal design.

## Known Limitations (Draft v0.1)

- Analytical procedures are specified at a conceptual level; detailed statistical models will be developed once data characteristics are known
- Software implementation details (R, Python packages) are not specified — the focus is on analytical logic
- Power analyses in `hypotheses.md` assume effect sizes that may be revised after pilot data
- The single-subject design limits inferential statistics; emphasis is on descriptive and visual analysis

---

## Qualitative Coding Approach

### Coding Framework

Qualitative data (structured research notes, research memos, screenshot annotations) will be coded using a hybrid approach:

1. **Deductive coding:** Apply codes derived from the CRG-ANL construct ontology and benchmark taxonomy
2. **Inductive coding:** Allow emergent codes to arise from the data
3. **Axial coding:** Identify relationships between codes and constructs

### Code Hierarchy

```
CRG (top-level)
├── Cognitive_Safety
│   ├── Overload
│   ├── Confusion
│   ├── Frustration
│   ├── Attention_Loss
│   └── Metacognitive_Disruption
├── Instructional_Integrity
│   ├── Content_Error
│   ├── Inconsistency
│   ├── Assessment_Invalidity
│   ├── Feedback_Failure
│   └── Prerequisite_Violation
├── Learner_Agency
│   ├── Goal_Override
│   ├── Strategy_Limitation
│   ├── Choice_Absence
│   └── Auto_Advance
├── Human_AI_Shared_Responsibility
│   ├── Opaque_Adaptivity
│   ├── Hidden_Optimization
│   ├── Uncertainty_Unmarked
│   └── Responsibility_Unclear
├── Transition_Integrity
│   ├── Abrupt_Change
│   ├── Missing_Bridge
│   ├── Context_Loss
│   └── Agency_Bypass
└── Emergent_Codes
    ├── [to be populated from data]
```

### Coding Procedure

1. **First pass — deductive:** Code all data using the pre-defined code hierarchy
2. **Second pass — inductive:** Identify passages that do not fit existing codes; generate emergent codes
3. **Third pass — axial:** Map relationships between codes; identify patterns and themes
4. **Review:** Revisit earlier sessions with refined codebook; assess code stability

### Codebook Maintenance

The codebook is a living document stored in `05_experiments/codebook.md`.
It is updated after every 5 sessions to incorporate new emergent codes and refine existing definitions.
All codebook changes are documented in `07_project_operations/change_log.md`.

---

## Quantitative Analysis

### Analysis Levels

| Level | Unit of Analysis | Methods |
|-------|-----------------|---------|
| **Event level** | Individual observations | Descriptive statistics, severity distributions |
| **Session level** | Single learning session | Summary statistics, NASA-TLX profiles, subjective scale profiles |
| **Weekly level** | 1 week of sessions | Trend detection, preliminary benchmarks |
| **Monthly level** | 1 month of sessions | Full benchmark application, longitudinal trends |
| **Phase level** | Course phase (orientation, core, etc.) | Comparative analysis across phases |
| **Study level** | Full pilot | Comprehensive synthesis, publication-ready analysis |

### Descriptive Analysis

For all quantitative data:

- **Distributions:** Histograms and density plots for all continuous variables
- **Central tendency:** Means, medians, and modes with confidence intervals
- **Variability:** Standard deviations, ranges, interquartile ranges
- **Temporal patterns:** Time-series plots of key metrics across sessions

### Benchmark Score Calculation

Benchmark scores are computed according to the aggregation rules defined in `01_science/benchmark_taxonomy.md`:

```
Step 1: Normalize severity scores (1–5) to 0–1 scale: score = (severity - 1) / 4
Step 2: Compute sub-dimension scores as mean of normalized severities
Step 3: Compute primary dimension scores as weighted mean of sub-dimensions
Step 4: Compute overall governance score as weighted mean of primary dimensions
Step 5: Classify using severity thresholds (Excellent ≥ 0.80, Good ≥ 0.60, etc.)
```

### Time-Series Analysis

For longitudinal data:

- **Trend detection:** Visual inspection of score trajectories over time
- **Change point analysis:** Identify sessions where benchmark scores shift significantly
- **Rolling averages:** 3-session and 5-session moving averages to smooth noise
- **Session-to-session change:** First-differencing to identify volatility

### Correlational Analysis

For exploring relationships between variables:

- **Bivariate correlations:** Pearson or Spearman correlations between:
  - NASA-TLX mental demand and Cognitive Safety scores
  - Subjective agency ratings and Learner Agency scores
  - Instructional Integrity scores and perceived clarity ratings
  - Transition Integrity scores and session completion rates
- **Cross-lag analysis:** Explore whether governance scores at session N predict experience outcomes at session N+1

### Single-Subject Experimental Design

Given the N-of-1 design, the following approaches are employed:

- **Visual analysis:** Primary method — inspect graphs for trends, level changes, and variability
- **Percentage of non-overlapping data (PND):** Compare baseline vs. intervention phases (if applicable)
- **Tau-U:** Non-overlap effect size for single-subject data
- **Celeration lines:** Track rate of change over time

### Inferential Statistics (Cautious Application)

Where sample size permits (e.g., across many sessions or many observations):

- **Mixed-effects models:** Account for nesting of observations within sessions
- **Generalized estimating equations (GEE):** For repeated measures with binary outcomes
- **Survival analysis:** Time-to-event analysis (e.g., time to first confusion episode)

These are applied cautiously, with explicit acknowledgment of the single-subject limitation.

---

## Triangulation Strategy

### Data Source Triangulation

| Source | What It Captures | Complementarity |
|--------|-----------------|----------------|
| Observation YAML | Objective event coding | Factual record of instructional actions |
| NASA-TLX | Subjective cognitive load | Internal state not visible in observations |
| Subjective scales | Perceived experience | Affective and evaluative responses |
| Research notes | Qualitative reflection | Context, interpretation, meaning-making |
| Screenshots | Visual evidence | Objective capture of AI outputs and interfaces |

### Methodological Triangulation

| Method | Purpose | Convergence Check |
|--------|---------|-------------------|
| Quantitative (benchmarks) | Measure prevalence and severity | Do benchmark scores correlate with subjective ratings? |
| Qualitative (coding) | Understand mechanisms | Do coded themes explain quantitative patterns? |
| Visual (screenshots) | Verify claims | Do screenshots support observation codes? |
| Self-report (scales) | Capture internal states | Do self-reports align with objective indicators? |

### Triangulation Procedure

1. Compute quantitative benchmark scores
2. Code qualitative data for corresponding themes
3. Compare: Do high Cognitive Safety scores align with low confusion codes?
4. Compare: Do low Instructional Integrity scores align with high frustration ratings?
5. Where sources disagree, investigate: Is the discrepancy due to measurement error, construct validity issues, or genuine complexity?
6. Document convergence and divergence in research memos

---

## Visualization Strategy

### Standard Visualizations

| Visualization | Purpose | Update Frequency |
|--------------|---------|-----------------|
| Benchmark score time series | Track governance scores over sessions | Monthly |
| Severity distribution bar chart | Show frequency of each severity level | Monthly |
| NASA-TLX profile radar chart | Compare workload dimensions | Weekly |
| Subjective scales heatmap | Show rating patterns across sessions | Monthly |
| Transition integrity flow diagram | Visualize transition success/failure | Monthly |
| Observation type frequency chart | Show what events are most common | Weekly |

### Publication Visualizations

| Visualization | Publication Use |
|--------------|-----------------|
| Longitudinal benchmark trajectory | Empirical papers (P3, P4, P5) |
| Construct-to-outcome DAG | Conceptual paper (P1) |
| Severity distribution by dimension | All empirical papers |
| Correlation matrix | Methodology paper (P2) |
| Session-level dashboard | Technical reports |

---

## Maturity Path

This artifact advances from Draft to Stable when:
- [ ] Pilot data (n ≥ 10 sessions) has been analyzed using the specified procedures
- [ ] Codebook has stabilized (no new emergent codes in 2 consecutive updates)
- [ ] Triangulation convergence rates have been computed
- [ ] Visualization templates have been validated for clarity and accuracy
- [ ] Publication-ready analysis scripts have been documented
