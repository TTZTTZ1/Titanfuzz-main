import torch

# Create a random tensor
A = torch.randn(5, 5, dtype=torch.float64)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')

# Compute the nuclear norm of the matrix
nuclear_norm = torch.linalg.norm(A, ord='nuc')

# Compute the L1 norm of each column
l1_norm_columns = torch.linalg.norm(A, ord=1, dim=0)

# Compute the L2 norm of each row
l2_norm_rows = torch.linalg.norm(A, ord=2, dim=1)

print(f"Frobenius Norm: {frobenius_norm}")
print(f"Nuclear Norm: {nuclear_norm}")
print(f"L1 Norm of Columns: {l1_norm_columns}")
print(f"L2 Norm of Rows: {l2_norm_rows}")