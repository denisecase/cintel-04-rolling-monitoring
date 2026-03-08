# Apply Ideas

Technique: Observe system behavior over time using rolling windows or moving averages.

Rolling calculations help smooth short-term variation and reveal longer-term patterns.

A good dataset for this module:

- contains observations ordered over time
- includes repeated measurements

## Example Systems

### Website Visits

Possible fields:

- timestamp
- visits

Questions to explore:

- What does a rolling average reveal about traffic trends?
- Are there periods of unusually high activity?

### Energy Demand

Possible fields:

- timestamp
- demand_mw

Questions to explore:

- Do rolling averages reveal peak usage patterns?
- Are there seasonal or daily cycles?

### Public Transit Ridership

Possible fields:

- date
- rides

Questions to explore:

- How does ridership change across days or weeks?
- Do rolling averages reveal longer trends?

### Application Response Time

Possible fields:

- timestamp
- latency_ms

Questions to explore:

- Does system performance degrade during certain periods?
- Do rolling metrics reveal slow trends not visible in individual observations?

### Temperature Monitoring

Possible fields:

- timestamp
- temperature

Questions to explore:

- How do rolling averages change across time?
- Are there patterns across days or seasons?
