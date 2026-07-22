from numpy import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

x= linspace(0, 1 ,100)
y= sin(2*pi*3*x)

fig, axes = plt.subplots(1, 4, figsize=(12, 3))
n=arange(1,10)
axes[0].scatter(x, y)
axes[1].step(n, n**2)
axes[2].bar(n, n**2)
axes[3].fill_between(x, y)
axes[0].hist(np.random.randn(1000), bins=50)
show()