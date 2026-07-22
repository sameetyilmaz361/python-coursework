import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def C(t):
    return 20 * np.exp(-0.15 * t)

auc_48 , error = quad(C, 0 , 48)
auc_inf , error = quad (C, 0 , np.inf)

percentage = (auc_48 / auc_inf) * 100
print(f"First 48 hours percentege {percentage}%")

t = np.linspace(0 , 60 , 500)
t_48 = np.linspace(0 , 48 , 500)

fig , (ax1, ax2) = plt.subplots (2 , 1 , figsize = (8,4))

ax1.plot(t, C(t), 'b')
ax1.fill_between(t_48 , C(t_48), label = '0-48h AUC')
ax1.set_title('0-48h AUC')
ax1.legend()

ax2.plot(t, C(t), 'r')
ax2.fill_between(t, C(t), label= '0-Inf AUC')
ax2.set_title('0-Inf AUC')
ax2.legend()

plt.show()