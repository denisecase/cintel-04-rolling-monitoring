"""
rolling_monitor_case.py - Project script (example).

Author: Denise Case
Date: 2026-03

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

    INPUT FILE: data/system_metrics_timeseries_case.csv
    OUTPUT FILE: artifacts/rolling_metrics_case.csv

Terminal command to run this file from the root project folder

    uv run python -m cintel.rolling_monitor_case

OBS:
  Don't edit this file - it should remain a working example.
  Use as much of this code as you can when creating your own pipeline script,
  and change the monitoring logic as needed for your project.
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P5", level="DEBUG")

# === DEFINE GLOBAL PATHS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "system_metrics_timeseries_case.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "rolling_metrics_case.csv"

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
    # STEP 1: READ CSV DATA FILE INTO A POLARS DATAFRAME (TABLE)
    # ----------------------------------------------------
    df = pl.read_csv(DATA_FILE)

    LOG.info(f"Loaded {df.height} time-series records")

    # ----------------------------------------------------
    # STEP 2: SORT DATA BY TIME
    # ----------------------------------------------------
    # Time-series analysis requires observations to be ordered.
    df = df.sort("timestamp")

    LOG.info("Sorted records by timestamp")

    # ----------------------------------------------------
    # STEP 3: DEFINE ROLLING WINDOW RECIPES
    # ----------------------------------------------------
    # A rolling window computes statistics over the most recent
    # N observations. The window "moves" forward one row at a time.

    # Example: if WINDOW_SIZE = 3
    # row 1 → mean of rows [1]
    # row 2 → mean of rows [1,2]
    # row 3 → mean of rows [1,2,3]
    # row 4 → mean of rows [2,3,4]

    WINDOW_SIZE: int = 3

    # ----------------------------------------------------
    # STEP 3.1: DEFINE ROLLING MEAN FOR # OF REQUESTS
    # ----------------------------------------------------
    # The `requests` column holds the count of requests handled at each timestamp.
    requests_rolling_mean_recipe: pl.Expr = (
        pl.col("requests").rolling_mean(WINDOW_SIZE).alias("requests_rolling_mean")
    )

    # ----------------------------------------------------
    # STEP 3.2: DEFINE ROLLING MEAN FOR # OF ERRORS
    # ----------------------------------------------------
    # The `errors` column holds the count of errors encountered at each timestamp.
    errors_rolling_mean_recipe: pl.Expr = (
        pl.col("errors").rolling_mean(WINDOW_SIZE).alias("errors_rolling_mean")
    )

    # ----------------------------------------------------
    # STEP 3.3: DEFINE ROLLING MEAN FOR LATENCY
    # ----------------------------------------------------
    # The `total_latency_ms` column holds the total latency in milliseconds at each timestamp.
    latency_rolling_mean_recipe: pl.Expr = (
        pl.col("total_latency_ms")
        .rolling_mean(WINDOW_SIZE)
        .alias("latency_rolling_mean")
    )

    # ----------------------------------------------------
    # STEP 3.4: APPLY THE ROLLING RECIPES IN A NEW DATAFRAME
    # ----------------------------------------------------
    # with_columns() evaluates the recipes and adds the new columns
    df_with_rolling = df.with_columns(
        [
            requests_rolling_mean_recipe,
            errors_rolling_mean_recipe,
            latency_rolling_mean_recipe,
        ]
    )

    LOG.info("Computed rolling mean signals")

    # ----------------------------------------------------
    # STEP 4: SAVE RESULTS AS AN ARTIFACT
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
