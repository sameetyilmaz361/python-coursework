import numpy as np

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

elementwise_product = A * B
matrix_product = np.dot(A, B)

inverse_A = np.linalg.inv(A)

check= np.dot(A, inverse_A)
ifeye = np.allclose(check, np.eye(3))

print("Element-wise product:\n", elementwise_product)
print("Matrix product:\n", matrix_product)  
print("Inverse of A:\n", inverse_A)
print("Is A * A^-1 close to the identity matrix?", ifeye)