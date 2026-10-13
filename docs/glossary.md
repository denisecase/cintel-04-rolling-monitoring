# Glossary

## Quick Lookup

Common terms used in this module:

- **Rolling Window** - a moving subset of the most recent observations used to compute statistics
- **Rolling Mean** - the average of values within a rolling window
- **Window Size** - the number of observations included in the rolling calculation
- **Signal** - a raw or derived metric used to monitor system behavior
- **Rolling Signal** - a signal computed across successive windows of observations to reveal patterns and reduce short-term variation
- **Monitoring** - observing system behavior over time using metrics and signals

## Rolling Window

A rolling window calculates statistics using the most recent **N observations**.
The window moves forward one row at a time.

In this example, a complete window is required before calculating a mean.

Example (window size = 3):

```text
row 1 --> null (not enough observations)
row 2 --> null (not enough observations)
row 3 --> mean of [1, 2, 3]
row 4 --> mean of [2, 3, 4]
```

The first two results are null because fewer than three observations are available.
Once the window is full, each new observation replaces the oldest observation.

## Window Size

The number of observations used in the rolling calculation.
Small windows respond quickly to changes.
Large windows smooth the signal but respond more slowly.

## Monitoring Signal

A metric used to observe system behavior. Examples:

- requests per minute
- error rate
- average latency

## Rolling Monitoring

The process of **computing rolling statistics** to track how system behavior evolves across observations.
Rolling monitoring is a core technique in **continuous intelligence systems**.

---

[◄ Back to 🏠 Home](index.md)
