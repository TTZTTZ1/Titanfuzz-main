import torch

# Create a random tensor
A = torch.randn(3, 4, dtype=torch.float64)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Compute the L2 norm of each row
row_l2_norms = torch.linalg.norm(A, ord=2, dim=1)

# Compute the L1 norm of each column
col_l1_norms = torch.linalg.norm(A, ord=1, dim=0)

print("Frobenius Norm:", frobenius_norm)
print("Row L2 Norms:", row_l2_norms)
print("Column L1 Norms:", col_l1_norms)