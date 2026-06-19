import torch

# Generate input data
input_tensor = torch.tensor([0.5, 1.0], dtype=torch.float)

# Call the API
result = torch.special.i1e(input_tensor)