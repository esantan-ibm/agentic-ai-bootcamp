#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REQ_FILE="${SCRIPT_DIR}/requirements.txt"

# Ensure orchestrate CLI is available
command -v orchestrate >/dev/null 2>&1 || { echo "Error: 'orchestrate' CLI not found in PATH"; exit 1; }

# Ensure requirements.txt exists
[[ -f "${REQ_FILE}" ]] || { echo "Error: requirements.txt not found at ${REQ_FILE}"; exit 1; }

echo "Importing Python tools..."
TOOLS=(
  "risk_analysis_tools.py"
  "kyc_application_tools.py"
  "regulatory_reporting_tools.py"
)

for tool in "${TOOLS[@]}"; do
  orchestrate tools import \
    -k python \
    -f "${SCRIPT_DIR}/tools/${tool}" \
    -r "${REQ_FILE}"
done

echo "Importing agents..."
AGENTS=(
  "customer_risk_profile.yaml"
  "kyc_status.yaml"
  "regulatory_reporting_agent.yaml"
  "compliance_super_agent.yaml"
)

for agent in "${AGENTS[@]}"; do
  orchestrate agents import -f "${SCRIPT_DIR}/agents/${agent}"
done

echo "Import process complete. You can verify with:"
echo "  orchestrate tools list"
echo "  orchestrate agents list"
