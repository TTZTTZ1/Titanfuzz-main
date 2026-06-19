import torch

# Create a random tensor
A = torch.randn(3, 4)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')

print(f"Frobenius Norm: {frobenius_norm}")