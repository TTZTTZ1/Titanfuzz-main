import torch

# Create a batched matrix A and a right-hand side tensor B
batch_size = 2
n = 3
k = 2
A = torch.randn(batch_size, n, n)
B = torch.randn(batch_size, n, k)

# Solve AX = B
X = torch.linalg.solve(A, B)

print(X)