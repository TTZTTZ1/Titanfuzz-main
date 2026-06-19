import torch

# Generate valid input data
input_tensor = torch.tensor([2.0, 3.0, 4.5], dtype=torch.float)

# Call the API
result = torch.arccosh(input_tensor)