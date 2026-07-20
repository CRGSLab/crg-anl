# 01_science: Canonical Scientific Knowledge

**Purpose:**  
This workstream contains the foundational scientific knowledge of the CRG-ANL Research Program.
Every artifact herein is canonical — it represents the current best understanding of the constructs, questions, hypotheses, and methods that define the research agenda.

**Relationships:**  
- `02_engineering/` implements the designs specified by schemas and protocols defined here
- `03_evidence/` populates observations structured according to the observation schema defined here
- `04_literature/` informs and is informed by the construct definitions and research questions here
- `05_experiments/` executes protocols derived from the study protocol defined here
- `06_publications/` communicates findings framed by the research program and questions defined here
- `07_project_operations/` governs the evolution of all artifacts in this workstream

**Inputs:**  
- Scholarly literature (via `04_literature/`)
- Pilot study evidence (via `05_experiments/`)
- Peer review and scientific critique (via Issues and Discussions)

**Outputs:**  
- Construct definitions that constrain and shape all downstream research
- Research questions that guide evidence collection
- Hypotheses that structure analytical inquiry
- Benchmark taxonomy that organizes evaluation
- Study protocol that governs data collection
- Glossary that standardizes terminology

**Ownership:**  
Principal Investigator, with construct definitions subject to peer review before major version increments.

---

## Artifacts

| Artifact | File | Description |
|----------|------|-------------|
| Research Program | `research_program.md` | Mission, vision, themes, student experience model section, scientific scope, long-term roadmap |
| Student Experience Model | `student_experience_model.md` | Standalone 4-layer SX model with causal graph, construct mappings, operationalization path |
| Research Questions | `research_questions.md` | Central and subsidiary research questions organized by construct |
| Hypotheses | `hypotheses.md` | Testable hypotheses with operationalizations, construct→proxy→direction mappings, and adjudication plans |
| Construct Definitions | `construct_definitions.md` | Canonical definitions of all 11 core constructs |
| Benchmark Taxonomy | `benchmark_taxonomy.md` | Hierarchical evaluation framework with operational definitions |
| Measures and Instruments | `measures_and_instruments.md` | Survey items, scales, reflection prompts, and event instrumentation mapping |
| Analysis Plan | `analysis_plan.md` | Qualitative coding approach, quantitative methods, triangulation strategy |
| Threats to Validity | `threats_to_validity.md` | Validity threats and mitigation strategies for researcher-as-subject design |
| Publication Roadmap | `publication_roadmap.md` | Planned publications with venues, timelines, and dependencies |
| Study Protocol | `study_protocol.md` | Researcher-as-subject protocol for the Quantic longitudinal study |
| Research Glossary | `research_glossary.md` | Standardized terminology with definitions and cross-references |

## Observation Schema

The canonical observation schema is a scientific artifact jointly maintained by `01_science/` and `02_engineering/`.
The authoritative version resides at `02_engineering/schemas/observation_schema.yaml` and is referenced here because it defines the structure of all evidence collected in the research program.
Changes to the observation schema require scientific review (from this workstream) and are versioned according to the schema's own version number.

## Versioning

Scientific artifacts in this workstream follow semantic versioning:

- **Major (X.0.0):** Fundamental changes to construct definitions, research questions, or scope
- **Minor (x.Y.0):** Additions of new constructs, questions, or analytical frameworks
- **Patch (x.y.Z):** Corrections, clarifications, or expansions of existing content

Current version: **0.1.0** (foundation complete, subject to refinement through pilot studies)
