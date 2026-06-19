import torch

# Create a random square matrix A and a right-hand side matrix B
A = torch.randn(3, 3)
B = torch.randn(3, 2)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)