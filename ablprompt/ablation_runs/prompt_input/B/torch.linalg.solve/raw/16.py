import torch

# Create a random symmetric positive definite matrix A
A = torch.randn(3, 3)
A = A @ A.T + 0.5 * torch.eye(3)

# Create a random right-hand side vector B
B = torch.randn(3)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)