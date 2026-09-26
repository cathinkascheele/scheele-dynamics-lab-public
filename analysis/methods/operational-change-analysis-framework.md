# A Practical Framework for Operational Change Analysis in Complex Infrastructure Systems

## Purpose

This document presents a reusable framework for evaluating operational
changes in infrastructure systems, such as changes to routes, turnaround
locations, stopping patterns, capacity measures, operating plans, or
infrastructure.

The framework was developed through practical analysis of railway
operations data. The underlying principles are applicable to other
networked infrastructure systems.

The central principle is:

> Evaluate where a change appears in the system, whether the spatial
> performance pattern changes, which alternative explanations are
> plausible, and whether the observed difference exceeds normal system
> variation.

------------------------------------------------------------------------

## 1. Start with the intervention

Define the operational change before analysing the data:

-   What changed?
-   When did the change start and end?
-   Which parts of the system were exposed?
-   Which services, units, or areas could plausibly be affected?
-   What mechanism is expected to connect the intervention to system
    performance?

Formulate a simple mechanism-based hypothesis:

> If intervention X affects the system through mechanism Y, change Z is
> expected in these parts of the system.

This creates a clear link between the operational intervention, the
expected mechanism, and the observations used to evaluate it.

------------------------------------------------------------------------

## 2. Define the unit of analysis and the population

Specify what one observation represents, for example:

-   train × station
-   departure
-   day
-   event
-   segment
-   network node

Then define and validate the analytical population explicitly.

For railway data, relevant dimensions may include:

-   train number
-   service or line
-   direction
-   route variant
-   number of stops or observed locations
-   origin and destination
-   regular services versus additional or special services

Special operating periods can introduce new train numbers, service
patterns, and route variants. Revalidate historical filters whenever the
operating regime changes.

------------------------------------------------------------------------

## 3. Perform an explicit data-quality check

At minimum, inspect:

-   date range
-   number of observations
-   number of operational units
-   missing values
-   duplicates
-   invalid timestamps
-   classification errors
-   extreme values
-   geographical consistency

Generate a short validation summary before running the main analysis.

The objective is to understand which data issues could materially affect
the conclusions.

------------------------------------------------------------------------

## 4. Define performance metrics explicitly

For punctuality analysis, for example:

-   delay = actual time − scheduled time
-   early departures or negative values are handled explicitly
-   the punctuality threshold is stated explicitly

Use complementary performance measures where useful:

-   punctuality (%)
-   mean delay
-   median delay
-   tail or extreme-event measures

Punctuality and mean delay describe different properties of the
distribution and are often most informative when evaluated together.

------------------------------------------------------------------------

## 5. Inspect the distribution before trimming

Operational delay distributions are often right-skewed and contain
extreme events.

Before applying a cutoff, inspect statistics such as:

-   mean
-   standard deviation
-   90th percentile
-   95th percentile
-   99th percentile
-   99.5th percentile
-   99.9th percentile
-   maximum

When the objective is to characterise typical system behaviour, a common
percentile cutoff can be used, for example the 99.5th percentile.

Extreme events may represent genuine operational conditions. The
treatment of the tail should therefore follow the analytical objective.

Retain the untrimmed data for robustness checks or dedicated disruption
analysis where appropriate.

------------------------------------------------------------------------

## 6. Start with the spatial performance profile

A single aggregate KPI often hides important structure in networked
infrastructure.

Calculate performance by location or segment and, where relevant, by
direction:

`location → punctuality / delay`

This reveals:

-   where delay accumulates
-   where delay is recovered
-   persistent bottlenecks
-   local deviations
-   endpoint effects
-   whether an intervention changes the overall level or the spatial
    shape of system performance

Analyse directions separately when system dynamics are
direction-dependent.

------------------------------------------------------------------------

## 7. Distinguish level from shape

Two periods can have different average performance while retaining
almost the same spatial profile.

This distinction provides useful information about the system.

### Similar shape, different level

This pattern can indicate a stable underlying spatial structure combined
with generally better or worse operating conditions during one period.

### Changed shape

A change in shape can indicate altered system behaviour, exposure, or
constraints at particular locations.

A useful diagnostic question is:

> Did the intervention shift the overall performance level, or did it
> change where performance is gained or lost within the system?

------------------------------------------------------------------------

## 8. Test the most important alternative explanation

A before/after difference can have several plausible causes.

Common alternative explanations include:

-   seasonality
-   traffic volume
-   timetable changes
-   infrastructure works
-   concurrent operational measures
-   passenger demand
-   weather
-   changes in data quality

Choose comparison periods according to the strongest plausible
alternative explanation.

For example, when an intervention occurs during summer and the
post-intervention reference period is autumn, the corresponding summer
period from an earlier year can provide a useful seasonal control.

A practical comparison structure can include:

-   intervention period
-   post-intervention or normal-operation period
-   same season in an earlier year
-   long-term reference profile

------------------------------------------------------------------------

## 9. Build a long-term reference profile

With sufficient historical data, calculate a monthly performance profile
over a longer period.

For each location, calculate:

-   median monthly performance
-   25th percentile (Q25)
-   75th percentile (Q75)

The interquartile range is:

`IQR = Q75 − Q25`

and provides a simple descriptive measure of temporal variation.

### Step 1 -- calculate one value per month

Calculate performance separately for each location and direction for
every month.

For example:

  Month        Location A   Location B   Location C
  ---------- ------------ ------------ ------------
  Jan 2024            91%          89%          87%
  Feb 2024            92%          90%          88%
  Mar 2024            90%          88%          84%
  ...                 ...          ...          ...
  Dec 2025            91%          89%          86%

Two complete years provide up to 24 monthly observations for each
location.

The reference therefore describes variation in **monthly performance
profiles**, rather than treating every underlying operational
observation as an independent reference point.

### Step 2 -- estimate typical monthly performance

For each location, calculate the median of the monthly values.

If the median punctuality at a location is 90%, this can be interpreted
as a typical monthly performance level of approximately 90%.

The median is relatively robust to individual unusually good or poor
months.

Calculating the median at every location produces a **typical spatial
performance profile** for the system.

### Step 3 -- describe normal month-to-month variation

Q25 and Q75 describe the middle 50% of the monthly observations.

For example:

-   Q25 = 88%
-   median = 90%
-   Q75 = 92%

Half of the observed months lie between 88% and 92%.

This interval can be plotted as a band around the median spatial
profile.

### Step 4 -- interpret the IQR

For the example above:

`IQR = 92 − 88 = 4 percentage points`

A narrow IQR band indicates relatively stable monthly performance at
that location.

A wide IQR band indicates greater month-to-month variation.

This provides context for an intervention-period deviation. A
three-percentage-point difference can be unusual at a highly stable
location and ordinary at a location with substantial historical
variation.

The long-term reference therefore supports a more useful question:

> How large is the observed difference relative to the variation
> normally seen in this part of the system?

### Important interpretation

The Q25--Q75 band is a descriptive historical variation band, not a
confidence interval.

It describes how monthly performance has varied in the observed history.
It does not represent statistical uncertainty around a causal-effect
estimate.

------------------------------------------------------------------------

## 10. Define common exposure

When an intervention changes route length or geographical exposure,
total before/after KPIs may represent different operating conditions.

For example, if period A terminates at node X while period B continues
to node Y, period A may show better endpoint performance because it is
no longer exposed to segment X--Y.

Separate the analysis into:

1.  **common exposure** -- the part of the system shared by both
    operating regimes
2.  **changed tail or segment** -- the part present in only one regime

This makes it possible to distinguish system-wide performance changes
from changes caused by reduced or altered exposure.

------------------------------------------------------------------------

## 11. Quantify small visual differences

When plotted profiles appear nearly identical, calculate the differences
explicitly.

For example:

`Δ punctuality = intervention − reference`

`Δ delay = intervention − reference`

A compact summary table can be useful:

  Direction   Comparison                          Δ punctuality   Δ delay
  ----------- --------------------------------- --------------- ---------
  A           intervention − seasonal control               ...       ...
  A           intervention − post-period                    ...       ...
  B           intervention − seasonal control               ...       ...
  B           intervention − post-period                    ...       ...

Effect size provides the quantitative context needed to interpret small
visible separations between curves.

------------------------------------------------------------------------

## 12. Test spatial consistency

An average effect can hide opposing local changes.

Calculate the difference at each location:

`Δ_i = KPI_intervention,i − KPI_reference,i`

Plot the differences around a zero reference line.

### Interpretation

-   **Consistent sign across locations:** evidence of a small but
    spatially systematic difference may be present.
-   **Positive and negative values around zero:** the average difference
    is unlikely to represent a uniform system-wide shift.
-   **A spatial gradient:** this can motivate further investigation of
    propagation, local exposure, or another spatial mechanism.

This step connects aggregate effect size with the spatial structure of
the network.

------------------------------------------------------------------------

## 13. Use cause data diagnostically

Cause data become particularly useful after the main analysis identifies
a pattern that requires explanation.

For an identified deviation, examine at least two dimensions:

### Frequency

How many events or registrations are associated with each cause?

### Consequence

How many delay minutes are associated with each cause?

Together, these distinguish:

-   frequent low-impact events
-   rare high-impact events
-   causes with disproportionately large system consequences

A further descriptive measure can be:

`delay minutes / registration`

Interpret this measure in the context of how cause registrations are
generated and attributed operationally.

------------------------------------------------------------------------

## 14. Distinguish primary events from propagation

In complex operational systems, the registered primary cause may
represent only the first stage of the total system effect.

A local disturbance can propagate through system interactions:

`primary event → local delay → conflict/capacity constraint → secondary delay → further propagation`

Two periods with similar numbers of primary events can therefore produce
very different total performance.

Relevant extensions include:

-   primary delay minutes versus secondary delay minutes
-   number of primary events versus total consequence
-   consequence per event
-   downstream geographical effects
-   time-lagged propagation

This provides a natural transition from descriptive operational analysis
to dynamic and network-based modelling.

------------------------------------------------------------------------

## 15. Separate observation, interpretation, and mechanism

Structure reporting at three levels.

### Observation

> Punctuality was 3.4 percentage points higher.

### Interpretation

> The difference is substantially smaller when the same season in the
> previous year is used as the reference.

### Mechanism hypothesis

> Seasonal operating conditions may account for a substantial part of
> the observed difference.

This structure keeps measured results, analytical interpretation, and
proposed mechanisms clearly separated.

------------------------------------------------------------------------

## 16. Use an evidence ladder

### Strongly supported

Directly observed and robust across relevant comparisons and checks.

### Indication

A pattern is present, with plausible alternative explanations remaining.

### Not identifiable from the current design

The available data and comparison design cannot distinguish between
competing explanations.

A valid operational-analysis conclusion can therefore be:

> The analysis provides no evidence of a substantial system-wide effect
> within the analysed part of the network.

This describes the evidential result without treating an undetected
effect as proof of an exact zero effect.

------------------------------------------------------------------------

## 17. Use a stopping rule

Exploratory operational data can generate many potentially interesting
analytical branches.

Before opening a new branch, ask:

1.  Could this realistically change the main conclusion?
2.  Does an existing finding require an explanation?
3.  Is this needed to answer the analytical question?
4.  Is it primarily an interesting side finding?

Items in the fourth category can be parked for later work.

A dedicated section such as:

`Exploratory findings – outside the main analysis`

preserves useful observations while keeping the primary analysis
focused.

------------------------------------------------------------------------

## 18. Recommended analysis pipeline

A reusable workflow can be organised as follows:

1.  **Operational question and mechanism hypothesis**
2.  **Intervention period**
3.  **Population and route variants**
4.  **Data-quality validation**
5.  **Delay distribution and tail behaviour**
6.  **Aggregate performance metrics**
7.  **Spatial profile by direction**
8.  **Common exposure**
9.  **Seasonal or other relevant control**
10. **Long-term reference and variation band**
11. **Quantified effect size**
12. **Location- or segment-level consistency**
13. **Targeted cause analysis where useful**
14. **Robustness checks**
15. **Conclusion at the appropriate evidence level**
16. **Park additional hypotheses**

Once the data structure and analytical code are established, this
workflow can support relatively rapid evaluation of new operational
changes. The time required depends primarily on data quality,
comparability, and the complexity of the operational question.

------------------------------------------------------------------------

## 19. Reusable visual outputs

A standard set of figures can include:

### Data quality

-   delay distribution
-   percentile / tail inspection

### Main analysis

-   punctuality across the system by direction
-   mean delay across the system by direction

### Reference profiles

-   intervention period
-   post-intervention / normal-operation period
-   seasonal control
-   long-term median reference

### Robustness

-   long-term median profile with IQR band
-   location-level differences around zero

### Diagnostic analysis

-   cause frequency
-   delay minutes by cause
-   delay minutes per registration
-   primary versus secondary delay

------------------------------------------------------------------------

## 20. Generalisation to complex infrastructure systems

The underlying system logic can be expressed as:

`network → exposure → local constraints → disturbance → accumulation → propagation → system performance`

This framework is relevant to systems such as:

-   railways
-   power grids
-   water distribution
-   telecommunications
-   logistics networks
-   other capacity-constrained infrastructure systems

The domain-specific mechanisms differ, while many analytical questions
remain similar:

-   Where does the deviation originate?
-   How does it propagate?
-   Which spatial patterns are stable?
-   What represents normal temporal variation?
-   How does exposure change?
-   When does a local event become a system-level disturbance?
-   How robust is the system to perturbations?

These questions provide a bridge between operational data analysis and
mechanism-based modelling of complex networks.
