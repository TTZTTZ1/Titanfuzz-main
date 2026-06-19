import torch

# Create a batch of random matrices A and right-hand side B
batch_size = 3
n = 4
A = torch.randn(batch_size, n, n)
B = torch.randn(batch_size, n)

# Solve AX = B
X = torch.linalg.solve(A, B)

print(X)