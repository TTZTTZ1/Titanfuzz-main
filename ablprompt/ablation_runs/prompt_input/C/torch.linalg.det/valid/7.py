import torch

# Create a random 3x3 matrix
A = torch.randn(3, 3)

# Compute the determinant of the matrix
determinant = torch.linalg.det(A)

print("The determinant of the matrix is:", determinant)