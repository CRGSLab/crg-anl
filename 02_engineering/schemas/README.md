# Schemas

**Purpose:**  
Canonical data schemas in YAML format that define the structure of all research data in the CRG-ANL program.

**Relationships:**  
- Implements data structures required by constructs in `01_science/`
- Used by the benchmark engine in `../benchmark_engine/`
- Governed by the observation protocol in `01_science/study_protocol.md`

---

## Available Schemas

| Schema | File | Description |
|--------|------|-------------|
| Observation | `observation_schema.yaml` | Canonical observation record |
| Session | `session_schema.yaml` | Session metadata and summary |
| Experiment | `experiment_schema.yaml` | Study-level metadata |
| Benchmark Result | `benchmark_result_schema.yaml` | Benchmark output structure |

## Schema Design Principles

1. **YAML format:** Human-readable and machine-parseable
2. **Required vs optional:** Clear distinction between mandatory and optional fields
3. **Validation rules:** Type constraints, range checks, enum values
4. **Extensibility:** New fields can be added without breaking existing data
5. **Versioning:** Each schema includes a version number
