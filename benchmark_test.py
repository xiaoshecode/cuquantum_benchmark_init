"""Run bounded cuQuantum QFT benchmarks without executing on import."""

import argparse
import math
import subprocess
import time


def run_benchmarks(start_qubits=1, max_qubits=32, timeout_seconds=300):
    """Return 0 on completion, 124 on timeout, or the benchmark's error code."""
    if (
        start_qubits < 1
        or max_qubits < start_qubits
        or not math.isfinite(timeout_seconds)
        or timeout_seconds <= 0
    ):
        raise ValueError("Require 1 <= start_qubits <= max_qubits and timeout_seconds > 0")
    for nqubits in range(start_qubits, max_qubits + 1):
        command = [
            "cuquantum-benchmarks",
            "circuit",
            "--benchmark",
            "qft",
            "--frontend",
            "pennylane",
            "--backend",
            "pennylane-lightning-gpu",
            "--nqubits",
            str(nqubits),
            "--ngpus",
            "1",
        ]
        print(f"Running benchmark with nqubits = {nqubits}...", flush=True)
        started = time.monotonic()
        try:
            subprocess.run(command, check=True, timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            print(f"Benchmark exceeded {timeout_seconds:g} seconds; stopping.")
            return 124
        except subprocess.CalledProcessError as error:
            print(f"Benchmark failed with exit code {error.returncode}.")
            return error.returncode
        except FileNotFoundError:
            print("cuquantum-benchmarks was not found; activate its installed environment.")
            return 127
        print(f"Elapsed time: {time.monotonic() - started:.2f} seconds")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-qubits", type=int, default=1)
    parser.add_argument("--max-qubits", type=int, default=32)
    parser.add_argument("--timeout", type=float, default=300, help="Seconds per benchmark")
    args = parser.parse_args(argv)
    try:
        return run_benchmarks(args.start_qubits, args.max_qubits, args.timeout)
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
