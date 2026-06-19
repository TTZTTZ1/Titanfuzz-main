import torch

# Prepare input data
input_tensor = torch.randn(1, 3, 4, 5, 6)
padding = (1, 2, 3, 4, 5, 6)

# Call the API
output_tensor = torch.nn.functional.pad(input_tensor, padding, mode='reflect')