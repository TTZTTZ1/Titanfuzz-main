import torch

# Prepare valid input data
input_tensor = torch.tensor([0.5, -0.5, 1.2, -1.7])

# Call the API
result = torch.special.round(input_tensor)

print(result)