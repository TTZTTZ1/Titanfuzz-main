import torch

# Create a random tensor
A = torch.randn(4, 5)

# Compute the Frobenius norm of the tensor
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Print the result
print("Frobenius Norm:", frobenius_norm)