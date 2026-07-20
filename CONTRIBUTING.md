# Contributing to CRG-ANL

The CRG-ANL Research Program welcomes contributions that advance the scientific mission of evaluating and improving Constitutional Runtime Governance in AI-native educational systems.

---

## What We Accept

| Contribution Type | Location | Requirements |
|------------------|----------|-------------|
| **Scientific critique** | Issues or Discussions | Must reference specific constructs, definitions, or evidence |
| **Construct refinement** | `01_science/construct_definitions.md` | Must include definition, theoretical motivation, relationships, and example observations |
| **Benchmark taxonomy expansion** | `01_science/benchmark_taxonomy.md` | Must include parent dimension, operational definition, and measurement approach |
| **Literature annotations** | `04_literature/annotated_bibliography/` | Must include full citation, summary, relevance to CRG-ANL constructs, and critical assessment |
| **Observation schema evolution** | `02_engineering/schemas/` | Must be backward-compatible or include migration rationale |
| **Decision records** | `07_project_operations/decision_log.md` | Must use ADR format with context, decision, consequences |
| **Pilot protocol feedback** | `05_experiments/pilot_001/` | Must reference specific protocol sections |

## What We Do Not Accept

- Implementation code (this is a scientific operating system, not a software project)
- Fabricated observations or datasets
- Empty placeholder files or TODOs without substantive content
- Contributions without production-quality documentation

## Draft Artifacts

New artifacts may be contributed as **Draft v0.1** documents that are structurally complete but explicitly mark provisional content in a **Known Limitations** section.
A Draft artifact must contain:
- Complete structure and all required sections
- Explicit "Known Limitations" section documenting what is provisional
- A maturity path describing what evidence or review is needed to advance to Stable status

Draft artifacts are not "placeholders" — they are complete, usable documents that acknowledge their own provisional status.

## Contribution Process

1. **Open an issue** describing the proposed contribution and its scientific rationale
2. **Reference relevant constructs** and existing artifacts
3. **Await maintainer review** before submitting changes
4. **Follow engineering standards**: Markdown, YAML, Mermaid, semantic line breaks
5. **Ensure every new directory has a README** with purpose, relationships, inputs, outputs, and ownership

## Style Guidelines

### Markdown
- One sentence per line (semantic line breaks)
- Use ATX-style headings (`#` not `===`)
- Prefer tables for structured comparisons
- Use Mermaid for all diagrams

### YAML
- 2-space indentation
- Consistent key ordering within files
- Comments explaining non-obvious values

### Scientific Writing
- Define terms on first use
- Distinguish between established claims and hypotheses
- Cite relevant literature where applicable
- Distinguish between normative (should) and descriptive (is) claims

## Contact

For questions about the research program: open a Discussion.  
For bug reports in documentation: open an Issue.  
For private inquiries: [researcher-email@domain.com]
