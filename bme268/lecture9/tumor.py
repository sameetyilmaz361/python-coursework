from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def tumor_growth(V, t, r, K):
    return r * V * (1 - V / K)

t = np.linspace(0, 300, 1000)

V = odeint(tumor_growth, 0.5, t, args=(0.04, 100.0))


# Find when V = 50
idx_50 = np.argmin(np.abs(V[:,0] - 50))

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(t, V[:,0], 'g-', lw=2)
ax.axhline(50, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('Time (days)')
ax.set_ylabel('Tumor Volume (cm^3)')
ax.set_title('Logistic Tumor Growth')
ax.legend();  ax.grid(True, alpha=0.3)

plt.show()



