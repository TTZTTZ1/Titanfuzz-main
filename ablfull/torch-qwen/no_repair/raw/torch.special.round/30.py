import torch

# Prepare valid input data
input_tensor = torch.tensor([1.5, -0.4, 3.7])

# Call the API
output_tensor = torch.special.round(input_tensor)

print(output_tensor)