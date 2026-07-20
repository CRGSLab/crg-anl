# Ethics Protocol

**Artifact:** Ethics Protocol  
**Version:** 0.1.0 (Draft)  
**Status:** Draft — pending IRB consultation and institutional review  
**Canonical:** Yes — governs all ethical aspects of the research program  

---

## Overview

This document specifies the ethical framework for the CRG-ANL Research Program.
It addresses researcher-as-subject boundaries, consent, risk assessment, and institutional compliance.

## Known Limitations (Draft v0.1)

- This protocol has not yet been reviewed by an Institutional Review Board (IRB)
- Some provisions (e.g., data sharing consent) assume a future phase with external participants
- The researcher-as-subject design creates unique ethical considerations that may require IRB guidance

---

## Researcher-as-Subject Boundaries

### What Constitutes Researcher-as-Subject Data

Data collected under this protocol includes:
- The researcher's own learning interactions with the Quantic platform
- The researcher's subjective cognitive and emotional states during learning
- The researcher's reflections on the learning experience
- Screenshots of the platform interface (showing only the researcher's own content)
- Platform-generated content (AI explanations, assessments, feedback) encountered by the researcher

### What Does NOT Constitute Researcher-as-Subject Data

The following are explicitly excluded from this research:
- Data about other Quantic students (names, progress, scores, interactions)
- Platform analytics not directly visible to the researcher during their own sessions
- Instructor or administrator data
- Any content accessed through means other than the researcher's own student account

### Boundary Enforcement

- All observations are filtered through the lens of the researcher's own experience
- If the researcher observes another student's data on screen (e.g., leaderboard, forum post), it is not recorded
- Screenshots are reviewed before deposition to ensure no other student data is visible
- If a screenshot inadvertently captures other student information, it is deleted and not deposited

## Consent Framework

### Self-Consent (Researcher-as-Subject)

As both researcher and sole subject, the Principal Investigator provides self-consent for their own data collection.
This consent is documented through:

- Explicit acknowledgment in this ethics protocol
- Written consent statement signed by the Principal Investigator
- Annual re-affirmation of consent

### Consent Statement

> I, [Principal Investigator Name], consent to participate in the CRG-ANL Research Program as the sole research subject.
> I understand that my learning interactions with the Quantic MS in AI Engineering platform will be systematically observed, recorded, and analyzed.
> I understand that the data collected will include my subjective cognitive states, emotional responses, learning performance, and reflections.
> I understand that I may withdraw from the study at any time without penalty.
> I understand that my data will be managed according to the Data Management Plan (see `data_management_plan.md`).

### Future Participant Consent (Pilot 002 and Beyond)

If future pilots involve participants other than the researcher, the following consent procedures will apply:

- **Informed consent:** Written consent obtained before data collection
- **Voluntary participation:** Participants may withdraw at any time
- **Right to data deletion:** Participants may request deletion of their data
- **Right to review:** Participants may review their own data
- **Minimal risk:** Research poses no greater risk than normal educational activity

## Risk Assessment

### Risks to the Researcher (Subject)

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| Cognitive burden from data collection | High | Low | Protocol designed for minimal burden (~17 minutes per session); sessions may be paused or terminated |
| Emotional distress from reflecting on negative experiences | Medium | Low | Researcher may skip reflective prompts; protocol includes well-being checks |
| Reduced learning quality due to research demands | Low | Medium | Regular self-checks; protocol may be adjusted if learning quality declines |
| Privacy concerns from data storage | Low | Medium | Data stored securely with encryption; see Data Management Plan |

### Risks to Other Students

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| Unintentional collection of other student data | Low | High | Explicit exclusion protocol; screenshot review; data deletion if breach occurs |
| Platform criticism affecting other students | Low | Low | Findings reported constructively; criticism directed at design patterns, not individuals |
| Identification of the researcher affecting their student status | Very Low | Medium | Researcher status disclosed to Quantic if required by terms of service |

### Risks to the Institution (Quantic)

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| Negative publicity from critical findings | Low | Medium | Findings reported constructively; advance communication with Quantic if findings are critical |
| Misrepresentation of platform capabilities | Low | Medium | Claims proportionate to evidence; limitations explicitly stated |

## Deception Policy

### No Deception

The CRG-ANL Research Program does not involve deception.
The researcher is fully aware that they are the subject of research.
All data collection procedures are transparent.

### Transparency with Platform

The researcher will:
- Comply with Quantic's terms of service
- Disclose research activity to Quantic if required
- Not use automated tools or scripts that violate platform terms
- Not share proprietary platform content beyond what is necessary for research documentation

## Vulnerable Populations

The researcher-as-subject design does not involve vulnerable populations.
If future pilots involve participants under 18, individuals with cognitive disabilities, or other vulnerable groups, additional ethical safeguards will be implemented.

## Data Ethics

### Ownership

The researcher owns their own data.
The Principal Investigator controls research outputs (publications, datasets).

### Platform Content

AI-generated instructional content encountered during sessions is documented for research purposes.
This documentation is considered fair use for research and criticism.
Platform branding and proprietary interface elements are minimized in screenshots.

### Publication Ethics

- All findings reported honestly, including negative results and null findings
- Limitations disclosed transparently
- Claims proportionate to evidence
- Single-subject limitations acknowledged in all publications
- Constructive framing: criticism directed at design patterns and systemic issues, not individuals or institutions

## Compliance

### Institutional Review Board (IRB)

This protocol will be submitted to an IRB for review.
Given the researcher-as-subject design and minimal risk profile, this may qualify for exempt review, but the Principal Investigator will seek formal IRB determination.

See `irb_readiness.md` for IRB submission preparation.

### Platform Terms of Service

The researcher will:
- Review and comply with Quantic's terms of service
- Document any terms relevant to research activity
- Seek clarification from Quantic if terms are ambiguous
- Cease data collection if terms change to prohibit research activity

### Data Protection Regulations

If future pilots involve participants from jurisdictions with data protection regulations (GDPR, CCPA), additional compliance measures will be implemented.

---

## Maturity Path

This artifact advances from Draft to Stable when:
- [ ] IRB review has been completed and determination received
- [ ] Quantic terms of service have been reviewed and compliance confirmed
- [ ] Consent documentation has been completed and signed
- [ ] Risk mitigation procedures have been tested in initial pilot sessions
- [ ] Annual review and re-affirmation procedures have been established
