from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def pharmokinetics(C, t, k):
    return -k * C

C0 = 10.0;  k = 0.3
t = np.linspace(0, 24, 200)

C_num = odeint(pharmokinetics, C0, t, args=(k,))
C_exact = C0 * np.exp(-k * t)

plt.plot(t, C_num[:,0], 'b')
plt.plot(t, C_exact, 'r--')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration (mg/L)')
plt.title('Drug Elimination - Numerical vs. Analytical')
plt.legend(['odeint (numerical)', 'analytical'])            
plt.grid(True, alpha=0.3)
plt.show()