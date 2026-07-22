import numpy as np

I = np.eye(10)

A = np.random.rand(10, 10)

result = np.dot(I, A)

correct = np.allclose(result, A)

print("Result is correct:", correct)