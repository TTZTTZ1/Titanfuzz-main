import torch

# Create a batched coefficient matrix A and a right-hand side matrix B
batch_size = 3
n = 4
k = 2
A = torch.randn(batch_size, n, n)
B = torch.randn(batch_size, n, k)

# Solve AX = B
X = torch.linalg.solve(A, B)

print(X)