import torch

# Create a random square matrix A
A = torch.randn(3, 3)

# Create a random right-hand side tensor B
B = torch.randn(3, 1)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)