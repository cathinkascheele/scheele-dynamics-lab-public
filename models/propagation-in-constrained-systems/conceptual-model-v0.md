# Conceptual Propagation Model (v0)

## Purpose

This model represents the baseline conceptual framework developed during the exploratory analysis.
It is intentionally minimal and designed to capture core mechanisms of propagation in scheduled, capacity-constrained operational systems.

The model serves as a reference structure for subsequent model extensions.

Later developments are treated as separate model versions.

---

## System Variables

Let

- $S(t)$ denote system-level propagation response at time $t$
- $P(t)$ denote total primary disturbance load at time $t$
- $M(t)$ denote accumulated operational friction or latent system pressure

---

## Primary Disturbance Input

Primary disturbance load is represented as a weighted combination of disturbance categories:

$$
P(t)=\sum_{n=1}^{N}\alpha_n C_n(t)+\alpha_I I(t)+\alpha_E E(t)
$$

where

- $C_n(t)$ represents operational disturbance categories
- $I(t)$ represents structural or infrastructure-related disturbances
- $E(t)$ represents external disturbances outside direct operational control

The coefficients $\alpha$ represent the relative contribution of each disturbance category to the overall disturbance load.

The formulation is intentionally generic and abstracts from domain-specific classification systems.

---

## Accumulated Operational Friction

Accumulated operational friction is represented by $M(t)$ with dynamics

$$
M(t+1)=\rho M(t)+\eta_L L(t)+\eta_D D(t)+\eta_T T(t)+\eta_X X(t)
$$

where

- $M(t)$ represents accumulated operational pressure
- $L(t)$ represents local operational load
- $D(t)$ represents high-density or peak operating conditions
- $T(t)$ represents schedule pressure, resource tightness, or limited recovery margins
- $X(t)$ represents additional small operational frictions not explicitly captured elsewhere

The parameter $\rho$ captures persistence of operational friction within the system.

The coefficients $\eta$ represent the contribution of contextual operational factors to accumulated system pressure.

---

## Propagation Dynamics

System-level propagation evolves according to

$$
S(t+1)=\beta S(t)+\gamma P(t)+\mu M(t)
$$

where

- $\beta$ represents persistence of propagation effects
- $\gamma$ represents sensitivity to primary disturbances
- $\mu$ represents sensitivity to accumulated operational friction

---

## Interpretation

Model v0 operates on aggregated and operationally defined quantities.

The variables $P(t)$ and $S(t)$ represent disturbances and propagation effects as they are typically observed in operational environments, while $M(t)$ represents a latent or partially unobserved form of accumulated operational friction not explicitly captured in such representations.

In this formulation, system-level propagation is interpreted as an emergent response arising from the interaction between primary disturbances and accumulated operational pressure rather than as the direct consequence of isolated disturbance events alone.

The underlying input variables remain intentionally abstract, while the relations between disturbance load, accumulated pressure, and propagation response are approximated as linear.

---

## Stability Intuition

A simple stability intuition follows from the propagation equation

$$
S(t+1)=\beta S(t)+\gamma P(t)+\mu M(t)
$$

If new disturbances are temporarily ignored, the system reduces to

$$
S(t+1)=\beta S(t)
$$

This implies:

- if $|\beta|<1$, propagation effects gradually decay
- if $\beta=1$, propagation persists
- if $|\beta|>1$, propagation amplifies over time

Operationally, $\beta$ captures the extent to which existing system pressure propagates into subsequent system states.

Systems with sufficient buffer capacity and recovery mechanisms tend to operate in a stable regime ($\beta<1$), whereas high congestion, persistent load, or repeated disturbance interactions may push the system toward critical or unstable propagation regimes.

---

## Limitations and Motivation for Extension

Model v0 assumes that disturbance effects are constant and independent of system state.

However, exploratory observations suggest that similar disturbance categories may produce very different propagation outcomes depending on operational context, accumulated system pressure, timing, and interaction with other ongoing processes.

While Model v0 includes state variables such as accumulated operational friction, the system response remains linear and governed by constant parameters. The model therefore allows pressure to accumulate, but does not allow the system’s sensitivity to disturbances to vary with system state.

In practice, propagation behavior appears increasingly sensitive under high load and constrained operating conditions, indicating state-dependent amplification rather than only state-dependent accumulation.

In addition, disturbances within the same category are not necessarily homogeneous. Their impact may vary substantially depending on timing, topology, coupling opportunities, and interaction with concurrent disturbances. In Model v0, such variability is implicitly averaged out.

These limitations motivate an extension in which propagation sensitivity is allowed to vary with system state.

A full network representation may ultimately be required to capture spatial and agent-level propagation mechanisms. However, before introducing explicit network structure, it is useful to isolate a more basic limitation of Model v0:

the model assumes constant disturbance effects, whereas observed propagation behavior appears strongly dependent on current system conditions.

Model v1 therefore introduces state-dependent propagation as the minimal extension required to represent this mechanism more explicitly.

---

## Model Status

This specification is treated as the baseline conceptual propagation model.

Subsequent model versions introduce additional mechanisms such as:

- state-dependent amplification
- structural coupling effects
- constrained flow
- network-sensitive propagation
- heterogeneous agent interaction
