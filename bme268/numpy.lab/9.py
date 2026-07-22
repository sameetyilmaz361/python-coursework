import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [30, 32, 35, 40, 45, 50, 55, 60, 55, 50, 40, 35] 
rainfall = [2.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 6.5, 5.0, 4.0, 3.0, 2.5]

fig, (ax1,ax2) = plt.subplots(1,2)

ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)')
ax1.plot(months, temperatures, color='red', linewidth=2)

ax2.set_xlabel('Month')
ax2.set_ylabel('Rainfall (mm)')
ax2.plot(months, rainfall, color='blue', linewidth=2)
ax2.set_title('Monthly Temperature and Rainfall')

fig.tight_layout()
plt.show()
