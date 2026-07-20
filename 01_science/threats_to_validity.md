# Threats to Validity

**Artifact:** Threats to Validity  
**Version:** 0.1.0 (Draft)  
**Status:** Draft — threat assessment will be updated after initial pilot data  
**Canonical:** Yes — governs validity protection strategies  

---

## Overview

This document identifies threats to the validity of the CRG-ANL Research Program and specifies mitigation strategies.
It addresses both standard validity categories (internal, external, construct, statistical conclusion) and threats specific to the researcher-as-subject methodology and single-program context.

## Known Limitations (Draft v0.1)

- Threat assessments are based on anticipated risks; empirical verification requires pilot data
- Some threats (e.g., Hawthorne effect) cannot be fully eliminated in a researcher-as-subject design, only minimized
- Mitigation effectiveness will be assessed through the bias audit protocol defined in `01_science/study_protocol.md`

---

## Internal Validity Threats

Internal validity concerns whether observed relationships between instructional events and student experience outcomes are causal rather than spurious.

| Threat | Description | Risk Level | Mitigation Strategy |
|--------|-------------|------------|---------------------|
| **History effects** | External events (platform updates, personal circumstances) confound session outcomes | Medium | Document all external events in session metadata; include as covariates in analysis |
| **Maturation** | The researcher improves as a learner over time, independently of instructional quality | High | Track learning curve separately from governance effects; use within-session comparisons where possible |
| **Testing effects** | Repeated measurement (NASA-TLX, scales) sensitizes the researcher to the constructs being measured | Medium | Vary item wording occasionally; include attention checks; assess scale stability over time |
| **Instrumentation drift** | Observation coding criteria change over time as the researcher gains experience | Medium | Review and recode early sessions with refined criteria; document coding evolution |
| **Regression to the mean** | Extreme scores on early sessions tend to normalize, creating artificial trends | Low | Use multiple measurements per session; avoid over-interpreting single extreme values |
| **Selection bias** | The researcher selectively records or remembers certain types of events | Medium | Structured observation schema with required fields; code all events meeting criteria |

## External Validity Threats

External validity concerns whether findings generalize beyond the specific researcher, platform, and context.

| Threat | Description | Risk Level | Mitigation Strategy |
|--------|-------------|------------|---------------------|
| **Single subject** | Findings may not generalize to other learners with different cognitive profiles, prior knowledge, or learning preferences | High | Acknowledge explicitly in all publications; document researcher characteristics in detail; design Pilot 002 for cross-subject validation |
| **Single platform** | Findings are specific to Quantic's mobile-first, AI-generated content model | High | Acknowledge explicitly; design Pilot 002 for cross-platform validation; compare findings to published evaluations of other platforms |
| **Expert learner** | The researcher's expertise may make them more sensitive to instructional errors than typical learners | Medium | Document expertise level; note that sensitivity to errors is a methodological advantage for integrity detection; Pilot 002 with non-expert subject would test generalizability |
| **Self-selection** | The researcher chose this program and is motivated to study it, potentially biasing engagement | Low | Document motivation levels; acknowledge that engagement may be higher than average |
| **Time-bound context** | AI systems evolve rapidly; findings may not generalize to future versions | Medium | Document platform version and date for all observations; acknowledge temporal limitations |

## Construct Validity Threats

Construct validity concerns whether the measures accurately represent the theoretical constructs they claim to measure.

| Threat | Description | Risk Level | Mitigation Strategy |
|--------|-------------|------------|---------------------|
| **Mono-method bias** | Over-reliance on self-report measures for Cognitive Safety and Agency | Medium | Triangulate self-report with objective indicators (timing, error rates, screenshot evidence) |
| **Mono-operation bias** | Each construct measured by only one instrument type | Medium | Use multiple items per construct; combine observation coding, self-report, and objective indicators |
| **Construct underrepresentation** | The observation schema may miss important instructional events | Medium | Include "other" observation type; inductive coding allows emergent categories; schema reviewed after every 5 sessions |
| **Construct-irrelevant variance** | Measures capture phenomena unrelated to the target construct | Low | Content validation of all items against construct definitions; expert review of observation codes |
| **Halo effects** | Overall impression of the session influences specific ratings | Medium | Separate rating administration (NASA-TLX before subjective scales); include negative-item variants |

## Statistical Conclusion Validity Threats

Statistical conclusion validity concerns whether statistical analyses produce accurate conclusions.

| Threat | Description | Risk Level | Mitigation Strategy |
|--------|-------------|------------|---------------------|
| **Low statistical power** | Single-subject design may lack power to detect effects | High | Use visual analysis as primary method; apply effect sizes (Cohen's d, Tau-U) rather than p-values; report confidence intervals where possible |
| **Violated assumptions** | Parametric tests may violate normality, independence, or homogeneity assumptions | Medium | Use non-parametric alternatives; bootstrap confidence intervals; explicitly test assumptions |
| **Fishing and error rate inflation** | Multiple comparisons increase Type I error risk | Medium | Pre-register primary analyses; distinguish confirmatory from exploratory; apply Bonferroni or FDR corrections for exploratory analyses |
| **Unreliability of measures** | Self-report and observation coding may have low reliability | Medium | Assess inter-rater reliability (if independent coding possible); assess test-retest reliability; use multiple indicators per construct |
| **Restriction of range** | Single subject may show limited variability on some measures | Medium | Use within-session variability; track session-to-session change rather than absolute levels |

## Researcher-as-Subject Specific Threats

These threats are unique to the researcher-as-subject methodology.

| Threat | Description | Risk Level | Mitigation Strategy |
|--------|-------------|------------|---------------------|
| **Confirmation bias** | Researcher notices and records evidence supporting prior expectations | High | Pre-register hypotheses; document all expectations before data collection; adversarial review of conclusions; seek disconfirming evidence |
| **Hawthorne effect** | Being observed (even by self) changes learning behavior | Medium | Normalize observation through practice; compare early vs. late sessions for adaptation; acknowledge in limitations |
| **Expectancy effects** | Researcher's expectations about the platform influence observations and ratings | High | Document all prior expectations; blinded analysis where possible; compare observations against objective evidence (screenshots, logs) |
| **Demand characteristics** | Researcher unconsciously produces data that confirms the study's aims | Medium | Use structured observation schema to constrain subjective flexibility; include "other" category for unexpected events |
| **Expertise bias** | Domain expertise makes researcher more critical (or more forgiving) than typical learners | Medium | Document expertise level; compare ratings to objective indicators; acknowledge in limitations |
| **Emotional investment** | Researcher's personal stake in the program affects emotional ratings | Medium | Include emotion-neutral items; track emotional investment as a covariate; acknowledge in limitations |
| **Recall bias** | Memory of past sessions degrades or is selectively reconstructed | Low | Record observations immediately after sessions; use structured templates; never rely on memory for coding |

## Single-Program Context Threats

These threats arise from studying only one educational program.

| Threat | Description | Risk Level | Mitigation Strategy |
|--------|-------------|------------|---------------------|
| **Platform-specific effects** | Quantic's mobile-first, micro-learning format may produce unique cognitive safety patterns | Medium | Document platform characteristics in detail; compare findings to published research on other platforms; design Pilot 002 for cross-platform validation |
| **Curriculum-specific effects** | AI Engineering curriculum may have unique integrity challenges compared to other subjects | Low | Document curriculum structure; compare integrity patterns across topics (foundational vs. advanced); acknowledge subject-specific limitations |
| **Cohort effects** | The researcher is part of a specific cohort with specific platform version and features | Low | Document platform version for all sessions; track platform updates as potential confounds |
| **Temporal confounds** | Platform may update during the study, confounding longitudinal trends | Medium | Document all platform updates; include version as covariate; analyze pre/post-update data separately |

## Mitigation Effectiveness Assessment

The effectiveness of all mitigation strategies is assessed through:

1. **Bias audit protocol** (monthly): Review observations for confirmation bias, expectancy effects, and selective recording
2. **Protocol fidelity audit** (monthly): Assess compliance with observation and coding procedures
3. **Triangulation check** (monthly): Compare self-report, observation, and objective indicators for convergence
4. **Adversarial review** (quarterly): Independent critique of methods, findings, and conclusions

Results of all validity assessments are documented in `07_project_operations/meeting_notes.md`.

---

## Maturity Path

This artifact advances from Draft to Stable when:
- [ ] Pilot data (n ≥ 10 sessions) has been analyzed for evidence of each threat
- [ ] Mitigation effectiveness has been empirically assessed
- [ ] Threat assessment has been updated with observed (not just anticipated) risks
- [ ] Bias audit results have been incorporated
- [ ] Publication reviewers have validated the threat analysis
