import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-5, 5, 100)
bar_data = [3, 7, 2, 5, 8]
bar_x = np.arange(len(bar_data))
hist_data = np.random.normal(loc=0, scale=1, size=1000)


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

axes[0, 0].plot(x_vals, x_vals**2, color='purple')
axes[0, 0].set_title('Parabol (y = x^2)')

axes[0, 1].plot(x_vals, np.sin(x_vals), color='orange')
axes[0, 1].set_title('Sinüs Dalgası')

axes[1, 0].bar(bar_x, bar_data, color='teal')
axes[1, 0].set_title('Çubuk Grafik')

axes[1, 1].hist(hist_data, bins=30, color='crimson', edgecolor='black')
axes[1, 1].set_title('Histogram (Normal Dağılım)')

fig.tight_layout()
plt.show()