import torch

# Example: Batch matrix multiplication
batch_size = 5
matrix_dim = 4
a = torch.randn(batch_size, matrix_dim, matrix_dim)
b = torch.randn(batch_size, matrix_dim, matrix_dim)

result = torch.einsum('bij,bjk->blk', a, b)
print(result)