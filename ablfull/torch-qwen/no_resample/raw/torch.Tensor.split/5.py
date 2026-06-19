import torch

# Task 2: Generate input data
tensor = torch.randn(10)
split_size_or_sections = [2, 3, 5]

# Task 3: Call the API
result = tensor.split(split_size_or_sections)

print(result)