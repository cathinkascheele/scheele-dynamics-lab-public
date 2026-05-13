# Propagation in Constrained Systems

## Model Development

The model was developed iteratively through exploratory analysis, qualitative observation, and gradual abstraction of recurring system behavior.

Early exploratory work focused on identifying possible propagation drivers, recurrent system patterns, and mechanisms that could explain why similar disturbances sometimes produced very different system-level outcomes.

Initial analysis combined aggregated performance metrics, temporal comparisons, localized inspection of operational behavior, and integration of partially connected data sources through shared operational identifiers.

Several early observations suggested that propagation behavior could not be explained by isolated disturbance magnitude alone, but appeared to emerge through constrained coupling opportunities shaped by timing, system state, load, and network structure.

Exploratory analysis further suggested that aggregated performance metrics and isolated cause categories were often informative at the local level, but less sufficient for explaining propagation behavior across highly coupled system states. Similar aggregate outcomes could arise through fundamentally different interaction patterns depending on topology, temporal clustering, capacity constraints, and accumulated operational stress.

As model development progressed, parts of the emerging hypotheses were compared against literature related to nonlinear dynamics, propagation in coupled systems, and agent-based representations of operational behavior.

These observations motivated the development of increasingly structure-oriented models intended to represent propagation, coupling, and state-dependent system behavior more explicitly.

Development proceeded through successive abstraction stages:

1. exploratory observation of recurring propagation patterns
2. qualitative hypothesis development
3. aggregate conceptual models of disturbance accumulation
4. state-dependent amplification models
5. structural propagation models incorporating coupling exposure, bottlenecks, and constrained flow

## Scope

The model is intended to explore how propagation emerges in constrained and coupled systems, and how such mechanisms can be represented in an interpretable structural form.

The focus is not full system replication or direct prediction, but the development of model structures that can support:

- propagation impact scores
- ranking of agents, locations, or events by system-level exposure
- identification of vulnerable timing–location combinations
- analysis of threshold behavior and cascade regimes
- comparison between local event size and system-level effect
- exploratory visualizations for operational interpretation

In an operational setting, such outputs could support real-time situational awareness or retrospective impact analysis. In this repository, current examples are treated as conceptual and exploratory rather than validated operational decision tools.

## Contents

- `conceptual-model-v0.md`  
  Aggregate conceptual model of disturbance accumulation and secondary propagation.

- `conceptual-model-v1.md`  
  Extension introducing state-dependent amplification effects.

- `structural-model-v2.md`  
  Structural propagation model based on coupling exposure and constrained flow.

- `minimal-proxy.md`  
  Minimal proxy system illustrating propagation and absorption mechanisms.

- `scripts/`  
  Prototype implementations and exploratory model scripts.

- `visualizations/`  
  Conceptual diagrams, proxy outputs, animations, and exploratory visualizations.
