import torch

# Create a tensor
tensor = torch.randn(2, 3, 4)

# Prepare valid input data
dims = (1, 0, 2)

# Call the API
permuted_tensor = tensor.permute(dims)