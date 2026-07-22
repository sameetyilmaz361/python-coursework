import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig = plt.figure(figsize=(18, 5))

ax1 = fig.add_subplot(1, 3, 1)
pc = ax1.pcolormesh(X, Y, Z, cmap='inferno', shading='auto')
ax1.set_title('(a) pcolor Grafiği')
fig.colorbar(pc, ax=ax1)

ax2 = fig.add_subplot(1, 3, 2)
contours = ax2.contour(X, Y, Z, levels=10, cmap='viridis')
ax2.clabel(contours, inline=True, fontsize=8)
ax2.set_title('(b) Kontur Grafiği')
fig.colorbar(contours, ax=ax2)

ax3 = fig.add_subplot(1, 3, 3, projection='3d')
surf = ax3.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')
ax3.set_title('(c) 3D Yüzey Grafiği')


fig.tight_layout()
plt.show()