import torch

# Prepare valid input data
input_tensor = torch.randn(1, 1, 4, 5, 6)
padding = (1, 1, 1, 1, 1, 1)

# Call the API
output_tensor = torch.nn.functional.reflective_pad(input_tensor, padding)