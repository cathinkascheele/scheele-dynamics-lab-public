# Operational Performance Diagnostic System

## Motivation

Operational organizations often rely on key performance indicators and recurring reports to monitor whether performance is meeting expectations.

These measures are useful for establishing status and identifying major events. However, recurring reporting can also contain large amounts of detail that describe normal variation or persistent, already-known conditions without necessarily adding new diagnostic information.

For example, a location or asset may consistently contribute strongly to poor performance because of a known structural limitation. Repeating the same finding each reporting period may be important for status monitoring, but it provides limited new insight unless the pattern changes.

This project explores whether operational reporting can instead combine broad status monitoring with a more selective diagnostic process.

Instead of presenting the same level of detail for every reporting period, the system would first establish overall performance and identify meaningful deviations from relevant baselines. Where deviations are detected, additional analysis would be triggered automatically to characterize when, where and under what system state they emerged.

The goal is to create a reproducible analytical process that reduces unnecessary manual filtering, applies consistent criteria for selecting what deserves attention, and supports more robust interpretation of operational performance.

Railway operations provide one useful setting for exploring this idea. Performance develops across time, locations, directions, train runs, events and changing system states. Meaningful deterioration may therefore arise from a single dominant event, but it may also emerge from combinations of smaller effects that are difficult to see in aggregated cause categories alone.

---

## Core question

The central question is:

**Can operational reporting distinguish normal variation from meaningful performance deviations and automatically investigate those deviations in enough detail to support interpretation and decision-making?**

The system would move from questions such as

> *How did the operation perform, and what happened?*

towards a more structured diagnostic process:

* **What deviated from the relevant normal pattern?**
* **Where, when and under what system state did the deviation emerge?**
* **What underlying pattern best characterizes it — for example, a single event, repeated local deterioration, or distributed effects across multiple train runs?**

The diagnostic process would allow both single dominant causes and more distributed or interacting patterns to emerge from the data.

A deterioration might, for example, be dominated by one major infrastructure event. In another case, no individual cause category may appear unusual, while combinations of time, location, direction, existing delay and system load are associated with a broader pattern of delay accumulation.

The system would automate the initial diagnostic process, extracting the context needed to understand what happened and leaving the operational interpretation and possible response to human judgement.

---

## System concept

The project would use entirely synthetic railway data designed to reproduce general structural characteristics of operational data environments.

Rather than beginning with a single clean dataset, the synthetic inputs would include multiple sources with different granularities, formats and identifiers.

A possible architecture is:

**heterogeneous synthetic data → Python ingestion and validation → DuckDB / SQL transformations → analytical data model → baseline construction → robust deviation detection → automated diagnostic drill-down → interactive operational report**

The analytical model could combine information about train runs, observations along a route, operational events, delay causes, locations, performance indicators and capacity-related conditions.

The exact data model and technology stack would be determined when the project enters active development.

---

## Diagnostic approach

A central methodological problem is defining what constitutes a meaningful deviation.

The largest observed value is not necessarily the most informative one. A location that routinely produces high delays may be operating within its normal range, while a normally stable location may show a smaller absolute value that represents a substantial departure from its usual behaviour.

A central component would therefore be comparison against an appropriate historical or contextual baseline rather than simply ranking the largest observed values.

Depending on the question, the relevant baseline might be defined across combinations such as

* line,
* direction,
* location,
* time of day,
* day type,
* and relevant system state.

The challenge is to define reference groups that are specific enough to be meaningful while still containing enough observations to characterize normal variation reliably.

Simple and interpretable robust statistics, such as medians, quantiles and median absolute deviation, would be preferred where they provide sufficient diagnostic value.

Robustness is an important part of the project. The selection of deviations should rely on explicit and reproducible criteria rather than ad hoc manual inspection, while remaining transparent enough that the reasoning behind a flagged pattern can be understood.

---

## Automated drill-down

Detected deviations would trigger additional analysis automatically.

The system could progressively examine dimensions such as

**status → deviation → line → direction → time → location → train runs → events → system state**

The exact path would depend on the type of deviation rather than following the same fixed reporting structure every time.

For example, deterioration in an aggregate performance indicator might not correspond to any unusually large cause category. The diagnostic process could instead reveal distributed delay accumulation across multiple services in a specific direction and time window, occurring under an already elevated system load.

In other cases, the analysis may identify one dominant event or a recurrent local pattern.

The purpose of the drill-down is to characterize the structure of the deviation using the smallest amount of detail needed to make the pattern interpretable.

Where combinations of conditions are associated with disproportionate deterioration, the resulting pattern may also provide hypotheses about mechanisms that contribute to cascading effects. These hypotheses would require further analysis before being interpreted causally, but they may help identify where deeper system understanding could support future operational or preventive measures.

---

## Decision support

The intended output is a diagnostic operational report rather than a conventional KPI-heavy dashboard.

The same analytical engine should support both routine status monitoring and targeted diagnostic analysis.

Periods with no substantial deviations could be reported accordingly rather than generating unnecessary detail:

> *No substantial deviations from the relevant baseline were detected.*

Where deviations occur, the system would provide a consistent diagnostic summary of the relevant temporal, spatial and operational context.

The final human task would remain interpretive:

* Is the detected pattern operationally important?
* Is the underlying mechanism already understood?
* Is it potentially actionable?
* Does it require deeper specialist analysis?
* Could improved understanding of the pattern support preventive or mitigating measures?

In this sense, the system is intended as decision support rather than automated decision-making.

---

## Technical scope

The project is intended to demonstrate an integrated analytical workflow involving

* Python,
* SQL and analytical database operations,
* data modelling,
* ingestion and validation of heterogeneous data,
* analytics engineering,
* contextual baseline construction,
* robust deviation detection,
* automated diagnostic drill-down,
* sequence-based analysis of individual train runs,
* analytical QA,
* visualization,
* and operational decision support.

DuckDB is one possible analytical database because it would allow the project to demonstrate SQL and explicit data modelling while remaining lightweight and locally reproducible.

More complex methods, including machine learning, would only be introduced if they provide clear analytical value beyond simpler and more transparent approaches.

---

## Analytical limitations

Observed associations between disruptions, operating conditions and performance would not automatically be interpreted as causal relationships.

The diagnostic system may identify where unusual patterns occur, how they are structured and which system states coincide with them, but causal explanations would require additional evidence or analysis.

---

## Development status

**Status:** Concept
**Target:** 2026–2027
**Expected output:** Operational diagnostic analysis system
