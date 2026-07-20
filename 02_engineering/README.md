# 02_engineering: Reference Implementation Design

**Purpose:**  
This workstream contains the design specifications, architecture documentation, and schema definitions for the CRG-ANL reference implementation.
It describes how the scientific concepts defined in `01_science/` would be operationalized in software, without containing implementation code.

**Relationships:**  
- `01_science/` provides the constructs, taxonomy, and protocol that engineering designs must support
- `03_evidence/` receives data structured according to the schemas defined here
- `05_experiments/` executes protocols using the instrumentation specifications defined here
- `06_publications/` presents figures and tables generated according to the visualization specifications defined here

**Inputs:**  
- Construct definitions from `01_science/construct_definitions.md`
- Benchmark taxonomy from `01_science/benchmark_taxonomy.md`
- Observation schema requirements from `01_science/study_protocol.md`

**Outputs:**  
- Architecture specifications describing system components and interactions
- Benchmark engine design documenting how benchmarks would be executed
- Instrumentation specifications for data collection tools
- Learner Cockpit design specifications
- Evaluation pipeline design documenting automated analysis workflows
- Canonical schemas in YAML format for all data structures
- Runtime governance design documenting constitutional constraint enforcement

**Ownership:**  
Principal Investigator and Engineering Lead, with schema changes subject to scientific review.

---

## Important Clarification: Architecture and Specifications Only

**02_engineering/ contains architecture documents, design specifications, interface contracts, and data schemas only.**
It does not contain implementation code, executable scripts, compiled binaries, or runnable software.
The Build Contract (CRGB-BC-001) explicitly states: "Do not write implementation code."

All content in this workstream is documentation — specifications that describe how a reference implementation would be structured, what interfaces it would expose, and what data contracts it would honor.
If implementation is pursued in the future, it will reside in a separate repository.

## Subdirectories

| Directory | Contents |
|-----------|----------|
| `architecture/` | System architecture specifications, component diagrams, interaction models |
| `benchmark_engine/` | Benchmark engine design: registry, execution, scoring, aggregation |
| `instrumentation/` | Data collection tool specifications: observation recorder, rating interfaces, capture protocols |
| `learner_cockpit/` | Learner Cockpit design: information architecture, display specifications, interaction patterns |
| `evaluation_pipeline/` | Pipeline design: stages, data flow, transformation specifications, report generation |
| `schemas/` | Canonical YAML schemas: observation, session, experiment, benchmark result, governance metric |
| `runtime_governance/` | Runtime governance design: constitutional rules, violation detection, intervention specifications |
