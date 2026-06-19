import torch

# Task 2: Generate input data
batch_size = 2
matrix_dim = 3
input_tensor = torch.randn(batch_size, matrix_dim, matrix_dim)

# Task 3: Call the API torch.bmm
result = torch.bmm(input_tensor, input_tensor)
print(result)