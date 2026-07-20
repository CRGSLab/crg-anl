# 03_evidence: Canonical Research Evidence

**Purpose:**  
This workstream contains all research evidence collected during CRG-ANL studies.
Evidence includes structured observations, coded events, screenshots, field notes, datasets, and analysis exports.
All evidence is organized by study and session for reproducibility.

**Relationships:**  
- `01_science/` provides the study protocol and observation schema that govern evidence collection
- `02_engineering/` provides the schemas and instrumentation specifications for evidence structure
- `05_experiments/` generates the evidence through pilot study execution
- `06_publications/` draws on evidence for findings, figures, and tables

**Inputs:**  
- Researcher observations during learning sessions
- Screenshot captures
- Structured ratings (NASA-TLX, subjective scales)
- Researcher notes and memos

**Outputs:**  
- Validated observation YAML files
- Coded event classifications
- Annotated screenshots
- Structured field notes
- Analysis-ready datasets
- Benchmark result exports

**Ownership:**  
Principal Investigator. Evidence is added by the researcher during data collection and validated through the evaluation pipeline.

---

## Directory Structure

| Directory | Contents | Naming Convention |
|-----------|----------|-------------------|
| `observations/` | Structured observation YAML files | `OBS-{study}-{session}-{sequence}.yaml` |
| `coded_events/` | Event classifications and coding decisions | `{study}_coded_events_{session}.md` |
| `screenshots/` | Annotated screenshot captures | `{session}_{description}_{NNN}.png` |
| `field_notes/` | Researcher notes and memos | `{DATE}_session_{NNN}_notes.md` |
| `datasets/` | Analysis-ready datasets (Parquet, CSV) | `{study}_dataset_{description}.parquet` |
| `analysis_exports/` | Benchmark results and analysis outputs | `{study}_benchmark_{date}.yaml` |

## Evidence Standards

1. **All observations use the canonical schema** defined in `02_engineering/schemas/observation_schema.yaml`
2. **All evidence is timestamped** and linked to a specific study, course, lesson, and session
3. **Screenshots include annotations** with timestamp, observation reference, and description
4. **Field notes are structured** using the prompts defined in the study protocol
5. **Evidence is never modified after deposition** — corrections are made through new observations with references to the original

## Current Evidence

| Study | Status | Sessions | Observations |
|-------|--------|----------|-------------|
| pilot_001 | Awaiting first session | 0 | 0 |
