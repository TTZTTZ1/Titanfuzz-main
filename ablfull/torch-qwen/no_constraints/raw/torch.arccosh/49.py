import torch

# Prepare input data
x = torch.tensor([2.0], dtype=torch.float32)

# Call the API
result = torch.arccosh(x)