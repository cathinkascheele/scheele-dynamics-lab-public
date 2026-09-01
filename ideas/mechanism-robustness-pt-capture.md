# Mechanism Robustness and Regime Sensitivity in Pt Capture Materials

## Motivation

Platinum capture in the ammonia oxidation process involves materials designed to retain volatile platinum-containing species released under high-temperature operating conditions.

Research on Pt capture combines several complementary approaches.

Experimental studies determine which materials capture platinum under specific operating conditions.

Atomistic modelling, including density functional theory (DFT), can be used to investigate thermodynamic stability, defect chemistry, reaction pathways and other microscopic mechanisms.

Characterization techniques such as XRD, SEM/EDX and XPS provide complementary information about crystal structures, morphology, elemental distributions and chemical states.

Together, these approaches provide detailed insight into material behaviour.

Laboratory experiments, pilot plants and industrial reactors often differ in many variables simultaneously. While chemistry, thermodynamics and structural analysis provide important explanations, more complex operating environments may introduce several interacting effects at once. 

This motivated me to explore the question:

<br>

> **What would a small model need to represent in order to describe how material behaviour changes across operating environments?**

<br>

The case is intended primarily as a learning environment for exploring how mechanistic knowledge, operating conditions and system-level behaviour can be translated into small, interpretable models.

## Preliminary modelling question

One question that interests me is whether some aspects of Pt capture behaviour remain relatively stable across changing operating conditions, while others become more sensitive as the surrounding environment changes.

This raises a modelling question: what would a small representation need to preserve in order to describe such changes meaningfully?

Possible questions include::

- how dominant material behaviour changes across operating environments
- which variables or interactions appear necessary to distinguish different regimes
- whether some mechanisms or material responses are more robust to changing conditions than others
- what is gained or lost when the system is represented at a higher level than individual experiments or atomistic mechanisms

Before further model development, relevant literature and established modelling approaches will be reviewed to identify what can already be reused, adapted, or tested for this case.

## Relation to published work

This line of thinking was partly motivated by published Pt capture studies in which some materials appeared to behave relatively consistently across different environments, while others appeared to show stronger environmental dependence.

One example is the qualitative contrast observed between Nd₂O₃- and Gd₂O₃-based systems reported in

> Hessevik, Carlsen, Bestul, Waller, Fjellvåg & Sjåstad (2025), *Oxides for Pt Capture in the Ammonia Oxidation Process — A Screening Study*.

## Development status

**Status:** Concept
**Target:** Unscheduled
**Expected output:** Exploratory model
