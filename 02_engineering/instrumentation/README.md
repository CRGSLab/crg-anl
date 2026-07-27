# Instrumentation

**Purpose:** Research workflow automation and data collection tooling for the CRG-ANL researcher-as-subject protocol.

**Status:** Active — CLI tool `crg_session.py` operational

---

## `crg_session.py` — Session Manager CLI

A Python CLI tool that automates file creation, validation, cross-referencing, and git workflow for Pilot 001 data collection. It replaces the manual copy-paste-template workflow with interactive wizards while preserving all data quality requirements.

### Installation

Add an alias to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
alias crg='python3 /path/to/crg-anl/02_engineering/instrumentation/crg_session.py'
```

Or use the wrapper script directly:

```bash
./02_engineering/instrumentation/crg <command>
```

### Commands

| Command | When to use | What it does |
|---------|-------------|--------------|
| `crg start` | Before every session | Interactive pre-session wizard: creates baseline, session log, screenshot dir; offers to open Quantic |
| `crg event` | During session | Quick-log an observation event (15 sec in quick mode) |
| `crg end` | Immediately after session | Computes duration, appends footer to log |
| `crg post` | After `end` | Interactive NASA-TLX + 14 subjective scales + research notes |
| `crg code` | After `post` | Guided observation YAML generator with construct selection |
| `crg commit` | After all coding | Auto-generated git commit with descriptive message |
| `crg week` | Every Sunday | Weekly memo with auto-aggregated session counts |
| `crg status` | Any time | Shows active session state and completion checklist |
| `crg open` | Any time | Opens Quantic in browser |

### Workflow Example

```bash
crg start    # 2 min — pre-session wizard
crg event    # 15 sec — log event during studying
crg end      # 5 sec — end session
crg post     # 8 min — post-session instruments
crg code     # 3 min per observation — guided YAML
crg commit   # 10 sec — git commit
```

### Data Quality Improvements Over Manual Workflow

| Aspect | Manual | Automated |
|--------|--------|-----------|
| Filename generation | Copy-paste, error-prone | Auto-generated, always correct |
| Input validation | None | Every rating validated against scale |
| Cross-references | Manual copy | Auto-copied from baseline → log → YAML |
| Session numbering | Manual tracking | Auto-incremented in registry |
| Event logging | Full text during session | Quick mode: 15 seconds |
| Construct coding | Free-text | Guided selection from canonical enums |
| Git commits | Composed manually | Auto-generated with counts |
| Weekly counts | Manual tally | Auto-aggregated from registry |

### Files Managed

- `session_registry.json` — canonical session history (auto-generated)
- `current_session.json` — active session state (auto-generated)
- `test_crg_session.py` — integration tests

### Troubleshooting

| Problem | Solution |
|---------|----------|
| `crg` not found | Use full path: `python3 02_engineering/instrumentation/crg_session.py` |
| Registry seems wrong | Delete `session_registry.json` and `current_session.json`; tool will recreate |
| Want to edit files manually | All files are plain Markdown/YAML in `03_evidence/` — edit freely |
| Tool crashes | Files are never deleted by the tool; check `03_evidence/` for your data |

---

## Schema Files

- `observation_schema.yaml` — canonical YAML schema for coded observations

## Dependencies

- Python 3.9+
- No external packages (stdlib only)
