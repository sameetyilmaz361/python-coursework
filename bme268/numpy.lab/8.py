import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.uniform(-5, 5, 50)
y = np.random.uniform(-5, 5, 50)

distances = np.sqrt(x**2 + y**2)


fig, ax = plt.subplots()

sc = ax.scatter(x, y, c=distances, cmap='viridis', s=100, edgecolor='black')

cbar = fig.colorbar(sc, ax=ax)
cbar.set_label('Orijine Olan Uzaklık')

ax.set_xlabel('X Ekseni')
ax.set_ylabel('Y Ekseni')
ax.set_title('Mesafeye Göre Renklendirilmiş Saçılım Grafiği')
plt.show()