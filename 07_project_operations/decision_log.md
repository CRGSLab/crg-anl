# Decision Log

**Artifact:** Decision Log  
**Version:** 0.1.0  
**Status:** Active — all future architectural decisions must be recorded here  
**Canonical:** Yes — governs evolution of research infrastructure and methodology  

---

## ADR-001: Repository Structure — Seven Workstreams

**Status:** Accepted  
**Date:** 2026-07-13

### Context

The CRG-ANL Research Program needed a repository structure that supports:
- Canonical scientific knowledge (constructs, taxonomy, glossary)
- Reference implementation design (architecture, schemas, specifications)
- Canonical research evidence (observations, datasets, exports)
- External scientific knowledge (literature, annotations)
- Executable science (pilot protocols, analysis, results)
- Publication pipeline (papers, figures, tables)
- Laboratory management (decisions, changes, governance)

Traditional software project structures (src/, docs/, tests/) are inadequate for a scientific operating system.
Traditional research project structures (papers/, data/, notes/) lack the rigor and organization needed for longitudinal benchmark research.

### Decision

Adopt a seven-workstream structure:

1. `01_science/` — Canonical scientific knowledge
2. `02_engineering/` — Reference implementation design
3. `03_evidence/` — Canonical research evidence
4. `04_literature/` — External scientific knowledge
5. `05_experiments/` — Executable science
6. `06_publications/` — Publication pipeline
7. `07_project_operations/` — Laboratory management

Each workstream has a distinct purpose, defined relationships to other workstreams, specified inputs and outputs, and documented ownership.

### Consequences

**Positive:**
- Clear separation of concerns between scientific knowledge, evidence, and operations
- Each workstream can evolve independently with defined interfaces
- New researchers can understand the program structure quickly
- Directory numbering indicates logical flow from science to operations

**Negative:**
- More complex than a flat directory structure
- Requires discipline to maintain cross-workstream consistency
- Seven top-level directories may feel overwhelming initially

## ADR-002: No Implementation Code in Repository

**Status:** Accepted  
**Date:** 2026-07-13

### Context

The Build Contract (CRGB-BC-001) specifies that this repository is a scientific operating system, not a software project.
The repository must contain production-quality documentation, schemas, and specifications, but not implementation code.

### Decision

The repository contains:
- Documentation (Markdown)
- Schemas (YAML)
- Diagrams (Mermaid)
- Protocols (Markdown)
- Specifications (Markdown)

The repository does NOT contain:
- Implementation code (Python, JavaScript, etc.)
- Generated datasets
- Fake or fabricated observations
- Empty placeholder templates

### Consequences

**Positive:**
- Repository focuses on scientific rigor, not software engineering
- Reduced maintenance burden (no dependency management, testing, CI/CD)
- Artifacts are human-readable and version-control-friendly
- Clear separation between scientific design and potential implementation

**Negative:**
- Analysis must be performed manually or with ad-hoc scripts (not version-controlled here)
- No automated validation of schemas beyond manual review
- Future implementation will require a separate repository

## ADR-003: YAML as Canonical Schema Format

**Status:** Accepted  
**Date:** 2026-07-13

### Context

The observation schema and other data structures need a format that is:
- Human-readable (researchers will write observations by hand)
- Machine-parseable (for future automated processing)
- Version-controllable (clean diffs)
- Self-documenting (comments, structure)

### Decision

Use YAML as the canonical schema and data format.

### Consequences

**Positive:**
- Human-readable and writable
- Supports comments (unlike JSON)
- Clean diffs in version control
- Widely supported by parsing libraries

**Negative:**
- Less compact than JSON
- Parsing can be ambiguous with complex nested structures
- Not as type-safe as Protocol Buffers or Avro

## ADR-004: Semantic Versioning for Scientific Artifacts

**Status:** Accepted  
**Date:** 2026-07-13

### Context

Scientific artifacts (construct definitions, benchmark taxonomy, observation schema) evolve over time as the research program matures.
A versioning scheme is needed to track changes and ensure reproducibility.

### Decision

Use semantic versioning (MAJOR.MINOR.PATCH) for all canonical artifacts:

- **MAJOR:** Fundamental changes to definitions, scope, or structure
- **MINOR:** Additions of new constructs, dimensions, or features
- **PATCH:** Corrections, clarifications, or minor expansions

### Consequences

**Positive:**
- Clear communication of change magnitude
- Reproducibility (know which version produced which results)
- Dependency management (benchmarks reference specific schema versions)

**Negative:**
- Requires discipline to maintain version numbers
- May create confusion when multiple artifacts have different versions

## ADR-005: Observation Schema Field Set

**Status:** Accepted  
**Date:** 2026-07-13

### Context

The observation schema must capture all relevant information about an instructional event while remaining practical for the researcher to complete after each session.
Too many fields create burden; too few fields lose important information.

### Decision

The observation schema contains 16 fields organized into four categories:

**Identity:** observation_id, study, course, lesson, session_number, sequence_number, timestamp
**Classification:** observation_type, runtime_trigger, instructional_integrity_dimension, severity
**Impact:** cognitive_safety_impact, human_agency, shared_responsibility
**Analysis:** evidence_references, research_memo, candidate_intervention, future_benchmark_mapping

Plus embedded NASA-TLX and subjective ratings.

### Consequences

**Positive:**
- Comprehensive coverage of event characteristics
- Direct mapping to benchmark taxonomy dimensions
- Supports both immediate coding and later analytical refinement

**Negative:**
- 16 fields may feel burdensome for rapid event logging
- May require practice to complete efficiently
- Some fields may be rarely used (can be defaulted)

## ADR-006: Quantic as Inaugural Experimental Environment

**Status:** Accepted  
**Date:** 2026-07-13

### Context

The research program requires an AI-native educational environment for the inaugural longitudinal case study.
The environment must be accessible to the researcher, exhibit AI-mediated instruction, and provide sufficient instructional events for meaningful observation.

### Decision

Select the Quantic School of Business and Technology's MS in Artificial Intelligence Engineering program as the inaugural experimental environment (Case Study 001 / Pilot 001).

Rationale:
- Mobile-first, AI-enhanced delivery
- Researcher is an enrolled student with legitimate access
- Diverse curriculum spanning foundational to advanced AI topics
- Self-paced structure enables controlled session timing
- Professional audience relevant for enterprise training research

### Consequences

**Positive:**
- Immediate access to experimental environment
- Rich, diverse instructional content
- Longitudinal design supported by multi-course curriculum

**Negative:**
- Findings are specific to one platform
- Platform may change during the study period
- Single-subject design limits generalizability
- Mobile-first interface may have unique cognitive safety characteristics

## ADR-007: Mermaid for Diagrams

**Status:** Accepted  
**Date:** 2026-07-13

### Context

The research program requires diagrams for architecture, data flow, taxonomy, and timelines.
Diagrams must be:
- Version-controllable (text-based, not binary)
- Editable without specialized software
- Renderable in multiple contexts (GitHub, documentation, publications)

### Decision

Use Mermaid as the canonical diagram format.

### Consequences

**Positive:**
- Text-based (version-controllable)
- Rendered natively by GitHub and many documentation platforms
- No external tools required
- Wide variety of diagram types

**Negative:**
- Limited styling options compared to dedicated tools
- Complex diagrams can become unwieldy in text format
- Not all diagram types are supported
