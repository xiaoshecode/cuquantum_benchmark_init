#!/usr/bin/env bash
set -euo pipefail

# Override these variables in the environment for a single run.
BENCHMARK_NAME=${BENCHMARK_NAME:-random}
NUM_QUBITS=${NUM_QUBITS:-20}

exec cuquantum-benchmarks circuit \
    --frontend qiskit \
    --backend aer \
    --benchmark "$BENCHMARK_NAME" \
    --nqubits "$NUM_QUBITS" "$@"
