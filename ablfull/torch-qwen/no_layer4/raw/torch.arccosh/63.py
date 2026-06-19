import torch

# Prepare valid input data
input_tensor = torch.tensor([2.0, 3.0], dtype=torch.float)

# Call the API
result = torch.arccosh(input_tensor)