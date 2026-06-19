import torch

# Task 2: Generate input data
batch_size = 10
matrix_dim = 5
a = torch.randn(batch_size, matrix_dim, matrix_dim)
b = torch.randn(batch_size, matrix_dim, matrix_dim)

# Task 3: Call the API torch.bmm
result = torch.bmm(a, b)
print(result)