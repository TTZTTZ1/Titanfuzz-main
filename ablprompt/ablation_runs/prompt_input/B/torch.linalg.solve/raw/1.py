import torch

# Create a batch of random matrices A and a right-hand side tensor B
batch_size = 3
n = 4
k = 2
A = torch.randn(batch_size, n, n)
B = torch.randn(batch_size, n, k)

# Solve AX = B
X = torch.linalg.solve(A, B)

print(X)