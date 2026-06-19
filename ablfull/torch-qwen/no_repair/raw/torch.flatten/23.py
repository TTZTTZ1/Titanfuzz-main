import torch

# Prepare input data
input_tensor = torch.randn(3, 4)

# Call the API
flattened_tensor = torch.flatten(input_tensor, start_dim=0, end_dim=-1)