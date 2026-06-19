import torch

# Task 2: Generate input data
tensor = torch.randn(10)
split_size = 5

# Task 3: Call the API
result = tensor.split(split_size)

print(result)