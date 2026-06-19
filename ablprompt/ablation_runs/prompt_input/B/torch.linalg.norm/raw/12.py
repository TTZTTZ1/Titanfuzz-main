import torch

# Create a random tensor
A = torch.randn(3, 4, dtype=torch.float64)

# Compute the Frobenius norm of the tensor
norm_value = torch.linalg.norm(A, ord='fro')

print(f"Frobenius norm: {norm_value}")