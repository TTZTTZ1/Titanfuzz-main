import torch

# Task 2: Generate input data
tensor = torch.randn(6)
split_size_or_sections = [2, 2, 2]

# Task 3: Call the API
result = tensor.split(split_size_or_sections)

print(result)