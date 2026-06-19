import torch

# Create two random tensors with compatible shapes for batched matrix multiplication
batch_size = 2
matrix_size = 3
a = torch.randn(batch_size, matrix_size, matrix_size)
b = torch.randn(batch_size, matrix_size, matrix_size)

# Perform batched matrix multiplication using torch.matmul
result = torch.matmul(a, b)

print(result)