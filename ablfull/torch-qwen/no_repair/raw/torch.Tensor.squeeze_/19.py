import torch

# Prepare valid input data
tensor = torch.randn(1, 3, 1, 4)

# Call the API
result = tensor.squeeze_(dim=0)