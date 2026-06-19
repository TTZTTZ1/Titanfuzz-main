import torch

# Prepare valid input data
tensor = torch.randn(3, 4)
dims = (1, 0)

# Call the API
result = tensor.permute(dims)