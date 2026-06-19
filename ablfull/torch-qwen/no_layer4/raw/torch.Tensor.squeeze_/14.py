import torch

# Prepare valid input data
input_tensor = torch.randn(1, 1, 5)

# Call the API
input_tensor.squeeze_()