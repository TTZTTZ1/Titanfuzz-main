import torch

# Create a batched coefficient matrix A of shape (*, n, n)
batch_size, n = 3, 4
A = torch.randn(batch_size, n, n)

# Create a right-hand side tensor B of shape (*, n, k)
k = 2
B = torch.randn(batch_size, n, k)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print(X)