import torch

# Example of using torch.einsum for a batch matrix multiplication and summing over an axis
batch_size = 4
matrix_size = 3
a = torch.randn(batch_size, matrix_size, matrix_size)
b = torch.randn(batch_size, matrix_size, matrix_size)

result = torch.einsum('bij,bjk->blk', a, b)
print(result)