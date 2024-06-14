import argparse
import json
import sys
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

import pytest


class JsonReporter:
  def __init__(self):
    self.testcases = []

  def pytest_runtest_logreport(self, report):
    if report.when == "call":
      test_result = {
        "name": report.nodeid,
        "hidden": False,  # Adjust based on your requirement
        "private": False,  # Adjust based on your requirement
        "score": 1 if report.passed else 0,
        "min_score": 0,  # Adjust based on your requirement
        "max_score": 1,  # Adjust based on your requirement
        "ok": True,
        "passed": report.passed,
        "feedback": report.longreprtext if report.failed else "Well done",
        "expected": "",  # Optionally fill this field
        "observed": "",  # Optionally fill this field
        "expand_feedback": True,
      }
      self.testcases.append(test_result)

  def generate_feedback(self, report):
    if report.passed:
      return "Well done"
    else:
      longrepr = str(report.longrepr)
      if "assert" in longrepr:
        try:
          # Extract the failing assertion details
          lines = longrepr.split("\n")
          assert_line = next(
            line for line in lines if line.strip().startswith("assert")
          )
          expected, observed = assert_line.split("==")
          expected = expected.strip().split()[-1]
          observed = observed.strip().split()[0]
          return f"Calling factorial({expected}) returned {observed} when {expected} was expected."
        except Exception:
          return longrepr
      return report.longreprtext

  def generate_report(self):
    return json.dumps({"testcases": self.testcases}, indent=4)


def run_pytest(verbose):
  reporter = JsonReporter()

  if not verbose:
    # Redirect stdout and stderr to suppress pytest output
    with StringIO() as buf, redirect_stdout(buf), redirect_stderr(buf):
      _ = pytest.main(["--tb=short", "--disable-warnings"], plugins=[reporter])
  else:
    _ = pytest.main(["--tb=short", "--disable-warnings"], plugins=[reporter])
  json_output = reporter.generate_report()
  print(json_output)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description="Run pytest and generate JSON report."
  )
  parser.add_argument(
    "--verbose", action="store_true", help="Enable verbose output"
  )
  args = parser.parse_args()

  exit_code = run_pytest(args.verbose)
  sys.exit(exit_code)