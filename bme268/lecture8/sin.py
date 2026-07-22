from numpy import *
from matplotlib.pyplot import *

x = linspace(0, 1, 100)
y = sin(2*pi*3*x)

figure()
plot(x, y, 'r-')
show()
