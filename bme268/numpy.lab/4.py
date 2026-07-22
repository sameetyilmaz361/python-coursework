import numpy as np

array=np.random.randint(0,101, size=20)

print(array)

mean=np.mean(array)
median=np.median(array)
std=np.std(array)

index50=np.where(array>50)

array[array < 25] = 0

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std}")
print(f"Indices of elements greater than 50: {index50}")
print("Modified array with elements less than 25 set to 0:\n", array)