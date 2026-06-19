import torch

# Create a random square coefficient matrix A
A = torch.randn(3, 3, dtype=torch.double)

# Create a right-hand side tensor B
B = torch.randn(3, dtype=torch.double)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)