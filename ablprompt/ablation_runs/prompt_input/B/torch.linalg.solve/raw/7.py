import torch

# Create a random batched coefficient matrix A
batch_size = 2
n = 3
A = torch.randn(batch_size, n, n)

# Create a random right-hand side tensor B
B = torch.randn(batch_size, n, 2)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)