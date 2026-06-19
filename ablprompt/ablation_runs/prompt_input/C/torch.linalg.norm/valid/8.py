import torch

# Create a random tensor
A = torch.randn(4, 5)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')

print("Frobenius Norm:", frobenius_norm.item())

# Compute the L2 norm of each column
l2_norm_columns = torch.linalg.norm(A, ord=2, dim=0)

print("L2 Norm of Columns:", l2_norm_columns.tolist())