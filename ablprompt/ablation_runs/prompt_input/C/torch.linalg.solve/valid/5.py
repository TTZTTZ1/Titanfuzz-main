import torch

# Create a random square matrix A and a right-hand side matrix B
n = 5
A = torch.randn(n, n)
B = torch.randn(n, 3)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)