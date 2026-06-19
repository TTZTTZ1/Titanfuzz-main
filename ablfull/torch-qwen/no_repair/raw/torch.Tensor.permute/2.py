import torch

# Create a sample tensor
tensor = torch.randn(2, 3, 4)

# Prepare valid input data for permute
dims = (0, 2, 1)

# Call the API
result = tensor.permute(dims)