import torch

# Prepare input data
tensor = torch.randn(10, 5)  # A 10x5 tensor
split_size = 2  # Scalar value for split_size
dim = 0  # Integer for dim

# Call the API
result = tensor.split(split_size, dim)