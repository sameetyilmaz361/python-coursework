import numpy as np

x = np.linspace(0 , 2 * np.pi, 100)

mask = np.sin(x) > 0.5

filtered_x = x[mask]

count = np.sum(mask)

print(f"Number of elements where sin(x) > 0.5: {count}")
print(f"Filtered x values: {filtered_x}")