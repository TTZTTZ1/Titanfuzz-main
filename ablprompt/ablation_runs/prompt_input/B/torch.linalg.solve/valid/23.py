import torch

# Create a batch of random matrices A and right-hand side tensors B
batch_size = 2
n = 3
k = 2
A = torch.randn(batch_size, n, n, dtype=torch.float64)
B = torch.randn(batch_size, n, k, dtype=torch.float64)

# Solve AX = B for each batch element
X = torch.linalg.solve(A, B)

print(X)