import torch

# Create a random tensor
A = torch.randn(3, 4, dtype=torch.float64)

# Compute the Frobenius norm of the matrix
norm_fro = torch.linalg.norm(A, ord='fro')

# Compute the nuclear norm of the matrix
norm_nuc = torch.linalg.norm(A, ord='nuc')

# Compute the L2 norm of each column
norm_col = torch.linalg.norm(A, ord=2, dim=0)

# Compute the L1 norm of each row
norm_row = torch.linalg.norm(A, ord=1, dim=1)

print("Frobenius Norm:", norm_fro)
print("Nuclear Norm:", norm_nuc)
print("Column-wise L2 Norms:", norm_col)
print("Row-wise L1 Norms:", norm_row)