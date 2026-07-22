import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def tumor_growth(V, t, r, K):
    return r * V * (1 - V / K)

t = np.linspace(0, 300, 1000)
V = odeint(tumor_growth, 0.5, t, args=(0.04, 100.0))

plt.plot(t, V[:, 0])
plt.xlabel('Time (days)')
plt.ylabel('Tumor Volume (mm³)')
plt.title('Tumor Growth Model')
plt.grid(True, alpha=0.3)
plt.axhline(50, color='gray')
plt.show()