import torch

# Prepare input data
input_tensor = torch.tensor([1.5, -2.3, 4.7], dtype=torch.float)

# Call the API
output_tensor = torch.special.round(input_tensor)