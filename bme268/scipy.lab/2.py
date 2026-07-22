from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def tumor_growth(V,t,r,K):
    return r * V * (1-V/K)

t = np.linspace (0, 300 , 1000)

V = odeint(tumor_growth, 0.5, t, args=(0.04, 100.0) )


idx_25 = np.argmin(np.abs(V[:,0] - 25))
idx_50 = np.argmin(np.abs(V[:,0] - 50))
idx_75 = np.argmin(np.abs(V[:,0] - 75))

fig, ax = plt.subplots(figsize=(8,4))

ax.plot(t, V[:,0], 'r' , lw=2)
ax.axhline(25, color='gray', ls = '--', label='25')
ax.axhline(50, color='green', ls = '--', label='50')
ax.axhline(75, color='yellow', ls = '--', label='75')
ax.set_xlabel('Time')
ax.set_ylabel('Tumor Growth')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_title('Tumor Growth')

plt.show()
