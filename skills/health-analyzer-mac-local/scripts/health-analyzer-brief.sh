#!/bin/bash
set -euo pipefail

HELPER_CANDIDATES=(
  "$HOME/Library/Containers/com.rumjahn.healthkitanalyzer/Data/Library/Application Support/Health Data AI Analyzer/bin/health-analyzer-brief"
  "$HOME/Library/Application Support/Health Data AI Analyzer/bin/health-analyzer-brief"
)

HELPER=""

for candidate in "${HELPER_CANDIDATES[@]}"; do
  if [[ -f "$candidate" ]]; then
    HELPER="$candidate"
    break
  fi
done

if [[ -z "$HELPER" ]]; then
  echo "Helper not found. Open Health Data AI Analyzer once so it can install the bundled helper." >&2
  echo "Checked:" >&2
  for candidate in "${HELPER_CANDIDATES[@]}"; do
    echo "  - $candidate" >&2
  done
  exit 1
fi

exec /bin/bash "$HELPER" "$@"
