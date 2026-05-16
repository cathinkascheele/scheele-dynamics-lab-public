# Propagation in Constrained Systems

## Model development

The current model formulation was developed iteratively through exploratory analysis, qualitative observation, and gradual abstraction of recurring system behavior.

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

---

## Scope

The modeling approach explores how propagation emerges in constrained and coupled systems, and how such mechanisms can be represented in an interpretable structural form.

The focus is not full system replication or direct prediction, but the development of structural models that can support:

- propagation impact scores
- ranking of agents, locations, or events by structural propagation impact
- identification of structurally vulnerable system configurations
- analysis of threshold behavior and cascade regimes
- comparison between local event size and system-level effect
- exploratory visualizations for operational interpretation

A central modeling objective is to investigate whether relatively small and interpretable structural models can later scale toward larger operational systems while still preserving operational usefulness and interpretability.

The intended direction is not hardcoded rule-based scoring, but propagation indicators that emerge from structural relations such as capacity constraints, timing, topology, bottlenecks, and downstream coupling exposure.

In an operational setting, such outputs could potentially support:

- real-time propagation impact scoring
- prioritization of mobile agents under constrained conditions
- identification of structurally vulnerable system configurations
- analysis of how local disturbances generate downstream system effects
- retrospective propagation analysis and operational review
- comparison between local delay magnitude and structural propagation impact
- identification of agents associated with disproportionate downstream system effects

For example, in a transport system, structurally derived impact scores could potentially support both operational prioritization and retrospective analysis without relying exclusively on isolated delay magnitude or aggregated performance measures.

Current examples in this repository are synthetic and exploratory rather than validated operational decision tools.

---

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

---

## Current status

This repository represents ongoing exploratory model development.

The current formulations and examples are intentionally minimal and primarily intended to investigate interpretable structural representations of propagation behavior in constrained systems.

The models should therefore be interpreted as conceptual and exploratory prototypes rather than validated operational systems.
