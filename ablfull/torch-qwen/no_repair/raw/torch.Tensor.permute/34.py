import torch

# Prepare input data
tensor = torch.randn(2, 3, 4)
dims = (0, 2, 1)

# Call the API
result = tensor.permute(dims)