import torch

# Create a random complex tensor
A = torch.randn(3, 3, dtype=torch.cfloat)

# Compute the determinant
det_A = torch.linalg.det(A)

print("Determinant:", det_A)