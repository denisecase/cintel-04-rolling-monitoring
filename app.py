"""app.py - Reactive marimo app for this project.

Marimo adds reactive controls.
Every function below is a marimo cell.

RUN LOCALLY:

  uv run marimo edit app.py     # edit
  uv run marimo run  app.py     # run as an app (CTRL+c quits)

WASM DEPENDENCIES:

Under WebAssembly (emscripten) the browser has no project environment.
This app uses polars in addition to marimo, so the first cell installs
polars with micropip when running under WASM.

NO LOGGING:

A browser-based WASM app has no persistent Python server to store log files,
so this notebook configures no logging.

PLAN CELLS FIRST

1. Imports (installs WASM deps, returns shared imports and constants)
2. Opening title and introduction (Markdown)
3. Load and sort the time-series data (same cell handles local and WASM
   environments, via cintel.utils_system)
4. Window size control (slider)
5. Compute rolling means (same logic as the CLI pipeline)
6. Show the rolling metrics table
7. Closing (Markdown)

Note: marimo triggers @app.cell functions automatically; we never call them.
The names starting with "_" are for our own organization; the engine ignores
them.
"""

# === ONLY THIS AT THE TOP OF THE FILE ===

import marimo

__generated_with = "0.25.0"

app = marimo.App(width="medium")

# === FIRST CELL IMPORTS AND RETURNS DEPENDENCIES TO MAKE IT SELF-CONTAINED ===


@app.cell
async def _():
    import sys

    if sys.platform == "emscripten":
        import micropip

        await micropip.install("polars")

    import marimo as mo
    import polars as pl

    from cintel.utils_system import compute_rolling_metrics, load_timeseries_metrics

    return compute_rolling_metrics, load_timeseries_metrics, mo, pl, sys


# === TITLE AND INTRODUCTION ===


@app.cell
def _(mo):
    mo.md(r"""
    # Rolling Monitoring

    A single observation can be noisy. A rolling average smooths short-term
    variation so longer-term trends stand out. Move the slider to see how
    window size changes what the data reveals.
    """)


# === LOAD AND SORT THE TIME-SERIES DATA ===


@app.cell
def _(load_timeseries_metrics, mo, sys):
    """Load the time-series data. Two environments, one cell.

    Locally, polars reads the CSV from data/.
    Under WASM (emscripten), Pyodide's open_url() fetches the CSV from
    public/ and load_timeseries_metrics() reads and sorts it from there
    instead.
    """
    notebook_location = mo.notebook_location()

    if notebook_location is None:
        raise RuntimeError("Unable to determine notebook location.")

    filename = "system_metrics_timeseries.csv"

    if sys.platform == "emscripten":
        from pyodide.http import open_url  # ty: ignore[unresolved-import]

        data_url = notebook_location / "public" / filename
        df = load_timeseries_metrics(open_url(str(data_url)))
    else:
        data_path = notebook_location.parents[1] / "data" / filename
        df = load_timeseries_metrics(data_path)

    return (df,)


# === WINDOW SIZE CONTROL ===


@app.cell
def _(mo):
    window_size = mo.ui.slider(1, 10, value=3, label="Rolling window size (rows)")
    window_size  # noqa: B018 (marimo often uses standalone expressions)
    return (window_size,)


# === COMPUTE ROLLING MEANS (SAME LOGIC AS THE CLI PIPELINE) ===


@app.cell
def _(compute_rolling_metrics, df, window_size):
    df_with_rolling = compute_rolling_metrics(df, window_size.value)
    return (df_with_rolling,)


# === SHOW THE ROLLING METRICS TABLE ===


@app.cell
def _(df_with_rolling, mo):
    mo.ui.table(df_with_rolling)


# === TYPICALLY END WITH A MARKDOWN SOURCE LINK AND CLOSING ===


@app.cell
def _(mo):
    mo.md(r"""
    ---
    [😊 Learn more at marimo.io](https://marimo.io/)
    ---

    **Running locally?**
    To stop the app, click in the VS Code terminal,
    then press **CTRL** and **c** together (CTRL+c).
    When it asks "Are you sure you want to quit? (y/N)",
    type **y** and press **Enter**.
    ---
    """)


if __name__ == "__main__":
    app.run()
