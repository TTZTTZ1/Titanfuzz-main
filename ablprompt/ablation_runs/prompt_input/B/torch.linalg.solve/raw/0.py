import torch

# Create a random batched matrix A and a right-hand side tensor B
batch_size = 2
n = 3
k = 4
A = torch.randn(batch_size, n, n)
B = torch.randn(batch_size, n, k)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)