import torch

# Generate input data
input_data = torch.tensor([2.0], dtype=torch.float32)

# Call the API
result = torch.arccosh(input_data)