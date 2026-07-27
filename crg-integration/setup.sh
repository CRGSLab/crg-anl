#!/usr/bin/env bash
# CRG-ANL Cockpit Integration Setup Script
# This script integrates cockpit with the crg-anl research project

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CRG_ANL_ROOT="/Users/coreyalejandro/projects/crg-anl"
COCKPIT_PATH="/opt/homebrew/bin/cockpit"

echo "=========================================="
echo "CRG-ANL Cockpit Integration Setup"
echo "=========================================="

# Check if cockpit is installed
if [[ -z "$(command -v cockpit)" ]]; then
    echo "Error: cockpit is not installed."
    echo "Install with: npm install -g @surething/cockpit"
    exit 1
fi

# Check if crg-anl directory exists
if [[ ! -d "$CRG_ANL_ROOT" ]]; then
    echo "Error: CRG-ANL project not found at $CRG_ANL_ROOT"
    exit 1
fi

echo "[OK] Cockpit is installed: $(which cockpit)"
echo "[OK] CRG-ANL project exists at $CRG_ANL_ROOT"

# Create cockpit workspace directory in crg-anl
COCKPIT_WORKSPACE="$CRG_ANL_ROOT/.cockpit"
mkdir -p "$COCKPIT_WORKSPACE"

cat > "$COCKPIT_WORKSPACE/settings.json" << 'EOF'
{
  "workspaces": {
    "crg-anl": {
      "name": "CRG-ANL Research Project",
      "path": "/Users/coreyalejandro/projects/crg-anl",
      "projectType": "research",
      "defaultEngine": "claude",
      "features": {
        "fileExplorer": true,
        "terminal": true,
        "browserBubble": false,
        "databaseBubbles": false,
        "codeGraph": true,
        "aiChat": true,
        "slashModes": true,
        "scheduledTasks": true
      },
      "researchConfig": {
        "constructsPath": "/Users/coreyalejandro/projects/crg-anl/01_science/",
        "benchmarkTaxonomyPath": "/Users/coreyalejandro/projects/crg-anl/01_science/benchmark_taxonomy.md",
        "fieldNotesPath": "/Users/coreyalejandro/projects/crg-anl/03_evidence/field_notes/",
        "observationLogsPath": "/Users/coreyalejandro/projects/crg-anl/02_engineering/instrumentation/"
      }
    }
  },
  "slashModes": {
    "research": [
      {
        "name": "clarify-only",
        "alias": "/qa",
        "description": "Clarify the research question without taking action"
      },
      {
        "name": "diagnose-only", 
        "alias": "/fx",
        "description": "Diagnose issues in learning systems without modifying code"
      },
      {
        "name": "explore-mode",
        "alias": "/ex",
        "description": "6-step structured research exploration (study → diverge → converge)"
      },
      {
        "name": "land-and-implement",
        "alias": "/go",
        "description": "Take converged plan and implement MVP stages"
      },
      {
        "name": "codegraph-explore",
        "alias": "/cg",
        "description": "Query project code graph for symbol/impact analysis"
      }
    ]
  },
  "benchmarks": [
    {
      "id": "cognitive-safety",
      "name": "Cognitive Safety Measurement",
      "path": "/Users/coreyalejandro/projects/crg-anl/01_science/benchmark_taxonomy.md"
    },
    {
      "id": "instructional-integrity", 
      "name": "Instructional Integrity Benchmarks",
      "path": "/Users/coreyalejandro/projects/crg-anl/02_engineering/architecture/"
    }
  ]
}
EOF

echo "[OK] Created cockpit workspace at $COCKPIT_WORKSPACE"

# Create a research-specific cockpit wrapper script
cat > "$CRG_ANL_ROOT/bin/research-cockpit.sh" << 'WRAPPER'
#!/usr/bin/env bash
# Research Cockpit Wrapper for CRG-ANL
# Provides both TUI and GUI access to the research environment

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COCKPIT_PATH="/opt/homebrew/bin/cockpit"
CRG_ANL_ROOT="$SCRIPT_DIR/../.."
PORT="${RESEARCH_COCKPIT_PORT:-3458}"

usage() {
    cat << EOF
Usage: $0 [command] [options]

Commands:
  start              Start research cockpit GUI (web interface)
  gui                Alias for start - open graphical interface
  tui                Terminal User Interface mode
  explore            Quick exploration of project structure  
  analyze <query>    Run AI analysis on research topics
  report <topic>     Generate AI-assisted report on a topic
  graph              Open code graph visualization
  observe <id>       Monitor active research sessions

Options:
  -p, --port PORT    Specify port (default: 3458)
  -n, --no-open      Don't auto-open browser
  -h, --help         Show this help

Examples:
  $0 start                    # Start GUI and open in browser
  $0 tui                      # Run terminal interface commands
  $0 explore .                # Quick project structure exploration
  $0 analyze "cognitive safety"   # AI analysis of cognitive safety constructs

EOF
    exit 0
}

case "${1:-}" in
    start|gui)
        echo "Starting CRG-ANL Research Cockpit GUI..."
        COCKPIT_OPEN_PROJECT="$CRG_ANL_ROOT" \
            PORT="$PORT" \
            "$COCKPIT_PATH" \
            --port "$PORT" \
            --no-open || true  # Don't open browser here, we'll do it after server starts
        
        if [[ -z "$(command -v open)" ]]; then
            echo "open command not found. Use: $0 gui --url http://localhost:$PORT"
        else
            sleep 3 && open "http://localhost:$PORT/?cwd=$CRG_ANL_ROOT" || true
        fi
        
        ;;
    
    tui)
        # Terminal User Interface - run cockpit commands directly
        shift
        "$COCKPIT_PATH" "$@" --cwd "$CRG_ANL_ROOT"
        
        ;;
    
    explore)
        echo "=== CRG-ANL Project Explorer ==="
        echo ""
        echo "Project Structure:"
        tree -L 2 --dirsfirst "$CRG_ANL_ROOT" 2>/dev/null || \
            find "$CRG_ANL_ROOT" -maxdepth 3 -type f | head -50
        
        echo ""
        echo "Recent Observation Logs:"
        if [[ -d "$CRG_ANL_ROOT/02_engineering/instrumentation/" ]]; then
            ls -la "$CRG_ANL_ROOT/02_engineering/instrumentation/session_registry.json" 2>/dev/null || \
                echo "No session registry found"
        fi
        
        echo ""
        echo "To use full GUI, run: $0 start"
        
        ;;
    
    analyze)
        if [[ -z "${2:-}" ]]; then
            echo "Error: Please specify a topic to analyze"
            echo "Example: $0 analyze 'cognitive safety' | Example: $0 analyze 'instructional integrity'"
            exit 1
        fi
        
        TOPIC="$2"
        PORT="${RESEARCH_COCKPIT_PORT:-3458}"
        
        echo "Analyzing: $TOPIC"
        echo "Starting research cockpit..."
        
        # Start server in background if not already running
        SERVER_PID=""
        cleanup() {
            [[ -n "$SERVER_PID" ]] && kill "$SERVER_PID" 2>/dev/null || true
        }
        trap cleanup EXIT
        
        # Check if server is running
        if ! curl -s "http://localhost:$PORT/api/version" >/dev/null 2>&1; then
            COCKPIT_OPEN_PROJECT="$CRG_ANL_ROOT" \
                PORT="$PORT" \
                "$COCKPIT_PATH" \
                --port "$PORT" \
                &
            SERVER_PID=$!
            
            # Wait for server to start
            echo "Waiting for server..."
            sleep 8
        else
            echo "Server already running at http://localhost:$PORT"
        fi
        
        # Send analyze request via CLI or browser automation would go here
        # For now, we provide a helpful prompt
        echo ""
        echo "To view AI analysis results, visit:"
        echo "  http://localhost:$PORT/"
        echo ""
        echo "Or use cockpit commands directly:"
        echo "  cockpit . --token YOUR_TOKEN"
        
        ;;
    
    report)
        TOPIC="${2:-}"
        if [[ -z "$TOPIC" ]]; then
            echo "Error: Please specify a topic for the report"
            exit 1
        fi
        
        PORT="${RESEARCH_COCKPIT_PORT:-3458}"
        
        # Start server if needed
        if ! curl -s "http://localhost:$PORT/api/version" >/dev/null 2>&1; then
            COCKPIT_OPEN_PROJECT="$CRG_ANL_ROOT" \
                PORT="$PORT" \
                "$COCKPIT_PATH" \
                --port "$PORT" &
            
            echo "Waiting for server..."
            sleep 5
            
            # Open browser with report prompt
            open "http://localhost:$PORT/?prompt=write+a+research+report+about+$TOPIC+using+crg-anl+project+context" || true
        else
            open "http://localhost:$PORT/?prompt=generate+research+report+on:+$TOPIC" || true
        fi
        
        ;;
    
    graph)
        # Open codegraph for the project
        echo "Opening CRG-ANL code graph visualization..."
        
        if command -v cockpit &>/dev/null; then
            "$COCKPIT_PATH" codegraph search --cwd "$CRG_ANL_ROOT" \
                -p "function\|class\|interface" || true
        else
            echo "cockpit not found. Install with: npm install -g @surething/cockpit"
        fi
        
        ;;
    
    observe)
        SESSION_ID="${2:-}"
        if [[ -z "$SESSION_ID" ]]; then
            echo "Usage: $0 observe <session_id>"
            echo "List active research sessions:"
            cockpit connection list --cwd "$CRG_ANL_ROOT" 2>/dev/null || true
        else
            # Monitor a specific session
            echo "Monitoring session: $SESSION_ID"
            
            if [[ -d "$COCKPIT_WORKSPACE/cockpit-state" ]]; then
                cat "$COCKPIT_WORKSPACE/cockpit-state/session-history.json" 2>/dev/null | \
                    grep -A 50 "\"$SESSION_ID\"" || echo "No session history found"
            else
                echo "Session state not persisted. Run with GUI for persistence."
            fi
            
        ;;
    esac

WRAPPER
chmod +x "$CRG_ANL_ROOT/bin/research-cockpit.sh"

echo "[OK] Created research cockpit wrapper at $CRG_ANL_ROOT/bin/research-cockpit.sh"

# Create a convenience script in the project root
cat > "$CRG_ANL_ROOT/cockpit" << 'CONVENIENCE'
#!/usr/bin/env bash
# Convenience script to launch CRG-ANL research cockpit

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESEARCH_COCKPIT="$SCRIPT_DIR/bin/research-cockpit.sh"

case "${1:-start}" in
    start|gui)
        RESEARCH_COCKPIT start "$@"
        ;;
    tui)
        RESEARCH_COCKPIT tui "$@"
        ;;
    explore)
        RESEARCH_COCKPIT explore "$@"
        ;;
    *)
        echo "Error: Use $RESEARCH_COCKPIT for commands"
        exit 1
        ;;
esac
CONVENIENCE
chmod +x "$CRG_ANL_ROOT/cockpit"

echo "[OK] Created convenience script at $CRG_ANL_ROOT/cockpit"

# Create a README for the cockpit integration
cat > "$COCKPIT_WORKSPACE/README.md" << 'README'
# CRG-ANL Cockpit Integration

This directory contains configuration and state for the Cockpit integration with CRG-ANL.

## Quick Start

```bash
# From any terminal
cd /Users/coreyalejandro/projects/crg-anl
./cockpit start       # Launch GUI
./cockpit tui         # Use terminal interface directly
./cockpit explore     # Quick project exploration
```

## Integration Features

- **GUI Mode**: Web-based IDE with file explorer, terminal bubbles, AI chat, and code graph
- **TUI Mode**: CLI commands for research operations without browser
- **Research Context**: Pre-configured to understand CRG-ANL's constructs and benchmarks
- **Slash Modes**: `/ex`, `/go`, `/cg` modes optimized for research workflows

## Configuration

See `settings.json` in this directory for current settings.
README

echo "[OK] Created workspace README at $COCKPIT_WORKSPACE/README.md"

# Create .gitignore to keep cockpit state out of commits
cat > "$COCKPIT_WORKSPACE/.gitignore" << 'GITIGNORE'
# Cockpit runtime state (don't commit)
cockpit-state/
session-history.json
*.tmp
*.lock

# Local caches
node_modules/
.next-prod/cache/

# IDE specific
.vscode/
.idea/
*.swp
*.swo
*~
GITIGNORE

echo "[OK] Created .gitignore at $COCKPIT_WORKSPACE/.gitignore"

echo ""
echo "=========================================="
echo "CRG-ANL Cockpit Integration Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "  1. Run: ./cockpit start     (opens GUI in browser)"
echo "  2. Run: ./cockpit tui       (use terminal interface directly)"
echo "  3. Visit http://localhost:3457/ for the web interface"
echo ""