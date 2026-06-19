import torch

# Create a random tensor
A = torch.randn(3, 4)

# Compute the Frobenius norm of the matrix
norm_fro = torch.linalg.norm(A, ord='fro')

# Compute the spectral norm of the matrix
norm_spectral = torch.linalg.norm(A, ord=2, dim=(0, 1))

print("Frobenius Norm:", norm_fro)
print("Spectral Norm:", norm_spectral)