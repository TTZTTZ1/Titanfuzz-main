import torch

# Create a random tensor
A = torch.randn(3, 4, dtype=torch.float64)

# Compute the Frobenius norm of the matrix
norm_fro = torch.linalg.norm(A, ord='fro')

# Compute the spectral norm of the matrix
norm_spectral = torch.linalg.norm(A, ord=2)

# Compute the nuclear norm of the matrix
norm_nuclear = torch.linalg.norm(A, ord='nuc')

print(f"Frobenius Norm: {norm_fro}")
print(f"Spectral Norm: {norm_spectral}")
print(f"Nuclear Norm: {norm_nuclear}")