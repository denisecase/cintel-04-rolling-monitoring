"""rolling_monitor.py - Project script (example).

Author: Your Name Here
Date: 2026-mm-dd

Time-Series System Metrics Data

- Data is taken from a system that records operational metrics over time.
- Each row represents one observation at a specific timestamp.
- The CSV file includes these columns:
  - timestamp: when the observation occurred
  - requests: number of requests handled
  - errors: number of failed requests
  - total_latency_ms: total response time in milliseconds

Purpose

- Read time-series system metrics from a CSV file.
- Demonstrate rolling monitoring using a moving window.
- Compute rolling averages to smooth short-term variation.
- Save the resulting monitoring signals as a CSV artifact.
- Log the pipeline process to assist with debugging and transparency.

Questions to Consider

- How does system behavior change over time?
- Why might a rolling average reveal patterns that individual observations hide?
- How can smoothing short-term variation help us understand longer-term trends?

Paths (relative to repo root)

    INPUT FILE: data/system_metrics_timeseries.csv
    OUTPUT FILE: artifacts/rolling_metrics.csv

Terminal command to run this file from the root project folder

    uv run python -m cintel.rolling_monitor

DESIGN:

Use this file to first learn and then apply your skills.

Reusable functions that do the work are kept in a utils file.
We import functions and pass in what they need through their parentheses.
Shared utility functions can be imported into a Python
module or a reactive marimo notebook app.

Reusable visualization functions may come from sources such as eda-vizkit.

SKILLS:

- Reading CSV files into Polars DataFrames.
- Defining and using constants for window sizes.
- Logging for debugging and transparency.
- Computing rolling averages for time-series analysis.
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
import polars as pl

from cintel.utils_system import compute_rolling_metrics, load_timeseries_metrics

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P4", level="DEBUG")

# === DEFINE GLOBAL PATHS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "system_metrics_timeseries.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "rolling_metrics.csv"

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    # Ensure artifacts directory exists
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # ----------------------------------------------------
    # STEP 1: READ AND SORT THE TIME-SERIES DATA
    # ----------------------------------------------------
    # load_timeseries_metrics() wraps polars' read_csv() and sorts by
    # timestamp — see utils_system.py. Time-series analysis requires
    # observations to be ordered, so the sort happens right where the
    # data is loaded.
    df: pl.DataFrame = load_timeseries_metrics(DATA_FILE)

    LOG.info(f"Loaded {df.height} time-series records, sorted by timestamp")

    # ----------------------------------------------------
    # STEP 2: COMPUTE ROLLING MEANS
    # ----------------------------------------------------
    # A rolling window computes statistics over the most recent
    # N observations. The window "moves" forward one row at a time.

    # Example: if WINDOW_SIZE = 3
    # row 1 → mean of rows [1]
    # row 2 → mean of rows [1,2]
    # row 3 → mean of rows [1,2,3]
    # row 4 → mean of rows [2,3,4]

    WINDOW_SIZE: int = 3

    LOG.info(f"WINDOW_SIZE: {WINDOW_SIZE}")

    # compute_rolling_metrics() adds requests_rolling_mean,
    # errors_rolling_mean, and latency_rolling_mean — see utils_system.py
    # for exactly how each rolling-mean expression is built.
    df_with_rolling: pl.DataFrame = compute_rolling_metrics(df, WINDOW_SIZE)

    LOG.info("Computed rolling mean signals")

    # ----------------------------------------------------
    # STEP 3: SAVE RESULTS AS AN ARTIFACT
    # ----------------------------------------------------
    df_with_rolling.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote rolling monitoring file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
