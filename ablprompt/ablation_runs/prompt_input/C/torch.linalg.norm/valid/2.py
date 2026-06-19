import torch

# Create a random tensor
A = torch.randn(3, 4)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Compute the L2 norm of each column
column_l2_norms = torch.linalg.norm(A, ord=2, dim=0)

print("Frobenius Norm:", frobenius_norm)
print("L2 Norm of Each Column:", column_l2_norms)