#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p repos
for name in extract ingest documents web; do
  if [ ! -d "repos/dds-pdf-$name" ]; then
    git clone "https://github.com/TomiCaratti13/dds-pdf-$name.git" "repos/dds-pdf-$name"
  fi
done
