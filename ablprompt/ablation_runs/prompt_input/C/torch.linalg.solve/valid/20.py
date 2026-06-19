import torch

# Create a random invertible matrix A and a right-hand side vector B
A = torch.randn(3, 3)
B = torch.randn(3)

# Solve the linear equation AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)