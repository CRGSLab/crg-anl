# IRB Readiness

**Artifact:** IRB Readiness  
**Version:** 0.1.0 (Draft)  
**Status:** Draft — pending IRB submission  
**Canonical:** Yes — documents IRB preparation status  

---

## Overview

This document tracks readiness for Institutional Review Board (IRB) submission.
It identifies what materials are prepared, what remains to be done, and what type of IRB review is anticipated.

---

## Anticipated IRB Review Type

Given the researcher-as-subject design with a single participant (the Principal Investigator), this study may qualify for **exempt review** under 45 CFR 46.104(d)(1):

> Research conducted in established or commonly accepted educational settings, involving normal educational practices.

However, the Principal Investigator will seek formal IRB determination rather than self-certifying exemption.

### Rationale for Exempt Classification

| Criterion | Assessment |
|-----------|-----------|
| Educational setting | Yes — Quantic MS in AI Engineering is an established educational program |
| Normal educational practices | Yes — the researcher engages in normal learning activities; observation does not alter the educational experience |
| Minimal risk | Yes — risks are limited to the researcher's own cognitive and emotional states, no greater than normal educational activity |
| No vulnerable populations | Yes — the sole participant is the Principal Investigator, a competent adult |
| No deception | Yes — the researcher is fully aware of the research nature |

### Contingency: Full Board Review

If the IRB determines that full board review is required (e.g., due to data sharing plans, longitudinal scope, or platform partnership), the following materials are prepared or in preparation:

---

## IRB Submission Materials

### Prepared

| Document | Location | Status |
|----------|----------|--------|
| Research protocol | `01_science/study_protocol.md` | Complete |
| Ethics protocol | `07_project_operations/ethics_protocol.md` | Draft |
| Data management plan | `07_project_operations/data_management_plan.md` | Draft |
| Consent form (self-consent) | Embedded in `ethics_protocol.md` | Draft |
| Risk assessment | `ethics_protocol.md` | Complete |
| Principal Investigator CV | External | Current |

### In Preparation

| Document | Location | Status | Blocker |
|----------|----------|--------|---------|
| IRB application form | External | Not started | Awaiting IRB selection |
| Platform approval letter (Quantic) | External | Not started | TBD whether required |
| Certificate of human subjects training (CITI) | External | Not started | Required before submission |

### Not Yet Required (Future Pilots)

| Document | Required For |
|----------|-------------|
| Informed consent form (external participants) | Pilot 002 and beyond |
| Assent form (minors) | Only if minors are involved |
| Vulnerable population safeguards | Only if vulnerable populations are involved |
| International research approval | Only if international participants are involved |

---

## IRB Submission Checklist

### Before Submission

- [ ] Select IRB (institutional affiliation TBD)
- [ ] Complete CITI human subjects training
- [ ] Finalize ethics protocol (after internal review)
- [ ] Finalize data management plan (after storage setup)
- [ ] Obtain platform approval letter (if required)
- [ ] Complete IRB application form
- [ ] Attach all supporting documents
- [ ] Principal Investigator signature

### After Submission

- [ ] Track IRB review status
- [ ] Respond to IRB queries or requests for modifications
- [ ] Obtain IRB determination letter
- [ ] File determination in `07_project_operations/`
- [ ] Update ethics protocol with IRB conditions or requirements
- [ ] Begin data collection only after IRB approval received

---

## IRB Conditions and Monitoring

### Anticipated Conditions

If IRB approval is granted, the following conditions are anticipated:

- Annual continuing review (if study duration > 1 year)
- Prompt reporting of any adverse events
- Prompt reporting of any protocol changes
- Final report upon study completion

### Monitoring Procedures

- IRB approval letter and all correspondence filed in `07_project_operations/`
- Annual continuing review reminders scheduled
- Protocol changes documented in `07_project_operations/decision_log.md` and submitted to IRB for approval
- Adverse events (if any) reported within 48 hours

---

## Maturity Path

This artifact is complete when:
- [ ] IRB determination has been received
- [ ] Approval letter is filed in `07_project_operations/`
- [ ] Any IRB conditions have been incorporated into the study protocol
- [ ] Data collection has begun under IRB-approved protocol
