import torch

# Generate input data
x = torch.tensor([0.5], dtype=torch.float32)

# Call the API
result = torch.special.i1e(x)