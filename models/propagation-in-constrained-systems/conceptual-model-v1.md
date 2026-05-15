# Conceptual Propagation Model (v1)

## Purpose

Model v1 extends Model v0 by introducing state-dependent amplification of disturbance impact. While Model v0 allows the system state to evolve over time, it assumes that the impact of disturbances is constant. Model v1 relaxes this assumption by allowing the system’s response to depend on its current level of operational stress.

The purpose of this extension is not to fully represent operational complexity, but to introduce a minimal mechanism through which identical disturbances may lead to different propagation outcomes under different system conditions.

Model v1 is an aggregate amplification model. It does not represent detailed operational mechanisms, but isolates how system state modulates the impact of incoming disturbances.

---

## System Variables

We retain the variables defined in Model v0.

The system state at time $t$ is given by:

$$
\{S(t), M(t)\}
$$

while $P(t)$ enters the system as an exogenous input.

The definition of $P(t)$ and its aggregation structure follow directly from Model v0.

The dynamics of $M(t)$ are also inherited from Model v0 and are not repeated here.

Model v1 operates on aggregated and operationally defined quantities. The variables $P(t)$ and $S(t)$ reflect disturbances and propagation effects as they are typically represented in operational environments, while $M(t)$ represents unobserved or diffuse operational friction not explicitly captured in such representations.

---

## Propagation Dynamics

Model v1 modifies the propagation equation by introducing state-dependent sensitivity:

$$
S(t+1)=\beta S(t)+\gamma(M(t))P(t)+\mu M(t)
$$

where

- $\beta$ represents persistence of propagation effects  
- $\mu$ represents the direct contribution of accumulated operational friction  
- $\gamma(M(t))$ represents sensitivity to primary disturbances as a function of system state  

---

## State-Dependent Sensitivity

In Model v1, sensitivity is specified as an increasing but saturating function of accumulated operational friction:

$$
\gamma(M(t))=
\gamma_{\min}
+
(\gamma_{\max}-\gamma_{\min})
\frac{M(t)^2}{M(t)^2+K^2}
$$

where

- $\gamma_{\min}$ is baseline sensitivity under low operational stress  
- $\gamma_{\max}$ is the upper bound of sensitivity in a high-stress regime  
- $K$ determines the scale at which sensitivity transitions between regimes  

This specification captures three key properties:

- weak sensitivity at low $M(t)$  
- accelerating increase in sensitivity at intermediate levels  
- saturation at high $M(t)$  

---

## Interpretation

Model v1 retains the structure of Model v0 but removes the assumption of constant response.

In this formulation, identical disturbance loads $P(t)$ may produce different levels of propagation response depending on the system state $M(t)$. The system is therefore not only driven by disturbances, but also by its current susceptibility to disturbances.

At low levels of accumulated pressure, disturbances are more easily absorbed. As $M(t)$ increases, the same disturbance load produces a stronger propagation effect.

The nonlinearity is introduced exclusively through $\gamma(M)$ in order to isolate the mechanism through which identical disturbances may produce different outcomes depending on system state.

---

## Regime Intuition

Model v1 implies the existence of qualitatively different operating regimes:

- **Low-stress regime**  
  Low $M(t)$ → weak sensitivity → limited propagation  

- **Transition regime**  
  Intermediate $M(t)$ → rapidly increasing sensitivity  

- **High-stress regime**  
  High $M(t)$ → near-saturated sensitivity → strong propagation  

This provides a mechanism through which relatively small differences in system state may lead to large differences in outcomes.

---

## Why Nonlinearity is Introduced in $\gamma(M)$

The nonlinear specification is applied to $\gamma(M)$ because it directly represents the system’s susceptibility to incoming disturbance load.

Introducing nonlinearity elsewhere (for example in accumulation or persistence terms) would introduce additional mechanisms such as nonlinear recovery or nonlinear buildup. Model v1 deliberately avoids this in order to isolate a single effect:

identical disturbances produce different outcomes depending on system state.

---

## Model Status

Model v1 is a minimal nonlinear extension of Model v0.

It does not include explicit network structure, spatial interaction, or heterogeneous agent behavior. Instead, it isolates a single mechanism: state-dependent amplification of disturbance impact.

As such, it should be interpreted as an aggregate state model rather than a structural propagation model.

This provides a conceptual basis for:

- understanding propagation as a state-dependent process  
- identifying conditions under which propagation becomes amplified  
- guiding analysis of context-dependent effects  
- informing the design of subsequent structural model extensions

---

## Remaining Limitations

Model v1 introduces state-dependent amplification, but still operates on aggregated system quantities.

The model does not explicitly represent:

- spatial structure  
- coupling topology  
- constrained flow  
- heterogeneous agents  
- localized interaction mechanisms  

Propagation is therefore represented as an aggregate system response rather than as an explicit structural process.

These limitations motivate the transition toward more structure-oriented propagation models.
