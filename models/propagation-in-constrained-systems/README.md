# Propagation in Constrained Systems

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

- `conceptual-propagation-model-v0.md`
  Aggregate conceptual model of disturbance accumulation and secondary propagation.

- `conceptual-propagation-model-v1.md`
  Extension introducing state-dependent amplification effects.

- `structural-propagation-model-v2.md`
  Structural propagation model based on coupling exposure and constrained flow.
- `scripts/`
  Prototype implementations and exploratory model scripts.

- `visualizations/`
  Conceptual diagrams, synthetic outputs, and exploratory visualizations.

## Status

Early-stage exploratory model development.

Three initial representations have been sketched, with synthetic examples used to illustrate possible outputs. Current implementations are simple and deterministic, and are intended as a starting point for further modelling and literature review.
