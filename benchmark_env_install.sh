#!/usr/bin/env bash
set -euo pipefail

# This repository is a runner, not the cuQuantum Benchmarks package itself.
if [[ $# -ne 1 || ! -d "$1" ]]; then
    echo "Usage: bash benchmark_env_install.sh /path/to/cuQuantum/benchmarks" >&2
    exit 2
fi
python -m pip install "${1%/}[all]"
