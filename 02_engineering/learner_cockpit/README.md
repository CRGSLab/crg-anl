# Learner Cockpit

**Purpose:**  
Design specifications for the Learner Cockpit — a persistent, learner-visible interface element that displays real-time information about the AI system's state, confidence, limitations, and governance status.

**Relationships:**  
- Implements the construct defined in `01_science/construct_definitions.md` (C8)
- Supports Learner Agency (C4) and Human–AI Shared Responsibility (C5)
- Displays Runtime Governance (C1) and Runtime Intervention (C7) status

**Inputs:**  
- Construct definition for Learner Cockpit
- Requirements from Cognitive Safety, Agency, and Shared Responsibility constructs

**Outputs:**  
- Information architecture specification
- Display layout designs
- Interaction pattern definitions

---

## Design Principles

1. **Always visible:** The cockpit is persistent, not hidden behind menus
2. **Non-intrusive:** Cockpit information does not distract from learning
3. **Actionable:** Information enables informed learner decisions
4. **Honest:** The cockpit accurately reflects AI state, including limitations
5. **Educational:** The cockpit teaches learners about AI governance

## Information Architecture

### Primary Display (always visible)

| Element | Display | Purpose |
|---------|---------|---------|
| Governance Status | "Governed" / "Caution" / "Alert" | Real-time CRG status |
| AI Confidence | "High" / "Moderate" / "Low" | Epistemic transparency |
| Topic | Current topic name | Context maintenance |
| Progress | "3/5 concepts" | Progress awareness |

### Secondary Display (expandable)

| Element | Display | Purpose |
|---------|---------|---------|
| Responsibility Distribution | "AI: content, feedback / You: goals, pacing" | Shared responsibility visibility |
| Recent Interventions | Timestamped list with reasons | Intervention transparency |
| AI Limitations | "Cannot access web / Knowledge: Apr 2024" | Epistemic humility |
| Cognitive Load Indicator | "Load: Moderate" | Safety monitoring |

### Tertiary Display (detailed view)

| Element | Display | Purpose |
|---------|---------|---------|
| Constitution Summary | List of active governance rules | Governance comprehensibility |
| Session History | Timeline of events and interventions | Situation awareness |
| Override Controls | Buttons to override AI decisions | Agency support |
