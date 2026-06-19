import torch

# Prepare valid input data
tensor = torch.randn(1, 1, 2, 2)

# Call the API
result = tensor.squeeze_(dim=0)