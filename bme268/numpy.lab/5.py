import numpy as np

matrix=np.arange(1,37).reshape(6,6)
print(matrix)

submatrix=matrix[1:4,1:4]
print(submatrix)

flattened=matrix.flatten()

every_third=flattened[::3]
print(every_third)