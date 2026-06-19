import torch

# Prepare input data
input_tensor = torch.tensor([0.5], dtype=torch.float)

# Call the API
result = torch.special.i1e(input=input_tensor)