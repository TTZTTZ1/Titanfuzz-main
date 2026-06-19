import torch

# Create a random tensor
A = torch.randn(3, 4)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')
print("Frobenius Norm:", frobenius_norm)

# Compute the L2 norm of each row
row_l2_norms = torch.linalg.norm(A, ord=2, dim=1)
print("Row L2 Norms:", row_l2_norms)

# Compute the L1 norm of each column
col_l1_norms = torch.linalg.norm(A, ord=1, dim=0)
print("Column L1 Norms:", col_l1_norms)