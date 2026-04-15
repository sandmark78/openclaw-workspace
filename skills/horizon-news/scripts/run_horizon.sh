#!/bin/bash
# Run Horizon news aggregation from the workspace
# Usage: run_horizon.sh [--hours N]
set -euo pipefail

HORIZON_DIR="/home/node/.openclaw/workspace/Horizon"
DATA_DIR="${HORIZON_DIR}/data"

# Ensure data dirs exist
mkdir -p "${DATA_DIR}/summaries"

# Check config exists
if [ ! -f "${DATA_DIR}/config.json" ]; then
    echo "ERROR: ${DATA_DIR}/config.json not found"
    echo "Run: cp ${DATA_DIR}/config.example.json ${DATA_DIR}/config.json"
    echo "Then edit config.json with your settings"
    exit 1
fi

# Check .env exists
if [ ! -f "${HORIZON_DIR}/.env" ]; then
    echo "ERROR: ${HORIZON_DIR}/.env not found"
    echo "Run: cp ${HORIZON_DIR}/.env.example ${HORIZON_DIR}/.env"
    echo "Then add your API key (DASHSCOPE_API_KEY)"
    exit 1
fi

cd "${HORIZON_DIR}"

# Install deps if needed (first run)
if ! command -v uv &>/dev/null; then
    echo "Installing uv..."
    pip install uv 2>/dev/null || true
fi

# Sync deps
uv sync 2>/dev/null || pip install -e . 2>/dev/null

# Run Horizon
exec uv run horizon "$@"
