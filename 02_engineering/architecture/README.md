# Architecture

**Purpose:**  
System architecture specifications for the CRG-ANL reference implementation, describing components, interactions, data flows, and design decisions.

**Relationships:**  
- Informed by constructs in `01_science/construct_definitions.md`
- Guides benchmark engine design in `../benchmark_engine/`
- Guides pipeline design in `../evaluation_pipeline/`
- Governed by decision log in `07_project_operations/decision_log.md`

**Inputs:**  
- Construct definitions, benchmark taxonomy, observation schema requirements

**Outputs:**  
- Architecture diagrams, component specifications, data flow documentation

---

## System Overview

The CRG-ANL reference implementation is designed as a modular scientific data pipeline that transforms raw instructional observations into structured evidence, benchmark scores, and research outputs.

```mermaid
graph LR
    subgraph Input
        O[Observations<br/>YAML files]
        M[Metadata<br/>Session info]
        S[Subjective Ratings<br/>NASA-TLX, scales]
    end

    subgraph Processing
        V[Schema Validator]
        C[Coder<br/>Event classification]
        B[Benchmark Engine]
    end

    subgraph Output
        R[Benchmark Results<br/>Scores, severity]
        D[Datasets<br/>Parquet, CSV]
        F[Figures<br/>Visualizations]
        Rep[Reports<br/>Markdown]
    end

    O --> V
    M --> V
    S --> V
    V --> C
    C --> B
    B --> R
    B --> D
    R --> F
    R --> Rep
```

## Components

### 1. Schema Validator

Validates all observation YAML files against the canonical observation schema.
Ensures data integrity before processing.

**Responsibilities:**
- Validate YAML syntax
- Validate required fields
- Validate field types and ranges
- Validate cross-field consistency
- Report validation errors with line numbers

### 2. Event Coder

Classifies raw observations into the benchmark taxonomy dimensions.
Assigns severity ratings and maps observations to benchmark dimensions.

**Responsibilities:**
- Classify observation_type against taxonomy
- Map observations to instructional_integrity_dimension
- Assess cognitive_safety_impact
- Evaluate human_agency and shared_responsibility
- Assign severity ratings

### 3. Benchmark Engine

Executes benchmark calculations across all dimensions of the taxonomy.
Aggregates sub-dimension scores into primary dimension scores and overall governance scores.

**Responsibilities:**
- Load coded observations
- Calculate sub-dimension scores
- Aggregate to primary dimension scores
- Calculate overall governance score
- Generate severity distributions
- Produce benchmark reports

### 4. Visualization Generator

Produces publication-ready figures from benchmark results.

**Responsibilities:**
- Generate score charts (bar, radar, time series)
- Generate severity distribution charts
- Generate correlation matrices
- Generate longitudinal trend plots
- Export in publication formats (PNG, SVG, PDF)

### 5. Report Generator

Produces structured research reports from benchmark results and evidence.

**Responsibilities:**
- Generate session reports
- Generate weekly summary reports
- Generate monthly benchmark reports
- Generate pilot study reports
- Export in Markdown format

## Data Flow

```mermaid
sequenceDiagram
    participant R as Researcher
    participant O as Observation YAML
    participant V as Schema Validator
    participant C as Event Coder
    participant B as Benchmark Engine
    participant D as Dataset
    participant Rep as Report

    R->>O: Write observation after session
    O->>V: Validate
    V-->>O: Validation result
    O->>C: Code event
    C->>B: Coded observations
    B->>B: Calculate scores
    B->>D: Export results
    B->>Rep: Generate report
    Rep-->>R: Review findings
```

## Design Principles

1. **Schema-first:** All data structures are defined in YAML schemas before any processing
2. **Reproducible:** Every transformation is deterministic and version-controlled
3. **Extensible:** New benchmark dimensions can be added without modifying existing code
4. **Transparent:** All processing steps are documented and inspectable
5. **Minimal:** The simplest design that satisfies the scientific requirements
