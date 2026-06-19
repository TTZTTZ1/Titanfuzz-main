import torch

# Prepare valid input data
input_data = torch.tensor([0.5, -0.5, 2.7, -2.7], dtype=torch.float)

# Call the API
output = torch.special.round(input_data)

print(output)