# Propagation in Constrained Systems

## Status

> **Early-stage exploratory model development**
>
> Model v0 is conceptually complete for its current scope and includes a small numerical illustration of persistence behaviour.
>
> Model v1 is an early working hypothesis exploring state-dependent sensitivity and has not yet been systematically tested with respect to parameter behaviour, limiting cases, or alternative functional forms.
>
> Model v2 is an exploratory structural playground investigating a substantially different representation based on local capacity pressure, spatial structure, and coupling exposure. Its role and relationship to the earlier models remain open.
>
> Further work will include literature review, comparison with established model classes, and more systematic evaluation of which representations and mechanisms are useful to retain.

<br>

<br>


## Model development

The project originated in exploratory operational analysis where aggregated indicators and event-level summaries provided limited insight into differences in underlying system behaviour.

Similar patterns of poor system performance could arise from very different combinations of underlying events — sometimes without any single event providing a convincing explanation. Conversely, apparently similar local disturbances could be associated with very different downstream outcomes depending on the surrounding operational conditions.

This led me to explore whether a different representation of the same operational behaviour might make the underlying relationships easier to understand, which became the starting point for an independent modelling process.

An early, tentative modelling hypothesis was that observed outcomes may depend more on the state of the system in which they occur, the structural position of the affected part of the network, and the dependencies and coupling through which effects can propagate, rather than on the magnitude of individual disturbances alone.

Delay propagation is already a well-established area of railway research, spanning analytical, dynamical, network-based, simulation and data-driven approaches. This makes it a useful setting in which to explore a broader modelling question:

<br>

> **What must a minimal representation preserve in order to meaningfully study delay propagation?**

<br>

## Scope

The project explores how propagation can be represented in constrained and coupled systems using relatively small, interpretable models.

Such representations could be used to explore:

- whether some system states or structural configurations are more vulnerable to propagation than others
- which combinations of timing, disturbance patterns, network position, topology and coupling are associated with greater downstream impact
- whether some agents, locations or states consistently show higher propagation potential
- whether impact scores or profiles provide useful ways of summarising that propagation potential
- what is gained or lost when the same propagation problem is represented at different levels of detail

Detailed planning, traffic management and real-time prioritization often rely on larger simulation, optimization or decision-support systems. However, small, transparent models might still be useful as part of an analytical framework for operational analysis and decision support.

## Contents

- `conceptual-model-v0.md`
  Baseline linear discrete-time model of disturbance, background friction, and propagation.

- `conceptual-model-v1.md`
  State-dependent propagation formulation.

- `structural-model-v2.md`
  Structural formulation using local capacity pressure and coupling exposure.

- `scripts/`
  Prototype implementations and exploratory model scripts.

- `visualizations/`
  Model-generated illustrations, synthetic examples, and exploratory visualizations.

## Status

Early-stage exploratory model development.

Three initial representations have been sketched, with synthetic examples used to illustrate possible outputs. Current implementations are simple and deterministic, and are intended as a starting point for further modelling and literature review.
