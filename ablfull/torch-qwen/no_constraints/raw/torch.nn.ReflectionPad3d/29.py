import torch

# Generate input data
input_tensor = torch.randn(1, 1, 2, 2, 2)
padding = (1, 1, 1, 1, 1, 1)

# Call the API
output_tensor = torch.nn.functional.reflective_pad(input_tensor, padding)