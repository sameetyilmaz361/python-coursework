import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

fig, ax = plt.subplots(figsize = (8,4))

ax.plot(x, y_sin, color='blue', linestyle='--', label='sin(x)')
ax.plot(x, y_cos, color='red', linestyle='-', label='cos(x)')
ax.plot(x, y_tan, color='green', linestyle='-.', label='tan(x)')

ax.set_ylim(-2, 2)
ax.set_xlabel('x')
ax.set_ylabel('y')  
ax.set_title('Trigonometric Functions')
ax.legend()

fig.savefig('trigonometric_functions.png', dpi=150)
plt.show()