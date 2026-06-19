import torch

# Create a batch of random matrices A and right-hand side tensors B
batch_size = 3
n = 4
k = 2
A = torch.randn(batch_size, n, n, dtype=torch.double)
B = torch.randn(batch_size, n, k, dtype=torch.double)

# Solve AX = B for each batch
X = torch.linalg.solve(A, B)

print(X)