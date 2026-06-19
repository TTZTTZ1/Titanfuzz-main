import torch

# Create a random batch of square matrices
batch_size = 3
n = 4
A = torch.randn(batch_size, n, n, dtype=torch.cdouble)

# Compute the determinant of each matrix in the batch
determinants = torch.linalg.det(A)

print("Determinants:", determinants)