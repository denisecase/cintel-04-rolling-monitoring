# Project Instructions

## Goal

Apply **rolling monitoring** to examine how system behavior
changes across successive observations.

## A. Set Up Machine

Complete [Workflow A: Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
if your machine is not ready.

## B. Explore Example Project

Follow [Workflow B: Explore Example Project](https://denisecase.github.io/pro-analytics-02/workflow-b-explore-example-project/).

Explore how the example:

- Reads time-series system metrics.
- Sorts observations by timestamp.
- Defines a rolling window size.
- Calculates rolling averages using Polars.
- Saves rolling monitoring results as an artifact.

Notice how changing the window size affects
the calculated results.

## C. Start New Project

Follow [Workflow C: Start New Project](https://denisecase.github.io/pro-analytics-02/workflow-c-start-new-project/).

IMPORTANT: New repository name:
**cintel-04-rolling-monitoring-custom**.

VERIFY: You have completed git add-commit-push to GitHub at least twice.

## D. Apply Skills

Follow [Workflow D: Apply Skills](https://denisecase.github.io/pro-analytics-02/workflow-d-apply-skills/).

**Your problem:** Identify periods of worsening
system reliability using rolling error rates.

You may use the example time-series dataset
or choose another suitable time series.

### Progression 1. Your Project Works Like the Example

Ensure your new custom project runs like the example.

Verify that key files have been updated to use **your GitHub account** and
the **new custom repository name**.

### Progression 2. Make a Technical Modification

Change the rolling window size.

For example, compare windows of 3 and 5 observations.

Observe how the change affects the results.

### Progression 3. Apply to a New Problem

Investigate whether rolling error rates reveal
periods of worsening reliability.

- Calculate error rate for each observation.
- Compute rolling averages of error rate.
- Compare at least two window sizes.
- Identify patterns or periods of concern.
- Save the rolling signals as artifacts.
- Explain which window size is more useful and why.

A larger window may reduce short-term variation
but respond more slowly to changing conditions.

## E. Finalize Project

Follow [Workflow E: Finalize Project](https://denisecase.github.io/pro-analytics-02/workflow-e-finalize/).

Use `docs/index.md` to report:

- Data and observation intervals.
- Rolling signals and window sizes.
- Technical modifications.
- Results and a time-series visual.
- Patterns observed and their interpretation.
- Limitations and possible improvements.

Include a clickable link to your repository and artifacts.

## Success

- [ ] README.md project-specific links use **your GitHub account**
- [ ] README.md project-specific links use **your custom repository name**.
- [ ] docs/index.md project-specific links use **your GitHub account**
- [ ] docs/index.md project-specific links use **your custom repository name**.
- [ ] pyproject.toml `name` has been changed to use **your custom repository name**.
- [ ] The `src/cintel` folder reflects your authorship and custom work.
- [ ] All necessary commands are provided and work successfully.
- [ ] Links to the Professional Python Guide (pro-analytics-02) remain unchanged.
- [ ] Commit history shows **at least** the git add-commit-push history required in the instructions.

---

[◄ Back to Home](index.md)
