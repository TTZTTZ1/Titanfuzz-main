import torch

# Create a random 3x3 matrix with float64 dtype
A = torch.randn(3, 3, dtype=torch.float64)

# Compute the determinant of the matrix
determinant = torch.linalg.det(A)

print("Determinant:", determinant)