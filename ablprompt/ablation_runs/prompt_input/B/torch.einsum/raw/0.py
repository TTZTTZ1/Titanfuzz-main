import torch

# Example: Batch matrix multiplication and addition
batch_size = 5
matrix_dim = 4

# Create random tensors
a = torch.randn(batch_size, matrix_dim, matrix_dim)
b = torch.randn(batch_size, matrix_dim, matrix_dim)
c = torch.randn(batch_size, matrix_dim)

# Perform batch matrix multiplication followed by addition
result = torch.einsum('bij,bjk->blk', a, b) + c

print(result)