import torch

# Task 2: Generate input data
input_tensor = torch.randn(4, 5)
split_size_or_sections = [2, 2]
dim = 0

# Task 3: Call the API
result = input_tensor.split(split_size_or_sections, dim)