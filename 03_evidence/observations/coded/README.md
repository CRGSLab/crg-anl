# Coded Observations

**Purpose:** YAML-formatted observation records following the canonical observation schema.

**Naming convention:** `obs_YYYYMMDD_NNN_<construct>.yaml`

Where:
- `YYYYMMDD` = session date
- `NNN` = sequential observation number
- `<construct>` = primary construct code:
  - `c1_crg` — Constitutional Runtime Governance
  - `c2_cog_safety` — Cognitive Safety
  - `c3_inst_integrity` — Instructional Integrity
  - `c4_agency` — Learner Agency
  - `c5_shared_resp` — Human–AI Shared Responsibility
  - `c6_transition` — Transition Integrity
  - `c10_governance_window` — Persistent Governance Window

**Schema:** `02_engineering/schemas/observation_schema.yaml`

**Created:** After every session by coding events from the session log. See `QUICKSTART.md` Phase 3.
