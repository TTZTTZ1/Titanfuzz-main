import torch

# Create a random tensor
A = torch.randn(3, 4)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Compute the spectral norm of the matrix
spectral_norm = torch.linalg.norm(A, ord=2, dim=(0, 1))

print("Frobenius Norm:", frobenius_norm)
print("Spectral Norm:", spectral_norm)