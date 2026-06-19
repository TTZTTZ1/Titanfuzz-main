import torch

# Task 2: Generate input data
tensor = torch.randn(6, 4)
split_sizes = [2, 2, 2]

# Task 3: Call the API
result = tensor.split(split_sizes)

print(result)