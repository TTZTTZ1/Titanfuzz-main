import torch

# Create a random 3x3 matrix with complex numbers
A = torch.randn(3, 3, dtype=torch.cfloat)

# Compute the determinant of the matrix
det_A = torch.linalg.det(A)

print("Determinant of A:", det_A)