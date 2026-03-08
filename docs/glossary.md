# Glossary

## Quick Lookup

Common terms used in this module:

- **Rolling Window** - a moving subset of the most recent observations used to compute statistics
- **Rolling Mean** - the average of values within a rolling window
- **Window Size** - the number of observations included in the rolling calculation
- **Signal** - a derived metric created to better understand system behavior
- **Rolling Signal** - a signal computed across recent observations to smooth noise
- **Monitoring** - observing system behavior over time using metrics and signals

## Rolling Window

A rolling window calculates statistics using the most recent **N observations**.
The window "moves" forward one row at a time.
Example (window size = 3):

```
row 1 → mean of [1]
row 2 → mean of [1,2]
row 3 → mean of [1,2,3]
row 4 → mean of [2,3,4]
```

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
