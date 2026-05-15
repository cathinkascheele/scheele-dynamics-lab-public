"""
Minimal v2 impact score demo.

This script illustrates how the structural propagation model can be
operationalized on a small synthetic network.

Model:
    u(l,t) = L(l,t) / C(l)
    h(u) = max(0, u - 1)
    I_a(t) = k_a(t) * h(u(l_a(t), t))

The example is synthetic and not calibrated to operational data.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Agent:
    name: str
    location: str
    coupling_exposure: float


# Synthetic network capacities
capacity = {
    "A1->X": 1,
    "B1->X": 1,
    "X": 2,
    "X->A4": 1,
    "X->B4": 1,
}

# Synthetic local load at one selected time step
load = {
    "A1->X": 1,
    "B1->X": 2,
    "X": 3,
    "X->A4": 1,
    "X->B4": 1,
}

# Synthetic agents and their downstream coupling exposure
agents = [
    Agent("A1", "A1->X", 1.2),
    Agent("A2", "X", 3.8),
    Agent("B1", "B1->X", 0.8),
    Agent("B2", "X", 2.1),
]


def utilization(location: str) -> float:
    """Local capacity utilization u(l,t)."""
    return load[location] / capacity[location]


def activation(u: float) -> float:
    """Activation function h(u)."""
    return max(0.0, u - 1.0)


def impact_score(agent: Agent) -> float:
    """Agent-level propagation impact I_a(t)."""
    u = utilization(agent.location)
    return agent.coupling_exposure * activation(u)


def main() -> None:
    rows = []

    for agent in agents:
        u = utilization(agent.location)
        h = activation(u)
        impact = impact_score(agent)

        rows.append({
            "agent": agent.name,
            "location": agent.location,
            "load": load[agent.location],
            "capacity": capacity[agent.location],
            "u": round(u, 2),
            "h(u)": round(h, 2),
            "k": agent.coupling_exposure,
            "impact": round(impact, 2),
        })

    rows = sorted(rows, key=lambda r: r["impact"], reverse=True)

    print("\nMinimal v2 impact score demo")
    print("-" * 80)
    print(f"{'Agent':<8} {'Location':<10} {'L':>3} {'C':>3} {'u':>6} {'h(u)':>6} {'k':>6} {'I':>6}")
    print("-" * 80)

    for r in rows:
        print(
            f"{r['agent']:<8} "
            f"{r['location']:<10} "
            f"{r['load']:>3} "
            f"{r['capacity']:>3} "
            f"{r['u']:>6} "
            f"{r['h(u)']:>6} "
            f"{r['k']:>6} "
            f"{r['impact']:>6}"
        )

    print("-" * 80)
    print("Interpretation: agents with both local activation and high downstream coupling exposure receive the highest impact score.")


if __name__ == "__main__":
    main()
