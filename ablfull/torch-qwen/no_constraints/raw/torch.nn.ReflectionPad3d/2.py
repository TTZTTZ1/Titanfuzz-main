import torch

# Prepare valid input data
input_tensor = torch.randn(1, 1, 2, 4, 6)
padding = (1, 1, 1, 1, 1, 1)

# Call the API
output_tensor = torch.nn.functional.pad(input_tensor, padding, mode='reflect')