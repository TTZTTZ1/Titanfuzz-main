import torch

# Prepare input data
tensor = torch.randn(10, 5)
split_size_or_sections = [4, 6]
dim = 0

# Call the API
result = tensor.split(split_size_or_sections, dim)