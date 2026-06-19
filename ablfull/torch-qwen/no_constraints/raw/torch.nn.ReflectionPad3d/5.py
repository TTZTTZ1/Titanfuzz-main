import torch

# Prepare valid input data
input_tensor = torch.randn(1, 1, 2, 3, 4)
padding = (1, 2, 3, 4, 5, 6)

# Call the API
output_tensor = torch.nn.functional.pad(input_tensor, padding, mode='reflect')