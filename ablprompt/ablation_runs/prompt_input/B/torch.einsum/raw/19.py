import torch

# Example of using torch.einsum for batch matrix multiplication
batch_size = 5
matrix_size = 4

# Create two batches of matrices
a = torch.randn(batch_size, matrix_size, matrix_size)
b = torch.randn(batch_size, matrix_size, matrix_size)

# Perform batch matrix multiplication using einsum
result = torch.einsum('bij,bjk->blk', a, b)

print(result)