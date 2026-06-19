import torch

# Create a random tensor
A = torch.randn(3, 4, dtype=torch.float32)

# Compute the Frobenius norm of the tensor
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Print the result
print(f"Frobenius Norm: {frobenius_norm}")