import torch

# Task 2: Generate input data
tensor = torch.randn(4, 4)
split_size_or_sections = [2, 2]
dim = 0

# Task 3: Call the API
result = tensor.split(split_size_or_sections, dim)