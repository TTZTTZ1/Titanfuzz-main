import torch

# Task 2: Generate input data
tensor = torch.randn(10, 5)
split_size = 2

# Task 3: Call the API
result = tensor.split(split_size, dim=0)

print(result)