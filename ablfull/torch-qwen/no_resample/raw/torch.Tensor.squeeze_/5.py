import torch

# Prepare valid input data
input_tensor = torch.randn(1, 3, 1, 4)

# Call the API
result = input_tensor.squeeze_(dim=0)