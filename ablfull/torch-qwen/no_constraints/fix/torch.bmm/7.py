import torch
batch_size = 2
matrix_dim = 3
input_tensor = torch.randn(batch_size, matrix_dim, matrix_dim)
result = torch.bmm(input_tensor, input_tensor)
print(result)