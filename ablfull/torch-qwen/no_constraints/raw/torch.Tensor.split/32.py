import torch

# Task 2: Generate input data
tensor = torch.randn(5, 5)
split_size = 2
dim = 0

# Task 3: Call the API
result = tensor.split(split_size, dim)