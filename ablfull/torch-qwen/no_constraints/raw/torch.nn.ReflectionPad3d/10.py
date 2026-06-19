import torch

# Prepare valid input data
padding = (1, 2, 3, 4, 5, 6)
input_tensor = torch.randn(1, 3, 10, 10, 10)

# Call the API
output_tensor = torch.nn.functional.pad(input_tensor, padding, mode='reflect')