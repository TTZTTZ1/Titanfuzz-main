import torch

# Create two random matrices for batch matrix multiplication
batch_size = 10
matrix_dim = 5
matrix_a = torch.randn(batch_size, matrix_dim, matrix_dim)
matrix_b = torch.randn(batch_size, matrix_dim, matrix_dim)

# Perform batch matrix multiplication using torch.bmm
result = torch.bmm(matrix_a, matrix_b)

print(result)