import torch

# Create a random square matrix A
A = torch.randn(3, 3, dtype=torch.double)

# Create a random right-hand side tensor B
B = torch.randn(3, dtype=torch.double)

# Solve the linear system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)