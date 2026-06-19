import torch
batch_size = 2
matrix_dim = 3
a = torch.randn(batch_size, matrix_dim, matrix_dim)
b = torch.randn(batch_size, matrix_dim, matrix_dim)
result = torch.bmm(a, b)