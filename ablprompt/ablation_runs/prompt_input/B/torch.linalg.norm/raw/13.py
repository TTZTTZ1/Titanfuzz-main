import torch

# Create a random tensor
A = torch.randn(3, 4, dtype=torch.float64)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Compute the L2 norm along dimension 1
l2_norm_dim1 = torch.linalg.norm(A, ord=2, dim=1, keepdim=True)

print("Frobenius Norm:", frobenius_norm)
print("L2 Norm along dim 1:", l2_norm_dim1)