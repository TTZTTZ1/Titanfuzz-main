import torch

# Prepare valid input data
input_data = torch.tensor([2.0, 3.5], dtype=torch.float)

# Call the API
output = torch.arccosh(input_data)