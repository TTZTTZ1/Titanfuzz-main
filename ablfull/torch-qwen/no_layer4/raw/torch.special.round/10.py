import torch

# Prepare input data
input_data = torch.tensor([1.5, -0.7, 2.3, -1.8], dtype=torch.float)

# Call the API
result = torch.special.round(input_data)