import torch

# Prepare input data
tensor = torch.randn(10)
split_size = 5
dim = 0

# Call the API
result = tensor.split(split_size, dim)