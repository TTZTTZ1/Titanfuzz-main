import torch

# Create a random square matrix A
A = torch.randn(3, 3, dtype=torch.float64)

# Create a random right-hand side matrix B
B = torch.randn(3, 2, dtype=torch.float64)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)