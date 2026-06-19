import torch

# Create a random tensor
A = torch.randn(3, 4)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Compute the L2 norm of each row
row_l2_norms = torch.linalg.norm(A, ord=2, dim=1, keepdim=True)

print("Frobenius Norm:", frobenius_norm)
print("Row L2 Norms:", row_l2_norms)