# 07_project_operations: Laboratory Management

**Purpose:**  
This workstream contains all operational documentation for managing the CRG-ANL Research Program: decision logs, change logs, meeting notes, roadmaps, and governance documentation.

**Relationships:**  
- Governs the evolution of all artifacts across all workstreams
- Documents the rationale for architectural and methodological decisions
- Records project status and future plans

**Inputs:**  
- Decisions made during research execution
- Changes to protocols, schemas, or constructs
- Meeting discussions and outcomes

**Outputs:**  
- Decision records (ADR format)
- Change logs
- Meeting notes
- Updated roadmaps
- Governance documentation

---

## Artifacts

| Artifact | File | Purpose |
|----------|------|---------|
| Decision Log | `decision_log.md` | ADR-style records of all architectural and methodological decisions |
| Change Log | `change_log.md` | Record of changes to canonical artifacts with rationale |
| Meeting Notes | `meeting_notes.md` | Notes from research meetings, discussions, and reviews |
| Roadmap | `roadmap.md` | Current and planned research activities with timelines |
| Governance | `governance.md` | Project governance structure, roles, and processes |

## Decision Log Format

All decisions follow the Architecture Decision Record (ADR) format:

```markdown
# ADR-NNN: Decision Title

## Status
Proposed / Accepted / Deprecated / Superseded

## Context
What is the issue that we're seeing that is motivating this decision?

## Decision
What is the change that we're proposing or have agreed to?

## Consequences
What becomes easier or more difficult to do and any risks introduced?
```

## Change Log Format

All changes to canonical artifacts are recorded with:
- Date
- Artifact affected
- Change description
- Rationale
- Impact assessment
