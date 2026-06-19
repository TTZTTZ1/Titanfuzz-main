import torch

# Create a random 3x3 matrix
A = torch.randn(3, 3)

# Compute the determinant
determinant = torch.linalg.det(A)

print("Determinant:", determinant)