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

## Location and Capacity

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

## Activation Function

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

## Agent-Level Impact

Each agent $a$ at time $t$ has:

$$
I_a(t)=k_a(t)\cdot h(u(\ell_a(t),t))
$$

where:

- $I_a(t)$ represents agent-level propagation impact or propagation potential  
- $\ell_a(t)$ represents the current location of agent $a$  
- $k_a(t)$ represents coupling exposure

---

## Coupling Factor $k_a(t)$

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

The model separates local activation pressure from downstream propagation opportunity, allowing propagation exposure to be analyzed without requiring full system simulation.

---

## Model Scope

The model is:

- structural (not statistical)  
- mechanism-based (not descriptive)  
- minimal (few variables, high interpretability)  

It is intended for:

- identifying propagation risk  
- comparing system configurations  
- ranking agents, locations, or events by propagation exposure  
- supporting operational interpretation and decision support  

Model v2 is formulated as an operational impact model designed to be interpretable, testable, and scalable.
