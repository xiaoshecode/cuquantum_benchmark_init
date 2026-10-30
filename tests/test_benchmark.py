import subprocess
import unittest
from unittest.mock import patch

import benchmark_test


class BenchmarkTests(unittest.TestCase):
    @patch("benchmark_test.subprocess.run")
    def test_bounded_sequence_and_timeout_argument(self, run):
        self.assertEqual(benchmark_test.run_benchmarks(2, 3, 5), 0)
        self.assertEqual(run.call_count, 2)
        self.assertEqual(run.call_args_list[0].args[0][-3], "2")
        self.assertEqual(run.call_args.kwargs, {"check": True, "timeout": 5})

    @patch("benchmark_test.subprocess.run", side_effect=subprocess.TimeoutExpired("bench", 5))
    def test_timeout_stops_sequence(self, run):
        self.assertEqual(benchmark_test.run_benchmarks(1, 4, 5), 124)
        run.assert_called_once()

    @patch("benchmark_test.subprocess.run", side_effect=subprocess.CalledProcessError(7, "bench"))
    def test_failure_propagates(self, run):
        self.assertEqual(benchmark_test.run_benchmarks(), 7)
        run.assert_called_once()

    @patch("benchmark_test.subprocess.run", side_effect=FileNotFoundError)
    def test_missing_command(self, run):
        self.assertEqual(benchmark_test.run_benchmarks(), 127)

    @patch("benchmark_test.subprocess.run")
    def test_invalid_ranges_do_not_start(self, run):
        for args in [(0, 1, 3), (2, 1, 3), (1, 2, 0), (1, 2, float("nan")), (1, 2, float("inf"))]:
            with self.assertRaises(ValueError):
                benchmark_test.run_benchmarks(*args)
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
