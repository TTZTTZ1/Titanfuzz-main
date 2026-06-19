import torch

# Generate input data
input_tensor = torch.randn(2, 3, 4)

# Call the API
result = torch.flatten(input_tensor, start_dim=1, end_dim=-1)