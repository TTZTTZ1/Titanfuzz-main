import torch

# Create a random tensor
A = torch.randn(3, 4)

# Compute the Frobenius norm of the matrix
norm_fro = torch.linalg.norm(A, ord='fro')

# Compute the L2 norm of each row
norm_row = torch.linalg.norm(A, ord=2, dim=1, keepdim=True)

print("Frobenius norm:", norm_fro)
print("L2 norm of each row:", norm_row)