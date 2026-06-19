import torch

# Prepare valid input data
input_tensor = torch.randn(1, 1, 2, 3)

# Call the API
input_tensor.squeeze_(dim=(0, 1))