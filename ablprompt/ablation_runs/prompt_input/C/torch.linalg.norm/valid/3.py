import torch

# Create a random tensor
A = torch.randn(5, 5)

# Compute the Frobenius norm of the tensor
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Compute the nuclear norm of the tensor
nuclear_norm = torch.linalg.norm(A, ord='nuc')

# Compute the L2 norm along dimension 0
l2_norm_dim0 = torch.linalg.norm(A, ord=2, dim=0)

# Keep the reduced dimension
l2_norm_dim0_keepdim = torch.linalg.norm(A, ord=2, dim=0, keepdim=True)

print("Frobenius Norm:", frobenius_norm)
print("Nuclear Norm:", nuclear_norm)
print("L2 Norm along dim 0:", l2_norm_dim0)
print("L2 Norm along dim 0 with keepdim:", l2_norm_dim0_keepdim)