# Structural Propagation Model (v2)

## Purpose

Model v2 represents propagation as an interaction between structural constraints, local capacity pressure, and downstream coupling exposure.

The model investigates whether a small set of structural quantities can produce useful indicators of propagation risk and system-level impact.

The central modeling question is how to define $k_a(t)$ so that it captures relevant coupling structure without requiring full system simulation.

---

## System

The system is represented as:

$$
G = (N, E, A, S)
$$

where:

- $N$: nodes or locations  
- $E$: connections or flow paths between nodes  
- $A$: mobile agents interacting with the system  
- $S$: structural properties associated with the network, such as bottlenecks, capacity distribution, recovery margins, and operational design constraints

---

## Location and capacity

Each location $\ell \in N \cup E$ has:

- Capacity: $C(\ell)$  
- Load: $L(\ell, t)$

Local load $L(\ell,t)$ emerges from the distribution and interaction of agents across the system graph, while structural properties $S$ influence capacity distribution and downstream coupling opportunities.

Define local utilization:

$$
u(\ell, t)=\frac{L(\ell,t)}{C(\ell)}
$$

where:

- $u(\ell,t)$ represents local capacity utilization

---

## Activation function

Propagation is activated only when capacity is exceeded:

$$
h(u)=\max(0,u-1)
$$

where:

- $h(u)$ represents propagation activation under excess capacity utilization

Interpretation:

- $u \leq 1$: no propagation pressure  
- $u > 1$: excess load activates propagation pressure  

---

## Agent-level impact

Each agent $a$ at time $t$ has:

$$
I_a(t)=k_a(t)\cdot h(u(\ell_a(t),t))
$$

where:

- $I_a(t)$ represents agent-level propagation impact or propagation potential  
- $\ell_a(t)$ represents the current location of agent $a$  
- $k_a(t)$ represents coupling exposure

---

## Coupling factor $k_a(t)$

The coupling factor represents the downstream coupling exposure available to agent $a$ at time $t$.

In the minimal formulation, coupling exposure is derived from the system graph and the current position of the agent:

$$
k_a(t)=k(G,\ell_a(t))
$$

where:

- $G$: system graph and structural properties  
- $\ell_a(t)$: current location of agent $a$  

The function $k$ may represent the number, strength, or structural importance of downstream interactions reachable from the agent’s current position.

Mobile agents are treated as primary propagation carriers because they continuously move through the graph and encounter new coupling opportunities.

---

## Interpretation

Propagation emerges when local capacity pressure interacts with downstream coupling opportunities defined by system structure.

Thus:

- high load without coupling → limited spread  
- high coupling without load → limited spread  
- propagation becomes amplified when both are present  

The model separates local activation pressure from downstream propagation opportunity, allowing structurally mediated propagation behavior to be analyzed without requiring full system simulation.

---

## Model scope

Model v2 is a minimal structural propagation model intended to isolate how local capacity pressure and downstream coupling exposure interact to produce system-level propagation potential.

The model is:

- structural rather than statistical  
- mechanism-oriented rather than descriptive  
- intentionally minimal and interpretable  

It is intended for exploratory analysis of:

- structural propagation impact  
- structurally vulnerable system configurations  
- coupling-sensitive propagation behavior  
- differences between local disturbance magnitude and downstream system effect  

The formulation is designed to support interpretable operational reasoning without requiring full operational replication or detailed simulation.

---

## Remaining limitations

Model v2 introduces explicit structural coupling and localized propagation activation, but several core challenges remain unresolved.

A central open problem is how to define and estimate coupling exposure $k_a(t)$ in a way that captures operationally relevant downstream interaction structure without requiring full system simulation.

Related challenges include:

- determining which structural properties are operationally important
- representing topology, bottlenecks, density, timing, and coupling opportunities in a tractable form
- distinguishing local disturbance magnitude from structural propagation importance
- scaling from small synthetic structures toward larger operational systems
- evaluating whether structurally derived propagation indicators correspond to observed system-level effects

The current formulation should therefore be interpreted as an exploratory structural framework rather than a validated operational model.

---

## Model status

---

Model v2 is an exploratory structural formulation representing the current direction of the modelling work.

It was developed to investigate whether propagation can be represented more directly through local constraints and coupling structure rather than only through aggregated system-level quantities.

The formulation is not yet a complete or validated model. Key definitions, including capacity, load, spatial units, coupling exposure, and the relation between local activation and observed propagation, remain open.

Further development should build these elements systematically and evaluate whether the structural representation provides useful information beyond the simpler aggregate formulations.

---
