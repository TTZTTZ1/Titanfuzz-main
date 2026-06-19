import torch

# Create a random tensor
A = torch.randn(3, 4, dtype=torch.float32)

# Compute the Frobenius norm of the matrix
norm_fro = torch.linalg.norm(A, ord='fro')

# Compute the nuclear norm of the matrix
norm_nuc = torch.linalg.norm(A, ord='nuc')

# Compute the L2 norm along dimension 1
norm_l2_dim1 = torch.linalg.norm(A, ord=2, dim=1)

print("Frobenius Norm:", norm_fro)
print("Nuclear Norm:", norm_nuc)
print("L2 Norm along dim 1:", norm_l2_dim1)