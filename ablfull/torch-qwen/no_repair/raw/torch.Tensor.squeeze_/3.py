import torch

# Prepare valid input data
input_tensor = torch.randn(1, 1, 3, 4)

# Call the API
result = input_tensor.squeeze_()