# Operational Change in a Constrained Rail System


## Status

>**Current stage: simulation design and synthetic data generation.**

Planned development:

- generate the scheduled operational structure,
- introduce realistic service-pattern variation,
- simulate operational performance and disturbances,
- validate the generated dataset,
- load the data into DuckDB,
- define and validate the analytical population using SQL,
- analyse temporal and spatial performance patterns,
- investigate the 2025 operational change,
- perform targeted diagnostic analysis of relevant operational constraints.

<br>

<br>

## Overview

This case investigates how the effect of an operational change develops through a spatially structured rail system.

The analysis uses a fully synthetic operational dataset with known underlying mechanisms. The objective is to create a controlled system in which operational effects, normal variability, seasonality, and local constraints can be separated and investigated.

The synthetic data are generated first. The resulting dataset is then analysed as if the underlying mechanisms were unknown.

The case is designed around a central analytical question:

**Can the effect of an operational change be distinguished from normal temporal and spatial variation, and how does that effect evolve as trains move through the system?**

---

## Simulation design

### Network

The synthetic system consists of one fictional regional rail line with 16 locations:

**A–B–C–D–E–F–G–H–I–J–K–L–M–N–O–P**

Operations are simulated in both directions over three years:

- 2023
- 2024
- 2025

The general operating structure is assumed to remain sufficiently stable over this period for historical performance profiles to provide a meaningful reference.

---

### Service patterns

The modal stopping pattern, covering approximately 85% of services, consists of the full A–P route.

The remaining services consist of legitimate partial-route or alternative operating patterns.

The modal population is not explicitly labelled in the raw dataset. It must therefore be identified and validated from the observed service patterns before the main analysis is performed.

This introduces a realistic population-definition problem without making service-pattern heterogeneity the main focus of the case.

---

### Spatial structure

Most of the corridor has relatively stable operational characteristics.

The L–P section has substantially higher natural variability due to constraints imposed by the local infrastructure topology.

This instability is direction-dependent.

Services travelling from P toward A may carry variability from the unstable section toward L. Planned recovery capacity around L limits further propagation into the more stable part of the corridor.

The resulting spatial performance profile should therefore reflect both local instability and the system's ability to recover from it.

---

### Temporal and seasonal variation

The system contains a recurring annual seasonal component.

Operational performance is generally better during the summer period. The simulated performance data include an underlying annual seasonal pattern.

The seasonal structure must therefore be identified from historical observations during the analysis.

This is important because the operational change is introduced during the summer of 2025, creating a potential confounding explanation for any observed improvement.

---

### Operational change

An operational change is introduced on **15 June 2025** for the modal service pattern in the **A→P direction**.

The change increases turnaround/recovery margin before departure from A.

The intended mechanism is:

**increased recovery margin → reduced inherited delay → improved initial punctuality**

The change therefore affects the state in which trains enter the corridor rather than directly changing running times through the corridor.

The P→A direction is not directly exposed to the operational change but is retained in the analysis to characterise directional system behaviour and provide additional context for temporal changes affecting the line more broadly.

---

### Local operational constraint

Location D contains a persistent operational conflict mechanism that exists throughout the full simulation period.

The probability and/or consequence of this conflict depends partly on the state and timing with which a train reaches D.

This creates the possibility that trains entering the corridor in a better initial state encounter a downstream constraint that absorbs part of the initial improvement.

The downstream intervention effect is **not explicitly forced to disappear** in the simulation. Instead, the local operational mechanism is simulated and the resulting spatial performance profile is allowed to emerge from the generated data.

---

### Operational cause data

A separate synthetic cause-event dataset will contain registered operational disturbances.

These data are intended primarily for diagnostic analysis after the main performance analysis has identified spatial patterns that require further investigation.

Cause data may provide evidence consistent with particular operational mechanisms, but are not intended to establish causality on their own.

---

## Analytical challenge

The synthetic system is deliberately designed so that a simple before/after comparison is insufficient.

The analysis must distinguish between:

1. normal historical variation,
2. recurring seasonal variation,
3. the local effect of the 2025 operational change,
4. the spatial persistence or erosion of that effect,
5. local operational constraints,
6. unrelated operational variability.

A naive comparison of summer 2025 with the immediately preceding period may attribute normal seasonal improvement to the operational change.

Historical observations from 2023 and 2024 provide a reference for determining whether the 2025 spatial performance profile contains changes beyond normal seasonal and historical variation.

---

## Ground truth and analysis

The mechanisms described above constitute the **simulation ground truth**.

They are defined before the synthetic dataset is generated and before the main analytical workflow is developed.

The analysis will subsequently treat the generated operational data as observations from an unknown system.

This separation between **simulation design** and **analysis** is intentional: the generator defines the mechanisms, while the analytical workflow must determine what conclusions are supported by the resulting observations.
