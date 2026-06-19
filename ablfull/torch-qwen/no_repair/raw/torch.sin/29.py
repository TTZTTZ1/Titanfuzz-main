import torch

# Prepare valid input data
input_data = torch.tensor([0.5, -0.5, 1.0], dtype=torch.float)

# Call the API
output = torch.sin(input_data)