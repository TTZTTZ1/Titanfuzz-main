import torch

# Create a batch of random matrices A and right-hand side vectors B
batch_size = 3
n = 4
k = 2
A = torch.randn(batch_size, n, n)
B = torch.randn(batch_size, n, k)

# Solve AX = B for each batch element
X = torch.linalg.solve(A, B)

print(X)