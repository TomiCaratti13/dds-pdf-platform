#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
mkdir -p results
target="$(mktemp)"
trap 'rm -f "$target"' EXIT
for n in 1 2 3 4; do
  printf 'POST %s/extract\nContent-Type: application/pdf\n@%s/tests/stress/pdfs/%s.pdf\n\n' "${BASE_URL:-http://localhost:8081}" "$(pwd)" "$n" >> "$target"
done
vegeta attack -targets="$target" -rate=50/s -duration=30s -timeout=30s > results/vegeta.bin
vegeta report results/vegeta.bin
vegeta report -type=json results/vegeta.bin > results/vegeta.json
