#!/usr/bin/env bash
# Research Cockpit Wrapper for CRG-ANL
# Provides both TUI (Terminal User Interface) and GUI (Graphical User Interface) access

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COCKPIT_PATH="/opt/homebrew/bin/cockpit"
CRG_ANL_ROOT="${CRG_ANL_ROOT:-$SCRIPT_DIR/..}"
PORT="${RESEARCH_COCKPIT_PORT:-3458}"

usage() {
    cat << EOF
Usage: $0 [command] [options]

Commands:
  start              Start research cockpit GUI (web interface)
  gui                Alias for start - open graphical interface  
  tui                Terminal User Interface mode
  explore            Quick exploration of project structure  
  analyze <query>    Run AI analysis on research topics via browser prompt

Options:
  --cwd PATH         Override the CRG-ANL root directory (default: $CRG_ANL_ROOT)
  -p, --port PORT    Specify port (default: 3458)
  -n, --no-open      Don't auto-open browser in GUI mode
  -h, --help         Show this help

Examples:
  $0 start                    # Start GUI and open in browser
  $0 tui                      # Run terminal interface commands directly
  $0 explore                  # Quick project structure exploration  
  $0 analyze "cognitive safety"   # AI analysis via browser prompt
EOF
    exit 0
}

# Parse --cwd option if provided
CRG_ANL_ROOT_OVERRIDE=""
if [[ "${1:-}" == "--cwd" ]]; then
    CRG_ANL_ROOT_OVERRIDE="${2:-}"
    shift 2
fi

case "${1:-}" in
    start|gui)
        echo "Starting CRG-ANL Research Cockpit GUI..."
        
        # Use override if provided, otherwise use default
        ROOT_DIR="${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}"
        
        COCKPIT_OPEN_PROJECT="$ROOT_DIR" \
            PORT="$PORT" \
            "$COCKPIT_PATH" \
            --port "$PORT" \
            --no-open
        
        # Open browser after server starts
        if [[ -n "$(command -v open)" ]]; then
            echo "Opening browser at http://localhost:$PORT..."
            sleep 3 && open "http://localhost:$PORT/?cwd=$ROOT_DIR" || true
        else
            echo "open command not found. Visit: http://localhost:$PORT/"
        fi
        
        ;;
    
    tui)
        # Terminal User Interface - run cockpit CLI commands directly
        shift
        ROOT_DIR="${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}"
        
        if [[ $# -eq 0 ]]; then
            echo "TUI mode: Run cockpit commands for the current project"
            echo "Available TUI commands:"
            echo "  connection list         # List all bubbles (term + browser)"
            echo "  terminal <id> output    # Read terminal output"
            echo "  codegraph search        # Search code graph"
            echo ""
            echo "Example: $0 tui connection list --cwd $ROOT_DIR"
            exit 1
        fi
        
        "$COCKPIT_PATH" "$@" --cwd "$ROOT_DIR"
        
        ;;
    
    explore)
        echo "=== CRG-ANL Project Explorer ==="
        echo ""
        echo "Project Root: ${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}"
        echo ""
        echo "Directory Structure (depth 3):"
        
        # Use find with better formatting, handling non-existent tree command
        if command -v tree &>/dev/null; then
            tree -L 2 --dirsfirst "${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}" 2>/dev/null | head -100 || \
                echo "tree failed"
        else
            # Fallback: use find with colorized output
            echo ""
            echo "Project directories:"
            find "${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}" -maxdepth 3 -type d | head -80 | while read dir; do
                basename "$dir"
            done
            
            echo ""
            echo "Key files and recent observations:"
            
            # Show important directories with their contents summary
            for key_dir in \
                "01_science/research_program.md" \
                "02_engineering/architecture/README.md" \
                "03_evidence/field_notes/" \
                "05_experiments/pilot_001/protocol.md"; do
                
                if [[ -f "${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}/$key_dir" ]]; then
                    echo ""
                    echo "[+] $key_dir ($(wc -l < "${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}/$key_dir") lines)"
                elif [[ -d "${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}/$(dirname "$key_dir")" ]]; then
                    echo ""
                    echo "[-] $key_dir (directory exists: $(ls -la "${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}/$(dirname "$key_dir")/" 2>/dev/null | head -5))"
                fi
            done
            
            # Show session registry if it exists
            SESSION_REGISTRY="${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}/02_engineering/instrumentation/session_registry.json"
            if [[ -f "$SESSION_REGISTRY" ]]; then
                echo ""
                echo "[+] Session Registry: $SESSION_REGISTRY"
                echo "    Active sessions: $(grep -c '"id"' "$SESSION_REGISTRY" 2>/dev/null || echo 'N/A')"
                cat "$SESSION_REGISTRY" | head -30 2>/dev/null
            else
                echo ""
                echo "[-] No session registry found at $SESSION_REGISTRY"
            fi
            
        fi
        
        echo ""
        echo "To use full GUI, run: $0 start"
        
        ;;
    
    analyze)
        TOPIC="${2:-}"
        if [[ -z "$TOPIC" ]]; then
            echo "Error: Please specify a topic to analyze"
            exit 1
        fi
        
        PORT="${RESEARCH_COCKPIT_PORT:-3458}"
        
        echo "Analyzing research topic: $TOPIC"
        echo ""
        
        # Check if server is running
        if ! curl -s "http://localhost:$PORT/api/version" >/dev/null 2>&1; then
            echo "Starting research cockpit..."
            ROOT_DIR="${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}"
            
            COCKPIT_OPEN_PROJECT="$ROOT_DIR" \
                PORT="$PORT" \
                "$COCKPIT_PATH" \
                --port "$PORT" &
            
            echo "Waiting for server to start (this may take ~10 seconds)..."
            sleep 8
            
            # Open browser with analysis prompt
            open "http://localhost:$PORT/?prompt=analyze+the+research+topic:+$TOPIC+in+context+of+CRG-ANL" || true
        else
            echo "Server already running at http://localhost:$PORT"
            echo ""
            echo "Opening browser with analysis prompt..."
            open "http://localhost:$PORT/?prompt=analyze+research:+$TOPIC" || true
        fi
        
        ;;
    
    graph)
        ROOT_DIR="${CRG_ANL_ROOT_OVERRIDE:-$CRG_ANL_ROOT}"
        
        echo "Running codegraph search on: $ROOT_DIR"
        echo ""
        
        if command -v cockpit &>/dev/null; then
            "$COCKPIT_PATH" codegraph search --cwd "$ROOT_DIR" \
                -p "function\|class\|interface\|const\|let\|var" || true
        else
            echo "cockpit not found. Install with: npm install -g @surething/cockpit"
        fi
        
        ;;

esac