# State-Dependent Propagation Dynamics (Model v1)

## Status
> **Early conceptual extension / working hypothesis**
>
> Model v1 introduces state-dependent sensitivity as one possible extension of Model v0. The current formulation is not yet treated as a developed model.
>
> Remaining work includes:
> - defining parameter domains and constraints
> - examining limiting cases and parameter behaviour
> - testing sensitivity to the chosen functional form for $\gamma(M)$
> - deciding whether $M(t)$ should both contribute directly through $\mu M(t)$ and modulate the response to $P(t)$ through $\gamma(M(t))$
> - comparing this formulation with alternative representations before treating it as the next model stage

<br>

<br>

## Purpose

Model v1 extends Model v0 by introducing state-dependent amplification of disturbance impact. While Model v0 allows the system state to evolve over time, it assumes that the impact of disturbances is constant. Model v1 relaxes this assumption by allowing the system’s response to depend on its current level of operational stress.

The purpose of this extension is to introduce a minimal mechanism through which identical disturbances may lead to different propagation outcomes under different system conditions.

Model v1 is an aggregate amplification model. It does not represent detailed operational mechanisms, but isolates how system state modulates the impact of incoming disturbances.

---

## System variables

We retain the variables defined in Model v0.

The system state at time $t$ is given by:

$$
\{S(t), M(t)\}
$$

while $P(t)$ enters the system as an exogenous input.

Model v1 treats $P(t)$ and $M(t)$ as abstract model quantities representing primary disturbance load and background operational friction.

---

## Propagation dynamics

Model v1 modifies the propagation equation by introducing state-dependent sensitivity:

$$
S(t+1)=\beta S(t)+\gamma(M(t))P(t)+\mu M(t)
$$

where

- $\beta$ represents persistence of propagation effects  
- $\mu$ represents the direct contribution of operational friction  
- $\gamma(M(t))$ represents sensitivity to primary disturbances as a function of system state  

---

## State-dependent sensitivity

In Model v1, sensitivity is specified as an increasing and saturating function of background operational friction:

$$
\gamma(M(t))=
\gamma_{\min}
+
(\gamma_{\max}-\gamma_{\min})
\frac{M(t)^2}{M(t)^2+K^2}
$$

where

- $\gamma_{\min}$ is baseline sensitivity at low background operational friction
- $\gamma_{\max}$ is the upper bound of sensitivity
- $K$ determines the scale at which sensitivity transitions toward the high-sensitivity regime

This specification captures three key properties:

- low sensitivity at low $M(t)$
- increasing sensitivity as $M(t)$ grows
- saturation toward $\gamma_{\max}$ at high $M(t)$

---

## Interpretation

Model v1 retains the structure of Model v0 but removes the assumption of constant response.

In this formulation, identical disturbance loads $P(t)$ may produce different levels of propagation response depending on the system state $M(t)$. The system is therefore not only driven by disturbances, but also by its current susceptibility to disturbances.

At low levels of background operational friction, disturbances are more easily absorbed. As $M(t)$ increases, the same disturbance load produces a stronger propagation effect.

The nonlinearity is introduced exclusively through $\gamma(M)$ in order to isolate the mechanism through which identical disturbances may produce different outcomes depending on system state.

---

## Regime intuition

Model v1 implies the existence of qualitatively different operating regimes:

- **Low-stress regime**  
  Low $M(t)$ → weak sensitivity → limited propagation  

- **Transition regime**  
  Intermediate $M(t)$ → rapidly increasing sensitivity  

- **High-stress regime**  
  High $M(t)$ → near-saturated sensitivity → strong propagation  

This provides a mechanism through which relatively small differences in system state may lead to large differences in outcomes.

---

## Why nonlinearity is introduced in $\gamma(M)$

The nonlinear specification is applied to $\gamma(M)$ because it directly represents the system’s susceptibility to incoming disturbance load.

Introducing nonlinearity elsewhere (for example in accumulation or persistence terms) would introduce additional mechanisms such as nonlinear recovery or nonlinear buildup. Model v1 deliberately avoids this in order to isolate a single effect:

identical disturbances produce different outcomes depending on system state.

---

## Limitations

- The chosen functional form for $\gamma(M)$ has not yet been systematically tested against alternative representations.
- Parameter ranges and limiting behaviour remain to be examined.
- The model does not explicitly represent spatial topology or structural dependencies between locations, and therefore does not resolve how propagation moves through the system.
