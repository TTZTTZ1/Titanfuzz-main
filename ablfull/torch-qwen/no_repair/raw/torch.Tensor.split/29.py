import torch

# Prepare input data
tensor = torch.randn(4, 5)
split_size_or_sections = [2, 2]
dim = 0

# Call the API
result = tensor.split(split_size_or_sections, dim)