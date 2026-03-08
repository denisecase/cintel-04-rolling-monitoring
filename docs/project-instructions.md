# Project Instructions

## WEDNESDAY: Complete Workflow Phase 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/).

Complete:

1. Phase 1. **Start & Run** – copy the project and confirm it runs
2. Phase 2. **Change Authorship** – update the project to your name and GitHub account
3. Phase 3. **Read & Understand** – review the project structure and code

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Complete:

1. Phase 4. **Make a Technical Modification**
2. Phase 5. **Apply the Skills to a New Problem**

3. Phase 2. **Change Authorship** – update the project to your name and GitHub account
4. Phase 3. **Read & Understand** – review the project structure and code

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Complete:

1. Phase 4. **Make a Technical Modification**
2. Phase 5. **Apply the Skills to a New Problem**

## Topic

Rolling monitoring using moving window statistics.

In this project, you will monitor how system behavior changes over time by computing **rolling averages** of key metrics.

Rolling statistics help analysts smooth short-term noise and detect patterns that develop across time.

## Learning Objectives

After completing this project, you should be able to:

- Explain why analysts use rolling statistics for monitoring
- Compute rolling averages for system metrics
- Add rolling signals to a DataFrame
- Run and validate a professional Python project
- Interpret how behavior evolves across observations

## Example Code

The example file is located in:

```
src/cintel/rolling_monitor_case.py
```

It demonstrates:

- reading system metrics from a CSV file
- defining a rolling window size
- computing rolling averages for multiple metrics
- adding rolling signals to a DataFrame
- writing monitoring outputs to an artifacts file
- logging the pipeline process

Run the example and review the code before creating your own version.

## Dataset

The example dataset is located in the `data/` folder.

Example fields include:

- `requests`
- `errors`
- `total_latency_ms`

Each row represents one **system observation**.

Rolling monitoring computes statistics across the most recent observations to help reveal trends.

## Your Phase 4: Technical Modification Task

Using the example as a guide:

1. Copy `src/cintel/rolling_monitor_case.py`.
2. Rename the copy to `src/cintel/rolling_monitor_yourname.py`.
3. Run your copied file to confirm it executes correctly.
4. Modify the program by changing or extending the rolling monitoring logic.

Possible modifications include:

- changing the rolling window size
- adding a rolling statistic for another metric
- computing a rolling minimum, maximum, or median
- monitoring an additional column

Then:

- run the project
- confirm the new rolling signals appear in the output artifact
- confirm the program logs useful messages

The goal of this phase is to practice modifying a working monitoring pipeline.

## Phase 5: Apply the Skills

In Phase 5 you will apply rolling monitoring to a new situation.

Possible approaches include:

- applying rolling monitoring to a different dataset
- monitoring additional system signals
- experimenting with different window sizes
- analyzing how rolling signals change over time

Update your documentation in `docs/` to explain:

- what rolling signals you created
- what window size you used
- what patterns you observed
- what the signals reveal about system behavior

Rolling monitoring is a core component of **continuous intelligence systems**, where analysts observe how system behavior evolves over time.

If you would like to apply these skills to a real dataset instead of the provided example data, see suggested datasets:

https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/


---

## Note on Progress

Earlier approaches to rolling monitoring often required managing the window manually.
For example, a Python implementation might use a **deque** data structure
to store the most recent values and update the rolling window as new observations arrive.

Modern data tools make this much simpler.

Libraries such as **Polars** provide the **built-in rolling window operations** used in this module.
Instead of managing the window directly, we just **describe the calculation (the _recipe_)**, and the library efficiently performs the computation _across the entire dataset_.

If this project appears a bit simple or straightforward,
it is partly because the tools have improved considerably.
See what you can do with these powerful tools.

Continuing education and staying current with evolving data tools
is an investment that pays off,
often significantly enhancing the efficiency and maintainability of our projects.
