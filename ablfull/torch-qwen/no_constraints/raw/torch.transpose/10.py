import torch

# Prepare valid input data
input_tensor = torch.randn(4, 5)

# Call the API
transposed_tensor = torch.transpose(input_tensor, 0, 1)