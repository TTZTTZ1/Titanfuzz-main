import torch

# Create a random complex matrix
A = torch.randn(3, 3, dtype=torch.cfloat)

# Compute the determinant
det_A = torch.linalg.det(A)

print("Determinant of A:", det_A)