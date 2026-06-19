import torch

# Prepare valid input data
data = torch.randn(2, 3, 4)
dims = (0, 2, 1)

# Call the API
result = data.permute(dims)