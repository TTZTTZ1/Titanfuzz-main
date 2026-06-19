import torch

# Prepare input data
input_tensor = torch.randn(1, 3, 4, 4, 4)
padding = (1, 1, 1, 1, 1, 1)

# Call the API
output_tensor = torch.nn.functional.pad(input_tensor, padding, mode='reflect')