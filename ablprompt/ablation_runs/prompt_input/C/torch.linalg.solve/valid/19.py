import torch

# Create a random square matrix A
A = torch.randn(3, 3)

# Create a right-hand side vector B
B = torch.randn(3)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)