import torch

# Prepare valid input data
tensor = torch.randn(2, 3, 4)

# Call the API
permuted_tensor = tensor.permute(2, 0, 1)