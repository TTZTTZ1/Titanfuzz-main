import torch

# Prepare input data
tensor = torch.randn(10)
split_size_or_sections = [3, 4, 3]
dim = 0

# Call the API
result = tensor.split(split_size_or_sections, dim)

print(result)