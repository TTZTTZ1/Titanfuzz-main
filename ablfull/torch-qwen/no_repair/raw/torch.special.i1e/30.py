import torch

# Prepare input data
input_data = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)

# Call the API
result = torch.special.i1e(input_data)