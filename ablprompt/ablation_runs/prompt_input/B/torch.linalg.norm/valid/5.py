import torch

# Create a random tensor
A = torch.randn(3, 4)

# Compute the Frobenius norm of the matrix
norm_value = torch.linalg.norm(A, ord='fro')

print("Frobenius norm:", norm_value)