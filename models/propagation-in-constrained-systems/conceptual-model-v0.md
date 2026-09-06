# First Abstraction of Propagation Dynamics (Model v0)

## Purpose

This version is a first explicit abstraction of an observed operational phenomenon.

It translates a small set of commonly observed disturbance and operating-condition categories into a simple linear discrete-time dynamic representation, with the purpose of making assumptions about propagation, persistence, and system state explicit.

The model's role is exploratory: to provide a concrete starting point for examining what a minimal representation would need to preserve, which quantities can reasonably be treated as separate, and where a simple additive formulation becomes insufficient.

---

## System variables

Let

- $S(t)$ denote system-level propagation response at time $t$
- $P(t)$ denote total primary disturbance load at time $t$
- $M(t)$ denote accumulated background operational friction at time $t$

---

## Primary disturbance input

Primary disturbance load is represented as a combination of disturbance categories:

$$
P(t)=\sum_{k\in\lbrace C,I,E\rbrace}\sum_{n=1}^{N_k} D_{k,n}(t)
$$

where

- $C$ denotes operational disturbances
- $I$ denotes infrastructure-related disturbances
- $E$ denotes external disturbances outside direct operational control
- $D_{k,n}(t)$ denotes the disturbance magnitude of event $n$ in category $k$ at time $t$

---

## Background operational friction

Background operational friction is represented by $M(t)$ with dynamics

$$
M(t+1)=\rho M(t)+L(t)+Q(t)+T(t)+X(t)
$$

where

* $M(t)$ represents accumulated background operational friction
* $L(t)$ represents the contribution from location-specific structural or operational friction
* $Q(t)$ represents the contribution from traffic density or concentration
* $T(t)$ represents the contribution from timetable tightness or limited recovery margins
* $X(t)$ represents other small operational frictions not explicitly represented

The parameter $\rho$ represents the persistence of background operational friction between time steps.


---

## Propagation dynamics

System-level propagation evolves according to the propagation equation

$$
S(t+1)=\beta S(t)+\gamma P(t)+\mu M(t)
$$

where

- $\beta$ represents persistence of propagation effects
- $\gamma$ represents sensitivity to primary disturbances
- $\mu$ represents sensitivity to accumulated operational friction

---

## Model assumptions and parameter constraints

The following assumptions are used in v0.

The model uses non-negative state variables and contributions:

$$
P(t), M(t), S(t), L(t), Q(t), T(t), X(t) \geq 0.
$$

The persistence parameters are restricted to

$$
0\leq \rho \leq 1,
\qquad
0\leq \beta \leq 1.
$$

The coupling coefficients are restricted to

$$
\gamma \geq 0,
\qquad
\mu \geq 0.
$$


---

## Interpretation

Model v0 uses aggregated operational quantities that are in principle quantifiable from observed operations, while the formulation remains theoretical and uses abstract or synthetic inputs.

The index $t$ denotes a discrete operational time step.

In this formulation, propagation arises from the combined influence of existing propagation, primary disturbances, and accumulated operational friction rather than from isolated disturbance events alone.


---

## Persistence intuition

In the ideal case where no primary disturbance or background operational friction contributes,

$$
P(t)=0,
\qquad
M(t)=0,
$$

and the system thus reduces to

$$
S(t+1)=\beta S(t).
$$

This implies:

* if $0 \leq \beta < 1$, existing propagation effects gradually decay
* if $\beta = 1$, existing propagation effects persist unchanged

Operationally, $\beta$ represents the fraction of existing propagation carried forward between time steps.



---

## Limitations and motivation for extension

Model v0 represents propagation through a direct linear and additive structure. This makes the relations between the model components explicit, but also imposes several strong assumptions.

The coupling parameters $\gamma$ and $\mu$ are fixed. The model can therefore represent different overall sensitivities to primary disturbances and background operational friction, but these sensitivities do not change with the evolving system state.

The contributions $L(t)$, $Q(t)$, $T(t)$, and $X(t)$ enter $M(t)$ additively. Their possible interactions are not represented explicitly. In an operational railway system, these factors may instead be coupled, so that the effect of one condition depends on the presence or magnitude of another.

The spatial representation is also left unresolved. If the model were developed further, the spatial unit represented by a location would need to be defined—for example as a point, section, corridor, or operational area—and related explicitly to the representation of propagation. This would also require defining when an effect should be interpreted as local and when it constitutes propagation beyond the originating location.

These structural assumptions motivate exploring alternative representations that capture system state and interaction effects more directly, without necessarily introducing a fully explicit representation of all underlying dependencies.

---

## Status

Model v0 is conceptually complete as a baseline linear propagation model.
