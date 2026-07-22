from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def pharmacokinetics(C, t, k):
    return -k * C

C0 = 10.0;  k = 0.3
t = np.linspace(0, 24, 200)

# Numerical solution
C_num = odeint(pharmacokinetics, C0, t, args=(k,))

# Analytical solution (for verification)
C_exact = C0 * np.exp(-k * t)

# Plot both
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(t, C_num[:,0], 'b-', lw=2, label='odeint (numerical)')
ax.plot(t, C_exact, 'r--', lw=2, label='analytical')
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Concentration (mg/L)')
ax.set_title('Drug Elimination - Numerical vs. Analytical')
ax.legend();  ax.grid(True, alpha=0.3)
plt.show()
