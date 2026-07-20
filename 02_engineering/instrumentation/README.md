# Instrumentation

**Purpose:**  
Specifications for data collection tools used during researcher-as-subject sessions.

**Relationships:**  
- Implements the observation protocol from `01_science/study_protocol.md`
- Produces observations conforming to `../schemas/observation_schema.yaml`
- Deposits evidence in `03_evidence/`

**Inputs:**  
- Study protocol procedures
- Observation schema field specifications
- Session metadata

**Outputs:**  
- Observation records in YAML format
- NASA-TLX ratings
- Subjective scale ratings
- Screenshot annotations
- Researcher notes

---

## Instruments

### 1. Observation Recorder

A structured interface for recording instructional events during sessions.

**Required Fields:**
- Timestamp (auto-generated)
- Observation type (dropdown from taxonomy)
- Runtime trigger (free text)
- Severity (1-5 scale)
- Instructional integrity dimension (dropdown)

**Optional Fields:**
- Cognitive safety impact
- Human agency assessment
- Shared responsibility assessment
- Evidence references
- Research memo
- Candidate intervention

### 2. NASA-TLX Interface

Standardized NASA Task Load Index rating interface.

**Dimensions:**
- Mental Demand (0-100 slider)
- Physical Demand (0-100 slider)
- Temporal Demand (0-100 slider)
- Performance (0-100 slider, inverted)
- Effort (0-100 slider)
- Frustration (0-100 slider)

### 3. Subjective Scales Interface

Post-session subjective rating interface.

**Items (all 1-7 Likert scale):**
- I felt in control of my learning
- I understood why the AI made its decisions
- I trusted the information the AI provided
- The AI was transparent about its limitations
- I felt safe to make mistakes
- The pace was appropriate
- The difficulty was appropriate
- The AI understood my learning needs
- I would recommend this experience
- I feel I learned something valuable

### 4. Screenshot Capture Protocol

Specifications for capturing and annotating screenshots:
- Filename format: `{session_id}_{description}_{sequence}.png`
- Minimum resolution: 1920x1080
- Annotation: timestamp, observation reference, brief description
- Storage: `03_evidence/screenshots/`
