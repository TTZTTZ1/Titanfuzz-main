import torch

# Prepare valid input data
tensor = torch.randn(2, 3)
dims = (1, 0)

# Call the target API
result = tensor.permute(dims)