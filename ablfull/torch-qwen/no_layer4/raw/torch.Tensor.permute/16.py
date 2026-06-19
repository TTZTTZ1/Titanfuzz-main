import torch

# Prepare input data
tensor = torch.randn(2, 3)
dims = (1, 0)

# Call the API
result = tensor.permute(dims)