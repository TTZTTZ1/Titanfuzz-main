import torch
batch_size = 10
matrix_dim = 5
a = torch.randn(batch_size, matrix_dim, matrix_dim)
b = torch.randn(batch_size, matrix_dim, matrix_dim)
result = torch.bmm(a, b)
print(result)