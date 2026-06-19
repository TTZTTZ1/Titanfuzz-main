import torch

# Prepare valid input data
input_tensor = torch.tensor([-float('inf'), 0., float('inf')])

# Call the API
result = torch.isneginf(input_tensor)

print(result)