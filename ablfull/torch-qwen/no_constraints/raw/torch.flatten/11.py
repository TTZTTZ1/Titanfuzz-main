import torch

# Generate input data
input_tensor = torch.randn(4, 3, 2)

# Call the API
flattened_tensor = torch.flatten(input_tensor)