# Data Management Plan

**Artifact:** Data Management Plan (DMP)  
**Version:** 0.1.0 (Draft)  
**Status:** Draft — storage and access procedures will be refined after infrastructure setup  
**Canonical:** Yes — governs all research data  

---

## Overview

This document specifies how research data is collected, stored, managed, shared, and retained in the CRG-ANL Research Program.
It applies to all data in the `03_evidence/` workstream and any associated materials.

## Known Limitations (Draft v0.1)

- Specific storage infrastructure (cloud provider, local server) is not yet finalized
- Sharing policy depends on IRB determination and platform terms of service
- Retention periods are proposed defaults and may be adjusted based on institutional requirements

---

## Data Inventory

### What Data Is Collected

| Data Type | Format | Location | Retention Class |
|-----------|--------|----------|-----------------|
| Observation YAML files | YAML | `03_evidence/observations/` | long_term_7yr |
| Coded event classifications | Markdown | `03_evidence/coded_events/` | long_term_7yr |
| Screenshots | PNG | `03_evidence/screenshots/` | long_term_7yr |
| Researcher field notes | Markdown | `03_evidence/field_notes/` | long_term_7yr |
| NASA-TLX ratings | YAML (embedded in observations) | `03_evidence/observations/` | long_term_7yr |
| Subjective scale ratings | YAML (embedded in observations) | `03_evidence/observations/` | long_term_7yr |
| Session summaries | YAML | `03_evidence/observations/` | long_term_7yr |
| Analysis datasets | Parquet, CSV | `03_evidence/datasets/` | medium_term_3yr |
| Benchmark results | YAML | `03_evidence/analysis_exports/` | medium_term_3yr |
| Monthly reports | Markdown | `05_experiments/pilot_001/monthly_reports/` | medium_term_3yr |
| Decision records | Markdown | `07_project_operations/` | permanent |
| Research memos | Markdown | `03_evidence/field_notes/` | long_term_7yr |

### What Data Is NOT Collected

- Personal information about other students
- Platform authentication credentials
- Financial or payment information
- Health information beyond self-reported cognitive states
- Biometric data

## Storage

### Local Storage

All raw data is stored on encrypted local storage:
- **Device:** Researcher's primary computer
- **Encryption:** Full-disk encryption ( FileVault / BitLocker / LUKS)
- **Backup:** Encrypted external drive, updated weekly
- **Access:** Password-protected user account; screen lock after 5 minutes of inactivity

### Repository Storage

Version-controlled artifacts (observation schemas, protocols, reports) are stored in the Git repository:
- **Platform:** GitHub (private repository during active research)
- **Access:** Principal Investigator only during single-subject phase; contributors added with explicit permission
- **Exclusions:** Raw evidence directories (screenshots, datasets) are gitignored; only schemas and reports are version-controlled

### Cloud Storage (Future)

If cloud storage is adopted for backup or collaboration:
- **Provider:** TBD (must support end-to-end encryption)
- **Encryption:** Client-side encryption before upload
- **Access:** Multi-factor authentication; access logging
- **Jurisdiction:** Data stored in jurisdiction compatible with research institution

## Access Controls

### Access Levels

| Level | Role | Permissions |
|-------|------|-------------|
| **Owner** | Principal Investigator | Full read, write, delete, share |
| **Contributor** | Approved research collaborator | Read, write (observations, notes); no delete |
| **Reviewer** | Peer reviewer, auditor | Read only (anonymized data) |
| **Public** | General public | Read only (published datasets, reports) |

### Authentication

- All access requires authenticated login
- Strong passwords (minimum 12 characters, mixed case, symbols)
- Multi-factor authentication for cloud access
- Access logs maintained for all data access

## Sharing Policy

### What Can Be Shared

| Data | Sharing Condition | Format |
|------|-------------------|--------|
| Observation schemas | Always | YAML |
| Benchmark taxonomy | Always | Markdown |
| Construct definitions | Always | Markdown |
| Anonymized benchmark scores | After pilot completion | CSV, YAML |
| Anonymized NASA-TLX profiles | After pilot completion | CSV |
| De-identified observation excerpts | After pilot completion | Markdown |
| Research reports | After internal review | Markdown, PDF |
| Full dataset | IRB approval + platform permission | Structured archive |

### What Cannot Be Shared

- Screenshots containing platform proprietary content (without permission)
- Raw observation YAML with embedded subjective ratings (without de-identification)
- Any data that could identify the researcher (if anonymity is requested)
- Any data covered by platform terms of service restrictions

### Licensing

- Research data: CC-BY 4.0 (where ethically and legally permissible)
- Research infrastructure: MIT License
- Platform content: Subject to Quantic terms of service

## Retention

### Retention Schedule

| Retention Class | Duration | Rationale |
|----------------|----------|-----------|
| **Permanent** | Indefinite | Decision records, canonical artifacts, publications |
| **Long-term (7 years)** | 7 years from study completion | Primary research data; supports replication and verification |
| **Medium-term (3 years)** | 3 years from study completion | Analysis outputs, intermediate datasets |
| **Short-term (1 year)** | 1 year from creation | Working drafts, temporary files |
| **Destroy post-analysis** | After analysis complete | Sensitive preliminary notes, unverified observations |

### Destruction Procedures

- Data marked for destruction is securely deleted (not just moved to trash)
- Backups of destroyed data are also purged
- Destruction is documented in the change log
- Data that has been published or shared cannot be recalled from recipients

## Anonymization

### What Is Anonymized

- Researcher name replaced with participant ID (e.g., P001)
- Dates shifted by consistent offset (preserving temporal relationships)
- Session locations generalized (e.g., "home office" not "123 Main St")
- Platform version numbers retained (scientifically relevant)

### What Is NOT Anonymized

- Construct definitions and benchmark taxonomy (public by design)
- Observation schemas (public by design)
- Research methodology (public by design)
- Platform name (attribution required by research standards)

## Privacy

### Personally Identifiable Information (PII)

PII is minimized in the research design:
- No collection of names, addresses, phone numbers, or email addresses of other individuals
- Researcher's own contact information is stored separately from research data
- Screenshots are reviewed for PII before deposition
- The `contains_pii` field in the observation schema flags any observation that may contain PII

### Platform Data

- AI-generated instructional content is documented for research purposes under fair use
- Platform interface screenshots are minimized to show only relevant elements
- Proprietary platform code, algorithms, or backend data are not accessed or collected

## Backup and Recovery

### Backup Schedule

| Data | Frequency | Location |
|------|-----------|----------|
| Observation YAML files | Daily (after each session) | Local + external drive |
| Screenshots | Daily (after each session) | Local + external drive |
| Repository commits | After each significant change | GitHub (private) |
| Monthly reports | Monthly | Repository + external drive |
| Full dataset archive | Monthly | External drive + cloud (if adopted) |

### Recovery Procedures

- Primary data loss: Restore from external drive backup
- External drive failure: Restore from cloud backup (if adopted)
- Repository loss: Restore from GitHub (if private repo maintained)
- All backups tested quarterly for integrity

## Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Principal Investigator** | Data ownership, access control, sharing decisions, retention enforcement |
| **Researcher (Subject)** | Data generation, quality control, PII review |
| **Future Data Steward** | Long-term preservation, access management (if PI unavailable) |

---

## Maturity Path

This artifact advances from Draft to Stable when:
- [ ] Storage infrastructure has been established and tested
- [ ] Backup and recovery procedures have been tested
- [ ] IRB has approved the data management approach
- [ ] First data deposit has been completed successfully
- [ ] Access control procedures have been documented and tested
