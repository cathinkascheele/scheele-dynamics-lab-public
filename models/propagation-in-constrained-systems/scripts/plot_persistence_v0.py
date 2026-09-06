import numpy as np
import matplotlib.pyplot as plt

n_steps = 15
s0 = 1.0
betas = [0.0, 0.5, 0.9, 1.0]

t = np.arange(n_steps + 1)

for beta in betas:
    s = np.zeros(n_steps + 1)
    s[0] = s0

    for i in range(n_steps):
        s[i + 1] = beta * s[i]

    plt.plot(t, s, marker="o", label=fr"$\beta={beta}$")

plt.xlabel("Time step")
plt.ylabel("Propagation state $S(t)$")
plt.title("Persistence behaviour in the ideal case")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
