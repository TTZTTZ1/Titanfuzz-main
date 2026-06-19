import torch

# Create a random tensor
A = torch.randn(4, 5)

# Compute the Frobenius norm of the matrix
frobenius_norm = torch.linalg.norm(A, ord='fro')
print("Frobenius Norm:", frobenius_norm)

# Compute the L2 norm of each column
l2_norm_columns = torch.linalg.norm(A, ord=2, dim=0)
print("L2 Norm of Columns:", l2_norm_columns)

# Compute the L1 norm of each row
l1_norm_rows = torch.linalg.norm(A, ord=1, dim=1)
print("L1 Norm of Rows:", l1_norm_rows)

# Keep dimensions after reduction
keepdim_result = torch.linalg.norm(A, ord=2, dim=1, keepdim=True)
print("L2 Norm of Rows with keepdim:", keepdim_result)