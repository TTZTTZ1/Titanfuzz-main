import torch

# Prepare valid input data
input_tensor = torch.randn(3, 4, 5)

# Call the API
flattened_tensor = torch.flatten(input_tensor, start_dim=1, end_dim=-1)