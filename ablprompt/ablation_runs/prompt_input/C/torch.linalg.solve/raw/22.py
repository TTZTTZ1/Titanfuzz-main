import torch

# Create a random square matrix A of size 3x3
A = torch.randn(3, 3)

# Create a right-hand side vector B of size 3
B = torch.randn(3)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)